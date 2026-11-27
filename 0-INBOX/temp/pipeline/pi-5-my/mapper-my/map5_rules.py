"""Shared rules of the pi-5 Pāli→Burmese keyword mapping (Kathāvatthu «အငြင်းပွားရာ အကြောင်းအရာများကို ဆွေးနွေးခြင်း»).

Settled on phase 1 (preamble + 1-puggalakatha, map_ch1.py); imported by the phase-2 scripts (ch2-15, ch16-31) and the
phase-3 consistency scan. NOTHING RUNS ON IMPORT: every file is read lazily (functools.lru_cache) the first time a
function needs it; the module only defines constants, tables and functions.

Contents
  paths and loaders          segments(), keyword_rows(), prior(), terms()
  presence verifier          chunk_present(), presence()     (a copy of the pi-4 check, pi-4-my/mapper-my/
                                                             presence_check.py, plus the endings marked «pi-5»)
  frame / stock tables       FRAME (dialectic machinery, speakers, sets, headings), STOCK (core terms of the book that
                             recur in every kathā), NUM_MY (counts)
  context functions          FUNCS[name](kw, pali, my) -> value; a table value «@name» calls one
  lookup engine              Mapper(tables, ctx).lookup(ch, sid, kw, pali, my) — CTX[sid] -> chapter tables -> FRAME /
                             STOCK -> pi-5 terms (my5-zeroshot-terms.md) -> a pi-1 … pi-4 value the text has as a phrase
                             -> compose rules -> a pi-1 … pi-4 value present by an ending rule
  verifier                   verify_file(ch, mapped_dir)

Phase 3 (2026-11-21, coordinator decisions on phase 2): the module overrides of the two phase-2 groups that hold
beyond one segment are here (STOCK «phase 3» block, FUNCS «phase 3» block); the three mechanics are fixed (negate():
a gapped negative «S … မV» is checked part by part; glue(): a verb is not glued through a verbal noun «…ခြင်း»; phrase_present(): the perfect predicate «Xပြီး ဖြစ်» stands for «Xပြီးသော» as in presence()); the book-wide
rules of phase 2 run in the Mapper for every chapter: S1 stem fallback (stem_fn), S3 / G3 negatives inside a multiword
keyword (negate), G1 / G2 the Pāli order of two composed members (pali_order). Single-segment forms stay as CTX rules
in the chapter scripts.

Usage in a chapter script (see map_ch1.py):
    import map5_rules as R
    M = R.Mapper(chapter_tables={"2-parihanikatha": T_CH2}, ctx=CTX)
    lines, problems = M.map_chapter("2-parihanikatha")
"""
import re
import pathlib
import collections
import functools

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
MY = ROOT / "AI_translation/burmese/pi-5-burmese-plain-zeroshot_split_chapters"
PI = ROOT / "AI_translation/pali/pi-5_split_chapters"
MAPS = {t: ROOT / f"AI_translation/burmese/{t}-keywords-by-reference-pali-burmese-plain.md"
        for t in ("pi-1", "pi-2", "pi-3", "pi-4")}
TERMS_FILE = HERE.parent / "my5-zeroshot-terms.md"
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")
LINE = re.compile(r"^\[([^\]]+)\] (.*)$")
NONE = "(no direct equivalent)"
PUG = "ပုဂ္ဂိုလ်"
# pi-2 first where pi-1 and pi-2 differ (brief), then pi-3, pi-4 (the order of the pi-4 mapper, pi-4 added), then pi-1
PRIOR_ORDER = ("pi-2", "pi-3", "pi-4", "pi-1")

CHAPTERS = ["preamble", "1-puggalakatha", "2-parihanikatha", "3-brahmacariyakatha", "4-jahatikatha",
            "5-sabbamatthitikatha", "6-atitakkhandhadikatha", "7-ekaccam-atthitikatha", "8-satipatthanakatha",
            "9-hevatthikatha", "10-dutiyavaggo", "11-tatiyavaggo", "12-catutthavaggo", "13-pancamavaggo",
            "14-chatthavaggo", "15-sattamavaggo", "16-atthamavaggo", "17-navamavaggo", "18-dasamavaggo",
            "19-ekadasamavaggo", "20-dvadasamavaggo", "21-terasamavaggo", "22-cuddasamavaggo",
            "23-pannarasamavaggo", "24-solasamavaggo", "25-sattarasamavaggo", "26-attharasamavaggo",
            "27-ekunavisatimavaggo", "28-visatimavaggo", "29-ekavisatimavaggo", "30-bavisatimavaggo",
            "31-tevisatimavaggo"]


def low(w):
    return w[:1].lower() + w[1:]


def strip_brackets(pali):
    """the Pāli without its variant / editorial brackets «[…]»."""
    return re.sub(r"\s*\[[^\]]*\]", "", pali)


# =====================================================================================================================
# loaders (lazy)
# =====================================================================================================================
@functools.lru_cache(maxsize=None)
def segments(path):
    """{block id: the segment's text, its lines joined by one space, the ^id removed}."""
    out, buf = {}, []
    for l in pathlib.Path(path).read_text(encoding="utf-8-sig").splitlines():
        if not l.strip():
            continue
        buf.append(l)
        m = ID.search(l)
        if m:
            out[m.group(1)] = re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", " ".join(buf))
            buf = []
    return out


def burmese(ch):
    return segments(str(MY / f"{ch}.md"))


def pali(ch):
    return segments(str(PI / f"{ch}.md"))


@functools.lru_cache(maxsize=None)
def keyword_rows(ch):
    """[(sid, [kw, …])] of mapper-my/<ch>.keywords.md, in file order."""
    rows = []
    for l in (HERE / f"{ch}.keywords.md").read_text(encoding="utf-8").splitlines():
        m = LINE.match(l)
        if m:
            rows.append((m.group(1), [k.strip() for k in m.group(2).split(", ")]))
    return rows


@functools.lru_cache(maxsize=None)
def prior():
    """{tag: {low(kw): Counter(value)}} of the final pi-1 … pi-4 Burmese mappings."""
    out = {}
    for t, p in MAPS.items():
        d = collections.defaultdict(collections.Counter)
        for l in p.read_text(encoding="utf-8").splitlines():
            m = LINE.match(l)
            if not m:
                continue
            for kv in m.group(2).split(", "):
                if "=" in kv:
                    k, v = kv.split("=", 1)
                    d[low(k)][v] += 1
        out[t] = d
    return out


def prev_vals(kw, tag=None):
    c = collections.Counter()
    for t in ([tag] if tag else PRIOR_ORDER):
        c.update(prior()[t].get(low(kw), {}))
    return c


@functools.lru_cache(maxsize=None)
def terms():
    """my5-zeroshot-terms.md lines «- Pāli = Burmese» -> {low(pāli): burmese}: single forms only (no «/» pairs, no
    «၊» lists, no frames with P / Q / X, at most four Pāli words); the notes «(…)» on the Pāli side go."""
    t = {}
    for l in TERMS_FILE.read_text(encoding="utf-8").splitlines():
        if not l.startswith("- ") or " = " not in l:
            continue
        p, b = l[2:].split(" = ", 1)
        p = re.sub(r"\s*\([^)]*\)", "", p).strip().rstrip(".?!").strip()
        b = re.sub(r"\s*\((?=[^)]*[A-Za-z])[^()]*\)\s*$", "", b.strip()).rstrip("။").strip()
        if not p or not b or " / " in p or " / " in b or "၊" in b or "…" in p or "…" in b:
            continue
        if re.search(r"\b[PQX]\b", p) or len(p.split()) > 4 or "⟦" in b:
            continue
        t.setdefault(low(p), b)
    return t


# =====================================================================================================================
# presence verifier (copy of the pi-4 check, endings unchanged, plus the pi-5 endings)
# =====================================================================================================================
ATTR_FROM = tuple(dict.fromkeys((
    "သော်", "၍", "ပြီး", "သည်", "ခြင်း", "သူ", "ပြီ", "ကြသော", "ဘဲ", "သေးသော", "၊", "သည့်",   # pi-1 / pi-2 N11
    "လျက်", "ကုန်သော", "ကြသည်", "၏", "ကြ၏", "။", "”",                                    # pi-2 12-14 M1
    "ကြ", "ဟူ", "ဟု",                                                                   # pi-2 15-16 P1
    "ကုန်",                                                                             # pi-2 17
    "သနည်း", "ရာ", "သေးသည်",                                                          # pi-3 M7
    "လည်း", "ကား", "သေး", "လျှင်", "စဉ်", "လိမ့်မည်", "သကဲ့သို့", "သဖြင့်",              # pi-4 P3
    "သလော",                                                                             # pi-5 Q1
)))
VERB_FROM = tuple(dict.fromkeys((
    "ပါ၏", "၏", "ပြီ", "သော", "၍", "ပြီး", "ခြင်း", "ရန်", "သည့်", "ကြ", "၊", "ဟူ", "လိမ့်မည်", "။",  # pi-1
    "ရာ", "”", "သနည်း",                                                                  # pi-2 12-14 M1
    "လျှင်",                                                                            # pi-2 15-16 P5 / P6
    "ပါစေ", "သမျှ", "ဟု", "ကုန်", "အံ့", "လော့", "မည်",                                     # pi-2 17
    "လည်း", "ကား", "သူ", "ဘဲ", "ကာ", "သတတ်", "သကဲ့သို့",                                  # pi-4 P3
    "သလော", "ပါ", "…",                                                                  # pi-5 Q1
)))


ABS_FROM = ("ပြီးမှ", "ပြီးလျှင်", "ပြီး", "လျက်")                                     # pi-5 Q1


def chunk_present(c, text):
    if c in text:
        return "exact"
    if c.endswith("သော") and len(c) > 3:
        st = c[:-3]
        if any(st + e in text for e in ATTR_FROM):
            return "attr"
    if c.endswith("သည်") and len(c) > 3:
        st = c[:-3]
        if any(st + e in text for e in VERB_FROM):
            return "verb"
    if c.endswith("ည့်") and c[:-3] + "ည်" in text:
        return "attr-fut"
    if c.endswith("ပြီးသော") and c[:-3] + " ဖြစ်" in text:
        return "perf-pred"
    if c.endswith("သည်") and len(c) > 3:
        st = c[:-3]
        if "မ" + st in text:
            return "neg-verb"
        for i in range(0, len(st)):
            if any(st[:i] + "မ" + st[i:] + e in text for e in VERB_FROM):
                return "neg-verb"
    if c.endswith("၍") and len(c) > 1 and ("မ" + c[:-1] + "ဘဲ" in text or "မ" + c[:-1] + "ခဲ့ဘဲ" in text):
        return "neg-abs"       # pi-4 A2 (pi-5: also the past «မXခဲ့ဘဲ»)
    if c.endswith("၍") and len(c) > 1 and any(c[:-1] + e in text for e in ABS_FROM):
        return "abs"           # pi-5 Q1: an absolutive «X၍» against the text's «Xပြီးမှ / Xပြီးလျှင် / Xပြီး / Xလျက်»
    if c.endswith("သူ") and len(c) > 2 and c[:-2] + "သော ပုဂ္ဂိုလ်" in text:
        return "name-attr"
    for t in ("လိမ့်မည်", "ခဲ့သည်"):
        if c.endswith(t) and c[:-len(t)] + "ကြ" + t.replace("ခဲ့သည်", "ခဲ့") in text.replace("ခဲ့ကြ", "ကြခဲ့"):
            return "plural"
    for i in range(1, len(c)):
        if c[:i] + "မ" + c[i:] in text or c[:i] + " မ" + c[i:] in text:
            return "neg-infix"
    if c.endswith("သော") and len(c) > 3:
        st = c[:-3]
        for i in range(0, len(st)):
            if any((st[:i] + "မ" + st[i:]) + e in text for e in ATTR_FROM):
                return "neg-attr"
    return None


def presence(v, text):
    """-> (ok, [(chunk, rule) for every chunk not found literally])"""
    if v == NONE:
        return True, []
    bare = re.sub("[“”‘’]", "", text)
    nobr = re.sub(r" ?\[[^\]]*\]", "", text)
    rules = []
    for part in re.split(r" … ", v):
        for c in part.split():
            c = c.strip("“”‘’()")
            if not c:
                continue
            r = chunk_present(c, text) or chunk_present(c, bare) or chunk_present(c, nobr)
            if r is None:
                return False, [(c, None)]
            if r != "exact":
                rules.append((c, r))
    return True, rules


# =====================================================================================================================
# frame and stock tables (settled on 1-puggalakatha; see map-table.md for the reasons)
# =====================================================================================================================
# ---- FRAME-BEGIN
# The dialectic machinery and the stock frame words of the Kathāvatthu (my5-zeroshot-terms §3-§6), settled on
# 1-puggalakatha. Dictionary forms: pi-1 rules 1-11 (nouns without final particles, attributives «…သော», verbs
# «…သည်», absolutives «…၍»), pi-2 N1-N11, pi-3 M1-M9, pi-4 P1-P8; the NEW pi-5 rules Q1-Q8 (map-table.md).
FRAME = {
    # answers and the eight-fold refutation (anuloma / paṭikamma / niggaha / upanayana / niggamana)
    "Āmantā": "ဟုတ်ပါသည်",                       # Q2: the answer formula «ဟုတ်ပါသည်။» whole
    "Ājānāhi": "လက်ခံသည်",                       # «ချေပချက်ကို လက်ခံလော့» (rule 4)
    "niggahaṃ": "@niggaha", "niggaha": "@niggaha", "niggaho": "@niggaha", "niggahe": "@niggaha",
    "paṭikammaṃ": "ပြန်လှန် ချေပချက်", "paṭikamma": "ပြန်လှန် ချေပချက်", "paṭikamme": "ပြန်လှန် ချေပချက်",
    "upanayana": "ဆက်စပ် အသုံးချချက်", "niggamana": "နိဂုံးချုပ်ချက်", "paṭipādanā": "ဆက်စပ် တင်ပြချက်",
    "anuloma": "အစဉ်အတိုင်း", "anulomaṃ": "အစဉ်အတိုင်း", "paccanīka": "ပြောင်းပြန်", "paccanīkaṃ": "ပြောင်းပြန်",
    "Anulomapaccanīkaṃ": "အစဉ်အတိုင်းနှင့် ပြောင်းပြန်", "Paccanīkānulomaṃ": "ပြောင်းပြန်နှင့် အစဉ်အတိုင်း",
    "paṭijānantaṃ": "ဝန်ခံနေသော", "paṭijānantā": "ဝန်ခံနေသော", "paṭiññāya": "ဝန်ခံချက်", "hetāya": "ထို",
    "niggaṇhāma": "ချေပသည်", "niggaṇhāsi": "ချေပသည်",
    "niggahetabbe": "@niggahetabba", "niggahetabbā": "@niggahetabba",
    "Suniggahito": "ကောင်းစွာ ချေပခြင်း ခံရသော", "Dunniggahitā": "မကောင်းစွာ ချေပခြင်း ခံရသော",
    "dunniggahite": "မကောင်းစွာ ချေပခြင်း", "niggahite": "ချေပခြင်း", "dukkaṭe": "မကောင်းစွာ ပြုခဲ့သော",
    "suniggahitova": "@roman", "hevameva": "@hevameva",
    "tava": "သင်", "ṭīkā": "ဋီကာ", "oloketabbā": "ကြည့်သည်",
    "vata": "@vata", "micchā": "@miccha", "Nanu": "မဟုတ်လော", "Tena hi": "@tenahi", "hevaṃ": "ဤသို့",
    # the speakers' note «[iminā lakkhaṇena sakavādī/paravādīpucchā dassitā]»
    "pucchā": "@puccha", "dassitā": "ပြထားသော", "lakkhaṇena": "အမှတ်အသား", "vādī": "@vadi",
    # the proposition of the Puggalakathā (§4, §7)
    "upalabbhati": "တွေ့ရသည်", "upalabbhanti": "တွေ့ရသည်", "nupalabbhati": "မတွေ့ရ", "nupalabbhanti": "မတွေ့ရ",
    "saccikaṭṭhaparamatthena": "အမှန်တကယ် အဆုံးစွန် အနက်",      # rule 1: the instrumental «အားဖြင့်» goes
    "paramatthena": "အဆုံးစွန် အနက်", "atthena": "@atthena", "parama": "@parama",
    "paramattho": "အဆုံးစွန် အရာ", "saccikaṭṭho": "@saccikattho", "saccikaṭṭha": "@saccikattho",
    "aṭṭho": "အရာ", "aṭṭha": "@attha_thing", "suddha": "@suddha", "okāsa": "နေရာ", "avayava": "အစိတ်အပိုင်း",
    "Sabbattha": "နေရာတိုင်း", "Sabbadā": "အချိန်တိုင်း", "Sabbesu": "@sabbesu",
    # sets and ordinals (§5)
    "Pañcamo": "ပဉ္စမ", "Chaṭṭho": "ဆဋ္ဌမ", "Sattamo": "သတ္တမ", "aṭṭhaka": "ရှစ်ပါးအစု",
    "Saṃkhittaṃ": "အကျဉ်းချုပ်",
    # quotations and reasons (§3)
    "bhagavatā": "မြတ်စွာဘုရား", "suttanto": "သုတ္တန်", "Vuttaṃ": "ဟောတော်မူသည်", "vuttaṃ": "ဟောတော်မူသည်",
    "Vuttaṃ bhagavatā": "မြတ်စွာဘုရား … ဟောတော်မူသည်", "bhikkhave": "ရဟန်း", "bhante": "အသျှင်ဘုရား",
    "kāraṇena": "အကြောင်း", "katvā": "@katva", "eva": "@eva",
    # headings and colophons (§2)
    "kathā": "@katha", "anuyogo": "စစ်ဆေးမေးမြန်းခြင်း", "anuyoga": "စစ်ဆေးမေးမြန်းခြင်း", "vaggo": "ဝဂ်",
    "niṭṭhitā": "ပြီးဆုံးသော", "saṃsandanaṃ": "နှိုင်းယှဉ်ခြင်း", "saṃsandanā": "နှိုင်းယှဉ်ခြင်း",
    "suddhika": "ရိုးရိုး", "opamma": "ဥပမာ", "catukka": "လေးပါး", "naya": "@naya", "sodhanaṃ": "စိစစ်ခြင်း",
    # pronouns of the frames
    "koci": "@koci", "Yo": "@yo", "yo": "@yo", "yaṃ": "@yam", "yena": "@yena", "Aññaṃ": "@anna", "aññaṃ": "@anna",
    "añño": "@anna", "Añño": "@anna", "aññā": "@anna_f", "Aññā": "@anna_f", "Aññe": "@anna", "aññe": "@anna",
    "Aññāni": "@anna",
    "hoti": "@hoti", "atthi": "ရှိသည်", "Atthi": "ရှိသည်", "bhavati": "ဖြစ်သည်",
}
# Core terms of the book that recur in every kathā (my5-zeroshot-terms §7-§8), settled on 1-puggalakatha.
STOCK = {
    "puggala": "ပုဂ္ဂိုလ်", "puggalo": "ပုဂ္ဂိုလ်", "Puggalo": "ပုဂ္ဂိုလ်", "puggalassa": "ပုဂ္ဂိုလ်",
    "puggalā": "ပုဂ္ဂိုလ်", "puggalaṃ": "ပုဂ္ဂိုလ်", "puggalānaṃ": "ပုဂ္ဂိုလ်",
    "paññatti": "သတ်မှတ်ချက်", "paññatta": "သတ်မှတ်ချက်", "upādāya": "မှီ၍", "upādā": "@upada", "nissāya": "မှီ၍",
    "sandhāvati": "ကူးသွားသည်", "sandhāvanti": "ကူးသွားသည်", "upapajjati": "ပြန်လည် ဖြစ်ပေါ်သည်",
    "paññāyati": "ထင်ရှားသည်", "cavati": "@cavati", "cuto": "သေသော",
    "kattā": "ပြုလုပ်သူ", "kāretā": "ပြုလုပ်စေသူ", "kattā kāretā": "ပြုလုပ်သူ … ပြုလုပ်စေသူ",
    "paṭisaṃvedī": "ခံစားသော", "vipākapaṭisaṃvedī": "အကျိုးကို ခံစားသော", "kārako": "ပြုသူ",
    "Kammakārako": "ကံကို ပြုသူ", "kammakārako": "ကံကို ပြုသူ",
    "paṭisaṃvedeti": "ခံစားသည်", "paṭisaṃvedenti": "ခံစားသည်", "karoti": "@karoti", "karonti": "@karoti",
    "sukhadukkhaṃ": "ချမ်းသာနှင့် ဆင်းရဲ", "kalyāṇa": "ကောင်းမွန်သော", "pāpakāni": "ယုတ်မာသော",
    "pāpakānaṃ": "ယုတ်မာသော", "Kalyāṇapāpakāni": "ကောင်းမွန်သော … ယုတ်မာသော",
    "Kalyāṇapāpakānaṃ": "ကောင်းမွန်သော … ယုတ်မာသော", "kammāni": "ကံ", "kammānaṃ": "ကံ", "vipāko": "အကျိုး",
    "Vipāko": "အကျိုး",
    "saṅkhato": "ပြုပြင်ဖန်တီးထားသော", "asaṅkhato": "ပြုပြင်ဖန်တီးထားခြင်း မရှိသော",
    "sappaccayo": "အကြောင်း ရှိသော", "appaccayo": "အကြောင်း မရှိသော", "sassato": "@sassato",
    "nimitto": "အမှတ်အသား ရှိသော", "animitto": "အမှတ်အသား မရှိသော",
    "vijjamāno": "ရှိနေသော", "saṃvijjamāno": "ထင်ရှား ရှိနေသော",
    "khayadhammaṃ": "ကုန်ခန်းတတ်သော သဘော … ရှိသော", "vayadhammaṃ": "ပျက်စီးတတ်သော သဘော … ရှိသော",
    "virāgadhammaṃ": "ပြယ်ပျောက်တတ်သော သဘော … ရှိသော", "nirodhadhammaṃ": "ချုပ်ငြိမ်းတတ်သော သဘော … ရှိသော",
    "vipariṇāmadhammaṃ": "ဖောက်ပြန်ပြောင်းလဲတတ်သော သဘော ရှိသော",
    "virāga": "@viraga",
    "sotāpanno": "သောတာပန်", "sakadāgāmī": "သကဒါဂါမ်", "anāgāmī": "အနာဂါမ်", "arahā": "ရဟန္တာ",
    "manusso": "လူ", "devo": "နတ်", "hutvā": "ဖြစ်၍", "jīvaṃ": "အသက်", "jīvo": "အသက်", "sarīraṃ": "ကိုယ်ခန္ဓာ",
    "rūpaṃ": "@rupam", "Rūpaṃ": "@rupam", "rūpa": "@rupa", "dukkhaṃ": "@dukkha", "Dukkhaṃ": "@dukkha",
    "dukkha": "@dukkha", "sukhaṃ": "@sukha", "sukha": "@sukha", "dhātuyā": "@dhatuya",
    "nibbānaṃ": "နိဗ္ဗာန်", "Nibbānaṃ": "နိဗ္ဗာန်", "nibbānassa": "နိဗ္ဗာန်",
    "parinibbānaṃ": "ပရိနိဗ္ဗာန် ပြုခြင်း", "Parinibbuto": "ပရိနိဗ္ဗာန် ပြုပြီးသော",
    "parinibbute": "ပရိနိဗ္ဗာန် ပြုတော်မူပြီးသော",
    "sayaṃ": "မိမိ", "para": "@para", "hitāya": "@hitaya",
    "bhagavā": "မြတ်စွာဘုရား", "saccavādī": "မှန်သော စကားကို ဆိုတော်မူသော", "tathavādī": "ဟုတ်တိုင်း ဆိုတော်မူသော",
    "avitathavādī": "မမှားယွင်းဘဲ ဆိုတော်မူသော", "anaññathavādī": "အခြားတစ်မျိုး မဆိုတော်မူသော",
    "sacca": "@sacca", "tatha": "ဟုတ်တိုင်း", "vitatha": "မှားယွင်း", "aññatha": "အခြားတစ်မျိုး",
    "Khandhesu": "အစုအဝေး", "khandhesu": "အစုအဝေး", "Khandhā": "အစုအဝေး",
    # recurring keywords of the later kathās, added after the frame-coverage check (frame-coverage.md); the words of
    # the pi-5 text (my5_formulas.py harmonise values where named)
    "jahati": "@jahati",                 # F.JAHATI «စွန့်ပယ်» (harmonise B2; kept apart from pajahati «ပယ်»)
    "paṇidhi": "@panidhi",               # F.AVATTANA, the last item «ဆုတောင်းခြင်း» (harmonise B6)
    "uddānaṃ": "အကျဉ်းချုပ်",            # «Tassuddānaṃ» = «ထို၏ အကျဉ်းချုပ်»
    "antarikā": "@antarika", "samodhānaṃ": "ပေါင်းဆုံခြင်း", "vīta": "@vita", "bhāvito": "@bhavito",
    "bhāvitā": "@bhavito", "arahattā": "@arahatta", "arahatta": "@arahatta", "phalā": "@phala", "phala": "@phala",
    "phalaṃ": "@phala", "bojjha": "@bojjha", "aṅgā": "@anga", "gati": "@gati", "taṇhā": "@tanha",
    # phase 3: the module overrides of phase 2 (notes-ch2-15.md, notes-ch16-31.md «Module overrides») that hold beyond
    # one segment; a tuple («a», «b», …) = the first value the segment has as a phrase, then one present by the ending
    # rules, else the pi-1 … pi-4 value (alt)
    "parinibbāyī": "ပရိနိဗ္ဗာန် ပြုသော",                     # Q8 / pi-4 (the pi-5 terms list «…ပြုသူ»)
    "parinibbuto": ("ပရိနိဗ္ဗာန် ပြုပြီးသော", "ပရိနိဗ္ဗာန် ပြုတော်မူခဲ့သော", "ပရိနိဗ္ဗာန် ပြုတော်မူသော"),
    "parinibbute": ("ပရိနိဗ္ဗာန် ပြုတော်မူပြီးသော", "ပရိနိဗ္ဗာန် စံဝင်တော်မူပြီးသော"),
    "thero": ("မထေရ်", "ထေရ်"),
    "sukhadukkhaṃ": ("ချမ်းသာနှင့် ဆင်းရဲ", "ချမ်းသာ ဆင်းရဲ", "သုခ ဒုက္ခ"),
    "nirodhadhammaṃ": ("ချုပ်ငြိမ်းတတ်သော သဘော … ရှိသော", "ချုပ်ငြိမ်းခြင်း သဘော ရှိသော"),
    "aṅga": "@anga", "aṅgo": "@anga", "aṅgaṃ": "@anga", "aṅgānaṃ": "@anga",
    "dhammo": "@dhammo",
    "maggo": "@magga", "maggaṃ": "@magga", "magga": "@magga",
    "rāga": ("ရာဂ", "တပ်မက်မှု"), "rāgo": ("ရာဂ", "တပ်မက်မှု"),
    "samāpatti": ("ဈာန် ဝင်စားခြင်း", "သမာပတ်"),
    "nirodho": ("ချုပ်ငြိမ်းခြင်း", "ချုပ်သော"), "nirodhaṃ": ("ချုပ်ငြိမ်းရာ ဈာန်", "ချုပ်ငြိမ်းခြင်း", "ချုပ်သော"),
    "dhātū": "@dhatu_plane", "dukkhā": "@dukkha", "jano": "@jana", "janassa": "@jana",
    # phase 3 consistency scan (map-harmonise-notes.md §B)
    "atta": "@atta",                                    # ch16-31 FUNCS3 atta, book-wide
    "yoni": ("မွေးဖွားရာ အမျိုးအစား", "မွေးဖွားရာ"),    # not bhava's «ဘဝ» (ch11 / ch14 lists «bhavo … yoni»)
    "dhammapade": "“ဓမ္မပဒ”",                          # rule 1: «“ဓမ္မပဒ”၌» without the final «၌»
}
NUM_MY = {"eka": "တစ်", "ekassa": "တစ်", "dve": "နှစ်", "dvinnaṃ": "နှစ်", "tayo": "သုံး", "tiṇṇaṃ": "သုံး",
          "cattāro": "လေး", "catunnaṃ": "လေး", "pañca": "ငါး", "pañcannaṃ": "ငါး", "aṭṭha": "ရှစ်"}
# ---- FRAME-END


# =====================================================================================================================
# context functions
# =====================================================================================================================
def first_compound(pali, stems):
    """the value of the FIRST stem (by position) found at a word start in the Pāli segment."""
    best = None
    for st, val in stems:
        m = re.search(r"(?<![\wāīūṃṅñṭḍṇḷ])" + st, pali, flags=re.I)
        if m and (best is None or m.start() < best[0]):
            best = (m.start(), val)
    return best[1] if best else None


def by_first(stems, default):
    """one sense per segment (pi-1 harmonise decision 3): the sense of the FIRST of the stems in the Pāli."""
    def f(kw, pali, my):
        v = first_compound(pali, stems)
        return v if v is not None else default
    return f


def by_sub(stems, default):
    """as by_first, but the stem may stand inside a compound."""
    def f(kw, pali, my):
        best = None
        for st, val in stems:
            i = pali.find(st)
            if i >= 0 and (best is None or i < best[0]):
                best = (i, val)
        return best[1] if best else default
    return f


def pref(*vals):
    """the first value the segment's text has (presence check); else the last (one sense per segment, the text's
    own word)."""
    def f(kw, pali, my):
        for v in vals:
            if presence(v, my)[0]:
                return v
        return vals[-1]
    return f


def literal(*vals):
    """the first value whose every « … » part stands literally in the text; else the last."""
    def f(kw, pali, my):
        for v in vals:
            if all(p in my for p in v.split(" … ")):
                return v
        return vals[-1]
    return f


def alt(*vals):
    """phase 3 (the phase-2 tuples, group rule S2): the first value the segment's Burmese has as a phrase, then the
    first present by the ending rules, else the pi-1 … pi-4 value (one sense per segment, the text's own word)."""
    def f(kw, pali, my):
        for v in vals:
            if v == NONE or presence(v, my)[0] and phrase_ok(v, my):
                return v
        for v in vals:
            if presence(v, my)[0]:
                return v
        return "@prior"
    return f


def in_text(pali_word, value):
    """value where the Pāli has the word outside the variant brackets, else (no direct equivalent) (pi-3 M2: a word
    only inside a Roman-script variant has no Burmese)."""
    rx = re.compile(r"(?<![\wāīūṃṅñṭḍṇḷ])" + pali_word + r"(?![\wāīūṃṅñṭḍṇḷ])", re.I)

    def f(kw, pali, my):
        return value if rx.search(strip_brackets(pali)) else NONE
    return f


# ---- FUNCS-BEGIN
_W = r"(?![a-zāīūṃṅñṭḍṇḷ])"           # end of a Pāli word


def has(*words):
    """True when every Burmese string is in the text."""
    return lambda my: all(w in my for w in words)


def first_in_text(*vals):
    """the candidate whose first « … » part stands earliest in the text (one sense per segment: the first)."""
    def f(kw, pali, my):
        pos = [(my.find(v.split(" … ")[0]), i, v) for i, v in enumerate(vals) if v.split(" … ")[0] in my]
        return min(pos)[2] if pos else vals[-1]
    return f


def if_text(word, value, other="@prior"):
    """value where the text has the Burmese word, else other (default: the pi-1 … pi-4 value present)."""
    return lambda kw, pali, my: value if word in my else other


def by_first_checked(stems, fallbacks):
    """by_first, the value checked against the text: when the first stem's sense is not in the segment's Burmese,
    the first fallback that is (one sense per segment, the text's own word)."""
    def f(kw, pali, my):
        v = first_compound(strip_brackets(pali), stems)
        if v is not None and presence(v, my)[0]:
            return v
        for w in fallbacks:
            if w == "@prior" or presence(w, my)[0]:
                return w
        return fallbacks[-1]
    return f


_LONG = {"a": "[aā]", "i": "[iī]", "u": "[uū]"}


def pali_has(kw, pali):
    """the keyword stands in the Pāli outside the variant brackets (also with the sandhi length before «ti»:
    karotīti, puggaloti …)."""
    k = low(kw)
    rx = re.escape(k[:-1]) + _LONG.get(k[-1], re.escape(k[-1])) if k else ""
    return bool(re.search(r"(?<![a-zāīūṃṅñṭḍṇḷ])" + rx + r"(?:n?ti)?" + _W, strip_brackets(pali), flags=re.I))


def f_roman(kw, pali, my):
    """pi-3 M2: a keyword that stands only inside a Roman-script variant bracket has no Burmese."""
    return "@prior" if pali_has(kw, pali) else NONE


def f_miccha(kw, pali, my):
    """micchā: the verdict «…ti micchā» = «မှားသည်» (text «…ဟူသည် မှားသည်»), the verdict «idaṃ te micchā» = «အမှား»
    («… သင်၏ အမှား ဖြစ်သည်»), the compound member (micchādiṭṭhi …) = «မှားယွင်းသော» (pi-1 … pi-4); one sense per
    segment, the first in the Pāli."""
    p = strip_brackets(pali)
    v = first_compound(p, [(r"micchā(?=[a-zāīūṃṅñṭḍṇḷ])", "မှားယွင်းသော"), (r"te micchā" + _W, "အမှား"),
                           (r"micchā" + _W, "မှားသည်")])
    for c in [v, "မှားသည်", "အမှား", "မှားယွင်းသော"]:
        if c and presence(c, my)[0]:
            return c
    return "@prior"


def f_rupa(kw, pali, my):
    """rūpa (compound member), one sense per segment by the first compound (pi-3 / pi-4 f_rupa): the fine-material
    plane «သိမ်မွေ့သော ရုပ်» (rūpāvacara, rūpabhava, rūpadhātuyā as a plane, rūparāga …), the visible object
    «အဆင်းအရောင်» (rūpāyatana, rūpadhātu as an element, rūpasaññā …), matter «ရုပ်» (rūpakkhandha …); checked
    against the text."""
    p = strip_brackets(pali)
    stems = [("rūpāvacar", "သိမ်မွေ့သော ရုပ်"), ("rūpabhav", "သိမ်မွေ့သော ရုပ်"), ("rūpasahagat", "သိမ်မွေ့သော ရုပ်"),
             ("rūparāg", "သိမ်မွေ့သော ရုပ်"), ("rūpūpag", "သိမ်မွေ့သော ရုပ်"), ("rūpadhātuyā", "သိမ်မွေ့သော ရုပ်"),
             ("rūpadhātū", "သိမ်မွေ့သော ရုပ်"), ("rūpī", "သိမ်မွေ့သော ရုပ်"),
             ("rūpāyatan", "အဆင်းအရောင်"), ("rūpadhāt", "အဆင်းအရောင်"), ("rūpasaññ", "အဆင်းအရောင်"),
             ("rūpataṇh", "အဆင်းအရောင်"), ("rūpārammaṇ", "အဆင်းအရောင်"), ("rūpakkhandh", "ရုပ်"), ("rūpa", "ရုပ်")]
    v = first_compound(p, stems)
    if v == "သိမ်မွေ့သော ရုပ်" and "သိမ်မွေ့သော ရုပ်" not in my:
        v = None
    if v == "အဆင်းအရောင်" and "အဆင်းအရောင်" not in my:
        v = None
    if v is not None and presence(v, my)[0]:
        return v
    for c in ("ရုပ်", "အဆင်းအရောင်", "သိမ်မွေ့သော ရုပ်"):
        if c in my:
            return c
    return "@prior"


def f_rupam(kw, pali, my):
    """rūpaṃ: matter «ရုပ်» (the khandha); the seen object «အဆင်းအရောင်» in «rūpaṃ passati / cakkhunā rūpaṃ»
    (pi-5 harmonise B2 F.RUPA_SEEN; pi-2 ^2-517); one sense per segment, the first in the Pāli."""
    p = strip_brackets(pali)
    v = first_compound(p, [(r"rūpaṃ passat", "အဆင်းအရောင်"), (r"cakkhunā rūpaṃ", "အဆင်းအရောင်"),
                           (r"rūpaṃ disvā", "အဆင်းအရောင်"), (r"rūpa[ṃñm]", "ရုပ်")]) or "ရုပ်"
    if presence(v, my)[0]:
        return v
    return "ရုပ်" if "ရုပ်" in my else "@prior"


_DUKKHA = [("dukkhassant", "ဒုက္ခ"), ("dukkhassa antakiriy", "ဒုက္ခ"), ("dukkhamev", "ဒုက္ခ"),
           ("dukkhasacc", "ဒုက္ခ"), ("dukkhanirodh", "ဒုက္ခ"), ("dukkhasamuday", "ဒုက္ခ"), ("dukkhe" + _W, "ဒုက္ခ"),
           ("dukkhañāṇ", "ဒုက္ခ"), ("dukkhaṃ ariy", "ဒုက္ခ"), ("dukkhadassan", "ဒုက္ခ"),
           ("dukkhaṃ vedan", "နာကျင်သော"), ("dukkhāya vedan", "နာကျင်သော"), ("dukkhā vedan", "နာကျင်သော"),
           ("dukkhavedan", "နာကျင်သော"), ("adukkhamasukh", "နာကျင်"), ("dukkhindriy", "နာကျင်မှု"),
           ("sukhadukkh", "ဆင်းရဲ"), ("āpāyikaṃ dukkh", "ဆင်းရဲ"), ("nerayikaṃ dukkh", "ဆင်းရဲ"),
           ("dukkhudray", "ဆင်းရဲ"), ("dukkhavipāk", "ဆင်းရဲသော"), ("dukkh", "ဆင်းရဲ")]
_SUKHA = [("sukhaṃ vedan", "သာယာသော"), ("sukhā vedan", "သာယာသော"), ("sukhāya vedan", "သာယာသော"),
          ("sukhavedan", "သာယာသော"), ("adukkhamasukh", "သာယာ"), ("sukhindriy", "သာယာမှု"),
          ("sukhasahagat", "သာယာမှု"), ("sukhadukkh", "ချမ်းသာ"), ("dibbaṃ sukh", "ချမ်းသာ"),
          ("mānusakaṃ sukh", "ချမ်းသာ"), ("sukhudray", "ချမ်းသာ"), ("sukhavipāk", "ချမ်းသာသော"),
          ("sukh", "ချမ်းသာ")]


def f_dukkha(kw, pali, my):
    """dukkha, one sense per segment by the first compound (pi-3 f_dukkha with the pi-5 words): the truth / the end of
    suffering «ဒုက္ခ», painful feeling «နာကျင်သော» (adukkhamasukha «နာကျင်»), pain as the opposite of pleasure
    «ဆင်းရဲ» (sukhadukkha, āpāyika dukkha: my5-zeroshot-terms §7 / §8); checked against the text."""
    return by_first_checked(_DUKKHA, ["ဆင်းရဲ", "ဒုက္ခ", "နာကျင်သော", "နာကျင်မှု", "@prior"])(kw, pali, my)


def f_sukha(kw, pali, my):
    """sukha, likewise: pleasant feeling «သာယာသော», happiness «ချမ်းသာ» (dibbaṃ / mānusakaṃ sukhaṃ, sukhadukkha:
    my5-zeroshot-terms), the faculty «သာယာမှု» (pi-1 … pi-4)."""
    return by_first_checked(_SUKHA, ["ချမ်းသာ", "သာယာသော", "သာယာမှု", "@prior"])(kw, pali, my)


def f_anna(kw, pali, my):
    """añña «other»: the text's word «တခြားစီ» (aññaṃ A añño B «Aနှင့် Bသည် တခြားစီ ဖြစ်», pi-1 Aññaṃ), «တခြား»
    (pi-2) where the text has it alone, «အခြား» (anañño «အခြား မဖြစ်ဘဲ», aññatra «မှ အခြား»)."""
    for v in ("တခြားစီ", "တခြား", "အခြား"):
        if v in my:
            return v
    return "@prior"


def f_anna_f(kw, pali, my):
    """aññā: final knowledge «အပြည့်အဝ သိမြင်ခြင်း» (aññindriya, pi-1 … pi-4) or the feminine «other» (f_anna), by the
    first in the Pāli."""
    p = strip_brackets(pali)
    v = first_compound(p, [("aññindriy", "K"), ("aññātāv", "K"), (r"aññā" + _W, "O"), (r"aññaṃ", "O"),
                           (r"añño", "O")])
    if v == "K" and "အပြည့်အဝ သိမြင်" in my:
        return "အပြည့်အဝ သိမြင်ခြင်း" if "အပြည့်အဝ သိမြင်ခြင်း" in my else "@prior"
    # phase 3 (ch2-15 override): sammadaññāvimutto «… သိ၍ လွတ်မြောက်», aññāpaṭivedha «ရဟန္တာ ဖိုလ်ကို ထိုးထွင်း»
    v = first_compound(p, [("sammadaññ", "သိ၍"), ("aññāpaṭivedh", "ရဟန္တာ ဖိုလ်")])
    if v is not None and presence(v, my)[0]:
        return v
    return f_anna(kw, pali, my)


def f_hoti(kw, pali, my):
    """hoti: the copula «ဖြစ်သည်» (pi-4), existence «ရှိသည်» (pi-1 / pi-2) where the text has no «ဖြစ်»."""
    return "ဖြစ်သည်" if "ဖြစ်" in my else "ရှိသည်"


def f_karoti(kw, pali, my):
    """karoti / karonti = «ပြုသည်» (pi-4); only inside a Roman-script variant = (no direct equivalent)."""
    if not pali_has(kw, pali):
        return NONE
    for v in ("ပြုသည်", "ပြုလုပ်သည်"):
        if presence(v, my)[0]:
            return v
    return "@prior"


def f_sassato(kw, pali, my):
    """sassato: the predicate adjective «ထာဝရ တည်မြဲသော» (my5-zeroshot-terms «puggalo sassato»; rule 3); the view
    «… တည်မြဲသည်ဟု / ဟူသော» keeps the pi-1 / pi-2 clause «ထာဝရ တည်မြဲသည်» (rule 4)."""
    if re.search("ထာဝရ တည်မြဲသည်(ဟု|ဟူ)", my) and not re.search("ထာဝရ တည်မြဲသော|ထာဝရ တည်မြဲသူ|ထာဝရ တည်မြဲသလော", my):
        return "ထာဝရ တည်မြဲသည်"
    return "ထာဝရ တည်မြဲသော"


def f_upada(kw, pali, my):
    """upādā: «မှီ၍» (Upādāpaññatti, «upādāya»; absolutive kept, pi-1), the fragment of anupādā(parinibbāna) «စွဲလမ်းမှု
    မရှိဘဲ» = the positive part «စွဲလမ်းမှု» (rule 8)."""
    if re.search(r"anupādā", strip_brackets(pali)) and "စွဲလမ်းမှု" in my and "anupādā" not in kw:
        if not re.search(r"upādāpaññatt|upādāya", strip_brackets(pali), flags=re.I) or "မှီ၍" not in my:
            return "စွဲလမ်းမှု"
    return "မှီ၍" if "မှီ၍" in my else "@prior"


def f_dhatuya(kw, pali, my):
    """dhātuyā (rūpa- / arūpa- / kāmadhātuyā): the plane «ဘုံ» (pi-2 dhātu = ဘုံ) where the text has it, else
    the element «ဓာတ်»."""
    return "ဘုံ" if "ဘုံ" in my and re.search(r"(rūpa|kāma)dhātuyā", pali, flags=re.I) else "ဓာတ်"


def f_phala(kw, pali, my):
    """phala: the path-fruit «ဖိုလ်» (sotāpatti- / sakadāgāmi- / anāgāmi- / arahattaphala «…ဖိုလ်», pi-4), the fruit
    «အသီးအပွင့်» (saphala, iṭṭhaphala: my5-zeroshot-terms), the result «အကျိုး» (pi-4); by the first in the Pāli."""
    p = strip_brackets(pali)
    v = first_compound(p, [(r"(sotāpatti|sakadāgāmi|anāgāmi|arahatta|sāmañña)phal", "ဖိုလ်"),
                           (r"(sa|iṭṭha|aniṭṭha|kanta|akanta|manuñña|amanuñña|secanaka|asecanaka)phal", "အသီးအပွင့်"),
                           (r"phal", "အကျိုး")])
    for c in [v, "ဖိုလ်", "အသီးအပွင့်", "အကျိုး"]:
        if c and c in my:
            return c
    return "@prior"


FUNCS = {
    "jahati": lambda kw, pali, my: "စွန့်ပယ်သည်" if "စွန့်ပယ်" in my else "@prior",
    "panidhi": lambda kw, pali, my: "ဆုတောင်းခြင်း" if "ဆုတောင်းခြင်း" in my else "@prior",
    # jhānantarikā «ဈာန်တို့အကြား ကာလ» (ch26, phase 3), else «ကြားအပိုင်း»
    "antarika": lambda kw, pali, my: "အကြား ကာလ" if "အကြား ကာလ" in my else (
        "ကြားအပိုင်း" if "ကြားအပိုင်း" in my else "@prior"),
    "vita": lambda kw, pali, my: "ကင်းသော" if presence("ကင်းသော", my)[0] else "@prior",
    "bhavito": lambda kw, pali, my: "ပွားများပြီးသော" if presence("ပွားများပြီးသော", my)[0] else (
        "ပွားများထားသော" if presence("ပွားများထားသော", my)[0] else (           # phase 3 (ch16-31 override 7)
            "ပွားများသော" if presence("ပွားများသော", my)[0] else "@prior")),
    "arahatta": lambda kw, pali, my: "ရဟန္တာ အဖြစ်" if "ရဟန္တာ အဖြစ်" in my else (
        "အရဟတ္တ" if "အရဟတ္တ" in my else "@prior"),
    "phala": f_phala,
    "bojjha": lambda kw, pali, my: "ဗောဇ္ဈင်" if "ဗောဇ္ဈင်" in my else "@prior",
    "anga": lambda kw, pali, my: NONE if "bojjhaṅg" in pali and "ဗောဇ္ဈင်" in my and "အင်္ဂါ" not in my
        else ("အင်္ဂါ" if "အင်္ဂါ" in my else "@prior"),       # pi-2 decision 4: one Burmese word, one member
    "gati": lambda kw, pali, my: "လားရာ" if "လားရာ" in my else "@prior",
    # phase 3 (ch16-31 override 5): the member aṅga of bojjhaṅga (one Burmese word «ဗောဇ္ဈင်», pi-2 decision 4) =
    # (no direct equivalent) where the FIRST aṅga compound of the Pāli is bojjhaṅga; else «အင်္ဂါ»
    "anga": lambda kw, pali, my: NONE if (first_compound(strip_brackets(pali), [
        (r"[a-zāīūṃṅñṭḍṇḷ]*bojjhaṅg", "B"), (r"[a-zāīūṃṅñṭḍṇḷ]+aṅg", "A"), ("aṅg", "A")]) == "B"
        and "ဗောဇ္ဈင်" in my) else ("အင်္ဂါ" if "အင်္ဂါ" in my else (
        NONE if "bojjhaṅg" in pali and "ဗောဇ္ဈင်" in my else "@prior")),
    "tanha": pref("တပ်မက်မှု", "တဏှာ"),
    "niggaha": lambda kw, pali, my: "ချေပချက်" if "ချေပချက်" in my else (
        "ချုပ်ကိုင်ခြင်း" if "ချုပ်ကိုင်ခြင်း" in my else "@prior"),
    "niggahetabba": pref("ချေပရမည့်", "ချေပရသည်"),
    "roman": f_roman,
    # hevameva: the main text's «hevamevaṃ» «ဤနည်းအတိုင်းပင်» (the variant «hevameva» is the same word)
    "hevameva": lambda kw, pali, my: "ဤနည်းအတိုင်းပင်" if "hevameva" in strip_brackets(pali).lower()
        and "ဤနည်းအတိုင်းပင်" in my else NONE,
    "vata": lambda kw, pali, my: "အမှန်ပင်" if "အမှန်ပင်" in my and re.search(r"vata re|\bvata\b", pali) else "@prior",
    "miccha": f_miccha,
    "tenahi": first_in_text("သို့ဖြစ်လျှင်", "သို့ဖြစ်၍"),
    "puccha": if_text("အမေး", "အမေး", "@prior"),
    "vadi": lambda kw, pali, my: by_sub([("sakavād", "မိမိဘက်"), ("paravād", "တစ်ဖက်သား")], None)(kw, pali, my)
        if re.search(r"sakavād|paravād", pali) and ("မိမိဘက်" in my or "တစ်ဖက်သား" in my)
        else ("ဆိုတော်မူသော" if presence("ဆိုတော်မူသော", my)[0] else "@prior"),
    "atthena": if_text("အနက်", "အနက်"),
    "parama": if_text("အဆုံးစွန်", "အဆုံးစွန်"),
    "saccikattho": literal("အမှန်တကယ် အရာ", "အမှန်တကယ် … အရာ"),
    "attha_thing": lambda kw, pali, my: "အရာ" if "အရာ" in my and "ṭṭh" in pali else (number(kw, my) or "@prior"),
    "suddha": pref("ရိုးရိုး", "သက်သက်"),
    "sabbesu": if_text("အရာအားလုံး", "အရာအားလုံး"),
    "katva": if_text("အကြောင်းပြု", "အကြောင်းပြု၍"),
    "eva": by_first_checked([("attheva", "ပင်"), ("sveva", "ပင်"), ("teneva", "ပင်"), ("tasseva", "ပင်"),
                             ("tatheva", "ပင်"), ("ekova", "သာ"), ("dukkhameva", "သာ")], ["သာ", "ပင်"]),
    "katha": lambda kw, pali, my: next((v for v in ("ဆွေးနွေးချက်", "ဆွေးနွေးခြင်း") if v in my), "@prior"),
    "naya": lambda kw, pali, my: "နည်း" if "နည်း" in my else "@prior",
    "koci": pref("တစ်စုံတစ်ယောက်", "တစ်စုံတစ်ရာ"),
    "yo": lambda kw, pali, my: "အကြင်သူ" if "အကြင်သူ" in my else NONE,
    "yam": lambda kw, pali, my: "အကြင်အရာ" if "အကြင်အရာ" in my else NONE,
    "yena": lambda kw, pali, my: "အကြင်အရာ" if "အကြင်အရာဖြင့်" in my else NONE,
    "anna": f_anna, "anna_f": f_anna_f, "hoti": f_hoti, "upada": f_upada,
    "cavati": lambda kw, pali, my: "စုတေသည်" if "စုတေ" in my else "သေသည်",
    "karoti": f_karoti, "sassato": f_sassato,
    "viraga": lambda kw, pali, my: "ပြယ်ပျောက်" if "ပြယ်ပျောက်တတ်" in my else "@prior",
    "rupam": f_rupam, "rupa": f_rupa, "dukkha": f_dukkha, "sukha": f_sukha, "dhatuya": f_dhatuya,
    "para": by_first_checked([("paracitt", "အခြားသူ"), ("paraṃ lok", "တမလွန်"), ("parasmā lok", "တမလွန်"),
                              ("paraṅkār", "သူတစ်ပါး"), ("paraṃkār", "သူတစ်ပါး"), ("paravād", "တစ်ဖက်သား")],
                             ["@prior"]),
    "hitaya": pref("အကျိုးစီးပွား", "အကျိုး"),
    # phase 3 (ch16-31 override 10): the bare noun dhammo «သဘောတရား / တရား»; where the FIRST dhammo of the Pāli is
    # a -dhammo compound (avipariṇāmadhammo, ṭhitadhammo) the pi-1 … pi-4 compound value «သဘော ရှိသော»
    "dhammo": lambda kw, pali, my: "@prior" if (lambda m: m and m.group(1))(re.search(
        r"(?<![a-zāīūṃṅñṭḍṇḷ])([a-zāīūṃṅñṭḍṇḷ]*)dhammo", strip_brackets(pali), flags=re.I))
        else alt("သဘောတရား", "တရား")(kw, pali, my),
    # phase 3 (ch16-31 override 3): the loanword «သုခ» of the Sukhānuppadāna kathā (ch24) and ch25, where the
    # chapter table names it; else f_sukha
    "sukha_loan": lambda kw, pali, my: "သုခ" if "သုခ" in my else f_sukha(kw, pali, my),
    # phase 3: magga = the path «မဂ်» where the text has it, the road «လမ်း» (maggāmagga, the verses) otherwise
    "magga": lambda kw, pali, my: "မဂ်" if "မဂ်" in my and not re.search(r"maggāmagg", pali) else (
        "လမ်း" if "လမ်း" in my else ("မဂ်" if "မဂ်" in my else "@prior")),
    # phase 3 (ch16-31 override 10): dhātū before «ti» (kāma- / rūpa- / arūpadhātūti) the plane «ဘုံ», else «ဓာတ်»
    "dhatu_plane": lambda kw, pali, my: "ဘုံ" if "ဘုံ" in my and re.search(r"(kāma|rūpa)dhāt", pali) else (
        "ဓာတ်" if "ဓာတ်" in my else "@prior"),
    # phase 3: atta of attabhāva «ကိုယ်ခန္ဓာ» = «ကိုယ်» (pi-2 decision 4: the one word to the first member); else the
    # pi-1 / pi-2 «အတ္တ», pi-4 «မိမိ»
    "atta": lambda kw, pali, my: "ကိုယ်" if "attabhāv" in pali and "ကိုယ်ခန္ဓာ" in my else (
        "အတ္တ" if "အတ္တ" in my else ("မိမိ" if "မိမိ" in my else "@prior")),
    # phase 3: jano / janassa of puthujjana: the one Burmese word «ပုထုဇဉ်» goes to puthu (pi-2 decision 4)
    "jana": lambda kw, pali, my: NONE if "puthujjan" in pali.lower() and "ပုထုဇဉ်" in my else "@prior",
    "sacca": by_first_checked([("saccavād", "မှန်သော"), ("saccato", "အမှန်")], ["@prior"]),
}
# ---- FUNCS-END


def alt_name(vals):
    """the FUNCS name of a tuple value («@alt:a|b|…»), registered on first use."""
    name = "alt:" + "|".join(vals)
    FUNCS.setdefault(name, alt(*vals))
    return "@" + name


for _tab in (FRAME, STOCK):          # the tuples of the module tables (phase 3) as «@alt:…» values
    for _k, _v in list(_tab.items()):
        if isinstance(_v, tuple):
            _tab[_k] = alt_name(_v)


# =====================================================================================================================
# lookup engine
# =====================================================================================================================
def contiguous(v, my):
    parts = v.split(" … ")
    if not all(p in my for p in parts):
        return False
    return len(parts) == 1 or v.replace(" … ", " ") not in my


def contiguous_rule(v, my):
    for part in v.split(" … "):
        if part in my:
            continue
        if not part.endswith("သော") or not any(part[:-3] + e in my for e in ATTR_FROM):
            return False
    return True


def pi_get(kw, my, tiers=("contig", "literal", "rule")):
    """the most frequent pi-2 (then pi-3, pi-4, pi-1) value of the keyword present in the segment, by tier (pi-4
    engine): contiguous phrase, then every chunk literal, then (verbs «…သည်» or a whole phrase with another
    attributive ending) by an ending rule."""
    ranked = [(t, [v for v, _ in prev_vals(kw, t).most_common() if v != NONE]) for t in PRIOR_ORDER]
    for tier in tiers:
        for tag, vals in ranked:
            for v in vals:
                if tier == "rule" and not (v.endswith("သည်") or contiguous_rule(v, my)):
                    continue
                ok, rules = presence(v, my)
                if not ok:
                    continue
                if (tier == "contig" and contiguous(v, my)) or (tier == "literal" and not rules) or tier == "rule":
                    return v, tag
    return None, None


def find_pos(v, my):
    first = v.split(" … ")[0]
    cands = [first[:-3], first] if first.endswith(("သော", "သည်")) else [first]
    w = first.split()[0]
    cands.append(w)
    if w.endswith(("သော", "သည်")):
        cands.append(w[:-3])
    for c in cands:
        if c:
            p = my.find(c)
            if p < 0 and c.startswith("မ"):
                p = my.find(c[1:])
            if p >= 0:
                return p
    return 10 ** 6


# the particles that may stand between two members of a multiword keyword in the text: they stay inside the value
# (pi-1 rule 1: only the particles at the END of a value go; «ပုဂ္ဂိုလ်၏ သတ်မှတ်ချက်», «ရုပ်ကို မှီ၍»). The «လည်း» of
# ca («also») is not part of a keyword: a member followed by «…လည်း» is joined with « … » (Q4).
PARTICLES = ("", "ကို", "သည်", "၏", "၌", "တွင်", "နှင့်", "မှ", "ဖြင့်", "အား", "သို့", "က", "ကား", "သည်ပင်", "ပင်",
             "ဟု", "ဟူသော", "နှင့်တကွ", "နှင့်အတူ", "အားဖြင့်", "တို့", "တို့၏", "တို့ကို", "တို့သည်", "တို့၌",
             "တို့နှင့်", "တို့နှင့်တကွ", "များ", "များကို", "များ၏", "၏ပင်", "ကိုပင်")


def phrase_present(s, my, verb_from=None):
    """the phrase stands in the text, its final «သည် / သော» standing for one of the text's endings (rules 3 / 4); a
    perfect participle «Xပြီးသော» also as the text's perfect predicate «Xပြီး ဖြစ်» (phase 3: as presence() does)."""
    if s in my:
        return True
    if s.endswith("သည်"):
        return any(s[:-3] + e in my for e in (verb_from or VERB_FROM))
    if s.endswith("သော"):
        if s.endswith("ပြီးသော") and s[:-3] + " ဖြစ်" in my:
            return True
        return any(s[:-3] + e in my for e in ATTR_FROM)
    return False


# phase 3: a finite verb is glued to its neighbour only in a verbal form, not through the verbal noun «…ခြင်း»
# («ရဟန္တာ၏ ဆုတ်ယုတ်ခြင်း» is parihāni, not «Parihāyati arahā»)
GLUE_VERB_FROM = tuple(e for e in VERB_FROM if e != "ခြင်း")


def phrase_ok(v, my):
    """every « … » part of the value stands as a phrase in the text (its final «သည် / သော» by an ending rule): a
    multiword value is not assembled from chunks scattered over the segment."""
    return all(phrase_present(p, my) for p in v.split(" … "))


def glue(a, b, my):
    """the particle that joins value a to value b where they are adjacent in the text, else None."""
    a_last, b_first = a.split(" … ")[-1], b.split(" … ")[0]
    vf = GLUE_VERB_FROM if is_verb(b) and " … " not in b else None
    if phrase_present(f"{a_last}{b_first}", my, vf) and not phrase_present(f"{a_last} {b_first}", my, vf):
        return "\0"            # one written word in the text («နတ်မျက်စိ»): no space
    for p in PARTICLES:
        if phrase_present(f"{a_last}{p} {b_first}", my, vf):
            return p + " "
    return None


def is_verb(v):
    """a finite verb value («…သည်», or the negative «မX» of rule 9 / pi-2 «na uppajjati»)."""
    last = v.split(" … ")[-1].split()[-1]
    return last.endswith("သည်") or (last.startswith("မ") and v in NEG_VERBS)


NEG_VERBS = {"မတွေ့ရ"}


def occurrences(v, my):
    """all positions in the text of the value's first part (or its stem without the final «သည် / သော», or its first
    chunk, or that chunk's stem; a negative «မX» also as X)."""
    first = v.split(" … ")[0]
    cands = [first[:-3], first] if first.endswith(("သော", "သည်")) else [first]
    w = first.split()[0]
    cands.append(w)
    if w.endswith(("သော", "သည်")):
        cands.append(w[:-3])
    for c in cands:
        if c and c in my:
            return [m.start() for m in re.finditer(re.escape(c), my)]
    return []


def span_order(vals, my):
    """Q3: the members' values in the order of their tightest window in the text (the members of one phrase stand
    together); a finite verb goes last (Burmese is verb-final)."""
    import itertools
    best = None
    for perm in itertools.permutations(range(len(vals))):
        if any(is_verb(v) for v in vals) and not is_verb(vals[perm[-1]]):
            continue
        occ = [occurrences(vals[i], my) for i in perm]
        if not all(occ):
            continue
        w = None
        for start in occ[0]:
            pos, ok = start, True
            for o in occ[1:]:
                nxt = [q for q in o if q > pos]
                if not nxt:
                    ok = False
                    break
                pos = nxt[0]
            if ok and (w is None or pos - start < w):
                w = pos - start
        if w is not None and (best is None or w < best[0]):
            best = (w, perm)
    if best is None:
        order = [v for _, _, v in sorted(zip([find_pos(v, my) for v in vals], range(len(vals)), vals))]
        return [v for v in order if not is_verb(v)] + [v for v in order if is_verb(v)]
    return [vals[i] for i in best[1]]


def join_text_order(vals, my):
    """multiword keyword: its members' values joined in TEXT order (Q3), « … » where they are not adjacent (rule 10);
    a member adjacent to the next keeps the particle between them (rule 1)."""
    vals = [v for v in vals if v != NONE]
    if not vals:
        return NONE
    vals = list(dict.fromkeys(vals))
    if len(vals) == 2 and not any(is_verb(v) for v in vals):   # an adjacent pair in either order first (pi-4 P8)
        for x, y in ((vals[0], vals[1]), (vals[1], vals[0])):
            g = glue(x, y, my)
            if g is not None:
                return x + g.replace("\0", "") + y
    order = span_order(vals, my)
    out = order[0]
    for v in order[1:]:
        if v in out:
            continue
        g = glue(out, v, my)
        out = out + (g.replace("\0", "") if g is not None else " … ") + v
    return out


def table_get(tab, kw):
    for k in (kw, low(kw), kw[:1].upper() + kw[1:]):
        if k in tab:
            return tab[k]
    return None


NEG_WORDS = ("na", "no")


def kathā_heading(kw, v, my):
    """phase 3 scan (A1): a kathā heading «X-kathā» = the text's phrase «Xအကြောင်း ဆွေးနွေးချက်» where it stands (rule 1:
    the inner «အကြောင်း» stays; rule 10: « … » only for discontinuous parts)."""
    if low(kw).endswith("kathā") and v.endswith(" … ဆွေးနွေးချက်"):
        g = v[:-len(" … ဆွေးနွေးချက်")] + "အကြောင်း ဆွေးနွေးချက်"
        if g in my:
            return g
    return v


def internal_neg(kw):
    """a multiword keyword with na / no after its first word («anāgāmī na parihāyati», «Na parihāyati anāgāmī» is
    initial and goes through compose)."""
    ws = [low(w) for w in kw.split()]
    return len(ws) > 1 and ws[0] not in NEG_WORDS + ("neva",) and any(w in NEG_WORDS for w in ws[1:])


def make_stem(tables):
    """S1 (phase 2 ch2-15, approved after the phase-3 review): the stem fallback over the pi-1 … pi-4 values and the
    given tables: a single keyword that nothing else maps takes the value of a keyword of the same stem (the longest
    common beginning, at least the keyword less four letters, length within five) that the segment's Burmese has as a
    phrase, most frequent first (a table value counts 50)."""
    pool = collections.defaultdict(collections.Counter)
    for t in PRIOR_ORDER:
        for k, c in prior()[t].items():
            pool[k].update(c)
    for tab in tables:
        for k, v in tab.items():
            for x in (v if isinstance(v, tuple) else (v,)):
                if not x.startswith("@") and x != NONE:
                    pool[low(k)][x] += 50
    keys = sorted(k for k in pool if " " not in k)

    def stem(kw, my):
        k = low(kw)
        for n in range(len(k), max(4, len(k) - 4) - 1, -1):
            pre = k[:n]
            c = collections.Counter()
            for kk in keys:
                if kk.startswith(pre) and abs(len(kk) - len(k)) <= 5:
                    c.update(pool[kk])
            for v, _ in c.most_common():
                if presence(v, my)[0] and phrase_ok(v, my):
                    return v
        return None
    stem.pool = pool
    return stem


CLAUSE_BOUND = re.compile("[။…–“”]")          # sentence end, the «…pe…» gap, a quotation or dash
WEAK_BOUND = re.compile("[။၊…–“”]")           # also the list comma «၊»


def clause_order(x, y, my, bound=CLAUSE_BOUND):
    """phase 3 (G2 made exact): the text has x before y within ONE clause (no «။ … – “ ”» between them; with
    WEAK_BOUND no «၊» either), the x not standing inside y's own words («ရုပ်» of «ရုပ်မရှိသော ဘုံ»)."""
    yf = y.split(" … ")[0]
    py = occurrences(y, my)
    for a in occurrences(x, my):
        if len(yf) > len(x.split(" … ")[0]) and any(b <= a < b + len(yf) for b in py):
            continue
        if any(a < b and not bound.search(my[a:b]) for b in py):
            return True
    return False


class Mapper:
    """chapter_tables: {ch: {kw: value}}; ctx: {sid: {kw: value}}; a value «@name» calls FUNCS[name] (or the
    mapper's own funcs); a tuple value = alt(). stem: a make_stem() function (S1) for single keywords nothing else
    maps. SRC[(sid, kw)] records where each value came from.

    lookup(): CTX / table entry first; a negative inside a multiword keyword (S3 / G3) = negate(the rest); else the
    chain (_chain); a single keyword the chain cannot map = the stem fallback (S1); two members joined by compose =
    pali_order (G1 / G2)."""

    def __init__(self, chapter_tables=None, ctx=None, funcs=None, shared=None, stem=None):
        self.tables = {ch: {k: (alt_name(v) if isinstance(v, tuple) else v) for k, v in tab.items()}
                       for ch, tab in (chapter_tables or {}).items()}
        self.ctx = {sid: {k: (alt_name(v) if isinstance(v, tuple) else v) for k, v in tab.items()}
                    for sid, tab in (ctx or {}).items()}
        self.stem = stem
        self.order = True             # G1 / G2 (pali_order); ORDER[(ch, sid, kw)] = (text-order value, new value)
        self.ORDER = {}
        self.funcs = dict(FUNCS)
        self.funcs.update(funcs or {})
        self.shared = {}
        for tab in [FRAME, STOCK] + list((shared or {}).values()):
            for k, v in tab.items():
                self.shared.setdefault(low(k), v)
        self.SRC = {}

    # -- values
    def resolve(self, v, kw, pali, my):
        while v is not None and v.startswith("@"):
            v = self.funcs[v[1:]](kw, pali, my)
            if v == "@prior":
                v = pi_get(kw, my)[0]
                if v is None:
                    raise KeyError(kw)
        return v

    def lookup(self, ch, sid, kw, pali, my):
        ws = kw.split()
        if internal_neg(kw) and table_get(self.ctx.get(sid, {}), kw) is None \
                and table_get(self.tables.get(ch, {}), kw) is None:
            rest = " ".join(w for w in ws if low(w) not in NEG_WORDS)
            v = negate(self.lookup(ch, sid, rest, pali, my), my)
            self.SRC[(sid, kw)] = "neg"
            return v
        try:
            v = self._chain(ch, sid, kw, pali, my)
        except KeyError:
            if " " in kw or self.stem is None:
                raise
            v = self.stem(kw, my)
            if v is None:
                raise
            self.SRC[(sid, kw)] = "stem"
            return kathā_heading(kw, v, my)
        v = kathā_heading(kw, v, my)
        if len(ws) == 2 and self.SRC.get((sid, kw)) == "compose" and v != NONE and self.order:
            w = self.pali_order(ch, sid, ws, v, pali, my)
            if w != v:
                self.ORDER[(ch, sid, kw)] = (v, w)
            v = w
        return v

    def pali_order(self, ch, sid, ws, v, pali, my):
        """two members joined by compose (phase 2 G1 / G2, book-wide): (G1) the «ပင်» of eva / va between them is not
        part of the keyword (as Q4: « … »); (G2) where the text has the members in the Pāli order too, that order (an
        adjacent pair in the other order with no particle between them may be a neighbouring phrase); an adjacency
        with a particle is the text's own construction and stays («ဆိုးသော လားရာကို ပယ်ပြီးသော»). Phase 3 (G2 made
        exact): an attributive «…သော X» adjacency is a construction too and stays; a bare adjacency «Y X» goes to the
        Pāli order only where the text has «X … Y» inside one clause with no «၊» between; a gapped «Y … X» only where
        the text has «X … Y» inside one clause (a window across «။ / … / – / “ ”» is not the text's order)."""
        try:
            x, y = (self._chain(ch, sid, w, pali, my) for w in ws)
        except KeyError:
            return v
        if NONE in (x, y) or is_verb(x) or is_verb(y) or x == y:
            return v
        for g in ("ပင် ", "သည်ပင် ", "၏ပင် ", "ကိုပင် "):
            if v in (x + g + y, y + g + x):
                v = (x + " … " + y) if v.startswith(x) else (y + " … " + x)
        g_rev = glue(y, x, my)
        glued = g_rev is not None and g_rev.strip() and v == y + g_rev + x
        attributive = v == y + " " + x and y.split()[-1].endswith("သော")   # phase 3: «…သော X» is a construction
        if v.startswith(y) and v.endswith(x) and len(v) > len(y) + len(x) - 1 and not glued and not attributive:
            adjacent = v in (y + " " + x, y + x)
            if clause_order(x, y, my, WEAK_BOUND if adjacent else CLAUSE_BOUND):
                g = glue(x, y, my)
                return x + (g.replace("\0", "") if g is not None else " … ") + y
        return v

    def _chain(self, ch, sid, kw, pali, my):
        v = table_get(self.ctx.get(sid, {}), kw)
        if v is not None:
            self.SRC[(sid, kw)] = "ctx"
            return self.resolve(v, kw, pali, my)
        v = table_get(self.tables.get(ch, {}), kw)
        if v is None:
            v = table_get(FRAME, kw)
            src = "frame"
        else:
            src = "table"
        if v is None:
            v = table_get(STOCK, kw)
            src = "stock"
        if v is None:
            v = table_get(self.shared, kw)
            src = "table"
        if v is not None:
            self.SRC[(sid, kw)] = src
            return self.resolve(v, kw, pali, my)
        t = terms().get(low(kw))
        if t is not None and presence(t, my)[0] and all(p in my for p in t.split(" … ")):
            self.SRC[(sid, kw)] = "terms"
            return t
        v, tag = pi_get(kw, my, tiers=("contig",))
        if v is not None:
            self.SRC[(sid, kw)] = tag
            return v
        if t is not None and presence(t, my)[0] and phrase_ok(t, my):
            self.SRC[(sid, kw)] = "terms"
            return t
        if " " in kw:
            v, tag = pi_get(kw, my)      # binding: a pi-1 … pi-4 multiword value the text has (by an ending rule)
            if v is not None and phrase_ok(v, my):
                self.SRC[(sid, kw)] = tag
                return v
            try:
                v = self.compose(ch, sid, kw, pali, my)
            except KeyError:
                v = None
            if v is not None and presence(v, my)[0]:
                self.SRC[(sid, kw)] = "compose"
                return v
        v = number(kw, my)
        if v is not None:
            self.SRC[(sid, kw)] = "compose"
            return v
        v, tag = pi_get(kw, my)
        if v is not None:
            self.SRC[(sid, kw)] = tag
            return v
        raise KeyError(kw)

    def compose(self, ch, sid, kw, pali, my):
        ws = kw.split()
        if low(ws[0]) in ("na", "no", "neva"):
            rest = " ".join(ws[1:])
            v = self.lookup(ch, sid, rest, pali, my)
            return negate(v, my)
        if len(ws) > 2:          # pi-4: a multiword part with a value of its own first («nibbānassa paṭisaṃvedī» + V)
            for a_, b_ in ((" ".join(ws[:-1]), ws[-1]), (ws[0], " ".join(ws[1:]))):
                multi = a_ if " " in a_ else b_
                if table_get(self.ctx.get(sid, {}), multi) is not None or table_get(self.tables.get(ch, {}), multi) \
                        is not None or table_get(self.shared, multi) is not None or low(multi) in terms():
                    try:
                        x, y = self.lookup(ch, sid, a_, pali, my), self.lookup(ch, sid, b_, pali, my)
                    except KeyError:
                        continue
                    return join_text_order([x, y], my)
        vals = [self.lookup(ch, sid, w, pali, my) for w in ws]
        return join_text_order(vals, my)

    # -- chapters
    def map_chapter(self, ch):
        my, pa = burmese(ch), pali(ch)
        lines, problems, unmapped, nne = [], [], [], 0
        for sid, kws in keyword_rows(ch):
            pairs = []
            for kw in kws:
                try:
                    v = self.lookup(ch, sid, kw, pa.get(sid, ""), my[sid])
                except KeyError:
                    unmapped.append((sid, kw))
                    v = "?"
                else:
                    if not presence(v, my[sid])[0]:
                        problems.append((sid, kw, v))
                pairs.append(f"{kw}={v}")
                nne += v == NONE
            lines.append(f"[{sid}] " + ", ".join(pairs))
        return lines, problems, unmapped, nne


def negate(v, my):
    """«na / no X» and a negative inside a multiword keyword (S3 / G3, Q5): the LAST verb chunk «Xသည် / Xသော» becomes
    the text's «မX» (pi-1 rule 9: free na = the text's prefix «မ»; pi-2 «na uppajjati = … မဖြစ်ပေါ်»), or its infix
    «XမY» (ဖြစ်ပေါ် / တွေ့ရ …), or «X မဟုတ်» (pi-1 rule 5); every « … » part is checked in the text by itself (phase 3:
    the old check took a gapped «S … မV» as one literal phrase and never found it). With no such form: «X … မဟုတ်»
    where the text has «မဟုတ်» (pi-1 rule 5), else «X မဟုတ်» (the module's earlier fallback)."""
    if v == NONE:
        return v
    head, sep, last = v.rpartition(" … ")
    pre, sp, w = last.rpartition(" ")
    base = head + sep + pre + sp
    if w.endswith(("သည်", "သော")) and len(w) > 3:
        st = w[:-3]
        cands = [base + st[:i] + "မ" + st[i:] for i in range(0, len(st))] + [base + st + " မဟုတ်"]
        for c in cands:
            if all(p in my for p in c.split(" … ")):
                return c
    if "မဟုတ်" in my and v + " မဟုတ်" not in my:       # G3: «X … မဟုတ်» (pi-1 rule 5)
        return v + " … မဟုတ်"
    if v.endswith("သော"):
        return v[:-3] + "သည် မဟုတ်သော"
    return v + " မဟုတ်"


neg_value = negate             # the phase-1 name


def number(kw, my):
    n = NUM_MY.get(low(kw))
    if n is None:
        return None
    for c in ("ယောက်", "ပါး", "မျိုး", "ကြိမ်", "ခု", ""):
        if n + c in my:
            return n + c
    return None


# =====================================================================================================================
# verifier
# =====================================================================================================================
def verify_file(ch, mapped_dir=HERE):
    """-> (lines, bad, fails, punct, ruled): the brief's keyword-preservation check (bad), presence failures, «, » /
    «၊» / « / » inside a value or a wrong pair count (punct), and every chunk matched by an ending rule (ruled)."""
    mapped_dir = pathlib.Path(mapped_dir)
    a = [l.split("] ", 1) for l in (HERE / f"{ch}.keywords.md").read_text(encoding="utf-8").splitlines()]
    b = [l.split("] ", 1) for l in (mapped_dir / f"{ch}.mapped.md").read_text(encoding="utf-8").splitlines()]
    assert [x[0] for x in a] == [x[0] for x in b]
    bad = [i for (i, x), (_, y) in zip(a, b)
           if [k.strip() for k in x.split(", ")] != [k.split("=", 1)[0] for k in y.split(", ")]]
    my = burmese(ch)
    fails, ruled = [], []
    for (i, x), (_, y) in zip(a, b):
        for kv in y.split(", "):
            k, v = kv.split("=", 1)
            ok, rules = presence(v, my[i[1:]])
            if not ok:
                fails.append((i, k, v))
                continue
            for c, r in rules:
                ruled.append((i[1:], k, c, r))
    punct = [i for (i, x), (_, y) in zip(a, b)
             if any(", " in v or "၊" in v or " / " in v for v in [kv.split("=", 1)[1] for kv in y.split(", ")])
             or y.count("=") != len(x.split(", "))]
    return len(a), bad, fails, punct, ruled
