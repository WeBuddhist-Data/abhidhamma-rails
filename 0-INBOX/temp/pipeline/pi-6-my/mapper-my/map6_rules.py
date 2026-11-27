"""Shared rules of the pi-6 Pāli→Burmese keyword mapping (Yamaka «အတွဲလိုက် မေးဖြေခြင်း»).

Settled on phase 1 (preamble, 1-mulayamaka, 2-01-khandhayamaka; map_sample.py); imported by the three phase-2 agents
(2-02 … 5-03; 6-01 … 8; 9-01 … 10-13) and the phase-3 consistency scan; phase 3 (2026-11-22) moved the agreed group
overrides in (BOOK) and fixed five mechanics (map-harmonise-notes.md §D, phase3-changes.tsv). NOTHING RUNS ON IMPORT: every file is read
lazily (functools.lru_cache) the first time a function needs it; the module only defines constants, tables and
functions. Copied from pi-5 `pi-5-my/mapper-my/map5_rules.py` (not imported): the loaders, the presence verifier
(pi-1 … pi-5 endings), the lookup engine (Q3 text order, Q4 «လည်း», Q5 negatives, S1 stem fallback, S3 / G3
negatives inside a multiword keyword, G1 / G2 Pāli order), the generic context helpers; the Kathāvatthu tables are
replaced by the Yamaka tables below.

Contents
  paths and loaders          segments(), keyword_rows(), prior() (pi-1 … pi-5 FINAL mappings), terms()
  presence verifier          chunk_present(), presence() (the pi-5 check: pi-1 … pi-5 endings)
  frame / stock tables       FRAME (answers, particles, headings, titles), STOCK (core terms of the book)
  morphology (pi-6)          base_forms()   the «-ti» / «ca» / «ceva» forms of a keyword -> its base form (R1)
                             parse_verb(), verb_cands()  every verb in every tense and polarity (R2)
                             participle_cands()  -anta / -amāna / -itvā (R3)
                             khandha_value(), mula_cands(), Mapper.mulaka()  khandha names; ch. 1 root compounds;
                                            the «(X-mūlakaṃ)» labels (R4)
                             place_cands(), shared_being()  planes and the beings of a plane (R5)
                             heading_value(), title_value()  vāra / naya / uddesa headings, colophons, titles (R6)
                             lad_gap()      the «လည်း» gap inside one value (R7)
                             family_cands() anusaya, sacca, -samaṅgī names (R8)
                             morph_value()  R2-R5 / R8 checked against the segment (pick(): the text's own form)
  context functions          FUNCS[name](kw, pali, my) -> value; a table value «@name» calls one
  BOOK (phase 3)             the phase-2 group rules made book-wide (g1 G1-G11, g2 V1-V7 / O1-O9, g3 W1-W7 / O1-O7):
                             BOOK table, book_auto() (the regex families: vāra names f_vara, cited sections f_aka,
                             citta compounds f_citta, sa-X-ka persons f_saka, feminine participles f_fem), f_nayatana,
                             f_plane_adj; f_rupam (g1 override 1); title_value() for cited titles in any case
  phase-3 mechanics          1 pi_get literal tier needs phrase_ok; 2 base_forms skips finite «-anti» (_finite);
                             3 shared_being only across one other plane; 4 -amāno = person «…ဆဲသူ»; 5 the ending
                             «Xပြီး မဟုတ်» (perf-neg); the spaced negative of a joined compound verb (neg-verb-sp)
  lookup engine              Mapper(tables, ctx).lookup(ch, sid, kw, pali, my): CTX[sid] -> chapter tables -> BOOK ->
                             book_auto() -> FRAME /
                             STOCK -> title -> morphology -> mūlaka labels -> base form (R1) -> pi-6 terms -> a pi-1 … pi-5 value the text has
                             as a phrase -> compose rules -> a pi-1 … pi-5 value present by an ending rule -> stem
                             fallback (S1) -> heading (R6); every value then gets the «လည်း» gap of R7
  verifier                   verify_file(ch, mapped_dir)

Usage in a chapter script (see map_sample.py):
    import map6_rules as R
    M = R.Mapper(chapter_tables={"3-01-ayatanayamaka": T}, ctx=CTX, stem=R.make_stem([R.FRAME, R.STOCK, T]))
    lines, problems, unmapped, nne = M.map_chapter("3-01-ayatanayamaka")
"""
import re
import pathlib
import collections
import functools

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
MY = ROOT / "AI_translation/burmese/pi-6-burmese-plain-zeroshot_split_chapters"
PI = ROOT / "AI_translation/pali/pi-6_split_chapters"
MAPS = {t: ROOT / f"AI_translation/burmese/{t}-keywords-by-reference-pali-burmese-plain.md"
        for t in ("pi-1", "pi-2", "pi-3", "pi-4", "pi-5")}
TERMS_FILE = HERE.parent / "my6-zeroshot-terms.md"
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")
LINE = re.compile(r"^\[([^\]]+)\] (.*)$")
NONE = "(no direct equivalent)"
PUG = "ပုဂ္ဂိုလ်"
# pi-2 first where pi-1 and pi-2 differ (brief), then pi-3, pi-4, pi-5 (the order of the pi-5 mapper, pi-5 added
# before pi-1), then pi-1
PRIOR_ORDER = ("pi-2", "pi-3", "pi-4", "pi-5", "pi-1")

CHAPTERS = ["preamble", "1-mulayamaka", "2-01-khandhayamaka", "2-02-khandhayamaka",
            "3-01-ayatanayamaka", "3-02-ayatanayamaka", "3-03-ayatanayamaka", "3-04-ayatanayamaka",
            "3-05-ayatanayamaka", "3-06-ayatanayamaka", "4-dhatuyamaka",
            "5-01-saccayamaka", "5-02-saccayamaka", "5-03-saccayamaka",
            "6-01-sankharayamaka", "6-02-sankharayamaka"] + \
           [f"7-{i:02d}-anusayayamaka" for i in range(1, 12)] + \
           ["8-cittayamaka", "9-01-dhammayamaka", "9-02-dhammayamaka", "9-03-dhammayamaka"] + \
           [f"10-{i:02d}-indriyayamaka" for i in range(1, 14)]
SAMPLE = ["preamble", "1-mulayamaka", "2-01-khandhayamaka"]


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
    """{tag: {low(kw): Counter(value)}} of the final pi-1 … pi-5 Burmese mappings."""
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
    """my6-zeroshot-terms.md lines «- Pāli = Burmese» -> {low(pāli): burmese}: single forms only (no «/» pairs, no
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
        if re.search(r"[A-Za-zāīūṃṅñṭḍṇḷ;=«»]", b):           # pi-6: a line with several «a = b; c = d» pairs
            continue
        p = re.sub(r"^[0-9-]+\.\s*", "", p)                      # «2-10. Hetuvārādi»
        b = re.sub(r"^[0-9-]+\.\s*", "", b)
        if re.search(r"\b[PQX]\b", p) or len(p.split()) > 4 or "⟦" in b:
            continue
        t.setdefault(low(p), b)
    return t


# =====================================================================================================================
# presence verifier (copy of the pi-5 check, endings unchanged)
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
        return "perf-neg"      # phase 3 mechanic 5 (g2 U4): the negated perfect predicate «Xပြီး မဟုတ်»
    if c.endswith("သည်") and len(c) > 3:
        st = c[:-3]
        if "မ" + st in text:
            return "neg-verb"
        for i in range(0, len(st)):
            if any(st[:i] + "မ" + st[i:] + e in text for e in VERB_FROM):
                return "neg-verb"
        for i in range(1, len(st)):     # phase 3 (g3 U4): a joined compound verb against its spaced negative
            if st[i - 1] != " " and any(st[:i] + " မ" + st[i:] + e in text for e in VERB_FROM):
                return "neg-verb-sp"    # «မျက်မှောက်ပြုခဲ့သည်» / the text's «မျက်မှောက် မပြုခဲ့၊»
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
# frame and stock tables (settled on the sample chapters; see map-table.md for the reasons)
# =====================================================================================================================
# ---- FRAME-BEGIN
# The question / answer machinery of the Yamaka (my6-zeroshot-terms §1-§3): answers, particles, the book and chapter
# titles, the headings that the heading rule (R6) cannot read from the text. Dictionary forms: pi-1 rules 1-11, pi-2
# N1-N11, pi-3 M1-M9, pi-4 P1-P8, pi-5 Q1-Q8 / S1-S6 / G1-G5; the NEW pi-6 rules R1-R9 (map-table.md).
FRAME = {
    NONE: NONE,                                  # a keyword «(no direct equivalent)» of the keyword files
    "Āmantā": "ဟုတ်ပါသည်",                       # pi-5 Q2: the answer formula whole
    "Natthi": "မရှိသည်",                          # pi-1 … pi-5 value (rule 4; the text «မရှိပါ။», ending «ပါ»)
    "No": "မဟုတ်ပါ",                             # the answer «မဟုတ်ပါ။» whole, as Āmantā (Q2)
    "ca": NONE, "pana": NONE, "vā": NONE, "ti": NONE, "pi": NONE, "eva": NONE, "yeva": NONE,
    "Namo": "ရှိခိုးသည်", "bhagavato": "မြတ်စွာဘုရား", "arahato": "ရဟန္တာ",
    "sammāsambuddhassa": "အမှန်ကို ကိုယ်တိုင် အပြည့်အဝ သိမြင်တော်မူသော ဘုရားရှင်",
    "Abhidhammapiṭake": "အဘိဓမ္မာပိဋက",          # pi-1 … pi-5 (rule 1: the final «တွင်» goes)
    "Yamakapāḷi": "အတွဲလိုက် မေးဖြေခြင်း",          # rule 7: the title whole
    # headings the text builds with a number between two parts (R6 reads the others from the text)
    "Hetuvārādi": "အကြောင်းအလိုက် ဖော်ပြချက် စသည်",
    "uddeso": "အကျဉ်း ဖော်ပြချက်", "Uddeso": "အကျဉ်း ဖော်ပြချက်",
    "niddeso": "အကျယ် ဖော်ပြချက်", "Niddeso": "အကျယ် ဖော်ပြချက်",
    "Uddesavāro": "အကျဉ်း ဖော်ပြချက်", "Niddesavāro": "အကျယ် ဖော်ပြချက်",   # colophons «“X” ပြီးဆုံးပြီ»
    "anulomaṃ": "အဟုတ်ပြ ပုံစံ", "paccanīkaṃ": "အငြင်းပြ ပုံစံ",
    "Pavatti": "ဖြစ်ပျက်ခြင်း", "pavatti": "ဖြစ်ပျက်ခြင်း",
}
# Core terms of the book (my6-zeroshot-terms §6-§8), settled on the sample chapters. A tuple = the first value the
# segment has as a phrase, then the first present by an ending rule, else the pi-1 … pi-5 value (alt).
STOCK = {
    # ch. 1 bases (rule 3 / rule 5; pi-1 … pi-5 values)
    "kusalā": "ကုသိုလ်", "kusalaṃ": "ကုသိုလ်", "kusala": "ကုသိုလ်",
    "akusalā": "အကုသိုလ်", "akusalaṃ": "အကုသိုလ်", "akusala": "အကုသိုလ်",
    "abyākatā": "ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော", "abyākataṃ": "ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော",
    "nāmā": "စိတ်ပိုင်း", "nāmaṃ": "စိတ်ပိုင်း", "nāma": "စိတ်ပိုင်း",
    "kusalā dhammā": "ကုသိုလ် သဘောတရား", "akusalā dhammā": "အကုသိုလ် သဘောတရား",
    "abyākatā dhammā": "ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော သဘောတရား", "nāmā dhammā": "စိတ်ပိုင်း သဘောတရား",
    "dhammā": "သဘောတရား",
    "Sahetukaṃ": "အမြစ် ရှိသော", "sahetukā": "အမြစ် ရှိသော", "Ahetukaṃ": "အမြစ် မရှိသော", "ahetukā": "အမြစ် မရှိသော",
    "Mūlaṃ": "အမြစ်", "Mūlāni": "အမြစ်", "mūlāni": "အမြစ်", "mūlaṃ": "အမြစ်", "mūla": "အမြစ်",
    # the hetuvāra list (my6 notes-sample departure 1: each of the ten words its own Burmese)
    "hetu": "@hetu", "hetū": "@hetu", "nidānaṃ": "ဇာစ်မြစ်", "sambhavo": "ဖြစ်တည်ရာ", "pabhavena": "ပေါ်ထွက်ရာ",
    "pabhavo": "ပေါ်ထွက်ရာ", "Samuṭṭhānāhārārammaṇā": "ဖြစ်ပေါ်လာရာ အာဟာရ အာရုံ",   # rule 6: the «၊» of the list goes
    "paccayo": "အထောက်အပံ့", "samudayena": "ဖြစ်ပေါ်ခြင်း", "samudayo": "ဖြစ်ပေါ်ခြင်း",
    "ekato": "တစ်ပြိုင်နက်", "Avasesā": ("ကြွင်းကျန်သော", "ကြွင်းသော"), "avasesā": ("ကြွင်းကျန်သော", "ကြွင်းသော"),
    "ṭhapetvā": "ချန်ထား၍",
    # ch. 2 terms (pi-1 / pi-2 / pi-5 values)
    "Pañcakkhandhā": "အစုအဝေး ငါးပါး", "khandho": "အစုအဝေး", "khandhā": "အစုအဝေး", "khandhe": "အစုအဝေး",
    "khandhaṃ": "အစုအဝေး", "khandhassa": "အစုအဝေး", "khandhānaṃ": "အစုအဝေး",
    "rūpaṃ": "@rupam", "rūpa": "@rupam", "vedanā": "ခံစားမှု", "vedanaṃ": "ခံစားမှု", "saññā": "မှတ်သိမှု",
    "saññaṃ": "မှတ်သိမှု", "saṅkhārā": "ပြုပြင်ဖန်တီးမှု", "saṅkhāre": "ပြုပြင်ဖန်တီးမှု",
    "viññāṇaṃ": "သိစိတ်", "Diṭṭhisaññā": "အယူ ဖြစ်သော မှတ်သိမှု",
    # persons (pi-4 P6 agent nouns «…သူ»; my6-zeroshot-terms §6)
    "pacchimabhavikā": "နောက်ဆုံး ဘဝ ရှိသူ",
    "sabbesaṃ": "အားလုံး", "puggalo": PUG, "puggalā": PUG, "puggalānaṃ": PUG, "puggalassa": PUG,
    "okāso": "နေရာ", "okāse": "နေရာ",
    # recurring keywords of the later chapters, added after the frame-coverage check (frame-coverage.md); the words
    # of the pi-6 text (harmonise-table.tsv B1 moment leads, the persons of ch. 5-10)
    "pavatte": "ဘဝ တည်နေစဉ်",                                   # «ဘဝ တည်နေစဉ် … ခဏ၌» (pavatti, the course of life)
    "uppādakkhaṇe": "ဖြစ်ခြင်း ခဏ", "bhaṅgakkhaṇe": "ပြိုပျက်ခြင်း ခဏ",   # harmonise B1 (rule 1: the final «၌» goes)
    "uppādakkhaṇaṃ": "ဖြစ်ခြင်း ခဏ", "bhaṅgakkhaṇaṃ": "ပြိုပျက်ခြင်း ခဏ",
    "Pacchimabhavikānaṃ": ("နောက်ဆုံး ဘဝ ရှိသူ", "နောက်ဆုံး ဘဝ ရှိသော"),   # «… ရှိသော ယောက်ျားတို့» (rule 3)
    "pacchimabhavikānaṃ": ("နောက်ဆုံး ဘဝ ရှိသူ", "နောက်ဆုံး ဘဝ ရှိသော"),
    "Itaresaṃ": ("အခြားသူ", "အခြား"), "itaresaṃ": ("အခြားသူ", "အခြား"),        # «အခြား ယောက်ျားတို့» (10-09)
    "Itarāsaṃ": ("အခြားသူ", "အခြား"), "itarāsaṃ": ("အခြားသူ", "အခြား"),
    "arahantānaṃ": "ရဟန္တာ", "arahato": "ရဟန္တာ", "arahā": "ရဟန္တာ", "Arahā": "ရဟန္တာ", "arahantaṃ": "ရဟန္တာ",
    "puthujjanā": "ပုထုဇဉ်", "puthujjanānaṃ": "ပုထုဇဉ်", "Puthujjanassa": "ပုထုဇဉ်", "puthujjanassa": "ပုထုဇဉ်",
    "nirodhasamāpannānaṃ": "ချုပ်ငြိမ်းခြင်း သမာပတ်ကို ဝင်စားနေသူ",
    "aggamaggaṃ": "အမြတ်ဆုံး မဂ်", "Aggamaggassa": "အမြတ်ဆုံး မဂ်", "aggamaggassa": "အမြတ်ဆုံး မဂ်",
    "maggaṃ": ("မဂ်", "လမ်း"), "maggassa": ("မဂ်", "လမ်း"), "magga": ("မဂ်", "လမ်း"),
    "pacchimacittaṃ": "နောက်ဆုံး စိတ်", "pacchimacittassa": "နောက်ဆုံး စိတ်", "Pacchimacittassa": "နောက်ဆုံး စိတ်",
    "somanassena": "ဝမ်းမြောက်မှု", "upekkhāya": "ဥပေက္ခာ",       # «…နှင့်အတူ» (harmonise table; pi-5 upekkhāya)
    "pahīno": "ပယ်ပြီးသော", "appahīno": "မပယ်ရသေးသော",            # pi-5 pahīno; the quoted «“မပယ်ရသေး”» (rule 3)
}
# R8 (frame-coverage): the families of compound names whose members the text keeps apart; a value «X သစ္စာ» etc.
SACCA = {"dukkha": "ဒုက္ခ", "samudaya": "ဖြစ်ပေါ်ခြင်း", "nirodha": "ချုပ်ငြိမ်းခြင်း", "magga": "မဂ်"}   # pi-2 / pi-5
SAMANGI = {"aggamagga": "အမြတ်ဆုံး မဂ်", "anāgāmimagga": "အနာဂါမိမဂ်", "magga": "မဂ်", "pacchimacitta": "နောက်ဆုံး စိတ်",
           "citta": "စိတ်", "phala": "ဖိုလ်"}                         # harmonise-table «-samaṅgī = Xနှင့် ပြည့်စုံသူ»
ANUSAYA = {"kāmarāg": "ကာမရာဂ", "paṭigh": "မုန်းတီးမှု", "mān": "မာန", "diṭṭh": "အယူ", "vicikicch": "ယုံမှားမှု",
           "bhavarāg": "ဘဝရာဂ", "avijj": "အမှန်ကို မသိမှု"}       # pi-2 / pi-5 «X ကိန်းအောင်းခြင်း» (the seven anusayā)
_ANUSAYA = re.compile(r"^(kāmarāg|paṭigh|mān|diṭṭh|vicikicch|bhavarāg|avijj)ānusay(o|aṃ|ena|assa|e|ā|ānaṃ)$")
_SACCA = re.compile(r"^(dukkha|samudaya|nirodha|magga)sacc(aṃ|assa|e|ā|ena|āni|ānaṃ|a)$")
_SAMANGI = re.compile(r"^(\w+?)samaṅg(ī|īnaṃ|ino|iṃ|i|issa|īna|īhi)$")


def family_cands(kw):
    """R8: the anusaya names in every case «X ကိန်းအောင်းခြင်း» (pi-2 / pi-5; the case particle goes, rule 1); sacca names «X သစ္စာ» (pi-2 dukkhasaccaṃ «ဒုက္ခ သစ္စာ», pi-5 nirodhasaccaṃ «ချုပ်ငြိမ်းခြင်း သစ္စာ»; the pi-6
    samudaya «ဖြစ်ပေါ်ခြင်း», magga «မဂ်»); a -samaṅgī person «Xနှင့် ပြည့်စုံသူ» (pi-4 P6 agent noun; the text's
    «…နှင့် ပြည့်စုံသူ»), its attributive «…နှင့် ပြည့်စုံသော» before another person noun (rule 3)."""
    w = low(kw)
    for b in [w] + base_forms(w):
        m = _SACCA.match(b)
        if m:
            return [SACCA[m.group(1)] + " သစ္စာ"]
        m = _ANUSAYA.match(b)
        if m:
            return [ANUSAYA[m.group(1)] + " ကိန်းအောင်းခြင်း"]
        m = _SAMANGI.match(b)
        if m and m.group(1) in SAMANGI:
            x = SAMANGI[m.group(1)]
            return [x + "နှင့် ပြည့်စုံသူ", x + "နှင့် ပြည့်စုံသော"]
    return None
NUM_MY = {"eka": "တစ်", "ekassa": "တစ်", "dve": "နှစ်", "dvinnaṃ": "နှစ်", "tayo": "သုံး", "tiṇṇaṃ": "သုံး",
          "cattāro": "လေး", "catunnaṃ": "လေး", "pañca": "ငါး", "pañcannaṃ": "ငါး", "aṭṭha": "ရှစ်",
          "tīṇi": "သုံး", "nava": "ကိုး", "dvīsu": "နှစ်", "tīsu": "သုံး", "catūsu": "လေး", "pañcasu": "ငါး",
          "chasu": "ခြောက်", "sattasu": "ခုနစ်", "aṭṭhasu": "ရှစ်", "navasu": "ကိုး", "dasasu": "ဆယ်", "cha": "ခြောက်",
          "satta": "ခုနစ်", "dasa": "ဆယ်", "catūhi": "လေး", "dvīhi": "နှစ်", "tīhi": "သုံး"}
# ---- FRAME-END


# =====================================================================================================================
# morphology of the Yamaka keywords (pi-6 rules R1-R6; see map-table.md)
# =====================================================================================================================
_V = "aāiīuūeo"


def base_forms(kw):
    """R1: the «-ti» (quotation / question) and «ca / ceva / ñca / ñceva / yeva» forms of a keyword -> candidate base
    forms, in order (the keyword's own value is the base's: the quotative and ca have no Burmese word of their own,
    pi-1 rule 9 / pi-5 Q4). vedanākkhandhoti -> vedanākkhandho; uppajjatīti -> uppajjati; uppajjitthāti ->
    uppajjittha; rūpanti -> rūpaṃ; kusalañca -> kusalaṃ; ekamūlañceva -> ekamūlaṃ; manindriyañca -> manindriyaṃ."""
    out = []
    k = kw

    def add(x):
        if x and x != kw and x not in out:
            out.append(x)
    for suf, rep in (("ñceva", "ṃ"), ("ñcāti", "ṃ"), ("ñca", "ṃ"), ("ṃyeva", "ṃ"), ("yeva", ""), ("ceva", ""),
                     ("cāti", "")):
        if k.endswith(suf) and len(k) > len(suf) + 2:
            add(k[:-len(suf)] + rep)
    if k.endswith("ca") and len(k) > 4 and k[-3] in _V:
        add(k[:-2])
    if k.endswith("ti") and len(k) > 4:
        s = k[:-2]
        if s[-1] in "āīū":
            add(s)
            add(s[:-1] + {"ā": "a", "ī": "i", "ū": "u"}[s[-1]])
        elif s[-1] in "oe":
            add(s)
        elif s.endswith("n") and s[-2] in _V and not _finite(k):
            add(s[:-1] + "ṃ")          # phase 3 mechanic 2: a finite «-anti / -enti / -onti» is not «-aṃ + ti»
    return out


def _finite(w):
    """phase 3 mechanic 2 (g1 override 4, g3 O8): the word is itself a finite verb of R2 (root + finite ending, with
    the negative prefix n- / na-), so its «-anti» is the 3rd plural, not «-aṃ + ti» (parijānanti, nirujjhissanti)."""
    w = low(w)
    cands = [w]
    if w.startswith("n"):
        cands += [w[1:], w[2:], w[3:]] + (["a" + w[2:]] if w.startswith("nā") else [])
    for x in cands:
        for root, _, _ in VERB_ROOTS:
            if x.startswith(root) and any(x[len(root):] == e for e, _ in VERB_ENDS):
                return True
    return False


# ---- R2: verbs of the pavattivāra and the later vāras -----------------------------------------------------------
# root -> (positive stem, negative stem): the forms of the pi-6 text (my6_formulas.py VERB, make_ch3 / ch7a / ch10
# PVERB; pi-1 … pi-5 values where they exist: uppajjati ဖြစ်ပေါ်သည် pi-1 / pi-2 / pi-5, nirujjhati ချုပ်ငြိမ်းသည် pi-2
# / pi-5, pajahati ပယ်သည် pi-5, parijānāti ပိုင်းခြား သိသည် pi-5, bhāveti ပွားများသည် pi-5, sacchikaroti
# မျက်မှောက်ပြုသည် pi-5, paṭilabhati ရရှိသည် pi-2, anuseti ကိန်းအောင်းသည် pi-2, upapajjati ပြန်လည် ဖြစ်ပေါ်သည်
# pi-5, cavati စုတေသည် pi-5)
VERB_ROOTS = [
    ("uppajj", "ဖြစ်ပေါ်", "မဖြစ်ပေါ်"), ("nirujjh", "ချုပ်ငြိမ်း", "မချုပ်ငြိမ်း"),
    ("upapajj", "ပြန်လည် ဖြစ်ပေါ်", "ပြန်လည် မဖြစ်ပေါ်"), ("pajah", "ပယ်", "မပယ်"),
    ("parijān", "ပိုင်းခြား သိ", "ပိုင်းခြား မသိ"), ("bhāv", "ပွားများ", "မပွားများ"),
    ("sacchikar", "မျက်မှောက်ပြု", "မျက်မှောက် မပြု"), ("sacchākā", "မျက်မှောက်ပြု", "မျက်မှောက် မပြု"),
    ("paṭilabh", "ရရှိ", "မရရှိ"), ("anus", "ကိန်းအောင်း", "မကိန်းအောင်း"),
    ("parinibbāy", "ပရိနိဗ္ဗာန် ပြု", "ပရိနိဗ္ဗာန် မပြု"), ("parinibb", "ပရိနိဗ္ဗာန် ပြု", "ပရိနိဗ္ဗာန် မပြု"),
    ("cav", "စုတေ", "မစုတေ"),
]
_ROOT = {r: (p, n) for r, p, n in VERB_ROOTS}
# Pāli finite endings -> tense (longest first); «issānti» / «attha» / «iti» are the text's slips (harmonise A3)
VERB_ENDS = [("issānti", "fut"), ("issanti", "fut"), ("essanti", "fut"), ("issati", "fut"), ("essati", "fut"),
             ("ittha", "past"), ("attha", "past"), ("iṃsu", "past"), ("si", "past"),
             ("anti", "pres"), ("enti", "pres"), ("onti", "pres"), ("ati", "pres"), ("eti", "pres"), ("oti", "pres"),
             ("āti", "pres"), ("iti", "pres"), ("atī", "pres")]
NEG_VERBS = {"မတွေ့ရ"} | {n for _, _, n in VERB_ROOTS} | {n + "ခဲ့" for _, _, n in VERB_ROOTS} | \
            {n + "လိမ့်မည်" for _, _, n in VERB_ROOTS}


def parse_verb(kw):
    """'uppajjati' / 'nuppajjitthāti' / 'na nirujjhissatīti' / 'nappajahati' -> (root, tense, neg), else None."""
    w = low(kw.strip())
    neg = False
    if w.startswith("na "):
        neg, w = True, w[3:]
    for b in [w] + base_forms(w):
        cands = [(b, neg)]
        if b.startswith("n") and not neg:
            cands += [(b[1:], True), (b[2:], True), (b[3:], True)]     # nuppajjati, nappajahati (na + pp)
            if b.startswith("nā"):
                cands.append(("a" + b[2:], True))                       # nānuseti (na + anuseti)
        for x, ng in cands:
            for root, _, _ in VERB_ROOTS:
                if x.startswith(root):
                    rest = x[len(root):]
                    for end, tense in VERB_ENDS:
                        if rest == end:
                            return root, tense, ng
    return None


def verb_cands(root, tense, neg):
    """R2: the dictionary forms of a finite verb (pi-1 rule 4 «…သည်»; future «…လိမ့်မည်» as pi-1 uppajjissati; past
    «…ခဲ့သည်»; the negative = the text's «မ» + verb without «သည်», pi-2 / pi-5 Q5), then the text's other
    constructions of the same verb (rule 3: future participle «…မည့်», the positive «…သော» by the ending rule)."""
    p, n = _ROOT[root]
    if neg:
        return {"pres": [n], "past": [n + "ခဲ့"], "fut": [n + "လိမ့်မည်", n + "မည့်"]}[tense]
    return {"pres": [p + "သည်"], "past": [p + "ခဲ့သည်", p + "ခဲ့သော"],
            "fut": [p + "လိမ့်မည်", p + "မည့်", p + "မည်"]}[tense]


# ---- R3: participles and absolutives ------------------------------------------------------------------------------
PART_ENDS = [("antānaṃ", "person"), ("antīnaṃ", "person"), ("antassa", "person"), ("antiyā", "person"),
             ("antā", "person"), ("ante", "person"), ("anto", "person"),
             ("amānānaṃ", "person"), ("amānassa", "person"), ("amānaṃ", "thing"), ("amāno", "mperson"),
             ("amānā", "thing"), ("amāne", "thing"), ("amāna", "thing"),
             ("itvā", "abs"), ("itvāna", "abs")]


def participle_cands(kw):
    """R3: a present participle = the text's «…ဆဲ» (pi-4 cavamāne «သေဆဲ»); of persons the agent noun «…ဆဲသူ» (pi-4
    P6), else the attributive «…ဆဲ» the text builds without a marker (rule 3: «ပြန်လည် ဖြစ်ပေါ်ဆဲ နောက်ဆုံး ဘဝ
    ရှိသူ»); an absolutive «…၍» (pi-1: absolutives keep «၍»; pi-5 Q1 also against «…ပြီး»)."""
    w = low(kw)
    for b in [w] + base_forms(w):
        for root, p, _ in VERB_ROOTS:
            if b.startswith(root):
                rest = b[len(root):]
                for end, kind in PART_ENDS:
                    if rest == end:
                        if kind == "abs":
                            return [p + "၍"]
                        if kind == "person":
                            return [p + "ဆဲသူ", p + "ဆဲ", p + "ဆဲသော"]
                        if kind == "mperson":      # phase 3 mechanic 4 (g2 O3): -amāno (masc. nom.) is a person
                            return [p + "ဆဲသူ", p + "ဆဲ", p + "ဆဲသော", p + "နေသော"]   # «…ဆဲသူ» where the text has it
                        return [p + "ဆဲ", p + "ဆဲသော", p + "နေသော"]
    return None


# ---- R4: khandha names; the ch. 1 root compounds ---------------------------------------------------------------
KHANDHA = {"rūpa": "ရုပ်", "vedanā": "ခံစားမှု", "saññā": "မှတ်သိမှု", "saṅkhāra": "ပြုပြင်ဖန်တီးမှု",
           "viññāṇa": "သိစိတ်"}                                     # pi-2 ^2-1 (my6-zeroshot-terms §8)
_KH = re.compile(r"^(rūpa|vedanā|saññā|saṅkhāra|viññāṇa)kkhandh(o|aṃ|assa|e|ā|ena|ānaṃ|esu|a)$")


def khandha_value(kw):
    m = _KH.match(low(kw))
    return KHANDHA[m.group(1)] + " အစုအဝေး" if m else None


# bases of ch. 1 (my6-zeroshot-terms §7: before a root «ကုသိုလ်၏»; the abyākata base adjectival, rule 6 without «၊»);
# the stems without their final vowel (kusal-a-mūla, kusal-ā-rammaṇā)
MULA_BASE = [("akusal", "အကုသိုလ်၏", "အကုသိုလ်"), ("kusal", "ကုသိုလ်၏", "ကုသိုလ်"),
             ("abyākat", "ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော", "ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော"),
             ("nām", "စိတ်ပိုင်း၏", "စိတ်ပိုင်း")]
# the hetuvāra synonyms after a base (notes-sample departure 1; my6-zeroshot-terms §7)
HETU_SUF = [("hetū", "အကြောင်း"), ("hetu", "အကြောင်း"), ("nidānā", "ဇာစ်မြစ်"), ("sambhavā", "ဖြစ်တည်ရာ"),
            ("ppabhavā", "ပေါ်ထွက်ရာ"), ("pabhavā", "ပေါ်ထွက်ရာ"), ("samuṭṭhānā", "ဖြစ်ပေါ်လာရာ"),
            ("āhārā", "အာဟာရ"), ("ārammaṇā", "အာရုံ"), ("paccayā", "အထောက်အပံ့"), ("samudayā", "ဖြစ်ပေါ်ခြင်း")]
_MULA = re.compile(r"^(eka|aññamañña)?(mūlamūl|mūl)(ak)?(ā|aṃ|āni|ena|o|e|ānaṃ|assa|a)$")


def mula_cands(kw):
    """R4: the ch. 1 root compounds (my6-zeroshot-terms §7), as candidates (the engine takes the one the text has).
    A root noun predicated of the dhammā = the noun (pi-1 rule 2: the copula «ဖြစ်ကြ» goes; the plural «များ» goes,
    rule 1): kusalamūlā = ကုသိုလ်၏ အမြစ်, kusalamūlamūlā = ကုသိုလ်၏ အမြစ်၏ အမြစ်, aññamaññamūlā = အချင်းချင်း
    အမြစ်; a possessive / «based on» adjective = the attributive «…သော» with its object (rule 3: ekamūlā = တူညီသော
    အမြစ် ရှိသော, kusalamūlakā = ကုသိုလ်၏ အမြစ်ကို အခြေခံသော); the instrumental kusalamūlena = the noun without
    «နှင့်» (rule 1); -samuṭṭhāna «Xမှ ဖြစ်ပေါ်လာသော» (pi-1 cittasamuṭṭhāna); -mūlasahajātā «X၏ အမြစ်နှင့်အတူ
    ပေါ်ပေါက်သော» (pi-5 sahajāta); the hetuvāra X-hetū … X-samudayā = «X၏ Y» (each synonym its own word)."""
    w = low(kw)
    for st, gen, plain in MULA_BASE:
        if w.startswith(st) and w[len(st):len(st) + 1] in ("a", "ā"):
            rest = w[len(st):]
            suf = rest[1:] if rest[0] == "a" else rest
            out = []
            if re.match(r"^mūlasahajāt(ā|aṃ|o|ānaṃ|a|e)$", suf):
                out.append(f"{gen} အမြစ်နှင့်အတူ ပေါ်ပေါက်သော")
            for h, my in HETU_SUF:
                if suf == h:
                    out.append(f"{gen} {my}")
            if re.match(r"^samuṭṭhān(aṃ|ā|o|a)$", suf):
                out.append(f"{plain}မှ ဖြစ်ပေါ်လာသော")
            m = _MULA.match(suf)
            if m and not m.group(1):
                core = "အမြစ်၏ အမြစ်" if m.group(2) == "mūlamūl" else "အမြစ်"
                out.append(f"{gen} {core}" + ("ကို အခြေခံသော" if m.group(3) else ""))
            return out or None
    m = _MULA.match(w)
    if not m:
        return None
    core = "အမြစ်၏ အမြစ်" if m.group(2) == "mūlamūl" else "အမြစ်"
    if m.group(1) == "eka":
        return ["တူညီသော " + core + ("ကို အခြေခံသော" if m.group(3) else " ရှိသော")]
    if m.group(1) == "aññamañña":
        return ["အချင်းချင်း " + core + ("ကို အခြေခံသော" if m.group(3) else "")]
    return [core + ("ကို အခြေခံသော" if m.group(3) else "")]


# ---- R5: planes and the beings of a plane -------------------------------------------------------------------------
# my6-zeroshot-terms §6 (pi-2 ^2-234 vokāra planes, pi-2 asaññasatta, pi-5 arūpa «ရုပ်မရှိသော ဘုံ»); the later
# chapters' planes from the harmonise table (kāma- «ကာမဘုံ», rūpāvacara «သိမ်မွေ့သော ရုပ်ဘုံ»)
PLACES = [("pañcavokār", "အစုအဝေး ငါးပါး ရှိသော ဘဝ"), ("catuvokār", "အစုအဝေး လေးပါး ရှိသော ဘဝ"),
          ("ekavokār", "အစုအဝေး တစ်ပါး ရှိသော ဘဝ"), ("asaññasatt", "အသညသတ် ဘုံ"),
          ("suddhāvās", "သုဒ္ဓါဝါသ ဘုံ"), ("arūpāvacar", "ရုပ်မရှိသော ဘုံ"), ("rūpāvacar", "သိမ်မွေ့သော ရုပ်ဘုံ"),
          ("kāmāvacar", "ကာမဘုံ"), ("arūpadhāt", "ရုပ်မရှိသော ဘုံ"), ("rūpadhāt", "သိမ်မွေ့သော ရုပ်ဘုံ"),
          ("kāmadhāt", "ကာမဘုံ"), ("arūp", "ရုပ်မရှိသော ဘုံ")]
BEINGS = {"asaññasatt": "အသညသတ်"}                 # pi-2 Asaññasattā / asaññasattānaṃ = အသညသတ် (the beings)
_PLACE_END = re.compile(r"^(a|aṃ|e|ā|o|uyā|u|ū|esu|ūsu|ānaṃ|assa|ehi|ūnaṃ|ānaṃ)$")


def place_cands(kw):
    """R5: a plane in any case = the plane's name without the case particle (rule 1: «…၌ / …မှ» go); the beings of a
    plane (gen. pl. -ānaṃ / -assa) = the text's «P၌ ရှိသူ» (agent noun, pi-4 P6), its attributive «P၌ ရှိသော» before
    another person noun (rule 3: «… ဘဝ၌ ရှိသော အခြားသူ»), the beings' own name (asaññasattānaṃ = အသညသတ်, pi-2), the
    shared «P … ရှိသူ» of two coordinated planes (shared_being), the attributive «Pနှင့် ဆိုင်သော» (kāmāvacarānaṃ
    pacchimacittaṃ «ကာမဘုံနှင့် ဆိုင်သော နောက်ဆုံး စိတ်», rule 3), else the plane."""
    w = low(kw)
    for b in [w] + base_forms(w):
        for st, p in PLACES:
            if b.startswith(st) and _PLACE_END.match(b[len(st):]):
                end = b[len(st):]
                if end in ("ānaṃ", "assa"):
                    return ([BEINGS[st]] if st in BEINGS else []) + [p + "၌ ရှိသူ", p + "၌ ရှိသော",
                                                                       ("@shared", p), p + "နှင့် ဆိုင်သော", p]
                if st in BEINGS and end == "ā":
                    return [p, BEINGS[st]]
                return [p]
    return None


def shared_being(p, my):
    """R5: the beings of two coordinated planes share one «…၌ ရှိသူ / ရှိသော» («သိမ်မွေ့သော ရုပ်ဘုံနှင့် ရုပ်မရှိသော ဘုံ၌
    ရှိသူတို့»): the first plane's value = «P … ရှိသူ» (pi-1 rule 10, the discontinuous part; pi-5 Q4)."""
    # phase 3 mechanic 3 (g2 O2, ^6-6-47): the words between «Pနှင့်» and «၌ ရှိသူ» must be ONE other plane, so the
    # shared ending stays inside the coordinated noun phrase (not «ကာမဘုံနှင့် ဆိုင်သော … ဘုံ၌ ရှိသူ» across a clause)
    other = "|".join(re.escape(q) for q in sorted({q for _, q in PLACES if q != p}, key=len, reverse=True))
    m = re.search(re.escape(p) + r"နှင့် (?:" + other + r")၌ (ရှိသူ|ရှိသော)", my)
    return f"{p} … {m.group(1)}" if m else None


# ---- R6: headings (vāra / naya / uddesa / niddesa) and titles -----------------------------------------------------
_LABEL = re.compile(r"\((?:[A-ZĀĪŪṄÑṬḌṆḶa-zāīūṅñṭḍṇḷṃ]{1,4}|[က-အ]|\d+)\)|\b\d+(?:-\d+)?\.|[0-9၀-၉]+(?:-[0-9၀-၉]+)?\.")
HEAD_END = re.compile(r"(vāro|vāra|vāre|vāraṃ|nayo|naya|uddeso|niddeso|niddesa|uddesa|ādi|yamakaṃ|pāḷi|kaṃ)$")


def heading_parts(text):
    """the parts of a heading line between its labels «(Ka) / (က) / (1) / 2.»."""
    t = re.sub(r"^#+\s*", "", text.strip())
    return [p.strip(" .။") for p in _LABEL.split(t) if p.strip(" .။")]


def heading_value(kw, pali, my):
    """R6 (pi-1 rule 7: a heading keyword that IS a whole heading part gets the text's whole part): the Burmese part
    at the same position as the Pāli part that is the keyword; the colophon «X niṭṭhito» = the text's title inside
    «“ … ”» (pi-2 ^2-153)."""
    if not HEAD_END.search(low(kw)):
        return None
    if pali.lstrip().startswith("#"):
        pp, mp = heading_parts(pali), heading_parts(my)
        if len(pp) == len(mp):
            for a, b in zip(pp, mp):
                if low(a) == low(kw):
                    return b
    m = re.search(re.escape(kw) + r"\s+niṭṭhit", pali, flags=re.I)
    if m:
        q = re.findall(r"“([^”]+)”\s*(?:ကျမ်း )?ပြီးဆုံးပြီ", my)
        if len(q) == 1:
            return q[0]
    return None


@functools.lru_cache(maxsize=None)
def topics():
    """my6-zeroshot-terms §1: {Xyamakaṃ: «Xများကို အတွဲလိုက် မေးဖြေခြင်း»} (the approved and the PROPOSED names)."""
    out = {}
    for l in TERMS_FILE.read_text(encoding="utf-8").splitlines():
        if l.startswith("- Xyamakaṃ"):
            for m in re.finditer(r"(\w+yamakaṃ) = ([^;(]+?)(?: \(PROPOSED\))?(?:;|$)", l):
                out[low(m.group(1))] = m.group(2).strip()
    return out


def title_value(kw, my):
    """rule 7: a chapter title Xyamakaṃ / Xyamakapāḷi (and, phase 3, the cited title in any case: āyatanayamake,
    dhātuyamakampi, khandhayamake, dhammayamakanti …) = the approved title whole."""
    # phase 3 (g1 G9, g2 V7 book-wide): a chapter title cited in a note in any case = the approved title whole
    m = re.match(r"^(\w+yamak)(aṃ|apāḷi|e|epi|assa|ampi|anti|añca)$", low(kw))
    if not m:
        return None
    t = topics().get(m.group(1) + "aṃ")
    return t if t and t in my else None




# =====================================================================================================================
# context helpers (copied from pi-5 map5_rules.py, unchanged)
# =====================================================================================================================

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
    first present by the ending rules, else the pi-1 … pi-5 value (one sense per segment, the text's own word)."""
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
    """value where the text has the Burmese word, else other (default: the pi-1 … pi-5 value present)."""
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



def pick(cands, my):
    """the first candidate the segment's Burmese has as a phrase (its final «သည် / သော» by an ending rule), then the
    first present by the ending rules; None where none is (one form per segment, the text's own form)."""
    if not cands:
        return None
    for v in cands:
        if v == NONE or (presence(v, my)[0] and (phrase_ok(v, my) or phrase_ok(v, flat(my)))):
            return v
    for v in cands:
        if presence(v, my)[0]:
            return v
    return None


def flat(my):
    """the text without the list comma «၊» (pi-1 rule 6: the «၊» inside a term is dropped in the value)."""
    return my.replace("၊ ", " ").replace("၊", "")


def morph_value(kw, pali, my):
    """R2-R5 (and R1 for each): the morphological value of a keyword, checked against the text; None if the keyword
    is not of these shapes or no form is in the text. -> (value, source)"""
    if " " in kw and not low(kw).startswith("na "):
        return None, None                     # a multiword keyword goes through compose (Q3)
    pv = parse_verb(kw)
    if pv:
        v = pick(verb_cands(*pv), my)
        if v:
            return v, "verb"
    pc = participle_cands(kw)
    if pc:
        v = pick(pc, my)
        if v:
            return v, "verb"
    for b in [kw] + base_forms(kw):
        v = khandha_value(b)
        if v and presence(v, my)[0]:
            return v, "khandha"
        v = pick(mula_cands(b), my)
        if v:
            return v, "mula"
    fc = family_cands(kw)
    if fc:
        v = pick(fc, my)
        if v:
            return v, "family"
    pl = place_cands(kw)
    if pl:
        pl = [shared_being(c[1], my) if isinstance(c, tuple) else c for c in pl]
        v = pick([c for c in pl if c], my)
        if v:
            return v, "place"
    return None, None


# ---- FUNCS-BEGIN


_FREE_RUPA = re.compile("ရုပ်(?!မရှိ|ဘုံ| မရှိ| ရှိလျက်| အစုအဝေး)")


def f_rupam(kw, pali, my):
    """rūpa: matter «ရုပ်» (pi-1 / pi-2 / pi-5); the visible object «အဆင်းအရောင်» (pi-1 / pi-5 rūpāyatana,
    rūpārammaṇa) where the Pāli has the āyatana / object sense and the text that word; one sense per segment.
    Phase 3 (g1 override 1, f_rupam_g1, book-wide): in the āyatana / dhātu padasodhana «rūpaṃ rūpāyatanaṃ?» the text
    has «ရုပ်သည် အဆင်းအရောင် အာရုံခံ နယ်ပယ် …»: «အဆင်းအရောင်» is the word of the keyword rūpāyatanaṃ, so the bare rūpaṃ is
    «ရုပ်» wherever the text has a free «ရုပ်» (not inside «ရုပ်မရှိသော ဘုံ / ရုပ်ဘုံ / ရုပ် မရှိ / ရုပ် ရှိလျက် / ရုပ်
    အစုအဝေး»)."""
    if _FREE_RUPA.search(my):
        return "ရုပ်"
    if re.search(r"rūpāyatan|rūpārammaṇ|rūpadhātu(?!yā)|rūpāni passati|cakkhunā rūpaṃ", strip_brackets(pali), re.I) \
            and "အဆင်းအရောင်" in my:
        return "အဆင်းအရောင်"
    if "ရုပ်" in my:
        return "ရုပ်"
    return "@prior"


FUNCS = {
    # hetu: «အကြောင်း» (the hetuvāra list, notes-sample departure 1; pi-4 / pi-5 «အကြောင်း»); else the pi-1 … pi-5
    # value the text has («အမြစ်»: ahetuka / sahetuka)
    "hetu": lambda kw, pali, my: "အကြောင်း" if "အကြောင်း" in my else "@prior",
    "rupam": f_rupam,
}
# ---- FUNCS-END



# =====================================================================================================================
# alt values
# =====================================================================================================================
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
# BOOK: the phase-2 group rules and module overrides, made book-wide in phase 3 (coordinator decisions 2026-11-22:
# g1 G1-G11 and T_ALL / FUNCS_G1, g2 V1-V7 and O1-O9, g3 W1-W7 and O1-O7; notes-g1 / notes-g2 / notes-g3). A keyword
# that occurs in ONE segment of the book only stays a per-segment rule (CTX) in its group script.
# =====================================================================================================================
# ---- R6 in a body line (g1 G1, g2 V1, g3 W7): a vāra named in a colophon / note «X-vāro / -vāre / -vārepi / -vāraṃ /
# -vārena» = «Xအလိုက် ဖော်ပြချက်» (rule 7; rule 1: the case particle goes; Q4: api «လည်း» goes); a heading line keeps the
# heading rule's whole part (R6)
VARA = {"uppādavāranirodha": "ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် ချုပ်ငြိမ်းခြင်း",
        "uppādanirodha": "ဖြစ်ပေါ်ခြင်းနှင့် ချုပ်ငြိမ်းခြင်း", "uppāda": "ဖြစ်ပေါ်ခြင်း", "nirodha": "ချုပ်ငြိမ်းခြင်း",
        "uppajjana": "ဖြစ်ပေါ်ခြင်း", "pariññā": "ပိုင်းခြား သိခြင်း", "pahīna": "ပယ်ပြီး ဖြစ်ခြင်း",
        "pajahana": "ပယ်ခြင်း", "sānusaya": "ကိန်းအောင်းခြင်း ရှိသူ", "anusaya": "ကိန်းအောင်းခြင်း",
        "uppattiṭṭhāna": "ဖြစ်ပေါ်ရာ နေရာ", "puggala": "ပုဂ္ဂိုလ်", "dhamma": "သဘောတရား",
        "puggaladhamma": "ပုဂ္ဂိုလ်နှင့် သဘောတရား", "paṇṇatti": "သတ်မှတ်ချက်", "pavatti": "ဖြစ်ပျက်ခြင်း",
        "bhāvanā": "ဘာဝနာ ပွားများခြင်း"}
_VARA = re.compile(r"^(\w+?)vār(o|e|epi|aṃ|ena|a|ampi)$")


def vara_value(kw):
    m = _VARA.match(low(kw))
    if not m or m.group(1) not in VARA:
        return None
    return VARA[m.group(1)] + "အလိုက် ဖော်ပြချက်"


def f_vara(kw, pali, my):
    if pali.lstrip().startswith("#"):
        h = heading_value(kw, pali, my)
        if h:
            return h
    v = vara_value(kw)
    if v and (phrase_ok(v, my) or phrase_ok(v, flat(my))):
        return v
    h = heading_value(kw, pali, my)
    return h if h else "@prior"


# ---- the editorial sections yassaka / yatthaka / yassayatthaka (g1 G2, g2 V3) = «Q အပိုင်း» with the cited question
# word of the text's quotation «“အကြင်သူအား” / “အကြင်နေရာ၌” / “အကြင်သူအား အကြင်နေရာ၌” အပိုင်း» (the cited word keeps its
# «အား / ၌», rule 1 inner particles; the quotation marks, the final «၌ / တွင် / ကို / များ» and the «လည်း» of -pi go, g2 U2
# decided); X-sadisaṃ «Q အပိုင်းနှင့် တူညီသည်» (rule 4), the text's adverbial «…နှင့် တူညီအောင်» where it has that; a
# keyword only inside a Roman-script variant = (no direct equivalent) (pi-3 M2)
AKA_Q = {"yassa": "အကြင်သူအား", "yattha": "အကြင်နေရာ၌", "yassayattha": "အကြင်သူအား အကြင်နေရာ၌"}
_AKA = re.compile(r"^(yassa ?yattha|yassa|yattha)k(aṃ|am|ā|ānaṃ|e|a|o)(pi)?(sadis(aṃ|o|ā))?$")


def f_aka(kw, pali, my):
    m = _AKA.match(low(kw))
    if not m:
        return "@prior"
    if not pali_has(kw, pali):
        return NONE
    v = AKA_Q[m.group(1).replace(" ", "")] + " အပိုင်း"
    if m.group(4):
        for end in ("နှင့် တူညီသည်", "နှင့် တူညီအောင်"):
            if presence(v + end, my)[0] and phrase_ok(v + end, re.sub("[“”]", "", my)):
                return v + end
        return v + "နှင့် တူညီသည်"
    return v


# ---- X-sampayutta / X-vippayutta citta compounds and their moments (g1 G5, g3 W1): «Xနှင့် ယှဉ်တွဲသော / ကင်းကွာသော စိတ် /
# နောက်ဆုံး စိတ်» (pi-1 rule 3, pi-1 ^1-1 «…နှင့် ယှဉ်တွဲသော», pi-2 ^2-767 «…နှင့် ကင်းကွာသော»); two members «Aနှင့် … ၍
# Bနှင့် … သော» (the text's absolutive); -pacchimacittasamaṅgī «… နောက်ဆုံး စိတ်နှင့် ပြည့်စုံသူ» (R8); upapatticitta
# «ပြန်လည် ဖြစ်ပေါ်ခြင်း စိတ်»; with a moment «… စိတ်၏ ဖြစ်ခြင်း ခဏ / ပြိုပျက်ခြင်း ခဏ» (harmonise B1: the final «၌» goes)
CMEM = {"taṇhā": "တပ်မက်မှု", "magga": "မဂ်", "kusala": "ကုသိုလ်", "akusala": "အကုသိုလ်", "saddhā": "ယုံကြည်မှု",
        "somanassa": "ဝမ်းမြောက်မှု", "upekkhā": "ဥပေက္ခာ", "ñāṇa": "ဉာဏ်"}
_CMX = "(akusala|kusala|taṇhā|magga|saddhā|somanassa|upekkhā|ñāṇa)(sampayutta|vippayutta)"
_CITTA = re.compile(r"^((?:" + _CMX.replace("(", "(?:") + r")+)(pacchimacittasamaṅg|pacchimacitt|citt)"
                    r"(īnaṃ|ī|assa|aṃ|e|ānaṃ|a)$")
MOMENT = {"uppādakkhaṇe": "ဖြစ်ခြင်း ခဏ", "bhaṅgakkhaṇe": "ပြိုပျက်ခြင်း ခဏ"}


def citta_value(w):
    w = low(w)
    if re.match(r"^upapatticitt(assa|e|aṃ)$", w):
        return "ပြန်လည် ဖြစ်ပေါ်ခြင်း စိတ်"
    m = _CITTA.match(w)
    if not m:
        return None
    mem = re.findall(_CMX, m.group(1))
    parts = [CMEM[x] + "နှင့် " + ("ယှဉ်တွဲ" if y == "sampayutta" else "ကင်းကွာ") for x, y in mem]
    head = {"citt": "စိတ်", "pacchimacitt": "နောက်ဆုံး စိတ်", "pacchimacittasamaṅg": "နောက်ဆုံး စိတ်နှင့် ပြည့်စုံသူ"}
    return " ".join(p + "၍" for p in parts[:-1]) + (" " if len(parts) > 1 else "") + parts[-1] + "သော " + \
        head[m.group(2)]


def f_citta(kw, pali, my):
    ws = kw.split()
    c = citta_value(ws[0])
    if c is None:
        return "@prior"
    if len(ws) == 2 and low(ws[1]) in MOMENT:
        return c + "၏ " + MOMENT[low(ws[1])]
    return c


# ---- sa-X-ka / a-X-ka persons (g1 G3, g3 W2; g1 U2 decided): the dictionary adjective «X ရှိသော / X မရှိသော» (pi-1
# rule 3 as Sahetukaṃ «အမြစ် ရှိသော»; the text's «X ရှိလျက် / X မရှိဘဲ» by the ending rule, pi-2 N11); arūpaka «ရုပ်
# မရှိသော» (the person without matter, not the plane)
SAKA = {"cakkhuk": "မျက်စိ", "sotak": "နား", "ghānak": "နှာခေါင်း", "jivhak": "လျှာ", "kāyak": "ကိုယ်",
        "rūpak": "ရုပ်", "cittak": "စိတ်"}
_SAKA = re.compile(r"^(sa|a)(cakkhuk|sotak|ghānak|jivhak|kāyak|rūpak|cittak)(ānaṃ|ā|assa|o|aṃ|e)$")


def f_saka(kw, pali, my):
    m = _SAKA.match(low(kw))
    if not m:
        return "@prior"
    return SAKA[m.group(2)] + (" ရှိသော" if m.group(1) == "sa" else " မရှိသော")


def f_nayatana(kw, pali, my):
    """g1 G4 (U1 decided): na + āyatana in one Pāli word (pi-1 / pi-2 nariya «အရိယာ မဟုတ်သော»): the subject nāyatanā
    «အာရုံခံ နယ်ပယ်တို့ မဟုတ်သော အရာ» = the gapped «အာရုံခံ နယ်ပယ် … မဟုတ်သော» (rule 1: no plural marker in a value); the
    predicate «… အာရုံခံ နယ်ပယ် မဟုတ်သလော» = «အာရုံခံ နယ်ပယ် မဟုတ်» (pi-1 rule 5, Q5)."""
    subj, pred = "အာရုံခံ နယ်ပယ် … မဟုတ်သော", "အာရုံခံ နယ်ပယ် မဟုတ်"
    if low(kw) == "nāyatanā":
        if "အာရုံခံ နယ်ပယ်တို့ မဟုတ်သော" in my:
            return subj
        return "အာရုံခံ နယ်ပယ် မဟုတ်သော" if "အာရုံခံ နယ်ပယ် မဟုတ်သော" in my else pred
    return pred if pred in my else subj


def f_plane_adj(kw, pali, my):
    """g2 V6 / O2: a plane genitive plural before «pacchimacittaṃ» («yassa cittassa anantarā kāmāvacarānaṃ
    pacchimacittaṃ») is the text's adjective «Pနှင့် ဆိုင်သော» (harmonise A2) where the keyword's FIRST occurrence in the
    segment stands there (one sense per segment); elsewhere the beings of R5."""
    base = place_cands(kw)
    m = re.search(r"(?<![\wāīūṃṅñṭḍṇḷ])" + re.escape(kw) + r"(?![\wāīūṃṅñṭḍṇḷ])( pacchimacittaṃ)?", strip_brackets(pali))
    if base and m and m.group(1):
        p = base[-1]
        if p + "နှင့် ဆိုင်သော" in my:
            return p + "နှင့် ဆိုင်သော"
    v = morph_value(kw, pali, my)[0]
    return v if v else "@prior"


def f_fem(kw, pali, my):
    """g3 W3: a feminine participle -antīnaṃ «itthīnaṃ upapajjantīnaṃ» «ပြန်လည် ဖြစ်ပေါ်ဆဲ မိန်းမတို့» = the attributive
    «Sဆဲ» before the noun (R3); after a relative «… tāsaṃ upapajjantīnaṃ» «…မိန်းမတို့အနက် ပြန်လည် ဖြစ်ပေါ်ဆဲသူတို့» the
    agent noun; the keyword's FIRST occurrence decides (one sense per segment)."""
    pc = participle_cands(kw)
    if not pc:
        return "@prior"
    m = re.search(r"(\S+)\s+" + re.escape(kw) + r"(?![\wāīūṃṅñṭḍṇḷ])", strip_brackets(pali))
    attr = pc[1]
    if m and m.group(1).lower() != "tāsaṃ" and re.search(re.escape(attr) + " (?!သူ)", my):
        return attr
    for v in pc:
        if presence(v, my)[0] and phrase_ok(v, my):
            return v
    return "@prior"


FUNCS.update({"vara": f_vara, "aka": f_aka, "citta": f_citta, "saka": f_saka, "nayatana": f_nayatana,
              "plane_adj": f_plane_adj, "fem": f_fem})

SV = "စတင်ကြံစည်မှုနှင့် ဆက်လက်သုံးသပ်မှု ရှိ"                 # g2 V4 (pi-1 ^1-M1-6 savitakkasavicāra)
AV = "စတင်ကြံစည်မှုလည်း မရှိ ဆက်လက်သုံးသပ်မှုလည်း မရှိ"          # pi-1 ^1-1401 (rule 6: the «၊» goes)
KS = "ကိုယ်၏ ပြုပြင်ဖန်တီးမှု"                                   # g2 O1 (= vacī- / cittasaṅkhāro «နှုတ်၏ / စိတ်၏»)
UPNI = {"uppād": "ဖြစ်ပေါ်ခြင်း", "nirodh": "ချုပ်ငြိမ်းခြင်း", "uppādanirodh": "ဖြစ်ပေါ်ခြင်းနှင့် ချုပ်ငြိမ်းခြင်း"}
PAT = "အငြင်းပြ ပုံစံ"
AÑÑA = "အပြည့်အဝ သိမြင်ခြင်း"                     # g3 W4: the pi-2 faculty name without «၏ စွမ်းရည်»
ANAÑÑA = "မသိရသေးသည်ကို သိရတော့မည်ဟူသော"          # g3 W4 / U1: without the text's added head noun «အရာ»
AÑÑĀTĀVĪ = "အပြည့်အဝ သိမြင်ပြီးသူ"                 # pi-5 aññātāvī
# ---- BOOK-BEGIN
BOOK = {
    # g1 override 1: rūpaṃ (f_rupam) is the module STOCK value; yattha «where» (g1 G8, g2 O6, g3 O6; U3 decided)
    "yattha": "အကြင်နေရာ", "Yattha": "အကြင်နေရာ", "Yassa yattha": "အကြင်သူအား အကြင်နေရာ",
    # g1 G1: the bare action nouns of a vāra note (Q4: the «လည်း» of pi goes; rule 1: the «၌»)
    "uppādanirodhepi": UPNI["uppādanirodh"],
    # g1 G7: cakka = the round «လှည့်ပတ်ခြင်း» (the phase-1 headings «…cakkavāro = … လှည့်ပတ်ခြင်း ဖော်ပြချက်»)
    "Cakkaṃ": "လှည့်ပတ်ခြင်း", "cakkaṃ": "လှည့်ပတ်ခြင်း",
    # g1 G6: the non-āyatana kinds of sota / gandha / rasa = «X၏ Y» (rule 1 the inner «၏»)
    "taṇhāsotaṃ": "တပ်မက်မှု ရေစီး",
    "Sīlagandho": "သီလ၏ အနံ့", "samādhigandho": "သမာဓိ၏ အနံ့", "paññāgandho": "ပညာ၏ အနံ့",
    "Attharaso": "အနက်၏ အရသာ", "dhammaraso": "တရား၏ အရသာ", "vimuttiraso": "လွတ်မြောက်မှု၏ အရသာ",
    # g1 G4: na + āyatana (f_nayatana)
    "nāyatanā": "@nayatana", "nāyatanaṃ": "@nayatana", "nāyatananti": "@nayatana",
    # g1 G10: the persons of ch. 5 (the agent noun, its attributive before another person noun; rule 3 / P6)
    "caññe": ("အခြားသူ", "အခြား"),
    "Abhisametāvīnaṃ": ("ထင်ထင်ရှားရှား သိမြင်ပြီးသူ", "ထင်ထင်ရှားရှား သိမြင်ပြီးသော"),
    "abhisametāvīnaṃ": ("ထင်ထင်ရှားရှား သိမြင်ပြီးသူ", "ထင်ထင်ရှားရှား သိမြင်ပြီးသော"),
    "Anabhisametāvīnaṃ": ("ထင်ထင်ရှားရှား မသိမြင်ရသေးသူ", "ထင်ထင်ရှားရှား မသိမြင်ရသေးသော"),
    "anabhisametāvīnaṃ": ("ထင်ထင်ရှားရှား မသိမြင်ရသေးသူ", "ထင်ထင်ရှားရှား မသိမြင်ရသေးသော"),
    "āpāyikānaṃ": ("အပါယ်၌ ရှိသူ", "အပါယ်၌ ရှိသော"), "Āpāyikānaṃ": ("အပါယ်၌ ရှိသူ", "အပါယ်၌ ရှိသော"),
    "aggaphalassa": "အမြတ်ဆုံး ဖိုလ်", "aggaphalaṃ": "အမြတ်ဆုံး ဖိုလ်",       # agga- pi-2 ^2-1029
    # g2 V6: the plane genitive plural before pacchimacittaṃ (f_plane_adj)
    "kāmāvacarānaṃ": "@plane_adj", "rūpāvacarānaṃ": "@plane_adj", "arūpāvacarānaṃ": "@plane_adj",
    # g2 O1 (with mechanic 1): kāyasaṅkhāra = the text's «ကိုယ်၏ ပြုပြင်ဖန်တီးမှု»
    "kāyasaṅkhāro": KS, "kāyasaṅkhāraṃ": KS, "kāyasaṅkhārassa": KS, "kāyasaṅkhārā": KS,
    "vaciṃ": "နှုတ်",                                       # Vaciñca (R1) = vacī «နှုတ်» (pi-5)
    "tesaṃyeva": "ထိုသူ",                                   # g2 U6 decided: R1 = tesaṃ «ထိုသူ», rule 1
    # g2 V4: vitakka / vicāra qualifiers
    "avitakkaavicāraṃ": AV + "သော", "Avitakkaavicāraṃ": AV + "သော",
    "avitakkaavicāracittassa uppādakkhaṇe": AV + "သော စိတ်၏ ဖြစ်ခြင်း ခဏ",
    "avitakkaavicāracittassa bhaṅgakkhaṇe": AV + "သော စိတ်၏ ပြိုပျက်ခြင်း ခဏ",
    "Savitakkasavicārapacchimacittassa uppādakkhaṇe": SV + "သော နောက်ဆုံး စိတ်၏ ဖြစ်ခြင်း ခဏ",
    "Savitakkasavicārapacchimacittassa bhaṅgakkhaṇe": SV + "သော နောက်ဆုံး စိတ်၏ ပြိုပျက်ခြင်း ခဏ",
    "Avitakkaavicārapacchimacittassa uppādakkhaṇe": AV + "သော နောက်ဆုံး စိတ်၏ ဖြစ်ခြင်း ခဏ",
    "Avitakkaavicārapacchimacittassa bhaṅgakkhaṇe": AV + "သော နောက်ဆုံး စိတ်၏ ပြိုပျက်ခြင်း ခဏ",
    "avitakkaavicārapacchimacittasamaṅgīnaṃ": AV + "သော နောက်ဆုံး စိတ်နှင့် ပြည့်စုံသူ",
    "Savitakkasavicārabhūmiyaṃ": SV + "ရာ အဆင့်", "Avitakkaavicārabhūmiyaṃ": AV + "ရာ အဆင့်",
    "Savitakkasavicārapacchimacittassa": SV + "သော နောက်ဆုံး စိတ်", "Avitakkaavicārapacchimacittassa": AV + "သော နောက်ဆုံး စိတ်",
    # g2 O8: samāpannānaṃ = the agent noun «… ဝင်စားနေသူ» (P6), its attributive before a noun
    "samāpannānaṃ": ("ဝင်စားနေသူ", "ဝင်စားနေသော"),
    # g2 V7: paṭiloma = paccanīka «အငြင်းပြ ပုံစံ»; the na-plane labels; other ch. 7 values
    "paṭilomaṃ": PAT, "paṭilomapuggalo": "ပုဂ္ဂိုလ်အလိုက် " + PAT, "paṭilomaokāso": "နေရာအလိုက် " + PAT,
    "paṭilomapuggalokāsā": "ပုဂ္ဂိုလ်နှင့် နေရာအလိုက် " + PAT,
    "kāmārāgānusayo": "ကာမရာဂ ကိန်းအောင်းခြင်း",           # the source slip (kāmā-) of kāmarāgānusayo (R8)
    "bhaṅgā": "ပြိုပျက်သော",                                # g2 U7 decided: the dictionary form (rule 3)
    "pahīnā": "ပယ်ပြီးသော", "appahīnā": "မပယ်ရသေးသော",       # g2 O4 (STOCK pahīno / appahīno)
    # g2 O3 upapajjamāno: now mechanic 4 of participle_cands (no table entry)
    "kāmadhātuṃyeva": "ကာမဘုံ",                              # R1 (eva «ပင်» goes)
    "Nakāmadhātumūlakaṃ": "ကာမဘုံ မဟုတ်သော ဘုံကို အခြေခံသော",
    "Narūpadhātumūlakaṃ": "သိမ်မွေ့သော ရုပ်ဘုံ မဟုတ်သော ဘုံကို အခြေခံသော",
    "Naarūpadhātumūlakaṃ": "ရုပ်မရှိသော ဘုံ မဟုတ်သော ဘုံကို အခြေခံသော",
    "Nakāmanaarūpadhātumūlakaṃ": "ကာမဘုံလည်း မဟုတ် ရုပ်မရှိသော ဘုံလည်း မဟုတ်သော ဘုံကို အခြေခံသော",
    "Narūpanaarūpadhātumūlakaṃ": "သိမ်မွေ့သော ရုပ်ဘုံလည်း မဟုတ် ရုပ်မရှိသော ဘုံလည်း မဟုတ်သော ဘုံကို အခြေခံသော",
    "Nakāmanarūpadhātumūlakaṃ": "ကာမဘုံလည်း မဟုတ် သိမ်မွေ့သော ရုပ်ဘုံလည်း မဟုတ်သော ဘုံကို အခြေခံသော",
    # g2 V2 / U1 decided: sa- / nir-anusaya persons, the whole meaning of the word
    "sānusayo": "ကိန်းအောင်းခြင်း ရှိသူ", "sānusayā": "ကိန်းအောင်းခြင်း ရှိသူ",
    "niranusayo": "ကိန်းအောင်းခြင်း မရှိသူ", "niranusayā": "ကိန်းအောင်းခြင်း မရှိသူ",
    # g2 V5: the dvandva around a repeated noun; saraṇaaraṇā (U3 decided: «အတွဲ» only for a -duka keyword)
    "Atītānāgataṃ": "အတိတ် … အနာဂတ်",
    "saraṇaaraṇā": "ပဋိပက္ခ ရှိသော ပဋိပက္ခ မရှိသော",
    # g2 O5 / U4 decided (with mechanic 5): uppannaṃ the perfect participle in every segment
    "uppannaṃ": "ဖြစ်ပေါ်ပြီးသော",
    # g2 V7: the ch. 8 headings (rule 7 / R6: the text's whole part)
    "nanirodhavāro": "မချုပ်ငြိမ်းခြင်း ဖော်ပြချက်",
    "Suddhacittasāmaññaṃ": "ရိုးရိုး စိတ် အထွေထွေ", "Suddhacittasāmañña": "ရိုးရိုး စိတ် အထွေထွေ",
    "Suttantacittamissakaviseso": "သုတ္တန်လာ စိတ်များကို ရောစပ်သော ထူးခြားချက်",
    "Abhidhammacittamissakaviseso": "အဘိဓမ္မာလာ စိတ်များကို ရောစပ်သော ထူးခြားချက်",
    "Sarāgapacchimacittassa uppādakkhaṇe": "ရာဂ ရှိသော နောက်ဆုံး စိတ်၏ ဖြစ်ခြင်း ခဏ",
    # g3 W4: the bare words of the faculties
    "aññaṃ": AÑÑA, "Aññaṃ": AÑÑA, "aññanti": AÑÑA, "Aññañca": AÑÑA,
    "anaññātaññassāmīti": ANAÑÑA, "Anaññātaññassāmītiṃ": ANAÑÑA, "Anaññātaññassāmītiñca": ANAÑÑA,
    "Aññātāviṃ": AÑÑĀTĀVĪ, "Aññātāviñca": AÑÑĀTĀVĪ,
    # g3 W5 / O1: «X-ñca dhamme ca ṭhapetvā» «Xနှင့် သဘောတရားများကို ချန်ထား၍» (U3 decided: the gapped abyākata value)
    "Kusalañca dhamme": "ကုသိုလ်နှင့် သဘောတရား", "Akusalañca dhamme": "အကုသိုလ်နှင့် သဘောတရား",
    "Abyākatañca dhamme": "ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော … သဘောတရား",
    # g3 W2: persons qualified by a citta factor (as pi-2 ñāṇavippayuttānaṃ «ဉာဏ်နှင့် ကင်းကွာသော»)
    "ñāṇasampayuttānaṃ": "ဉာဏ်နှင့် ယှဉ်တွဲသော", "Ñāṇasampayuttānaṃ": "ဉာဏ်နှင့် ယှဉ်တွဲသော",
    # g3 W7: the headings with a source digit and no dot (R6 cannot split them)
    "Suddhadhammavāro": "ရိုးရိုး သဘောတရား ဖော်ပြချက်",
    "Suddhadhammamūlacakkavāro": "ရိုးရိုး သဘောတရားကို အခြေခံ၍ လှည့်ပတ်ခြင်း ဖော်ပြချက်",
}
# ---- BOOK-END


def book_auto(kw):
    """the family function of a keyword that BOOK does not list (g1 / g2 / g3 regex families), else None."""
    w = low(kw.split()[0])
    ws = kw.split()
    if citta_value(w) is not None and (len(ws) == 1 or (len(ws) == 2 and low(ws[1]) in MOMENT)):
        return "@citta"
    if len(ws) == 1 and vara_value(kw):
        return "@vara"
    if _AKA.match(low(kw)):
        return "@aka"
    if len(ws) == 1 and _SAKA.match(w):
        return "@saka"
    if len(ws) == 1 and re.match(r"^(upapajj|cav)antīnaṃ$", w):
        return "@fem"
    return None


for _k, _v in list(BOOK.items()):
    if isinstance(_v, tuple):
        BOOK[_k] = alt_name(_v)


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
    """the most frequent pi-2 (then pi-3, pi-4, pi-5, pi-1) value of the keyword present in the segment, by tier (pi-4
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
                # phase 3 mechanic 1 (g2 O1, kāyasaṅkhāro): the literal tier needs the value's words together
                # (phrase_ok), not chunks scattered over the segment
                if (tier == "contig" and contiguous(v, my)) or \
                        (tier == "literal" and not rules and (phrase_ok(v, my) or phrase_ok(v, flat(my)))) or \
                        tier == "rule":
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
        if s.endswith("ပြီးသော") and (s[:-3] + " ဖြစ်" in my or s[:-3] + " မဟုတ်" in my):
            return True             # phase 3 mechanic 5: also the negated perfect predicate «Xပြီး မဟုတ်»
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
    """the particle that joins value a to value b where they are adjacent in the text (pi-6: also in the text without
    the list comma «၊», pi-1 rule 6), else None."""
    a_last, b_first = a.split(" … ")[-1], b.split(" … ")[0]
    vf = GLUE_VERB_FROM if is_verb(b) and " … " not in b else None
    fm = flat(my)

    def pp(s):
        return phrase_present(s, my, vf) or phrase_present(s, fm, vf)
    if pp(f"{a_last}{b_first}") and not pp(f"{a_last} {b_first}"):
        return "\0"            # one written word in the text («နတ်မျက်စိ»): no space
    for p in PARTICLES:
        if pp(f"{a_last}{p} {b_first}"):
            return p + " "
    return None


def is_verb(v):
    """a finite verb value («…သည်», or the negative «မX» of rule 9 / pi-2 «na uppajjati»)."""
    last = v.split(" … ")[-1].split()[-1]
    return last.endswith("သည်") or (last.startswith("မ") and v in NEG_VERBS)




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
    """S1 (phase 2 ch2-15, approved after the phase-3 review): the stem fallback over the pi-1 … pi-5 values and the
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
                # phase 3: a gapped table value («အတိတ် … အနာဂတ်», rule 10) belongs to its own construction and is
                # no stem donor (it took atītepi / atītānāgatepi when BOOK joined the pool)
                if not x.startswith("@") and x != NONE and " … " not in x:
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


def lad_gap(v, my):
    """R7 (pi-1 rule 10 / pi-5 Q4 for one keyword): a value that the text has as a phrase only with the «လည်း» of ca /
    pi inside it gets « … » at that place (ekamūlañceva «တူညီသော အမြစ်လည်း ရှိ» = တူညီသော အမြစ် … ရှိသော; kusalamūlakañceva
    «ကုသိုလ်၏ အမြစ်ကိုလည်း အခြေခံ» = ကုသိုလ်၏ အမြစ်ကို … အခြေခံသော); the «လည်း» of «neither … nor» inside a term stays
    (abyākata, pi-1 rule 6)."""
    if v == NONE or " … " in v or phrase_ok(v, my) or phrase_ok(v, flat(my)):
        return v
    ch = v.split(" ")
    for i in range(1, len(ch)):
        l, r = " ".join(ch[:i]), " ".join(ch[i:])
        for m in (my, flat(my)):
            if phrase_present(l + "လည်း " + r, m):
                return l + " … " + r
    return v


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
            return lad_gap(v, my)
        if len(ws) == 2 and self.SRC.get((sid, kw)) == "compose" and v != NONE and self.order:
            w = self.pali_order(ch, sid, ws, v, pali, my)
            if w != v:
                self.ORDER[(ch, sid, kw)] = (v, w)
            v = w
        return lad_gap(v, my)

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

    def _tables(self, ch, sid, kw, pali, my):
        """the CTX / chapter table / FRAME / STOCK / shared value of the keyword (resolved), else None."""
        v = table_get(self.ctx.get(sid, {}), kw)
        if v is not None:
            self.SRC[(sid, kw)] = "ctx"
            return self.resolve(v, kw, pali, my)
        v = table_get(self.tables.get(ch, {}), kw)
        src = "table"
        if v is None:                 # phase 3: the book-wide group rules (BOOK, then the regex families)
            v = table_get(BOOK, kw)
            if v is None:
                v = book_auto(kw)
            src = "book"
        if v is None:
            v = table_get(FRAME, kw)
            src = "frame"
        if v is None:
            v = table_get(STOCK, kw)
            src = "stock"
        if v is None:
            v = table_get(self.shared, kw)
            src = "table"
        if v is not None:
            self.SRC[(sid, kw)] = src
            return self.resolve(v, kw, pali, my)
        return None

    def _chain(self, ch, sid, kw, pali, my):
        """pi-6 order: the tables (keyword) -> the chapter title (rule 7) -> morphology R2-R5 -> the tables (base form,
        R1) -> the pi-5 chain (pi-6 terms, pi-1 … pi-5 values, compose, counts) for the keyword, then for its base
        forms -> the heading rule R6."""
        v = self._tables(ch, sid, kw, pali, my)
        if v is not None:
            return v
        v = title_value(kw, my)
        if v is not None:
            self.SRC[(sid, kw)] = "title"
            return v
        v, src = morph_value(kw, pali, my)
        if v is not None:
            self.SRC[(sid, kw)] = src
            return v
        v = self.mulaka(ch, sid, kw, pali, my)
        if v is not None:
            self.SRC[(sid, kw)] = "mulaka"
            return v
        for b in base_forms(kw):
            v = self._tables(ch, sid, b, pali, my)
            if v is not None:
                self.SRC[(sid, kw)] = "base:" + self.SRC.get((sid, b), "?")
                return v
        try:
            return self._rest(ch, sid, kw, pali, my)
        except KeyError:
            pass
        for b in base_forms(kw):
            try:
                v = self._rest(ch, sid, b, pali, my)
            except KeyError:
                continue
            self.SRC[(sid, kw)] = "base:" + self.SRC.get((sid, b), "?")
            return v
        v = heading_value(kw, pali, my)
        if v is not None:
            self.SRC[(sid, kw)] = "heading"
            return v
        raise KeyError(kw)

    def mulaka(self, ch, sid, kw, pali, my):
        """R4 (labels of the later chapters): «(Cakkhāyatanamūlakaṃ)» «(မျက်စိ အာရုံခံ နယ်ပယ်ကို အခြေခံ၍)» = the value of the
        term + «ကို အခြေခံသော» (as ch. 1 kusalamūlaka; rule 3: the absolutive «၍» of the text by the ending rule)."""
        m = re.match(r"^(.+?)mūlak(aṃ|ā|o|ānaṃ|assa)$", low(kw))
        if not m or m.group(1) in ("", "eka", "aññamañña", "mūla") or any(m.group(1).startswith(b) and len(
                m.group(1)) <= len(b) + 1 for b, _, _ in MULA_BASE):
            return None
        x = m.group(1)
        for t in (x[:-1] + "aṃ" if x.endswith("a") else x, x + "ṃ", x, x[:-1] + "o" if x.endswith("a") else x):
            try:
                v = self._chain(ch, sid, t, pali, my)
            except KeyError:
                continue
            if v != NONE and " … " not in v:
                w = v + "ကို အခြေခံသော"
                if presence(w, my)[0] and (phrase_ok(w, my) or phrase_ok(w, flat(my))):
                    return w
        return None

    def _rest(self, ch, sid, kw, pali, my):
        """the pi-5 chain after the tables (unchanged)."""
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
            v, tag = pi_get(kw, my)      # binding: a pi-1 … pi-5 multiword value the text has (by an ending rule)
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
        if len(ws) == 2 and low(ws[0]) in NUM_MY:      # «dvīsu vedanāsu» = the text's «ခံစားမှု နှစ်ပါး» (counts keep
            n = NUM_MY[low(ws[0])]                    # the text's classifier, pi-1 decision 5; noun + count adjacent)
            try:
                x = self.lookup(ch, sid, ws[1], pali, my)
            except KeyError:
                x = None
            if x and x != NONE:
                for c in ("ပါး", "မျိုး", "ယောက်", "ခု", "ကြိမ်", ""):
                    if f"{x} {n}{c}" in my or f"{x}{n}{c}" in my:
                        return f"{x} {n}{c}"
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
