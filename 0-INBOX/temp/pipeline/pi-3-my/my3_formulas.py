"""Shared Burmese formulas for pi-3 (Dhātukathā, «ဓာတ်များအကြောင်း ဆွေးနွေးခြင်း»), plain audience.

Every pi-3 Burmese generator imports this module, so that identical Pāli gets identical Burmese, within pi-3 and
with the FINAL pi-1 / pi-2 Burmese (the rails texts). Writes no files at import (no bytecode either). It holds:
  * pi-1 / pi-2 reuse, read only: F2 = the final pi-2 module (pi-2-my/my2_formulas.py with the source patches of
    pi-2-my/rails/my_formulas_rails.py applied in memory, as rails/build_rails.py does; it loads the final pi-1
    module itself: P1 = F2.P1). FINAL = an index of the rails texts of pi-1 and pi-2 aligned with their Pāli by
    block ID; the topic names, mātikā terms, headings and colophons that pi-1 / pi-2 already have are READ FROM THE
    RAILS TEXT through it (katame(), tattha(), items(), heads()), never retyped. Nothing in pi-1-my / pi-2-my is
    written. Where the zero-shot modules and the rails text differ, the rails text wins (it is what is read);
  * the book frame, headings, colophons (HEAD, COLO), the five mātikās and the fourteen methods (MATIKA, NAYA_*);
  * the number words in the instrumental (INSTR) and the three counted nouns (KIND);
  * the subjects (SUBJ: Pāli nominative -> (Burmese, number)), built from FINAL;
  * the frames of the first method (saṅgaha / asaṅgaha questions and answers: q_sangaha(), q_asangaha(),
    answer_my()); later methods add their frames to EXTRA_RULES;
  * the engine: translate_line() -> heading / colophon / fixed line / sentences_my(); any text no rule matches
    raises Miss: nothing is guessed.
Later chapters: import this module, add entries to the tables (never change an existing value without the user's
approval), add (regex, function) pairs to EXTRA_RULES (tried on each sentence before the built-ins).
"""
import pathlib
import re
import sys
import types
import unicodedata

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
PIPE = HERE.parent
ROOT = HERE.parents[3]
P2DIR = PIPE / "pi-2-my"


class Miss(Exception):
    pass


# ===================================================================================== final pi-2 (and pi-1) module
def _patched(src, patches, where):
    for old, new, count, reason in patches:
        n = src.count(old)
        if n != count:
            raise SystemExit(f"{where}: rails patch occurs {n}x, expected {count} ({reason})")
        src = src.replace(old, new)
    return src


def _load(name, path):
    mod = types.ModuleType(name)
    mod.__file__ = str(path)
    exec(compile(path.read_text(encoding="utf-8"), str(path), "exec"), mod.__dict__)
    return mod


_L2 = _load("pi2_my_rails_layer", P2DIR / "rails" / "my_formulas_rails.py")
_saved = sys.modules.get("my2_formulas")
F2 = types.ModuleType("my2_formulas")
F2.__file__ = str(P2DIR / "my2_formulas.py")
sys.modules["my2_formulas"] = F2
exec(compile(_patched((P2DIR / "my2_formulas.py").read_text(encoding="utf-8"), _L2.FORMULA_PATCHES,
                      "my2_formulas.py"), F2.__file__, "exec"), F2.__dict__)
if hasattr(_L2, "after_import"):
    _L2.after_import(F2)
if _saved is None:
    sys.modules.pop("my2_formulas", None)
else:
    sys.modules["my2_formulas"] = _saved
P1 = F2.P1

C = P1.COMMA                         # «၊»
END = P1.END                         # «။»
PE = P1.PE                           # …pe… / …Pe… = one «…»
DH, DHP = P1.DHAMMA, P1.DHAMMA_PL    # သဘောတရား / သဘောတရားများ
CL = P1.CL                           # ပါး
TIKA, DUKA = P1.TIKA, P1.DUKA        # သုံးမျိုးတွဲ / နှစ်မျိုးတွဲ
KHANDHA = P1.KHANDHA                 # အစုအဝေး
AYATANA = "အာရုံခံ နယ်ပယ်"            # āyatana (pi-1 / pi-2 final)
DHATU = "ဓာတ်"                       # dhātu (pi-1 / pi-2 final)
NAYA = "ခွဲနည်း"                      # naya (pi-1 rails L07 «Catukkanayo = ဈာန် လေးပါး ခွဲနည်း»; pi-2 COLO)
VARA = P1.VARA                       # ဖော်ပြချက်
MATIKA_W = P1.MATIKA                 # ခေါင်းစဉ်စာရင်း


# ===================================================================================== FINAL: the rails texts
ID_RE = re.compile(r" (\^[0-9A-Za-z-]+)\s*$")
BOOKS = {
    "1": (ROOT / "AI_translation/pali/pi-1_split_chapters",
          ROOT / "AI_translation/burmese/pi-1-burmese-plain-rails_split_chapters"),
    "2": (ROOT / "AI_translation/pali/pi-2_split_chapters",
          ROOT / "AI_translation/burmese/pi-2-burmese-plain-rails_split_chapters"),
}


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
    """Pāli and FINAL Burmese segments of pi-1 / pi-2 by block ID: SEG[book][id] = (file, pāli lines, my lines)."""

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
                    if k not in bb or len(bb[k]) != len(v):
                        raise SystemExit(f"FINAL: pi-{book} {f.name} {k} not aligned")
                    d[k] = (f.name, v, bb[k])
            self.SEG[book] = d

    def lines(self, book):
        for k, (f, p, b) in self.SEG[book].items():
            for x, y in zip(p, b):
                yield k, f, x, y

    def seg(self, book, bid):
        return self.SEG[book][bid]


FINAL = _Final()
WITNESS = {}     # Pāli key -> (book, block id) where the final Burmese was read (for the terms file and the checker)


def _strip_id(s):
    m = ID_RE.search(s)
    return s[:m.start()] if m else s


def _novar(s):
    return re.sub(r" ?\[[^\]]*\]", "", s)


def katame(term):
    """pi-1 «Katame dhammā TERM?» -> the final Burmese «… သဘောတရားများ» (every occurrence must agree)."""
    q = f"Katame dhammā {term}?"
    found = {}
    for k, f, p, b in FINAL.lines("1"):
        if _novar(p).startswith(q):
            m = re.match(r"(.+?) ဟူသည် အဘယ်တို့နည်း။", b)
            if not m:
                raise Miss(f"katame: no Burmese question at {k}")
            found.setdefault(m[1], k)
    if len(found) != 1:
        raise Miss(f"katame {term}: {len(found)} renderings {list(found)[:3]}")
    my, k = next(iter(found.items()))
    WITNESS.setdefault(term + " dhammā", ("1", k))
    return my


MATIKA_LINE_RE = re.compile(r"\((?:Ka|Kha|Ga)\) (?P<t>.+?) dhammā\.")


def matika(term):
    """pi-1 Mātikā line «(Ka) TERM dhammā.» -> its final Burmese «… သဘောတရားများ» (without label and «။»)."""
    found = {}
    for k, f, p, b in FINAL.lines("1"):
        if f != "1-matika.md":
            continue
        m = MATIKA_LINE_RE.fullmatch(_novar(_strip_id(p)))
        if m and m["t"].lower() == term.lower():
            found.setdefault(re.sub(r"^\(\S+\) ", "", _novar(_strip_id(b))).rstrip("။"), k)
    if len(found) != 1:
        raise Miss(f"matika {term}: {len(found)} renderings")
    my, k = next(iter(found.items()))
    WITNESS.setdefault(term + " dhammā", ("1", k))
    return my


def tattha(book, term, bid=None):
    """«Tattha katamo / katamā / katamaṃ / katame TERM?» -> the final Burmese «ထိုတို့အနက် … ဟူသည် …»."""
    q = re.compile(r"Tattha katam(?:o|ā|aṃ|e|āni) " + re.escape(term) + r"\?")
    found = {}
    for k, f, p, b in FINAL.lines(book):
        if bid and k != bid:
            continue
        if q.match(p):
            m = re.match(r"ထိုတို့အနက် (.+?) ဟူသည် အဘယ်(?:တို့)?နည်း။", b)
            if not m:
                raise Miss(f"tattha: no Burmese question at {k}")
            found.setdefault(m[1], k)
    if len(found) != 1:
        raise Miss(f"tattha {term}: {len(found)} renderings {list(found)[:3]}")
    my, k = next(iter(found.items()))
    WITNESS.setdefault(term, (book, k))
    return my


def items(book, bid, line=0):
    """A list line «Head – a, b, c.» / its Burmese «Head – a၊ b၊ c။» -> (head pair, {pāli item: burmese item})."""
    p = _novar(_strip_id(FINAL.seg(book, bid)[1][line]))
    b = _novar(_strip_id(FINAL.seg(book, bid)[2][line]))
    ph, pl = p.split(" – ", 1)
    bh, bl = b.split(" – ", 1)
    pi = [x.strip() for x in pl.rstrip(".").split(",")]
    my = [x.strip() for x in bl.rstrip("။").split("၊")]
    if len(pi) != len(my):
        raise Miss(f"items {bid}: {len(pi)} vs {len(my)}")
    for x in pi:
        WITNESS.setdefault(x, (book, bid))
    WITNESS.setdefault(ph.split(", ")[0], (book, bid))
    return (ph.split(", ")[0], bh.split("၊ ")[0]), dict(zip(pi, my))


def plain_list(book, bid, line=0):
    """A list line «a, b, c – …» / «a၊ b၊ c – …» (no head) -> {pāli item: burmese item}."""
    p = _novar(_strip_id(FINAL.seg(book, bid)[1][line]))
    b = _novar(_strip_id(FINAL.seg(book, bid)[2][line]))
    return p, b


def witness(book, bid, pali, my):
    """A value read by hand from a rails segment: both must occur in it (checked here and by check_sample.py)."""
    f, p, b = FINAL.seg(book, bid)
    if pali.lower() not in " ".join(p).lower() or my not in " ".join(b):
        raise Miss(f"witness {bid}: «{pali}» / «{my}» not in the segment")
    WITNESS.setdefault(pali, (book, bid))
    return my


def heads(book, pali):
    """A heading or colophon «Pāli» with the same text in pi-1 / pi-2 -> its final Burmese (all must agree)."""
    found = {}
    for k, f, p, b in FINAL.lines(book):
        pt, bt = _strip_id(p), _strip_id(b)
        pt = re.sub(r"^#+ ", "", pt)
        bt = re.sub(r"^#+ ", "", bt)
        if pt.rstrip(".") == pali:
            found.setdefault(bt.rstrip("။"), k)
    if len(found) != 1:
        raise Miss(f"heads {pali}: {len(found)} renderings {list(found)[:3]}")
    my, k = next(iter(found.items()))
    WITNESS.setdefault(pali, (book, k))
    return my


# ===================================================================================== book frame
NAMO = P1.NAMO
ABHI = P1.ABHI
TITLE = "ဓာတ်များအကြောင်း ဆွေးနွေးခြင်း"      # Dhātukathāpāḷi (book title, Burmese only; proposed)
TITLE1 = P1.TITLE                            # Dhammasaṅgaṇī «သဘောတရားများကို စုစည်းရေတွက်ခြင်း»
TITLE2 = F2.TITLE                            # Vibhaṅga «ခွဲခြမ်းစိတ်ဖြာခြင်း»
assert heads("1", "Abhidhammapiṭake") == ABHI and heads("2", "Vibhaṅgapāḷi") == TITLE2

# ===================================================================================== numbers
NUM_MY = {1: "တစ်", 2: "နှစ်", 3: "သုံး", 4: "လေး", 5: "ငါး", 6: "ခြောက်", 7: "ခုနစ်", 8: "ရှစ်", 9: "ကိုး", 10: "ဆယ်",
          11: "ဆယ့်တစ်", 12: "ဆယ့်နှစ်", 13: "ဆယ့်သုံး", 14: "ဆယ့်လေး", 15: "ဆယ့်ငါး", 16: "ဆယ့်ခြောက်",
          17: "ဆယ့်ခုနစ်", 18: "ဆယ့်ရှစ်", 22: "နှစ်ဆယ့်နှစ်"}
for _n, _k in zip(range(1, 11), ("eka", "dvi", "ti", "catu", "pañca", "cha", "satta", "aṭṭha", "nava", "dasa")):
    assert P1.NUM[_k] == NUM_MY[_n]
witness("2", "^2-978", "dvādasāyatanāni", f"{AYATANA} {NUM_MY[12]}{CL}")
witness("2", "^2-978", "aṭṭhārasa dhātuyo", f"{DHATU} {NUM_MY[18]}{CL}")
witness("2", "^2-978", "bāvīsatindriyāni", f"{P1.INDRIYA} {NUM_MY[22]}{CL}")
witness("2", "^2-171", "Ekādasāyatanā", f"{AYATANA} {NUM_MY[11]}{CL}")

# instrumental number words (counts of the answers) -> number
INSTR = {"ekena": 1, "ekāya": 1, "dvīhi": 2, "tīhi": 3, "catūhi": 4, "pañcahi": 5, "chahi": 6, "sattahi": 7,
         "aṭṭhahi": 8, "navahi": 9, "dasahi": 10, "ekādasahi": 11, "dvādasahi": 12, "terasahi": 13, "cuddasahi": 14,
         "pannarasahi": 15, "soḷasahi": 16, "sattarasahi": 17, "aṭṭhārasahi": 18}
# the three counted nouns: Pāli instrumental endings -> kind
KIND = {"k": KHANDHA, "a": AYATANA, "d": DHATU}
COUNT_TOK = {}       # one Pāli count token -> (kind, number); number 0 = «na kehici / na kāhici»
for _w, _n in INSTR.items():
    if _w == "ekāya":
        COUNT_TOK["ekāya dhātuyā"] = ("d", 1)
        continue
    if _w == "ekena":
        COUNT_TOK["ekena khandhena"] = ("k", 1)
        COUNT_TOK["ekenāyatanena"] = ("a", 1)
        continue
    COUNT_TOK[f"{_w} khandhehi"] = ("k", _n)
    COUNT_TOK[f"{_w[:-1]}āyatanehi"] = ("a", _n)
    COUNT_TOK[f"{_w} dhātūhi"] = ("d", _n)
COUNT_TOK["dvādasāyatanehi"] = ("a", 12)       # ^3-20 (without the -h- of «dvādasahāyatanehi»)
COUNT_TOK["na kehici khandhehi"] = ("k", 0)
COUNT_TOK["na kehici āyatanehi"] = ("a", 0)
COUNT_TOK["na kāhici dhātūhi"] = ("d", 0)
_CT_ALT = "|".join(sorted(map(re.escape, COUNT_TOK), key=len, reverse=True))
COUNT_RE = re.compile(rf"(?:{_CT_ALT})", re.IGNORECASE)        # «Catūhi khandhehi» opens a sentence
COUNTS_RE = re.compile(rf"(?:(?:{_CT_ALT})(?:,? (?=\S))?)+", re.IGNORECASE)


def count_my(kind, n):
    return f"{KIND[kind]} {NUM_MY[n]}{CL}"


# ===================================================================================== saṅgaha / sampayoga words
SANGAHA_V = "အကျုံးဝင်"            # saṅgahita (included; pi-1 ^1-1044 «atītaṃsena saṅgahitā = အတိတ် အပိုင်း၌ အကျုံးဝင်သော»)
ASANGAHA_V = "အကျုံးမဝင်"          # asaṅgahita (not included)
witness("1", "^1-1044", "atītaṃsena saṅgahitā", f"အတိတ် အပိုင်း၌ {SANGAHA_V}သော")
SAMPAYUTTA_V = "ယှဉ်တွဲ"            # sampayutta (pi-1 SAMP «နှင့် ယှဉ်တွဲသော»)
VIPPAYUTTA_V = "ကင်းကွာ"           # vippayutta (pi-1 VIPP «နှင့် ကင်းကွာသော»)
assert P1.SAMP == f"နှင့် {SAMPAYUTTA_V}သော" and P1.VIPP == f"နှင့် {VIPPAYUTTA_V}သော"
NOUN_W = {"saṅgaho": f"{SANGAHA_V}ခြင်း", "asaṅgaho": f"{ASANGAHA_V}ခြင်း",
          "sampayogo": f"{SAMPAYUTTA_V}ခြင်း", "vippayogo": f"{VIPPAYUTTA_V}ခြင်း"}
THING = "သည့်အရာ"                 # nominal participle «… သည့်အရာ» (what is included …)
ACC_W = {"saṅgahitaṃ": SANGAHA_V + THING, "asaṅgahitaṃ": ASANGAHA_V + THING,
         "sampayuttaṃ": SAMPAYUTTA_V + THING, "vippayuttaṃ": VIPPAYUTTA_V + THING}
INS_W = {k[:-2] + "ena": v + "ဖြင့်" for k, v in ACC_W.items()}     # saṅgahitena … = «… သည့်အရာဖြင့်»
STEM_W = {"saṅgaha": NOUN_W["saṅgaho"], "asaṅgaha": NOUN_W["asaṅgaho"], "sampayoga": NOUN_W["sampayogo"],
          "vippayoga": NOUN_W["vippayogo"], "saṅgahita": ACC_W["saṅgahitaṃ"], "asaṅgahita": ACC_W["asaṅgahitaṃ"],
          "sampayutta": ACC_W["sampayuttaṃ"], "vippayutta": ACC_W["vippayuttaṃ"]}
PADA = "ပုဒ်"                      # pada (term) in the method names
NIDDESA = "အကျယ် " + VARA     # -niddeso = «အကျယ် ဖော်ပြချက်» (pi-1 Ekakaniddeso, pi-2)
UDDESA = "အကျဉ်း " + VARA                 # Uddeso = «အကျဉ်း ဖော်ပြချက်» (pi-1 ^1-2-1-0)
assert heads("1", "Uddeso") == UDDESA and heads("1", "Ekakaniddeso") == f"တစ်မျိုးတွဲ {NIDDESA}"

# the fourteen items of the Nayamātikā (= the fourteen methods), Pāli words
NAYA_ITEMS = ["saṅgaho asaṅgaho", "saṅgahitena asaṅgahitaṃ", "asaṅgahitena saṅgahitaṃ", "saṅgahitena saṅgahitaṃ",
              "asaṅgahitena asaṅgahitaṃ", "sampayogo vippayogo", "sampayuttena vippayuttaṃ",
              "vippayuttena sampayuttaṃ", "sampayuttena sampayuttaṃ", "vippayuttena vippayuttaṃ",
              "saṅgahitena sampayuttaṃ vippayuttaṃ", "sampayuttena saṅgahitaṃ asaṅgahitaṃ",
              "asaṅgahitena sampayuttaṃ vippayuttaṃ", "vippayuttena saṅgahitaṃ asaṅgahitaṃ"]


def naya_item_my(p):
    """«saṅgahitena sampayuttaṃ vippayuttaṃ» -> «အကျုံးဝင်သည့်အရာဖြင့် ယှဉ်တွဲသည့်အရာ၊ ကင်းကွာသည့်အရာ»."""
    w = p.lower().split()
    if w[0] in NOUN_W:
        return f"{C} ".join(NOUN_W[x] for x in w)
    return INS_W[w[0]] + " " + f"{C} ".join(ACC_W[x] for x in w[1:])


# method names (the «…padaniddeso» headings and colophons): Pāli compound (as the source) -> NAYA_ITEMS index
NIDDESO_PI = ["Saṅgahāsaṅgaha", "Saṅgahitenaasaṅgahita", "Asaṅgahitenasaṅgahita", "Saṅgahitenasaṅgahita",
              "Asaṅgahitenaasaṅgahita", "Sampayogavippayoga", "Sampayuttenavippayutta", "Vippayuttenasampayutta",
              "Sampayuttenasampayutta", "Vippayuttenavippayutta", "Saṅgahitenasampayuttavippayutta",
              "Sampayuttenasaṅgahitāsaṅgahita", "Asaṅgahitenasampayuttavippayutta", "Vippayuttenasaṅgahitāsaṅgahita"]


def naya_name_my(i):
    """Method i (0-13) as a compound: the two members of a pair joined by «နှင့်» (list item: «၊»)."""
    w = NAYA_ITEMS[i].split()
    if w[0] in NOUN_W:
        return f"{NOUN_W[w[0]]}နှင့် {NOUN_W[w[1]]}"
    rest = [ACC_W[x] for x in w[1:]]
    return INS_W[w[0]] + " " + "နှင့် ".join(rest)


NIDDESO = {pi + "padaniddeso": f"{naya_name_my(i)} {PADA}ကို {NIDDESA}" for i, pi in enumerate(NIDDESO_PI)}

ORD = dict(P1.ORD)
ORD.update({"navama": "နဝမ", "dasama": "ဒသမ", "ekādasama": "ဧကာဒသမ", "dvādasama": "ဒွါဒသမ",
            "terasama": "တေရသမ", "cuddasama": "စုဒ္ဒသမ"})
NAYA_ORD = ["paṭhama", "dutiya", "tatiya", "catuttha", "pañcama", "chaṭṭha", "sattama", "aṭṭhama", "navama",
            "dasama", "ekādasama", "dvādasama", "terasama", "cuddasama"]
ORD_COLO = {"paṭhamo": "paṭhama", "dutiyo": "dutiya", "tatiyo": "tatiya", "catuttho": "catuttha",
            "pañcamo": "pañcama", "chaṭṭho": "chaṭṭha", "sattamo": "sattama", "aṭṭhamo": "aṭṭhama",
            "navamo": "navama", "dasamo": "dasama", "ekādasamo": "ekādasama", "dvādasamo": "dvādasama",
            "terasamo": "terasama", "cuddasamo": "cuddasama"}

# ===================================================================================== headings
HEAD = {
    "Uddeso": UDDESA,
    "Nayamātikā": f"{NAYA} {MATIKA_W}",
    "Abbhantaramātikā": f"အတွင်း {MATIKA_W}",
    "Nayamukhamātikā": f"{NAYA}၏ တံခါးဝ {MATIKA_W}",
    "Lakkhaṇamātikā": f"လက္ခဏာ {MATIKA_W}",
    "Bāhiramātikā": f"ပြင်ပ {MATIKA_W}",
    "Khandho": KHANDHA, "Āyatanaṃ": AYATANA, "Dhātu": DHATU, "Saccaṃ": "သစ္စာ", "Indriyaṃ": P1.INDRIYA,
    "Tikaṃ": heads("2", "Tikaṃ"), "Dukaṃ": heads("2", "Dukaṃ"),
}
for _o in NAYA_ORD:
    HEAD[_o[0].upper() + _o[1:] + "nayo"] = f"{ORD[_o]} {NAYA}"
HEAD.update(NIDDESO)
assert HEAD["Tikaṃ"] == TIKA and HEAD["Dukaṃ"] == DUKA
witness("2", "^2-1", "Pañcakkhandhā", f"{KHANDHA} ငါး{CL}")
witness("1", "^1-M2-66", "bāhirā dhammā", f"ပြင်ပ {DHP}")

# ===================================================================================== colophons «(X.)»
COLO = {
    "Dukamūlakaṃ": heads("2", "Dukamūlakaṃ"), "Tikamūlakaṃ": heads("2", "Tikamūlakaṃ"),
    "Catukkaṃ": heads("2", "Catukkaṃ"), "Pañcakaṃ": heads("2", "Pañcakaṃ"),
}
COLO["Ekamūlakaṃ"] = COLO["Dukamūlakaṃ"].replace(DUKA, "တစ်မျိုးတွဲ", 1)          # pi-2 pattern
COLO["Catukkamūlakaṃ"] = COLO["Dukamūlakaṃ"].replace(DUKA, "လေးမျိုးတွဲ", 1)
COLO["Dvādasakaṃ"] = f"{NUM_MY[12]}မျိုးတွဲ"                                       # pi-2 «Pañcakaṃ» pattern
COLO["Aṭṭhārasakaṃ"] = f"{NUM_MY[18]}မျိုးတွဲ"
assert COLO["Dukamūlakaṃ"] == f"{DUKA}ကို အခြေခံသော {NAYA}" and COLO["Catukkaṃ"] == "လေးမျိုးတွဲ"


# ===================================================================================== variant readings
SIGLA = dict(P1.SIGLA)
SIGLA["?"] = "အမည်မသိ မူ"          # «(?)» = unknown edition (pi-2 ^2-916, ^2-924)
witness("2", "^2-924", "(?)", "(အမည်မသိ မူ)")
VAR_KIND = {"upādānapaccayā kammabhavo": P1.PATHA, "parittāramaṇā": P1.LEKHANA, "na hetū ahetukā": P1.PATHA}
VAR_NOTE = {   # editorial words after the sigla
    "vibha. dukapañhāpucchakepi": f"“{TITLE2}” {DUKA} {F2.HEAD['Pañhāpucchakaṃ']}၌လည်း",
}
VAR_RE = re.compile(r"\[(?P<t>[^\[\]()]+?) \((?P<s>[^()]+)\)(?: (?P<n>[^\[\]]+))?\]")


def var_my(br):
    """«[upādānapaccayā kammabhavo (sī. syā.)]» -> «[ပါဌ်ကွဲ (Sī., Syā.): upādānapaccayā kammabhavo]»."""
    m = VAR_RE.fullmatch(br)
    if not m or m["t"] not in VAR_KIND:
        raise Miss("variant: " + br)
    sig = ", ".join(SIGLA[s] for s in m["s"].split())
    note = ""
    if m["n"]:
        if m["n"] not in VAR_NOTE:
            raise Miss("variant note: " + br)
        note = f"{C} {VAR_NOTE[m['n']]}"
    return f"[{VAR_KIND[m['t']]} ({sig}): {m['t']}{note}]"


# ===================================================================================== subjects (topic names)
SUBJ = {}        # Pāli nominative (first letter lower case) -> (Burmese, "sg" / "pl")


def _add(p, my, num, w=None):
    """w: the WITNESS key (the Pāli read in the rails segment) when it differs from the subject itself."""
    k = p[0].lower() + p[1:]
    if k in SUBJ and SUBJ[k][0] != my:
        raise SystemExit(f"subject conflict {p}: {SUBJ[k][0]} / {my}")
    SUBJ[k] = (my, num)
    if w:
        WITNESS.setdefault(k, WITNESS[w])
    elif p in WITNESS:
        WITNESS.setdefault(k, WITNESS[p])


FEM = set()      # feminine singular subjects (their «-ā» verb is singular)
# aggregates (pi-2 ^2-1)
_h, _it = items("2", "^2-1")
for _p, _m in _it.items():
    _add(_p, _m, "sg")
_add(_h[0], _h[1], "pl")
# bases (pi-2 ^2-155)
_h, _it = items("2", "^2-155")
for _p, _m in _it.items():
    _add(_p, _m, "sg")
_add(_h[0], _h[1], "pl")
# elements (pi-2 ^2-183)
_h, _it = items("2", "^2-183")
for _p, _m in _it.items():
    _add(_p, _m, "sg")
    FEM.add(_p)
_add(_h[0], _h[1], "pl")
# faculties (pi-2 ^2-219)
_h, _it = items("2", "^2-219")
for _p, _m in _it.items():
    _add(_p, _m, "sg")
_add(_h[0], _h[1], "pl")
# truths (pi-2 ^2-218, the pañhāpucchaka subjects «Xသည်»)
for _p, _m in (("Dukkhasaccaṃ", "ဒုက္ခ သစ္စာ"), ("Samudayasaccaṃ", "ဖြစ်ပေါ်ခြင်း သစ္စာ"),
               ("Nirodhasaccaṃ", "ချုပ်ငြိမ်းခြင်း သစ္စာ"), ("Maggasaccaṃ", "မဂ် သစ္စာ")):
    _add(_p, witness("2", "^2-218", _p, _m + "သည်")[:-3], "sg")
_add("Cattāri saccāni", items("2", "^2-206")[0][1], "pl")
# dependent arising (pi-2 6-paticcasamuppadavibhango, «Tattha katamo X?»)
for _p, _bid in (("avijjā", "^2-226"), ("avijjāpaccayā saṅkhārā", "^2-226"), ("saṅkhārapaccayā viññāṇaṃ", "^2-227"),
                 ("viññāṇapaccayā nāmarūpaṃ", "^2-228"), ("nāmarūpapaccayā saḷāyatanaṃ", "^2-229"),
                 ("saḷāyatanapaccayā phasso", "^2-230"), ("phassapaccayā vedanā", "^2-231"),
                 ("vedanāpaccayā taṇhā", "^2-232"), ("taṇhāpaccayā upādānaṃ", "^2-233"),
                 ("upapattibhavo", "^2-234")):
    _add(_p, tattha("2", _p, _bid), "pl" if _p.endswith("saṅkhārā") else "sg")
FEM.update({"avijjā", "phassapaccayā vedanā", "vedanāpaccayā taṇhā"})
_add("kammabhavo", witness("2", "^2-234", "atthi kammabhavo", "ကံ ဘဝ ရှိသည်")[:-len(" ရှိသည်")], "sg",
     "atthi kammabhavo")
# the kinds of existence (pi-2 ^2-234, list of «upapattibhavo»)
_p, _b = (_novar(_strip_id(x)) for x in (FINAL.seg("2", "^2-234")[1][1], FINAL.seg("2", "^2-234")[2][1]))
_pl = re.search(r"\? (.+?) – ayaṃ", _p)[1].split(", ")
_bl = []
for _f in re.search(r"နည်း။ (.+?) – ဤသည်", _b)[1].split("၊ "):      # an item may hold «၊» (neva … na …)
    if _bl and not _bl[-1].endswith("ဘဝ"):
        _bl[-1] += "၊ " + _f
    else:
        _bl.append(_f)
assert len(_pl) == len(_bl) == 9
for _x, _y in zip(_pl, _bl):
    WITNESS.setdefault(_x, ("2", "^2-234"))
    _add(_x, _y, "sg")
# birth … despair (pi-2 4-saccavibhango «Tattha katamā jāti?» …)
for _p, _bid in (("jāti", "^2-191"), ("jarā", "^2-192"), ("maraṇaṃ", "^2-193"), ("soko", "^2-194"),
                 ("paridevo", "^2-195"), ("dukkhaṃ", "^2-196"), ("upāyāso", "^2-198")):
    _add(_p, tattha("2", _p, _bid), "sg")
FEM.update({"jāti", "jarā"})
_add("domanassaṃ", tattha("2", "domanassaṃ", "^2-197"), "sg")
# the wings of awakening (pi-1 ^1-357 «lokuttaraṃ X bhāveti» = «လောကကို ကျော်လွန်သော Xကို ပွားများ၍»;
# pi-2 ^2-U26 «Cattāro satipaṭṭhānā, … ariyo aṭṭhaṅgiko maggo»)
for _p, _m in (("satipaṭṭhānaṃ", "သတိပဋ္ဌာန်"), ("sammappadhānaṃ", "မှန်ကန်သော ကြိုးပမ်းအားထုတ်ခြင်း"),
               ("iddhipādo", "ဣဒ္ဓိပါဒ်")):
    _w = "lokuttaraṃ " + (_p[:-1] + "aṃ" if _p.endswith("o") else _p)
    _add(_p, witness("1", "^1-357", _w, f"လောကကို ကျော်လွန်သော {_m}ကို")[len("လောကကို ကျော်လွန်သော "):-len("ကို")],
         "sg", _w)
_bU = _strip_id(FINAL.seg("2", "^2-U26")[2][0])
_pU = ["cattāro satipaṭṭhānā", "cattāro sammappadhānā", "cattāro iddhipādā", "pañcindriyāni", "pañca balāni",
       "satta bojjhaṅgā", "ariyo aṭṭhaṅgiko maggo"]
_mU = re.search(r"နည်း။ ([^။]+?) – ဤသည်ကို “သူတော်ကောင်းတရား”", _bU)[1].split("၊ ")
assert len(_mU) == 7
for _x, _y in zip(_pU, _mU):
    _add(_x, _y, "sg" if _x.startswith("ariyo") else "pl")
    WITNESS.setdefault(_x, ("2", "^2-U26"))
_add("jhānaṃ", witness("2", "^2-623", "jhānaṃ", P1.NAMES["jhānaṃ"]), "sg")
_add("cattāri jhānāni", items("2", "^2-623")[0][1], "pl")
_add("catasso appamaññāyo", items("2", "^2-683")[0][1], "pl")
_add("appamaññā", witness("2", "^2-683", "appamaññāyo", SUBJ["catasso appamaññāyo"][0].rsplit(" ", 1)[0]), "sg",
     "appamaññāyo")
FEM.add("appamaññā")
# phasso … manasikāro (pi-1 NAMES = pi-1 final; adhimokkho pi-2 ^2-281, manasikāro pi-2 ^2-766)
for _p in ("phasso", "vedanā", "saññā", "cetanā", "cittaṃ"):
    _add(_p, witness("1", "^1-1", f"{_p} hoti", f"{P1.NAMES[_p]} ရှိ")[:-len(" ရှိ")], "sg", f"{_p} hoti")
FEM.update({"vedanā", "saññā", "cetanā"})
_add("adhimokkho", witness("2", "^2-281", "adhimokkho", "စိတ်၏ ဆုံးဖြတ်မှု")[len("စိတ်၏ "):], "sg")
_add("manasikāro", witness("2", "^2-766", "manasikāro", "နှလုံးသွင်းခြင်း"), "sg")
_add("paṭiccasamuppādo", witness("2", "^2-6-0", "Paṭiccasamuppādavibhaṅgo",
                                 "အကြောင်းတို့ကို မှီ၍ ဖြစ်ပေါ်ပုံ"), "sg", "Paṭiccasamuppādavibhaṅgo")
assert heads("1", "Mātikā") == MATIKA_W
HEAD["Paṭiccasamuppādādi"] = f"{SUBJ['paṭiccasamuppādo'][0]} စသည်"

# mātikā terms «X dhammā» (pi-1 nikkhepakaṇḍa / aṭṭhakathākaṇḍa «Katame dhammā X?»)
TERM_ALIAS = {   # pi-3 spelling -> pi-1 spelling of the same term
    "upādinnupādāniyā": "upādiṇṇupādāniyā", "anupādinnupādāniyā": "anupādiṇṇupādāniyā",
    "anupādinnaanupādāniyā": "anupādiṇṇaanupādāniyā", "upādinnā": "upādiṇṇā", "anupādinnā": "anupādiṇṇā",
}
NO_DHAMMA = {"vipākadhammadhammā", "nevavipākanavipākadhammadhammā"}     # the subject has no separate «dhammā»


def dhamma_subject(p):
    """«Kusalā dhammā» / «Vipākadhammadhammā» -> final pi-1 Burmese «ကုသိုလ် သဘောတရားများ» (plural)."""
    k = p[0].lower() + p[1:]
    if k in SUBJ:
        return SUBJ[k]
    if k in NO_DHAMMA:
        t = k
    elif k.endswith(" dhammā"):
        t = k[:-len(" dhammā")]
    else:
        raise Miss("subject: " + p)
    t = TERM_ALIAS.get(t, t)
    try:
        my = katame(t)
    except Miss:
        my = matika(t)        # «kenaci viññeyyā»: pi-1 asks it with its pair in one question
    WITNESS.setdefault(k, WITNESS.get(t + " dhammā"))
    SUBJ[k] = (my, "pl")
    return SUBJ[k]


USED = set()     # subject keys used by the generated text (for the checker's reuse test)


def subject(p):
    k = p[0].lower() + p[1:]
    USED.add(k)
    if k in SUBJ:
        return SUBJ[k]
    return dhamma_subject(p)


def var_split(p):
    """«Parittārammaṇā [parittāramaṇā (?)] dhammā» -> («Parittārammaṇā dhammā», bracket, words before it)."""
    m = re.search(r" (\[[^\]]+\])", p)
    if not m:
        return p, None, 0
    return p[:m.start()] + p[m.end():], m[1], len(p[:m.start()].split())


def subject_my(p):
    """One subject (with an optional variant bracket) -> (Burmese, number)."""
    q, br, pos = var_split(p)
    my, num = subject(q)
    if br:
        brm = var_my(br)
        if my.endswith(" " + DHP) and pos == len(q.split()) - 1:      # «X [v] dhammā»: bracket before သဘောတရားများ
            my = my[:-len(DHP)] + brm + " " + DHP
        elif pos == len(q.split()):                                  # «X [v]»: after the name
            my = my + " " + brm
        else:
            raise Miss("variant position: " + p)
    k = q[0].lower() + q[1:]
    if num == "sg" and k in FEM:
        num = "fsg"
    return my, num


CA_RE = re.compile(r"(\S+?)(ñca| ca)(?: |$)")


def subjects_my(p):
    """«A» / «A ca B ca» / «Añca Bñca» -> (Burmese, number); two or more = «Aနှင့် Bတို့» / «A၊ Bနှင့် Cတို့» (plural)."""
    q = var_split(p)[0]
    if (q[0].lower() + q[1:]) in SUBJ or q.endswith(" dhammā") or not re.search(r"(?:ñca| ca)(?: |$)", q):
        return subject_my(p)
    pos, names = 0, []
    for m in CA_RE.finditer(p):
        if m.start() != pos:
            raise Miss("ca list: " + p)
        names.append(subject_my(m[1] + ("ṃ" if m[2] == "ñca" else ""))[0])
        pos = m.end()
    if pos != len(p) or len(names) < 2:
        raise Miss("ca list: " + p)
    my = f"{C} ".join(names[:-1]) + "နှင့် " + names[-1]
    return my + "တို့", "pl"


# ===================================================================================== frames of the first method
SUBJ_MARK = "သည်"
VERB = {     # (positive?, number) -> statement / question / zero-run verb
    True: {"st": {"sg": SANGAHA_V + "သည်", "pl": SANGAHA_V + "ကြသည်"},
           "q": {"sg": SANGAHA_V + "သနည်း", "pl": SANGAHA_V + "ကြသနည်း"}},
    False: {"st": {"sg": ASANGAHA_V, "pl": ASANGAHA_V + "ကြ"},
            "q": {"sg": ASANGAHA_V + "သနည်း", "pl": ASANGAHA_V + "ကြသနည်း"}},
}
ZERO_TAIL = "မရှိ"                 # «na kehici …»: «(အကျုံး(မ)ဝင်)ရာ X၊ Y မရှိ» (there is no X where it is (not) included)
WHERE = "ရာ"
KATI = "မည်မျှ"                    # kati (pi-2 ^2-978)
IN = "တွင်"
IN_PL = "တို့တွင်"
THAPETVA = f"{P1.TERMS['asaṅkhatā']} {DH}ကို {KHANDHA} ရေတွက်ရာမှ ချန်ထား၍"   # asaṅkhataṃ khandhato ṭhapetvā
assert P1.THAPETVA == "ကို ချန်ထား၍"
witness("2", "^2-218", "Nirodhasaccaṃ asaṅkhataṃ", f"{P1.TERMS['asaṅkhatā']} {DH}")
THAP_P = "asaṅkhataṃ khandhato ṭhapetvā"
Q1_P = "katihi khandhehi katihāyatanehi katihi dhātūhi"
Q1_MY = f"{KHANDHA} {KATI}{C} {AYATANA} {KATI}{C} {DHATU} {KATI}{IN_PL}"
VERB_RE = r"(?P<neg>a?)saṅgahit(?P<e>o|aṃ|ā|āni)"


def number(e, state_num):
    """Pāli verb ending + the subject's number -> «sg» / «pl»."""
    if e in ("o", "aṃ"):
        return "sg"
    if e == "āni":
        return "pl"
    if state_num is None:
        raise Miss("number of «-ā» unknown")
    return "sg" if state_num == "fsg" else state_num


def counts_parse(s):
    """«catūhi khandhehi, ekenāyatanena …» -> [(kind, n), …] (the whole string must be count tokens)."""
    toks = COUNT_RE.findall(s)
    if re.sub(r"[, ]", "", s) != "".join(t.replace(" ", "") for t in toks):
        raise Miss("counts: " + s)
    return [COUNT_TOK[t.lower()] for t in toks]


def counts_my(cs, pos, num, verb=True):
    """Counts + polarity -> Burmese: positive runs «A n-ပါး၊ B m-ပါးတို့တွင် VERB», zero runs «VERB-ရာ A၊ B မရှိ»."""
    runs = []
    for kind, n in cs:
        z = n == 0
        if runs and runs[-1][0] == z:
            runs[-1][1].append((kind, n))
        else:
            runs.append((z, [(kind, n)]))
    out = []
    for i, (z, r) in enumerate(runs):
        last = i == len(runs) - 1
        if z:
            v = (SANGAHA_V if pos else ASANGAHA_V) + WHERE
            out.append(f"{v} " + f"{C} ".join(KIND[k] for k, _ in r) + f" {ZERO_TAIL}")
        else:
            lst = f"{C} ".join(count_my(k, n) for k, n in r)
            if not verb and last:
                out.append(lst)
                continue
            post = IN if len(r) == 1 and r[0][1] == 1 else IN_PL
            out.append(f"{lst}{post} {VERB[pos]['st'][num]}")
    return f"{C} ".join(out)


STATE = {}       # per line: «num» = the number of the last subject


def chunk_my(ch, last):
    """One chunk between ellipses: «[SUBJ] [ṭhapetvā] [COUNTS [VERB]]» or a question «SUBJ katihi … saṅgahito?»."""
    m = re.fullmatch(rf"(?P<s>.+?) {Q1_P} {VERB_RE}\?", ch)
    if m:
        if m["neg"]:
            raise Miss("question polarity: " + ch)
        my, num = subjects_my(m["s"])
        STATE["num"] = num
        return f"{my}{SUBJ_MARK} {Q1_MY} {VERB[True]['q'][number(m['e'], num)]}{END}"
    m = re.fullmatch(rf"Katihi {VERB_RE}\?", ch)
    if m:
        if not m["neg"]:
            raise Miss("question polarity: " + ch)
        return f"{KATI}{IN_PL} {VERB[False]['q'][number(m['e'], STATE.get('num'))]}{END}"
    m = re.fullmatch(rf"(?P<pre>.*?)(?P<c>{COUNTS_RE.pattern}) ?{VERB_RE}\.", ch, re.IGNORECASE) if last else None
    vm = None
    if m:
        pre, cs, vm = m["pre"], m["c"], m
    else:
        mc = COUNTS_RE.search(ch)
        if mc and mc.end() == len(ch.rstrip(", ")):
            pre, cs = ch[:mc.start()], ch[mc.start():]
        elif not COUNT_RE.search(ch) and THAP_P not in ch:
            pre, cs = ch, ""
        else:
            raise Miss("chunk: " + ch)
    pre = pre.strip()
    thap = pre.endswith(THAP_P)
    if thap:
        pre = pre[:-len(THAP_P)].strip()
    parts = []
    if pre:
        my, num = subjects_my(pre)
        STATE["num"] = num
        parts.append(my + SUBJ_MARK)
    if thap:
        parts.append(THAPETVA)
    if cs:
        c = counts_parse(cs.strip())
        if vm:
            n = number(vm["e"], STATE.get("num"))
            parts.append(counts_my(c, not vm["neg"], n) + END)
        else:
            parts.append(counts_my(c, True, "sg", verb=False))
    elif vm:
        raise Miss("verb without counts: " + ch)
    return " ".join(parts)


ELL_RE = re.compile(r"\s*(?:…pe…|…Pe…|…)\s*")


def sentence_my(s):
    """One Pāli sentence (ending in «?» or «.») -> Burmese; chunks between ellipses keep one «…» each."""
    for rx, fn in EXTRA_RULES:
        m = rx.fullmatch(s)
        if m:
            r = fn(m)
            if r is not None:
                return r
    chunks = ELL_RE.split(s)
    seps = ELL_RE.findall(s)
    out = []
    for i, ch in enumerate(chunks):
        out.append(chunk_my(ch, i == len(chunks) - 1))
    res = out[0]
    for sep, x in zip(seps, out[1:]):
        res += PE + " " + x
    return res


SENT_RE = re.compile(r"(?<=[?.])\s+(?=[A-ZĀĪŪṬḌṆÑ])")


def sentences_my(body):
    """A content line: protect «[…]», split into sentences, translate each, join with one space."""
    brs = re.findall(r"\[[^\]]+\]", body)
    prot = body
    for i, b in enumerate(brs):
        prot = prot.replace(b, f"⟦{i}⟧", 1)
    sents = SENT_RE.split(prot.strip())
    out = []
    for s in sents:
        for i, b in enumerate(brs):
            s = s.replace(f"⟦{i}⟧", b)
        out.append(sentence_my(s))
    return " ".join(out)


# ===================================================================================== fixed lines (the mātikās)
FIXED = {}
FIXED_USES = {}    # fixed line -> the SUBJ keys it reuses (recorded in USED when the line is generated)
EXTRA_RULES = []    # later chapters: (compiled regex on one sentence, function(match) -> Burmese or None)

TOPIC_ORDER = ["pañcakkhandhā", "dvādasāyatanāni", "aṭṭhārasa dhātuyo", "cattāri saccāni", "bāvīsatindriyāni",
               "paṭiccasamuppādo", "cattāro satipaṭṭhānā", "cattāro sammappadhānā", "cattāro iddhipādā",
               "cattāri jhānāni", "catasso appamaññāyo", "pañcindriyāni", "pañca balāni", "satta bojjhaṅgā",
               "ariyo aṭṭhaṅgiko maggo"]
SEVEN = ["phasso", "vedanā", "saññā", "cetanā", "cittaṃ", "adhimokkho", "manasikāro"]
NAYAMUKHA = {"Tīhi saṅgaho": f"သုံး{CL}ဖြင့် {NOUN_W['saṅgaho']}", "tīhi asaṅgaho": f"သုံး{CL}ဖြင့် {NOUN_W['asaṅgaho']}",
             "catūhi sampayogo": f"လေး{CL}ဖြင့် {NOUN_W['sampayogo']}",
             "catūhi vippayogo": f"လေး{CL}ဖြင့် {NOUN_W['vippayogo']}"}
FIXED["Tīhi saṅgaho, tīhi asaṅgaho, catūhi sampayogo, catūhi vippayogo."] = \
    f"{C} ".join(NAYAMUKHA.values()) + END
LAKKHANA = {"Sabhāgo": "တူညီသော သဘော", "visabhāgo": "ကွဲပြားသော သဘော"}
FIXED["Sabhāgo, visabhāgo."] = f"{C} ".join(LAKKHANA.values()) + END
FIXED["Sabbāpi dhammasaṅgaṇī dhātukathāya mātikāti."] = \
    f"“{TITLE1}” အားလုံးသည်လည်း “{TITLE}”၏ {MATIKA_W} ဖြစ်သည်{END}"
COLO_RE = re.compile(r"\((?P<t>[^()]+)\.\)")
NUMLIST_RE = re.compile(r"\((\d+)\)( ?)")


def numbered_my(body, fn):
    """«(1) A (2) B …» -> «(1) A' (2) B' …» (spacing after «(n)» as the source; the last item's «.» -> «။»)."""
    parts = NUMLIST_RE.split(body)
    if parts[0].strip():
        raise Miss("numbered: " + body)
    out = []
    for i in range(1, len(parts), 3):
        n, sp, txt = parts[i], parts[i + 1], parts[i + 2]
        end = txt.rstrip().endswith(".")
        t = txt.strip().rstrip(".")
        out.append(f"({n}){sp}{fn(int(n), t)}{END if end else ''}")
    return " ".join(out)


def topic_my(n, t):
    if n == 16:
        ws = t.split()
        if [w.lower() for w in ws] != SEVEN:
            raise Miss("topic 16: " + t)
        return f"{C} ".join(subject(w)[0] for w in ws)
    k = t[0].lower() + t[1:]
    if TOPIC_ORDER[n - 1] != k:
        raise Miss(f"topic {n}: {t}")
    return subject(k)[0]


def naya_my(n, t):
    if NAYA_ITEMS[n - 1] != t.lower():
        raise Miss(f"naya item {n}: {t}")
    return naya_item_my(t)


NUMBERED = {"^3-1": naya_my, "^3-2": topic_my}


# ===================================================================================== the engine
HEAD_RE = re.compile(r"(?P<h>#+) (?P<t>.+)$")
NIDDESA_COLO_RE = re.compile(r"(?P<n>\S+padaniddeso) (?P<o>\S+)\.")


def line_my(body, bid=None):
    m = HEAD_RE.fullmatch(body)
    if m:
        t = m["t"]
        if t == "Abhidhammapiṭake":
            return f"{m['h']} {ABHI}"
        if t == "Dhātukathāpāḷi":
            return f"{m['h']} {TITLE}"
        if t not in HEAD:
            raise Miss("heading: " + t)
        return f"{m['h']} {HEAD[t]}"
    if body == "Namo tassa bhagavato arahato sammāsambuddhassa":
        return NAMO
    m = COLO_RE.fullmatch(body)
    if m:
        if m["t"] not in COLO:
            raise Miss("colophon: " + body)
        return f"({COLO[m['t']]}{END})"
    m = NIDDESA_COLO_RE.fullmatch(body)
    if m:
        if m["n"] not in NIDDESO or m["o"] not in ORD_COLO:
            raise Miss("colophon: " + body)
        return f"{ORD[ORD_COLO[m['o']]]} {NIDDESO[m['n']]}{END}"
    if body in FIXED:
        USED.update(FIXED_USES.get(body, ()))       # the topic names a fixed (verse) line reuses
        return FIXED[body]
    if bid in NUMBERED and NUMLIST_RE.match(body):
        return numbered_my(body, NUMBERED[bid])
    return sentences_my(body)


def translate_line(line, bid=None):
    """One source line (with or without its block ID) -> Burmese line (block ID kept)."""
    if not line.strip():
        return ""
    m = ID_RE.search(line)
    body = line[:m.start()] if m else line
    STATE.clear()
    my = line_my(body.strip(), bid)
    my = unicodedata.normalize("NFC", my)
    return my + (" " + m.group(1) if m else "")


# ===================================================================================== consistency pass (harmonise)
# Book-wide values of the consistency pass (harmonise-brief.md, harmonise-todo.md; log in harmonise-notes.md). The
# frame words below are shared by the generators of methods 2-14 (make_ch3-6-8-9.py, make_ch7-10-11.py,
# make_ch12-15.py); install() adds the table entries those generators need (numbers, aliases, sigla, variants,
# headings, the book colophon, the singular saṅkhāra subject and ALL summary verses of the book) to the tables above.
# make_sample.py does not call install(): the user-approved sample strings and my3-zeroshot-terms.md stay as they were.
WITH = "နှင့်"                      # X-ena (saṅgahitā / sampayuttā / vippayuttā) = «Xနှင့်» (pi-1 SAMP «နှင့် ယှဉ်တွဲသော»)
WITH_PL = "တို့" + WITH             # counts with sampayutta / vippayutta: «A n-ပါး၊ B m-ပါးတို့နှင့်»
SOME = "၏ အချို့"                   # kehici: «… တို့၏ အချို့နှင့် V» (one count of one: «…၏ အချို့နှင့်»)
SOME_PL = "တို့" + SOME
REL = f"သော {DHP}"                 # ye dhammā V = «…V-သော သဘောတရားများ» (pi-1 ^1-1115)
TE = f"ထို{DHP}"                   # te dhammā = «ထိုသဘောတရားများ(သည်)» (pi-1 ^1-1091)
TEHI = f"ထို{DH}တို့" + WITH         # tehi dhammehi = «ထိုသဘောတရားတို့နှင့်» (pi-1 ^1-1115, identical Pāli)
NATTHI = "မရှိ"                    # Natthi. = «မရှိ။» (pi-1 ^1-1221, ^1-1433)
BY = NOUN_W["saṅgaho"] + "ဖြင့်"    # khandhasaṅgahena = «အစုအဝေး အကျုံးဝင်ခြင်းဖြင့်»
witness("1", "^1-1091", "te dhammā", TE + SUBJ_MARK)
witness("1", "^1-1115", "Tehi dhammehi ye dhammā sampayuttā", f"{TEHI} {SAMPAYUTTA_V}{REL}၊")
witness("1", "^1-1221", "Natthi", NATTHI)


def chain_item_my(name_my):
    """B3: a chain item «X-ena ye dhammā…» whose verb is elided = «Xနှင့်…» (the relative «Vသော သဘောတရားများ» is said
    once, where the Pāli says the verb: «… Y-ena ye dhammā V» = «… Yနှင့် Vသော သဘောတရားများ»)."""
    return name_my + WITH


def bare_item_my(term_my):
    """B7: a bare instrumental item «Saṃyojanehi…» (no «dhammehi ye dhammā») = the pi-1 term without «သဘောတရားများ»
    and without «နှင့်» («နှောင်ကြိုး ဖြစ်သော…»): the «…» stands for the elided words, as in the Pāli."""
    if not term_my.endswith(" " + DHP):
        raise Miss("bare item: " + term_my)
    return term_my[:-len(" " + DHP)]


# summary verses: one vocabulary for the whole book (B5)
V_LOC = IN                           # verse locatives (-e / -esu / -su, ettha) = «တွင်» (the sample's IN)
GOCCHA = "အစု"                       # gocchaka (pi-1 Hetugocchakaṃ «အမြစ်တို့၏ အစု»)
ANTARA = "ကြားညှပ်"                  # antara (pi-1 Cūḷantaradukaṃ «ကြားညှပ် နှစ်မျိုးတွဲ အစုငယ်»)
CULA_W, MAHA_W = "အစုငယ်", "အစုကြီး"  # cūḷa- / mahā- (antara) (pi-1 Cūḷantaradukaṃ / Mahantaradukaṃ)
PACCAYAKARA = "အကြောင်းတို့၏ အခြင်းအရာ"   # paccayākāra
PACCAYA_SEC = "အကြောင်း အပိုင်း"       # paccaye (the section of conditions)
UPARI = "အထက်"                       # upari / uddhaṃ (tato upari = «ထို့အထက်»)
TATO = "ထို့"                         # tato
PARE = "နောက်"                       # pare (tato pare = «ထို့နောက်»)
ATHA = "ထို့နောက်"                    # atha
PUNA = "တဖန်"                         # puna / punadeva
TATHA = "ထို့အတူ"                     # tathā / tathariva
LABBH = {"sg": "မတွေ့ရ", "pl": "မတွေ့ရကြ"}   # na labbhati / na labbhare, na labbhanti
SAMUCCHEDA = "ပိုင်းဖြတ်ခြင်း"            # samuccheda
MOGHA = "မေးခွန်း အချည်းနှီး ဖြစ်သောကြောင့်"   # moghapucchakena
MATTHAKA = "အဆုံး"                    # matthake
APARA = "နောက်"                       # aparante = «နောက် ကြားညှပ်»
JIVITA = "အသက်"                       # jīvitaṃ (pi-2 termbase)
ITTHI, PUMA, RUPA_W = "မိန်းမ", "ယောက်ျား", "ရုပ်"   # itthi / pumaṃ / rūpaṃ (verse)
MAHABHAVA = "ဘဝကြီး"                  # mahābhavā
BHAVA_W = "ဘဝ"                        # bhavā
VISAYO = "အပိုင်းအခြား"                 # visayo (as written, no adopted emendation)
SUBUDDHO = f"ဤ{NAYA}ကို ကောင်းစွာ နားလည်အပ်သည်"   # esa nayo subuddho (esanayo)
_INSTALLED = []


def _v(fn):
    """Build one verse line and record the topic names it reuses (USED is restored: a line records its names in USED
    only when it is generated, through FIXED_USES)."""
    before = set(USED)
    my = fn()
    uses = USED - before
    USED.clear()
    USED.update(before)
    return my, uses


def _verses():
    S = lambda k: subject(k)[0]                                  # noqa: E731
    sg = lambda k: S(k)[:-len(DHP)] + DH                         # «X dhammā» term as one «… သဘောတရား»
    cn = lambda n: f"{NUM_MY[n]}{CL}"                            # noqa: E731
    pc = lambda n: f"{PADA} {cn(n)}"                             # «padā» with a number = «ပုဒ် N-ပါး»
    IND, KH, AY, DT = P1.INDRIYA, KHANDHA, AYATANA, DHATU
    CULA, MAHA, PITTHI = heads("1", "Cūḷantaradukaṃ"), heads("1", "Mahantaradukaṃ"), heads("1", "Piṭṭhidukaṃ")
    assert CULA == f"{ANTARA} {DUKA} {CULA_W}" and MAHA == f"{ANTARA} {DUKA} {MAHA_W}"
    witness("1", "^1-M2-6", "Hetugocchakaṃ", GOCCHA)
    TIKA_L, GOCCHA_L = f"{TIKA}တို့{V_LOC}", f"{GOCCHA}တို့{V_LOC}"
    PATICCA = S("paṭiccasamuppādo")
    VITVIC = S("savitakkasavicārā dhammā").split(" ရှိသော")[0]
    assert VITVIC == "စတင်ကြံစည်မှုနှင့် ဆက်လက်သုံးသပ်မှု"
    NAMARUPA, SALAY = "စိတ်ပိုင်းနှင့် ရုပ်ပိုင်း", f"{AY} {cn(6)}"
    assert S("viññāṇapaccayā nāmarūpaṃ").endswith(NAMARUPA) and S("nāmarūpapaccayā saḷāyatanaṃ").endswith(SALAY)
    assert S("itthindriyaṃ").startswith(ITTHI + "၏") and S("purisindriyaṃ").startswith(PUMA + "၏")
    assert S("jīvitindriyaṃ").startswith(JIVITA + "၏")
    L = {
        # ---- 3-dutiyanayo ^3-178
        "Dasāyatanā sattarasa dhātuyo,": lambda: f"{AY} {cn(10)}{C} {DT} {cn(17)}{C}",
        "Sattindriyā asaññābhavo ekavokārabhavo;":
            lambda: f"{IND} {cn(7)}{C} {S('asaññābhavo')}{C} {S('ekavokārabhavo')}{C}",
        "Paridevo sanidassanasappaṭighaṃ,": lambda: f"{S('paridevo')}{C} {sg('sanidassanasappaṭighā dhammā')}{C}",
        "Anidassanaṃ punadeva [punareva (pī.)] sappaṭighaṃ upādāti.":
            lambda: f"{sg('anidassanā dhammā')}{C} {PUNA} {var_my('[punareva (pī.)]')} {sg('sappaṭighā dhammā')}{C} "
                    f"{sg('upādā dhammā')}{END}",
        # ---- 4-tatiyanayo ^3-190
        "Tayo khandhā tathā saccā, indriyāni ca soḷasa;":
            lambda: f"{KH} {cn(3)}{C} {TATHA} သစ္စာများ{C} {IND} {cn(16)}လည်း{C}",
        "Padāni paccayākāre, cuddasūpari cuddasa.":
            lambda: f"{PACCAYAKARA}{V_LOC} {pc(14)}{C} {UPARI}{V_LOC} {cn(14)}{END}",
        "Samatiṃsa padā honti, gocchakesu dasasvatha;":
            lambda: f"{ATHA} {GOCCHA} {cn(10)}တို့{V_LOC} {pc(30)} အပြည့် ရှိသည်{C}",
        "Duve cūḷantaradukā [cullantaradukā (sī.)], aṭṭha honti mahantarāti.":
            lambda: f"{cn(2)}သည် {CULA} {var_my('[cullantaradukā (sī.)]')} ဖြစ်သည်{C} "
                    f"{cn(8)}သည် {ANTARA} {MAHA_W} ဖြစ်သည်{END}",
        # ---- 5-catutthanayo ^3-200, 12-ekadasamanayo ^3-416
        "Dve saccā pannarasindriyā, ekādasa paṭiccapadā;":
            lambda: f"သစ္စာ {cn(2)}{C} {IND} {cn(15)}{C} {PATICCA}၏ {pc(11)}{C}",
        "Uddhaṃ puna ekādasa, gocchakapadamettha tiṃsavidhāti [tiṃsavidhanti (pī.)].":
            lambda: f"{UPARI}{V_LOC} {PUNA} {cn(11)}{C} ဤနေရာ{V_LOC} {GOCCHA}တို့၏ {PADA}သည် {NUM_MY[30]}မျိုး ရှိသည် "
                    f"{var_my('[tiṃsavidhanti (pī.)]')}{END}",
        "Uddhaṃ puna ekādasa, gocchakapadamettha tiṃsavidhāti.":
            lambda: f"{UPARI}{V_LOC} {PUNA} {cn(11)}{C} ဤနေရာ{V_LOC} {GOCCHA}တို့၏ {PADA}သည် {NUM_MY[30]}မျိုး ရှိသည်{END}",
        # ---- 6-pancamanayo ^3-227, 14-terasamanayo ^3-455
        "Rūpañca dhammāyatanaṃ dhammadhātu, itthipumaṃ jīvitaṃ nāmarūpaṃ;":
            lambda: f"{RUPA_W}{C} {S('dhammāyatanaṃ')}{C} {S('dhammadhātu')}{C} {ITTHI}{C} {PUMA}{C} {JIVITA}{C} "
                    f"{NAMARUPA}{C}",
        "Dve bhavā jāti jarā maccurūpaṃ, anārammaṇaṃ no cittaṃ cittena vippayuttaṃ.":
            lambda: f"{BHAVA_W} {cn(2)}{C} {S('jāti')}{C} {S('jarā')}{C} {S('maraṇaṃ')}{C} {sg('rūpino dhammā')}{C} "
                    f"{sg('anārammaṇā dhammā')}{C} {sg('no cittā dhammā')}{C} {sg('cittavippayuttā dhammā')}{END}",
        "Dve bhavā jātijarā maccurūpaṃ, anārammaṇaṃ no cittaṃ cittena vippayuttaṃ.":
            lambda: f"{BHAVA_W} {cn(2)}{C} {S('jāti')}{C} {S('jarā')}{C} {S('maraṇaṃ')}{C} {sg('rūpino dhammā')}{C} "
                    f"{sg('anārammaṇā dhammā')}{C} {sg('no cittā dhammā')}{C} {sg('cittavippayuttā dhammā')}{END}",
        "Visaṃsaṭṭhaṃ samuṭṭhāna-sahabhu anuparivatti;":
            lambda: f"{sg('cittavisaṃsaṭṭhā dhammā')}{C} {sg('cittasamuṭṭhānā dhammā')}{C} "
                    f"{sg('cittasahabhuno dhammā')}{C} {sg('cittānuparivattino dhammā')}{C}",
        "Visaṃsaṭṭhaṃ samuṭṭhānasahabhu, anuparivatti bāhiraṃ upādā;":
            lambda: f"{sg('cittavisaṃsaṭṭhā dhammā')}{C} {sg('cittasamuṭṭhānā dhammā')}{C} "
                    f"{sg('cittasahabhuno dhammā')}{C} {sg('cittānuparivattino dhammā')}{C} {sg('bāhirā dhammā')}{C} "
                    f"{sg('upādā dhammā')}{C}",
        "Bāhiraṃ upādā dve, visayo [dvevīsati (syā.)] esanayo subuddho.":
            lambda: f"{sg('bāhirā dhammā')}{C} {sg('upādā dhammā')}{C} {cn(2)}{C} {VISAYO} "
                    f"{var_my('[dvevīsati (syā.)]')}{C} {SUBUDDHO}{END}",
        "Dve visayo esanayo subuddhoti.": lambda: f"{cn(2)}{C} {VISAYO}{C} {SUBUDDHO}{END}",
        # ---- 7-chatthanayo ^3-307, 11-dasamanayo ^3-408
        "Dhammāyatanaṃ dhammadhātu, dukkhasaccañca jīvitaṃ;":
            lambda: f"{S('dhammāyatanaṃ')}{C} {S('dhammadhātu')}{C} {S('dukkhasaccaṃ')}နှင့် {JIVITA}{C}",
        "Saḷāyatanaṃ nāmarūpaṃ, cattāro ca mahābhavā.":
            lambda: f"{SALAY}{C} {NAMARUPA}{C} {MAHABHAVA} {cn(4)}တို့လည်း{END}",
        "Jāti jarā ca maraṇaṃ, tikesvekūnavīsati;":
            lambda: f"{S('jāti')}{C} {S('jarā')}နှင့် {S('maraṇaṃ')}{C} {TIKA_L} {cn(19)}{C}",
        "Gocchakesu ca paññāsa, aṭṭha cūḷantare padā.":
            lambda: f"{GOCCHA_L} {cn(50)}{C} {ANTARA} {CULA_W}{V_LOC} {pc(8)}{END}",
        "Mahantare pannarasa, aṭṭhārasa tato pare;":
            lambda: f"{ANTARA} {MAHA_W}{V_LOC} {cn(15)}{C} {TATO}{PARE}{V_LOC} {cn(18)}{C}",
        "Tevīsa padasataṃ etaṃ, sampayoge na labbhatīti.":
            lambda: f"ဤ{PADA} {cn(123)}ကို {NOUN_W['sampayogo']}{V_LOC} {LABBH['sg']}{END}",
        # ---- 8-sattamanayo ^3-316
        "Khandhā caturo āyatanañca mekaṃ;": lambda: f"{KH} {cn(4)}နှင့် {AY} {cn(1)}{C}",
        "Dhātūsu satta dvepi ca indriyato.": lambda: f"{DT}တို့{V_LOC} {cn(7)}{C} {IND}တို့မှလည်း {cn(2)}{END}",
        "Tayo paṭicca tathariva phassapañcamā;":
            lambda: f"{PATICCA}မှ {cn(3)}{C} {TATHA} {S('phasso')} စသော {cn(5)}{C}",
        "Adhimuccanā manasi tikesu tīṇi.":
            lambda: f"{S('adhimokkho')}{C} {S('manasikāro')}{C} {TIKA_L} {cn(3)}{END}",
        "Sattantarā dve ca manena yuttā;":
            lambda: f"{ANTARA}တို့မှ {cn(7)}{C} {S('cittaṃ')}နှင့် ယှဉ်သော {cn(2)}လည်း{C}",
        "Vitakkavicāraṇā upekkhakāya cāti.": lambda: f"{VITVIC}{C} {sg('upekkhāsahagatā dhammā')}လည်း{END}",
        # ---- 9-atthamanayo ^3-318, 15-cuddasamanayo ^3-518
        "Dhammāyatanaṃ dhammadhātu, atha jīvitaṃ nāmarūpaṃ;":
            lambda: f"{S('dhammāyatanaṃ')}{C} {S('dhammadhātu')}{C} {ATHA} {JIVITA}{C} {NAMARUPA}{C}",
        "Saḷāyatanaṃ jātijarāmataṃ, dve ca tike na labbhare.":
            lambda: f"{SALAY}{C} {S('jāti')}{C} {S('jarā')}{C} {S('maraṇaṃ')}{C} {TIKA_L} {cn(2)}လည်း "
                    f"{LABBH['pl']}{END}",
        "Paṭhamantare satta ca, gocchake dasa aparante;":
            lambda: f"{ORD['paṭhama']} {ANTARA}{V_LOC} {cn(7)}{C} {GOCCHA_L} {cn(10)}{C} {APARA} {ANTARA}{V_LOC}",
        "Cuddasa cha ca matthake, iccete sattacattālīsa dhammā;":
            lambda: f"{cn(14)}{C} {MATTHAKA}{V_LOC} {cn(6)}{C} ဤသို့ ဤ{DH} {cn(47)}တို့သည်",
        "Samucchede na labbhanti, moghapucchakena cāti.":
            lambda: f"{SAMUCCHEDA}{V_LOC} {LABBH['pl']}{C} {MOGHA}လည်း{END}",
        # ---- 10-navamanayo ^3-345, 13-dvadasamanayo ^3-447
        "Arūpakkhandhā cattāro, manāyatanameva ca;":
            lambda: f"ရုပ် မဟုတ်သော {KH} {cn(4)}{C} {S('manāyatanaṃ')}လည်း{C}",
        "Rūpakkhandhā cattāro, manāyatanameva ca;":
            lambda: f"{S('rūpakkhandho')}မှလွဲ၍ {KH} {cn(4)}{C} {S('manāyatanaṃ')}လည်း{C}",
        "Viññāṇadhātuyo satta, dve saccā cuddasindriyā.":
            lambda: f"သိစိတ် {DT} {cn(7)}{C} သစ္စာ {cn(2)}{C} {IND} {cn(14)}{END}",
        "Paccaye dvādasa padā, tato upari soḷasa;":
            lambda: f"{PACCAYA_SEC}{V_LOC} {pc(12)}{C} {TATO}{UPARI}{V_LOC} {cn(16)}{C}",
        "Tikesu aṭṭha gocchake, tecattālīsameva ca.": lambda: f"{TIKA_L} {cn(8)}{C} {GOCCHA_L} {cn(43)}လည်း{END}",
        "Mahantaraduke satta, padā piṭṭhi dukesu cha;": lambda: f"{MAHA}{V_LOC} {cn(7)}{C} {PITTHI}{V_LOC} {pc(6)}{C}",
        "Mahantaraduke satta, padā piṭṭhidukesu cha;": lambda: f"{MAHA}{V_LOC} {cn(7)}{C} {PITTHI}{V_LOC} {pc(6)}{C}",
        "Navamassa padassete, niddese saṅgahaṃ gatāti.":
            lambda: f"ဤ{PADA}တို့သည် {ORD['navama']} {PADA}ကို {NIDDESA}{V_LOC} {SANGAHA_V}ကြသည်{END}",
    }
    return L


def install():
    """Add the book-wide table entries of the consistency pass (idempotent); called by the generators of methods
    2-14 at import."""
    if _INSTALLED:
        return
    _INSTALLED.append(True)
    NUM_MY.update({19: "ဆယ့်ကိုး", 30: "သုံးဆယ်", 43: "လေးဆယ့်သုံး", 47: "လေးဆယ့်ခုနစ်", 50: "ငါးဆယ်",
                   123: "တစ်ရာ့နှစ်ဆယ့်သုံး"})
    TERM_ALIAS.update({"paccupannārammaṇā": "paccuppannārammaṇā",     # A5: ^3-210 spelling slip
                       "na hetusahetukā": "na hetū sahetukā"})          # A5: ^3-213 / ^3-279 (one word in pi-3)
    SIGLA["bahūsu"] = heads_sigla("bahūsu")                            # B8: pi-1 / pi-2 «(Bahūsu)»
    VAR_KIND.update({"anupādiṇṇehi": P1.PATHA, "na hetūhi sahetukehi": P1.PATHA, "punareva": P1.LEKHANA,
                     "cullantaradukā": P1.LEKHANA, "tiṃsavidhanti": P1.LEKHANA, "dvevīsati": P1.PATHA})
    HEAD["Khandhādi"] = f"{KHANDHA} စသည်"                               # B6: pattern of Paṭiccasamuppādādi
    HEAD["Saccādi"] = f"{HEAD['Saccaṃ']} စသည်"
    HEAD["Phassādisattakaṃ"] = f"{SUBJ['phasso'][0]} စသည့် {NUM_MY[7]}မျိုးတွဲ"   # sattaka: pi-2 «Pañcakaṃ» pattern
    witness("1", "^1-1616", "Dhammasaṅgaṇīpakaraṇaṃ niṭṭhitaṃ", f"“{TITLE1}” ကျမ်း ပြီးဆုံးပြီ")
    witness("2", "^2-1044", "Vibhaṅgapakaraṇaṃ niṭṭhitaṃ", f"“{TITLE2}” ကျမ်း ပြီးဆုံးပြီ")
    FIXED["Dhātukathāpakaraṇaṃ niṭṭhitaṃ."] = f"“{TITLE}” ကျမ်း ပြီးဆုံးပြီ{END}"   # B6: pi-1 / pi-2 pattern
    # B4: singular «avijjāpaccayā saṅkhārena» = pi-2 ^2-249 (plural «saṅkhārā / saṅkhārehi» = the sample, pi-2 ^2-227)
    _add("avijjāpaccayā saṅkhāro", tattha("2", "avijjāpaccayā saṅkhāro", "^2-249"), "sg")
    for p, fn in _verses().items():
        if p in FIXED:
            raise SystemExit("verse already fixed: " + p)
        FIXED[p], FIXED_USES[p] = _v(fn)
    VERSES.update({p: FIXED[p] for p in FIXED_USES})


VERSES = {}


def heads_sigla(s):
    """A siglum «(s)» -> the form of the FINAL pi-1 / pi-2 Burmese brackets «(Form): …» (all must agree)."""
    found = set()
    for book in ("1", "2"):
        for k, f, p, b in FINAL.lines(book):
            if f"({s})" in p:
                found.update(re.findall(r"\((" + re.escape(s) + r")\): ", b, re.IGNORECASE))
    if len(found) != 1:
        raise Miss(f"siglum {s}: {found}")
    return found.pop()
