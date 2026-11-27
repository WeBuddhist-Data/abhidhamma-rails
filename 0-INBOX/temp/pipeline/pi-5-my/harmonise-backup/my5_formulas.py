"""Shared Burmese formulas for pi-5 (Kathāvatthu, «အငြင်းပွားရာ အကြောင်းအရာများကို ဆွေးနွေးခြင်း»), plain audience.

Every pi-5 Burmese generator imports this module, so that identical Pāli gets identical Burmese, within pi-5 and with
the FINAL pi-1 … pi-4 Burmese (the rails texts). Writes no files at import (no bytecode either). It holds:
  * FINAL: an index of the rails texts of pi-1 … pi-4 aligned with their Pāli by block ID (read only; nothing in
    pi-1-my … pi-4-my is imported or written). heads() (whole lines, headings, colophons), items() (the topic lists
    «Head – a, b, c») and witness() (a term: the Pāli must occur in the Pāli segment and the Burmese in its rails
    Burmese) READ or CHECK every reused value; WITNESS records them for the terms file and the reuse test;
  * the book frame, headings, set names (closers), ordinals, sakavādī / paravādī, the editorial-note and variant
    renderer (bracket_my());
  * Cl, the proposition clause: one Burmese clause with its final verb, so that the same proposition can be
    rendered as a statement, a question, a condition, a bare series item or a «nanu» question (Cl.f(form, depth));
    quote marks inside a clause are written «…» (one level down) and ‹…› (two levels down) and set by depth;
  * the nouns (khandha / āyatana / dhātu / indriya from the pi-2 lists, NOUN) and the clause RULES built on them;
  * PROP: shared propositions (Pāli, canonical form -> Cl); prop_my() translates a proposition, splitting a compound
    one at «, » / «; » / «…» into the longest known parts;
  * the dialectic FRAMES (sentence level) and LINE_FRAMES (the multi-sentence lines «Tvaṃ ce pana …»,
    «Ese ce dunniggahite …», «Na hevaṃ niggahetabbe. Tena hi …»), and the engine translate_line().
A sentence that no frame, table or rule matches raises Miss: nothing is guessed.
Later chapters: import this module, add entries to the tables (never change an existing value without the user's
approval), put the chapter's unique prose in the generator's own tables (merged into PROP / SENT / LINES).
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


# ===================================================================================== FINAL: rails texts pi-1 … pi-4
ID_RE = re.compile(r" (\^[0-9A-Za-z-]+)\s*$")
BOOKS = {b: (ROOT / f"AI_translation/pali/pi-{b}_split_chapters",
             ROOT / f"AI_translation/burmese/pi-{b}-burmese-plain-rails_split_chapters") for b in "1234"}


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
    """A heading, colophon or whole line «Pāli» of pi-1 … pi-4 -> its final Burmese (all must agree)."""
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


# ===================================================================================== basics and book frame
C = "၊"                               # clause / list break
END = "။"                             # end of a statement or question
PE = "…"                              # …pe… / …Pe… / … = one «…»
NAMO = heads("Namo tassa bhagavato arahato sammāsambuddhassa")
ABHI = heads("Abhidhammapiṭake")
TITLE = "အငြင်းပွားရာ အကြောင်းအရာများကို ဆွေးနွေးခြင်း"     # Kathāvatthu(pāḷi) (book title, Burmese only; proposed)
TITLE2 = heads("Vibhaṅgapakaraṇaṃ niṭṭhitaṃ").split("”")[0].lstrip("“")
TITLE4 = "ပုဂ္ဂိုလ်များကို သတ်မှတ်ဖော်ပြခြင်း"                  # pi-4 book title (pi-4 my4_formulas.TITLE)
witness("4", "^4-0", "Puggalapaññattipāḷi", TITLE4)
BOOK_END = f"“{TITLE}” ကျမ်း ပြီးဆုံးပြီ"                       # Kathāvatthupakaraṇaṃ niṭṭhitaṃ (pattern of pi-1 … pi-3)
assert heads("Dhammasaṅgaṇīpakaraṇaṃ niṭṭhitaṃ").endswith("” ကျမ်း ပြီးဆုံးပြီ")
_DONE = heads("Mātikā niṭṭhitā")                                 # «“ခေါင်းစဉ်စာရင်း” ပြီးဆုံးပြီ»
DONE = "“{}” ပြီးဆုံးပြီ"                                          # X niṭṭhitā / niṭṭhito / niṭṭhitaṃ (section end)
assert _DONE == DONE.format(heads("Mātikā"))
PUGGALA = witness("2", "^2-643", "ekaṃ puggalaṃ", "ပုဂ္ဂိုလ်")       # puggala (pi-1 / pi-2 / pi-4)
CL_P = "ယောက်"                                                     # classifier of persons (pi-2 / pi-4)
CL = "ပါး"                                                         # classifier of things (pi-1 / pi-2)
BHAGAVA = witness("1", "^T-1", "bhagavato", "မြတ်စွာဘုရား")         # bhagavā / bhagavatā
NUM_MY = {1: "တစ်", 2: "နှစ်", 3: "သုံး", 4: "လေး", 5: "ငါး", 6: "ခြောက်", 7: "ခုနစ်", 8: "ရှစ်", 9: "ကိုး", 10: "ဆယ်",
          12: "ဆယ့်နှစ်", 18: "ဆယ့်ရှစ်", 22: "နှစ်ဆယ့်နှစ်"}
ORD_MY = {1: "ပထမ", 2: "ဒုတိယ", 3: "တတိယ", 4: "စတုတ္ထ", 5: "ပဉ္စမ", 6: "ဆဋ္ဌမ", 7: "သတ္တမ", 8: "အဋ္ဌမ", 9: "နဝမ",
          10: "ဒသမ"}
ORD_PI = {"paṭhamo": 1, "dutiyo": 2, "tatiyo": 3, "catuttho": 4, "pañcamo": 5, "chaṭṭho": 6, "sattamo": 7,
          "aṭṭhamo": 8, "navamo": 9, "dasamo": 10, "paṭhama": 1, "dutiya": 2, "tatiya": 3, "catuttha": 4,
          "pañcama": 5, "chaṭṭha": 6, "sattama": 7, "aṭṭhama": 8, "navama": 9, "dasama": 10}
witness("2", "^2-1", "Pañcakkhandhā", f"အစုအဝေး {NUM_MY[5]}{CL}")
witness("2", "^2-183", "Aṭṭhārasa dhātuyo", f"ဓာတ် {NUM_MY[18]}{CL}")
witness("2", "^2-219", "Bāvīsatindriyāni", f"စွမ်းရည် {NUM_MY[22]}{CL}")

# --- the two speakers, the editorial notes, the answers
SAKAVADI = "မိမိဘက်"                                  # sakavādī (the orthodox speaker)
PARAVADI = "တစ်ဖက်သား"                                # paravādī (the opponent)
NOTE = {
    "iminā lakkhaṇena sakavādīpucchā dassitā": f"ဤအမှတ်အသားဖြင့် {SAKAVADI}၏ အမေးကို ပြထားသည်",
    "iminā lakkhaṇena paravādīpucchā dassitā": f"ဤအမှတ်အသားဖြင့် {PARAVADI}၏ အမေးကို ပြထားသည်",
    "ṭīkā oloketabbā": "ဋီကာကို ကြည့်ပါ",
}
YES = "ဟုတ်ပါသည်"                                     # Āmantā (assent; the end mark is added by the frame)
NO_SAY = "ဤသို့ မဆိုသင့်ပါ"                           # Na hevaṃ vattabbe
SAY_ANS = "ဆိုသင့်ပါသည်"                              # Vattabbaṃ (answer)
SANKHITTA = "(အကျဉ်းချုပ်)"                           # (Saṃkhittaṃ)
WRONG = "ဟူသည် မှားသည်"                               # … "ti micchā
WRONG_TE = "ဟူသော ဤစကားသည် သင်၏ အမှား ဖြစ်သည်"        # … "ti idaṃ te micchā
SAY, NOT_SAY = "ဤသို့ ဆိုသင့်သည်", "ဤသို့ကား မဆိုသင့်"   # vattabbe kho – / no ca vattabbe –

# --- set names closing a block (closers) and the refutation ordinals
CLOSE = {
    "Anulomapañcakaṃ": "အစဉ်အတိုင်း ငါးပါးအစု",
    "Paccanīkapañcakaṃ": "ပြောင်းပြန် ငါးပါးအစု",
    "Paṭikammacatukkaṃ": "ပြန်လှန် ချေပချက် လေးပါးအစု",
    "Niggahacatukkaṃ": "ချေပချက် လေးပါးအစု",
    "Upanayanacatukkaṃ": "ဆက်စပ် အသုံးချချက် လေးပါးအစု",
    "Niggamanacatukkaṃ": "နိဂုံးချုပ်ချက် လေးပါးအစု",
    "Aṭṭhakaniggaho": "ချေပချက် ရှစ်ပါးအစု",
}
NIGGAHA = "ချေပချက်"                                  # niggaha (refutation)
PATIKAMMA = "ပြန်လှန် ချေပချက်"                        # paṭikamma (counter-refutation)


def niggaho_my(n):            # Paṭhamo / Dutiyo … niggaho.
    return f"{ORD_MY[n]} {NIGGAHA}"


# ===================================================================================== quotes and clauses
def mark(d):
    """Quote marks for a quotation standing at depth d (1 = “…”, 2 = ‘…’, 3+ = none, as the Pāli)."""
    return {1: ("“", "”"), 2: ("‘", "’")}.get(d, ("", ""))


def q_set(text, depth):
    """Set the relative marks of a table string at depth: «…» = one level down, ‹…› = two levels down."""
    o1, c1 = mark(depth + 1)
    o2, c2 = mark(depth + 2)
    return text.replace("«", o1).replace("»", c1).replace("‹", o2).replace("›", c2)


class Cl:
    """A proposition clause: «pre» + final verb (+ «post»). v / nv = positive / negative verb stem; neg = the
    clause is negative; v None = a fragment (an elided series item) that keeps its words in every form."""

    def __init__(self, pre, v=None, nv=None, neg=False, post=""):
        self.pre, self.v, self.nv, self.neg, self.post = pre, v, nv, neg, post

    def f(self, form, depth=0):
        if self.v is None:
            out = self.pre + self.post
        else:
            verb = self.nv if self.neg else self.v
            tail = {
                "stmt": verb if self.neg else verb + "သည်",
                "q": verb + "သလော",
                "bare": verb,
                "cond": verb + "လျှင်",
                "nanu": (verb if self.neg else verb + "သည်") + " မဟုတ်လော",
                "rel": verb + "သော",
            }[form]
            out = (self.pre + " " if self.pre else "") + tail + self.post
        return q_set(out, depth)


def V(pre, verb="ဖြစ်", neg=False, post=""):
    """Shortcut: a clause with one of the standard verbs (positive / negative stems)."""
    nv = {"ဖြစ်": "မဟုတ်", "ရှိ": "မရှိ", "တွေ့ရ": "မတွေ့ရ"}.get(verb, "မ" + verb)
    return Cl(pre, verb, nv, neg, post)


def FR(text):
    """A fragment (elided series item) without a verb of its own."""
    return Cl(text)


# ===================================================================================== nouns (pi-2 lists)
class N:
    """A Burmese noun phrase with the Pāli forms that name it (nom, ca = «X ca» / «Xñca», loc, abl, acc)."""

    def __init__(self, my, pali, pl=False):
        self.my, self.pali, self.pl = my, pali, pl

    @property
    def obj(self):
        return self.my + "ကို"


NOUN = {}        # Pāli form -> (N, set of roles)


def add_noun(my, pl=False, **forms):
    n = N(my, forms, pl)
    for role, pf in forms.items():
        for x in ([pf] if isinstance(pf, str) else pf):
            NOUN.setdefault(x, (n, set()))[1].add(role)
    return n


def noun(x, role):
    """The noun whose Pāli form x has this role (nom, ca, loc, abl, acc), else None."""
    hit = NOUN.get(x)
    return hit[0] if hit and role in hit[1] else None


_KH_H, _KH = items("2", "^2-1")              # rūpakkhandho … -> «ရုပ် အစုအဝေး» …
_AY_H, _AY = items("2", "^2-154")
_DH_H, _DH = items("2", "^2-183")
_IN_H, _IN = items("2", "^2-219")
KHANDHA_W = _KH_H.split()[0]                 # «အစုအဝေး»
AYATANA_W = "အာရုံခံ နယ်ပယ်"
DHATU_W = "ဓာတ်"
INDRIYA_W = "စွမ်းရည်"


def _kh(stem):                               # «ရုပ် အစုအဝေး» -> «ရုပ်»
    return _KH[stem + "kkhandho"].rsplit(" ", 1)[0]


RUPA = add_noun(_kh("rūpa"), nom="rūpaṃ", ca="rūpañca", loc="rūpasmiṃ", abl="rūpā", acc="rūpaṃ")
VEDANA = add_noun(_kh("vedanā"), nom="vedanā", ca="vedanā ca", loc="vedanāya", abl="vedanāya", acc="vedanaṃ")
SANNA = add_noun(_kh("saññā"), nom="saññā", ca="saññā ca", loc="saññāya", abl="saññāya", acc="saññaṃ")
SANKHARA = add_noun(_kh("saṅkhāra") + "တို့", pl=True, nom="saṅkhārā", ca="saṅkhārā ca", loc="saṅkhāresu",
                    abl="saṅkhārehi", acc="saṅkhāre")
VINNANA = add_noun(_kh("viññāṇa"), nom="viññāṇaṃ", ca="viññāṇañca", loc="viññāṇasmiṃ", abl="viññāṇā",
                   acc="viññāṇaṃ")
KHANDHA5 = [RUPA, VEDANA, SANNA, SANKHARA, VINNANA]
AYATANA = {}
for _p, _m in _AY.items():                   # cakkhāyatanaṃ …
    _s = _p[:-1]                              # «cakkhāyatana»
    AYATANA[_s] = add_noun(_m, nom=_p, ca=_s + "ñca", loc=_s + "smiṃ", abl=_s[:-1] + "ā", acc=_p)
DHATU = {}
for _p, _m in _DH.items():                   # cakkhudhātu …
    DHATU[_p] = add_noun(_m, nom=_p, ca=_p + " ca", loc=_p + "yā", abl=_p + "yā", acc=_p + "ṃ")
INDRIYA = {}
for _p, _m in _IN.items():                   # cakkhundriyaṃ …
    _s = _p[:-1]
    INDRIYA[_s] = add_noun(_m, nom=_p, ca=_s + "ñca", loc=_s + "smiṃ", abl=_s[:-1] + "ā", acc=_p)
INDRIYA["vīriyindriya"] = NOUN["vīriyindriyaṃ"][0]
PUG = add_noun(PUGGALA, nom="puggalo", loc="puggalasmiṃ", acc="puggalaṃ")

SACC = "အမှန်တကယ် အဆုံးစွန် အနက်အားဖြင့်"              # saccikaṭṭhaparamatthena
FACT = "အမှန်တကယ် အဆုံးစွန် အရာ"                        # saccikaṭṭho paramattho
SACCIKATTHA_W = "အမှန်တကယ် အရာ"                          # saccikaṭṭho alone (Vacanasodhana, headings)
FACT_AS = f"{FACT} ဖြစ်သည့်အတိုင်း"                     # yo saccikaṭṭho paramattho, tato …
FOUND = "တွေ့ရ"                                          # upalabbhati (stem; negative «မတွေ့ရ»)
WHERE = {"sabbattha": "နေရာတိုင်း၌", "sabbadā": "အချိန်တိုင်း၌", "sabbesu": "အရာအားလုံး၌"}


def found_cl(n, ca=False, full=True, neg=False, pre=""):
    """X (ca) (n)upalabbhati (saccikaṭṭhaparamatthena)."""
    obj = n.my + ("ကိုလည်း" if ca else "ကို")
    words = " ".join(x for x in (pre, obj, SACC if full else "") if x)
    return V(words, FOUND, neg)


def other_cl(*ns):
    """aññaṃ A añño B (añño C) = «Aနှင့် Bသည် တခြားစီ ဖြစ်» (pi-1 «aññaṃ jīvaṃ aññaṃ sarīraṃ»)."""
    names = [n if isinstance(n, str) else n.my for n in ns]
    head = "နှင့် ".join(names[:-1]) + "နှင့် " + names[-1] if len(names) > 1 else names[0]
    return V(f"{head}သည် {OTHER}")


# ===================================================================================== reused terms (witnessed)
JIVA_SARIRA_SAME = witness("1", "^1-1105", "taṃ jīvaṃ taṃ sarīr", "အသက်သည် ကိုယ်ခန္ဓာပင် ဖြစ်")
JIVA_SARIRA_OTHER = witness("1", "^1-1105", "aññaṃ jīvaṃ aññaṃ sarīr", "အသက်နှင့် ကိုယ်ခန္ဓာသည် တခြားစီ ဖြစ်")
OTHER = "တခြားစီ"                                        # añña … añña (pi-1)
JIVA = witness("1", "^1-1105", "jīvaṃ", "အသက်")
SARIRA = witness("1", "^1-1105", "sarīr", "ကိုယ်ခန္ဓာ")
KAYA = witness("2", "^2-154", "Kāyo anicco", "ကိုယ်")       # kāya (the body; kept apart from sarīra)
SASSATA = witness("1", "^1-1105", "Sassato lokoti", "ထာဝရ တည်မြဲ")
ASASSATA = witness("1", "^1-1105", "asassato lokoti", "ထာဝရ မတည်မြဲ")
SAPPACCAYA = witness("1", "^1-M2-7", "sappaccayā dhammā", "အကြောင်း ရှိသော")
SANKHATA = witness("1", "^1-M2-8", "saṅkhatā dhammā", "ပြုပြင်ဖန်တီးထားသော")
ASANKHATA = witness("1", "^1-M2-8", "asaṅkhatā dhammā", "ပြုပြင်ဖန်တီးထားခြင်း မရှိသော")
SANIDASSANA = witness("1", "^1-M2-9", "sanidassanā dhammā", "မြင်နိုင်သော")
ANIDASSANA = "မမြင်နိုင်သော"                              # anidassana (pi-1 ^1-M1-22 «မမြင်နိုင်သော်လည်း»)
witness("1", "^1-M1-22", "anidassanasappaṭighā dhammā", "မမြင်နိုင်")
SAPPATIGHA = witness("1", "^1-M1-22", "anidassanasappaṭighā dhammā", "ထိခိုက်မှု ရှိသော")
APPATIGHA = "ထိခိုက်မှု မရှိသော"                           # appaṭigha
NIMITTA = witness("1", "^1-M2-133", "samathanimittañca", "အမှတ်အသား")
witness("1", "^1-1386", "vipāko", "ကံ၏ အကျိုး")
KAMMA = "ကံ"                                                # kamma (pi-1 «ကံ၏ အကျိုး»)
VIPAKA = "အကျိုး"                                           # vipāka (pi-1 «ကံ၏ အကျိုး»)
NIBBANA = witness("1", "^1-1386", "nibbānañca", "နိဗ္ဗာန်")
SATTA = witness("1", "^1-645", "sattā yāpenti", "သတ္တဝါ")    # satta (being)
KHATTIYA = witness("2", "^2-974", "Khattiyosmīti", "မင်းမျိုး")
BRAHMANA = witness("2", "^2-974", "brāhmaṇosmīti", "ပုဏ္ဏား")
VESSA = witness("2", "^2-974", "vessosmīti", "ကုန်သည်မျိုး")
SUDDA = witness("2", "^2-974", "suddosmīti", "သူဆင်းရဲမျိုး")
GAHATTHA = witness("2", "^2-974", "gahaṭṭhosmīti", "လူဝတ်ကြောင်")
PABBAJITA = witness("2", "^2-974", "pabbajitosmīti", "ရဟန်း")
MATA = witness("1", "^1-1221", "natthi mātā", "အမိ")
PITA = witness("1", "^1-1221", "natthi pitā", "အဖ")
UPADAYA = witness("1", "^1-616", "catunnaṃ mahābhūtānaṃ upādāya", "ကို မှီ၍")   # upādāya (pi-1)
PANNATTI = witness("1", "^1-M2-108", "paññatti dhammā", "သတ်မှတ်ချက်")           # paññatti (pi-1 / pi-4)
SOTAPANNA = witness("4", "^4-M-7", "Sotāpanno", "သောတာပန်")
SAKADAGAMI = witness("4", "^4-M-7", "Sakadāgāmī", "သကဒါဂါမ်")
ANAGAMI = witness("4", "^4-M-7", "Anāgāmī", "အနာဂါမ်")
ARAHA = witness("4", "^4-11", "Arahā abhayūparato", "ရဟန္တာ")
UBHATO = witness("4", "^4-M-7", "Ubhatobhāgavimutto", "နှစ်ဖက်စလုံးမှ လွတ်မြောက်သူ")
PANNAVIM = witness("4", "^4-M-7", "Paññāvimutto", "ပညာဖြင့် လွတ်မြောက်သူ")
KAYASAKKHI = witness("4", "^4-M-7", "Kāyasakkhī", "ကိုယ်ဖြင့် မျက်မှောက်ပြုသူ")
DITTHIPPATTA = witness("4", "^4-M-7", "Diṭṭhippatto", "မှန်ကန်သော အယူသို့ ရောက်သူ")
SADDHAVIM = witness("4", "^4-M-9", "saddhāvimutto", "ယုံကြည်မှုဖြင့် လွတ်မြောက်သူ")
DHAMMANUSARI = witness("4", "^4-M-7", "Dhammānusārī", "တရားကို အစဉ်လိုက်သူ")
SADDHANUSARI = witness("4", "^4-M-7", "Saddhānusārī", "ယုံကြည်မှုကို အစဉ်လိုက်သူ")
ATTAHITA = witness("4", "^4-M-10", "attahitāya paṭipanno", "မိမိ၏ အကျိုးအတွက် ကျင့်ကြံသူ")
ATTAHITA_PUG = "မိမိ၏ အကျိုးအတွက် ကျင့်ကြံသော ပုဂ္ဂိုလ်"   # atthi puggalo attahitāya paṭipanno (pi-4 phrase + puggalo)
SUTTANTA = witness("1", "^1-M-2-14-0", "Suttantikadukamātikā", "သုတ္တန်")
DIBBACAKKHU = witness("4", "^4-184", "dibbena cakkhunā visuddhena atikkantamānusakena",
                      "စင်ကြယ်၍ လူ၏ မျက်စိကို ကျော်လွန်သော နတ်မျက်စိဖြင့်")
CUTUPAPATA = witness("4", "^4-184", "cavamāne upapajjamāne hīne paṇīte suvaṇṇe dubbaṇṇe, sugate duggate",
                     "သေဆဲ၊ ဖြစ်ပေါ်ဆဲ၊ ယုတ်ညံ့သော၊ မွန်မြတ်သော၊ အဆင်း လှသော၊ အဆင်း ဆိုးသော၊ ကောင်းသော လားရာ "
                     "ရှိသော၊ ဆိုးသော လားရာ ရှိသော")
YATHAKAMMA = witness("4", "^4-184", "yathākammūpage satte pajānāti",
                     "ကံအားလျော်စွာ ရောက်သွားကြသော သတ္တဝါတို့ကို ကွဲပြားစွာ သိ")
PUBBENIVASA = witness("4", "^4-183", "pubbenivāsaṃ anussarati", "ရှေးဘဝများကို အဖန်ဖန် အောက်မေ့")
PARACITTA = witness("2", "^2-805", "paracitte ñāṇaṃ", "အခြားသူ၏ စိတ်ကို သိ")
ASAVAKHAYA = witness("2", "^2-805", "āsavānaṃ khaye ñāṇaṃ", "စိတ်အစွန်းအထင်းတို့ ကုန်ခန်းခြင်း")
IDDHI = witness("2", "^2-805", "Iddhividhe ñāṇaṃ", "ဣဒ္ဓိ")
SOTADHATU_DIBBA = "နတ်နား ဓာတ်ဖြင့်"                         # dibbāya sotadhātuyā (sotadhātu = «နား ဓာတ်», pi-2)
witness("2", "^2-805", "sotadhātuvisuddhiyā ñāṇaṃ", "နား ဓာတ်")
KAYANUPASSI = witness("2", "^2-205", "kāye kāyānupassī viharati", "ကိုယ်၌ ကိုယ်ကို အဖန်ဖန် ရှုသူ ဖြစ်လျက်")
VEDANANUPASSI = witness("2", "^2-487", "vedanāsu vedanānupassī viharati", "ခံစားမှုတို့၌ ခံစားမှုကို အဖန်ဖန် ရှုသူ")
CITTANUPASSI = witness("2", "^2-487", "citte cittānupassī viharati", "စိတ်၌ စိတ်ကို အဖန်ဖန် ရှုသူ")
DHAMMANUPASSI = "သဘောတရားတို့၌ သဘောတရားကို အဖန်ဖန် ရှုသူ"      # dhammesu dhammānupassī (pi-2 ^2-487 pattern)
witness("2", "^2-487", "dhammesu dhammānupassī viharati", DHAMMANUPASSI)
DUKKHA_END = witness("4", "^4-31", "dukkhassantaṃ karoti", "ဒုက္ခ၏ အဆုံးကို ပြု")
SAMMADITTHI = witness("1", "^1-1", "sammādiṭṭhi hoti", "မှန်ကန်သော အယူ")
PANATIPATA = witness("2", "^2-487", "Pāṇātipātā veramaṇī", "သူ့အသက်ကို သတ်ခြင်း")
MANUSSA = witness("2", "^2-974", "manussosmīti", "လူ")
DEVA = witness("2", "^2-974", "devosmīti", "နတ်")
NERAYIKA = witness("2", "^2-1009", "nerayikānaṃ", "ငရဲသား")
TIRACCHANA = witness("2", "^2-1009", "tiracchānagatānaṃ", "တိရစ္ဆာန်")
PETA = witness("2", "^2-1009", "petānaṃ", "ပြိတ္တာ")
SANGHA = witness("2", "^2-932", "saṅghaṃ vā", "သံဃာ")


# ===================================================================================== headings and colophons
HEAD = {
    "Abhidhammapiṭake": ABHI,
    "Kathāvatthupāḷi": TITLE,
    "Suddhasaccikaṭṭho": f"ရိုးရိုး {SACCIKATTHA_W}",
    "Anulomapaccanīkaṃ": "အစဉ်အတိုင်းနှင့် ပြောင်းပြန်",
    "Paccanīkānulomaṃ": "ပြောင်းပြန်နှင့် အစဉ်အတိုင်း",
    "(Ka) okāsasaccikaṭṭho": f"(က) နေရာနှင့် ဆိုင်သော {SACCIKATTHA_W}",
    "(Ka) kālasaccikaṭṭho": f"(က) အချိန်နှင့် ဆိုင်သော {SACCIKATTHA_W}",
    "(Ka) avayavasaccikaṭṭho": f"(က) အစိတ်အပိုင်းနှင့် ဆိုင်သော {SACCIKATTHA_W}",
    "(Kha) okāsasaccikaṭṭho": f"(ခ) နေရာနှင့် ဆိုင်သော {SACCIKATTHA_W}",
    "(Kha) kālasaccikaṭṭho": f"(ခ) အချိန်နှင့် ဆိုင်သော {SACCIKATTHA_W}",
    "(Kha) avayavasaccikaṭṭho": f"(ခ) အစိတ်အပိုင်းနှင့် ဆိုင်သော {SACCIKATTHA_W}",
}
KATHA_W = "ဆွေးနွေးချက်"                                   # kathā (a debate / discussion)
ANUYOGA_W = "စစ်ဆေးမေးမြန်းခြင်း"                          # anuyoga (an inquiry)
VAGGA_W = "ဝဂ်"                                            # vagga (a group of debates)
SECTION = {      # section names: heading (no end mark) = colophon (+ «။») when the colophon only repeats the name
    "Puggalakathā": f"ပုဂ္ဂိုလ်အကြောင်း {KATHA_W}",
    "Suddhikasaṃsandanaṃ": "ရိုးရိုး နှိုင်းယှဉ်ခြင်း",
    "Suddhikasaṃsandanā": "ရိုးရိုး နှိုင်းယှဉ်ခြင်း",
    "Opammasaṃsandanaṃ": "ဥပမာဖြင့် နှိုင်းယှဉ်ခြင်း",
    "Catukkanayasaṃsandanaṃ": "နည်း လေးပါးဖြင့် နှိုင်းယှဉ်ခြင်း",
    "Lakkhaṇayuttikathā": f"လက္ခဏာနှင့် ယုတ္တိအကြောင်း {KATHA_W}",
    "Vacanasodhanaṃ": "စကားလုံးကို စိစစ်ခြင်း",
    "Paññattānuyogo": f"{PANNATTI}ကို {ANUYOGA_W}",
    "Gatianuyogo": f"လားရာကို {ANUYOGA_W}",
    "Upādāpaññattānuyogo": f"မှီ၍ {PANNATTI}ကို {ANUYOGA_W}",
    "Purisakārānuyogo": f"လူ၏ ပြုလုပ်မှုကို {ANUYOGA_W}",
    "Abhiññānuyogo": f"ထူးကဲစွာ သိခြင်းကို {ANUYOGA_W}",
    "15-18. Ñātakānuyogādi": f"15-18. ဆွေမျိုးကို {ANUYOGA_W} စသည်",
    "Paṭivedhānuyogo": f"ထိုးထွင်း သိမြင်ခြင်းကို {ANUYOGA_W}",
    "Saṅghānuyogo": f"{SANGHA}ကို {ANUYOGA_W}",
    "Saccikaṭṭhasabhāgānuyogo": f"{SACCIKATTHA_W}နှင့် တူညီခြင်းကို {ANUYOGA_W}",
}
witness("2", "^2-805", "chasu abhiññāsu", "ထူးကဲစွာ သိခြင်း")       # abhiññā (pi-2)
witness("2", "^2-U58", "duggatiṃ", "လားရာ")                           # gati (pi-2 «ဆိုးသော လားရာ»)
HEAD.update(SECTION)
VAGGA_NAME = {"Kalyāṇa": "“ကောင်းမွန်သော”"}                       # Kalyāṇavaggo (named after kalyāṇa, pi-4 kalyāṇa)


def vagga_end(name, n):       # Kalyāṇavaggo paṭhamo.
    return f"{ORD_MY[n]} {VAGGA_NAME[name]} {VAGGA_W}"


COLO = {f"{k} niṭṭhitā": DONE.format(v) for k, v in SECTION.items()}
COLO.update({k: v for k, v in SECTION.items()})
COLO.update(CLOSE)


# ===================================================================================== brackets
PATHA, LEKHANA = "ပါဌ်ကွဲ", "စာလုံးပေါင်းကွဲ"                     # variant labels (pi-1 style rules)
witness("1", "^1-M2-142", "suttantamātikā (syā.)", f"[{PATHA} (Syā.): suttantamātikā]")
witness("1", "^1-M2-126", "paṭisandhāro ca (ka.)", f"[{LEKHANA} (Ka.): paṭisandhāro ca]")
SIGLA = {"sī.": "Sī.", "syā.": "Syā.", "ka.": "Ka.", "pī.": "Pī.", "kaṃ.": "Kaṃ.", "bahūsu": "အများစု၌", "?": "မသေချာ"}
REF = {"a. ni.": "“အင်္ဂုတ္တရနိကာယ်”", "ma. ni.": "“မဇ္ဈိမနိကာယ်”", "dī. ni.": "“ဒီဃနိကာယ်”",
       "saṃ. ni.": "“သံယုတ္တနိကာယ်”", "itivu.": "“ဣတိဝုတ်”", "su. ni.": "“သုတ္တနိပါတ်”",
       "cūḷani.": "“စူဠနိဒ္ဒေသ”", "dha. pa.": "“ဓမ္မပဒ”", "pu. pa.": f"“{TITLE4}”",
       "pu. pa. mātikā": f"“{TITLE4}” {heads('Mātikā')}"}
witness("2", "^2-760", "ma. ni. 1.148", f"{REF['ma. ni.']} 1.148")
VAR_KIND = {     # the variant's Pāli -> word variant (PATHA) or spelling only (LEKHANA)
    "saccikaṭṭhaparamaṭṭhenāti": LEKHANA, "no vata re": PATHA, "tvaṃ": PATHA, "suniggahitova": PATHA,
    "hevameva": LEKHANA, "dunniggahitāva": PATHA, "aññātāvindriyañca": PATHA, "mahiso": LEKHANA,
    "anamataggāyaṃ": LEKHANA, "bāvīsatiyā": PATHA, "cattāro": PATHA, "kāyasakkhī": LEKHANA,
    "katamāni tīṇi": PATHA, "ohacca": LEKHANA, "uhacca": LEKHANA, "yathāpi": PATHA, "sammati": LEKHANA,
    "dukkhaṃ": PATHA, "anupalabbhamāne": LEKHANA, "yamidaṃ": PATHA, "yampitaṃ": PATHA,
}
REF_NOTE = {     # editors' remarks after a reference -> Burmese
    "itivuttakepi": f"{REF['itivu.']}၌လည်း",
    "thokaṃ visadisaṃ": "အနည်းငယ် ကွဲပြားသည်",
    "ālapanamattameva nānaṃ": "ခေါ်ဝေါ်ပုံသာ ကွဲပြားသည်",
    "dhammapade": f"{REF['dha. pa.']}၌",
    "mogharājamāṇavapucchāniddesa": "မောဃရာဇ လုလင်၏ အမေးကို ဖွင့်ဆိုချက်",
    "puggalapaññattiyaṃ": f"{REF['pu. pa.']}၌",
    "atthato ekaṃ": "အဓိပ္ပာယ်အားဖြင့် တူသည်",
}
_REF_RE = re.compile(r"(?P<r>pu\. pa\. mātikā|a\. ni\.|ma\. ni\.|dī\. ni\.|saṃ\. ni\.|itivu\.|su\. ni\.|"
                     r"cūḷani\.|dha\. pa\.|pu\. pa\.) (?P<n>[\d.\-]+)")
_READ_RE = re.compile(r"(?P<t>[^\[\](),;]+?) \((?P<s>[^()]+)\)")


def _ref_my(s):
    """«saṃ. ni. 2.133; itivu. 24 itivuttakepi» -> «“…” 2.133၊ “…” 24၊ …» (references and the remarks after them)."""
    out, pos = [], 0
    s = s.strip()
    while pos < len(s):
        m = _REF_RE.match(s, pos)
        if m:
            out.append(f"{REF[m['r']]} {m['n']}")
            pos = m.end()
        else:
            for k, v in REF_NOTE.items():
                if s.startswith(k, pos):
                    out.append(v)
                    pos += len(k)
                    break
            else:
                raise Miss("reference: " + s)
        for sep in ("; ", ", ", " "):
            if s.startswith(sep, pos):
                pos += len(sep)
                break
    return f"{C} ".join(out)


def _sig_my(s):
    """«syā. pī.» -> «Syā., Pī.»; «a. ni. 3.47» (a reference as siglum) -> «“…” 3.47»."""
    if _REF_RE.fullmatch(s):
        return _ref_my(s)
    parts = re.findall(r"kaṃ\.|[a-zāīū]+\.|bahūsu|\?", s)
    if " ".join(parts) != s:
        raise Miss("sigla: " + s)
    return ", ".join(SIGLA[x] for x in parts)


BR_TABLE = {     # whole brackets that no rule builds
    "[(āmantā) (?) evaṃ anantaravārattayepi]": f"[({YES}) (မသေချာ) နောက်ဆက်တွဲ အကြိမ် သုံးကြိမ်၌လည်း ဤနည်းတူ]",
}


def bracket_my(br):
    """One bracket of the Pāli -> Burmese: editorial note, references, variant readings (pi-1 label style)."""
    if br in BR_TABLE:
        return BR_TABLE[br]
    body = br[1:-1]
    if body in NOTE:
        return f"[{NOTE[body]}]"
    if _REF_RE.match(body):
        return f"[{_ref_my(body)}]"
    note = ""
    if body.endswith(" ṭīkā oloketabbā"):
        body, note = body[:-len(" ṭīkā oloketabbā")], NOTE["ṭīkā oloketabbā"]
    reads = list(_READ_RE.finditer(body))
    pos, parts = 0, []
    for rm in reads:
        if body[pos:rm.start()].strip(" ,") != "":
            raise Miss("variant: " + br)
        pos = rm.end()
        t = rm["t"].strip()
        if t not in VAR_KIND:
            raise Miss("variant kind: " + br)
        parts.append((VAR_KIND[t], _sig_my(rm["s"]), t))
    if not parts or body[pos:].strip():
        raise Miss("variant: " + br)
    k0, s0, t0 = parts[0]
    out = [f"{k0} ({s0}): {t0}"] + [f"({s}): {t}" for _, s, t in parts[1:]] + ([note] if note else [])
    return "[" + f"{C} ".join(out) + "]"


# ===================================================================================== propositions
PROP = {}        # canonical Pāli proposition (lower case first letter, no quotes / brackets / final «ti») -> Cl
RULES = []       # (compiled regex on a canonical proposition, function(match) -> Cl)


def rule(rx):
    def deco(fn):
        RULES.append((re.compile(rx), fn))
        return fn
    return deco


def _cands(p):
    """Candidate canonical forms of a Pāli proposition: as is; final «n» (from «nti») -> «ṃ»; long final vowel
    shortened (from «āti» / «īti» / «ūti»); and the same after removing a final «ti» (a part «…tīti,»)."""
    p = p.strip()
    out = [p]
    if p.endswith("ti"):
        out.append(p[:-2])
    res = []
    for x in out:
        res.append((x, x is not p))
        if x.endswith("n"):
            res.append((x[:-1] + "ṃ", x is not p))
        for a, b in (("ā", "a"), ("ī", "i"), ("ū", "u")):
            if x.endswith(a):
                res.append((x[:-1] + b, x is not p))
    return res


def lookup(p):
    """A canonical proposition -> (Cl, had_ti) from PROP or RULES, else None."""
    for x, had_ti in _cands(p):
        k = x[:1].lower() + x[1:]
        if k in PROP:
            return PROP[k], had_ti
        for rx, fn in RULES:
            m = rx.fullmatch(k)
            if m:
                r = fn(m)
                if r is not None:
                    return r, had_ti
    return None


SEP_RE = re.compile(r"(, |; |… )")
SERIES_FORM = {"q": "q", "stmt": "stmt", "bare": "bare", "nanu": "stmt", "cond": "bare", "rel": "rel"}


def norm_pe(s):
    """«…pe…» -> «…»; « …» -> «…» (one ellipsis per Pāli ellipsis)."""
    s = s.replace("…pe…", "…").replace("…Pe…", "…")
    return re.sub(r" …", "…", s)


def prop_my(p, form="stmt", depth=0):
    """Translate a (possibly compound) proposition. A compound is cut at «, » / «; » / «… » into the longest known
    parts; non-final parts before «, » / «; » are statements («…ဟူ၍» when the Pāli part ends in «ti»), parts before
    «…» take the series form of the whole (bare forms when a «, » / «; » part still follows the series)."""
    p = norm_pe(p.strip())
    if p.endswith("…"):
        raise Miss("prop ends in …: " + p)
    hit = lookup(p)
    if hit:
        return hit[0].f(form, depth)
    parts = SEP_RE.split(p)
    toks, seps = parts[0::2], parts[1::2]
    out, i = [], 0
    while i < len(toks):
        for j in range(len(toks), i, -1):
            cand = toks[i]
            for k in range(i + 1, j):
                cand += seps[k - 1] + toks[k]
            hit = lookup(cand)
            if hit:
                cl, had_ti = hit
                last = j == len(toks)
                if last:
                    out.append(cl.f(form, depth))
                else:
                    sep = seps[j - 1]
                    if sep == "… ":
                        later = any(x in (", ", "; ") for x in seps[j:])
                        out.append(cl.f("bare" if later else SERIES_FORM[form], depth) + "… ")
                    else:
                        txt = cl.f("stmt", depth) + ("ဟူ၍" if had_ti else "")
                        out.append(txt + C + " ")
                i = j
                break
        else:
            raise Miss("proposition: " + p + "  ‖  part: " + toks[i])
    return "".join(out)


def pq(p, form, depth=0):
    """prop_my() for a frame slot (the Pāli slot may still carry its final «ti»)."""
    return prop_my(p, form, depth)


# --- the Puggalakathā proposition and its correlative (the first debate; recurring in later kathās)
for _neg, _pf in ((False, ""), (True, "n")):
    PROP[f"yo saccikaṭṭho paramattho, tato so puggalo {_pf}upalabbhati saccikaṭṭhaparamatthena"] = V(
        f"{FACT_AS} ထို{PUGGALA}ကို {SACC}", FOUND, _neg)

# --- the shared clause rules (nouns × the Puggalakathā predicates)
_UPAL = r"(?P<neg>n)?upalabbh(?:ati|anti)(?P<s> saccikaṭṭhaparamatthena)?"


@rule(r"(?P<w>sabbattha |sabbadā |sabbesu )?(?P<x>.+?) " + _UPAL)
def _r_found(m):
    """X (ca) (n)upalabbhati (saccikaṭṭhaparamatthena); sabbattha / sabbadā / sabbesu X …"""
    x = m["x"]
    n = noun(x, "ca") or noun(x, "nom")
    if n is None:
        return None
    ca = noun(x, "ca") is not None and noun(x, "nom") is None
    pre = WHERE[m["w"].strip()] if m["w"] else ""
    return found_cl(n, ca=ca, full=bool(m["s"]), neg=bool(m["neg"]), pre=pre)


@rule(r"aññ(?:aṃ|o|ā|e) (?P<a>[^,]+?),? aññ(?:aṃ|o|ā|e) (?P<b>[^,]+?)(?:,? añño (?P<c>.+))?")
def _r_other(m):
    """aññaṃ A añño B (añño C): «Aနှင့် Bသည် တခြားစီ ဖြစ်» (pi-1 pattern)."""
    ns = [noun(m["a"], "nom"), noun(m["b"], "nom")] + ([noun(m["c"], "nom")] if m["c"] else [])
    if None in ns:
        return None
    return other_cl(*ns)


@rule(r"(?P<a>\S+) puggalo")
def _r_is(m):
    """X puggalo (X is the person) / Xsmiṃ puggalo (the person is in X)."""
    n = noun(m["a"], "nom")
    if n is not None and n is not PUG:
        return V(f"{n.my}သည် {PUGGALA}")
    n = noun(m["a"], "loc")
    if n is not None:
        return V(f"{n.my}၌ {PUGGALA}", "ရှိ")
    return None


@rule(r"aññatra (?P<a>\S+) puggalo")
def _r_apart(m):
    n = noun(m["a"], "abl")
    return V(f"{n.my}မှ အခြား၌ {PUGGALA}", "ရှိ") if n else None


@rule(r"puggalasmiṃ (?P<a>\S+)")
def _r_in(m):
    n = noun(m["a"], "nom")
    return V(f"{PUGGALA}၌ {n.my}", "ရှိ") if n else None


@rule(r"(?P<a>\S+) upādāya(?P<p> puggalassa paññatti)?")
def _r_upadaya(m):
    """X upādāya (puggalassa paññatti): «Xကို မှီ၍ (ပုဂ္ဂိုလ်၏ သတ်မှတ်ချက် ရှိ)»."""
    n = noun(m["a"], "acc")
    if n is None:
        return None
    if m["p"]:
        return V(f"{n.my}{UPADAYA} {PUGGALA}၏ {PANNATTI}", "ရှိ")
    return FR(f"{n.my}{UPADAYA}")


@rule(r"vuttaṃ bhagavatā – (?P<x>.+)")
def _r_vutt(m):
    """vuttaṃ bhagavatā – "X" inside a proposition (X from the QUOTE table)."""
    try:
        return vutt_cl(QUOTE_RAW(m["x"]))
    except Miss:
        return None


# ===================================================================================== the dialectic frames
def claim(p, q, depth):
    """vattabbe kho – ‘P,’ no ca vattabbe – ‘Q’ (the claim standing at depth; P, Q quoted one level down)."""
    o, c = mark(depth + 1)
    s = f"{SAY} – {o}{pq(p, 'stmt', depth + 1)}{c}"
    if q is None:
        return s
    return s + f"{C} {NOT_SAY} – {o}{pq(q, 'stmt', depth + 1)}{c}"


def if_my(p, q, depth=0, neg=False, alt=False):
    """Hañci P, tena vata re vattabbe – "Q"ti. (neg: Hañci P; no ca vata re vattabbe – "Q"ti.)"""
    o, c = mark(depth + 1)
    pre = "သို့မဟုတ် အကယ်၍" if alt else "အကယ်၍"
    say = "အမှန်ပင် ဤသို့လည်း မဆိုသင့်" if neg else f"ထို့ကြောင့် အမှန်ပင် {SAY}"
    cond = pq(p, "cond", depth)
    if not cond.endswith("လျှင်"):            # a condition ending in a quotation: a break before the consequence
        cond += C
    return f"{pre} {cond} {say} – {o}{pq(q, 'stmt', depth + 1)}{c}"


def ifnot_my(q, p, depth=0):
    """No ce pana vattabbe – "Q"ti, no ca vata re vattabbe – "P"ti."""
    o, c = mark(depth + 1)
    return (f"တစ်ဖန် အကယ်၍ ဤသို့ မဆိုသင့်လျှင် – {o}{pq(q, 'stmt', depth + 1)}{c}{C} "
            f"အမှန်ပင် ဤသို့လည်း မဆိုသင့် – {o}{pq(p, 'stmt', depth + 1)}{c}")


def yam_my(p, q, te=False, depth=0):
    """Yaṃ tattha vadesi – "vattabbe kho – ‘P,’ no ca vattabbe – ‘Q’"ti (idaṃ te) micchā."""
    o, c = mark(depth + 1)
    return f"ထိုအရာ၌ သင်ပြောသော စကား – {o}{claim(p, q, depth + 1)}{c}{WRONG_TE if te else WRONG}"


AJ = {"niggahaṃ": f"{NIGGAHA}ကို လက်ခံလော့", "paṭikammaṃ": f"{PATIKAMMA}ကို လက်ခံလော့"}
TAIL = {  # Tena hi ye kate niggahe se niggahe dukkaṭe. Sukate paṭikamme. Sukatā paṭipādanāti.
    "Tena hi ye kate niggahe se niggahe dukkaṭe.":
        f"သို့ဖြစ်၍ ပြုခဲ့သော {NIGGAHA}တို့သည် မကောင်းစွာ ပြုခဲ့သော {NIGGAHA}တို့ ဖြစ်သည်{END}",
    "Sukate paṭikamme.": f"{PATIKAMMA}ကို ကောင်းစွာ ပြုခဲ့သည်{END}",
    "Sukatā paṭipādanāti.": f"ဆက်စပ် တင်ပြချက်ကို ကောင်းစွာ ပြုခဲ့သည်{END}",
}
TVAM_TAIL = (f"ထိုအရာ၌ သင်၏ ထိုဝန်ခံချက်ဖြင့် ဤသို့ ဝန်ခံနေသော သင့်ကို ဤသို့ ချေပရမည်{END} "
             f"ထို့ကြောင့် ငါတို့သည် သင့်ကို ချေပကြသည်{END} သင်သည်လည်း ကောင်းစွာ ချေပခြင်း ခံရသည်{END}")
ESE_HEAD = f"အကယ်၍ ဤသည် မကောင်းစွာ ချေပခြင်း ဖြစ်လျှင် ထိုအရာ၌ ဤနည်းအတိုင်းပင် ရှုလော့{END}"
ESE_TAIL = (f"ထိုအရာ၌ ထိုဝန်ခံချက်ဖြင့် ဤသို့ ဝန်ခံနေသော ငါတို့ကို သင်သည် ဤသို့ မချေပရ{END} "
            f"သို့သော် သင်သည် ငါ့ကို ချေပသည်{END} ငါတို့သည်လည်း မကောင်းစွာ ချေပခြင်း ခံရသည်{END}")
NA_HEAD = f"ဤသို့ မချေပရ{END}"                                   # Na hevaṃ niggahetabbe.

KATVA = "ဟု အကြောင်းပြု၍"                                        # …ti katvā
TENA_CA = "ထိုအကြောင်းကြောင့်လည်း"                                # tena ca kāraṇena
TENEVA = "ထိုအကြောင်းကြောင့်ပင်"                                   # teneva kāraṇena
ATTHEVA = f"ထိုသို့သော {SUTTANTA} အမှန်ပင် ရှိသလော"                # Attheva suttantoti?
TENA_HI = "သို့ဖြစ်လျှင်"                                          # Tena hi
VUTTA_PRE = f"{BHAGAVA} ဤသို့ ဟောတော်မူ"                          # vuttaṃ bhagavatā – (verb stem)


def vutt_cl(quote_my):
    """vuttaṃ bhagavatā – "X" as a clause: «မြတ်စွာဘုရား ဤသို့ ဟောတော်မူ(သည်) – «X»» (X = Burmese, its own
    inner quotes written with ‹…›)."""
    return Cl(f"{BHAGAVA} ဤသို့", "ဟောတော်မူ", "မဟောတော်မူ", post=f" – «{quote_my}»")


QUOTE = {       # Pāli quotation (no quotes, no brackets) -> Burmese (its own inner quotes written ‹…›)
    "atthi puggalo attahitāya paṭipanno": f"{ATTAHITA_PUG} ရှိသည်",      # pu. pa. mātikā 4.24 (pi-4 wording)
}


def quote_my(pali, depth):
    k = norm_pe(pali.strip())
    if k not in QUOTE:
        raise Miss("quotation: " + k)
    return q_set(QUOTE[k], depth)


SENT = dict(TAIL, **{"Namo tassa bhagavato arahato sammāsambuddhassa": NAMO})  # whole sentence (no quotes / brackets, «…pe…» as «…») -> Burmese with its end mark
LINES = {}       # whole line (no quotes / brackets) -> Burmese line (brackets: ⟦n⟧ placeholders or appended)
FRAMES = []      # (compiled regex on a sentence without quotes / brackets, function(match) -> Burmese)
LINE_FRAMES = []  # (compiled regex on a whole line without quotes / brackets, function(match) -> Burmese)


def frame(rx, line=False):
    def deco(fn):
        (LINE_FRAMES if line else FRAMES).append((re.compile(rx), fn))
        return fn
    return deco


E_RX = r"(?P<e>\.…\.?|…\.?|\.|)"       # sentence end after «…pe…» folding: «.», «…», «….», «.…», «.….», none


def endmark(e):
    """«.» -> «။»; «…» / «….» -> «…» (the full stop goes); «.…» / «.….» -> «။ …»; none -> «။»."""
    if "…" in e:
        return END + " " + PE if e.startswith(".") else PE
    return END


@frame(r"Āmantā(?:\?|" + E_RX + ")")
def _f_yes(m):
    """Āmantā. / Āmantā…pe… / Āmantā? (a source slip, ^5-95: rendered as the statement)."""
    return YES + endmark(m["e"] or ".")


@frame(r"Na hevaṃ vattabbe" + E_RX)
def _f_no(m):
    return NO_SAY + endmark(m["e"])


@frame(r"Vattabbaṃ\.")
def _f_say(m):
    return SAY_ANS + END


@frame(r"Ājānāhi (?P<k>niggahaṃ|paṭikammaṃ)\.")
def _f_aj(m):
    return AJ[m["k"]] + END


@frame(r"(?P<h>[Hh])añci (?P<alt>vā pana )?(?P<p>.+?)[,;] (?P<neg>tena|no ca) vata re vattabbe – (?P<q>.+?)ti\.")
def _f_if(m):
    return if_my(m["p"], m["q"], neg=m["neg"] == "no ca", alt=bool(m["alt"])) + END


@frame(r"Yaṃ tattha vadesi – vattabbe kho – (?P<p>.+?)(?:, no ca vattabbe – (?P<q>.+?))?ti (?P<te>idaṃ te )?"
       r"micchā" + E_RX)
def _f_yam(m):
    return yam_my(m["p"], m["q"], te=bool(m["te"])) + endmark(m["e"])


@frame(r"(?P<p>[^–]+?)ti micchā" + E_RX)
def _f_miccha(m):
    """P-ti micchā (a statement called wrong, ^5-78)."""
    return f"{pq(m['p'], 'stmt')} ဟူသည် မှားသည်" + endmark(m["e"])


@frame(r"No ce pana vattabbe – (?P<q>.+?)ti, no ca vata re vattabbe – (?P<p>.+?)ti\.")
def _f_ifnot(m):
    return ifnot_my(m["q"], m["p"]) + END


@frame(r"(?P<k>Anulomapañcakaṃ|Paccanīkapañcakaṃ|Paṭikammacatukkaṃ|Niggahacatukkaṃ|Upanayanacatukkaṃ|"
       r"Niggamanacatukkaṃ|Aṭṭhakaniggaho)\.")
def _f_close(m):
    return CLOSE[m["k"]] + END


@frame(r"(?P<o>Paṭhamo|Dutiyo|Tatiyo|Catuttho|Pañcamo|Chaṭṭho|Sattamo|Aṭṭhamo) niggaho\.")
def _f_ord(m):
    return niggaho_my(ORD_PI[m["o"].lower()]) + END


@frame(r"Na vattabbaṃ – (?P<p>.+?)ti\?")
def _f_navatt(m):
    return f"ဤသို့ မဆိုသင့်သလော – “{pq(m['p'], 'stmt', 1)}”{END}"


@frame(r"(?P<t>[Tt])ena hi (?P<na>na vattabbaṃ – )?(?P<p>.+?)(?:ti)?\.")
def _f_tenahi(m):
    if m["na"]:
        return f"{TENA_HI} ဤသို့ မဆိုသင့် – “{pq(m['p'], 'stmt', 1)}”{END}"
    return f"{TENA_HI} {pq(m['p'], 'stmt')}{END}"


@frame(r"(?P<pre>(?:\S+ upādāya… )*)(?P<a>\S+) upādāya (?P<b>.+?)ti vattabboti\?")
def _f_vattabbo(m):
    """(series) X upādāya "B puggalo"ti vattabboti? = «Xကို မှီ၍ “B”ဟု ဆိုသင့်သလော»."""
    pre = "".join(prop_my(x.strip(), "bare") + "… " for x in m["pre"].split("… ") if x.strip())
    return f"{pre}{prop_my(m['a'] + ' upādāya', 'bare')} “{pq(m['b'], 'stmt', 1)}”ဟု ဆိုသင့်သလော{END}"


@frame(r"(?P<a>\S+) (?:niruddhe|niruddhāya) (?P<b>.+?)ti vattabboti\?")
def _f_niruddhe(m):
    """X-mhi niruddhe "B niruddho"ti vattabboti? = «X ချုပ်ငြိမ်းသွားသောအခါ “B”ဟု ဆိုသင့်သလော»."""
    n = noun(m["a"][:1].lower() + m["a"][1:], "loc")
    if n is None:
        raise Miss("niruddhe: " + m["a"])
    return f"{n.my} ချုပ်ငြိမ်းသွားသောအခါ “{pq(m['b'], 'stmt', 1)}”ဟု ဆိုသင့်သလော{END}"


@frame(r"(?P<x>[^;]+); tena hi (?P<p>.+?)ti\.")
def _f_x_tenahi(m):
    """X; tena hi P-ti. (^5-214)"""
    return f"{pq(m['x'], 'stmt')}{C} {TENA_HI} {pq(m['p'], 'stmt')}{END}"


@frame(r"(?P<n>[A-ZĀĪŪ]\S+)vaggo (?P<o>paṭhamo|dutiyo|tatiyo|catuttho|pañcamo|chaṭṭho|sattamo|aṭṭhamo|navamo|dasamo)\.")
def _f_vagga_end(m):
    """Kalyāṇavaggo paṭhamo. (a vagga colophon, the vagga named by VAGGA_NAME)"""
    if m["n"] not in VAGGA_NAME:
        raise Miss("vagga name: " + m["n"])
    return vagga_end(m["n"], ORD_PI[m["o"]]) + END


@frame(r"Attheva suttantoti\?")
def _f_attheva(m):
    return ATTHEVA + END


@frame(r"Nanu (?P<p>.+?)ti\?")
def _f_nanu(m):
    return pq(m["p"], "nanu") + END


@frame(r"(?P<n>Nanu )?[Vv]uttaṃ bhagavatā – (?P<x>.+?)ti(?P<e>[.?!])")
def _f_vutt(m):
    """(Nanu) vuttaṃ bhagavatā – "QUOTE"ti?/!/. with a quotation of the QUOTE table."""
    cl = vutt_cl(QUOTE_RAW(m["x"]))
    form = "nanu" if m["n"] else ("q" if m["e"] == "?" else "stmt")
    return cl.f(form, 0) + END


def QUOTE_RAW(pali):
    k = norm_pe(pali.strip())
    for x, _ in _cands(k):
        if x in QUOTE:
            return QUOTE[x]
    raise Miss("quotation: " + k)


@frame(r"(?P<x>.+?)ti katvā (?P<k>tena ca kāraṇena|teneva kāraṇena) (?P<p>.+?)ti\?")
def _f_katva(m):
    return (f"{pq(m['x'], 'stmt')}{KATVA} {TENA_CA if m['k'].startswith('tena ca') else TENEVA} "
            f"{pq(m['p'], 'q')}{END}")


@frame(r"(?P<x>.+?)ti katvā\?")
def _f_katva_q(m):
    return f"{pq(m['x'], 'stmt')}ဟု အကြောင်းပြုသလော{END}"


# the multi-sentence lines (matched on the whole line before it is cut into sentences)
@frame(r"Tvaṃ ce pana maññasi – vattabbe kho – (?P<p>.+?), no ca vattabbe – (?P<q>.+?)ti, tena tava tattha hetāya "
       r"paṭiññāya hevaṃ paṭijānantaṃ hevaṃ niggahetabbe\. Atha taṃ niggaṇhāma\. Suniggahito ca hosi\.", line=True)
def _l_tvam(m):
    return f"တစ်ဖန် အကယ်၍ သင်သည် ဤသို့ ထင်လျှင် – “{claim(m['p'], m['q'], 1)}”{C} {TVAM_TAIL}"


@frame(r"Ese ce dunniggahite hevamevaṃ tattha dakkha\. Vattabbe kho – (?P<p>.+?), no ca vattabbe – (?P<q>.+?)ti\. "
       r"No ca mayaṃ tayā tattha hetāya paṭiññāya hevaṃ paṭijānantā hevaṃ niggahetabbā\. Atha maṃ niggaṇhāsi\. "
       r"Dunniggahitā ca homa\.", line=True)
def _l_ese(m):
    return f"{ESE_HEAD} {claim(m['p'], m['q'], 0)}{END} {ESE_TAIL}"


@frame(r"Na hevaṃ niggahetabbe\. Tena hi yaṃ niggaṇhāsi – hañci (?P<p>.+?), tena vata re vattabbe – (?P<q>.+?)ti\. "
       r"Yaṃ tattha vadesi – vattabbe kho – (?P<p2>.+?), no ca vattabbe – (?P<q2>.+?)ti micchā\.", line=True)
def _l_na(m):
    if (m["p"], m["q"]) != (m["p2"], m["q2"]):
        raise Miss("NA frame: P / Q differ")
    return (f"{NA_HEAD} သို့ဖြစ်၍ သင် ချေပသည်မှာ – “{if_my(m['p'], m['q'], depth=1)}{END} "
            f"{yam_my(m['p'], m['q'], depth=1)}”{END}")


# the generic frames (tried last)
@frame(r"(?P<p>.+?)(?:ti)?\?")
def _f_q(m):
    """P-ti? (a question)."""
    return pq(m["p"], "q") + END


@frame(r"(?P<p>.+?)(?:ti)?" + E_RX)
def _f_stmt(m):
    """A bare elided series or a statement: «…pe….» -> bare forms + «…»; «.» -> a statement + «။»."""
    if "…" in m["e"]:
        return pq(m["p"], "bare") + endmark(m["e"])
    return pq(m["p"], "stmt") + END


# ===================================================================================== the engine
HEAD_RE = re.compile(r"(?P<h>#+) (?P<t>.+)$")
BR_RE = re.compile(r" ?\[[^\]]*\]")
QUOTES = '"‘’“”'


def strip_q(s):
    return s.translate({ord(c): None for c in QUOTES})


def split_sents(s):
    """Cut a line (no brackets; quotes kept) into sentences: after «. » «? » «! » before a capital / quote / «(»
    at even «"» parity, and after «vattabbe…pe… » / «Āmantā…pe… » / «micchā…pe… » before a small letter.
    Returns (start, end) spans."""
    spans, start, par = [], 0, 0
    i = 0
    n = len(s)
    while i < n:
        ch = s[i]
        if ch == '"':
            par ^= 1
        if par == 0 and ch in ".?!" and i + 1 < n and s[i + 1] == " ":
            nxt = s[i + 2:i + 3]
            if nxt and (nxt.isupper() or nxt in "\"‘(“"):
                spans.append((start, i + 1))
                start = i + 2
                i += 2
                continue
        if par == 0 and s.startswith("…pe… ", i):
            left = s[start:i]
            if re.search(r"(vattabbe ?|Āmantā|micchā)$", left) and s[i + 5:i + 6].islower():
                spans.append((start, i + 4))
                start = i + 5
                i += 5
                continue
        i += 1
    spans.append((start, n))
    return [(a, b) for a, b in spans if s[a:b].strip()]


ANCHOR = {}      # Pāli word before a bracket -> Burmese anchor after which the translated bracket goes


def place(my, brs):
    """Insert translated brackets into one Burmese unit: (offset_in_unit, pali_word_before, bracket_my)."""
    for off, word, bmy in brs:
        if off == 0:
            my = f"{bmy} {my}"
            continue
        if "⟦b⟧" in my:
            my = my.replace(" ⟦b⟧", " " + bmy, 1) if " ⟦b⟧" in my else my.replace("⟦b⟧", " " + bmy, 1)
            continue
        if word == "" and "( )" in my:
            i = my.index("( )") + 3
            my = my[:i] + " " + bmy + my[i:]
            continue
        a = ANCHOR.get(word)
        if a and my.count(a) == 1:
            i = my.index(a) + len(a)
            my = my[:i] + " " + bmy + my[i:]
            continue
        m = re.search(r"(။|…)?$", my)
        i = m.start() if m.group(0) else len(my)
        my = my[:i] + " " + bmy + my[i:]
    return my


def unit_my(u):
    """One sentence (quotes and brackets removed) -> Burmese (slots ⟦b⟧ without a bracket are dropped)."""
    return _unit_my(u)


def _unit_my(u):
    key = norm_pe(u.strip())
    if key in SENT:
        return SENT[key]
    if key.startswith("( ) "):
        return "( ) " + _unit_my(key[4:])
    for rx, fn in FRAMES:
        m = rx.fullmatch(key)
        if m:
            try:
                return fn(m)
            except Miss:
                continue
    raise Miss("sentence: " + key)


def line_my(body):
    """A line without its block ID -> Burmese."""
    m = HEAD_RE.fullmatch(body)
    if m:
        t = m["t"]
        if t not in HEAD:
            raise Miss("heading: " + body)
        return f"{m['h']} {HEAD[t]}"
    # brackets out, remembering where they were
    brs, clean, pos = [], "", 0
    for bm in BR_RE.finditer(body):
        clean += body[pos:bm.start()]
        word = re.findall(r"[^\W\d]+$", clean.rstrip())
        brs.append((len(clean), word[-1] if word else "", bracket_my(bm.group(0).strip())))
        pos = bm.end()
    clean += body[pos:]
    key = norm_pe(strip_q(clean))
    if key in LINES:
        val = LINES[key]
        for i, (_, _, b) in enumerate(brs):
            tok = f"⟦{i}⟧"
            if tok in val:
                val = val.replace(tok, b)
            else:
                val = place(val, [(1, "", b)])
        return val
    if key.rstrip(".") in COLO:
        return COLO[key.rstrip(".")] + END
    for rx, fn in LINE_FRAMES:
        lm = rx.fullmatch(key)
        if lm:
            return place(fn(lm), [(o if o == 0 else 1, w, b) for o, w, b in brs])
    out = []
    for a, b in split_sents(clean):
        u = clean[a:b].strip()
        ub = [(o - a if o > a else (0 if o == a else 1), w, br) for o, w, br in brs if a <= o <= b]
        my = place(unit_my(strip_q(u)), ub)
        if "⟦b⟧" in my:
            raise Miss("bracket slot without a bracket: " + u[:60])
        out.append(my)
    return " ".join(out)


def translate_line(line):
    if not line.strip():
        return line
    m = ID_RE.search(line)
    body, tail = (line[:m.start()], line[m.start():]) if m else (line, "")
    return line_my(body.strip()) + tail
