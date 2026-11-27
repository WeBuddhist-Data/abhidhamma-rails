"""Shared rules of the pi-7 Pāli→Burmese keyword mapping (Paṭṭhāna «အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ»).

Settled on phase 1 (preamble, 1-00-paccaya, 1-02-vedanattika; map_sample.py) and imported by the phase-2 agents and
the phase-3 consistency scan. NOTHING RUNS ON IMPORT: every file is read lazily (functools.lru_cache) the first time a
function needs it; the module only defines constants, tables and functions. Copied from pi-6
`pi-6-my/mapper-my/map6_rules.py` (not imported): the loaders, the presence verifier (pi-1 … pi-6 endings, with the five
phase-3 mechanics of pi-6), the lookup engine (pi_get tiers with phrase_ok, S1 stem fallback, R1 base forms, R7 «လည်း»
gap, Q5 negatives), the generic context helpers. The Yamaka tables are replaced by the Paṭṭhāna tables below. The
pi-7 Burmese values come from the FINAL pi-7 text and its own term list (my7-zeroshot-terms.md, my7_formulas.py:
read, never imported) and from the FINAL pi-1 … pi-6 mappings.

Contents
  paths and loaders          segments(), keyword_rows(), prior() (pi-1 … pi-6 FINAL mappings), terms(), head_lex()
  presence verifier          chunk_present(), presence() (the pi-6 check, endings unchanged)
  frame / stock tables       FRAME (book frame, particles, link words, verbs, notes), STOCK (core terms of the book)
  Paṭṭhāna families (pi-7)   CONDS + cond_cands()   the 24 conditions in every case and polarity (T1-T4)
                             VARA + vara_cands()    the vāra names in every case (T5)
                             ORDER + order_cands()  anuloma / paccanīya orders (T5)
                             COUNT words, count groups (T6), numbers()
                             term_cands()           the triad / dyad term qualifiers in any case; na-X (T7, T8)
                             head_lex()             the text's own heading parts, book-wide (T9)
                             VERB_ROOTS / parse_verb()  verbs in every mood (T10)
  context functions          FUNCS[name](kw, pali, my) -> value; a table value «@name» calls one
  lookup engine              Mapper(tables, ctx).lookup(ch, sid, kw, pali, my): CTX[sid] -> chapter table -> FRAME /
                             STOCK -> families (conditions, vāra, order, counts) -> heading lexicon -> verbs ->
                             base form (R1) -> pi-7 terms -> a pi-1 … pi-6 value the text has -> term family (case
                             siblings, na-X) -> numbers -> heading rule (R6) -> stem fallback (S1); every value then
                             gets the «လည်း» gap of R7 and loses a list comma «၊» (rule 6)
  verifier                   verify_file(ch, mapped_dir)

Phase 3 (2026-11-26, the coordinator's module fixes; map-harmonise-notes.md, phase3-changes.tsv):
  1 word boundaries      occurs() / bounded_at(): a value chunk ends on a Burmese word boundary (phrase_present,
                         contiguous, the terms check, pick) - never the start of a longer word
  2 pīti                 BOOK pīti «ပီတိ» (no pi + iti)
  3 tadārammaṇatā        _GEN_RX skips a concatenated generator string; STOCK one value per text form
  4 noupādā              STOCK «မူလဓာတ်ကြီးများကို မှီ၍ ဖြစ်သည် မဟုတ်သော»
  5 R1 order             _chain: each step for the keyword and its base forms before the next step (tables, families,
                         pi values, then the term family)
  6 negatives            term_family: the plain na-X candidates of every value before a gapped one
  7 numbers              pali_number knows «bīsa(ti)»
  8 one value per term   f_sekkha (qualifier «…၏» / person), BOOK values of the group tables
  9 dictionary forms     BOOK (gaṇetabbā, vitthāretabbāni, uppādenti, vipassanti, bhāgo, pañcaviññāṇaṃ, paripuṇṇo …)
  and the decided points: gocchaka items bare (cluster_cands), natthi (f_natthi with the in-term mask and the T4 hyphen
  part), naviññeyyo (f_navinn), Nahetuṃ dhammaṃ = the term (cond_cands), vāra-compound parts (vara_part), vipākassa.

Usage in a chapter script (see map_sample.py):
    import map7_rules as R
    M = R.Mapper(chapter_tables={"1-01-kusalattika": T}, ctx=CTX, stem=R.make_stem([R.FRAME, R.STOCK, T]))
    lines, problems, unmapped, nne = M.map_chapter("1-01-kusalattika")
"""
import re
import bisect
import pathlib
import collections
import functools

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
MY = ROOT / "AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters"
PI = ROOT / "AI_translation/pali/pi-7_split_chapters"
MAPS = {t: ROOT / f"AI_translation/burmese/{t}-keywords-by-reference-pali-burmese-plain.md"
        for t in ("pi-1", "pi-2", "pi-3", "pi-4", "pi-5", "pi-6")}
TERMS_FILE = HERE.parent / "my7-zeroshot-terms.md"
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")
LINE = re.compile(r"^\[([^\]]+)\] (.*)$")
NONE = "(no direct equivalent)"
# pi-2 first where pi-1 and pi-2 differ (pi-1 brief), then pi-3, pi-4, pi-5, pi-6 (the order of the pi-5 / pi-6
# mappers, each later book added before pi-1), then pi-1
PRIOR_ORDER = ("pi-2", "pi-3", "pi-4", "pi-5", "pi-6", "pi-1")
SAMPLE = ["preamble", "1-00-paccaya", "1-02-vedanattika"]
PW = "a-zāīūṃṅñṭḍṇḷ"                       # Pāli letters (lower case)
_PW = r"(?![\wāīūṃṅñṭḍṇḷ])"               # end of a Pāli word


@functools.lru_cache(maxsize=None)
def chapters():
    """the 75 chapters of the keyword files, the preamble first, then in file-name order."""
    names = sorted(p.name[:-len(".keywords.md")] for p in HERE.glob("*.keywords.md"))
    return ["preamble"] + [n for n in names if n != "preamble"]


def low(w):
    return w[:1].lower() + w[1:]


def strip_brackets(pali):
    """the Pāli without its variant / editorial brackets «[…]» / «{…}»."""
    return re.sub(r"\s*[\[{][^\]}]*[\]}]", "", pali)


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
    """{tag: {low(kw): Counter(value)}} of the final pi-1 … pi-6 Burmese mappings."""
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


# the final particles a nominal value loses (pi-1 rule 1) and the sentence ends (rule 6)
FINAL_PART = ("တို့၌", "တို့၏", "တို့ကို", "တို့သည်", "တို့အား", "တို့", "များ", "၌", "၏", "ကို", "တွင်", "အား",
              "ဖြင့်", "မှ", "ဟု", "။")


def dict_noun(v):
    """rule 1 / rule 6: a nominal value without its final case particle / plural marker / «။», without the list comma
    «၊» inside it and without the emphasis asterisks of a heading."""
    v = v.replace("*", "").strip()
    v = v.replace("၊ ", " ").replace("၊", "").strip()
    changed = True
    while changed:
        changed = False
        for p in FINAL_PART:
            if v.endswith(p) and len(v) > len(p) + 1:
                v = v[:-len(p)].rstrip()
                changed = True
    return v


_TERM_KIND = re.compile(r"\s*\[[A-Za-z]{1,4}\]\s*$")       # the LEX kind «[n]» «[a]» «[x]» …


def _term_lines():
    """(pāli, burmese) of the «- Pāli = Burmese» lines of my7-zeroshot-terms.md, the notes «(…)» and the LEX kind
    «[…]» removed; frames with P / Q / X / Y / Z, «/» pairs and «…» lines left out."""
    out = []
    for l in TERMS_FILE.read_text(encoding="utf-8").splitlines():
        if not l.startswith("- ") or " = " not in l:
            continue
        p, b = l[2:].split(" = ", 1)
        p = re.sub(r"\s*\([^)]*\)", "", p).strip().rstrip(".?!").strip()
        b = _TERM_KIND.sub("", b.strip())
        b = re.sub(r"\s*\((?=[^)]*(?:pi-\d|NEW|[A-Za-z]))[^()]*\)\s*$", "", b).strip()
        if not p or not b or " / " in p or " / " in b or "…" in p or "…" in b or "§" in p:
            continue
        if re.search(r"[A-Za-zāīūṃṅñṭḍṇḷ;=«»]", b) or "(" in b:
            continue
        if re.search(r"\b[PQXYZ]\b|[A-Z]paccay|^X|Xp", p) or len(p.split()) > 4:
            continue
        if b.startswith("ကို "):
            b = b[len("ကို "):]          # a postposition entry «upanissāya = ကို အားကြီးစွာ မှီ၍»: the object is not part
        out.append((p, b))
    return out


@functools.lru_cache(maxsize=None)
def terms():
    """T11: my7-zeroshot-terms.md -> {low(pāli): burmese} in dictionary form (rule 1), single-word lines only."""
    t = {}
    for p, b in _term_lines():
        if " " not in p:
            b = dict_noun(b)
            if b.endswith("ကြသည်"):
                b = b[:-len("ကြသည်")] + "သည်"        # rule 4: the dictionary verb has no plural «ကြ» (pi-6 uppajjanti)
            if b:
                t.setdefault(low(p), b)
    return t


# T11: the words of the multiword lines of the pi-7 phrase lexicon (my7-zeroshot-terms «Phrase lexicon» [x] / [post]
# / [v] lines: the pañhāvāra deeds, the knowledges, the path moments), reviewed word by word: each Pāli word gets the
# part of the text's phrase that carries it, in dictionary form (rule 1 / rule 3 / rule 4). Used after the pi-1 … pi-6
# values (binding where the text has them).
LEXW = {
    "pahīne": "ပယ်ပြီးသော", "vikkhambhite": "ခွာထားပြီးသော", "samudāciṇṇe": "ဖြစ်ခဲ့ဖူးသော", "kilese": "ကိလေသာ",
    "nirodhā": "ချုပ်ငြိမ်းခြင်း သမာပတ်", "vuṭṭhahantassa": "ထမြောက်နေသူ", "duṭṭhena": "ပြစ်မှားသော",
    "assādeti": "သာယာ", "abhinandati": "နှစ်သက်သည်",            # «သာယာ နှစ်သက်သည်» (one «သည်» for two verbs)
    "assādenti": "သာယာ", "abhinandanti": "နှစ်သက်သည်",
    "dānaṃ": "ပေးလှူခြင်း", "datvā": "ပြု၍", "deti": "ပြုသည်",      # «ပေးလှူခြင်းကို ပြု၍ / ပြုသည်»
    "sīlaṃ": "သီလ", "samādiyitvā": "ဆောက်တည်၍", "samādiyati": "ဆောက်တည်သည်",
    "uposathakammaṃ": "ဥပုသ်ကို စောင့်ထိန်းသည်",                  # the act of the compound (T11; karoti then f_karoti)
    "jhānaṃ": "ဈာန်", "uppādeti": "ဖြစ်စေသည်", "vipassanaṃ": "ထိုးထွင်းသိမြင်ခြင်း", "maggaṃ": "မဂ်",
    "abhiññaṃ": "ထူးကဲစွာ သိခြင်း", "samāpattiṃ": "သမာပတ်", "mānaṃ": "မာန", "jappeti": "ဖြစ်ပေါ်စေသည်",
    "diṭṭhiṃ": "အယူ", "gaṇhāti": "စွဲယူသည်", "pāṇaṃ": "သတ္တဝါ", "hanati": "သတ်သည်", "adinnaṃ": "မပေးသည်",
    "ādiyati": "ယူသည်", "musā": "မုသား", "bhaṇati": "ပြောသည်", "pisuṇaṃ": "ကုန်းတိုက်သော စကား",
    "pharusaṃ": "ကြမ်းတမ်းသော စကား", "samphaṃ": "အကျိုးမဲ့ ပြိန်ဖျင်းသော စကား", "palapati": "ပြောသည်",
    "sandhiṃ": "အိမ်", "chindati": "ဖောက်ထွင်းသည်", "harati": "လုယူသည်",
    "ekāgārikaṃ": "အိမ်တစ်လုံးတည်းကို ဝိုင်း၍ တိုက်သည်", "paripanthe": "လမ်းခရီး",
    "paradāraṃ": "သူတစ်ပါး၏ မယား", "gacchati": "သွားသည်",
    "gāmaghātaṃ": "ရွာကို ဖျက်ဆီး၍ လုယက်သည်", "nigamaghātaṃ": "နိဂုံးကို ဖျက်ဆီး၍ လုယက်သည်",
    "mātaraṃ": "အမိ", "pitaraṃ": "အဖ", "arahantaṃ": "ရဟန္တာ", "jīvitā": "အသက်", "voropeti": "သတ်သည်",
    "tathāgatassa": "မြတ်စွာဘုရား", "lohitaṃ": "သွေး", "saṅghaṃ": "သံဃာ", "bhindati": "ဖြိုခွဲသည်",
    "attānaṃ": "မိမိကိုယ်", "pariyiṭṭhimūlakaṃ": "ရှာမှီးခြင်းကို အရင်းခံသော", "dukkhaṃ": "ဆင်းရဲ",
    "paccanubhoti": "ခံစားသည်",
    "aniccato": "မမြဲ", "dukkhato": "ဆင်းရဲ", "anattato": "အတ္တ မဟုတ်",   # pi-5 aniccato «မမြဲ» (rule 1: «ဟု» goes)
    "parihīne": "ဆုတ်ယုတ်သွားသော",
}


# =====================================================================================================================
# presence verifier (the pi-6 check, endings unchanged: pi-1 … pi-5 endings and the pi-6 phase-3 mechanics)
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
    if c.endswith("ပြီးသော") and c[:-3] + " မဟုတ်" in text:
        return "perf-neg"      # pi-6 phase 3 mechanic 5: the negated perfect predicate «Xပြီး မဟုတ်»
    if c.endswith("သည်") and len(c) > 3:
        st = c[:-3]
        if "မ" + st in text:
            return "neg-verb"
        for i in range(0, len(st)):
            if any(st[:i] + "မ" + st[i:] + e in text for e in VERB_FROM):
                return "neg-verb"
        for i in range(1, len(st)):     # pi-6 phase 3: a joined compound verb against its spaced negative
            if st[i - 1] != " " and any(st[:i] + " မ" + st[i:] + e in text for e in VERB_FROM):
                return "neg-verb-sp"
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
    nobr = re.sub(r" ?[\[{][^\]}]*[\]}]", "", text)
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
# frame and stock tables (settled on the sample chapters; see map-table.md for the reasons)
# =====================================================================================================================
# ---- FRAME-BEGIN
# The book frame, particles, link words, the verbs of the frames and the stock notes (my7-zeroshot-terms §1, §4, the
# sample's phrases). Dictionary forms: pi-1 rules 1-11, pi-2 N1-N11, pi-3 M1-M9, pi-4 P1-P8, pi-5 Q1-Q8 / S1-S6 /
# G1-G5, pi-6 R1-R9; the NEW pi-7 rules T1-T12 (map-table.md).
FRAME = {
    NONE: NONE,                                  # a keyword «(no direct equivalent)» of the keyword files
    "ca": NONE, "pana": NONE, "vā": NONE, "ti": NONE, "pi": NONE, "eva": NONE, "yeva": NONE, "siyā": NONE,
    "Namo": "ရှိခိုးသည်", "bhagavato": "မြတ်စွာဘုရား", "arahato": "ရဟန္တာ",        # pi-1 … pi-6 values
    "sammāsambuddhassa": "အမှန်ကို ကိုယ်တိုင် အပြည့်အဝ သိမြင်တော်မူသော ဘုရားရှင်",
    "tassa": ("ထို", NONE), "taṃ": ("ထိုအရာ", "ထို"),                     # the preamble's «ထိုမြတ်စွာဘုရား» (pi-1 … pi-6)
    "Abhidhammapiṭake": "အဘိဓမ္မာပိဋက",          # pi-1 … pi-6 (rule 1: the final «တွင်» goes)
    "Paṭṭhānapāḷi": "အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ",     # rule 7: the book title whole (notes-sample, NEW)
    # link words of the frames (my7-zeroshot-terms §4; pi-1 … pi-6 values): absolutives keep «…၍» (pi-1)
    "paṭicca": "မှီ၍", "nissāya": "မှီ၍", "ārabbha": "အာရုံပြု၍",
    "paccayo": "@paccayo",                       # pi-5 «အကြောင်း» (T3: «paccayena paccayo»)
    "aññamaññaṃ": "အချင်းချင်း",                 # pi-5 aññamañña «အချင်းချင်း»
    "garuṃ": "လေးစားဖွယ်ရာ",                     # «garuṃ katvā» «လေးစားဖွယ်ရာ ပြု၍» (the pi-7 text)
    "kiñci": "အချို့သော", "kāle": "အချိန်",       # «kiñci kāle» «အချို့သော အချိန်၌» (rule 1: «၌» goes)
    # the notes (my7-zeroshot-terms §6, this sample's phrases)
    "saṃkhittaṃ": "အကျဉ်းချုပ်", "Saṃkhittaṃ": "အကျဉ်းချုပ်", "saṃkhittā": "အကျဉ်းချုပ်",
    "vitthāretabbo": "အကျယ် ချဲ့ရမည့်", "vitthāretabbaṃ": "အကျယ် ချဲ့ရမည့်",   # pi-5 vitthāretabbaṃ (rule 3)
    "vitthāretabbā": "အကျယ် ချဲ့ရမည့်",
    "vitthārito": "အကျယ် ချဲ့ထားသော",            # «… ချဲ့ထားသည့်အတိုင်း» (rule 3: the participle «…သော»)
    "vācanāmaggena": "ရွတ်ဆိုသည့် နည်းလမ်း",      # rule 1: the postposition «အတိုင်း» goes
    "sajjhāyamaggena": "သရဇ္ဈာယ်သည့် နည်းလမ်း",
    "asammuyhantena": "မရောထွေးစေဘဲ",            # the text's adverbial «မXဘဲ» (pi-4 P3 / A2)
    "gaṇetabbaṃ": "ရေတွက်ရမည့်",                 # rule 3: a gerundive «…မည့်»
    "evaṃ": ("ထိုနည်းတူ", "ဤသို့"),              # «yathā … evaṃ» / a bare evaṃ (harmonise H14)
    "paṭṭhānavaraṃ": "မြတ်သော အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ",   # the verse «tikañca paṭṭhānavaraṃ dukuttamaṃ»
    "dukuttamaṃ": "နှစ်မျိုးတွဲတို့၏ အမြတ်ဆုံး ဆက်စပ်ပုံ",   # duka-uttama (the inner «တို့၏» stays, rule 1)
    "ekekassa": "တစ်ခုစီ", "padassa": "ပုဒ်",
    "gaṇitā": "ရေတွက်ထားသော",                    # «… ရေတွက်ထားသည့်အတိုင်း» (rule 3, as vitthārito)
    "ātāpeti": "ပူပန်စေသည်", "paritāpeti": "ပြင်းစွာ ပူပန်စေသည်",   # «ပူပန်စေ၍ ပြင်းစွာ ပူပန်စေသည်» (rule 4)
    "natthi": "@natthi",                         # the verb «မရှိ» / the condition «မရှိခြင်း» (f_natthi)
    # adverbs of the anantara / samanantara niddesa (rule 1: «၌» goes); the pi-7 text gives samanantarā the word of
    # its condition (notes-sample point 2)
    "anantarā": "ချက်ချင်း နောက်", "samanantarā": "ကောင်းစွာ ချက်ချင်း နောက်",
    "mūlakaṃ": ("အခြေခံ အကြောင်း", "@prior"),     # the note «(mūlakaṃ saṃkhittaṃ)» «(အခြေခံ အကြောင်းများကို …)»
    "karoti": "@karoti", "katvā": "@katva",
    "yāva": "အထိ",                               # «(yāva X …)» «(Xအထိ …)» (the postposition is the word)
    "ceva": NONE, "cāti": NONE,                   # ca / eva alone (pi-1 rule 9); pīti is the noun (BOOK, fix 2)
    "kātabbā": ("ပြုရမည့်", "ထည့်ရမည့်"), "kātabbaṃ": ("ပြုရမည့်", "ထည့်ရမည့်"),   # rule 3: the gerundive
    "kātabbo": ("ပြုရမည့်", "ထည့်ရမည့်"),         # «(paṭisandhi kātabbā)» «ပဋိသန္ဓေကို ထည့်ရမည်»
    "ninnānākaraṇaṃ": "ကွဲပြားချက် မရှိ",         # «(…၊ ကွဲပြားချက် မရှိ)»
    "vibhajitabbā": "ခွဲခြမ်းစိတ်ဖြာရမည့်", "vibhattā": "ခွဲခြမ်းစိတ်ဖြာထားသော",
    "gaṇanā": "ရေတွက်ချက်", "Gaṇanā": "ရေတွက်ချက်", "gaṇanāpi": "ရေတွက်ချက်",   # notes-sample «gaṇanā ရေတွက်ချက်»
    "anumajjantena": "ပြန်လည် စိစစ်လျက်",          # harmonise H10
}
# Core terms of the book (my7-zeroshot-terms §6, notes-sample «Doctrinal terms»), settled on the sample chapters. A
# tuple = the first value the segment has as a phrase, then the first present by an ending rule, else the pi-1 … pi-6
# value (alt).
_DHAMMA = "သဘောတရား"
_KHANDHA = "အစုအဝေး"
STOCK = {
    **{k: _DHAMMA for k in ("dhammo", "dhammā", "dhammaṃ", "dhamme", "dhammassa", "dhammānaṃ", "dhamma")},
    **{k: _KHANDHA for k in ("khandho", "khandhā", "khandhaṃ", "khandhe", "khandhassa", "khandhānaṃ", "khandha")},
    "rūpaṃ": "@rupam", "rūpānaṃ": "@rupam", "rūpa": "@rupam", "rūpassa": "@rupam",
    **{k: "မူလဓာတ်ကြီး" for k in ("mahābhūtā", "mahābhūtaṃ", "mahābhūte", "mahābhūtānaṃ", "mahābhūtassa")},
    **{k: "စိတ်နှင့် စိတ်၏ အဖော်" for k in ("cittacetasikā", "cittacetasikānaṃ", "cittacetasikaṃ")},
    **{k: "ထိုအရာနှင့် ယှဉ်တွဲသော" for k in ("taṃsampayuttakā", "taṃsampayuttakānaṃ", "taṃsampayuttaka")},
    "taṃsamuṭṭhānānaṃ": "ထိုအရာမှ ဖြစ်ပေါ်လာသော",
    # «-samuṭṭhāna»: the attributive (pi-2 cittasamuṭṭhānā; the text's supplied head noun «ရုပ်» is not part of the
    # keyword, harmonise H8 item 4)
    **{k: "စိတ်မှ ဖြစ်ပေါ်လာသော" for k in ("cittasamuṭṭhānānaṃ", "cittasamuṭṭhānaṃ", "cittasamuṭṭhānā")},
    "arūpino": "ရုပ် မဟုတ်သော", "arūpīnaṃ": "ရုပ် မဟုတ်သော", "Arūpino": "ရုပ် မဟုတ်သော",   # pi-5 arūpino
    "rūpino": "ရုပ် ဖြစ်သော", "rūpīnaṃ": "ရုပ် ဖြစ်သော", "Rūpino": "ရုပ် ဖြစ်သော",          # pi-1 rūpino dhammā
    **{k: "မူလဓာတ်ကြီးတို့ကို မှီ၍ ဖြစ်သော ရုပ်" for k in ("upādārūpānaṃ", "upādārūpaṃ", "upādārūpā")},  # pi-5
    **{k: "ကံ ပြုခဲ့သောကြောင့် ဖြစ်သော ရုပ်" for k in ("kaṭattārūpānaṃ", "kaṭattārūpaṃ", "kaṭattārūpā")},
    "kaṭattā": "ကံ ပြုခဲ့သောကြောင့်",           # «kaṭattā ca rūpānaṃ» (my7 FIXED)
    # moments and planes (harmonise B1 of pi-6: «… ခဏ» without the final «၌», rule 1)
    "okkantikkhaṇe": "သန္ဓေ သက်ဆင်းသော ခဏ", "paṭisandhikkhaṇe": "ပဋိသန္ဓေ နေသော ခဏ",
    "ahetukapaṭisandhikkhaṇe": "အမြစ် မရှိသော ပဋိသန္ဓေ နေသော ခဏ",
    "arūpe": "ရုပ်မရှိသော ဘုံ",                   # pi-6 R5 (rule 1: «၌» goes)
    "vatthuṃ": "မှီရာ ဝတ္ထု", "vatthu": "မှီရာ ဝတ္ထု",   # pi-5 vatthuṃ
    "purimā": "ရှေးရှေး", "pacchimānaṃ": "နောက်နောက်",   # the pi-5 rails «ရှေးရှေး … နောက်နောက်»
    "sampayuttakānaṃ": "ယှဉ်တွဲသော", "sampayuttā": "ယှဉ်တွဲသော", "sampayuttakā": "ယှဉ်တွဲသော",
    "sampayutto": "ယှဉ်တွဲသော", "sampayuttaṃ": "ယှဉ်တွဲသော",
    **{k: ("ကံ၏ အကျိုး ဖြစ်သော", "ကံ၏ အကျိုး") for k in ("vipāko", "vipākā", "vipākānaṃ", "vipākaṃ", "vipākassa")},
    "kusalākusalaṃ": "ကုသိုလ်နှင့် အကုသိုလ်",       # pi-5 kusalākusale (my7 FIXED «… ကံ»)
    "kammaṃ": "ကံ",
    "kabaḷīkāro": "လုတ်ပြု၍ စားရသော", "āhāro": "အာဟာရ",   # pi-1 kabaḷīkāro āhāro
    "imassa": "ဤ", "kāyassa": "ကိုယ်",            # «imassa kāyassa» «ဤကိုယ်»
    "jhānaṅgāni": "ဈာန်၏ အင်္ဂါ", "maggaṅgāni": "မဂ်၏ အင်္ဂါ",
    "cetanā": "စေ့ဆော်မှု", "Cetanā": "စေ့ဆော်မှု",
    "pacchājātā": "နောက်မှ ဖြစ်ပေါ်သော",
    "samanantaraniruddhā": "ချက်ချင်း ချုပ်ငြိမ်းပြီးသော", "samanantaravigatā": "ချက်ချင်း ပျောက်ကွယ်ပြီးသော",
    "paṭuppannānaṃ": "ပစ္စုပ္ပန်",
    "sabbe": "အားလုံး",
    # the pañhāvāra lexicon where a pi-1 … pi-6 value stands in the segment only inside ANOTHER phrase (map-table.md,
    # «values different from pi-1 … pi-6»)
    "maggaṃ": ("မဂ်", "လမ်း"), "samāpattiṃ": ("သမာပတ်", "@prior"), "deti": ("ပြုသည်", "@prior"),
    "nillopaṃ": ("ဥစ္စာ", "@prior"), "tiṭṭhati": ("ဓားပြ တိုက်သည်", "@prior"),
    # the kamma kinds «Sahajātā – / Nānākkhaṇikā –» (harmonise H7): the adjective (rule 3); the text's head noun «ကံ»
    # is the frame's addition, not part of the keyword
    "sahajātā": ("အတူ ပေါ်ပေါက်သော", "@prior"), "nānākkhaṇikā": ("ခဏ ကွဲပြားသော", "@prior"),
    **{k: "နိဗ္ဗာန်" for k in ("nibbānaṃ", "nibbānassa", "nibbāne", "nibbāna", "Nibbānaṃ")},   # burmese-style core
    # T11 / U2: the whole act; where …pe… cuts the verb off, the text's noun «ဥပုသ် စောင့်ထိန်းခြင်း» (g2, coordinator)
    # where it has it, else the bare noun
    "uposathakammaṃ": ("ဥပုသ်ကို စောင့်ထိန်းသည်", "ဥပုသ် စောင့်ထိန်းခြင်း", "ဥပုသ်"),
    "parikammaṃ": "ကြိုတင် ပြင်ဆင်မှု",          # «ပထမ ဈာန်၏ ကြိုတင် ပြင်ဆင်မှု» (1-01)
    "kiriyaṃ": ("ပြုရုံမျှသာ ဖြစ်သော", "@prior"),    # pi-1 … pi-6 (rule 3); the text's head noun «စိတ်» is its addition
    **{k: "ပဋိသန္ဓေ" for k in ("paṭisandhi", "paṭisandhiṃ", "paṭisandhiyā", "Paṭisandhi")},   # notes-sample
    "ekāgārikaṃ": ("အိမ်တစ်လုံးတည်းကို ဝိုင်း၍ တိုက်သည်", "အိမ်တစ်လုံးတည်း"),
    # ---- phase 3 fix 4: noupādā = T8 na-X of the pi-1 … pi-3 upādā «မူလဓာတ်ကြီးများကို မှီ၍ ဖြစ်သော» (the positive
    # upādā keeps that value; the module had taken the pi-5 «မှီ၍» of another kind of segment)
    **{k: "မူလဓာတ်ကြီးများကို မှီ၍ ဖြစ်သည် မဟုတ်သော" for k in ("noupādā", "Noupādā")},
    # ---- phase 3 fix 3: tadārammaṇatā is the text's phrase, one value per form the text has (1-01 «… အာရုံပြုသည့်
    # အနေဖြင့်», 1-03 … «… အာရုံပြုသော အဖြစ်ဖြင့်»; rule 1: «ဖြင့်» goes); the head noun «စိတ်သည်» of vipāko, which the
    # module had read from a concatenated generator string, is not the keyword's
    "tadārammaṇatā": ("ထိုအာရုံကို အာရုံပြုသည့် အနေ", "ထိုအာရုံကိုပင် အာရုံပြုသော အဖြစ်"),
    # ---- phase 3 (fix 1, word boundaries): two keywords the text writes as one word keep their own part, «dibbena
    # cakkhunā» «နတ်မျက်စိဖြင့်», «dibbāya sotadhātuyā / dibbassa sotassa» «နတ်နား …» (pi-1 … pi-6 «နတ်»; logged in
    # map-harmonise-notes §B as the boundary exception); cakkaṃ is the text's «(စက်ဝိုင်း)» (coordinator fix 1)
    **{k: "နတ်" for k in ("dibbena", "dibbaṃ", "dibbassa", "dibbāya", "dibbā", "dibbo")},
    **{k: "စက်ဝိုင်း" for k in ("cakkaṃ", "cakkā", "cakkāni")},
}
# ---- BOOK (phase 3): the agreed phase-2 overrides and group values that hold beyond one segment, the coordinator's
# dictionary forms (fix 9) and decisions. Same use as FRAME (a value is taken only where the segment has it; a tuple =
# the first value the segment has as a phrase). phase3-changes.tsv gives the reason of every value that changed.
_KIRIYA = "ပြုရုံမျှသာ ဖြစ်သော"
_VINNANANCA = "အဆုံး မရှိသော သိစိတ် နယ်ပယ်"
_NEVASANNA = "မှတ်သိမှု ရှိသည်လည်း မဟုတ် မှတ်သိမှု မရှိသည်လည်း မဟုတ်သော နယ်ပယ်"
_DLS = "အယူမှားနှင့် ကင်းကွာသော လောဘနှင့်အတူ ဖြစ်သော"        # g3 G3 / g4 G3 (rule 6: the «၊» goes)
_PARIPUNNA = ("ပြည့်စုံသော", "ပြည့်စုံစွာ")                       # fix 9 paripuṇṇo «ပြည့်စုံသော»; the text's adverb (g2)


def _sad(x):
    """an X-sadisa note (T5; g4 G1 / g5 G5-1): «Xနှင့် တူသည်», else the text's adverbial «Xနှင့် တူအောင်»."""
    return (x + "နှင့် တူသည်", x + "နှင့် တူအောင်")


BOOK = {
    # coordinator fix 2: pīti is the noun «ပီတိ», not pi + iti (g4)
    "pīti": "ပီတိ",
    # coordinator fix 9: dictionary forms book-wide (g1 … g4 overrides)
    **{k: "ရေတွက်ရမည့်" for k in ("gaṇetabbā", "gaṇetabbāni", "gaṇetabbo")},
    "vitthāretabbāni": "အကျယ် ချဲ့ရမည့်",
    "uppādenti": "ဖြစ်စေသည်",
    "vipassanti": "ထိုးထွင်း၍ ရှုသည်",
    "bhāgo": "အပိုင်း",
    **{k: "သိစိတ် ငါးပါး" for k in ("pañcaviññāṇaṃ", "Pañcaviññāṇaṃ")},
    **{k: _PARIPUNNA for k in ("paripuṇṇo", "paripuṇṇā", "paripuṇṇaṃ", "Paripuṇṇaṃ")},
    # coordinator decisions on the unclear points
    "naviññeyyo": "@naviñ", "naviññeyyaṃ": "@naviñ",       # the text's lexical negative «မသိနိုင်သော» (g3 / g5)
    "gaṇite": "ရေတွက်သော", "gahite": "ယူသော",                       # locative absolutes, «အခါ» goes (g1 / g2)
    "ṭhitena": "တည်၍", "gambhīrā": "နက်နဲ",                          # g1
    "kāraṇena": ("နည်းလမ်း", "အကြောင်း"),                           # g2: «iminā kāraṇena» «ဤနည်းလမ်းဖြင့်»
    "dassitanayena": "ပြထားသော နည်းအတိုင်း",                         # g2: «အတိုင်း» where the text has it
    "gāmaghātaṃ": ("ရွာကို ဖျက်ဆီး၍ လုယက်သည်", "ရွာ"),               # U2; the bare «ရွာ» before …pe… (g4)
    # nevadassanena: one form book-wide, the text's «သစ္စာကို မြင်ခြင်းဖြင့်လည်း ပယ်ရမည် မဟုတ်၊» (g2 G2-2, g5, g6)
    "nevadassanena": "သစ္စာကို မြင်ခြင်း … မဟုတ်", "Nevadassanena": "သစ္စာကို မြင်ခြင်း … မဟုတ်",
    # agreed phase-2 overrides (notes-g1 … notes-g6 «Module overrides»)
    "niyatamicchādiṭṭhi": "ကျိန်းသေသော မှားယွင်းသော အယူ", "niyatamicchādiṭṭhiyā": "ကျိန်းသေသော မှားယွင်းသော အယူ",
    "kusale": "ကုသိုလ်",                     # rule 5: «သဘောတရား» belongs to the dhamma keyword (g1, g2, g6)
    "paccavekkhitvā": ("ပြန်လည် ဆင်ခြင်၍", "@prior"),               # U3: the pi-7 word of paccavekkhati (g3, g4)
    **{k: "အတွင်းပိုင်း" for k in ("ajjhattikassa",)},             # g4 (fix 1: pi-2 «အတွင်း» is part of the word)
    # group values that recur in several groups (one value per term)
    "asammohantena": "မရောထွေးစေဘဲ", "Asammohantena": "မရောထွေးစေဘဲ",
    "atthappaṭisambhidāya": "အကျိုးအနက်ကို ပိုင်းခြားသိသော ဉာဏ်",
    "dhammappaṭisambhidāya": "တရားကို ပိုင်းခြားသိသော ဉာဏ်",
    "niruttippaṭisambhidāya": "စကားဖြင့် ဖော်ပြမှုကို ပိုင်းခြားသိသော ဉာဏ်",
    "paṭibhānappaṭisambhidāya": "ဉာဏ်ပေါ်မှုကို ပိုင်းခြားသိသော ဉာဏ်",
    "ṭhānāṭhānakosallassa": ("ဖြစ်နိုင်ခြင်းနှင့် မဖြစ်နိုင်ခြင်း၌ ကျွမ်းကျင်ခြင်း",
                             "ဖြစ်နိုင်သော အကြောင်းနှင့် မဖြစ်နိုင်သော အကြောင်း၌ ကျွမ်းကျင်မှု"),   # two text forms (§A)
    "suciṇṇāni": ("ကောင်းစွာ ကျင့်ခဲ့ဖူးသော", "ကောင်းစွာ ပြုခဲ့ဖူးသော"),   # rule 3 (the text's «…ပြုခဲ့ဖူးသည်တို့»)
    "paṭighātatthāya": "ချေဖျက်ရန်",
    "bandhitabbaṃ": "ဖွဲ့ရမည့်", "kātabbāni": "ပြုရမည့်",
    **{k: "သတ်မှတ်ရမည့်" for k in ("niyāmetabbaṃ", "niyāmetabbā", "niyāmetabbāni")},
    **{k: "ထုတ်နုတ်ရမည့်" for k in ("uddharitabbā", "uddharitabbaṃ", "uddharitabbo")},
    **{k: "ပြသရမည့်" for k in ("dassetabbo", "dassetabbaṃ", "dassetabbāni")},
    "cakkhusampadaṃ": "မျက်စိ ပြည့်စုံခြင်း", "sotasampadaṃ": "နား ပြည့်စုံခြင်း", "ghānasampadaṃ": "နှာခေါင်း ပြည့်စုံခြင်း",
    "vaṇṇasampadaṃ": "အဆင်းအရောင် ပြည့်စုံခြင်း", "saddasampadaṃ": "အသံ ပြည့်စုံခြင်း",
    "gandhasampadaṃ": "အနံ့ ပြည့်စုံခြင်း", "rasasampadaṃ": "အရသာ ပြည့်စုံခြင်း",
    "phoṭṭhabbasampadaṃ": "အထိအတွေ့ ပြည့်စုံခြင်း",
    "ekasadisā": "တူညီသည်", "ekasadisāni": "တူညီသည်",
    "garukārammaṇā": "လေးစားဖွယ်ရာ အာရုံ",
    "kiriyasamāpattiṃ": f"{_KIRIYA} သမာပတ်",
    "passitvā": "ကြည့်၍",
    "pañcāyatanāni": "အာရုံခံ နယ်ပယ် ငါးပါး", "Pañcāyatanāni": "အာရုံခံ နယ်ပယ် ငါးပါး",
    "sakabhaṇḍe": "မိမိ ပစ္စည်း", "Sakabhaṇḍe": "မိမိ ပစ္စည်း",
    "upanissayā": "အားကြီးသော အမှီ",                                # g3 G5 / g4 G4: «(tīṇi upanissayā)» the kinds
    "utu": "ရာသီဥတု", "Utu": "ရာသီဥတု",
    "viññāṇañcāyatanakiriyassa": f"{_VINNANANCA} {_KIRIYA}",
    "viññāṇañcāyatanavipākassa": f"{_VINNANANCA} ကံ၏ အကျိုး",
    "nevasaññānāsaññāyatanakiriyaṃ": f"{_NEVASANNA} {_KIRIYA}",
    "āmasanaṃ": "ရည်ညွှန်းပုံ", "āmasanā": "ရည်ညွှန်းပုံ",
    **{k: ("ဘဝ ဖြစ်စဉ် … ပဋိသန္ဓေ", "ဘဝ ဖြစ်ဆဲ ကာလ … ပဋိသန္ဓေ") for k in ("pavattipaṭisandhi", "pavattipaṭisandhiyā")},
    **{"diṭṭhigatavippayuttalobhasahagat" + e: _DLS for e in ("aṃ", "e", "ā", "ānaṃ", "o", "assa", "ena", "a")},
    "diṭṭhigatavippayuttalobhasahagatādhipati": _DLS + " အကြီးအမှူး",
    "lokiyadukasadisaṃ": _sad("လောကနှင့် သက်ဆိုင်ခြင်း နှစ်မျိုးတွဲ"),
    "sappaccayadukasadisaṃ": _sad("အကြောင်း ရှိခြင်း နှစ်မျိုးတွဲ"),
    "sappītikadukasadisaṃ": _sad("ပီတိ ရှိခြင်း နှစ်မျိုးတွဲ"),
    "dutiyagamanasadisaṃ": _sad("ဒုတိယ သွားပုံ"),
    # sekkha / asekkha (coordinator, g2): a qualifier «…၏» (the binding pi-1 / pi-2 value), a person noun bare
    **{k: "@sekkha" for k in ("sekkho", "sekkhaṃ", "sekkhassa", "sekkhe", "sekkhā", "sekkhānaṃ", "sekkhañca",
                              "sekkhāya", "asekkho", "asekkhaṃ", "asekkhassa", "asekkhe", "asekkhā", "asekkhānaṃ",
                              "asekkhañca", "asekkhāya")},
    # phase 3 scan alignments (one value per term; map-harmonise-notes §B)
    "suddhake": "ရိုးရိုး",                  # the text's head noun «အပိုင်း» is its addition (A5; g4 against g3)
    "arūpāvacare": ("ရုပ်မရှိသော ဘုံနှင့် ဆိုင်သော", "@prior"),   # «arūpāvacare khandhe» as the other arūpāvacara- forms
    "vipākassa": "@vipakassa",               # the noun after «kammaṃ», else the triad adjective (phase 1 §B)
}
FRAME.update(BOOK)          # BOOK wins over the phase-1 FRAME (paripuṇṇaṃ, suciṇṇāni: the tuples of the text's forms)
# ---- FRAME-END


# =====================================================================================================================
# Paṭṭhāna families (pi-7 rules T1-T10; see map-table.md)
# =====================================================================================================================
# ---- T1: the 24 conditions: stem -> N, the bare name (my7_formulas.CONDS, the FINAL pi-7 text; pi-5 rails values)
CONDS = [
    ("hetu", "အမြစ်"), ("ārammaṇa", "အာရုံ"), ("adhipati", "အကြီးအမှူး"),
    ("anantara", "ချက်ချင်း နောက်၌ ဖြစ်စေခြင်း"), ("samanantara", "ကောင်းစွာ ချက်ချင်း နောက်၌ ဖြစ်စေခြင်း"),
    ("sahajāta", "အတူ ပေါ်ပေါက်ခြင်း"), ("aññamañña", "အချင်းချင်း ထောက်ပံ့ခြင်း"), ("nissaya", "အမှီ"),
    ("upanissaya", "အားကြီးသော အမှီ"), ("purejāta", "ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်း"),
    ("pacchājāta", "နောက်မှ ဖြစ်ပေါ်ခြင်း"), ("āsevana", "အလေ့အကျင့် ပြုခြင်း"), ("kamma", "ကံ"),
    ("vipāka", "ကံ၏ အကျိုး"), ("āhāra", "အာဟာရ"), ("indriya", "စွမ်းရည်"), ("jhāna", "ဈာန်"), ("magga", "မဂ်"),
    ("sampayutta", "ယှဉ်တွဲခြင်း"), ("vippayutta", "ကင်းကွာခြင်း"), ("atthi", "ရှိခြင်း"), ("natthi", "မရှိခြင်း"),
    ("vigata", "ပျောက်ကွယ်ခြင်း"), ("avigata", "မပျောက်ကွယ်ခြင်း"),
]
N = dict(CONDS)
PACCAYA = "အကြောင်း"                              # pi-5 paccayo (^5-717)
NOT = "မဟုတ်"
# the counting locatives (Xe / Xyā) and the Pāli negative prefix of each condition
LOC = {s[:-1] + "e": s for s in N if s not in ("hetu", "adhipati", "atthi", "natthi")}
LOC.update({"hetuyā": "hetu", "adhipatiyā": "adhipati", "atthiyā": "atthi", "natthiyā": "natthi"})
_STEMS = sorted(N, key=len, reverse=True)


def cname(stem, neg=False):
    """T1: the name «Nဟူသော အကြောင်း», negative «Nဟူသော အကြောင်း မဟုတ်ခြင်း» (my7_formulas cond())."""
    return f"{N[stem]}ဟူသော {PACCAYA}" + (f" {NOT}ခြင်း" if neg else "")


def cabl(stem, neg=False):
    """T2: the ablative Xpaccayā «Nဟူသော အကြောင်းကြောင့်» (pi-2 «Xကြောင့်»: the cause marker is the keyword's own
    meaning and stays); negative «… ကြောင့် မဟုတ်» (pi-1 rule 9 «… မဟုတ်»; the adverbial «ဘဲ» goes, rule 6)."""
    return f"{N[stem]}ဟူသော {PACCAYA}ကြောင့်" + (f" {NOT}" if neg else "")


def split_neg(w):
    """'naārammaṇa…' -> (True, 'ārammaṇa…'); 'nonatthi…' -> (True, 'natthi…'); 'nādhipati' -> (True, 'adhipati');
    a stem that itself starts with «n» (natthi, nissaya) stays positive."""
    for pre in ("no", "na"):
        r = w[len(pre):]
        if w.startswith(pre) and (any(r.startswith(s) for s in _STEMS) or r in LOC or r[:-2] in LOC):
            return True, r
    if w.startswith("n") and len(w) > 2 and w[1] in "āeo" and any(("a" + w[2:]).startswith(s) for s in _STEMS):
        return True, "a" + w[2:]               # contracted na + a- («nādhipati»)
    if w.startswith("n") and any(w[1:].startswith(s) for s in _STEMS if s[0] in "aāu"):
        return True, w[1:]                     # «nāsevana», «nupanissaya»
    return False, w


# Pāli tails after «paccay» -> form
PACCAY_TAIL = [("opi", "n"), ("oti", "n"), ("o", "n"), ("aṃ", "n"), ("ena", "i"), ("ā", "ab"), ("āti", "ab"),
               ("assa", "n"), ("e", "n"), ("ādi", "adi"), ("ādayo", "adi"), ("ānaṃ", "n"), ("a", "bare")]
# other suffixes of a condition stem (headings and notes; my7-zeroshot-terms §2, the text's heading parts)
COND_SUF = [("paccayavāro", "vara"), ("paccayavāre", "vara"), ("mūlakaṃ", "mula"), ("mūlakādi", "mulaadi"),
            ("mūlakā", "mula"), ("mūlake", "mula"), ("dukaṃ", "duka"), ("dukāni", "dukas"), ("ādidukāni", "adidukas"),
            ("ādidukaṃ", "adiduka"), ("sabhāgaṃ", "sabhaga"), ("ādisabhāgaṃ", "adisabhaga"), ("ghaṭanā", "ghatana"),
            ("ghaṭanāya", "ghatana"), ("paccayasadisaṃ", "sadisa"), ("paccayasadisā", "sadisa"),
            ("paccayasadiso", "sadisa"), ("sadisaṃ", "bsadisa"), ("sadisā", "bsadisa"), ("sadiso", "bsadisa"),
            ("nti", "bare"), ("ti", "bare"), ("ñca", "bare"), ("mpi", "bare"), ("ṃ", "bare")]


def cond_parse(kw):
    """the condition reading of a keyword -> (neg, stem, form) or None. form: n name, ab ablative, i instrumental, loc
    counting locative, bare (ghaṭanā / hyphen compound), adi, vara, mula, duka, sabhaga, ghatana, sadisa …"""
    w = low(kw.strip("()"))
    for neg, r in ((False, w), split_neg(w)):
        p = _cond_parse(neg, r)
        if p:
            return p
    return None


def _cond_parse(neg, r):
    for s in _STEMS:
        if not r.startswith(s):
            continue
        rest = r[len(s):]
        if rest == "":
            return neg, s, "bare"
        if rest.startswith("paccay"):
            t = rest[len("paccay"):]
            for e, f in PACCAY_TAIL:
                if t == e:
                    return neg, s, f
        for e, f in COND_SUF:
            if rest == e:
                return neg, s, f
    if r in LOC:
        return neg, LOC[r], "loc"
    if r.endswith(("pi", "ñca")) and r[:-2] in LOC:
        return neg, LOC[r[:-2]], "loc"
    return None


def compound_form(kw, pali):
    """the frame of a hyphen-compound part (T4): the Pāli word that contains the keyword as a part decides the case of
    the whole compound: «…-Xpaccayā» ablative (body) / name (heading), «…-Xnti» / «…-X ghaṭanā» bare (ghaṭanā list)."""
    k = re.escape(low(kw))
    for m in re.finditer(r"[\w" + PW + r"-]*-?" + k + r"(?:-[\w" + PW + r"]+)*", low(strip_brackets(pali))):
        tok = m.group(0)
        if "-" not in tok:
            continue
        last = tok.rsplit("-", 1)[1]
        if last.endswith("paccayā") or last.endswith("paccayāti"):
            return "ab"
        if last.endswith("paccayo") or last.endswith("paccayaṃ"):
            return "n"
        if last.endswith(("nti", "ti", "ghaṭanā")):
            return "bare"
    return None


_SA = re.compile(r"^s(?:a|ā)(" + "|".join(sorted((s[1:] if s[0] in "aā" else s) for s in N)) + r")(aṃ|ā|o)?$")


def sa_cands(kw):
    """T4: «sa-X» (with the condition X) «(saupanissayaṃ)» = «Nဟူသော အကြောင်း ပါဝင်သော» (my7-zeroshot-terms §2); in a
    hyphen compound «Saindriya-maggaghaṭanā» the text closes the whole compound with one «ပါဝင်သော»: «… … ပါဝင်သော»
    (rule 10)."""
    m = _SA.match(low(kw))
    if not m:
        return None
    x = m.group(1)
    st = next((s for s in N if s == x or (s[0] in "aā" and s[1:] == x)), None)
    if st is None:
        return None
    nm = cname(st)
    return [f"{nm} ပါဝင်သော", f"{nm} … ပါဝင်သော"]


def cond_cands(kw, pali, heading=False):
    """T1-T4: the candidate values of a condition keyword, in order (the engine takes the first the text has). Phase 3
    (g3 override Nahetuṃ, book-wide): a bare «-ṃ / -u» form that the Pāli follows with «dhamma-» (also with one term
    between: «Nahetuṃ akusalaṃ dhammaṃ») is the dyad term, not the condition: no condition value."""
    p = cond_parse(kw)
    if not p:
        return sa_cands(kw)
    neg, s, f = p
    if f == "bare" and re.search(r"(?<![\w" + PW + r"-])" + re.escape(low(kw)) + r"(?:\s+[a-zāīūṃṅñṭḍṇḷ]+)?\s+dhamm",
                                 low(strip_brackets(pali))):
        return None
    nm, ab = cname(s, neg), cabl(s, neg)
    bare = N[s] + (f" {NOT}ခြင်း" if neg else "")
    if f == "bare":
        cf = "n" if heading else compound_form(kw, pali)
        if cf == "ab":
            return [ab, nm, bare]
        if cf == "n":
            return [nm, bare, ab]
        return [bare, nm, ab]
    if f == "n":
        return [nm, bare]
    if f == "i":
        return [nm]                    # pi-5 hetupaccayena «အမြစ်ဟူသော အကြောင်း» (the instrumental «ဖြင့်» goes)
    if f == "ab":
        return [ab, nm, bare] if not heading else [nm, ab, bare]   # a heading names the condition(s)
    if f == "loc":
        return [nm, bare]              # T2: the counting locative «Nဟူသော အကြောင်း၌ K» (rule 1: «၌» goes)
    if f == "adi":
        return [f"{nm} စသည်"]
    if f == "vara":
        return [f"{nm}အလိုက် ဖော်ပြချက်"]
    if f == "mula":
        return [f"{nm}ကို အခြေခံခြင်း", f"{nm}ကို အခြေခံသော"]
    if f == "mulaadi":
        return [f"{nm}ကို အခြေခံခြင်း စသည်"]
    if f == "duka":
        return [f"{nm}၏ နှစ်မျိုးတွဲ"]
    if f == "dukas":
        return [f"{nm}၏ နှစ်မျိုးတွဲ"]
    if f == "adidukas":
        return [f"{nm} စသည်တို့၏ နှစ်မျိုးတွဲ"]
    if f == "adiduka":
        return [f"{nm} စသည်တို့၏ နှစ်မျိုးတွဲ"]
    if f == "sabhaga":
        return [f"{nm}နှင့် တွဲဖက်သည်"]
    if f == "adisabhaga":
        return [f"{nm} စသည်တို့နှင့် တွဲဖက်သည်"]
    if f == "ghatana":
        return [f"{nm}၏ ပေါင်းစပ်ချက်", f"{nm} ပါဝင်သော ပေါင်းစပ်ချက်"]
    if f == "sadisa":
        return [f"{nm}နှင့် တူသည်", f"{bare}နှင့် တူသည်", f"{nm}နှင့် တူအောင်", f"{bare}နှင့် တူအောင်"]
    if f == "bsadisa":                 # harmonise H19: a bare X-sadisa = the bare name
        return [f"{bare}နှင့် တူသည်", f"{nm}နှင့် တူသည်", f"{bare}နှင့် တူအောင်", f"{nm}နှင့် တူအောင်"]
    return None


# ---- T5: vāra names and the orders
VARA = {"paṭicca": "မှီ၍ ဖြစ်ပေါ်ခြင်း", "sahajāta": "အတူ ပေါ်ပေါက်ခြင်း", "paccaya": "အကြောင်းပြု၍ ဖြစ်ပေါ်ခြင်း",
        "nissaya": "အမှီပြု၍ ဖြစ်ပေါ်ခြင်း", "saṃsaṭṭha": "ရောနှောခြင်း", "sampayutta": "ယှဉ်တွဲခြင်း",
        "pañhā": "ပြဿနာ", "pucchā": "အမေး", "vibhaṅga": "ခွဲခြမ်းစိတ်ဖြာခြင်း", "saṅkhyā": "ရေတွက်ခြင်း",
        "hetupaccaya": "အမြစ်ဟူသော အကြောင်း"}             # my7-zeroshot-terms §2 (notes-sample «Sections»)
VARA_END = [("vāro", ""), ("vāraṃ", ""), ("vāre", ""), ("vārepi", ""), ("vārampi", ""), ("vāropi", ""),
            ("vārassa", ""), ("vārena", ""), ("vārā", ""), ("vāra", ""), ("vārādi", " စသည်"),
            ("vārasadisaṃ", "နှင့် တူသည်"), ("vārasadisā", "နှင့် တူသည်"), ("vārasadiso", "နှင့် တူသည်"),
            ("vārasadisanti", "နှင့် တူသည်")]
_VARA = re.compile(r"^(" + "|".join(sorted(VARA, key=len, reverse=True)) + r")(" +
                   "|".join(re.escape(e) for e, _ in sorted(VARA_END, key=lambda x: -len(x[0]))) + r")$")


def vara_cands(kw):
    """T5: a vāra name in any case = «Xအလိုက် ဖော်ပြချက်» (pi-2 / pi-6 «…အလိုက် ဖော်ပြချက်»; rule 1: the case particle
    and the «လည်း» of -pi go, Q4); -ādi «… စသည်»; -sadisa «…နှင့် တူသည်» (rule 4; the text's «တူကြသည်» by the ending
    rule, harmonise H24)."""
    m = _VARA.match(low(kw))
    if not m:
        return None
    tail = dict(VARA_END)[m.group(2)]
    v = f"{VARA[m.group(1)]}အလိုက် ဖော်ပြချက်"
    if tail == "နှင့် တူသည်":           # the text's adverbial «…နှင့် တူအောင်» before «ပြုရမည် / ချဲ့ရမည်» (pi-6 g1)
        return [v + tail, v + "နှင့် တူအောင်"]
    return [v + tail]


def vara_part(kw, pali):
    """phase 3 (fix 1): the keyword is a part of a hyphen-compound vāra name «Sahajāta-paccaya-nissaya-…-sampayuttavāro»
    (the part is the vāra «Xအလိုက်» member: VARA[kw], «အကြောင်းပြု၍ ဖြစ်ပေါ်ခြင်း»)."""
    k = re.escape(low(kw))
    for m in re.finditer(r"[\w" + PW + r"-]*(?<![\w" + PW + r"])" + k + r"-[\w" + PW + r"-]*vār[\w" + PW + r"]*",
                         low(strip_brackets(pali))):
        return True
    return False


ORDER = {"anuloma": "အဟုတ်ပြ ပုံစံ", "paccanīya": "အငြင်းပြ ပုံစံ", "paccanīka": "အငြင်းပြ ပုံစံ",
         "anulomapaccanīya": "အဟုတ်ပြ အငြင်းပြ ပုံစံ", "paccanīyānuloma": "အငြင်းပြ အဟုတ်ပြ ပုံစံ"}
ORDER_PRE = {"": "", "paccay": "အကြောင်း ", "dhamm": "သဘောတရား "}
ORDER_END = {"aṃ": "", "e": "", "ampi": "", "ena": "", "assa": "", "a": "", "ādi": " စသည်", "āni": "",
             "agaṇanā": "၏ ရေတွက်ချက်", "agaṇanāya": "၏ ရေတွက်ချက်", "aṃ.": ""}
ORDER_END.update({"amātikā": "၏ ခေါင်းစဉ်စာရင်း", "amātikaṃ": "၏ ခေါင်းစဉ်စာရင်း"})
_ORDER = re.compile(r"^(x)?[aāp]?(nulomapaccanīy|accanīyānulom|nulom|accanīy|accanīk)(" +
                    "|".join(sorted((re.escape(e) for e in ORDER_END), key=len, reverse=True)) + r")$")


def order_cands(kw):
    """T5: anuloma / paccanīya (pi-6 «အဟုတ်ပြ / အငြင်းပြ ပုံစံ»; notes-sample «Sections and orders»): Paccayānulomaṃ
    «အကြောင်း အဟုတ်ပြ ပုံစံ», Dhammānulome «သဘောတရား အဟုတ်ပြ ပုံစံ» (rule 1: «၌» goes); then the mind moment anuloma
    «လျော်ညီခြင်း စိတ်» (harmonise H1), which f_anuloma chooses by the Pāli."""
    w = low(kw)
    pk, rest = "", w
    for p_ in ("paccay", "dhamm"):
        if w.startswith(p_) and len(w) > len(p_) + 4 and w[len(p_)] in "aā":
            r = w[len(p_):]
            r = "a" + r[1:] if r.startswith("ā") else r[1:]       # dhamm-ā-nuloma / dhamma-paccanīya
            if r.startswith(("anulom", "paccanīy", "paccanīk")):
                pk, rest = p_, r
                break
    m = _ORDER.match(rest)
    if not m or m.group(1):
        return None
    if not rest.startswith(("anu", "pacc")):
        return None
    pre = ORDER_PRE[pk]
    mid = {"nulomapaccanīy": "အဟုတ်ပြ အငြင်းပြ ပုံစံ", "accanīyānulom": "အငြင်းပြ အဟုတ်ပြ ပုံစံ",
           "nulom": "အဟုတ်ပြ ပုံစံ", "accanīy": "အငြင်းပြ ပုံစံ", "accanīk": "အငြင်းပြ ပုံစံ"}[m.group(2)]
    return [pre + mid + ORDER_END[m.group(3)]]


# ---- T6: counts (answers «… ခု»; khandha / mahābhūta «… ပါး»), counting groups «Nမျိုးတွဲ»
NUM_VAL = {"eka": 1, "ekaṃ": 1, "eko": 1, "ekassa": 1, "ekā": 1, "ekena": 1, "dve": 2, "dvinnaṃ": 2, "dvīhi": 2,
           "dvīsu": 2, "tīṇi": 3, "tayo": 3, "tiṇṇaṃ": 3, "tīhi": 3, "tīsu": 3, "tisso": 3, "tiṇṇannaṃ": 3,
           "cattāri": 4, "cattāro": 4, "catunnaṃ": 4, "catūhi": 4, "catūsu": 4, "pañca": 5, "pañcannaṃ": 5,
           "cha": 6, "satta": 7, "aṭṭha": 8, "nava": 9, "dasa": 10, "ekādasa": 11, "dvādasa": 12, "bārasa": 12,
           "terasa": 13, "cuddasa": 14, "catuddasa": 14, "pannarasa": 15, "pañcadasa": 15, "soḷasa": 16,
           "sattarasa": 17, "aṭṭhārasa": 18, "ekūnavīsati": 19, "vīsati": 20, "ekavīsati": 21, "bāvīsati": 22,
           "dvāvīsati": 22, "tevīsati": 23, "catuvīsati": 24}
MY_NUM = {1: "တစ်", 2: "နှစ်", 3: "သုံး", 4: "လေး", 5: "ငါး", 6: "ခြောက်", 7: "ခုနစ်", 8: "ရှစ်", 9: "ကိုး",
          10: "ဆယ်"}


def my_num(n):
    """the Burmese number word (my7_formulas NUMW; the text's «ဆယ့်… / နှစ်ဆယ့်… / သုံးဆယ့်…»)."""
    if n <= 10:
        return MY_NUM[n]
    t, u = divmod(n, 10)
    head = "" if t == 1 else MY_NUM[t]
    return head + ("ဆယ်" if u == 0 else "ဆယ့်" + MY_NUM[u])


GROUP = {"duk": 2, "tik": 3, "catukk": 4, "pañcak": 5, "chakk": 6, "sattak": 7, "aṭṭhak": 8, "navak": 9, "dasak": 10,
         "ekādasak": 11, "dvādasak": 12, "terasak": 13, "cuddasak": 14, "pannarasak": 15, "soḷasak": 16,
         "sattarasak": 17, "aṭṭhārasak": 18, "ekūnavīsak": 19, "vīsak": 20, "ekavīsak": 21, "bāvīsak": 22,
         "tevīsak": 23, "catuvīsak": 24}
_GROUP = re.compile(r"^(paccaya)?(" + "|".join(sorted(GROUP, key=len, reverse=True)) +
                    r")(aṃ|añca|añceva|ā|āni|e|ampi|a)$")


MULA_NUM = {"eka": 1, "du": 2, "dvi": 2, "ti": 3, "catu": 4, "pañca": 5, "cha": 6, "satta": 7, "aṭṭha": 8,
            "nava": 9, "dasa": 10, "ekādasa": 11, "dvādasa": 12, "terasa": 13, "cuddasa": 14, "pannarasa": 15,
            "soḷasa": 16, "sattarasa": 17, "aṭṭhārasa": 18, "ekūnavīsati": 19, "vīsati": 20, "ekavīsati": 21,
            "bāvīsati": 22, "dvāvīsati": 22, "tevīsati": 23, "catuvīsati": 24, "sabba": 0}
_MULA_N = re.compile(r"^(" + "|".join(sorted(MULA_NUM, key=len, reverse=True)) +
                     r")mūlak(aṃ|ā|e|assa|ena|ādi|ādikā|ādikaṃ|ādīni|añca|ampi)$")


def mula_num_cands(kw):
    """T6: the counted mūlaka headings and notes (my7-zeroshot-terms §2): Ekamūlakaṃ «အကြောင်း တစ်ခုကို
    အခြေခံခြင်း», Sabbamūlakaṃ «အကြောင်း အားလုံးကို အခြေခံခြင်း», -ādi / -ādikā «… စသည်»."""
    m = _MULA_N.match(low(kw))
    if not m:
        return None
    n = MULA_NUM[m.group(1)]
    x = "အားလုံး" if n == 0 else my_num(n) + "ခု"
    v = f"အကြောင်း {x}ကို အခြေခံခြင်း"
    return [v + " စသည်", v] if m.group(2).startswith("ādi") else [v]


_UNIT = {"": 0, "eka": 1, "dvā": 2, "dvi": 2, "bā": 2, "te": 3, "catu": 4, "pañca": 5, "cha": 6, "chab": 6, "satta": 7,
         "aṭṭha": 8, "nava": 9, "ekūna": -1}
_TENS = [("cattālīsa", 40), ("cattārīsa", 40), ("paññāsa", 50), ("paṇṇāsa", 50), ("vīsati", 20), ("vīsa", 20),
         ("bīsati", 20), ("bīsa", 20),             # phase 3 fix 7: chab-bīsa(ti) 26
         ("tiṃsati", 30), ("tiṃsa", 30), ("saṭṭhi", 60), ("sattati", 70), ("asīti", 80), ("navuti", 90)]


def pali_number(w):
    """a Pāli number word -> int (ekavīsa 21, sattatiṃsa 37, tettiṃsa 33, ekūnapaññāsa 49), else None."""
    if w in NUM_VAL:
        return NUM_VAL[w]
    for t, n in _TENS:
        if w.endswith(t):
            pre = w[:-len(t)]
            if t.startswith("tiṃs") and pre.endswith("t"):
                pre = pre[:-1]                      # tet-tiṃsa, catut-tiṃsa, chat-tiṃsa
            if pre in _UNIT:
                return n + _UNIT[pre]
    return None


def number_cands(kw):
    """T6: a count word = the text's count with its classifier (pi-1 decision 5: counts keep the text's classifier;
    the answers «… ခု», khandha / mahābhūta «… ပါး»); a counting group «Nမျိုးတွဲ» (pi-1 tika / duka «သုံးမျိုးတွဲ /
    နှစ်မျိုးတွဲ»; Paccayacatukkaṃ «အကြောင်း လေးမျိုးတွဲ»)."""
    w = low(kw)
    c = mula_num_cands(w)
    if c:
        return c
    m = _GROUP.match(w)
    if m:
        g = my_num(GROUP[m.group(2)]) + "မျိုးတွဲ"
        return [("အကြောင်း " if m.group(1) else "") + g]
    m = re.match(r"^(.+?)paccayā$", w)
    if m and pali_number(m.group(1)) is not None:        # «tevīsatipaccayā» «အကြောင်း နှစ်ဆယ့်သုံးပါး»
        return [f"{PACCAYA} {my_num(pali_number(m.group(1)))}ပါး"]
    n = pali_number(w)
    if n is None or n <= 0:
        return None
    x = my_num(n)
    return [x + "ခု", x + "ပါး", x + "မျိုး", x + "ယောက်", x]


# ---- T7 / T8: term qualifiers in any case; na-X (part 5)
A_ENDS = ("ānaṃ", "assa", "āya", "ena", "āni", "āhi", "esu", "aṃ", "ā", "o", "e", "a")
I_ENDS = ("īnaṃ", "issa", "iyā", "iyo", "ino", "inā", "ī", "iṃ", "i")
U_ENDS = ("ūnaṃ", "ussa", "uno", "unā", "uṃ", "ū", "u")


def case_siblings(w):
    """T7: the other case forms of an a-stem (or ī-stem) adjective keyword: savitakkasavicāro -> savitakkasavicārā,
    savitakkasavicāraṃ … (the value of a term does not depend on its case: rule 1 / rule 3)."""
    out = []
    for e in A_ENDS:
        if w.endswith(e) and len(w) > len(e) + 3:
            st = w[:-len(e)]
            out += [st + x for x in ("ā", "o", "aṃ", "assa", "e", "ānaṃ", "ena", "a", "āya", "āni") if st + x != w]
            break
    for e in I_ENDS:
        if w.endswith(e) and len(w) > len(e) + 3:
            st = w[:-len(e)]
            out += [st + x for x in ("ī", "ino", "īnaṃ", "issa", "inā", "i", "iṃ", "iyā", "iyo") if st + x != w]
            break
    for e in U_ENDS:
        if w.endswith(e) and len(w) > len(e) + 2:
            st = w[:-len(e)]
            out += [st + x for x in ("u", "uṃ", "ū", "uno", "ūnaṃ", "unā", "ussa") if st + x != w]
            break
    return out


# T12: «X-samuṭṭhāna» (originated from X) = «Xမှ ဖြစ်ပေါ်လာသော» (pi-2 cittasamuṭṭhānā «စိတ်မှ ဖြစ်ပေါ်လာသော»; the
# text's supplied head noun «ရုပ်» is not part of the keyword, harmonise H8 item 4)
SAMUTTHANA = {"citta": "စိတ်", "utu": "ရာသီဥတု", "āhāra": "အာဟာရ", "kamma": "ကံ", "taṃ": "ထိုအရာ",
              "kusala": "ကုသိုလ်", "akusala": "အကုသိုလ်"}
_SAMUT = re.compile(r"^(" + "|".join(sorted(SAMUTTHANA, key=len, reverse=True)) +
                    r")samuṭṭhān(aṃ|ā|ānaṃ|e|añca|assa|o|ampi|ena|añceva|āni)$")


def samutthana_cands(kw):
    m = _SAMUT.match(low(kw))
    return [SAMUTTHANA[m.group(1)] + "မှ ဖြစ်ပေါ်လာသော"] if m else None


# ---- T6: the paṭṭhāna titles «X-paṭṭhānaṃ» (my7-zeroshot-terms §2 Tikapaṭṭhānaṃ «သုံးမျိုးတွဲတို့၏ အကြောင်းနှင့်
# အကျိုး ဆက်စပ်ပုံ»)
PATTHANA = {"tika": "သုံးမျိုးတွဲ", "duka": "နှစ်မျိုးတွဲ", "dukatika": "နှစ်မျိုးတွဲနှင့် သုံးမျိုးတွဲ",
            "tikaduka": "သုံးမျိုးတွဲနှင့် နှစ်မျိုးတွဲ", "tikatika": "သုံးမျိုးတွဲနှင့် သုံးမျိုးတွဲ",
            "dukaduka": "နှစ်မျိုးတွဲနှင့် နှစ်မျိုးတွဲ"}
_PATTH = re.compile(r"^(" + "|".join(sorted(PATTHANA, key=len, reverse=True)) + r")paṭṭhān(aṃ|e|assa|a)$")


def patthana_cands(kw):
    m = _PATTH.match(low(kw))
    if not m:
        return None
    return [f"{PATTHANA[m.group(1)]}တို့၏ အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ", f"{PATTHANA[m.group(1)]} ဆက်စပ်ပုံ"]


# ---- T13: the cluster dyads of the gocchakas (burmese-style «Cross-book core terms»: the clusters «N-တို့၏ အစု»;
# pi-1 rule 3 sampayutta / vippayutta «Nနှင့် ယှဉ်တွဲသော / ကင်းကွာသော»; sa-X «N၏ အာရုံ ဖြစ်နိုင်သော»): the item
# itself the bare «N» (phase 3), no-X «N မဟုတ်သော» (T8), X-sampayutta, X-vippayutta, X-iya «N၏ အာရုံ ဖြစ်နိုင်သော»
CLUSTER = {"āsav": "စိတ်အစွန်းအထင်း", "saññojan": "နှောင်ကြိုး", "ganth": "အထုံး", "ogh": "ရေအလျဉ်",
           "yog": "ထမ်းပိုး", "nīvaraṇ": "အတားအဆီး", "parāmās": "မှားယွင်းသော ယူဆမှု", "upādān": "စွဲလမ်းမှု",
           "kiles": "ကိလေသာ"}
_ADJ_END = r"(o|aṃ|ā|assa|e|ānaṃ|ena|a|añca|añceva|āni|o ca|ova)"
_CLU = re.compile(r"^(s(?=ā))?(" + "|".join(sorted(CLUSTER, key=len, reverse=True)) +
                  r")(asampayutt|avippayutt|aniy|iy|ik|)" + _ADJ_END + r"$")


def cluster_cands(kw):
    w = low(kw)
    for b in [w] + base_forms(w):
        m = _CLU.match(b)
        if m:
            break
    else:
        return None
    x, kind = CLUSTER[m.group(2)], m.group(3)
    if m.group(1):                     # sāsava (with the āsavas as object) «N၏ အာရုံ ဖြစ်နိုင်သော» (sa-X, pi-1)
        kind = "iy"
    if kind == "asampayutt":
        return [f"{x}နှင့် ယှဉ်တွဲသော"]
    if kind == "avippayutt":
        return [f"{x}နှင့် ကင်းကွာသော"]
    if kind in ("iy", "ik", "aniy"):
        return [f"{x}၏ အာရုံ ဖြစ်နိုင်သော", f"{x}၏ အာရုံ မဖြစ်နိုင်သော"]
    if kind == "sampayutt":
        return [f"{x}နှင့် ယှဉ်တွဲသော"]
    if kind == "vippayutt":
        return [f"{x}နှင့် ကင်းကွာသော"]
    if kind in ("niy", "iy"):
        return [f"{x}၏ အာရုံ ဖြစ်နိုင်သော", f"{x}၏ အာရုံ မဖြစ်နိုင်သော"]
    # phase 3 (coordinator, gocchaka items; g3 G1): the item term is the bare noun N in every case (pi-1 rule 2, the
    # binding pi-1 Mātikā hetū «အမြစ်», āsavā «စိတ်အစွန်းအထင်း», saṃyojanā «နှောင်ကြိုး»); its negative «N မဟုတ်သော» (T8);
    # T13's «N ဖြစ်သော» goes book-wide
    return [x]


# ---- T7: the term tables of the pi-7 generators (make_*.py, my7_formulas.py), READ as text, never imported: the
# triad / dyad stems «"upādinnupādāniy": _tw("…", "ကံကြောင့် ဖြစ်၍ …")» and the lexicon entries «"gotrabhussa": "…"»
GEN_FILES = ("make_*.py", "my7_formulas.py")
_GEN_RX = re.compile(r'"([a-zA-ZāīūṃṅñṭḍṇḷĀĪŪṄÑṬḌṆḶ][a-zāīūṃṅñṭḍṇḷ\-]*)"\s*:\s*(?:[A-Za-z_.]+\(\s*"[^"]*"\s*,\s*)?'
                     r'"([^"{}]*[\u1000-\u109f][^"{}]*)"(?!\s*\+)')   # phase 3 fix 3: «"…" + new(…)» is no value
GEN_ENDS = ("", "a", "ā", "o", "aṃ", "assa", "e", "ānaṃ", "ena", "āya", "añca", "āni", "akā", "akaṃ", "ako",
            "akassa", "ake", "akānaṃ", "ī", "ino", "inaṃ", "īnaṃ", "issa", "iṃ", "āyo", "ehi", "esu", "āti", "oti",
            "anti", "ā ca", "o ca")


@functools.lru_cache(maxsize=None)
def gen_terms():
    """T7: {low(pāli stem or word): Counter(Burmese)} from the generators' term tables (values in dictionary form; a
    bare particle is no value)."""
    out = collections.defaultdict(collections.Counter)
    for pat in GEN_FILES:
        for f in sorted(HERE.parent.glob(pat)):
            for m in _GEN_RX.finditer(f.read_text(encoding="utf-8")):
                v = dict_noun(m.group(2).strip())
                if len(v) > 3 and v not in PARTICLES and not v.startswith(("ကို ", "နှင့် ")):
                    out[low(m.group(1))][v] += 1
    return out


def gen_values(w):
    """the generator values of a keyword: its own entry, or a stem entry + a case ending."""
    g = gen_terms()
    out = []
    for i in range(len(w), max(3, len(w) - 8), -1):
        if w[:i] in g and w[i:] in GEN_ENDS:
            out += [v for v, _ in g[w[:i]].most_common() if v not in out]
    return out


# T12 heads of a compound term: Pāli tail -> Burmese head
HEADS = [("purejātaṃ", "ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်း"), ("pacchājātaṃ", "နောက်မှ ဖြစ်ပေါ်ခြင်း"),  # the kinds of a condition
         ("sahagatānaṃ", "နှင့်အတူ ဖြစ်သော"), ("sahagataṃ", "နှင့်အတူ ဖြစ်သော"), ("sahagatā", "နှင့်အတူ ဖြစ်သော"),
         ("sahagato", "နှင့်အတူ ဖြစ်သော"), ("sahagate", "နှင့်အတူ ဖြစ်သော"), ("sahagatassa", "နှင့်အတူ ဖြစ်သော"),
         ("ādhipatiñca", "အကြီးအမှူး"), ("ādhipatiṃ", "အကြီးအမှူး"), ("ādhipatino", "အကြီးအမှူး"),
         ("ādhipatī", "အကြီးအမှူး"), ("ādhipati", "အကြီးအမှူး"), ("adhipati", "အကြီးအမှူး"),
         ("cittasamaṅgissa", "စိတ်နှင့် ပြည့်စုံသူ"), ("cittasamaṅgīnaṃ", "စိတ်နှင့် ပြည့်စုံသူ"),
         ("cittasamaṅgino", "စိတ်နှင့် ပြည့်စုံသူ"), ("cittasamaṅgī", "စိတ်နှင့် ပြည့်စုံသူ")]


def neg_term(v):
    """T8 (harmonise H21: the na-X rule of the pi-7 text): na + an attributive term «Xသော» = «Xသည် မဟုတ်သော»; na + a
    noun term «X» = «X မဟုတ်သော» (nakusalo «ကုသိုလ် မဟုတ်သော»; naabyākato «ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သည်
    မဟုတ်သော»); candidates in order."""
    if v.endswith("သော"):
        st = v[:-3]
        return [st + "သည် မဟုတ်သော", st + "သော … မဟုတ်", st + "သည် မဟုတ်"]
    return [v + " မဟုတ်သော", v + " မဟုတ်", v + " … မဟုတ်သော"]


# ---- T10: verbs
# root -> (positive stem, negative stem): the pi-7 text's forms (pi-1 … pi-6 values: uppajjati ဖြစ်ပေါ်သည်)
VERB_ROOTS = [("uppajj", "ဖြစ်ပေါ်", "မဖြစ်ပေါ်"), ("nirujjh", "ချုပ်ငြိမ်း", "မချုပ်ငြိမ်း")]
_ROOT = {r: (p, n) for r, p, n in VERB_ROOTS}
# Pāli finite endings -> mood (longest first): the optative «Siyā … uppajjeyya» = the potential «…နိုင်» (T10)
VERB_ENDS = [("eyyuṃ", "opt"), ("eyya", "opt"), ("issanti", "fut"), ("issati", "fut"), ("ittha", "past"),
             ("anti", "pres"), ("ati", "pres"), ("atī", "pres")]


def parse_verb(kw):
    """'uppajjati' / 'uppajjeyyuṃ' / 'nuppajjati' -> (root, mood, neg), else None."""
    w = low(kw.strip())
    for b in [w] + base_forms(w):
        cands = [(b, False)]
        if b.startswith("n"):
            cands += [(b[1:], True), (b[2:], True)]
        for x, ng in cands:
            for root, _, _ in VERB_ROOTS:
                if x.startswith(root):
                    rest = x[len(root):]
                    for end, mood in VERB_ENDS:
                        if rest == end:
                            return root, mood, ng
    return None


def verb_cands(root, mood, neg):
    """T10 (pi-1 rule 4 «…သည်»; the plural «ကြ» by the ending rule; Q5 negatives «မ + verb» without «သည်»): the
    optative of the pucchāvāra «Siyā … uppajjeyya» = «ဖြစ်ပေါ်နိုင်သည်» (the text's «ဖြစ်ပေါ်နိုင်သလော / နိုင်ကြသလော»,
    pi-5 Q1 ending «သလော»)."""
    p, n = _ROOT[root]
    if neg:
        return {"pres": [n], "past": [n + "ခဲ့"], "fut": [n + "လိမ့်မည်"], "opt": [n + "နိုင်", p + " မနိုင်"]}[mood]
    return {"pres": [p + "သည်"], "past": [p + "ခဲ့သည်"], "fut": [p + "လိမ့်မည်", p + "မည့်"],
            "opt": [p + "နိုင်သည်", p + "သည်"]}[mood]


# =====================================================================================================================
# R1 base forms (pi-6, with its phase-3 mechanic 2)
# =====================================================================================================================
_V = "aāiīuūeo"


def base_forms(kw):
    """R1 (pi-6): the «-ti» (quotation / question) and «ca / ceva / ñca / ñceva / pi / mpi» forms of a keyword ->
    candidate base forms, in order (the quotative, ca and pi have no Burmese word of their own, pi-1 rule 9 / pi-5
    Q4)."""
    out = []
    k = kw

    def add(x):
        if x and x != kw and x not in out:
            out.append(x)
    for suf, rep in (("ñceva", "ṃ"), ("ñcāti", "ṃ"), ("ñca", "ṃ"), ("ṃyeva", "ṃ"), ("yeva", ""), ("ceva", ""),
                     ("cāti", ""), ("mpi", "ṃ"), ("meva", "ṃ")):
        if k.endswith(suf) and len(k) > len(suf) + 2:
            add(k[:-len(suf)] + rep)
    if k.endswith("ca") and len(k) > 4 and k[-3] in _V:
        add(k[:-2])
    if k.endswith("pi") and len(k) > 4 and k[-3] in _V:
        add(k[:-2])
    if k.endswith("ti") and len(k) > 4:
        s = k[:-2]
        if s[-1] in "āīū":
            add(s)
            add(s[:-1] + {"ā": "a", "ī": "i", "ū": "u"}[s[-1]])
        elif s[-1] in "oe":
            add(s)
        elif s.endswith("n") and s[-2] in _V and not _finite(k):
            add(s[:-1] + "ṃ")          # pi-6 phase 3 mechanic 2: a finite «-anti» is not «-aṃ + ti»
    return out


def _finite(w):
    w = low(w)
    cands = [w] + ([w[1:], w[2:]] if w.startswith("n") else [])
    for x in cands:
        for root, _, _ in VERB_ROOTS:
            if x.startswith(root) and any(x[len(root):] == e for e, _ in VERB_ENDS):
                return True
    return False


# =====================================================================================================================
# T9: the heading lexicon (the text's own heading parts, book-wide)
# =====================================================================================================================
_LABEL = re.compile(r"\((?:[A-ZĀĪŪṄÑṬḌṆḶa-zāīūṅñṭḍṇḷṃ]{1,4}|[က-အ]|\d+)\)|\b\d+(?:-\d+)*\.?-?|"
                    r"[0-9၀-၉]+(?:-[0-9၀-၉]+)*\.?-?")


def heading_parts(text):
    """the parts of a heading line between its labels «(Ka) / (က) / (1) / 2. / 1-7.», and the bracketed sub-parts
    «Tevīsakaṃ (sāsevanaṃ)» as parts of their own."""
    t = re.sub(r"^#+\s*", "", text.strip()).replace("*", "")
    t = re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", t)
    out = []
    for p in _LABEL.split(t):
        for q in re.split(r"\s*[()]\s*", p):
            q = q.strip(" .။–")
            if q and re.search(r"[" + PW + r"A-Zက-အ]", q, re.I):
                out.append(q)
    return out


@functools.lru_cache(maxsize=None)
def head_lex():
    """T9: {low(Pāli heading part): Counter(Burmese part in dictionary form)} over every heading line of the book whose
    Pāli and Burmese have the same number of parts (the text's own heading translations; rule 7: a heading keyword
    that IS a whole heading part takes the whole part)."""
    lex = collections.defaultdict(collections.Counter)
    for ch in chapters():
        P, B = PI / f"{ch}.md", MY / f"{ch}.md"
        if not P.exists() or not B.exists():
            continue
        pl = {}
        for l in P.read_text(encoding="utf-8-sig").splitlines():
            m = ID.search(l)
            if l.startswith("#") and m:
                pl[m.group(1)] = l
        for l in B.read_text(encoding="utf-8-sig").splitlines():
            m = ID.search(l)
            if not (l.startswith("#") and m) or m.group(1) not in pl:
                continue
            a, b = heading_parts(pl[m.group(1)]), heading_parts(l)
            if len(a) != len(b):
                continue
            for x, y in zip(a, b):
                if " " not in x.strip() and not re.search("[a-zA-Z]", y):
                    lex[low(x.strip(" .,"))][dict_noun(y)] += 1
    return lex


def heading_value(kw, pali, my):
    """R6 (pi-6; pi-1 rule 7): in a heading line, the Burmese part at the same position as the Pāli part that is the
    keyword."""
    if not pali.lstrip().startswith("#"):
        return None
    pp, mp = heading_parts(pali), heading_parts(my)
    if len(pp) == len(mp):
        for a, b in zip(pp, mp):
            if low(a.strip(" .,")) == low(kw):
                return dict_noun(b)
    return None


# =====================================================================================================================
# context helpers (copied from pi-6 map6_rules.py, unchanged)
# =====================================================================================================================
def first_compound(pali, stems):
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


def pref(*vals):
    def f(kw, pali, my):
        for v in vals:
            if presence(v, my)[0]:
                return v
        return vals[-1]
    return f


def alt(*vals):
    """the first value the segment's Burmese has as a phrase, then the first present by the ending rules, else the
    pi-1 … pi-6 value (one sense per segment, the text's own word)."""
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
    rx = re.compile(r"(?<![\wāīūṃṅñṭḍṇḷ])" + pali_word + r"(?![\wāīūṃṅñṭḍṇḷ])", re.I)

    def f(kw, pali, my):
        return value if rx.search(strip_brackets(pali)) else NONE
    return f


_LONG = {"a": "[aā]", "i": "[iī]", "u": "[uū]"}


def pali_has(kw, pali):
    """the keyword stands in the Pāli outside the variant brackets (also with the sandhi length before «ti»)."""
    k = low(kw)
    rx = re.escape(k[:-1]) + _LONG.get(k[-1], re.escape(k[-1])) if k else ""
    return bool(re.search(r"(?<![a-zāīūṃṅñṭḍṇḷ])" + rx + r"(?:n?ti)?" + _PW, strip_brackets(pali), flags=re.I))


def pick(cands, my):
    """the first candidate the segment's Burmese has as a phrase (its final «သည် / သော» by an ending rule), then the
    first present by the ending rules; None where none is (one form per segment, the text's own form)."""
    if not cands:
        return None
    for v in cands:
        if v == NONE or (presence(v, my)[0] and (phrase_ok(v, my) or phrase_ok(v, flat(my)))):
            return v
    for v in cands:
        if presence(v, my)[0] and " … " not in v and len(v.split()) == 1 and (v not in my or occurs(v, my)):
            return v
    return None


def pick_phrase(cands, my):
    """as pick(), but only a candidate the text has as a phrase (or with the «လည်း» of ca / ceva inside it, R7)."""
    for v in cands or ():
        if v == NONE or (presence(v, my)[0] and phrase_gap_ok(v, my)):
            return v
    return None


def phrase_gap_ok(v, my):
    """the value stands as a phrase in the text, or does so with R7's « … » at the «လည်း» of ca / ceva."""
    return phrase_ok(v, my) or phrase_ok(v, flat(my)) or lad_gap(v, my) != v


def flat(my):
    """the text without the list comma «၊» (pi-1 rule 6: the «၊» inside a term is dropped in the value)."""
    return my.replace("၊ ", " ").replace("၊", "")


# ---- FUNCS-BEGIN
_FREE_RUPA = re.compile("ရုပ်(?!မရှိ|ဘုံ| မရှိ| ရှိလျက်| အစုအဝေး|ပိုင်း| မဟုတ်| ဖြစ်သော| အသက်)")


def f_rupam(kw, pali, my):
    """rūpa (pi-6 f_rupam, copied): matter «ရုပ်» (pi-1 / pi-2 / pi-5) wherever the text has a free «ရုပ်» (not
    inside «ရုပ်မရှိသော ဘုံ / ရုပ် မဟုတ်သော / ရုပ် ဖြစ်သော / ရုပ် အသက် / ရုပ်ပိုင်း …»); the visible object
    «အဆင်းအရောင်» (pi-1 / pi-5 rūpāyatana, rūpārammaṇa) where the Pāli has the object sense and the text that word;
    one sense per segment."""
    if _FREE_RUPA.search(my):
        return "ရုပ်"
    if re.search(r"rūpāyatan|rūpārammaṇ|rūpaṃ passati|cakkhunā rūpaṃ|rūpe", strip_brackets(pali), re.I) \
            and "အဆင်းအရောင်" in my:
        return "အဆင်းအရောင်"
    if "ရုပ်" in my:
        return "ရုပ်"
    return "@prior"


def f_paccayo(kw, pali, my):
    """paccayo: «အကြောင်း» (pi-5 ^5-717, T3), the predicate of «Xpaccayena paccayo» «Nဟူသော အကြောင်းဖြင့် အကြောင်း
    ဖြစ်သည်»; else the pi-1 … pi-6 value the text has."""
    return PACCAYA if PACCAYA in my else "@prior"


_IN_TERM = re.compile("မရှိ(?=သော|ခြင်း|သူ|သည့်|သည်လည်း|သည်ကို)")


def f_natthi(kw, pali, my):
    """natthi: the condition «မရှိခြင်း» in a ghaṭanā list (T4); as a hyphen-compound part (g1, T4) the condition name
    «မရှိခြင်းဟူသော အကြောင်း» in a heading («Natthi-vigatapaccayā»), the bare name «မရှိခြင်း» in a note
    («(Natthi-vigataṃ anantarasadisaṃ …)»); else the verb: pi-1 … pi-6 «မရှိသည်» where the text has it by an ending
    rule, else the text's «မရှိ» (pi-5 Q5). Phase 3 (coordinator; g4 G3): a «မရှိ…» that stands only inside a longer
    term («… မှတ်သိမှု မရှိသည်လည်း မဟုတ်», «… မရှိသည်ကို အာရုံပြုသော», the condition name «မရှိခြင်းဟူသော အကြောင်း»,
    «ရုပ်မရှိသော ဘုံ», «အမြစ် မရှိသော») is not the verb: those places are masked before the check."""
    c = pick_phrase(cond_cands(kw, pali, pali.lstrip().startswith("#")) or [], my)
    if c and compound_form(kw, pali):
        return c
    if re.search(r"(?<![\w" + PW + r"])" + re.escape(kw) + "-", pali):
        h = pick_phrase([cname("natthi")] if pali.lstrip().startswith("#") else [N["natthi"]], my)
        if h is not None:
            return h
    free = _IN_TERM.sub("မ·ရှိ", my)
    for v in ("မရှိသည်", "မရှိ"):
        if presence(v, free)[0] and phrase_ok(v, free):
            return v
    return c or "@prior"


ACT_OBJ = ("uposathakamm", "ekāgārik", "gāmaghāt", "nigamaghāt")   # compounds whose Burmese carries the verb


def f_karoti(kw, pali, my):
    """karoti / katvā after an act compound «uposathakammaṃ / ekāgārikaṃ / gāmaghātaṃ / nigamaghātaṃ» (T11): the text's
    verb belongs to the compound's value, so the verb has no word of its own (pi-2 harmonise: one Burmese word for two
    members, the other (no direct equivalent)); one sense per segment: the first «X karoti / katvā» decides; a free
    «garuṃ katvā» «ပြု၍» and the other uses keep their value."""
    w = low(kw)
    objs = [m.group(1) for m in re.finditer(r"(\w+)\s+" + re.escape(w) + _PW, low(strip_brackets(pali)))]
    if objs and all(o.startswith(ACT_OBJ) for o in objs):
        return NONE
    if w == "katvā":
        return "ပြု၍" if "ပြု၍" in my else "@prior"
    return "@prior"


_QUAL_NEXT = re.compile(r"\s+(?:(?:[a-zāīūṃṅñṭḍṇḷ]+\s+){0,3}(?:dhamm|khandh)|phalasamāpatt)", re.I)


def f_sekkha(kw, pali, my):
    """sekkha / asekkha (coordinator, g2 decision): as a qualifier of a dhamma / khandha (the Pāli word after
    the keyword, or up to three words later: «Sekkho ca nevasekkhanāsekkho ca dhammā») the binding pi-1 / pi-2 «ကျင့်ကြံဆဲသူ၏ / ကျင့်ကြံမှု ပြီးဆုံးသူ၏» in every case
    (fix 8: one value per term), a person noun the bare «ကျင့်ကြံဆဲသူ / ကျင့်ကြံမှု ပြီးဆုံးသူ»."""
    n = "ကျင့်ကြံမှု ပြီးဆုံးသူ" if low(kw).startswith("a") else "ကျင့်ကြံဆဲသူ"
    w = low(kw)
    qual = False
    for b in [w] + base_forms(w):
        if re.search(r"(?<![\w" + PW + r"])" + re.escape(b) + r"(?:ñca|ca)?" + _QUAL_NEXT.pattern,
                     strip_brackets(pali), re.I):
            qual = True
            break
    cands = [n + "၏", n] if qual else [n, n + "၏"]
    v = pick_phrase(cands, my)
    return v if v is not None else "@prior"


def f_vipakassa(kw, pali, my):
    """vipākassa (phase 3 scan; phase 1 §B vipāka noun / adjective): «kammaṃ vipākassa … paccayena paccayo» is the
    noun «ကံ၏ အကျိုး» (the text's «… ကံသည် ကံ၏ အကျိုးအား»); elsewhere the triad adjective «ကံ၏ အကျိုး ဖြစ်သော» (STOCK),
    one sense per segment: the first vipākassa of the segment decides."""
    m = re.search(r"(?<![\w" + PW + r"])(\w+)\s+vipākassa", strip_brackets(pali))
    if m and m.group(1).lower() == "kammaṃ":
        v = pick_phrase(["ကံ၏ အကျိုး"], my)
        if v is not None:
            return v
    return alt("ကံ၏ အကျိုး ဖြစ်သော", "ကံ၏ အကျိုး")(kw, pali, my)


def f_navinn(kw, pali, my):
    """naviññeyyo (coordinator): the text's own lexical negative «မသိနိုင်သော» where the text has it literally (2-xx,
    3-02, part 4); where the text has the T8 form «သိနိုင်သည် မဟုတ်သော» (part 5) the chain goes on (T8)."""
    if occurs("မသိနိုင်သော", my):
        return "မသိနိုင်သော"
    raise KeyError(kw)


FUNCS = {
    "sekkha": f_sekkha, "naviñ": f_navinn, "vipakassa": f_vipakassa,
    "karoti": f_karoti, "katva": f_karoti,
    "natthi": f_natthi,
    "rupam": f_rupam,
    "paccayo": f_paccayo,
}
# ---- FUNCS-END


def alt_name(vals):
    """the FUNCS name of a tuple value («@alt:a|b|…»), registered on first use."""
    name = "alt:" + "|".join(vals)
    FUNCS.setdefault(name, alt(*vals))
    return "@" + name


for _tab in (FRAME, STOCK):          # the tuples of the module tables as «@alt:…» values
    for _k, _v in list(_tab.items()):
        if isinstance(_v, tuple):
            _tab[_k] = alt_name(_v)


# =====================================================================================================================
# lookup engine (pi-6, single-word keywords; compose kept for a multiword keyword)
# =====================================================================================================================
def contiguous(v, my):
    parts = v.split(" … ")
    if not all(occurs(p, my) for p in parts):
        return False
    return len(parts) == 1 or v.replace(" … ", " ") not in my


def contiguous_rule(v, my):
    for part in v.split(" … "):
        if occurs(part, my):
            continue
        if not part.endswith("သော") or not any(occurs(part[:-3] + e, my) for e in ATTR_FROM):
            return False
    return True


def pi_get(kw, my, tiers=("contig", "literal", "rule")):
    """the most frequent pi-2 (then pi-3, pi-4, pi-5, pi-6, pi-1) value of the keyword present in the segment, by tier
    (pi-4 engine): contiguous phrase, then every chunk literal and together (phrase_ok, pi-6 phase-3 mechanic 1), then
    (verbs «…သည်» or a whole phrase with another attributive ending) by an ending rule."""
    ranked = [(t, [v for v, _ in prev_vals(kw, t).most_common() if v != NONE]) for t in PRIOR_ORDER]
    for tier in tiers:
        for tag, vals in ranked:
            for v in vals:
                if tier == "rule" and not (v.endswith("သည်") or contiguous_rule(v, my)):
                    continue
                ok, rules = presence(v, my)
                if not ok:
                    continue
                if (tier == "contig" and (contiguous(v, my) or contiguous(v, flat(my)))) or \
                        (tier == "literal" and not rules and phrase_gap_ok(v, my)) or \
                        tier == "rule":
                    return v, tag
    return None, None


PARTICLES = ("", "ကို", "သည်", "၏", "၌", "တွင်", "နှင့်", "မှ", "ဖြင့်", "အား", "သို့", "က", "ကား", "သည်ပင်", "ပင်",
             "ဟု", "ဟူသော", "နှင့်တကွ", "နှင့်အတူ", "အားဖြင့်", "တို့", "တို့၏", "တို့ကို", "တို့သည်", "တို့၌",
             "တို့နှင့်", "တို့နှင့်တကွ", "များ", "များကို", "များ၏", "၏ပင်", "ကိုပင်")


# ---- phase 3 fix 1: word boundaries. A value chunk matches only where it ends on a Burmese word boundary: the text
# goes on with a space / punctuation / the end, or with a particle or ending written on to the word (case particles,
# the plural, «လည်း / ပင် / သာ», the verb and attributive endings), never with more letters of the same word
# (ajjhattikassa «အတွင်း» is not the word of «အတွင်းပိုင်း», cakkaṃ «စက်» not that of «စက်ဝိုင်း»).
_BLETTER = re.compile(r"[က-၉၌-႟]")      # a Burmese letter, mark or digit (not «၊ ။»)
_BMARK = re.compile(r"[ါ-ှၖ-ၙၞ-ၠၢ-ၤၧ-ၭၱ-ၴႂ-ႍ"
                    r"ႏႚ-ႝ]")                 # a dependent vowel / medial / asat / tone mark
BOUND_PART = tuple(sorted(set((
    "၏", "၌", "ကို", "သည်", "တို့", "များ", "မှ", "ဖြင့်", "အား", "တွင်", "ဟု", "ဟူ", "နှင့်", "ကြောင့်", "လည်း", "ပင်",
    "သာ", "က", "ကား", "သို့", "၍", "သော", "သော်", "လျှင်", "ပြီ", "ကြ", "ခဲ့", "မည်", "မည့်", "လိမ့်", "နိုင်", "ပါ",
    "သလော", "သနည်း", "ရာ", "ရန်", "သည့်", "စဉ်", "ကုန်", "ဘဲ", "လျက်", "ကဲ့သို့", "သကဲ့သို့", "အတိုင်း", "အဖြစ်",
    "အခါ", "အနေ", "အတွက်", "ထက်", "ဆီ", "တိုင်း", "စွာ", "ပြီး", "ကာ", "သမျှ", "သတတ်", "မျှ",
    "အထိ", "လုံး", "တည်း", "ထံ",            # «… အခြေခံခြင်းအထိ», «ခုနစ်ခုလုံး», «တစ်ခုတည်း», «မယားထံ»
)), key=lambda x: (-len(x), x)))


def bounded_at(text, end):
    """the text at index `end` starts a new word: the end, a non-letter, or a particle / ending that ends a syllable."""
    if end >= len(text) or not _BLETTER.match(text[end]):
        return True
    for p in BOUND_PART:
        if text.startswith(p, end) and not _BMARK.match(text[end + len(p):end + len(p) + 1]):
            return True
    return False


def occurs(s, text):
    """s stands in the text ending on a word boundary (phase 3 fix 1)."""
    i = text.find(s)
    while i >= 0:
        if bounded_at(text, i + len(s)):
            return True
        i = text.find(s, i + 1)
    return False


def phrase_present(s, my, verb_from=None):
    """the phrase stands in the text, its final «သည် / သော» standing for one of the text's endings (rules 3 / 4), on a
    word boundary (phase 3 fix 1)."""
    if occurs(s, my):
        return True
    if s.endswith("သည်"):
        return any(occurs(s[:-3] + e, my) for e in (verb_from or VERB_FROM))
    if s.endswith("သော"):
        if s.endswith("ပြီးသော") and (occurs(s[:-3] + " ဖြစ်", my) or occurs(s[:-3] + " မဟုတ်", my)):
            return True
        return any(occurs(s[:-3] + e, my) for e in ATTR_FROM)
    if s.endswith("ည့်"):
        return occurs(s[:-3] + "ည်", my)
    return False


def phrase_ok(v, my):
    """every « … » part of the value stands as a phrase in the text (its final «သည် / သော» by an ending rule)."""
    return all(phrase_present(p, my) for p in v.split(" … "))


def is_verb(v):
    last = v.split(" … ")[-1].split()[-1]
    return last.endswith("သည်")


def table_get(tab, kw):
    for k in (kw, low(kw), kw[:1].upper() + kw[1:]):
        if k in tab:
            return tab[k]
    return None


def make_stem(tables):
    """S1 (pi-5 / pi-6, approved after the pi-6 phase-3 review): the stem fallback over the pi-1 … pi-6 values and the
    given tables: a single keyword that nothing else maps takes the value of a keyword of the same stem (the longest
    common beginning, at least the keyword less four letters, length within five) that the segment's Burmese has as a
    phrase, most frequent first (a table value counts 50). Prefix search by bisection over the sorted keys."""
    pool = collections.defaultdict(collections.Counter)
    for t in PRIOR_ORDER:
        for k, c in prior()[t].items():
            pool[k].update(c)
    for tab in tables:
        for k, v in tab.items():
            for x in (v if isinstance(v, tuple) else (v,)):
                if not x.startswith("@") and x != NONE and " … " not in x:
                    pool[low(k)][x] += 50
    keys = sorted(k for k in pool if " " not in k)

    def stem(kw, my):
        k = low(kw)
        kind = kw_kind(k)
        for n in range(len(k), max(4, len(k) - 4) - 1, -1):
            pre = k[:n]
            c = collections.Counter()
            i = bisect.bisect_left(keys, pre)
            while i < len(keys) and keys[i].startswith(pre):
                if abs(len(keys[i]) - len(k)) <= 5:
                    c.update(pool[keys[i]])
                i += 1
            for v, _ in c.most_common():
                for x in fit_kind(v, kind):
                    if x != NONE and presence(x, my)[0] and phrase_ok(x, my):
                        return x
        return None
    stem.pool = pool
    return stem


def kw_kind(k):
    """the grammatical shape of a Pāli keyword for the S1 guard (pi-7 mechanic M1): abs (absolutive -tvā), ger
    (gerundive -tabba-), fin (a finite verb -ati / -eti / -oti / -anti …), nom (anything else)."""
    if k.endswith(("tvā", "tvāna")):
        return "abs"
    if re.search(r"tabb(aṃ|o|ā|āni|e|aṃyeva)$", k):
        return "ger"
    if k.endswith(("ati", "eti", "oti", "enti", "onti", "āti", "anti")) and not k.endswith(("santi", "panti")):
        return "fin"
    return "nom"


def fit_kind(v, kind):
    """S1 guard (pi-7 mechanic M1): a stem donor's value in the keyword's own dictionary shape (rule 3 / rule 4 /
    the absolutive «…၍» of pi-1): a verb value «…သည်» never goes to a noun keyword, a noun value never to a verb; a
    finite donor becomes «X၍» for an absolutive, a participle «Xသော» becomes «Xသည်» for a finite verb."""
    if v == NONE:
        return []
    verb = v.endswith("သည်") or v.endswith("၍")
    if kind == "nom":
        return [] if verb else [v]
    if kind == "abs":
        if v.endswith("၍"):
            return [v]
        return [v[:-3] + "၍"] if v.endswith(("သည်", "သော")) else []
    if kind == "fin":
        if v.endswith("သည်") or (v.startswith("မ") and not v.endswith("သော")):
            return [v]
        return [v[:-3] + "သည်"] if v.endswith("သော") else []
    if kind == "ger":
        return [v] if v.endswith("မည့်") else ([v[:-3] + "ရမည့်"] if v.endswith("သည်") else [])
    return [v]


def lad_gap(v, my):
    """R7 (pi-6; pi-1 rule 10 / pi-5 Q4 for one keyword): a value that the text has as a phrase only with the «လည်း»
    of ca / pi inside it gets « … » at that place; the «လည်း» of «neither … nor» inside a term stays."""
    if v == NONE or " … " in v or phrase_ok(v, my) or phrase_ok(v, flat(my)):
        return v
    ch = v.split(" ")
    for i in range(1, len(ch)):
        l, r = " ".join(ch[:i]), " ".join(ch[i:])
        for m in (my, flat(my)):
            if phrase_present(l + "လည်း " + r, m):
                return l + " … " + r
    return v


def finish(v):
    """rule 6 / rule 10: no list comma «၊» and no «, » inside a value."""
    if v is None or v == NONE:
        return v
    return re.sub(r"\s+", " ", v.replace("၊", " ")).strip()


class Mapper:
    """chapter_tables: {ch: {kw: value}}; ctx: {sid: {kw: value}}; a value «@name» calls FUNCS[name] (or the mapper's
    own funcs); a tuple value = alt(). stem: a make_stem() function (S1) for keywords nothing else maps. SRC[(sid, kw)]
    records where each value came from. Lookups are cached per (chapter, segment, keyword)."""

    def __init__(self, chapter_tables=None, ctx=None, funcs=None, stem=None):
        self.tables = {ch: {k: (alt_name(v) if isinstance(v, tuple) else v) for k, v in tab.items()}
                       for ch, tab in (chapter_tables or {}).items()}
        self.ctx = {sid: {k: (alt_name(v) if isinstance(v, tuple) else v) for k, v in tab.items()}
                    for sid, tab in (ctx or {}).items()}
        self.stem = stem
        self.funcs = dict(FUNCS)
        self.funcs.update(funcs or {})
        self.SRC = {}
        self.cache = {}

    # -- values
    def resolve(self, v, kw, pali, my):
        while v is not None and v.startswith("@"):
            v = self.funcs[v[1:]](kw, pali, my)
            if v == "@prior":
                v = pi_get(kw, my)[0]
                if v is None:
                    for b in base_forms(kw):
                        v = pi_get(b, my)[0]
                        if v is not None:
                            break
                if v is None:
                    raise KeyError(kw)
        return v

    def lookup(self, ch, sid, kw, pali, my):
        key = (ch, sid, kw)
        if key in self.cache:
            v, src = self.cache[key]
            self.SRC[(sid, kw)] = src
            if v is None:
                raise KeyError(kw)
            return v
        try:
            v = self._lookup(ch, sid, kw, pali, my)
        except KeyError:
            self.cache[key] = (None, None)
            raise
        v = finish(v)
        self.cache[key] = (v, self.SRC.get((sid, kw)))
        return v

    def _lookup(self, ch, sid, kw, pali, my):
        try:
            v = self._chain(ch, sid, kw, pali, my)
        except KeyError:
            if " " in kw or self.stem is None:
                raise
            v = self.stem(kw, my)
            if v is None:
                raise
            self.SRC[(sid, kw)] = "stem"
            return lad_gap(v, my)
        return lad_gap(v, my)

    def _tables(self, ch, sid, kw, pali, my):
        """the CTX / chapter table / FRAME / STOCK value of the keyword (resolved), else None."""
        for tab, src in ((self.ctx.get(sid, {}), "ctx"), (self.tables.get(ch, {}), "table"), (FRAME, "frame"),
                         (STOCK, "stock")):
            v = table_get(tab, kw)
            if v is not None:
                try:
                    v = self.resolve(v, kw, pali, my)
                except KeyError:
                    if src in ("ctx", "table"):
                        raise
                    continue
                if src in ("frame", "stock") and not presence(v, my)[0]:
                    continue          # a book-wide value the segment does not have: the chain goes on
                self.SRC[(sid, kw)] = src
                return v
        return None

    def _families(self, kw, pali, my):
        """T1-T6: the Paṭṭhāna families, each candidate checked against the segment (pick)."""
        heading = pali.lstrip().startswith("#")
        if low(kw) in VARA and vara_part(kw, pali):
            v = pick_phrase([VARA[low(kw)]], my)
            if v is not None:
                return v, "vara"
        for fam, fn in (("cond", lambda: cond_cands(kw, pali, heading)), ("vara", lambda: vara_cands(kw)),
                        ("order", lambda: order_cands(kw)), ("count", lambda: number_cands(kw)),
                        ("samutthana", lambda: samutthana_cands(kw)), ("title", lambda: patthana_cands(kw))):
            c = fn()
            if c:
                v = pick_phrase(c, my)
                if v is not None:
                    return v, fam
        return None, None

    def _chain(self, ch, sid, kw, pali, my):
        """pi-7 order: tables -> families (T1-T6) -> heading lexicon (T9) -> verbs (T10) -> pi-7 terms -> pi-1 … pi-6
        value -> term family (T7 / T8) -> heading rule (R6). Phase 3 fix 5 (R1 order): each step is tried for the
        keyword and then for its R1 base forms before the next step, so a «-ñca / -ca / -pi / -ti» form takes its base
        form's table value before its own family value, and its base form's value before the term family
        (Vipākañca = vipākaṃ, Āsavañca = Āsavaṃ)."""
        forms = [(kw, "")] + [(b, "base:") for b in base_forms(kw)]

        def mark(tag, k, src):
            self.SRC[(sid, kw)] = tag + src if tag else src
        for k, tag in forms:
            v = self._tables(ch, sid, k, pali, my)
            if v is not None:
                if tag:
                    mark(tag, k, self.SRC.get((sid, k)) or "?")
                return v
        for k, tag in forms:
            v, fam = self._families(k, pali, my)
            if v is not None:
                mark(tag, k, fam)
                return v
            h = head_lex().get(low(k))
            if h:
                v = pick_phrase([x for x, _ in h.most_common()], my)
                if v is not None:
                    mark(tag, k, "headlex")
                    return v
            pv = parse_verb(k)
            if pv:
                v = pick(verb_cands(*pv), my)
                if v is not None:
                    mark(tag, k, "verb")
                    return v
        for k, tag in forms:
            try:
                v = self._rest(ch, sid, k, pali, my)
            except KeyError:
                continue
            if tag:
                mark(tag, k, self.SRC.get((sid, k)) or "?")
            return v
        for k, tag in forms:
            v = self.term_family(k, my)
            if v is not None:
                mark(tag, k, "term")
                return v
        v = heading_value(kw, pali, my)
        if v is not None and presence(v, my)[0]:
            self.SRC[(sid, kw)] = "heading"
            return v
        raise KeyError(kw)

    def _rest(self, ch, sid, kw, pali, my):
        """the pi-5 / pi-6 chain after the tables: pi-7 terms, a pi-1 … pi-6 value the text has (the term family is
        the next step of _chain, phase 3 fix 5)."""
        t = terms().get(low(kw))
        if t is not None and presence(t, my)[0] and all(occurs(p, my) or occurs(p, flat(my)) for p in t.split(" … ")):
            self.SRC[(sid, kw)] = "terms"
            return t
        v, tag = pi_get(kw, my, tiers=("contig",))
        if v is not None:
            self.SRC[(sid, kw)] = tag
            return v
        if t is not None and presence(t, my)[0] and phrase_ok(t, my):
            self.SRC[(sid, kw)] = "terms"
            return t
        t = LEXW.get(low(kw))
        if t is not None and presence(t, my)[0] and (phrase_ok(t, my) or phrase_ok(t, flat(my))):
            self.SRC[(sid, kw)] = "lex"
            return t
        v, tag = pi_get(kw, my)
        if v is not None:
            self.SRC[(sid, kw)] = tag
            return v
        raise KeyError(kw)

    def term_value(self, w, my, sibs=True):
        """the value of a term (its own key, then its case siblings, T7): pi-7 terms / heading lexicon / pi-1 … pi-6,
        the text's phrase first."""
        keys = [w] + (case_siblings(w) if sibs else [])
        keys += [k.replace("nn", "ṇṇ") for k in keys if "nn" in k]       # pi-1 spells upādiṇṇa (T7)
        for v in gen_values(w):
            if pick_phrase([v], my):
                return v
        for k in keys:
            t = terms().get(k)
            if t and pick_phrase([t], my):
                return t
            h = head_lex().get(k)
            if h:
                v = pick_phrase([x for x, _ in h.most_common()], my)
                if v:
                    return v
            for t_ in PRIOR_ORDER:
                for v, _ in prev_vals(k, t_).most_common():
                    if v != NONE and presence(v, my)[0] and phrase_gap_ok(v, my):
                        return v
                for v, _ in prev_vals(k + " dhammā", t_).most_common():       # pi-1 «X dhammā» (rule 5)
                    if v.endswith(" " + _DHAMMA):
                        v = v[:-len(_DHAMMA) - 1]
                        if presence(v, my)[0] and phrase_gap_ok(v, my):
                            return v
        return None

    def term_values_any(self, w):
        """the term's values in any case (unchecked), most frequent first: for the na-X rule."""
        c = collections.Counter()
        for v in gen_values(w):
            c[v] += 200
        sv = table_get(STOCK, w)
        if isinstance(sv, str) and not sv.startswith("@"):
            c[sv] += 300
        for v in samutthana_cands(w) or ():
            c[v] += 300
        keys = [w] + case_siblings(w)
        keys += [k.replace("nn", "ṇṇ") for k in keys if "nn" in k]
        for k in keys:
            if terms().get(k):
                c[terms()[k]] += 100
            for x, n in head_lex().get(k, {}).items():
                c[x] += 50 * n
            c.update({v: n for v, n in prev_vals(k).items() if v != NONE})
            for v, n in prev_vals(k + " dhammā").items():
                if v.endswith(" " + _DHAMMA):
                    c[v[:-len(_DHAMMA) - 1]] += n
        return [v for v, _ in c.most_common()]

    def term_family(self, kw, my):
        """T7 (case siblings), T8 (na-X) and T12 (a qualifier + a head word)."""
        w = low(kw)
        v = self.term_value(w, my)
        if v is not None:
            return v
        for pre in ("na", "no"):
            if w.startswith(pre) and len(w) > 5:
                x = w[len(pre):]
                for b in [x] + base_forms(x):
                    vals = self.term_values_any(b) + (cluster_cands(b) or []) + (samutthana_cands(b) or [])
                    if not vals and self.stem is not None:
                        v = self.stem(b, flat(my) + " " + my)
                        vals = [v] if v else []
                    # phase 3 fix 6: the plain na-X candidates of every value first; a gapped candidate «Nသော …
                    # မဟုတ်» / «N … မဟုတ်သော» only where no plain na-X form stands in the segment
                    for gapped in (False, True):
                        for v in vals:
                            c = pick_phrase([n for n in neg_term(v) if (" … " in n) == gapped], my)
                            if c is not None:
                                return c
        v = pick_phrase(cluster_cands(w), my)
        if v is not None:
            return v
        return self.head_compound(w, my)

    def qual_values(self, x):
        """the values of a compound's first member x as a qualifier: its term values in any case, the condition name
        (bare, and as an attributive «…သော» for a «…ခြင်း» name)."""
        out = []
        for k in (x, x + "ṃ", x + "o", x + "ā", x[:-1] + "aṃ" if x.endswith("a") else x):
            out += [v for v in self.term_values_any(k) if v not in out]
        if x in N:
            out += [N[x], N[x][:-len("ခြင်း")] + "သော" if N[x].endswith("ခြင်း") else N[x]]
        return [v for v in out if v and " … " not in v]

    def head_compound(self, w, my):
        """T12: «X-adhipati» = «X အကြီးအမှူး» (my7 LEX ārammaṇādhipati «အာရုံ အကြီးအမှူး», sahajātādhipati «အတူ
        ပေါ်ပေါက်သော အကြီးအမှူး»); «X-cittasamaṅgissa» = «X စိတ်နှင့် ပြည့်စုံသူ» (pi-6 R8 -samaṅgī «Xနှင့်
        ပြည့်စုံသူ», agent noun pi-4 P6; rule 1: «၏» goes): the first member's value as a qualifier + the head, as
        the text has it."""
        for head, hv in HEADS:
            if not w.endswith(head) or len(w) <= len(head) + 1:
                continue
            base = w[:-len(head)]
            if head.startswith("ā"):
                xs = [base + "a", base + "u", base + "i", base]
            else:
                xs = [base, base[:-1] + "a" if base.endswith("ā") else base]
            for x in dict.fromkeys(xs):
                for q in self.qual_values(x):
                    cs = [f"{q} {hv}", f"{q}{hv}"]
                    if hv == "အကြီးအမှူး":          # «maggādhipati» «မဂ်ကို အကြီးအမှူးပြုသော» (the triad term)
                        cs.append(f"{q}ကို အကြီးအမှူးပြုသော")
                    c = pick_phrase(cs, my)
                    if c is not None:
                        return c
        return None

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
