"""Shared Burmese formulas for pi-4 (Puggalapaññatti, «ပုဂ္ဂိုလ်များကို သတ်မှတ်ဖော်ပြခြင်း»), plain audience.

Every pi-4 Burmese generator imports this module, so that identical Pāli gets identical Burmese, within pi-4 and
with the FINAL pi-1 / pi-2 / pi-3 Burmese (the rails texts). Writes no files at import (no bytecode either). It holds:
  * FINAL: an index of the rails texts of pi-1, pi-2 and pi-3 aligned with their Pāli by block ID (read only;
    nothing in pi-1-my / pi-2-my / pi-3-my is imported or written). Every value that pi-1 / pi-2 / pi-3 already
    have is READ from, or CHECKED against, the rails text through it: heads() (headings, colophons, whole lines),
    items() (the topic lists «Head – a, b, c»), witness() (a term: the Pāli must occur in the Pāli segment and
    the Burmese in its rails Burmese). WITNESS records each of them for the terms file and the checker. Where the
    zero-shot modules of pi-1 / pi-2 / pi-3 and the rails text differ, the rails text wins (it is what is read);
  * the book frame, headings and colophons (HEAD, COLO, FIXED), number words for persons (NUM_MY, PERSONS);
  * the six designations (PANNATTI, TOPIC lists of pi-2) and their frame (designation_my());
  * NAME: the person-type name table for ALL types of the mātikā (ones to tens; key = the Pāli of the niddesa
    question «Katamo ca puggalo KEY?», lower case; ALIAS = other spellings of the same type, e.g. the mātikā form);
    PLURAL = the plural Pāli forms of the ch2 text -> the singular key; GROUP = the group names
    («Tayo gilānūpamā puggalā», «Pañca piṇḍapātikā» …); adj() = a name before «puggalo»;
  * PRED: the «atthekacco puggalo PRED» predicates of the mātikā whose Burmese is not «NAME ဖြစ်၏»;
  * the definition frame (Q_RE question, V_RE / VP_RE «ayaṃ vuccati puggalo "X"» / «ime vuccanti puggalā "X"»,
    IDHEKACCO) and SENT: the shared sentences of the definitions (Pāli sentence -> Burmese; «⟦n⟧» = the n-th
    variant bracket of the Pāli sentence, translated by var_my());
  * the engine: translate_line() -> heading / colophon / fixed line / numbered item / sentences; any text no rule
    matches raises Miss: nothing is guessed.
Later chapters: import this module, add entries to the tables (never change an existing value without the user's
approval), unique prose to the generator's own table (merged into SENT / LINES), new frames to EXTRA_RULES.
"""
import pathlib
import re
import sys
import unicodedata

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]


class Miss(Exception):
    pass


# ===================================================================================== FINAL: rails texts pi-1/2/3
ID_RE = re.compile(r" (\^[0-9A-Za-z-]+)\s*$")
BOOKS = {b: (ROOT / f"AI_translation/pali/pi-{b}_split_chapters",
             ROOT / f"AI_translation/burmese/pi-{b}-burmese-plain-rails_split_chapters") for b in "123"}


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
    """Pāli and FINAL Burmese segments by block ID: SEG[book][id] = (file, pāli lines, burmese lines)."""

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

    def lines(self, book=None):
        for b in ([book] if book else list(self.SEG)):
            for k, (f, p, m) in self.SEG[b].items():
                for x, y in zip(p, m):
                    yield b, k, f, x, y

    def seg(self, book, bid):
        return self.SEG[book][bid]


FINAL = _Final()
WITNESS = {}     # Pāli term -> (book, block id, Burmese) where the final Burmese was read / checked


def strip_id(s):
    m = ID_RE.search(s)
    return s[:m.start()] if m else s


def novar(s):
    return re.sub(r" ?\[[^\]]*\]", "", s)


def witness(book, bid, pali, my):
    """A value read by hand from a rails segment: the Pāli must occur in its Pāli, the Burmese in its Burmese."""
    f, p, m = FINAL.seg(book, bid)
    if pali.lower() not in " ".join(p).lower() or my not in " ".join(m):
        raise Miss(f"witness pi-{book} {bid}: «{pali}» / «{my}» not in the segment")
    WITNESS.setdefault(pali, (book, bid, my))
    return my


def heads(pali):
    """A heading, colophon or whole line «Pāli» of pi-1 / pi-2 / pi-3 -> its final Burmese (all must agree)."""
    found = {}
    for b, k, f, p, m in FINAL.lines():
        pt = re.sub(r"^#+ ", "", strip_id(p)).strip()
        mt = re.sub(r"^#+ ", "", strip_id(m)).strip()
        if pt.rstrip(".") == pali.rstrip("."):
            found.setdefault(mt.rstrip("။"), (b, k))
    if len(found) != 1:
        raise Miss(f"heads {pali}: {len(found)} renderings {list(found)[:3]}")
    my, (b, k) = next(iter(found.items()))
    WITNESS.setdefault(pali.rstrip("."), (b, k, my))
    return my


def items(book, bid, line=0):
    """A list line «Head – a, b, c.» / «Head – a၊ b၊ c။» -> (head Burmese, {pāli item: burmese item})."""
    p = novar(strip_id(FINAL.seg(book, bid)[1][line]))
    m = novar(strip_id(FINAL.seg(book, bid)[2][line]))
    ph, pl = p.split(" – ", 1)
    mh, ml = m.split(" – ", 1)
    pi = [x.strip() for x in pl.rstrip(".").split(",")]
    my = [x.strip() for x in ml.rstrip("။").split("၊")]
    if len(pi) != len(my):
        raise Miss(f"items {bid}: {len(pi)} vs {len(my)}")
    for x, y in zip(pi, my):
        WITNESS.setdefault(x, (book, bid, y))
    WITNESS.setdefault(ph, (book, bid, mh))
    return mh, dict(zip(pi, my))


# ===================================================================================== basics
C = "၊"                               # list / clause break
END = "။"                             # end of a statement
PE = "…"                              # …pe… / …Pe… = one «…»
NAMO = heads("Namo tassa bhagavato arahato sammāsambuddhassa")
ABHI = heads("Abhidhammapiṭake")
TITLE = "ပုဂ္ဂိုလ်များကို သတ်မှတ်ဖော်ပြခြင်း"     # Puggalapaññattipāḷi (book title, Burmese only; proposed)
TITLE1 = heads("Dhammasaṅgaṇīpakaraṇaṃ niṭṭhitaṃ").split("”")[0].lstrip("“")
TITLE2 = heads("Vibhaṅgapakaraṇaṃ niṭṭhitaṃ").split("”")[0].lstrip("“")
TITLE3 = heads("Dhātukathāpakaraṇaṃ niṭṭhitaṃ").split("”")[0].lstrip("“")
BOOK_END_PAT = heads("Dhātukathāpakaraṇaṃ niṭṭhitaṃ")           # «“…” ကျမ်း ပြီးဆုံးပြီ»
assert BOOK_END_PAT == f"“{TITLE3}” ကျမ်း ပြီးဆုံးပြီ"
MATIKA_W = heads("Mātikā")                                       # ခေါင်းစဉ်စာရင်း
MATIKA_END_PAT = heads("Mātikā niṭṭhitā")                        # «“ခေါင်းစဉ်စာရင်း” ပြီးဆုံးပြီ»
UDDESA = heads("Uddeso")                                         # အကျဉ်း ဖော်ပြချက်
NIDDESA = heads("Ekakaniddeso").split(" ", 1)[1]                 # အကျယ် ဖော်ပြချက်
PANNATTI = witness("1", "^1-M2-108", "paññatti dhammā", "သတ်မှတ်ချက်")   # paññatti = «သတ်မှတ်ချက်» (pi-1)
PUGGALA = witness("2", "^2-643", "ekaṃ puggalaṃ", "ပုဂ္ဂိုလ်")             # puggala = «ပုဂ္ဂိုလ်» (pi-1 / pi-2)
PUG_PL = PUGGALA + "တို့"
witness("1", "^1-1335", "Ye te puggalā", "ပုဂ္ဂိုလ်တို့")
CL_P = "ယောက်"                                                   # classifier of persons (pi-2 «ပုဂ္ဂိုလ် တစ်ယောက်»)
witness("2", "^2-643", "ekaṃ puggalaṃ", f"{PUGGALA} တစ်{CL_P}")
CL = "ပါး"                                                       # classifier of things (pi-1 / pi-2)
PATHA, LEKHANA = "ပါဌ်ကွဲ", "စာလုံးပေါင်းကွဲ"                     # variant labels (pi-1 style rules)
witness("1", "^1-M2-126", "paṭisandhāro ca (ka.)", f"[{LEKHANA} (Ka.): paṭisandhāro ca]")
witness("1", "^1-M2-142", "suttantamātikā (syā.)", f"[{PATHA} (Syā.): suttantamātikā]")

# number words: Pāli cardinal (any case form used) -> number; Burmese numbers
NUM_MY = {1: "တစ်", 2: "နှစ်", 3: "သုံး", 4: "လေး", 5: "ငါး", 6: "ခြောက်", 7: "ခုနစ်", 8: "ရှစ်", 9: "ကိုး", 10: "ဆယ်",
          12: "ဆယ့်နှစ်", 18: "ဆယ့်ရှစ်", 22: "နှစ်ဆယ့်နှစ်", 54: "ငါးဆယ့်လေး"}
NUM_PI = {"eka": 1, "ekaṃ": 1, "dve": 2, "dvinnaṃ": 2, "tayo": 3, "tīṇi": 3, "tiṇṇaṃ": 3, "tīhi": 3,
          "cattāro": 4, "cattāri": 4, "pañca": 5, "pañcannaṃ": 5, "cha": 6, "chahi": 6, "satta": 7, "aṭṭha": 8,
          "nava": 9, "dasa": 10}
for _n, _w in ((5, "ငါး"), (12, "ဆယ့်နှစ်"), (18, "ဆယ့်ရှစ်"), (22, "နှစ်ဆယ့်နှစ်")):
    assert NUM_MY[_n] == _w
witness("2", "^2-1", "Pañcakkhandhā", f"အစုအဝေး {NUM_MY[5]}{CL}")
witness("2", "^2-154", "Dvādasāyatanāni", f"အာရုံခံ နယ်ပယ် {NUM_MY[12]}{CL}")
witness("2", "^2-183", "Aṭṭhārasa dhātuyo", f"ဓာတ် {NUM_MY[18]}{CL}")
witness("2", "^2-219", "Bāvīsatindriyāni", f"စွမ်းရည် {NUM_MY[22]}{CL}")


def persons(n):
    """«Dve puggalā» = «ပုဂ္ဂိုလ် နှစ်ယောက်»; the counted noun stands before the number (pi-1 / pi-2)."""
    return f"{NUM_MY[n]}{CL_P}"


# ===================================================================================== variant readings
SIGLA = {"sī.": "Sī.", "syā.": "Syā.", "ka.": "Ka.", "pī.": "Pī."}
REF = {"a. ni.": "“အင်္ဂုတ္တရနိကာယ်”"}          # sutta references after the sigla (pi-2 ^2-957 pattern)
witness("2", "^2-957", "codiyamāno (sī. syā.) a. ni. 8.14",
        f"[{LEKHANA} (Sī., Syā.): codiyamāno၊ {REF['a. ni.']} 8.14]")
VAR_KIND = {     # the variant's Pāli -> word variant (PATHA) or spelling only (LEKHANA)
    "paccekabuddho": PATHA, "arahattāya": PATHA, "palāsī": LEKHANA, "uccaṅgupañño": LEKHANA,
    "garukatvā": LEKHANA, "paripūrīkārī": LEKHANA, "appasāvajjo": PATHA, "vipacitaññū": LEKHANA,
    "balibaddūpamā": LEKHANA, "sītibhūto": LEKHANA, "pāragato": PATHA, "ārambhati": LEKHANA, "phalesu": PATHA,
    "anāgantvā": PATHA, "sotāpannasakadāgāmī": PATHA,
    # ch2
    "phassitvā": LEKHANA, "paññavantā": LEKHANA, "sambodhiparāyaṇo": LEKHANA, "kālaṃ kiriyaṃ": LEKHANA,
}
VAR_RE = re.compile(r"\[(?P<t>[^\[\]()]+?) \((?P<s>[^()]+)\)(?: (?P<r>[a-z]+\. [a-z]+\.) (?P<n>[\d.]+))?\]")


def var_my(br):
    """«[appasāvajjo (syā. ka.) a. ni. 4.135]» -> «[ပါဌ်ကွဲ (Syā., Ka.): appasāvajjo၊ “အင်္ဂုတ္တရနိကာယ်” 4.135]»."""
    m = VAR_RE.fullmatch(br)
    if not m or m["t"] not in VAR_KIND:
        raise Miss("variant: " + br)
    sig = ", ".join(SIGLA[s] for s in re.findall(r"[a-zāīū]+\.", m["s"]))
    ref = f"{C} {REF[m['r']]} {m['n']}" if m["r"] else ""
    return f"[{VAR_KIND[m['t']]} ({sig}): {m['t']}{ref}]"


BR_RE = re.compile(r"\[[^\]]*\]")


def fill(my, pali):
    """Put the translated brackets of the Pāli into the placeholders ⟦0⟧, ⟦1⟧ … of a Burmese value."""
    brs = BR_RE.findall(pali)
    for i, br in enumerate(brs):
        tok = f"⟦{i}⟧"
        if my.count(tok) != 1:
            raise Miss(f"placeholder {tok} {my.count(tok)}x for «{pali[:60]}»")
        my = my.replace(tok, var_my(br))
    if "⟦" in my:
        raise Miss(f"placeholder without bracket in «{pali[:60]}»")
    return my


# ===================================================================================== the six designations
KH, AY, DT, SC, IN = "အစုအဝေး", "အာရုံခံ နယ်ပယ်", "ဓာတ်", "သစ္စာ", "စွမ်းရည်"
TOPIC = {"khandha": KH, "āyatana": AY, "dhātu": DT, "sacca": SC, "indriya": IN, "puggala": PUGGALA}
GEN_PL = {"khandhānaṃ": "khandha", "āyatanānaṃ": "āyatana", "dhātūnaṃ": "dhātu", "saccānaṃ": "sacca",
          "indriyānaṃ": "indriya", "puggalānaṃ": "puggala"}
LIST_HEAD = {}
LIST_ITEM = {}
for _b, _bid in (("2", "^2-1"), ("2", "^2-154"), ("2", "^2-183"), ("2", "^2-219")):
    _h, _it = items(_b, _bid)
    _ph = novar(strip_id(FINAL.seg(_b, _bid)[1][0])).split(" – ")[0]
    LIST_HEAD[_ph[0].lower() + _ph[1:]] = _h
    LIST_ITEM.update(_it)
assert LIST_HEAD["pañcakkhandhā"] == f"{KH} {NUM_MY[5]}{CL}" and LIST_HEAD["bāvīsatindriyāni"].startswith(IN)
LIST_HEAD["cattāri saccāni"] = items("2", "^2-206")[0]           # «သစ္စာ လေးပါး»
for _p, _m in (("dukkhasaccaṃ", "ဒုက္ခ သစ္စာ"), ("samudayasaccaṃ", "ဖြစ်ပေါ်ခြင်း သစ္စာ"),
               ("nirodhasaccaṃ", "ချုပ်ငြိမ်းခြင်း သစ္စာ"), ("maggasaccaṃ", "မဂ် သစ္စာ")):
    LIST_ITEM[_p] = witness("2", "^2-218", _p[0].upper() + _p[1:], _m + "သည်")[:-3]


def pannatti_my(stem):
    """khandhapaññatti = «အစုအဝေး သတ်မှတ်ချက်»."""
    return f"{TOPIC[stem]} {PANNATTI}"


def gen_my(gen):
    """khandhānaṃ = «အစုအဝေးတို့၏»."""
    return f"{TOPIC[GEN_PL[gen]]}တို့၏"


KITTAVATA_RE = re.compile(r"Kittāvatā (?P<g>\S+) (?P<s>\S+)paññatti\?")
YAVATA_RE = re.compile(r"Yāvatā (?P<h>.+?) – (?P<l>.+); ettāvatā (?P<g>\S+) (?P<s>\S+)paññatti\.")


def kittavata_my(m):
    g, s = m["g"], m["s"]
    if GEN_PL.get(g) != s:
        raise Miss("kittāvatā: " + m[0])
    return f"{gen_my(g)} {pannatti_my(s)}သည် အဘယ်မျှ ရှိသနည်း{END}"


def yavata_my(m):
    g, s = m["g"], m["s"]
    if GEN_PL.get(g) != s:
        raise Miss("yāvatā: " + m[0])
    its = [x.strip() for x in m["l"].split(",")]
    for x in its:
        if x not in LIST_ITEM:
            raise Miss("topic item: " + x)
    return (f"{LIST_HEAD[m['h']]} – {f'{C} '.join(LIST_ITEM[x] for x in its)} ရှိသမျှ{C} "
            f"ဤမျှသည် {gen_my(g)} {pannatti_my(s)} ဖြစ်သည်{END}")


# ===================================================================================== headings and colophons
NUM_STEM = {"Ekaka": 1, "Duka": 2, "Tika": 3, "Catukka": 4, "Pañcaka": 5, "Chakka": 6, "Sattaka": 7,
            "Aṭṭhaka": 8, "Navaka": 9, "Dasaka": 10}
COLO = {}        # «Ekakaṃ.» … «Dasakaṃ.» (pi-1 / pi-2 final)
for _s in NUM_STEM:
    COLO[_s + "ṃ"] = heads(_s + "ṃ")
    assert COLO[_s + "ṃ"] == f"{NUM_MY[NUM_STEM[_s]]}မျိုးတွဲ"
HEAD = {"Mātikā": MATIKA_W, "Niddeso": NIDDESA, "Puggalapaññattipāḷi": TITLE, "Abhidhammapiṭake": ABHI}
for _s, _n in NUM_STEM.items():
    HEAD[_s + "uddeso"] = f"{COLO[_s + 'ṃ']} {UDDESA}"                       # Ekakauddeso (pi-1 Uddeso)
    HEAD[_s + "puggalapaññatti"] = f"{COLO[_s + 'ṃ']} {pannatti_my('puggala')}"
    COLO[_s + "niddeso"] = f"{COLO[_s + 'ṃ']} {NIDDESA}"                     # Ekakaniddeso (pi-1 / pi-2)
for _s in ("Ekaka", "Duka", "Tika"):
    assert COLO[_s + "niddeso"] == heads(_s + "niddeso")
FIXED = {
    "Namo tassa bhagavato arahato sammāsambuddhassa": NAMO,          # no «။» (pi-1 / pi-2 / pi-3 preamble)
    "Puggalapaññattimātikā niṭṭhitā.": f"“{pannatti_my('puggala')} {MATIKA_W}” ပြီးဆုံးပြီ{END}",
    "Puggalapaññattipakaraṇaṃ niṭṭhitaṃ.": f"“{TITLE}” ကျမ်း ပြီးဆုံးပြီ{END}",
}
assert MATIKA_END_PAT == f"“{MATIKA_W}” ပြီးဆုံးပြီ"

# ===================================================================================== reused words (pi-1/2/3 final)
W = {}           # short key -> Burmese, every one witnessed in a rails segment


def _w(key, book, bid, pali, my):
    W[key] = witness(book, bid, pali, my)


_w("ariya", "1", "^1-1305", "ariyamaggesu", "အရိယာ")
_w("ariyamagga", "1", "^1-1038", "Ariyamaggaṃ", "အရိယာ မဂ်")
_w("magga", "2", "^2-807", "Sotāpattimagge", "မဂ်")
_w("phala", "2", "^2-807", "sotāpattiphale", "ဖိုလ်")
_w("maggasamangi", "1", "^1-1382", "maggasamaṅgissa", "မဂ်နှင့် ပြည့်စုံသူ")
_w("phalasamangi", "1", "^1-1383", "phalasamaṅgissa", "ဖိုလ်နှင့် ပြည့်စုံသူ")
_w("sotapattiphala", "2", "^2-807", "sotāpattiphale", "သောတာပတ္တိဖိုလ်")
_w("sakadagamiphala", "2", "^2-807", "sakadāgāmiphale", "သကဒါဂါမိဖိုလ်")
_w("anagamiphala", "2", "^2-807", "anāgāmiphale", "အနာဂါမိဖိုလ်")
_w("arahattaphala", "2", "^2-807", "arahattaphale", "ရဟန္တာဖိုလ်")
_w("sekkha", "1", "^1-M1-11", "sekkhā dhammā", "ကျင့်ကြံဆဲသူ")
_w("asekkha", "1", "^1-M1-11", "asekkhā dhammā", "ကျင့်ကြံမှု ပြီးဆုံးသူ")
_w("nevasekkha", "2", "^2-753", "nevasekkhanāsekkhā paññā",
   "ကျင့်ကြံဆဲသူ၏လည်း မဟုတ်၊ ကျင့်ကြံမှု ပြီးဆုံးသူ၏လည်း မဟုတ်သော")
_w("puthujjana", "2", "^2-U8", "puthujjano", "ပုထုဇဉ်")
_w("araha", "2", "^2-U55", "arahanto jīvitā", "ရဟန္တာ")
_w("sammasambuddha", "2", "^2-809", "sammāsambuddhā", "အမှန်ကို ကိုယ်တိုင် အပြည့်အဝ သိမြင်တော်မူသော ဘုရားရှင်")
_w("vimokkha", "2", "^2-828", "Aṭṭha vimokkhā", "လွတ်မြောက်ခြင်း ရှစ်ပါး")
_w("asava", "1", "^1-M2-14", "āsavā dhammā", "စိတ်အစွန်းအထင်း")
_w("samyojana", "2", "^2-17-4-7-0", "Tīṇi saṃyojanāni", "နှောင်ကြိုး သုံးပါး")
_w("samapatti", "1", "^1-M2-120", "samāpattikusalatā", "ဈာန် ဝင်စားရာ")
_w("vutthana", "1", "^1-M2-120", "samāpattivuṭṭhānakusalatā", "ဈာန် ဝင်စားရာမှ ထမြောက်ရာ")
_w("vijja", "1", "^1-M2-141", "vijjā ca", "အမှန်သိမြင်မှု")
_w("abhinna6", "2", "^2-756", "Chasu abhiññāsu", "ထူးကဲစွာ သိခြင်း ခြောက်ပါး")
_w("sacca", "2", "^2-206", "Cattāri saccāni", "သစ္စာ လေးပါး")
_w("dukkha", "2", "^2-206", "dukkhaṃ, dukkhasamudayo", "ဒုက္ခ၊ ဒုက္ခ ဖြစ်ပေါ်ခြင်း၊ ဒုက္ခ ချုပ်ငြိမ်းခြင်း၊ "
   "ဒုက္ခ ချုပ်ငြိမ်းရာသို့ ရောက်စေသော ကျင့်စဉ်")
_w("yathabhutam_pajanati", "2", "^2-760", "yathābhūtaṃ pajānāti", "ဟုတ်မှန်သည့်အတိုင်း ကွဲပြားစွာ သိ")
_w("tathagata", "2", "^2-760", "tathāgato", "မြတ်စွာဘုရား")
_w("idhekacco", "2", "^2-925", "Idhekacco samaṇo", "ဤလောက၌ အချို့သော")
_w("ekacco", "2", "^2-932", "Idhekacco assaddho", "အချို့သော")
_w("sabbepi", "1", "^1-1310", "Sabbepi kusalā dhammā", "ကုသိုလ် သဘောတရား အားလုံးသည်")
_w("ananantarika", "2", "^2-U55", "pañca kammāni ānantarikāni", "ချက်ချင်း အကျိုးပေးသော ကံ ငါးပါး")
_w("apubbam_acarimam", "2", "^2-809", "apubbaṃ acarimaṃ", "ရှေ့ မရှိ၊ နောက် မရှိဘဲ")
_w("atthanam", "2", "^2-809", "Aṭṭhānametaṃ anavakāso", "ဟူသည် မဖြစ်နိုင်သော အကြောင်း ဖြစ်သည်၊ အခွင့်အလမ်း မရှိ")
_w("thanam", "2", "^2-809", "Ṭhānañca kho etaṃ vijjati", "ဟူသည်ကား ဖြစ်နိုင်သော အကြောင်း ရှိသည်")
_w("pamada", "2", "^2-17-2-4-0", "Pamādo", "မေ့လျော့မှု")
_w("agamma", "2", "^2-760", "yaṃ balaṃ āgamma", "စွမ်းအားကို မှီ၍")
_w("ditthe_dhamme", "2", "^2-831", "diṭṭheva dhamme", "မျက်မှောက်ဘဝ၌ပင်")
_w("cetovimuttim", "2", "^2-831", "cetovimuttiṃ paññāvimuttiṃ", "စိတ်၏ လွတ်မြောက်ခြင်း၊ ပညာဖြင့် လွတ်မြောက်ခြင်း")
_w("avarana", "2", "^2-826", "kammāvaraṇena samannāgatā", "ကံ အဟန့်အတားနှင့် အပြည့်အဝ ပြည့်စုံသော")
_w("rupa_raga", "2", "^2-U49", "Rūparāgo, arūparāgo, māno, uddhaccaṃ, avijjā",
   "သိမ်မွေ့သော ရုပ်ဘဝကို တပ်မက်သော ရာဂ၊ ရုပ်မရှိသော ဘဝကို တပ်မက်သော ရာဂ၊ မာန၊ ယောက်ယက်ခတ်မှု၊ အမှန်ကို မသိမှု")
_w("orambhagiya", "2", "^2-17-6-1-0", "Pañcorambhāgiyāni saṃyojanāni", "အောက်ပိုင်း ဘုံနှင့် ဆိုင်သော နှောင်ကြိုး ငါးပါး")
_w("kamaraga", "2", "^2-919", "kāmarāgo", "ကာမရာဂ")
_w("tanubhavaya", "1", "^1-361", "tanubhāvāya", "ပါးလျစေရန်")
_w("opapatika", "2", "^2-1010", "Opapātikānaṃ petānaṃ", "အလိုအလျောက် ပေါ်လာသော")
_w("ayuppamana", "2", "^2-1022", "āyuppamāṇaṃ", "သက်တမ်း အတိုင်းအတာ")
_w("kalakiriya", "2", "^2-193", "kālakiriyā", "ကွယ်လွန်ခြင်း")
_w("sasankharena", "1", "^1-156", "sasaṅkhārena", "တိုက်တွန်းမှုဖြင့်")
_w("samanantara", "2", "^2-751", "samanantarā", "ချက်ချင်း နောက်၌")
_w("nibbatteti", "2", "^2-392", "nibbatteti", "ပေါ်ထွက်စေ")
_w("kulani", "2", "^2-514", "kulāni", "အမျိုး")
_w("deva", "1", "^1-1287", "deve", "နတ်")
_w("bhava", "2", "^2-809", "aṭṭhamaṃ bhavaṃ", "အဋ္ဌမ ဘဝ")
_w("Avihānaṃ", "2", "^2-1027", "Avihānaṃ devānaṃ", "အဝိဟာ နတ်")
for _p, _m in (("Atappānaṃ", "အတပ္ပါ"), ("Sudassānaṃ", "သုဒဿာ"), ("Sudassīnaṃ", "သုဒဿီ"), ("Akaniṭṭhānaṃ", "အကနိဋ္ဌ")):
    _w(_p, "2", "^2-1027", _p + " devānaṃ", _m + " နတ်")
_w("tehi_dhammehi", "3", "^3-355", "tehi dhammehi", "ထိုသဘောတရားတို့နှင့်")
_w("kusalesu", "1", "^1-M2-140", "kusalesu dhammesu", "ကုသိုလ် သဘောတရားတို့၌")
_w("indriya_sense", "1", "^1-M2-127", "indriyesu aguttadvāratā", "အာရုံခံ အင်္ဂါတို့၏ တံခါးကို မစောင့်ထိန်းခြင်း")

# ===================================================================================== consistency pass (harmonise)
# The book-wide forms chosen in the consistency pass (harmonise-todo.md A1 … A5, B1 … B8; log: harmonise-notes.md).
# Every generator takes these values from here, so that one Pāli item has one Burmese form in the whole book.
# ---- B4 the Buddha (coordinator decision): tathāgata and bhagavā = «မြတ်စွာဘုရား» (pi-1 / pi-2 / pi-3 termbases);
#      only in the ^4-177 epithet list «… buddho bhagavā» (tathāgato the subject) bhagavā = «ဘုန်းတော်ရှင်»
BHAGAVA = witness("1", "^T-1", "bhagavato", "မြတ်စွာဘုရား")       # bhagavā / bhagavatā / bhagavato
TATHAGATA = W["tathagata"]                                       # tathāgata = «မြတ်စွာဘုရား» (pi-2 ^2-760, termbase)
BHAGAVA_EPITHET = "ဘုန်းတော်ရှင်"                                 # bhagavā as an epithet of the subject tathāgato (^4-177)
# ---- B3 the person: So = «ထိုသူသည်», tassa / assa = «ထိုသူ၏» (…အတွက် / …ကို), Tassa evaṃ hoti = «ထိုသူအား …»
SO = "ထိုသူသည်"
TASSA = "ထိုသူ၏"
TASSA_EVAM = "ထိုသူအား ဤသို့ အကြံ"                                  # Tassa (na) evaṃ hoti = «… ဖြစ်၏ / မဖြစ်»
# ---- B1 frames of the group definitions
EVAMEVAM = witness("2", "^2-643", "evameva", "ထို့အတူပင်")          # evamevaṃ (pi-2 evameva)
SEYYA = "ဥပမာအားဖြင့်"                                              # seyyathāpi (nāma)
SANTO_PL = f"ရှိကြ၏{C} ထင်ရှား ရှိကြ၏"                                 # santo saṃvijjamānā (plural)
SANTO_SG = f"ရှိ၏{C} ထင်ရှား ရှိ၏"                                     # santo saṃvijjamāno (singular)
LOKE = "လောက၌"                                                       # lokasmiṃ
BHIKKHUSU = "ရဟန်းတို့အတွင်း၌"                                         # bhikkhūsu


def tathupamo_my(noun, pred):
    """«Seyyathāpi so NOUN PRED, tathūpamo ayaṃ puggalo.» = «ဥပမာအားဖြင့် ထိုNOUNသည် PREDသကဲ့သို့၊ ဤပုဂ္ဂိုလ်သည်
    ထိုNOUNနှင့် တူ၏။» (the Pāli comma = «၊»)."""
    return f"{SEYYA} ထို{noun}သည် {pred}သကဲ့သို့{C} ဤ{PUGGALA}သည် ထို{noun}နှင့် တူ၏{END}"


def tattha_katame_my(n, group):
    """«Tattha katame N GROUP puggalā?» = «ထိုတို့အနက် GROUP ပုဂ္ဂိုလ် N-ယောက် ဟူသည် အဘယ် ပုဂ္ဂိုလ်တို့နည်း။»."""
    return f"ထိုတို့အနက် {group} {PUGGALA} {persons(n)} ဟူသည် အဘယ် {PUGGALA}တို့နည်း{END}"


def katame_n_my(n):
    """«Katame N?» (no «puggalā» in the Pāli) = «အဘယ် N-ယောက်တို့နည်း။»."""
    return f"အဘယ် {persons(n)}တို့နည်း{END}"


def ime_santo_my(group, n, where, evam=False):
    """«(Evamevaṃ) ime N GROUP puggalā santo saṃvijjamānā WHERE.» = «(ထို့အတူပင်) GROUP ဤပုဂ္ဂိုလ် N-ယောက်တို့သည်
    WHERE ရှိကြ၏၊ ထင်ရှား ရှိကြ၏။»."""
    return f"{EVAMEVAM + ' ' if evam else ''}{group} ဤ{PUGGALA} {persons(n)}တို့သည် {where} {SANTO_PL}{END}"


VUCCATI_BARE = f"ဤ{PUGGALA}ကို {{}}ဟု ခေါ်သည်{END}"     # «Ayaṃ vuccati puggalo X.» without quotes: no quotes (A2 / B1)
# ---- B2 sentences shared between the chapters
DUSS_HOTI = witness("2", "^2-851", "dussīlo", "သီလ ပျက်သူ") + "၊ ယုတ်မာသော သဘော ရှိသူ ဖြစ်၏"
#   dussīlo hoti pāpadhammo: pi-2 dussīla «သီလ ပျက်သူ»; «X hoti Y» = «X၊ Y ဖြစ်၏» (the sample's «… lābhī hoti
#   akicchalābhī akasiralābhī» = «… ရရှိသူ၊ … ရရှိသူ၊ … ရရှိသူ ဖြစ်၏»)
SIL_HOTI = witness("2", "^2-851", "sīlavā", "သီလ ရှိသူ") + "၊ ကောင်းမွန်သော သဘော ရှိသူ ဖြစ်၏"   # sīlavā hoti kalyāṇadhammo
OFTEN_ANGRY = "ခဏခဏ အမျက်ဒေါသ ထွက်၏"                         # abhiṇhaṃ kujjhati (kodhano «အမျက်ဒေါသ ထွက်တတ်သူ»)
NOT_OFTEN_ANGRY = "ခဏခဏ အမျက်ဒေါသ မထွက်"                      # naheva kho abhiṇhaṃ kujjhati
KODHO_LONG = "ထိုသူ၏ ထိုအမျက်ဒေါသသည်ကား ကြာမြင့်စွာ ရှည်လျားသော ကာလပတ်လုံး ကိန်းအောင်း၏"   # So ca khvassa kodho …
KODHO_SHORT = "ထိုသူ၏ ထိုအမျက်ဒေါသသည်ကား ကြာမြင့်စွာ ရှည်လျားသော ကာလပတ်လုံး မကိန်းအောင်း"  # … na ciraṃ …
_NELA_A = witness("1", "^1-1350", "neḷā kaṇṇasukhā pemanīyā hadayaṅgamā porī bahujanakantā bahujanamanāpā",
                  "အပြစ်ကင်းသော၊ နား သာယာသော၊ ချစ်ခင်ဖွယ်ကောင်းသော၊ နှလုံးသားသို့ ရောက်သော၊ ယဉ်ယဉ်ကျေးကျေး ရှိသော၊ "
                  "လူအများ နှစ်သက်သော၊ လူအများ စိတ်တွေ့သော စကား ရှိ၏")
_NELA_B = witness("1", "^1-1350", "tathārūpiṃ vācaṃ bhāsitā hoti", "ထိုသို့သော စကားကို ပြောဆိုသူ ဖြစ်၏")
NELA = f"{_NELA_A} {_NELA_B}"            # yā sā vācā nelā … bahujanamanāpā tathārūpiṃ vācaṃ bhāsitā hoti (pi-1 ^1-1350)
NELA_C = f"{_NELA_A}{C} {_NELA_B}"       # the same with a comma before «tathārūpiṃ» (^4-99 in ch4)
SAMAHITE = ("ဤသို့ စိတ်သည် တည်ကြည်၍၊ စင်ကြယ်၍၊ ဖြူစင်၍၊ အမည်းအစက် မရှိ၍၊ ညစ်နွမ်းစေတတ်သော အညစ်အကြေး ကင်း၍၊ "
            "နူးညံ့၍၊ အသုံးပြုရန် သင့်တော်၍၊ တည်တံ့၍၊ မတုန်လှုပ်ခြင်းသို့ ရောက်သောအခါ")   # evaṃ samāhite citte … (ch5)
ASAVA4 = [f"ဤသည်တို့ကား {W['asava']}တို့", f"ဤသည်ကား {W['asava']} ဖြစ်ပေါ်ခြင်း",
          f"ဤသည်ကား {W['asava']} ချုပ်ငြိမ်းခြင်း", f"ဤသည်ကား {W['asava']} ချုပ်ငြိမ်းရာသို့ ရောက်စေသော ကျင့်စဉ်"]
#   "ime āsavā"ti … "ayaṃ āsavanirodhagāminī paṭipadā"ti (ime = plural «ဤသည်တို့ကား»)
JANATO = (f"ဤသို့ သိသော{C} ဤသို့ မြင်သော {TASSA} စိတ်သည် " +
          f"{C} ".join(f"{x} {W['asava']}မှလည်း လွတ်မြောက်၏" for x in ("ကာမ", "ဘဝ", "အမှန်ကို မသိမှု")) + END)
VIMUTTASMIM = f"လွတ်မြောက်ပြီးသောအခါ “လွတ်မြောက်ပြီ”ဟု ဉာဏ် ဖြစ်၏{END}"   # Vimuttasmiṃ vimuttamiti ñāṇaṃ hoti.
KHINA = ("“မွေးဖွားခြင်း ကုန်ပြီ၊ မြင့်မြတ်သော အကျင့်ကို ကျင့်ပြီးပြီ၊ ပြုဖွယ်ကို ပြုပြီးပြီ၊ ဤအဖြစ်အတွက် နောက်ထပ် "
         f"ပြုဖွယ် မရှိတော့ပြီ”ဟု ကွဲပြားစွာ သိ၏{END}")       # "Khīṇā jāti, … itthattāyā"ti pajānāti.
# ---- B5 distinct terms
VIPPATISARA = witness("1", "^1-1166", "cetaso vippaṭisāro", "နောင်တ ရခြင်း")   # vippaṭisāra (pi-1 / pi-2 termbase)
VIPPATISARI = "နောင်တ ရသူ"                                    # vippaṭisārī (kukkucca stays «နောင်တ ပူပန်မှု»)
VIPASSATI = "သေချာစွာ မြင်၍ ပတ်ဝန်းကျင်ကို ကြည့်"               # vipassati viloketi (no mark between: «၍», A1 rule)
# ---- B6 simile and list vocabulary
KHIRA = witness("2", "^2-174", "khīraṃ", "နွားနို့")             # khīra (pi-1 / pi-2 termbase)
SALLEKHA = "ခြိုးခြံခြင်း"                                       # sallekha (A3: no object «ကိလေသာကို» added)
IDHA_PANA = "တစ်ဖန်"                                             # Idha pana(ekacco) = «တစ်ဖန် ဤလောက၌ …» (ch4)
# ---- B7 one variant-bracket renderer for the whole book (replaces the three generator extensions)
VAR_KIND.update({
    # ch3 / ch4
    "dūsanā dūsitattaṃ": LEKHANA, "ussuyā ussuyanā": LEKHANA, "sukaṭadukkaṭānaṃ": LEKHANA, "samaggatā": PATHA,
    "evameva": LEKHANA, "dhammassavanāya": LEKHANA, "paṭhaviyā": LEKHANA, "patiṭṭhīyati": LEKHANA,
    "assavanoti": PATHA, "nikujjo": LEKHANA, "tilataṇḍulā": LEKHANA, "… ceva": PATHA, "pavattanī": LEKHANA,
    "paññāpeti": LEKHANA, "ehi bho": LEKHANA, "āṭhapanā": LEKHANA, "makkhīyanā makkhīyitattaṃ": LEKHANA,
    "makkhiyanā makkhiyitattaṃ": LEKHANA, "kakkhaḷatā kakkhaḷiyaṃ": PATHA, "asaṃgāhanā apariyogāhanā": LEKHANA,
    "vipariyesaggāho": PATHA, "tappetā ca, ayaṃ vuccati puggalo titto": PATHA, "gato": PATHA, "gantvā": PATHA,
    "kathalāya": LEKHANA, "kathalena": LEKHANA, "yesaṃ kho pana": PATHA, "patigaṇhāti": LEKHANA,
    # ch5
    "pisuṇāvāco": LEKHANA, "pharusāvāco": LEKHANA, "micchādiṭṭhī": LEKHANA, "sammādiṭṭhī": LEKHANA,
    "yuttapaṭibhāṇo": LEKHANA, "pakkavaṇṇī": LEKHANA, "āmavaṇṇī": LEKHANA, "sammiñjitaṃ": LEKHANA,
    "balibaddhā": LEKHANA, "sagavacaṇḍo": PATHA, "āsivisā": LEKHANA, "neva kho": PATHA,
    "paranimmitavasavattideve": LEKHANA, "veṇakule": LEKHANA, "daḷidde": LEKHANA, "paravaṇṇahāriyā": LEKHANA,
    "hatthāvalekhano": LEKHANA, "kalopimukhā": LEKHANA, "dvāhikampi": LEKHANA, "ulukapakkhampi": LEKHANA,
    "sāyaṃtatiyakampi": LEKHANA, "muddhābhisitto": PATHA, "santāgāraṃ": PATHA, "yaññāgāraṃ": PATHA,
    "khurājinaṃ": PATHA, "kaṇḍūyamāno": LEKHANA, "parihiṃsatthāyāti": PATHA, "anācārī": PATHA,
    "… sāviyogā": PATHA, "thīnamiddhaṃ": LEKHANA, "na dhammamaññāya na dhammānudhammapaṭipanno": PATHA,
    "na dhammamaññāya dhammānudhammappaṭipanno": PATHA,
    # ch6 … ch11
    "ārabbhajā": LEKHANA, "ayaṃ pana": PATHA, "satthambhati": LEKHANA, "ussādanaṃyeva": PATHA,
    "ussādanaññeva": PATHA, "santānetuṃ": PATHA, "āvīkatvā": LEKHANA, "sāmaṃyeva": PATHA, "uhasati": LEKHANA,
    "appicchaṃyeva": PATHA, "idamaṭṭhitaṃyeva": LEKHANA, "mokkho": PATHA, "nonītaṃ": LEKHANA,
    "dukkhassantaṃ karoti": PATHA, "sāhu": LEKHANA, "viriyaṃ": LEKHANA,
})
SIGLA_ALL = dict(SIGLA, **{"aṭṭhakathā": "အဋ္ဌကထာ", "sabbattha": "Sabbattha"})
witness("2", "^2-811", "aṭṭhakathā oloketabbā", "အဋ္ဌကထာ")
witness("2", "^2-754", "(sabbattha)", "(Sabbattha)")
REF.update({"vibha.": f"“{TITLE2}”", "ma. ni.": "“မဇ္ဈိမနိကာယ်”", "dī. ni.": "“ဒီဃနိကာယ်”"})
witness("2", "^2-760", "ma. ni. 1.148", f"{REF['ma. ni.']} 1.148")
witness("2", "^2-924", "dī. ni. 3.305", f"{REF['dī. ni.']} 3.305")
witness("2", "^2-832", "nijigiṃsanatā (sī.), jigiṃsanatā (syā.)", "(Sī.): nijigiṃsanatā၊ (Syā.): jigiṃsanatā")
LIKEWISE = witness("2", "^2-796", "evamuparipi", "ဤနည်းတူ")        # evaṃ / evameva in the editors' notes
BR_NOTE_END = {  # an editors' note after the readings (and references) -> Burmese
    "evamuparipi": f"နောက်တွင်လည်း {LIKEWISE}",                               # pi-2 ^2-796
    "evaṃ tīsu ṭhānesupi": f"နေရာ သုံးခုလုံး၌လည်း {LIKEWISE}",
    "evaṃ khuddakavibhaṅgadukaniddesepi": f"“{heads('Khuddakavatthuvibhaṅgo')}”၏ {COLO['Dukaniddeso']}၌လည်း {LIKEWISE}",
    "padasiddhi cintetabbā": "ပုဒ်၏ ဖြစ်ပုံကို စဉ်းစားရမည်",
    "rūpasiddhiṭīkāya pana sameti": "ရူပသိဒ္ဓိ ဋီကာနှင့်ကား ညီ၏",
    "passa aṅguttaranikāye": f"{REF['a. ni.']}ကို ကြည့်ပါ",
}
BR_NOTE = {      # a bracket that is only an editors' note -> Burmese
    "[( ) natthi sīhaḷapotthake. majjhimanikāye kandarakasuttepi evameva]":
        f"[( ) ကွင်းအတွင်းရှိ စကားရပ်သည် သီဟိုဠ် ပေစာမူ၌ မရှိ{C} {REF['ma. ni.']} ကန္ဒရကသုတ်၌လည်း {LIKEWISE}]",
    "[passa ma. ni. 2 kandarakasutte; a. ni. 1 attantapasutte ca]":
        f"[{REF['ma. ni.']} 2 ကန္ဒရကသုတ်နှင့် {REF['a. ni.']} 1 အတ္တန္တပသုတ်ကိုလည်း ကြည့်ပါ]",
}
_REF1 = re.compile(r"(?P<r>a\. ni\.|ma\. ni\.|dī\. ni\.|vibha\.) (?P<n>[\d.]+)")
_REFS = re.compile(r"(?: (?:a\. ni\.|ma\. ni\.|dī\. ni\.|vibha\.) [\d.]+;?)+$")
_READ = re.compile(r"(?P<t>[^\[\](),\s][^\[\]()]*?) \((?P<s>[^()]+)\)")
_sample_var_my = var_my


def var_all(br):
    """The one renderer of the book: «[a (sī.), b (syā. ka.) a. ni. 5.141; ma. ni. 1.440 NOTE]» -> «[L (Sī.): a၊
    (Syā., Ka.): b၊ “…” 5.141၊ “…” 1.440၊ NOTE]» (pi-2 ^2-832: the label once, from the first reading); a reading
    without sigla «[X]» = «[L: X]»; whole-bracket notes BR_NOTE; the sample's var_my() gives the same output for its
    own brackets (checked by the rebuild)."""
    if br in BR_NOTE:
        return BR_NOTE[br]
    body, note, refs = br[1:-1], "", []
    for k, v in BR_NOTE_END.items():
        if body.endswith(" " + k):
            body, note = body[:-len(k) - 1], v
    m = _REFS.search(body)
    if m:
        refs = [f"{REF[r['r']]} {r['n']}" for r in _REF1.finditer(m[0])]
        body = body[:m.start()]
    if "(" not in body:
        if body not in VAR_KIND:
            raise Miss("variant: " + br)
        parts = [(VAR_KIND[body], None, body)]
    else:
        whole = re.fullmatch(r"(?P<t>[^\[\]()]+?) \((?P<s>[^()]+)\)", body)
        reads = [whole] if whole and whole["t"] in VAR_KIND else list(_READ.finditer(body))
        pos, parts = 0, []
        for rm in reads:
            if body[pos:rm.start()] not in ("", ", "):
                raise Miss("variant: " + br)
            pos = rm.end()
            if rm["t"] not in VAR_KIND:
                raise Miss("variant kind: " + br)
            parts.append((VAR_KIND[rm["t"]], ", ".join(SIGLA_ALL[s] for s in rm["s"].split()), rm["t"]))
        if pos != len(body) or not parts:
            raise Miss("variant: " + br)
    k0, s0, t0 = parts[0]
    out = [f"{k0} ({s0}): {t0}" if s0 else f"{k0}: {t0}"] + [f"({s}): {t}" for _, s, t in parts[1:]]
    return "[" + f"{C} ".join(out + refs + ([note] if note else [])) + "]"


var_my = var_all          # fill() looks var_my up at call time: the one renderer for every chapter



# ===================================================================================== person-type names
NAME = {}        # niddesa key (lower case) -> Burmese name
ALIAS = {}       # other Pāli spelling of the same type (e.g. the mātikā form) -> key
PLURAL = {}      # plural Pāli form in the definitions -> key
_SRC = {}        # key -> mātikā section (1 … 10) for the terms file


def _n(sec, key, my, *alias):
    if key in NAME and NAME[key] != my:
        raise SystemExit(f"name conflict {key}: {NAME[key]} / {my}")
    NAME[key] = my
    _SRC.setdefault(key, sec)
    for a in alias:
        ALIAS[a] = key


VIM = "လွတ်မြောက်သူ"
PARI = "ပရိနိဗ္ဗာန် ပြုသူ"
# ---- (1) Ekaka: the 54 single types
_n(1, "samayavimutto", f"အချိန်အလိုက် {VIM}")
_n(1, "asamayavimutto", f"အချိန်အလိုက် မဟုတ်ဘဲ {VIM}")
_n(1, "kuppadhammo", "ပျက်ယွင်းတတ်သော သဘော ရှိသူ")
_n(1, "akuppadhammo", "မပျက်ယွင်းတတ်သော သဘော ရှိသူ")
_n(1, "parihānadhammo", "ဆုတ်ယုတ်တတ်သော သဘော ရှိသူ")
_n(1, "aparihānadhammo", "မဆုတ်ယုတ်တတ်သော သဘော ရှိသူ")
_n(1, "cetanābhabbo", "စေတနာဖြင့် ထိန်းနိုင်သူ")
_n(1, "anurakkhaṇābhabbo", "စောင့်ရှောက်ခြင်းဖြင့် ထိန်းနိုင်သူ")
_n(1, "puthujjano", W["puthujjana"])
_n(1, "gotrabhū", "အရိယာ အနွယ်သို့ ပြောင်းသူ")
_n(1, "bhayūparato", "ဘေးကို ကြောက်၍ ရှောင်ကြဉ်သူ")
_n(1, "abhayūparato", "ဘေးကို မကြောက်ဘဲ ရှောင်ကြဉ်သူ")
_n(1, "bhabbāgamano", "ရှေ့သို့ တိုးတက်ရန် ထိုက်တန်သူ")
_n(1, "abhabbāgamano", "ရှေ့သို့ တိုးတက်ရန် မထိုက်တန်သူ")
_n(1, "niyato", "လမ်းကြောင်း ကျိန်းသေသူ")
_n(1, "aniyato", "လမ်းကြောင်း မကျိန်းသေသူ")
_n(1, "paṭipannako", f"{W['magga']}ကို ကျင့်ကြံနေသူ")
_n(1, "phaleṭhito", f"{W['phala']}၌ တည်နေသူ", "phale ṭhito")
_n(1, "samasīsī", f"{W['asava']}နှင့် အသက် တပြိုင်နက် ကုန်ဆုံးသူ")
_n(1, "ṭhitakappī", "ကမ္ဘာကို တည်နေစေသူ")
_n(1, "ariyo", W["ariya"])
_n(1, "anariyo", f"{W['ariya']} မဟုတ်သူ")
_n(1, "sekkho", W["sekkha"])
_n(1, "asekkho", W["asekkha"])
_n(1, "nevasekkhanāsekkho", f"{W['sekkha']}လည်း မဟုတ်{C} {W['asekkha']}လည်း မဟုတ်သူ")
_n(1, "tevijjo", f"{W['vijja']} သုံး{CL} ရှိသူ")
_n(1, "chaḷabhiñño", f"{W['abhinna6']} ရှိသူ")
_n(1, "sammāsambuddho", W["sammasambuddha"])
_n(1, "paccekasambuddho", "ပစ္စေကဗုဒ္ဓါ")
_n(1, "ubhatobhāgavimutto", f"နှစ်ဖက်စလုံးမှ {VIM}")
_n(1, "paññāvimutto", f"ပညာဖြင့် {VIM}")
_n(1, "kāyasakkhī", "ကိုယ်ဖြင့် မျက်မှောက်ပြုသူ")
_n(1, "diṭṭhippatto", "မှန်ကန်သော အယူသို့ ရောက်သူ")
_n(1, "saddhāvimutto", f"ယုံကြည်မှုဖြင့် {VIM}")
_n(1, "dhammānusārī", "တရားကို အစဉ်လိုက်သူ")
_n(1, "saddhānusārī", "ယုံကြည်မှုကို အစဉ်လိုက်သူ")
_n(1, "sattakkhattuparamo", "အများဆုံး ခုနစ်ကြိမ်သာ ပြန်လည် ဖြစ်ပေါ်သူ")
_n(1, "kolaṅkolo", "အမျိုးမှ အမျိုးသို့ ကူးသူ")
_n(1, "ekabījī", "မျိုးစေ့ တစ်စေ့သာ ရှိသူ")
_n(1, "sakadāgāmī", "သကဒါဂါမ်")
_n(1, "anāgāmī", "အနာဂါမ်")
_n(1, "antarāparinibbāyī", f"သက်တမ်း၏ အလယ်သို့ မရောက်မီ {PARI}")
_n(1, "upahaccaparinibbāyī", f"သက်တမ်း၏ အလယ်ကို ကျော်ပြီးမှ {PARI}")
_n(1, "asaṅkhāraparinibbāyī", f"တိုက်တွန်းမှု မရှိဘဲ {PARI}")
_n(1, "sasaṅkhāraparinibbāyī", f"{W['sasankharena']} {PARI}")
_n(1, "uddhaṃsoto akaniṭṭhagāmī", "အထက်သို့ စီးဆင်း၍ အကနိဋ္ဌ ဘုံသို့ ရောက်သူ", "uddhaṃsotoakaniṭṭhagāmī")
_n(1, "sotāpanno", "သောတာပန်")
_n(1, "sotāpattiphalasacchikiriyāya paṭipanno", f"{W['sotapattiphala']}ကို မျက်မှောက်ပြုရန် ကျင့်ကြံသူ")
_n(1, "sakadāgāmiphalasacchikiriyāya paṭipanno", f"{W['sakadagamiphala']}ကို မျက်မှောက်ပြုရန် ကျင့်ကြံသူ")
_n(1, "anāgāmiphalasacchikiriyāya paṭipanno", f"{W['anagamiphala']}ကို မျက်မှောက်ပြုရန် ကျင့်ကြံသူ")
_n(1, "arahā", W["araha"])
_n(1, "arahattaphalasacchikiriyāya paṭipanno", f"{W['arahattaphala']}ကို မျက်မှောက်ပြုရန် ကျင့်ကြံသူ")
# ---- (2) Duka
_n(2, "kodhano", "အမျက်ဒေါသ ထွက်တတ်သူ")
_n(2, "upanāhī", "ရန်ငြိုး သိုထားတတ်သူ")
_n(2, "makkhī", "ကျေးဇူး ချေဖျက်တတ်သူ")
_n(2, "paḷāsī", "တုပြိုင်တတ်သူ")
_n(2, "issukī", "ငြူစူတတ်သူ")
_n(2, "maccharī", "ဝန်တိုတတ်သူ")
_n(2, "saṭho", "စဉ်းလဲသူ")
_n(2, "māyāvī", "လှည့်စားတတ်သူ")
_n(2, "ahiriko", "ဒုစရိုက်ကို မရှက်သူ")
_n(2, "anottappī", "ဒုစရိုက်ကို မကြောက်ရွံ့သူ")
_n(2, "dubbaco", "သွန်သင်ချက်ကို နားမထောင်သူ")
_n(2, "pāpamitto", "မိတ်ဆွေဆိုးနှင့် ပေါင်းသင်းသူ")
_n(2, "indriyesu aguttadvāro", "အာရုံခံ အင်္ဂါတို့၏ တံခါးကို မစောင့်ထိန်းသူ")
_n(2, "bhojane amattaññū", "အစားအစာ၌ အတိုင်းအရှည်ကို မသိသူ")
_n(2, "muṭṭhassati", "သတိလစ်သူ")
_n(2, "asampajāno", "ကောင်းစွာ ဆင်ခြင်သိမြင်ခြင်း မရှိသူ")
_n(2, "sīlavipanno", "သီလ ပျက်စီးသူ")
_n(2, "diṭṭhivipanno", "အယူ ပျက်စီးသူ")
_n(2, "ajjhattasaṃyojano", "အတွင်းပိုင်း နှောင်ကြိုး ရှိသူ")
_n(2, "bahiddhāsaṃyojano", "အပြင်ပိုင်း နှောင်ကြိုး ရှိသူ")
_n(2, "akkodhano", "အမျက်ဒေါသ မထွက်တတ်သူ")
_n(2, "anupanāhī", "ရန်ငြိုး မသိုထားတတ်သူ")
_n(2, "amakkhī", "ကျေးဇူး မချေဖျက်တတ်သူ")
_n(2, "apaḷāsī", "မတုပြိုင်တတ်သူ")
_n(2, "anissukī", "မငြူစူတတ်သူ")
_n(2, "amaccharī", "ဝန်မတိုတတ်သူ")
_n(2, "asaṭho", "မစဉ်းလဲသူ")
_n(2, "amāyāvī", "မလှည့်စားတတ်သူ")
_n(2, "hirimā", "ဒုစရိုက်ကို ရှက်သူ")
_n(2, "ottappī", "ဒုစရိုက်ကို ကြောက်ရွံ့သူ")
_n(2, "suvaco", "သွန်သင်ချက်ကို နားထောင်သူ")
_n(2, "kalyāṇamitto", "မိတ်ဆွေကောင်းနှင့် ပေါင်းသင်းသူ")
_n(2, "indriyesu guttadvāro", "အာရုံခံ အင်္ဂါတို့၏ တံခါးကို စောင့်ထိန်းသူ")
_n(2, "bhojane mattaññū", "အစားအစာ၌ အတိုင်းအရှည်ကို သိသူ")
_n(2, "upaṭṭhitassati", "သတိ တည်နေသူ")
_n(2, "sampajāno", "ကောင်းစွာ ဆင်ခြင်သိမြင်ခြင်း ရှိသူ")
_n(2, "sīlasampanno", "သီလ ပြည့်စုံသူ")
_n(2, "diṭṭhisampanno", "အယူ ပြည့်စုံသူ")
_n(2, "hīnādhimutto", "ယုတ်ညံ့သည်၌ စိတ်ညွတ်သူ")
_n(2, "paṇītādhimutto", "မွန်မြတ်သည်၌ စိတ်ညွတ်သူ")
_n(2, "titto", "ရောင့်ရဲပြီးသူ")
_n(2, "tappetā", "အခြားသူကို ရောင့်ရဲစေသူ")
# ---- (3) Tika
_n(3, "nirāso", "မျှော်လင့်ချက် မရှိသူ")
_n(3, "āsaṃso", "မျှော်လင့်ချက် ရှိသူ")
_n(3, "vigatāso", "မျှော်လင့်ချက် ကင်းပြီးသူ")
_n(3, "gūthabhāṇī", "မစင်ကဲ့သို့ စကားပြောသူ")
_n(3, "pupphabhāṇī", "ပန်းကဲ့သို့ စကားပြောသူ")
_n(3, "madhubhāṇī", "ပျားရည်ကဲ့သို့ စကားပြောသူ")
_n(3, "arukūpamacitto", "အနာနှင့် တူသော စိတ် ရှိသူ")
_n(3, "vijjūpamacitto", "လျှပ်စီးနှင့် တူသော စိတ် ရှိသူ")
_n(3, "vajirūpamacitto", "စိန်နှင့် တူသော စိတ် ရှိသူ")
_n(3, "andho", "မျက်စိ ကန်းသူ")
_n(3, "ekacakkhu", "မျက်စိ တစ်ဖက် ရှိသူ")
_n(3, "dvicakkhu", "မျက်စိ နှစ်ဖက် ရှိသူ")
_n(3, "avakujjapañño", "မှောက်ထားသော အိုးနှင့် တူသော ပညာ ရှိသူ")
_n(3, "ucchaṅgapañño", "ပေါင်ခွင်နှင့် တူသော ပညာ ရှိသူ")
_n(3, "puthupañño", "ကျယ်ပြန့်သော ပညာ ရှိသူ")
_n(3, "kāmesu ca bhavesu ca avītarāgo", "ကာမတို့၌လည်း ဘဝတို့၌လည်း ရာဂ မကင်းသူ")
_n(3, "kāmesu vītarāgo, bhavesu avītarāgo", "ကာမတို့၌ ရာဂ ကင်း၍ ဘဝတို့၌ ရာဂ မကင်းသူ",
   "kāmesu vītarāgo bhavesu avītarāgo")
_n(3, "kāmesu ca bhavesu ca vītarāgo", "ကာမတို့၌လည်း ဘဝတို့၌လည်း ရာဂ ကင်းသူ")
_n(3, "pāsāṇalekhūpamo", "ကျောက်ပေါ်ရှိ အရေးအကြောင်းနှင့် တူသူ")
_n(3, "pathavilekhūpamo", "မြေပေါ်ရှိ အရေးအကြောင်းနှင့် တူသူ")
_n(3, "udakalekhūpamo", "ရေပေါ်ရှိ အရေးအကြောင်းနှင့် တူသူ")
_n(3, "suppameyyo", "ချိန်ဆရ လွယ်သူ")
_n(3, "duppameyyo", "ချိန်ဆရ ခက်သူ")
_n(3, "appameyyo", "ချိန်ဆ၍ မရနိုင်သူ")
SEV = "ပေါင်းသင်းအပ်"
BHAJ = "ဆည်းကပ်အပ်"
PAYIR = "ချဉ်းကပ် ခစားအပ်"
SEV3_NO = f"မ{SEV}{C} မ{BHAJ}{C} မ{PAYIR}"
SEV3 = f"{SEV}{C} {BHAJ}{C} {PAYIR}"
_n(3, "na sevitabbo na bhajitabbo na payirupāsitabbo", f"{SEV3_NO}သူ")
_n(3, "sevitabbo bhajitabbo payirupāsitabbo", f"{SEV3}သူ")
_n(3, "sakkatvā garuṃ katvā sevitabbo bhajitabbo payirupāsitabbo", f"ရိုသေ၍ လေးစားကာ {SEV3}သူ")
_n(3, "jigucchitabbo na sevitabbo na bhajitabbo na payirupāsitabbo", f"စက်ဆုပ်အပ်၍ {SEV3_NO}သူ")
_n(3, "ajjhupekkhitabbo na sevitabbo na bhajitabbo na payirupāsitabbo", f"လျစ်လျူရှုအပ်၍ {SEV3_NO}သူ")
SILA_FULL, SAM_FULL, PANNA_FULL = "သီလတို့ကို ပြည့်စုံစွာ ကျင့်", "သမာဓိကို ပြည့်စုံစွာ ကျင့်", "ပညာကို ပြည့်စုံစွာ ကျင့်"
PART = "တစ်စိတ်တစ်ပိုင်းသာ ကျင့်"
_n(3, "sīlesu paripūrakārī, samādhismiṃ mattaso kārī, paññāya mattaso kārī",
   f"{SILA_FULL}၍ သမာဓိကို {PART}{C} ပညာကို {PART}သူ")
_n(3, "sīlesu ca paripūrakārī, samādhismiñca paripūrakārī, paññāya mattaso kārī",
   f"သီလတို့ကိုလည်း ပြည့်စုံစွာ ကျင့်၍ သမာဓိကိုလည်း ပြည့်စုံစွာ ကျင့်{C} ပညာကို {PART}သူ")
_n(3, "sīlesu ca paripūrakārī, samādhismiñca paripūrakārī, paññāya ca paripūrakārī",
   f"သီလတို့ကိုလည်း ပြည့်စုံစွာ ကျင့်၍ သမာဓိကိုလည်း ပြည့်စုံစွာ ကျင့်{C} ပညာကိုလည်း ပြည့်စုံစွာ ကျင့်သူ")
# ---- (4) Catukka
_n(4, "asappuriso", "သူတော်ကောင်း မဟုတ်သူ")
_n(4, "asappurisena asappurisataro", "သူတော်ကောင်း မဟုတ်သူထက် ပို၍ သူတော်ကောင်း မဟုတ်သူ")
_n(4, "sappuriso", "သူတော်ကောင်း")
_n(4, "sappurisena sappurisataro", "သူတော်ကောင်းထက် ပို၍ သူတော်ကောင်း ဖြစ်သူ")
_n(4, "pāpo", "ယုတ်မာသူ")
_n(4, "pāpena pāpataro", "ယုတ်မာသူထက် ပို၍ ယုတ်မာသူ")
_n(4, "kalyāṇo", "ကောင်းမွန်သူ")
_n(4, "kalyāṇena kalyāṇataro", "ကောင်းမွန်သူထက် ပို၍ ကောင်းမွန်သူ")
_n(4, "pāpadhammo", "ယုတ်မာသော သဘော ရှိသူ")
_n(4, "pāpadhammena pāpadhammataro", "ယုတ်မာသော သဘော ရှိသူထက် ပို၍ ယုတ်မာသော သဘော ရှိသူ")
_n(4, "kalyāṇadhammo", "ကောင်းမွန်သော သဘော ရှိသူ")
_n(4, "kalyāṇadhammena kalyāṇadhammataro", "ကောင်းမွန်သော သဘော ရှိသူထက် ပို၍ ကောင်းမွန်သော သဘော ရှိသူ")
_n(4, "sāvajjo", "အပြစ် ရှိသူ")
_n(4, "vajjabahulo", "အပြစ် များသူ")
_n(4, "appavajjo", "အပြစ် နည်းသူ")
_n(4, "anavajjo", "အပြစ် မရှိသူ")
_n(4, "ugghaṭitaññū", "အကျဉ်းကို ကြားရုံဖြင့် သိသူ")
_n(4, "vipañcitaññū", "အကျယ် ရှင်းပြမှ သိသူ")
_n(4, "neyyo", "လမ်းညွှန် ပို့ဆောင်ရသူ")
_n(4, "padaparamo", "စကားလုံးသာ အများဆုံး ရသူ")
YUTTA, MUTTA = "သင့်လျော်သော ဉာဏ်ပေါ်မှု", "လျင်မြန်သော ဉာဏ်ပေါ်မှု"
_n(4, "yuttappaṭibhāno no muttappaṭibhāno", f"{YUTTA} ရှိ၍ {MUTTA} မရှိသူ", "yuttappaṭibhāno, no muttappaṭibhāno")
_n(4, "muttappaṭibhāno no yuttappaṭibhāno", f"{MUTTA} ရှိ၍ {YUTTA} မရှိသူ", "muttappaṭibhāno, no yuttappaṭibhāno")
_n(4, "yuttappaṭibhāno ca muttappaṭibhāno ca", f"{YUTTA}လည်း ရှိ၍ {MUTTA}လည်း ရှိသူ")
_n(4, "neva yuttappaṭibhāno no muttappaṭibhāno", f"{YUTTA}လည်း မရှိ{C} {MUTTA}လည်း မရှိသူ")
UTT, PUN = "ကြိုးစားအားထုတ်မှု၏ အကျိုးဖြင့်", "ကောင်းမှု၏ အကျိုးဖြင့်"
LIVE, NOLIVE = "အသက်မွေး", "အသက် မမွေး"              # upajīvī / no … upajīvī (no before an agent word = «မ», as pi-2)
_n(4, "uṭṭhānaphalūpajīvī no puññaphalūpajīvī", f"{UTT} {LIVE}၍ {PUN} {NOLIVE}သူ")
_n(4, "puññaphalūpajīvī no uṭṭhānaphalūpajīvī", f"{PUN} {LIVE}၍ {UTT} {NOLIVE}သူ")
_n(4, "uṭṭhānaphalūpajīvī ca puññaphalūpajīvī ca", f"{UTT}လည်း {LIVE}၍ {PUN}လည်း {LIVE}သူ")
_n(4, "neva uṭṭhānaphalūpajīvī no puññaphalūpajīvī", f"{UTT}လည်း {NOLIVE}{C} {PUN}လည်း {NOLIVE}သူ")
_n(4, "tamo tamaparāyano", "မှောင်မိုက်မှ မှောင်မိုက်သို့ ရှေးရှုသူ")
_n(4, "tamo jotiparāyano", "မှောင်မိုက်မှ အလင်းသို့ ရှေးရှုသူ")
_n(4, "joti tamaparāyano", "အလင်းမှ မှောင်မိုက်သို့ ရှေးရှုသူ")
_n(4, "joti jotiparāyano", "အလင်းမှ အလင်းသို့ ရှေးရှုသူ")
_n(4, "oṇatoṇato", "နိမ့်ရာမှ နိမ့်ရာသို့ ဆင်းသူ")
_n(4, "oṇatuṇṇato", "နိမ့်ရာမှ မြင့်ရာသို့ တက်သူ")
_n(4, "uṇṇatoṇato", "မြင့်ရာမှ နိမ့်ရာသို့ ဆင်းသူ")
_n(4, "uṇṇatuṇṇato", "မြင့်ရာမှ မြင့်ရာသို့ တက်သူ")
_n(4, "rūpappamāṇo rūpappasanno", "အဆင်းအရောင်ကို အတိုင်းအတာ ထား၍ အဆင်းအရောင်၌ ကြည်ညိုသူ",
   "rūpappamāṇo, rūpappasanno")
_n(4, "ghosappamāṇo ghosappasanno", "အသံဗလံကို အတိုင်းအတာ ထား၍ အသံဗလံ၌ ကြည်ညိုသူ",
   "ghosappamāṇo, ghosappasanno")
_n(4, "lūkhappamāṇo lūkhappasanno", "ကြမ်းတမ်းခြင်းကို အတိုင်းအတာ ထား၍ ကြမ်းတမ်းခြင်း၌ ကြည်ညိုသူ",
   "lūkhappamāṇo, lūkhappasanno")
_n(4, "dhammappamāṇo dhammappasanno", "တရားကို အတိုင်းအတာ ထား၍ တရား၌ ကြည်ညိုသူ",
   "dhammappamāṇo, dhammappasanno")
_n(4, "sarāgo", "ရာဂ ရှိသူ")
_n(4, "sadoso", "ဒေါသ ရှိသူ")
_n(4, "samoho", "မောဟ ရှိသူ")
_n(4, "samāno", "မာန ရှိသူ")
_n(4, "anusotagāmī", "ရေစီးအတိုင်း လိုက်သွားသူ")
_n(4, "paṭisotagāmī", "ရေစီးကို ဆန်၍ သွားသူ")
_n(4, "ṭhitatto", "တည်ငြိမ်သော စိတ် ရှိသူ")
_n(4, "tiṇṇo pāraṅgato thale tiṭṭhati brāhmaṇo",
   "ကူးမြောက်ပြီး ကမ်းတစ်ဖက်သို့ ရောက်၍ ကုန်းပေါ်၌ ရပ်တည်နေသော ပုဏ္ဏား")
SUTA = "အကြားအမြင်"
_n(4, "appassuto sutena anupapanno", f"{SUTA} နည်း၍ {SUTA}နှင့် မပြည့်စုံသူ")
_n(4, "appassuto sutena upapanno", f"{SUTA} နည်း၍ {SUTA}နှင့် ပြည့်စုံသူ")
_n(4, "bahussuto sutena anupapanno", f"{SUTA} များ၍ {SUTA}နှင့် မပြည့်စုံသူ")
_n(4, "bahussuto sutena upapanno", f"{SUTA} များ၍ {SUTA}နှင့် ပြည့်စုံသူ")
_n(4, "samaṇamacalo", "မတုန်လှုပ်သော ရဟန်း")
_n(4, "samaṇapadumo", "ကြာနီနှင့် တူသော ရဟန်း")
_n(4, "samaṇapuṇḍarīko", "ကြာဖြူနှင့် တူသော ရဟန်း")
_n(4, "samaṇesu samaṇasukhumālo", "ရဟန်းတို့အနက် နူးညံ့သိမ်မွေ့သော ရဟန်း")
# ---- (5) Pañcaka (the five of the item (2); the definitions in ch6 take them as questions)
_n(5, "datvā avajānāti", "ပေးပြီးနောက် အထင်သေးသူ")
_n(5, "saṃvāsena avajānāti", "အတူ နေခြင်းဖြင့် အထင်သေးသူ")
_n(5, "ādheyyamukho", "ကြားကာစကို ယုံလွယ်သူ")
_n(5, "lolo", "စိတ် မတည်ငြိမ်သူ")
_n(5, "mando momūho", "ထုံထိုင်း၍ အလွန် တွေဝေသူ")
# ---- (8) Aṭṭhaka
_n(8, "maggasamaṅgī", W["maggasamangi"])
_n(8, "phalasamaṅgī", W["phalasamangi"])

PLURAL.update({"asamayavimuttā": "asamayavimutto", "akuppadhammā": "akuppadhammo",
               "aparihānadhammā": "aparihānadhammo", "bhayūparatā": "bhayūparato",
               "abhabbāgamanā": "abhabbāgamano", "bhabbāgamanā": "bhabbāgamano", "niyatā": "niyato",
               "aniyatā": "aniyato", "paṭipannakā": "paṭipannako", "phale ṭhitā": "phaleṭhito",
               "ṭhitakappino": "ṭhitakappī", "ariyā": "ariyo", "anariyā": "anariyo", "sekkhā": "sekkho",
               "nevasekkhanāsekkhā": "nevasekkhanāsekkho"})


def key_of(p):
    """A Pāli name (any case of the first letter, mātikā spelling, plural) -> its NAME key, else None."""
    k = p[0].lower() + p[1:] if p else p
    k = ALIAS.get(k, k)
    k = PLURAL.get(k, k)
    return k if k in NAME else None


def name(p):
    k = key_of(p)
    if k is None:
        raise Miss("name: " + p)
    return NAME[k]


def adj(my):
    """A name before «puggalo»: «…သူ» -> «…သော ပုဂ္ဂိုလ်»; a noun name -> «… ပုဂ္ဂိုလ်»."""
    return my[:-2] + "သော " + PUGGALA if my.endswith("သူ") else f"{my} {PUGGALA}"


# group names «Tayo gilānūpamā puggalā» (plural noun phrases; members defined in the later chapters)
GROUP = {
    "gilānūpamā": "လူနာနှင့် တူသော",
    "potthakūpamā": "လျှော်ပိတ်စနှင့် တူသော",
    "kāsikavatthūpamā": "ကာသိ ပိတ်စနှင့် တူသော",
    "dhammakathikā": "တရား ဟောပြောသော",
    "valāhakūpamā": "မိုးတိမ်နှင့် တူသော",
    "mūsikūpamā": "ကြွက်နှင့် တူသော",
    "ambūpamā": "သရက်သီးနှင့် တူသော",
    "kumbhūpamā": "အိုးနှင့် တူသော",
    "udakarahadūpamā": "ရေကန်နှင့် တူသော",
    "balībaddūpamā": "နွားလားနှင့် တူသော",
    "āsīvisūpamā": "မြွေဆိုးနှင့် တူသော",
    "rukkhūpamā": "သစ်ပင်နှင့် တူသော",
    "yodhājīvūpamā": "စစ်သည်နှင့် တူသော",
    "udakūpamā": "ရေထဲရှိ လူနှင့် တူသော",
    "maggasamaṅgino": "မဂ်နှင့် ပြည့်စုံသော",
    "phalasamaṅgino": "ဖိုလ်နှင့် ပြည့်စုံသော",
}
witness("1", "^1-1305", "vijjūpamā", "လျှပ်စီးနှင့် တူသော")        # -ūpama = «Xနှင့် တူသော» (pi-1)
GROUP_POST = {   # «Dve puggalā dullabhā lokasmiṃ.» (the quality after «puggalā»)
    "dullabhā lokasmiṃ": "လောက၌ ရခဲသော",
    "duttappayā": "ရောင့်ရဲစေရန် ခက်ခဲသော",
    "sutappayā": "ရောင့်ရဲစေရန် လွယ်ကူသော",
}
GROUP_NOUN = {   # the five ascetic practices «Pañca piṇḍapātikā.» (no «puggalā»: the group word is a person noun)
    "piṇḍapātikā": "ဆွမ်းခံ၍သာ စားသူ",
    "khalupacchābhattikā": "နောက်မှ ကပ်သော ဆွမ်းကို မစားသူ",
    "ekāsanikā": "တစ်ထိုင်တည်းသာ စားသူ",
    "paṃsukūlikā": "ပံ့သကူ သင်္ကန်းကိုသာ ဝတ်သူ",
    "tecīvarikā": "သင်္ကန်း သုံးထည်သာ ဆောင်သူ",
    "āraññikā": "တော၌ နေသူ",
    "rukkhamūlikā": "သစ်ပင်ရင်း၌ နေသူ",
    "abbhokāsikā": "လွင်တီးခေါင်၌ နေသူ",
    "nesajjikā": "မလျောင်းဘဲ ထိုင်၍သာ နေသူ",
    "yathāsanthatikā": "ခင်းထားသည့်အတိုင်း နေရာ၌ နေသူ",
    "sosānikā": "သုသာန်၌ နေသူ",
}
witness("2", "^2-1027", "Avihānaṃ", "အဝိဟာ")

# ===================================================================================== mātikā predicates
PRED = {}        # «atthekacco puggalo PRED» whose Burmese is not «NAME ဖြစ်၏» -> Burmese clause (no end mark)
ATTHI = f"{W['ekacco']} {PUGGALA}သည်"         # atthekacco puggalo = «အချို့သော ပုဂ္ဂိုလ်သည်»
IDHA = f"{W['idhekacco']} {PUGGALA}သည်"        # idhekacco puggalo = «ဤလောက၌ အချို့သော ပုဂ္ဂိုလ်သည်»
COP = "ဖြစ်၏"


def pred_my(p):
    if p in PRED:
        return PRED[p]
    k = key_of(p)
    if k:
        return f"{NAME[k]} {COP}"
    raise Miss("predicate: " + p)


# ===================================================================================== definition frames
Q_RE = re.compile(r"Katamo ca puggalo (?P<n>.+)\?")
V_RE = re.compile(r'[Aa]yaṃ vuccati puggalo "(?P<n>[^"]+)"\.')
VP_RE = re.compile(r'[Ii]me vuccanti puggalā "(?P<n>[^"]+)"\.')
VUCCATI = f"ဤ{PUGGALA}ကို “{{}}”ဟု ခေါ်သည်{END}"
VUCCANTI = f"ဤ{PUG_PL}ကို “{{}}”ဟု ခေါ်သည်{END}"
Q_TAIL = f" ဟူသည် အဘယ် {PUGGALA}နည်း{END}"          # Katamo ca puggalo X? = «X ဟူသည် အဘယ် ပုဂ္ဂိုလ်နည်း။»


def q_my(m):
    n = m["n"]
    if key_of(n):
        return name(n) + Q_TAIL
    ws = n.split(" ")                      # two types in one question: «A B?» = «Aနှင့် B»
    for i in range(1, len(ws)):
        a, b = " ".join(ws[:i]), " ".join(ws[i:])
        if key_of(a) and key_of(b):
            return f"{name(a)}နှင့် {name(b)}" + Q_TAIL
    raise Miss("question name: " + n)


SENT = {}        # Pāli sentence (or clause before / after a dash) -> Burmese; «⟦n⟧» = n-th bracket
LINES = {}       # whole Pāli line -> Burmese (lines no rule builds)
EXTRA_RULES = []  # later chapters: (compiled regex on one unit, function(match) -> Burmese)

# ---- shared sentences of the definitions (ch2; also the later chapters)
SAMAPATTI = W["samapatti"]
SAMAP_PL = SAMAPATTI + "တို့"
_RUPA_SAHA = "သိမ်မွေ့သော ရုပ်ဘုံနှင့်အတူ ဖြစ်သော"       # rūpasahagata (rūpa = the fine-material sphere, pi-1 plane name)
_ARUPA_SAHA = "ရုပ်မရှိသော ဘုံနှင့်အတူ ဖြစ်သော"         # arūpasahagata (arūpa = the immaterial sphere «ရုပ်မရှိသော»)
SENT["Idhekacco puggalo lābhī hoti rūpasahagatānaṃ vā arūpasahagatānaṃ vā samāpattīnaṃ."] = (
    f"{IDHA} {_RUPA_SAHA} {SAMAP_PL}ကိုဖြစ်စေ{C} {_ARUPA_SAHA} {SAMAP_PL}ကိုဖြစ်စေ ရရှိသူ {COP}{END}")
_WISH = f"အလိုရှိရာ၌{C} အလိုရှိသည်ကို{C} အလိုရှိသမျှ"
SENT["So ca kho na nikāmalābhī hoti na akicchalābhī na akasiralābhī; na yatthicchakaṃ yadicchakaṃ "
     "yāvaticchakaṃ samāpajjatipi vuṭṭhātipi."] = (
    f"ထိုသူသည်ကား စိတ်တိုင်းကျ ရရှိသူ မဟုတ်{C} မခက်ခဲဘဲ ရရှိသူ မဟုတ်{C} မပင်ပန်းဘဲ ရရှိသူ မဟုတ်{C} "
    f"{_WISH} ဝင်စားသည်လည်း မဟုတ်{C} ထမြောက်သည်လည်း မဟုတ်{END}")
SENT["So ca kho nikāmalābhī hoti akicchalābhī akasiralābhī; yatthicchakaṃ yadicchakaṃ yāvaticchakaṃ "
     "samāpajjatipi vuṭṭhātipi."] = (
    f"ထိုသူသည်ကား စိတ်တိုင်းကျ ရရှိသူ{C} မခက်ခဲဘဲ ရရှိသူ{C} မပင်ပန်းဘဲ ရရှိသူ {COP}{C} "
    f"{_WISH} ဝင်စားလည်း ဝင်စား၏{C} ထမြောက်လည်း ထမြောက်၏{END}")
_KUPP = f"ထို{PUGGALA}၏ ထို{SAMAP_PL}သည် {W['pamada']}ကို မှီ၍ ပျက်ယွင်းကုန်ရာ၏"
_PARI = f"ထို{PUGGALA}သည် {W['pamada']}ကို မှီ၍ ထို{SAMAP_PL}မှ ဆုတ်ယုတ်ရာ၏"
_POSS = W["thanam"]                                   # «… ဟူသည်ကား ဖြစ်နိုင်သော အကြောင်း ရှိသည်»
_IMPOSS = W["atthanam"]                               # «… ဟူသည် မဖြစ်နိုင်သော အကြောင်း ဖြစ်သည်၊ အခွင့်အလမ်း မရှိ»
SENT["Ṭhānaṃ kho panetaṃ vijjati, yaṃ tassa puggalassa pamādamāgamma tā samāpattiyo kuppeyyuṃ"] = f"{_KUPP} {_POSS}"
SENT["Aṭṭhānametaṃ anavakāso yaṃ tassa puggalassa pamādamāgamma tā samāpattiyo kuppeyyuṃ"] = f"{_KUPP} {_IMPOSS}"
SENT["Ṭhānaṃ kho panetaṃ vijjati, yaṃ so puggalo pamādamāgamma tāhi samāpattīhi parihāyeyya"] = f"{_PARI} {_POSS}"
SENT["Aṭṭhānametaṃ anavakāso yaṃ so puggalo pamādamāgamma tāhi samāpattīhi parihāyeyya"] = f"{_PARI} {_IMPOSS}"
_ALL_ARIYA = f"{W['ariya']} {PUGGALA} အားလုံးသည် {W['ariya']} လွတ်မြောက်ခြင်း၌"     # sabbepi ariyapuggalā ariye vimokkhe
SENT["Sabbepi ariyapuggalā ariye vimokkhe asamayavimuttā."] = f"{_ALL_ARIYA} {NAME['asamayavimutto']} ဖြစ်ကြ၏{END}"
SENT["Sabbepi ariyapuggalā ariye vimokkhe akuppadhammā."] = f"{_ALL_ARIYA} {NAME['akuppadhammo']} ဖြစ်ကြ၏{END}"
SENT["Sabbepi ariyapuggalā ariye vimokkhe aparihānadhammā."] = f"{_ALL_ARIYA} {NAME['aparihānadhammo']} ဖြစ်ကြ၏{END}"
_FALL = f"ထို{SAMAP_PL}မှ ဆုတ်ယုတ်၏"
_NOFALL = f"ထို{SAMAP_PL}မှ မဆုတ်ယုတ်"
SENT["Sace anusañceteti, na parihāyati tāhi samāpattīhi."] = f"အကယ်၍ အဖန်ဖန် စေတနာ ထားလျှင် {_NOFALL}{END}"
SENT["Sace na anusañceteti, parihāyati tāhi samāpattīhi"] = f"အကယ်၍ အဖန်ဖန် စေတနာ မထားလျှင် {_FALL}"
SENT["Sace anurakkhati, na parihāyati tāhi samāpattīhi."] = f"အကယ်၍ စောင့်ရှောက်လျှင် {_NOFALL}{END}"
SENT["Sace na anurakkhati, parihāyati tāhi samāpattīhi"] = f"အကယ်၍ မစောင့်ရှောက်လျှင် {_FALL}"
# the eight deliverances and the taints
VIMOK = f"{W['vimokkha']}ကို ကိုယ်ဖြင့် ထိ၍ နေ၏"                           # aṭṭha vimokkhe kāyena phusitvā viharati
KALA = "အခါအားလျော်စွာ"                                                  # kālena kālaṃ
SAMAYA = "အချိန်အလိုက်"                                                  # samayena samayaṃ
ASAVA_ALL = f"ပညာဖြင့် မြင်၍ ထိုသူ၏ {W['asava']}တို့လည်း ကုန်ခန်းကုန်၏"     # paññāya cassa disvā āsavā parikkhīṇā honti
ASAVA_SOME = f"ပညာဖြင့် မြင်၍ ထိုသူ၏ {W['asava']} အချို့တို့လည်း ကုန်ခန်းကုန်၏"   # … ekacce āsavā …
SENT["Idhekacco puggalo aṭṭha vimokkhe kāyena phusitvā viharati; paññāya cassa disvā āsavā parikkhīṇā honti"] = (
    f"{IDHA} {VIMOK}{C} {ASAVA_ALL}")
SENT["Idhekacco puggalo na heva kho aṭṭha vimokkhe kāyena phusitvā viharati; paññāya cassa disvā āsavā "
     "parikkhīṇā honti."] = (
    f"{IDHA} {W['vimokkha']}ကို ကိုယ်ဖြင့် ထိ၍ နေသည်ကား မဟုတ်{C} {ASAVA_ALL}{END}")
SENT["Idhekacco puggalo aṭṭha vimokkhe kāyena phusitvā viharati; paññāya cassa disvā ekacce āsavā parikkhīṇā "
     "honti."] = f"{IDHA} {VIMOK}{C} {ASAVA_SOME}{END}"
# the four truths known, the teaching seen (diṭṭhippatto, saddhāvimutto)
_KNOW = W["yathabhutam_pajanati"] + "၏"
_TR = W["dukkha"].split(f"{C} ")
SENT['Idhekacco puggalo "idaṃ dukkha"nti yathābhūtaṃ pajānāti, "ayaṃ dukkhasamudayo"ti yathābhūtaṃ pajānāti, '
     '"ayaṃ dukkhanirodho"ti yathābhūtaṃ pajānāti, "ayaṃ dukkhanirodhagāminī paṭipadā"ti yathābhūtaṃ pajānāti.'] = (
    f"{IDHA} " + f"{C} ".join(f"“ဤသည်ကား {t}”ဟု {_KNOW}" for t in _TR) + END)
SENT["Tathāgatappaveditā cassa dhammā paññāya vodiṭṭhā honti vocaritā."] = (
    f"{W['tathagata']} ဟောကြားထားသော တရားတို့ကိုလည်း ထိုသူသည် ပညာဖြင့် ကောင်းစွာ မြင်ပြီး၊ ကောင်းစွာ "
    f"ဆင်ခြင်ပြီး {COP}{END}")
SENT["Paññāya cassa disvā ekacce āsavā parikkhīṇā honti"] = ASAVA_SOME
SENT["Paññāya cassa disvā ekacce āsavā parikkhīṇā honti, no ca kho yathā diṭṭhippattassa"] = (
    f"{ASAVA_SOME}{C} သို့သော် {NAME['diṭṭhippatto']}ကဲ့သို့ကား မဟုတ်")
# stream-entry and non-return (sattakkhattuparamo … uddhaṃsoto)
_PARIKKHAYA = "ကုန်ခန်းခြင်းကြောင့်"                       # parikkhayā (pi-2 «khayā = … ကုန်ခန်းခြင်းကြောင့်»)
STREAM = (f"{IDHA} {W['samyojana']} {_PARIKKHAYA} {NAME['sotāpanno']} {COP}{C} အပါယ်သို့ မကျတတ်သော သဘော ရှိသူ{C} "
          f"ကျိန်းသေသူ{C} အပြည့်အဝ သိမြင်ခြင်းသို့ ရှေးရှုသူ")
SENT["Idhekacco puggalo tiṇṇaṃ saṃyojanānaṃ parikkhayā sotāpanno hoti avinipātadhammo niyato "
     "sambodhiparāyano."] = f"{STREAM} {COP}{END}"
SENT["Idhekacco puggalo tiṇṇaṃ saṃyojanānaṃ parikkhayā sotāpanno hoti avinipātadhammo niyato "
     "sambodhiparāyano [sambodhiparāyaṇo (sī. ka.)]."] = f"{STREAM} ⟦0⟧ {COP}{END}"
_END_DUKKHA = "ဒုက္ခ၏ အဆုံးကို ပြု၏"                         # dukkhassantaṃ karoti (dukkha = the truth «ဒုက္ခ»)
_SAMS = "ကူးသွား ကျင်လည်ပြီး"                                # sandhāvitvā saṃsaritvā
ANAGAMI = (f"{IDHA} {W['orambhagiya']} {_PARIKKHAYA} {W['opapatika'][:-3]}သူ {COP}{C} ထိုဘုံ၌ပင် {PARI} ဖြစ်၍ "
           f"ထိုလောကမှ ပြန်မလာတတ်သော သဘော ရှိသူ {COP}")
SENT["Idhekacco puggalo pañcannaṃ orambhāgiyānaṃ saṃyojanānaṃ parikkhayā opapātiko hoti, tattha parinibbāyī "
     "anāvattidhammo tasmā lokā"] = ANAGAMI
SENT["Idhekacco puggalo pañcannaṃ orambhāgiyānaṃ saṃyojanānaṃ parikkhayā opapātiko hoti, tattha parinibbāyī "
     "anāvattidhammo tasmā lokā."] = ANAGAMI + END
UPARI_PAHANA = f"အထက်ပိုင်း နှောင်ကြိုးတို့ကို ပယ်ရန် {W['ariyamagga']}ကို ဖြစ်ပေါ်စေ၏"   # ariyamaggaṃ sañjaneti upari…
# the Buddhas (also the chakka mātikā)
ANANUSSUTA = "ယခင်က မကြားဖူးသော တရားတို့၌ သစ္စာတို့ကို ကိုယ်တိုင်"   # pubbe ananussutesu dhammesu sāmaṃ saccāni
ABHISAM = "အပြည့်အဝ သိမြင်၏"                                     # abhisambujjhati
ANABHISAM = "အပြည့်အဝ မသိမြင်"                                   # anabhisambujjhati
SABBANNU = "အလုံးစုံကို သိသော ဉာဏ်သို့"                             # sabbaññutaṃ
BALA_VASI = "စွမ်းအားတို့၌ နိုင်နင်းခြင်းသို့"                      # balesu vasībhāvaṃ
witness("1", "^1-M2-131", "paṭisaṅkhānabalañca", "စွမ်းအား")

# ===================================================================================== the engine
HEAD_RE = re.compile(r"(?P<h>#+) (?P<t>.+)$")
NUM_ITEM_RE = re.compile(r"\((?P<n>\d+)\) (?P<t>.+)$")
LIST_HEAD_RE = re.compile(r"(?P<n>Dve|Tayo|Cattāro|Pañca|Cha|Satta|Aṭṭha|Nava|Dasa) puggalā –")
GROUP_RE = re.compile(r"(?P<a>Aparepi )?(?P<n>Tayo|Cattāro|Pañca|Satta) (?P<g>\S+) puggalā\.")
GROUP_NOUN_RE = re.compile(r"Pañca (?P<g>\S+)\.")
DESIG_RE = re.compile(r"(?P<q>Kittāvatā \S+ \S+paññatti\?) (?P<y>Yāvatā .+)")
GROUP_POST_RE = re.compile(r"(?P<n>Dve) puggalā (?P<g>.+)\.")
SPLIT_RE = re.compile(r"( – |(?<=[.?])\s+(?=[A-ZĀĪŪṬḌṆÑṄṚ\"]))")
ATTH_SPLIT_RE = re.compile(r"([,;.]) (?=[Aa]tthekacco puggalo )")


def unit_my(u):
    for rx, fn in EXTRA_RULES:
        m = rx.fullmatch(u)
        if m:
            r = fn(m)
            if r is not None:
                return r
    m = Q_RE.fullmatch(u)
    if m:
        return q_my(m)
    m = V_RE.fullmatch(u)
    if m:
        return VUCCATI.format(name(m["n"]))
    m = VP_RE.fullmatch(u)
    if m:
        return VUCCANTI.format(name(m["n"]))
    m = KITTAVATA_RE.fullmatch(u)
    if m:
        return kittavata_my(m)
    m = YAVATA_RE.fullmatch(u)
    if m:
        return yavata_my(m)
    if u in SENT:
        return fill(SENT[u], u)
    raise Miss("sentence: " + u)


def units_my(body):
    out = []
    for part in SPLIT_RE.split(body):
        if not part:
            continue
        if part == " – ":
            out.append(" – ")
        elif part.isspace():
            out.append(" ")
        else:
            out.append(unit_my(part))
    return "".join(out)


def names_line_my(t):
    """«A, B, C.» / «A ca, B ca.» / «A puggalo, B puggalo.» (names, optional bracket after a name) -> Burmese."""
    end = t.endswith(".")
    s = t[:-1] if end else t
    ca = re.fullmatch(r"(.+?) ca, (.+?) ca", s)
    if ca:
        return f"{name(ca[1])}နှင့် {name(ca[2])}" + (END if end else "")
    out, rest = [], s
    keys = sorted(set(NAME) | set(ALIAS), key=len, reverse=True)
    while rest:
        for k in keys:
            if rest[:len(k)].lower() == k.lower() and (len(rest) == len(k) or rest[len(k)] in " ,"):
                my = name(k)
                rest = rest[len(k):]
                br = re.match(r" (\[[^\]]*\])", rest)
                if br:
                    rest = rest[br.end():]
                if rest.startswith(" puggalo"):
                    my, rest = adj(my), rest[len(" puggalo"):]
                if br:
                    my = f"{my} {var_my(br[1])}"
                out.append(my)
                if rest.startswith(", "):
                    rest = rest[2:]
                elif rest:
                    raise Miss("names line: " + t)
                break
        else:
            raise Miss("names line: " + t)
    return f"{C} ".join(out) + (END if end else "")


def atthekacco_my(t):
    """«Atthekacco puggalo P1, atthekacco puggalo P2; …» -> «အချို့သော ပုဂ္ဂိုလ်သည် P1၊ …»."""
    parts = ATTH_SPLIT_RE.split(t)
    out = []
    for i in range(0, len(parts), 2):
        seg = parts[i]
        sep = parts[i + 1] if i + 1 < len(parts) else ""
        if i + 1 >= len(parts):          # last part: its own final mark
            if seg.endswith("."):
                seg, sep = seg[:-1], "."
        m = re.fullmatch(r"[Aa]tthekacco puggalo (?P<p>.+)", seg)
        if not m:
            raise Miss("atthekacco: " + seg)
        out.append(f"{ATTHI} {fill(pred_my(m['p']), m['p'])}" + {",": C, ";": C, ".": END, "": ""}[sep])
    return " ".join(out)


def item_my(t):
    if t in LINES:
        return fill(LINES[t], t)
    m = GROUP_POST_RE.fullmatch(t)
    if m and m["g"] in GROUP_POST:
        return f"{GROUP_POST[m['g']]} {PUGGALA} {persons(NUM_PI[m['n'].lower()])}{END}"
    m = GROUP_RE.fullmatch(t)
    if m and m["g"] in GROUP:
        a = "နောက်ထပ် " if m["a"] else ""
        return f"{a}{GROUP[m['g']]} {PUGGALA} {persons(NUM_PI[m['n'].lower()])}{END}"
    m = GROUP_NOUN_RE.fullmatch(t)
    if m and m["g"] in GROUP_NOUN:
        return f"{GROUP_NOUN[m['g']]} {persons(5)}{END}"
    if re.match(r"[Aa]tthekacco puggalo ", t):
        return atthekacco_my(t)
    try:
        return names_line_my(t)
    except Miss:
        pass
    return units_my(t)


def line_my(body):
    if body in LINES:
        return fill(LINES[body], body)
    if body in FIXED:
        return FIXED[body]
    m = HEAD_RE.fullmatch(body)
    if m:
        if m["t"] not in HEAD:
            raise Miss("heading: " + body)
        return f"{m['h']} {HEAD[m['t']]}"
    if body.endswith(".") and body[:-1] in COLO:
        return COLO[body[:-1]] + END
    m = DESIG_RE.fullmatch(body)
    if m:
        return f"{unit_my(m['q'])} {yavata_my(YAVATA_RE.fullmatch(m['y']))}"
    m = LIST_HEAD_RE.fullmatch(body)
    if m:
        return f"{PUGGALA} {persons(NUM_PI[m['n'].lower()])} –"
    m = NUM_ITEM_RE.fullmatch(body)
    if m:
        return f"({m['n']}) {item_my(m['t'])}"
    return units_my(body)


def translate_line(line, bid=None):
    if not line.strip():
        return line
    m = ID_RE.search(line)
    body, tail = (line[:m.start()], line[m.start():]) if m else (line, "")
    return line_my(body.strip()) + tail
