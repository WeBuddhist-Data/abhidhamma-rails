"""Shared Burmese formulas for pi-6 (Yamaka, «အတွဲလိုက် မေးဖြေခြင်း»), plain audience.

Every pi-6 Burmese generator imports this module, so that identical Pāli gets identical Burmese, within pi-6 and with
the FINAL pi-1 … pi-5 Burmese (the rails texts). Writes no files at import (no bytecode either). It holds:
  * FINAL: an index of the rails texts of pi-1 … pi-5 aligned with their Pāli by block ID (read only; nothing in
    pi-1-my … pi-5-my is imported or written). heads() (whole lines, headings), items() (the lists «Head – a, b, c»)
    and witness() (a term: the Pāli must occur in the Pāli segment and the Burmese in its rails Burmese) READ or
    CHECK every reused value at import; WITNESS records them for the terms file and the reuse test;
  * the book frame, chapter names (yamaka_name()), labels (Ka) (Kha) …, answers, variant brackets, «…pe…»;
  * my_verb(): every Pāli verb of the pavattivāra (uppajjati, nirujjhati in three times, both polarities) in each
    Burmese form (statement, correlative clause, question, the «no ca … na V» double negative);
  * the person / place phrases (group_my(), place_my()) and the pavattivāra frames (question, «… no ca …»,
    «… X ca … Y ca …», short answer);
  * ch. 1 (Mūlayamaka): the four bases, the root predicates (pred()), the hetuvāra synonym list, the frames;
  * ch. 2 (Khandhayamaka) paṇṇattivāra: the khandha terms (pi-2 list) and the definition frames;
  * the headings (heading()) and colophons (COLO), and the engine translate_line() / translate_file().
A sentence that no frame or table matches raises Miss: nothing is guessed.
Later chapters: import this module, add their own terms with add_term() / add_subject() / PLACES / H / COLO entries
(never change an existing value without the user's approval) and put unique lines into LINES.
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


# ===================================================================================== FINAL: rails texts pi-1 … pi-5
ID_RE = re.compile(r" (\^[0-9A-Za-z-]+)\s*$")
BOOKS = {b: (ROOT / f"AI_translation/pali/pi-{b}_split_chapters",
             ROOT / f"AI_translation/burmese/pi-{b}-burmese-plain-rails_split_chapters") for b in "12345"}


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


def witness(book, bid, pali, my, key=None):
    """A value read from a rails segment: the Pāli must occur in its Pāli, the Burmese in its Burmese."""
    f, p, m = FINAL.seg(book, bid)
    if pali.lower() not in " ".join(p).lower() or my not in " ".join(m):
        raise Miss(f"witness pi-{book} {bid}: «{pali}» / «{my}» not in the segment")
    WITNESS.setdefault(key or pali, (book, bid, my))
    return my


def heads(pali):
    """A heading or whole line «Pāli» of pi-1 … pi-5 -> its final Burmese (all occurrences must agree)."""
    found = {}
    for b, k, f, p, m in FINAL.lines():
        pt = re.sub(r"^#+ ", "", strip_id(p)).strip()
        mt = re.sub(r"^#+ ", "", strip_id(m)).strip()
        if pt == pali:
            found.setdefault(mt, (b, k))
    if len(found) != 1:
        raise Miss(f"heads {pali}: {len(found)} renderings {list(found)[:3]}")
    my, (b, k) = next(iter(found.items()))
    WITNESS.setdefault(pali, (b, k, my))
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


W = witness

# ===================================================================================== basics and book frame
C = "၊"                               # clause / list break
END = "။"                             # end of a statement or question
PE = "…"                              # …pe… / …Pe… (one «…»)
NAMO = heads("Namo tassa bhagavato arahato sammāsambuddhassa")
ABHI = heads("Abhidhammapiṭake")      # «အဘိဓမ္မာပိဋကတွင်»
TITLE = "အတွဲလိုက် မေးဖြေခြင်း"         # Yamakapāḷi (book title, Burmese only): "question and answer in pairs"
YAMAKA = "ကို အတွဲလိုက် မေးဖြေခြင်း"      # -yamaka(ṃ) of a chapter: «Xများကို အတွဲလိုက် မေးဖြေခြင်း»


def quoted(s):
    return f"“{s}”"


def finished(name):
    """«X niṭṭhito / niṭṭhitā.» = «“X” ပြီးဆုံးပြီ။» (pi-1 … pi-5 colophons)."""
    return f"{quoted(name)} ပြီးဆုံးပြီ{END}"


W("2", "^2-153", "Khandhavibhaṅgo niṭṭhito", "“အစုအဝေးများကို ခွဲခြမ်းစိတ်ဖြာခြင်း” ပြီးဆုံးပြီ။", key="X niṭṭhito.")

# --- labels (Ka) (Kha) … ---------------------------------------------------------------------------------------------
AKKHARA = {"Ka": "က", "Kha": "ခ", "Ga": "ဂ", "Gha": "ဃ", "Ṅa": "င", "Ca": "စ", "Cha": "ဆ", "Ja": "ဇ", "Jha": "ဈ",
           "Ña": "ည", "Ṭa": "ဋ", "Ṭha": "ဌ", "Ḍa": "ဍ", "Ḍha": "ဎ", "Ṇa": "ဏ", "Ta": "တ", "Tha": "ထ", "Da": "ဒ",
           "Dha": "ဓ", "Na": "န", "Pa": "ပ", "Pha": "ဖ", "Ba": "ဗ", "Bha": "ဘ", "Ma": "မ"}
LABEL_RE = re.compile(r"^\((" + "|".join(sorted(AKKHARA, key=len, reverse=True)) + r")\) ")
W("1", "^1-M1-1", "(Ka) kusalā dhammā", "(က) ကုသိုလ် သဘောတရားများ", key="(Ka)")
W("2", "^2-793", "(Gha)", "(ဃ)", key="(Gha)")


def label(ka):
    return f"({AKKHARA[ka]})"


# --- answers ---------------------------------------------------------------------------------------------------------
YES = W("5", "^5-1", "Āmantā", "ဟုတ်ပါသည်") + END          # Āmantā.
NATTHI = "မရှိပါ" + END       # Natthi. (there is no such person / case): the polite answer register of Āmantā / No
#                                (coordinator 2026-11-22; pi-5 Natthi «မရှိပါ။» ^5-355; pi-3 «မရှိ။» = explained exception)
W("5", "^5-355", "? Natthi.", "မရှိပါ။", key="Natthi.")
NO = "မဟုတ်ပါ" + END                                          # No. (proposal for later chapters; not in the sample)
ANSWERS = {"Āmantā.": YES, "Natthi.": NATTHI, "No.": NO}

# --- variant brackets ------------------------------------------------------------------------------------------------
SIGLA = {"sī.": "Sī.", "syā.": "Syā.", "ka.": "Ka.", "kaṃ.": "Kaṃ.", "pī.": "Pī.", "ma.": "Ma.", "?": "(မသေချာ)"}
EVAM_UPARI = "နောက်တွင်လည်း ဤနည်းတူ"     # evamuparipi (pi-2 ^2-718; pi-2 ^2-568 has «အောက်တွင်လည်း ဤနည်းအတိုင်း»)
W("2", "^2-718", "evamuparipi", EVAM_UPARI)
VAR_P = "ပါဌ်ကွဲ"                          # a word differs
VAR_L = "စာလုံးပေါင်းကွဲ"                   # spelling only
SPELLING = set()                         # variant readings that differ in spelling only (Pāli inner text); later chapters add


def variant(inner):
    """'reading (sī. syā.) evamuparipi' (inside the brackets) -> '[ပါဌ်ကွဲ (Sī., Syā.): reading၊ နောက်တွင်လည်း ဤနည်းတူ]'."""
    m = re.fullmatch(r"(.*?) \(([^)]*)\)( evamuparipi)?", inner.strip())
    if not m:
        raise Miss("variant: " + inner)
    reading, sig, up = m.groups()
    sig = ", ".join(SIGLA[s] for s in sig.split())
    lab = VAR_L if inner in SPELLING else VAR_P
    return f"[{lab} ({sig}): {reading}" + (f"{C} {EVAM_UPARI}" if up else "") + "]"


# ===================================================================================== verbs (pavattivāra)
VERB = {"uppajj": "ဖြစ်ပေါ်",            # uppajjati (pi-2 / pi-5 termbase)
        "nirujjh": "ချုပ်ငြိမ်း"}         # nirujjhati (pi-2 / pi-5 termbase)
W("2", "^2-204", "nirujjhamānā nirujjhati", "ချုပ်ငြိမ်းလျှင် ချုပ်ငြိမ်းသည်", key="nirujjhati")
W("2", "^2-203", "uppajjamānā uppajjati", "ဖြစ်ပေါ်လျှင် ဖြစ်ပေါ်သည်", key="uppajjati")
TENSE_MY = {"pres": "", "past": "ခဲ့", "fut": "လိမ့်မည်"}      # uppajjati / uppajjittha / uppajjissati
NEG = "မ"                                                     # every negative verb: «မ» + verb (+ tense)
BUT = "သို့သော်"                                               # no ca / na ca
NOT_SO = "ကား မဟုတ်"                                          # «no ca … na V»: «… မVသည်ကား မဟုတ်» (it is not that … not V)


def my_verb(root, tense, neg=False, form="stmt", pl=False):
    """root 'uppajj' / 'nirujjh'; tense 'pres' / 'past' / 'fut'; form:
    'stmt' (finite statement: ဖြစ်ပေါ်သည် / ဖြစ်ပေါ်ခဲ့သည် / ဖြစ်ပေါ်လိမ့်မည်; neg မဖြစ်ပေါ် / မဖြစ်ပေါ်ခဲ့ / မဖြစ်ပေါ်လိမ့်မည်),
    'cl' (first clause of a yassa / yattha question: ဖြစ်ပေါ်၏ / ဖြစ်ပေါ်ခဲ့၏ / ဖြစ်ပေါ်လိမ့်မည်; neg as stmt),
    'q' (question: ဖြစ်ပေါ်သလော / ဖြစ်ပေါ်ခဲ့သလော / ဖြစ်ပေါ်လိမ့်မည်လော; neg မဖြစ်ပေါ်သလော …),
    'attr' (relative: ဖြစ်ပေါ်သော / ဖြစ်ပေါ်ခဲ့သော / ဖြစ်ပေါ်မည့်; neg မ…).
    pl adds «ကြ» (plural subject)."""
    fut = tense == "fut"
    ko_ = "ကြ" if pl else ""
    v = (NEG if neg else "") + VERB[root] + ((ko_ + TENSE_MY[tense]) if fut else (TENSE_MY[tense] + ko_))
    if form == "stmt":
        return v if (neg or fut) else v + "သည်"
    if form == "cl":
        return v if (neg or fut) else v + "၏"
    if form == "q":
        return v + ("လော" if fut else "သလော")
    if form == "attr":
        return (v[:-len("လိမ့်မည်")] + "မည့်") if fut else v + "သော"
    raise ValueError(form)


def not_so(root, tense):
    """the double negative «no ca … nuppajjati»: «မဖြစ်ပေါ်သည်ကား မဟုတ်» / «မဖြစ်ပေါ်ခဲ့သည်ကား မဟုတ်» /
    «မဖြစ်ပေါ်လိမ့်မည်ကား မဟုတ်»."""
    v = my_verb(root, tense, True)
    return v + ("" if tense == "fut" else "သည်") + NOT_SO


_PALI_END = [("issanti", "fut"), ("issati", "fut"), ("ittha", "past"), ("attha", "past"),
             ("anti", "pres"), ("ati", "pres")]


def pali_verb(w):
    """'uppajjati' / 'nuppajjitthāti' / 'na nirujjhissatīti' … -> (root, tense, neg).
    'nirujjhattha' (a source slip for nirujjhittha, ^6-2-111) is read as past."""
    w = w.strip()
    neg = False
    if w.lower().startswith("na "):
        neg, w = True, w[3:]
    w = w[0].lower() + w[1:]
    w = re.sub(r"īti$", "i", w)
    w = re.sub(r"āti$", "a", w)
    if w.startswith("nuppajj"):
        neg, w = True, w[1:]
    for root in VERB:
        if w.startswith(root):
            rest = w[len(root):]
            for end, tense in _PALI_END:
                if rest == end:
                    return root, tense, neg
    raise Miss("pali_verb: " + w)


VB = r"(?:[Nn]a )?(?:[Nn]?[Uu]ppajj|[Nn]irujjh)\w*"            # one Pāli pavatti verb

# ===================================================================================== subjects (khandha names etc.)
KHANDHA_H, KHANDHA = items("2", "^2-1")    # «အစုအဝေး ငါးပါး», {rūpakkhandho: «ရုပ် အစုအဝေး», …}
SUBJ = dict(KHANDHA)                       # subject terms of the pavattivāra: Pāli nominative -> Burmese


def add_subject(pali, my):
    """Later chapters: add a pavattivāra subject (Pāli nominative singular / plural as in the text)."""
    if pali in SUBJ and SUBJ[pali] != my:
        raise Miss(f"add_subject {pali}: already «{SUBJ[pali]}»")
    SUBJ[pali] = my


def subj(tok):
    if tok not in SUBJ:
        raise Miss("subject: " + tok)
    return SUBJ[tok]


# ===================================================================================== persons and places
SATTA_ASANNA = W("2", "^2-18-4-3-0", "Asaññasattā", "အသညသတ်")      # the being without perception (pi-2)
W("2", "^2-234", "pañcavokārabhavo", "အစုအဝေး ငါးပါး ရှိသော ဘဝ")
W("2", "^2-234", "catuvokārabhavo", "အစုအဝေး လေးပါး ရှိသော ဘဝ")
W("2", "^2-234", "arūpabhavo", "ရုပ်မရှိသော ဘုံ")
# place key -> Burmese place noun; the case words: ၌ (in: acc. «upapajjantānaṃ», loc.), မှ (from: abl. «cavantānaṃ»)
PLACES = {
    "asaññasatta": f"{SATTA_ASANNA} ဘုံ",
    "pañcavokāra": "အစုအဝေး ငါးပါး ရှိသော ဘဝ",
    "catuvokāra": "အစုအဝေး လေးပါး ရှိသော ဘဝ",
    "ekavokāra": "အစုအဝေး တစ်ပါး ရှိသော ဘဝ",
    "arūpa": "ရုပ်မရှိသော ဘုံ",
    "suddhāvāsa": "သုဒ္ဓါဝါသ ဘုံ",          # proper name kept as a name (style rule; NEW)
}
W("2", "^2-234", "ekavokārabhavo", PLACES["ekavokāra"])
BEINGS_NAME = {"asaññasatta": f"{SATTA_ASANNA}တို့"}   # asaññasattānaṃ: «အသညသတ်တို့» (pi-2 «အသညသတ် နတ်တို့»)
_CASES = {"aṃ": "acc", "e": "loc", "ā": "abl", "ānaṃ": "gen"}
LOC, ABL = "၌", "မှ"
THEM = "သူတို့"                            # the persons (gen. pl. participles)
ALL_OF = "သူ အားလုံးတို့"                   # sabbesaṃ + participle
OTHERS = "အခြားသူတို့"                     # itaresaṃ (NEW)
HAS = "ရှိ"                               # beings of a place: «X၌ ရှိသူတို့»
# participle (gen. pl.) -> (Burmese verb with «ဆဲ», case word of its place)
PART = {
    "upapajjantānaṃ": (W("2", "^2-1017", "upapattikkhaṇe", "ပြန်လည် ဖြစ်ပေါ်") + "ဆဲ", LOC),   # upapajjati (pi-2 / pi-5)
    "cavantānaṃ": (W("2", "^2-1029", "cavanti", "စုတေ") + "ဆဲ", ABL),                     # cavati (pi-5 termbase)
    "parinibbantānaṃ": (W("4", "^4-M-7", "parinibbāyī", "ပရိနိဗ္ဗာန် ပြု") + "ဆဲ", LOC),     # parinibbāyati (pi-5)
}
PACCHIMA = "နောက်ဆုံး ဘဝ ရှိ"               # pacchimabhavika (NEW): «နောက်ဆုံး ဘဝ ရှိသူတို့»
W("4", "^4-184", "cavamāne upapajjamāne", "သေဆဲ၊ ဖြစ်ပေါ်ဆဲ", key="-anta / -amāna (participle «…ဆဲ»)")
GROUP_ATOMS = {     # whole phrases that are not built from the parts above (later chapters add)
    "ye arūpaṃ upapajjitvā parinibbāyissanti":
        f"{PLACES['arūpa']}{LOC} ပြန်လည် ဖြစ်ပေါ်ပြီး ပရိနိဗ္ဗာန် ပြုမည့်{THEM}",
}
AND = "နှင့်"


def _place_form(w):
    w = w.lower()
    for key in PLACES:
        for end, case in _CASES.items():
            if w == key[:-1] + end:
                return key, case
    return None


def _join_places(keys):
    """['catuvokāra', 'pañcavokāra'] -> «အစုအဝေး လေးပါး ရှိသော ဘဝနှင့် အစုအဝေး ငါးပါး ရှိသော ဘဝ»."""
    return (AND + " ").join(PLACES[k] for k in keys)


def _one_group(toks):
    """Consume one person group from the token list; return its Burmese («… သူတို့»)."""
    allf = othf = False
    if toks[0].lower() == "sabbesaṃ":
        allf = True
        toks.pop(0)
    if toks and toks[0].lower() == "itaresaṃ":
        othf = True
        toks.pop(0)
        if not toks:
            return OTHERS
    places, case = [], None
    while toks and _place_form(toks[0]):
        k, c = _place_form(toks[0])
        if places and c != case:
            break
        if places and c == "gen" and (k in BEINGS_NAME or places[-1] in BEINGS_NAME):
            break
        places.append(k)
        case = c
        toks.pop(0)
    if case == "gen" and not (toks and toks[0].lower() in PART):
        if len(places) == 1 and places[0] in BEINGS_NAME and not othf:
            return BEINGS_NAME[places[0]]
        loc = _join_places(places) + LOC
        return f"{loc} ရှိသော {OTHERS}" if othf else f"{loc} {HAS}{THEM}"
    if not toks:
        raise Miss("person group: no head")
    head = toks.pop(0).lower()
    if head == "pacchimabhavikānaṃ":
        # «pacchimabhavikānaṃ [place-acc …] upapajjantānaṃ» = those of the last existence being reborn (in …)
        j, pl2 = 0, []
        while j < len(toks) and _place_form(toks[j]) and _place_form(toks[j])[1] == "acc":
            pl2.append(_place_form(toks[j])[0])
            j += 1
        if j < len(toks) and toks[j].lower() == "upapajjantānaṃ":
            del toks[:j + 1]
            loc = (_join_places(pl2) + LOC + " ") if pl2 else ""
            return f"{loc}{PART['upapajjantānaṃ'][0]} {PACCHIMA}{THEM}"
        loc = (_join_places(places) + LOC + " ") if places else ""
        return f"{loc}{PACCHIMA}{THEM}"
    if head not in PART:
        raise Miss("person head: " + head)
    verb, cw = PART[head]
    loc = (_join_places(places) + cw + " ") if places else ""
    if othf:
        return f"{loc}{verb} {OTHERS}"
    return f"{loc}{verb}{ALL_OF if allf else THEM}"


def group_my(g):
    """Pāli person groups (before «tesaṃ») -> Burmese, groups joined «A နှင့် B» / «A၊ B နှင့် C»."""
    g = g.strip()
    if g.lower() in GROUP_ATOMS:
        return GROUP_ATOMS[g.lower()]
    toks = g.replace(",", "").split()
    parts = []
    while toks:
        parts.append(_one_group(toks))
    if len(parts) == 1:
        return parts[0]
    return f"{C} ".join(parts[:-1]) + f"{AND} " + parts[-1]


def place_my(g):
    """'Asaññasatte' / 'Pañcavokāre' (bare place before «tattha») -> «… ဘုံ၌»."""
    keys = []
    for w in g.split():
        f = _place_form(w)
        if not f or f[1] != "loc":
            raise Miss("place: " + g)
        keys.append(f[0])
    return _join_places(keys) + LOC


# ===================================================================================== pavattivāra frames
VA_PANA = "တစ်ဖန်"                       # (Kha) … vā pana …: «တစ်ဖန် …» (pi-5 «No ce pana» «တစ်ဖန် …»)
CL = {"yassa": ("အကြင်သူအား", "ထိုသူအား"),            # yassa … tassa (pi-2 ^2-199 «အကြင်သူအား»)
      "yattha": ("အကြင်နေရာ၌", "ထိုနေရာ၌"),            # yattha … tattha (okāsa «နေရာ»)
      "yassa yattha": ("အကြင်သူအား အကြင်နေရာ၌", "ထိုသူအား ထိုနေရာ၌")}
W("2", "^2-199", "Idha yassa te honti", "အကြင်သူအား", key="yassa")
W("4", "^4-M-11", "okās", "နေရာ", key="okāsa")
FT = {"tassa": "ထိုသူအား", "tattha": "ထိုနေရာ၌", "tassa tattha": "ထိုသူအား ထိုနေရာ၌"}
PRO = {"tesaṃ": "ထိုသူတို့အား", "tesaṃ tattha": "ထိုသူတို့အား ထိုနေရာ၌", "tattha": "ထိုနေရာ၌"}
DAT = "အား"
CLR = r"(?P<cl>[Yy]assa vā pana yattha|[Yy]assa yattha|[Yy]assa vā pana|[Yy]attha vā pana|[Yy]assa|[Yy]attha)"
PROR = r"(?:tesaṃ tattha|tattha|tesaṃ)"
Q_PAV = re.compile(rf"^{CLR} (?P<x>\S+) (?P<v1>{VB}) (?P<ft>tassa tattha|tassa|tattha) (?P<y>\S+) (?P<v2>{VB})[?.]$")
A_BUT = re.compile(rf"^(?P<who>.+?) (?P<pro>{PROR}) (?P<x>\S+) (?P<v1>{VB}), no ca (?P<pro2>{PROR}) (?P<y>\S+) "
                   rf"(?P<v2>{VB})\.$")
A_BOTH = re.compile(rf"^(?P<who>.+?) (?P<pro>{PROR}) (?P<x>\S+) ca (?P<v1>{VB}) (?P<y>\S+) ca (?P<v2>{VB})\.$")
A_SHORT = re.compile(rf"^(?P<v>{VB})\.$")


def V(pali_w, form="stmt"):
    root, tense, neg = pali_verb(pali_w)
    return my_verb(root, tense, neg, form)


def q_pavatti(cl, x, v1, ft, y, v2):
    """yassa X uppajjati tassa Y uppajjatīti? -> «အကြင်သူအား X ဖြစ်ပေါ်၏၊ ထိုသူအား Y ဖြစ်ပေါ်သလော။»"""
    c = cl.lower()
    pre = ""
    if " vā pana" in c:
        pre = VA_PANA + " "
        c = c.replace(" vā pana", "")
    return f"{pre}{CL[c][0]} {subj(x)} {V(v1, 'cl')}{C} {FT[ft]} {subj(y)} {V(v2, 'q')}{END}"


def who_my(who, pro):
    var = re.findall(r" ?(⟦\d+⟧)", who)              # a variant bracket inside the group: after «…အား»
    who = re.sub(r" ?⟦\d+⟧", "", who)
    if pro == "tattha":
        out = place_my(who)
    else:
        out = group_my(who) + DAT
    out += "".join(" " + v for v in var)
    return out + (" " + FT["tattha"] if pro == "tesaṃ tattha" else "")


def a_but(who, pro, x, v1, pro2, y, v2):
    """… tesaṃ X uppajjati, no ca tesaṃ Y uppajjati. -> «…အား X ဖြစ်ပေါ်သည်၊ သို့သော် ထိုသူတို့အား Y မဖြစ်ပေါ်။»;
    a negative second verb («no ca … nuppajjati») -> «… Y မဖြစ်ပေါ်သည်ကား မဟုတ်။»"""
    root2, tense2, neg2 = pali_verb(v2)
    v2m = not_so(root2, tense2) if neg2 else my_verb(root2, tense2, True)
    return f"{who_my(who, pro)} {subj(x)} {V(v1)}{C} {BUT} {PRO[pro2]} {subj(y)} {v2m}{END}"


def a_both(who, pro, x, v1, y, v2):
    """… tesaṃ X ca uppajjati Y ca uppajjati. -> «…အား Xလည်း ဖြစ်ပေါ်သည်၊ Yလည်း ဖြစ်ပေါ်သည်။»"""
    return f"{who_my(who, pro)} {subj(x)}လည်း {V(v1)}{C} {subj(y)}လည်း {V(v2)}{END}"


def pavatti_sentence(s):
    if s in ANSWERS:
        return ANSWERS[s]
    m = Q_PAV.match(s)
    if m:
        return q_pavatti(m["cl"], m["x"], m["v1"], m["ft"], m["y"], m["v2"])
    m = A_BUT.match(s)
    if m:
        return a_but(m["who"], m["pro"], m["x"], m["v1"], m["pro2"], m["y"], m["v2"])
    m = A_BOTH.match(s)
    if m:
        return a_both(m["who"], m["pro"], m["x"], m["v1"], m["y"], m["v2"])
    m = A_SHORT.match(s)
    if m:
        return V(m["v"]) + END             # Uppajjati. = «ဖြစ်ပေါ်သည်။» (the question's Y)
    return None


# ===================================================================================== ch. 1 (Mūlayamaka)
DHAMMA = "သဘောတရား"
DHAMMA_PL = DHAMMA + "များ"
ABY = W("1", "^1-M1-1", "abyākatā dhammā", "ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော")
W("1", "^1-M1-1", "akusalā dhammā", "အကုသိုလ် သဘောတရားများ")
W("1", "^1-M2-109", "nāmañca", "စိတ်ပိုင်း", key="nāma")
# base -> (before «သဘောတရား», genitive before a root word, as a noun (kusalaṃ, nāmaṃ …))
BASE = {"kusala": ("ကုသိုလ်", "ကုသိုလ်၏", "ကုသိုလ်"),
        "akusala": ("အကုသိုလ်", "အကုသိုလ်၏", "အကုသိုလ်"),
        "abyākata": (ABY, ABY, f"{ABY} {DHAMMA}"),        # adjectival, as pi-1 abyākatahetu «… မဟုတ်သော အမြစ်»
        "nāma": ("စိတ်ပိုင်း", "စိတ်ပိုင်း၏", "စိတ်ပိုင်း")}
MULA = "အမြစ်"                             # mūla (pi-1 kusalamūla «ကုသိုလ်၏ အမြစ်», pi-2 akusalamūla)
W("1", "^1-32", "alobho kusalamūlaṃ", "ကုသိုလ်၏ အမြစ်", key="kusalamūla")
W("1", "^1-389", "akusalamūl", "အကုသိုလ်၏ အမြစ်", key="akusalamūla")
MULAMULA = f"{MULA}၏ {MULA}"                # mūlamūla (NEW): «အမြစ်၏ အမြစ်»
EKA = "တူညီသော"                            # eka- in ekamūla «တူညီသော အမြစ်» (the same root) (NEW)
ANNA = W("1", "^1-1083", "aññamañña", "အချင်းချင်း")      # aññamañña (pi-1 / pi-5)
KA_VERB = "အခြေခံ"                          # -mūlaka «… ကို အခြေခံ» (based on) (NEW)
HAVE, BE = "ရှိ", "ဖြစ်"
NEGV = {BE: "မဟုတ်", HAVE: "မရှိ", KA_VERB: "မအခြေခံ"}
AHETUKA = W("1", "^1-M2-2", "ahetukā dhammā", "အမြစ် မရှိသော")      # ahetuka / sahetuka (pi-1 Mātikā)
SAHETUKA = W("1", "^1-M2-2", "sahetukā dhammā", "အမြစ် ရှိသော")
SAMUTTHANA = W("1", "^1-M2-60", "cittasamuṭṭhān", "မှ ဖြစ်ပေါ်လာသော", key="samuṭṭhāna")   # «ကုသိုလ်မှ ဖြစ်ပေါ်လာသော ရုပ်»
SAHAJATA = W("5", "^5-473", "sahajātā", "နှင့်အတူ ပေါ်ပေါက်သော")         # «ကုသိုလ်၏ အမြစ်နှင့်အတူ ပေါ်ပေါက်သော»
EKATO = W("1", "^1-1447", "ekato", "တစ်ပြိုင်နက်")
AVASESA = W("2", "^2-796", "avasesā paññā", "ကြွင်းကျန်သော")
AVASESA_N = f"{AVASESA} အရာများ"            # bare avasesā (the remaining things)
THAPETVA = W("2", "^2-796", "ṭhapetvā", "ချန်ထား၍")
RUPA_W = "ရုပ်"
NUM = {"Tīṇeva": "သုံး", "Tayo eva": "သုံး", "Naveva": "ကိုး"}
ONLY = "ပါးသာ ရှိသည်"                       # «X သုံးပါးသာ ရှိသည်» (only three X)
ALL = "ထိုအားလုံးတို့သည်"                   # sabbe te
WHATEVER = "မည်သည်တို့မဆို"                # ye keci / ye vā pana (pi-5 «… မည်သူမဆို၊ ထိုသူ အားလုံးတို့သည်»)
THING = "အရာ"
W("5", "^5-334", "Ye keci dukkhanti vācaṃ bhāsanti, sabbe te", "မည်သူမဆို၊ ထိုသူ အားလုံးတို့သည်", key="ye keci …, sabbe te …")
ARISE_TOGETHER = f"{EKATO} {my_verb('uppajj', 'pres', form='attr', pl=True)}"   # ekato uppajjanti (relative)


class Pred:
    """A root predicate: obj (the Burmese words before the verb) + verb (ဖြစ် / ရှိ / အခြေခံ)."""

    def __init__(self, obj, verb, plural_noun=False):
        self.obj, self.verb, self.pn = obj, verb, plural_noun

    def _o(self, pl):
        return self.obj + ("များ" if pl and self.pn else "")

    def q(self, pl=True):
        return f"{self._o(pl)} {self.verb}{'ကြ' if pl else ''}သလော"

    def attr(self):
        return f"{self._o(True)} {self.verb}ကြသော"

    def stmt(self, pl=True):
        return f"{self._o(pl)} {self.verb}{'ကြ' if pl else ''}သည်"

    def neg(self, pl=True):
        return f"{self._o(pl)} {NEGV[self.verb]}{'ကြ' if pl else ''}"

    def also(self, pl=True):
        return f"{self._o(pl)}လည်း {self.verb}{'ကြ' if pl else ''}"

    def noun(self):
        return self.obj


_B = "kusala|akusala|abyākata|nāma"
PRED_RE = re.compile(rf"^(?:(?P<b>{_B})mūlena )?(?P<k>eka|aññamañña)?(?P<b2>{_B})?mūl(?P<mm>amūl)?(?P<ka>ak)?"
                     rf"(?P<e>āni|ā|aṃ|a|añceva)$")
BASEW_RE = re.compile(r"^(?P<b>kusal|akusal|abyākat|nām)(?:ā|aṃ|a|añca)$")


def root_my(b):
    return f"{BASE[b][1]} {MULA}"


def pred(p):
    """Root predicate (Pāli) -> Pred. 'kusalamūlā' -> «ကုသိုလ်၏ အမြစ်(များ) ဖြစ်»; 'kusalamūlena ekamūlā' ->
    «ကုသိုလ်၏ အမြစ်နှင့် တူညီသော အမြစ် ရှိ»; 'kusalamūlakā' -> «ကုသိုလ်၏ အမြစ်ကို အခြေခံ»; …"""
    m = PRED_RE.match(p)
    if not m:
        raise Miss("pred: " + p)
    core = MULAMULA if m["mm"] else MULA
    ka = bool(m["ka"])
    pre = f"{root_my(m['b'])}{AND} " if m["b"] else ""
    if m["k"] == "eka":
        obj = f"{pre}{EKA} {core}"
        return Pred(obj + "ကို", KA_VERB) if ka else Pred(obj, HAVE)
    if m["k"] == "aññamañña":
        obj = f"{pre}{ANNA} {core}"
        return Pred(obj + "ကို", KA_VERB) if ka else Pred(obj, BE)
    if not m["b2"]:
        raise Miss("pred base: " + p)
    obj = f"{BASE[m['b2']][1]} {core}"
    return Pred(obj + "ကို", KA_VERB) if ka else Pred(obj, BE, plural_noun=True)


def bs(x):
    x = x[0].lower() + x[1:]
    m = BASEW_RE.match(x)
    if not m:
        raise Miss("base: " + x)
    return {"kusal": "kusala", "akusal": "akusala", "abyākat": "abyākata", "nām": "nāma"}[m["b"]]


def subject_noun(s):
    """Ka subject: 'kusalā' -> «ကုသိုလ် သဘောတရား»; a predicate -> «… ရှိကြသော သဘောတရား»."""
    if BASEW_RE.match(s):
        return f"{BASE[bs(s)][0]} {DHAMMA}"
    return f"{pred(s).attr()} {DHAMMA}"


def ye_keci(s, p):                     # (Ka) ye keci S dhammā, sabbe te P?
    return f"{subject_noun(s)} {WHATEVER}{C} {ALL} {pred(p).q()}{END}"


def ye_va_pana(p, s):                  # (Kha) ye vā pana P, sabbe te dhammā S?
    return f"{VA_PANA} {pred(p).attr()} {THING} {WHATEVER}{C} {ALL} {BASE[bs(s)][0]} {DHAMMA_PL} {BE}ကြသလော{END}"


def unti(p):
    return p[:-2] if p.endswith("ti") else p


C_KA = re.compile(r"^ye keci (?P<s>.+?) dhammā, sabbe te (?P<p>.+?)[?.]$")
C_KHA = re.compile(r"^ye vā pana (?P<p>.+?), sabbe te dhammā (?P<s>\S+?)[?.]$")
C_COUNT = re.compile(r"^(?P<n>Tīṇeva|Naveva) (?P<p>\S+)\.$")
C_AVAS = re.compile(r"^Avasesā (?P<s>\S+) dhammā na (?P<p>\S+)\.$")
C_RUPA = re.compile(r"^(?P<b>\w+?)samuṭṭhānaṃ rūpaṃ (?P<p>.+?),? na (?P<b2>\w+?aṃ)\.$")
C_BOTH = re.compile(r"^(?P<b>\w+?aṃ) (?P<p>.+?)ñceva (?P<b2>\w+?añca)\.$")
C_MULANI = re.compile(r"^Mūlāni yāni ekato uppajjanti (?P<b>\w+?)mūlāni (?P<e>\S+) ceva (?P<a>\S+) ca\.$")
C_SAHA = re.compile(r"^Avasesā (?P<b>\w+?)mūlasahajātā dhammā (?P<p>.+?),? na ca (?P<q>\S+)\.$")
C_HETUKA = re.compile(r"^(?P<h>A|Sa)hetukaṃ (?P<b>\w+?aṃ) (?P<p>.+)\.$")


def base_noun(w):
    b = bs(w)
    return BASE[b][2]


def ch1_sentence(s):
    m = C_KA.match(s)
    if m:
        return ye_keci(m["s"], unti(m["p"]))
    m = C_KHA.match(s)
    if m:
        return ye_va_pana(m["p"], unti(m["s"]))
    m = C_COUNT.match(s)
    if m:
        return f"{pred(m['p']).noun()} {NUM[m['n']]}{ONLY}{END}"
    m = C_AVAS.match(s)
    if m:
        return f"{AVASESA} {BASE[bs(m['s'])][0]} {DHAMMA_PL}သည် {pred(m['p']).neg()}{END}"
    m = C_RUPA.match(s)
    if m:
        b = bs(m["b"])
        p = m["p"]
        return (f"{BASE[b][2]}{SAMUTTHANA} {RUPA_W}သည် {pred(p).stmt(False)}{C} "
                f"{base_noun(m['b2'])} {NEGV[BE]}{END}")
    m = C_BOTH.match(s)
    if m:
        p = pred(m["p"] + "ṃ")
        return f"{base_noun(m['b'])}သည် {p.also(False)}{C} {base_noun(m['b2'])}လည်း {BE}သည်{END}"
    m = C_MULANI.match(s)
    if m:
        b = bs(m["b"])
        return (f"{ARISE_TOGETHER} {MULA}များ {BE}သည့် {root_my(b)}များသည် {pred(m['e']).also()}{C} "
                f"{pred(m['a']).also()}သည်{END}")
    m = C_SAHA.match(s)
    if m:
        b = bs(m["b"])
        return (f"{AVASESA} {root_my(b)}{SAHAJATA} {DHAMMA_PL}သည် {pred(m['p']).stmt()}{C} "
                f"{BUT} {pred(m['q']).neg()}{END}")
    m = C_HETUKA.match(s)
    if m:
        p = m["p"]
        neg = bool(re.search(r"(?:^| )na ", p))
        p = re.sub(r"(?:(?<= )|^)na ", "", p)
        pr = pred(p)
        b = bs(m["b"])
        h = AHETUKA if m["h"] == "A" else SAHETUKA
        sep = f"{C} " if b == "abyākata" else " "
        return f"{h}{sep}{BASE[b][2]}သည် {pr.neg(False) if neg else pr.stmt(False)}{END}"
    return None


# --- ch. 1 hetuvāra: the synonym list «Mūlaṃ hetu nidānañca …» (each Pāli word its own Burmese) -----------------------
HETU = {"mūlā": MULA,                      # mūla
        "hetū": "အကြောင်း",                 # hetu: cause (pi-4 / pi-5 sense «အကြောင်း»; NOT pi-1 «အမြစ်», see notes)
        "nidānā": "ဇာစ်မြစ်",               # nidāna (NEW)
        "sambhavā": "ဖြစ်တည်ရာ",            # sambhava (NEW)
        "ppabhavā": "ပေါ်ထွက်ရာ",           # pabhava (NEW)
        "samuṭṭhānā": "ဖြစ်ပေါ်လာရာ",       # samuṭṭhāna (as «…မှ ဖြစ်ပေါ်လာသော», pi-1)
        "āhārā": W("1", "^1-70", "tayo āhārā", "အာဟာရ", key="āhāra"),
        "ārammaṇā": W("1", "^1-M1-13", "ārammaṇ", "အာရုံ", key="ārammaṇa"),
        "paccayā": W("1", "^1-1344", "paccay", "အထောက်အပံ့", key="paccaya"),   # pi-1 / pi-2 termbase
        "samudayā": W("1", "^1-1063", "samuday", "ဖြစ်ပေါ်ခြင်း", key="samudaya")}
HETU_VERSE = (f"{MULA}{C} {HETU['hetū']}{AND} {HETU['nidānā']}{C} {HETU['sambhavā']}{AND} {HETU['ppabhavā']}{C}",
              f"{HETU['samuṭṭhānā']}{C} {HETU['āhārā']}{C} {HETU['ārammaṇā']}{{v}}{C} {HETU['paccayā']}{AND} "
              f"{HETU['samudayā']}{END}")
HETU_ITEM_RE = re.compile(r"^(?P<b>kusal|akusal|abyākat|nām)a?(?P<w>hetū|nidānā|sambhavā|ppabhavā|samuṭṭhānā|āhārā|"
                          r"ārammaṇā|paccayā|samudayā)(?P<ti> ?ti)?$")


def hetu_noun(b, w):
    return f"{BASE[b][1]} {HETU[w]}"


def hetu_piece(t):
    """One piece of a hetuvāra line (between «…»)."""
    t0 = t.strip()
    if not t0:
        return ""
    if t0 in ("?", "."):
        return END
    m = HETU_ITEM_RE.match(t0)
    if m:
        b = bs(m["b"] + "a")
        n = hetu_noun(b, m["w"]) + "များ"
        return f"{n} {BE}ကြသလော" if m["ti"] else n
    m = re.fullmatch(r"[Yy]e keci (?P<s>\w+) dhammā(?:, sabbe te (?P<p>.+))?", t0)
    if m:
        out = f"{BASE[bs(m['s'])][0]} {DHAMMA} {WHATEVER}"
        if m["p"]:
            out += f"{C} {ALL} {hetu_piece(m['p'])}"
        return out
    m = re.fullmatch(r"Tayo eva (?P<i>\S+), avasesā (?P<s>\w+) dhammā na (?P<p>\S+)", t0)
    if m:
        mi, mp = HETU_ITEM_RE.match(m["i"]), HETU_ITEM_RE.match(m["p"])
        return (f"{hetu_noun(bs(mi['b'] + 'a'), mi['w'])} {NUM['Tayo eva']}{ONLY}{C} {AVASESA} "
                f"{BASE[bs(m['s'])][0]} {DHAMMA_PL}သည် {hetu_noun(bs(mp['b'] + 'a'), mp['w'])}များ {NEGV[BE]}ကြ")
    raise Miss("hetu piece: " + t0)


def hetu_line(s):
    """The hetuvāra lines with «…pe…» / «…»: every «…» kept, each piece translated."""
    s = s.replace("…pe…", PE).replace("…Pe…", PE)
    out = []
    for p in s.split(PE):
        q = hetu_piece(p)
        out.append((" " if p.startswith(" ") and q not in ("", END) else "") + q)
    return PE.join(out)


# ===================================================================================== ch. 2 paṇṇattivāra (khandha)
W("1", "^1-1044", "rūpaṃ, vedanā, saññā, saṅkhārā, viññāṇaṃ", "ရုပ်၊ ခံစားမှု၊ မှတ်သိမှု၊ ပြုပြင်ဖန်တီးမှုများ၊ သိစိတ်",
  key="rūpaṃ, vedanā, saññā, saṅkhārā, viññāṇaṃ")
KHANDHA_W = W("5", "^5-212", "Khandhā", "အစုအဝေးတို့", key="khandhā")
# term -> (Burmese, plural)
PT = {"rūpaṃ": ("ရုပ်", False), "vedanā": ("ခံစားမှု", False), "saññā": ("မှတ်သိမှု", False),
      "saṅkhārā": ("ပြုပြင်ဖန်တီးမှုများ", True), "viññāṇaṃ": ("သိစိတ်", False),
      "khandho": ("အစုအဝေး", False), "khandhā": (KHANDHA_W, True)}
PT.update({k: (v, False) for k, v in KHANDHA.items()})
PT_ACC = {"vedanaṃ": "vedanā", "saññaṃ": "saññā", "saṅkhāre": "saṅkhārā", "khandhe": "khandhā"}
PT_ACC.update({k[:-1] + "aṃ": k for k in KHANDHA})          # rūpakkhandhaṃ …
PIYA = W("2", "^2-203", "Kiñca loke piyarūpaṃ sātarūpaṃ",
         "ချစ်ဖွယ် သဘော ရှိသော၊ နှစ်သက်ဖွယ်ကောင်းသော သဘော ရှိသော အရာ", key="piyarūpaṃ sātarūpaṃ")
DITTHI = W("1", "^1-M2-111", "diṭṭhi", "အယူ", key="diṭṭhi")
SPECIAL_SUBJ = {"Piyarūpaṃ sātarūpaṃ": PIYA,
                "Diṭṭhisaññā": f"{DITTHI} {BE}သော {PT['saññā'][0]}"}     # NEW: «အယူ ဖြစ်သော မှတ်သိမှု»


def add_term(pali, my, plural=False, acc=None):
    """Later chapters: add a paṇṇattivāra term (nominative) and its accusative form."""
    if pali in PT and PT[pali] != (my, plural):
        raise Miss(f"add_term {pali}: already {PT[pali]}")
    PT[pali] = (my, plural)
    if acc:
        PT_ACC[acc] = pali


def term(w):
    """Pāli term surface form (rūpanti, Rūpañca, vedanākkhandhoti, saññā ceva, khandhe …) -> (Burmese, plural)."""
    w = w.strip()
    if w.endswith(" ca") or w.endswith(" ceva"):
        w = w.rsplit(" ", 1)[0]
    w = w[0].lower() + w[1:]
    for suf, rep in (("ñceva", "ṃ"), ("ñca", "ṃ"), ("nti", "ṃ"), ("ti", "")):
        if w.endswith(suf) and ((w[: -len(suf)] + rep) in PT or (w[: -len(suf)] + rep) in PT_ACC):
            w = w[: -len(suf)] + rep
            break
    w = PT_ACC.get(w, w)
    if w not in PT:
        raise Miss("term: " + w)
    return PT[w]


def ko(t):
    return "ကြ" if t[1] else ""


def q_term(a, b, neg=False):
    """(Ka) rūpaṃ rūpakkhandho? -> «ရုပ်သည် ရုပ် အစုအဝေး ဖြစ်သလော။»;
    (Ka) na rūpaṃ na rūpakkhandho? -> «ရုပ် မဟုတ်သော အရာသည် ရုပ် အစုအဝေး မဟုတ်သလော။»"""
    A, B = term(a), term(b)
    if neg:
        return f"{A[0]} {NEGV[BE]}သော {THING}သည် {B[0]} {NEGV[BE]}သလော{END}"
    return f"{A[0]}သည် {B[0]} {BE}{ko(A)}သလော{END}"


def is_(t, pl):        # «… ဖြစ်(ကြ)သည်»
    return f"{t} {BE}{'ကြ' if pl else ''}သည်"


def isnt(t, pl):
    return f"{t} {NEGV[BE]}{'ကြ' if pl else ''}"


def leave(*ts):
    """ṭhapetvā: «Aနှင့် Bကို ချန်ထား၍၊»"""
    return f"{AND} ".join(t[0] for t in ts).replace(f" {AND} ", f"{AND} ") + f"ကို {THAPETVA}{C}"


SPEC = "(?P<s>" + "|".join(SPECIAL_SUBJ) + ")"
P1 = re.compile(rf"^{SPEC} (?P<a>\S+), na (?P<b>\S+)\.$")
P1B = re.compile(r"^(?P<s>\S+) ṭhapetvā avasesā (?P<a>\S+)(?P<v> ⟦\d+⟧)?, na (?P<b>\S+)\.$")
P2 = re.compile(r"^(?P<x>\S+) (?P<a>\S+?)(?P<ce>ñceva| ceva) (?P<b>\S+) ca\.$")
P3 = re.compile(r"^Avasesā (?P<a>\S+)(?P<v> ⟦\d+⟧)? na (?P<b>\S+)\.$")
P4 = re.compile(rf"^{SPEC} na (?P<b>\S+), (?P<a>\S+)\.$")
P4B = re.compile(r"^(?P<s>\S+) ṭhapetvā avasesā (?:(?P<k>\S+) )?na (?P<b>\S+), (?P<a>\S+)\.$")
P5 = re.compile(r"^(?P<a>\S+?ñca|\S+ ca) (?P<b>\S+?ñca|\S+ ca) ṭhapetvā avasesā na ceva (?P<a2>\S+) na ca (?P<b2>\S+)\.$")
P_Q = re.compile(r"^(?P<n1>na )?(?P<a>\S+) (?P<n2>na )?(?P<b>\S+?)[?.]$")


def pannatti_sentence(s):
    m = P1.match(s)
    if m:
        A, B = term(m["a"]), term(m["b"])
        return f"{SPECIAL_SUBJ[m['s']]}သည် {is_(A[0], False)}{C} {isnt(B[0], False)}{END}"
    m = P1B.match(s)
    if m:
        S, A, B = term(m["s"]), term(m["a"]), term(m["b"])
        return (f"{leave(S)} {AVASESA_N}သည် {A[0]}{m['v'] or ''} {BE}ကြသည်{C} {isnt(B[0], True)}{END}")
    m = P2.match(s)
    if m:
        X, B = term(m["x"]), term(m["b"])
        A = term(m["a"] + ("ñceva" if m["ce"] == "ñceva" else ""))
        return f"{X[0]}သည် {A[0]}လည်း {BE}{C} {B[0]}လည်း {BE}{ko(X)}သည်{END}"
    m = P3.match(s)
    if m:
        A, B = term(m["a"]), term(m["b"])
        return f"{AVASESA} {A[0]}သည်{m['v'] or ''} {isnt(B[0], A[1])}{END}"
    m = P4.match(s)
    if m:
        A, B = term(m["a"]), term(m["b"])
        return f"{SPECIAL_SUBJ[m['s']]}သည် {isnt(B[0], False)}{C} {is_(A[0], False)}{END}"
    m = P4B.match(s)
    if m:
        S, A, B = term(m["s"]), term(m["a"]), term(m["b"])
        subj_ = f"{AVASESA} {term(m['k'])[0]}" if m["k"] else AVASESA_N
        return f"{leave(S)} {subj_}သည် {isnt(B[0], True)}{C} {is_(A[0], True)}{END}"
    m = P5.match(s)
    if m:
        A, B, A2, B2 = (term(m[k]) for k in ("a", "b", "a2", "b2"))
        return f"{leave(A, B)} {AVASESA_N}သည် {A2[0]}လည်း {NEGV[BE]}{C} {B2[0]}လည်း {NEGV[BE]}{END}"
    m = P_Q.match(s)
    if m and bool(m["n1"]) == bool(m["n2"]):
        try:
            return q_term(m["a"], m["b"], bool(m["n1"]))
        except Miss:
            return None
    return None


# ===================================================================================== headings and colophons
UDDESO = heads("Uddeso")                                       # «အကျဉ်း ဖော်ပြချက်» (pi-1 / pi-3)
NIDDESO = W("1", "^1-2-3-1-0", "Ekakaniddeso", "အကျယ် ဖော်ပြချက်", key="niddeso")
VARA = "ဖော်ပြချက်"                                          # -vāra «… ဖော်ပြချက်» (pi-1 / pi-2 headings)
W("2", "^2-15-1-2-0", "Saccavāro", "သစ္စာအလိုက် ဖော်ပြချက်", key="Xvāro")
NAYA = W("3", "^3-1-1-0", "Naya", "ခွဲနည်း", key="naya")
ALIKE = "အလိုက်"
ADI = W("3", "^3-15-1-1-0", "Khandhādi", "စသည်", key="-ādi")
SUDDHA = W("5", "^5-1-1-0", "Suddh", "ရိုးရိုး", key="suddha")
PANNATTI = W("1", "^1-M2-108", "paññatti", "သတ်မှတ်ချက်", key="paṇṇatti")
PUGGALA = W("1", "^1-1050", "puggal", "ပုဂ္ဂိုလ်", key="puggala")
OKASA = "နေရာ"
TIMES = {"Paccuppanna": W("1", "^1-M1-18", "paccuppann", "ပစ္စုပ္ပန်", key="paccuppanna"),
         "Atīta": W("1", "^1-M1-18", "atītā", "အတိတ်", key="atīta"),
         "Anāgata": W("1", "^1-M1-18", "anāgat", "အနာဂတ်", key="anāgata")}
UPPADA = W("1", "^1-1-0", "Cittuppādakaṇḍaṃ", "ဖြစ်ပေါ်ခြင်း", key="uppāda")
NIRODHA = W("1", "^1-1063", "nirodh", "ချုပ်ငြိမ်းခြင်း", key="nirodha")
PAVATTI = "ဖြစ်ပျက်ခြင်း"                                    # pavatti (NEW: the occurrence, arising and ceasing)
ANULOMA = "အဟုတ်ပြ ပုံစံ"                                     # anuloma of a Yamaka question (NEW sense)
PACCANIKA = "အငြင်းပြ ပုံစံ"                                  # paccanīka (NEW sense; pi-5 «ပြောင်းပြန်» = debate order)
CAKKA = "လှည့်ပတ်ခြင်း"                                       # -cakka (the rotation of the terms) (NEW)
BASED = "ကို အခြေခံ၍"                                        # -mūla- of the mūlacakka headings
PADASODHANA = "စကားလုံးကို စိစစ်ခြင်း"                        # padasodhana (NEW)


def vara(x, alike=True):
    return f"{x}{ALIKE} {VARA}" if alike else f"{x} {VARA}"


def yamaka_name(x):
    """«Xများကို အတွဲလိုက် မေးဖြေခြင်း» (the chapter names)."""
    return f"{x}{YAMAKA}"


# the ten chapters: Pāli stem -> Burmese topic (pi-1 / pi-2 final); chapters 3-10 are PROPOSED for the later agents
TOPICS = {
    "Mūla": f"{MULA}များ",
    "Khandha": "အစုအဝေးများ",
    "Āyatana": W("1", "^1-M2-122", "āyatan", "အာရုံခံ နယ်ပယ်", key="āyatana") + "များ",
    "Dhātu": W("1", "^1-M2-121", "dhātu", "ဓာတ်", key="dhātu") + "များ",
    "Sacca": W("2", "^2-15-1-2-0", "Saccavāro", "သစ္စာ", key="sacca") + "များ",
    "Saṅkhāra": W("1", "^1-40", "saṅkhār", "ပြုပြင်ဖန်တီးမှု", key="saṅkhāra") + "များ",
    "Anusaya": W("1", "^1-1065", "anusay", "ကိန်းအောင်းခြင်း", key="anusaya") + "များ",
    "Citta": W("1", "^1-6", "cittaṃ", "စိတ်", key="citta"),
    "Dhamma": DHAMMA_PL,
    "Indriya": W("1", "^1-1", "indriy", "စွမ်းရည်", key="indriya") + "များ",
}
H = {f"{k}yamakaṃ": yamaka_name(v) for k, v in TOPICS.items()}
H.update({
    "Mūlayamakaṃ": yamaka_name(f"{MULA}များ"),
    "Khandhayamakaṃ": yamaka_name("အစုအဝေးများ"),
    "uddeso": UDDESO,
    "niddeso": NIDDESO,
    "Mūlavāro": vara(MULA),
    "2-10. Hetuvārādi": f"2-10. {vara(HETU['hetū'])} {ADI}",
    "Paṇṇattivāro": vara(PANNATTI),
    "Padasodhanavāro": vara(PADASODHANA, False),
    "Padasodhanamūlacakkavāro": vara(f"{PADASODHANA}{BASED} {CAKKA}", False),
    "Suddhakhandhavāro": vara(f"{SUDDHA} အစုအဝေး", False),
    "Suddhakhandhamūlacakkavāro": vara(f"{SUDDHA} အစုအဝေး{BASED} {CAKKA}", False),
    "Paṇṇattivāraniddesa": f"{vara(PANNATTI)}၏ {NIDDESO}",
    "anulomaṃ": ANULOMA,
    "paccanīkaṃ": PACCANIKA,
    "Pavattivāro 1. uppādavāro": f"{vara(PAVATTI)} 1. {vara(UPPADA)}",
    "Pavatti 2. nirodhavāro": f"{PAVATTI} 2. {vara(NIRODHA)}",
    "Paccuppannavāro": vara(TIMES["Paccuppanna"]),
    "Atītavāro": vara(TIMES["Atīta"]),
    "Anāgatavāro": vara(TIMES["Anāgata"]),
    "Paccuppannātītavāro": vara(f"{TIMES['Paccuppanna']}{AND} {TIMES['Atīta']}"),
    "Paccuppannānāgatavāro": vara(f"{TIMES['Paccuppanna']}{AND} {TIMES['Anāgata']}"),
    "Atītānāgatavāro": vara(f"{TIMES['Atīta']}{AND} {TIMES['Anāgata']}"),
    "anulomapuggalo": f"{PUGGALA}{ALIKE} {ANULOMA}",
    "anulomaokāso": f"{OKASA}{ALIKE} {ANULOMA}",
    "anulomapuggalokāsā": f"{PUGGALA}{AND} {OKASA}{ALIKE} {ANULOMA}",
    "paccanīkapuggalo": f"{PUGGALA}{ALIKE} {PACCANIKA}",
    "paccanīkaokāso": f"{OKASA}{ALIKE} {PACCANIKA}",
    "paccanīkapuggalokāsā": f"{PUGGALA}{AND} {OKASA}{ALIKE} {PACCANIKA}",
    "Mūlanayo": f"{MULA} {NAYA}",
    "Mūlamūlanayo": f"{MULAMULA} {NAYA}",
    "Mūlakanayo": f"{MULA}ကို {KA_VERB}ခြင်း {NAYA}",
    "Mūlamūlakanayo": f"{MULAMULA}ကို {KA_VERB}ခြင်း {NAYA}",
})
H.update({f"{k[0].upper()}{k[1:-1]}ā dhammā": f"{v[0]} {DHAMMA_PL}" for k, v in BASE.items()})   # Kusalā dhammā …


def heading(t):
    """Heading text (no #, no ID) -> Burmese. Handles «(Ka) uddeso», «(1) Mūlanayo», «Akusalā dhammā (1) mūlanayo»."""
    if t in H:
        return H[t]
    m = LABEL_RE.match(t)
    if m:
        return f"{label(m.group(1))} {heading(t[m.end():])}"
    m = re.fullmatch(r"\((\d+)\) (.+)", t)
    if m:
        return f"({m.group(1)}) {heading(m.group(2)[0].upper() + m.group(2)[1:])}"
    m = re.fullmatch(r"(\w+ dhammā) (\(\d+\) .+)", t)
    if m:
        return f"{heading(m.group(1))} {heading(m.group(2))}"
    raise Miss("heading: " + t)


COLO = {   # colophon lines (end of a section)
    "Mūlavārauddeso.": f"{vara(MULA)}၏ {UDDESO}{END}",
    "Uddesavāro niṭṭhito.": finished(UDDESO),
    "Mūlavāraniddeso.": f"{vara(MULA)}၏ {NIDDESO}{END}",
    "Niddesavāro niṭṭhito.": finished(NIDDESO),
    "Mūlayamakapāḷi niṭṭhitā.": finished(H["Mūlayamakaṃ"]),
    "Paṇṇattiuddesavāro.": f"{vara(PANNATTI)}၏ {UDDESO}{END}",
    "Paṇṇattiniddesavāro.": f"{vara(PANNATTI)}၏ {NIDDESO}{END}",
    "Uppādavāro niṭṭhito.": finished(vara(UPPADA)),
    "Namo tassa bhagavato arahato sammāsambuddhassa": NAMO,
}
# chapter colophons of the later chapters (PROPOSED; «Xyamakaṃ niṭṭhitaṃ.» / «Xyamakapāḷi niṭṭhitā.»)
COLO.update({f"{k}yamakaṃ niṭṭhitaṃ.": finished(H[f"{k}yamakaṃ"]) for k in TOPICS})
COLO.update({f"{k}yamakapāḷi niṭṭhitā.": finished(H[f"{k}yamakaṃ"]) for k in TOPICS})
LINES = {  # whole lines (Pāli without brackets, a bracket as ⟦v⟧ -> Burmese with {v})
    "Mūlaṃ hetu nidānañca, sambhavo pabhavena ca;": HETU_VERSE[0],
    "Samuṭṭhānāhārārammaṇā⟦v⟧, paccayo samudayena cāti.": HETU_VERSE[1],
    "Samuṭṭhānāhārārammaṇā, paccayo samudayena cāti.": HETU_VERSE[1].format(v=""),
    "Pañcakkhandhā – rūpakkhandho, vedanākkhandho, saññākkhandho, saṅkhārakkhandho, viññāṇakkhandho.":
        heads("Pañcakkhandhā – rūpakkhandho, vedanākkhandho, saññākkhandho, saṅkhārakkhandho, viññāṇakkhandho."),
}

# ===================================================================================== engine
SPLIT = re.compile(r"(?<=[?.]) (?=[A-ZĀĪŪṬḌṆÑṄ(])")
BRACKET = re.compile(r" ?\[([^\]]*)\]")
FRAMES = [pavatti_sentence, ch1_sentence, pannatti_sentence]


def sentence_my(s):
    for fn in FRAMES:
        r = fn(s)
        if r:
            return r
    raise Miss("no frame for: " + s)


def body_my(line):
    """A line without block ID, heading mark or item label -> Burmese."""
    if line in COLO:
        return COLO[line]
    vars_ = []

    def keep(m):
        vars_.append(variant(m[1]))
        return f" ⟦{len(vars_) - 1}⟧"
    if line in LINES:
        return LINES[line]
    key = BRACKET.sub("⟦v⟧", line)
    if key in LINES:
        v = BRACKET.search(line)[1]
        return LINES[key].format(v=" " + variant(v))
    if "…" in line:
        return hetu_line(line)
    line = BRACKET.sub(keep, line)
    out = " ".join(sentence_my(s) for s in SPLIT.split(line))
    for i, v in enumerate(vars_):
        out = out.replace(f"⟦{i}⟧", v)
    return out


def translate_line(line):
    if not line.strip():
        return ""
    bid = ""
    m = ID_RE.search(line)
    if m:
        bid, line = " " + m[1], line[: m.start()]
    h = re.match(r"^(#+) (.*)$", line)
    if h:
        return f"{h[1]} {heading(h[2])}{bid}"
    lab = ""
    m = LABEL_RE.match(line)
    if m:
        lab, line = label(m[1]) + " ", line[m.end():]
    out = lab + body_my(line) + bid
    left = re.sub(r"\[[^\]]*\]", "", out)
    if re.search(r"[A-Za-zāīūṃṅñṭḍṇḷ]", left.replace(bid, "")):
        raise Miss("Pāli left in: " + out)
    return out


def translate_text(text):
    return "\n".join(translate_line(l) for l in text.splitlines()) + "\n"
