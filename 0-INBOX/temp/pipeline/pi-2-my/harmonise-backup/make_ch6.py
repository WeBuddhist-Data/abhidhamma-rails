"""Burmese zero-shot of pi-2 chapter 6 (Paṭiccasamuppādavibhaṅgo, «အကြောင်းတို့ကို မှီ၍ ဖြစ်ပေါ်ပုံကို ခွဲခြမ်းစိတ်ဖြာခြင်း»).

usage: python3 -I -X utf8 make_ch6.py
Every line is generated from the Pāli by translate_line() through the frames and tables below, built on the approved
sample module my2_formulas.py (imported read-only; its tables are only extended in memory here) and on the FINAL pi-1
Burmese: the pi-1 synonym lists, the cittuppāda openings and the jhāna openings are read from the pi-1 rails text
(AI_translation/burmese/pi-1-burmese-plain-rails_split_chapters) with their item counts asserted. A sentence no frame
or table entry matches stops the run (Miss); nothing is guessed. The chapter is written only when every line passed;
on a stop the failing line is printed (nothing else is written). Every string new in this chapter is in NEW (and in
notes-ch6.md). Writes no other file.
"""
import pathlib
import re
import sys
import unicodedata

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import my2_formulas as F  # noqa: E402

P = F.P1
Miss = F.Miss
T = F.T
C, END, PE = F.C, F.END, F.PE
DH, DHP = F.DH, F.DHP
ROOT = F.ROOT
PALI = ROOT / "AI_translation/pali/pi-2_split_chapters"
OUT = ROOT / "AI_translation/burmese/pi-2-burmese-plain-zeroshot_split_chapters"
NAME = "6-paticcasamuppadavibhango.md"
NEW = {}            # Pāli -> Burmese, every string new in this chapter (logged in the notes)


def new(p, m):
    if NEW.get(p, m) != m:
        raise SystemExit("new-term conflict " + p)
    NEW[p] = m
    return m


# ===================================================================================== pi-1 final text (read only)
ID = re.compile(r" \^[0-9A-Za-z-]+\s*$")
VAR_STRIP = re.compile(r" ?\[[^\]]*\]")


def _p1_lines():
    out = []
    for p in sorted(F.P1_PALI.glob("*.md")):
        pl = p.read_text(encoding="utf-8-sig").split("\n")
        bl = (F.P1_RAILS / p.name).read_text(encoding="utf-8").split("\n")
        out += [(p.name, ID.sub("", a), ID.sub("", b)) for a, b in zip(pl, bl)]
    return out


P1LINES = _p1_lines()
P1_ALL_MY = "\n".join(b for _, _, b in P1LINES)


def p1_find(rx):
    r = re.compile(rx)
    for _, a, b in P1LINES:
        if r.search(a):
            return a, b
    raise SystemExit("pi-1 line not found: " + rx)


def p1_has(s):
    if s not in P1_ALL_MY:
        raise SystemExit("not in the pi-1 Burmese: " + s)
    return s


def p1_items(rx, pali, start, take=None):
    """The Burmese items of a pi-1 definition list: the pi-1 Pāli line matching rx must contain the items (pi-1
    spelling, '|'-separated, variants removed); the Burmese list runs from `start` to « ရှိသမျှ» and is split at «၊ »
    (variant notes removed); take = head / tail when only part of the pi-1 list is used. Returns [(pāli, burmese)]."""
    a, b = p1_find(rx)
    items = pali.split("|")
    if " ".join(items) not in VAR_STRIP.sub("", a).replace(",", ""):
        raise SystemExit("pi-1 items not in line: " + pali[:60])
    i = b.index(start) + len(start)
    j = b.index(" ရှိသမျှ", i)
    my = [VAR_STRIP.sub("", x) for x in b[i:j].split(C + " ")]
    if take == "head":
        my = my[:len(items)]
    elif take == "tail":
        my = my[-len(items):]
    if len(my) != len(items):
        raise SystemExit(f"pi-1 list count {pali[:40]}: {len(items)} Pāli / {len(my)} Burmese")
    return list(zip(items, my))


def p1_sentence_dict():
    """pi-1 Pāli sentence «Yasmiṃ samaye / Tasseva O, tasmiṃ samaye …» -> Burmese of O (up to «အချိန်၌»)."""
    D = {}
    for _, a, b in P1LINES:
        ps = [s for s in re.split(r"(?<=[.?])(?:\"|”)? (?=\S)", a) if s]
        bs = [s for s in re.split(r"(?<=။) ", b) if s]
        if len(ps) != len(bs):
            continue
        for s, t in zip(ps, bs):
            m = re.match(r"((?:Yasmiṃ samaye|Tasseva) .*?), tasmiṃ samaye", s)
            if m and f"အချိန်၌{C} ထိုအချိန်၌" in t:
                D.setdefault(m[1], set()).add(t.split(f"{C} ထိုအချိန်၌")[0])
    return D


P1_OPEN = p1_sentence_dict()

# ===================================================================================== variant readings, sigla
for _k, _v in {"cetayitattaṃ": P.PATHA, "kālaṃkiriyā": P.LEKHANA, "asulopo": P.LEKHANA, "dvedhāpatho": P.LEKHANA,
               "apariyogāhanā": P.LEKHANA, "vipariyesaggāho": P.LEKHANA, "paṭhavīkasiṇaṃ": P.LEKHANA,
               "paccayākāravibhaṅgo": P.PATHA}.items():
    if P.VAR_KIND.get(_k, _v) != _v:
        raise SystemExit("variant kind conflict " + _k)
    P.VAR_KIND[_k] = _v
P.SIGLA.setdefault("bahūsu", "Bahūsu")          # «in many (editions)» (new sigla, kept in Roman like the others)
var_my = P.var_my

# ===================================================================================== the twelve links (FINAL pi-1)
PS = "အကြောင်းတို့ကို မှီ၍ ဖြစ်ပေါ်ပုံ"         # paṭiccasamuppāda (pi-1 termbase, locked)
PACCAYA = "ကြောင့်"                            # Xpaccayā (pi-1 ^1-1343)
ARISE = "ဖြစ်ပေါ်သည်"                          # (… paccayā) B (hoti) = «Aကြောင့် B ဖြစ်ပေါ်သည်» (pi-1 ^1-1343)
_F1343 = p1_find(r"Tattha katamā paṭiccasamuppādakusalatā\? Avijjāpaccayā saṅkhārā")[1]
NAMA, RUPA2 = "စိတ်ပိုင်း", "ရုပ်ပိုင်း"           # nāma / rūpa of nāmarūpa (pi-1 ^1-1343, termbase)
FACT = {    # stem -> Burmese (pi-1 ^1-1343 values; the factors of the abhidhamma part new, logged)
    "avijjā": "အမှန်ကို မသိမှု", "saṅkhāra": P.SANKHARA, "viññāṇa": P.VINNANA, "nāma": NAMA,
    "nāmarūpa": f"{NAMA}နှင့် {RUPA2}", "saḷāyatana": "အာရုံခံ နယ်ပယ် ခြောက်ပါး", "phassa": P.PHASSA,
    "vedanā": P.FEEL, "taṇhā": "တပ်မက်မှု", "upādāna": P.UPA, "bhava": "ဘဝ", "jāti": "မွေးဖွားခြင်း",
    "jarāmaraṇa": new("jarāmaraṇaṃ", "အိုခြင်းနှင့် သေခြင်း"),
    "chaṭṭhāyatana": new("chaṭṭhāyatanaṃ", "ဆဋ္ဌမ အာရုံခံ နယ်ပယ်"),
    "kusalamūla": new("kusalamūlā", f"{T['kusalā']}၏ အမြစ်များ"),
    "akusalamūla": new("akusalamūla(paccayā)", f"{T['akusalā']}၏ အမြစ်များ"),
    "adhimokkha": new("adhimokkho", "ဆုံးဖြတ်မှု"),
    "pasāda": new("pasādo (confidence)", "ကြည်ညိုမှု"),
    "paṭigha": "မုန်းတီးမှု", "vicikicchā": "ယုံမှားမှု", "uddhacca": "ယောက်ယက်ခတ်မှု",
}
for _s in ("avijjā", "saṅkhāra", "viññāṇa", "nāmarūpa", "saḷāyatana", "phassa", "vedanā", "taṇhā", "upādāna",
           "bhava", "jāti"):
    p1_has(FACT[_s] + ("များ" if _s == "saṅkhāra" else "") + PACCAYA)
for _s in ("paṭigha", "vicikicchā", "uddhacca"):
    p1_has(FACT[_s] + "နှင့် ယှဉ်တွဲသော")             # pi-1 openings (paṭigha- / vicikicchā- / uddhaccasampayutta)
NOM = {     # nominative -> (stem, plural)
    "avijjā": ("avijjā", False), "saṅkhāro": ("saṅkhāra", False), "saṅkhārā": ("saṅkhāra", True),
    "viññāṇaṃ": ("viññāṇa", False), "nāmaṃ": ("nāma", False), "nāmarūpaṃ": ("nāmarūpa", False),
    "saḷāyatanaṃ": ("saḷāyatana", False), "chaṭṭhāyatanaṃ": ("chaṭṭhāyatana", False), "phasso": ("phassa", False),
    "vedanā": ("vedanā", False), "taṇhā": ("taṇhā", False), "upādānaṃ": ("upādāna", False), "bhavo": ("bhava", False),
    "jāti": ("jāti", False), "jarāmaraṇaṃ": ("jarāmaraṇa", False), "adhimokkho": ("adhimokkha", False),
    "pasādo": ("pasāda", False), "paṭighaṃ": ("paṭigha", False), "vicikicchā": ("vicikicchā", False),
    "uddhaccaṃ": ("uddhacca", False),
}
PL = "များ"
HETUKA = new("Xhetuka (avijjāhetuko …)", "Xကို အကြောင်းပြုသော").replace("X", "")   # as pi-1 cittahetukaṃ
SAMP = P.SAMP                                                                          # «နှင့် ယှဉ်တွဲသော»
p1_has("စိတ်" + HETUKA)
AMONG_THEM = new("(… nāmarūpaṃ viññāṇasampayuttaṃ nāmaṃ: the member)", "ယင်းတို့အနက်")
FINAL = p1_has("မွေးဖွားခြင်းကြောင့် အိုခြင်း၊ သေခြင်း၊ စိုးရိမ်ခြင်း၊ ငိုကြွေးခြင်း၊ ကိုယ်ဆင်းရဲခြင်း၊ "
               "စိတ်ဆင်းရဲမှု၊ ပြင်းစွာ ပူပန်ခြင်းတို့ ဖြစ်ပေါ်ကြသည်")
EVAM = p1_has("ဤသို့ ဤဒုက္ခ အစုအဝေး အားလုံး၏ ဖြစ်ပေါ်ခြင်း ရှိသည်")      # evametassa … samudayo hoti
EVAM_DH = new("Evametesaṃ dhammānaṃ samudayo hoti", f"ဤသို့ ဤ{DHP}၏ ဖြစ်ပေါ်ခြင်း ရှိသည်")
SANGATI = {"saṅgati": new("saṅgati", "စုဝေးခြင်း"), "samāgamo": new("samāgamo", "ဆုံဆည်းခြင်း"),
           "samodhānaṃ": new("samodhānaṃ", "ပေါင်းစည်းခြင်း"), "pātubhāvo": new("pātubhāvo", "ထင်ရှား လာခြင်း")}
LEMMA = new("«X»ti (lemma of a quoted statement)", "“X”ဟူရာ၌").replace("X", "{}")
TENA = new("tena vuccati «X»ti", "ထို့ကြောင့် “X”ဟု ဆိုသည်").replace("“X”", "{}")
CALLED = "ဟု ခေါ်သည်"                                  # vuccati (sample r_vuccati)


def fact(stem, cond=False, pl=False):
    """Burmese of a factor; the condition saṅkhāra is plural in the suttanta part (pi-1 ^1-1343)."""
    my = FACT[stem]
    if stem == "saṅkhāra" and (pl or (cond and STATE.get("part") == "sut")):
        my += PL
    return my


_STEMS = F._alt(FACT)
_NOMS = F._alt(NOM)
CLAUSE = (r"(?P<a>" + _STEMS + r")paccayā(?P<pi>pi)? (?P<b>" + _NOMS + r")(?: (?P<q>(?P<qs>" + _STEMS
          + r")(?P<qt>hetuk|sampayutt)(?:o|ā|aṃ)))?(?: (?P<n2>nāmaṃ|chaṭṭhāyatanaṃ))?")
CLAUSE_RE = re.compile(CLAUSE)


def _parts(m):
    a = F._low(m["a"])
    b, bpl = NOM[F._low(m["b"])]
    q = None
    if m["q"]:
        q = fact(F._low(m["qs"])) + (HETUKA if m["qt"] == "hetuk" else SAMP)
    return a, b, bpl, q


def clause_stmt(m):
    a, b, bpl, q = _parts(m)
    cond = fact(a, cond=True) + PACCAYA + ("လည်း" if m["pi"] else "")
    if m["n2"]:                    # «… nāmarūpaṃ viññāṇasampayuttaṃ nāmaṃ»: the quality belongs to the member
        n2 = fact(NOM[m["n2"]][0])
        return f"{cond} {fact(b, pl=bpl)} {ARISE}{C} {AMONG_THEM} {n2}သည် {q.removesuffix('သော')}သည်"
    return f"{cond} {(q + ' ') if q else ''}{fact(b, pl=bpl)} {ARISE}"


def clause_np(m):
    a, b, bpl, q = _parts(m)
    cond = fact(a, cond=True) + PACCAYA + ("လည်း" if m["pi"] else "")
    if m["n2"]:                    # the quality belongs to the member: «…၊ ယင်းတို့အနက် Q N2»
        return f"{cond} ဖြစ်သော {fact(b, pl=bpl)}{C} {AMONG_THEM} {q} {fact(NOM[m['n2']][0])}"
    mid = f"ဖြစ်၍ {q}" if q else "ဖြစ်သော"
    return f"{cond} {mid} {fact(b, pl=bpl)}"


# ===================================================================================== nouns of questions / closers
NOUN6 = {   # Pāli -> (Burmese, plural)
    "avijjā": (FACT["avijjā"], False), "saṅkhāro": (FACT["saṅkhāra"], False),
    "nāmaṃ": (NAMA, False), "rūpaṃ": (RUPA2, False), "nāmarūpaṃ": (FACT["nāmarūpa"], False),
    "jarā": ("အိုခြင်း", False), "maraṇaṃ": ("သေခြင်း", False),
    "soko": ("စိုးရိမ်ခြင်း", False), "paridevo": ("ငိုကြွေးခြင်း", False),
    "dukkhaṃ": ("ကိုယ်ဆင်းရဲခြင်း", False), "domanassaṃ": ("စိတ်ဆင်းရဲမှု", False),
    "upāyāso": ("ပြင်းစွာ ပူပန်ခြင်း", False),
    "kusalamūlā": (FACT["kusalamūla"], True),
}
for _p in ("soko", "paridevo", "dukkhaṃ", "domanassaṃ", "upāyāso", "jarā", "maraṇaṃ"):
    p1_has(NOUN6[_p][0])
p1_has(f"ထိုတို့အနက် {NAMA} ဟူသည် အဘယ်နည်း")
p1_has(f"ထိုတို့အနက် {RUPA2} ဟူသည် အဘယ်နည်း")
NOUN6.update({
    "puññābhisaṅkhāro": (new("puññābhisaṅkhāro", f"ကောင်းမှု ဖြစ်စေသော {P.SANKHARA}"), False),
    "apuññābhisaṅkhāro": (new("apuññābhisaṅkhāro", f"မကောင်းမှု ဖြစ်စေသော {P.SANKHARA}"), False),
    "āneñjābhisaṅkhāro": (new("āneñjābhisaṅkhāro", f"မတုန်လှုပ်သော {P.SANKHARA}"), False),
    "kāyasaṅkhāro": (new("kāyasaṅkhāro", f"ကိုယ် {P.SANKHARA}"), False),
    "vacīsaṅkhāro": (new("vacīsaṅkhāro", f"နှုတ် {P.SANKHARA}"), False),
    "cittasaṅkhāro": (new("cittasaṅkhāro", f"စိတ် {P.SANKHARA}"), False),
    "kammabhavo": (new("kammabhavo", "ကံ ဘဝ"), False),
    "upapattibhavo": (new("upapattibhavo", "ပဋိသန္ဓေ ဘဝ"), False),
})
p1_has("နှုတ်")


def noun6(x):
    k = F._low(x)
    if k in NOUN6:
        return NOUN6[k]
    raise Miss("noun: " + x)


def np_my(x):
    """Noun phrase of a question / closer: a link («Aကြောင့် ဖြစ်သော B»), a noun, or a «…pe…» sequence."""
    if "…pe…" in x:
        parts = [np_my(y.strip()) for y in x.split("…pe…")]
        return (PE + " ").join(p[0] for p in parts), parts[-1][1]
    m = CLAUSE_RE.fullmatch(x)
    if m:
        return clause_np(m), NOM[F._low(m["b"])][1]
    if F._low(x) in ("alobho", "adoso", "amoho"):
        return ITEM6[F._low(x)], False
    return noun6(x)


# ===================================================================================== definition lists
def mk(pairs, rename=None):
    rename = rename or {}
    return [(rename.get(p, p), m) for p, m in pairs]


LISTS = {}
_T1 = f"။ {P.TASMIM} "
LISTS["moha"] = mk(p1_items(
    r"Katamo tasmiṃ samaye moho hoti\? Yaṃ tasmiṃ samaye aññāṇaṃ",
    "aññāṇaṃ|adassanaṃ|anabhisamayo|ananubodho|asambodho|appaṭivedho|asaṃgāhanā|apariyogāhanā|asamapekkhanā|"
    "apaccavekkhanā|apaccakkhakammaṃ|dummejjhaṃ|bālyaṃ|asampajaññaṃ|moho|pamoho|sammoho|avijjā|avijjogho|"
    "avijjāyogo|avijjānusayo|avijjāpariyuṭṭhānaṃ|avijjālaṅgī|moho|akusalamūlaṃ", _T1))
_cet = p1_items(r"Katamā tasmiṃ samaye cetanā hoti\? Yā tasmiṃ samaye tajjāmanoviññāṇadhātusamphassajā cetanā",
                "tajjāmanoviññāṇadhātusamphassajā cetanā|sañcetanā|cetayitattaṃ", _T1)
if not _cet[0][1].endswith(" " + P.CETANA):
    raise SystemExit("cetanā head")
LISTS["cetanā"] = [("cetanā", P.CETANA), ("sañcetanā", _cet[1][1]), ("sañcetayitattaṃ", _cet[2][1])]
LISTS["citta"] = mk(p1_items(
    r"Katamaṃ tasmiṃ samaye cittaṃ hoti\? Yaṃ tasmiṃ samaye cittaṃ mano",
    "cittaṃ|mano|mānasaṃ|hadayaṃ|paṇḍaraṃ|mano|manāyatanaṃ|manindriyaṃ|viññāṇaṃ|viññāṇakkhandho|"
    "tajjāmanoviññāṇadhātu", _T1))
_TAJJA = LISTS["citta"][-1][1].removesuffix(P.NAMES["manoviññāṇadhātu"])          # «သက်ဆိုင်ရာ »
for _k, _d in (("cakkhu", f"{F.SENSE['cakkhu']} {P.VINNANA} ဓာတ်"), ("kāya", f"{F.SENSE['kāya']} {P.VINNANA} ဓာတ်"),
               ("mano", F.SRC["manodhātu"])):
    p1_has(_d)
    _key = "tajjā" + ("manodhātu" if _k == "mano" else _k + "viññāṇadhātu")
    LISTS["citta-" + _k] = LISTS["citta"][:-1] + [(_key, new(_key, _TAJJA + _d))]
LISTS["phassa"] = mk(p1_items(r"Katamo tasmiṃ samaye phasso hoti\? Yo tasmiṃ samaye phasso",
                              "phasso|phusanā|saṃphusanā|saṃphusitattaṃ", _T1),
                     {"saṃphusanā": "samphusanā", "saṃphusitattaṃ": "samphusitattaṃ"})
for _n, _rx, _it in (
        ("v-sukha-c", r"Yaṃ tasmiṃ samaye cetasikaṃ sātaṃ cetasikaṃ sukhaṃ cetosamphassajaṃ sātaṃ sukhaṃ vedayitaṃ "
                      r"cetosamphassajā sātā sukhā vedanā – ",
         "cetasikaṃ sātaṃ|cetasikaṃ sukhaṃ|cetosamphassajaṃ sātaṃ sukhaṃ vedayitaṃ|cetosamphassajā sātā sukhā vedanā"),
        ("v-neutral-c", r"Yaṃ tasmiṃ samaye cetasikaṃ neva sātaṃ nāsātaṃ cetosamphassajaṃ adukkhamasukhaṃ vedayitaṃ "
                        r"cetosamphassajā adukkhamasukhā vedanā – ",
         "cetasikaṃ neva sātaṃ nāsātaṃ|cetosamphassajaṃ adukkhamasukhaṃ vedayitaṃ|cetosamphassajā adukkhamasukhā vedanā"),
        ("v-dukkha-c", r"Yaṃ tasmiṃ samaye cetasikaṃ asātaṃ cetasikaṃ dukkhaṃ cetosamphassajaṃ asātaṃ dukkhaṃ vedayitaṃ "
                       r"cetosamphassajā asātā dukkhā vedanā – ",
         "cetasikaṃ asātaṃ|cetasikaṃ dukkhaṃ|cetosamphassajaṃ asātaṃ dukkhaṃ vedayitaṃ|"
         "cetosamphassajā asātā dukkhā vedanā"),
        ("v-sukha-k", r"Yaṃ tasmiṃ samaye kāyikaṃ sātaṃ kāyikaṃ sukhaṃ kāyasamphassajaṃ sātaṃ sukhaṃ vedayitaṃ "
                      r"kāyasamphassajā sātā sukhā vedanā – ",
         "kāyikaṃ sātaṃ|kāyikaṃ sukhaṃ|kāyasamphassajaṃ sātaṃ sukhaṃ vedayitaṃ|kāyasamphassajā sātā sukhā vedanā"),
        ("v-dukkha-k", r"Yaṃ tasmiṃ samaye kāyikaṃ asātaṃ kāyikaṃ dukkhaṃ kāyasamphassajaṃ asātaṃ dukkhaṃ vedayitaṃ "
                       r"kāyasamphassajā asātā dukkhā vedanā – ",
         "kāyikaṃ asātaṃ|kāyikaṃ dukkhaṃ|kāyasamphassajaṃ asātaṃ dukkhaṃ vedayitaṃ|kāyasamphassajā asātā dukkhā vedanā")):
    LISTS[_n] = p1_items(_rx, _it, _T1)
LISTS["lobha7"] = mk(p1_items(r"^Tattha katamo lobho\? Yo rāgo sārāgo",
                              "rāgo|sārāgo|anunayo|anurodho|nandī|nandīrāgo|cittassa sārāgo", "။ ", "head"),
                     {"nandīrāgo": "nandirāgo"})
LISTS["diṭṭhi"] = p1_items(
    r"Katamā tasmiṃ samaye micchādiṭṭhi hoti\? Yā tasmiṃ samaye diṭṭhi diṭṭhigataṃ",
    "diṭṭhi|diṭṭhigataṃ|diṭṭhigahanaṃ|diṭṭhikantāro|diṭṭhivisūkāyikaṃ|diṭṭhivipphanditaṃ|diṭṭhisaṃyojanaṃ|gāho|"
    "patiṭṭhāho|abhiniveso|parāmāso|kummaggo|micchāpatho|micchattaṃ|titthāyatanaṃ|vipariyāsaggāho", _T1)
LISTS["dosa"] = (p1_items(r"^Tattha katamo doso\? ", "cittassa āghāto", "ဤသို့ သဘောရှိသော ", "head")
                 + p1_items(r"Katamo tasmiṃ samaye doso hoti\? Yo tasmiṃ samaye doso dussanā",
                            "caṇḍikkaṃ|asuropo|anattamanatā cittassa", _T1, "tail"))
LISTS["kaṅkhā"] = mk(p1_items(
    r"Katamā tasmiṃ samaye vicikicchā hoti\? Yā tasmiṃ samaye kaṅkhā",
    "kaṅkhā|kaṅkhāyanā|kaṅkhāyitattaṃ|vimati|vicikicchā|dveḷhakaṃ|dvedhāpatho|saṃsayo|anekaṃsaggāho|āsappanā|"
    "parisappanā|apariyogāhanā|thambhitattaṃ cittassa|manovilekho", _T1),
    {"dvedhāpatho": "dvidhāpatho", "apariyogāhanā": "apariyogāhaṇā", "thambhitattaṃ cittassa": "chambhitattaṃ cittassa"})
LISTS["uddhacca"] = p1_items(r"Katamaṃ tasmiṃ samaye uddhaccaṃ hoti\? Yaṃ tasmiṃ samaye cittassa uddhaccaṃ",
                             "cittassa uddhaccaṃ|avūpasamo|cetaso vikkhepo|bhantattaṃ cittassa", _T1)
LISTS["alobha"] = p1_items(r"^Tattha katamo alobho\? Yo alobho",
                           "alobho|alubbhanā|alubbhitattaṃ|asārāgo|asārajjanā|asārajjitattaṃ|anabhijjhā|alobho|"
                           "kusalamūlaṃ", "။ ")
LISTS["adosa"] = p1_items(r"Katamo tasmiṃ samaye abyāpādo hoti\? Yo tasmiṃ samaye adoso",
                          "adoso|adussanā|adussitattaṃ|abyāpādo|abyāpajjo|adoso|kusalamūlaṃ", _T1)
_pa, _ = p1_find(r"maggapariyāpannaṃ – idaṃ tasmiṃ samaye paññindriyaṃ hoti")
_pa = VAR_STRIP.sub("", _pa).split("Yā tasmiṃ samaye ", 1)[1].split(" – ")[0]
LISTS["paññā"] = p1_items(r"maggapariyāpannaṃ – idaṃ tasmiṃ samaye paññindriyaṃ hoti", _pa.replace(" ", "|"), _T1)
LISTS["saddhā"] = p1_items(r"Katamaṃ tasmiṃ samaye saddhindriyaṃ hoti\? Yā tasmiṃ samaye saddhā",
                           "saddhā|saddahanā|okappanā|abhippasādo", _T1, "head")
_JARA = p1_items(r"Katamaṃ taṃ rūpaṃ rūpassa jaratā\? Yā rūpassa jarā",
                 "jarā|jīraṇatā|khaṇḍiccaṃ|pāliccaṃ|valittacatā|āyuno saṃhāni|indriyānaṃ paripāko", f"။ ရုပ်၏ ")
LISTS["jarā-s"] = _JARA
LISTS["jarā-d"] = [_JARA[0], _JARA[1], _JARA[5]]
LISTS["anicca"] = p1_items(r"Katamaṃ taṃ rūpaṃ rūpassa aniccatā\? Yo rūpassa khayo",
                           "khayo|vayo|bhedo|paribhedo|aniccatā|antaradhānaṃ", f"။ ရုပ်၏ ")
_DUKKHE = p1_items(r"^Tattha katamo moho\? Dukkhe aññāṇaṃ",
                   "Dukkhe aññāṇaṃ|dukkhasamudaye aññāṇaṃ|dukkhanirodhe aññāṇaṃ|"
                   "dukkhanirodhagāminiyā paṭipadāya aññāṇaṃ", "။ ", "head")
_BHEDO, _ANTAR = LISTS["anicca"][2][1], LISTS["anicca"][5][1]
_JATI, _MAR = FACT["jāti"], NOUN6["maraṇaṃ"][0]


def newlist(name, pairs):
    LISTS[name] = [(p, new(p, m)) if (p, m) not in KNOWN else (p, m) for p, m in pairs]


KNOWN = {("bhedo", _BHEDO), ("antaradhānaṃ", _ANTAR), ("maraṇaṃ", _MAR), ("jāti", _JATI),
         ("domanassaṃ", NOUN6["domanassaṃ"][0]), ("soko", NOUN6["soko"][0]), ("paridevo", NOUN6["paridevo"][0]),
         ("upāyāso", NOUN6["upāyāso"][0])}
newlist("jāti-s", [("jāti", _JATI), ("sañjāti", "ကောင်းစွာ မွေးဖွားခြင်း"), ("okkanti", "သက်ဆင်းခြင်း"),
                   ("abhinibbatti", "ထင်ရှားစွာ ပေါ်ထွက်ခြင်း"),
                   ("khandhānaṃ pātubhāvo", f"{F.KHANDHA}တို့၏ {SANGATI['pātubhāvo']}"),
                   ("āyatanānaṃ paṭilābho", "အာရုံခံ နယ်ပယ်တို့ကို ရရှိခြင်း")])
newlist("jāti-d", [("jāti", _JATI), ("sañjāti", "ကောင်းစွာ မွေးဖွားခြင်း"), ("nibbatti", "ပေါ်ထွက်ခြင်း"),
                   ("abhinibbatti", "ထင်ရှားစွာ ပေါ်ထွက်ခြင်း"), ("pātubhāvo", SANGATI["pātubhāvo"])])
newlist("maraṇa-s", [("cuti", "စုတေခြင်း"), ("cavanatā", "ရွေ့လျောခြင်း"), ("bhedo", _BHEDO),
                     ("antaradhānaṃ", _ANTAR), ("maccu", "သေမင်း"), ("maraṇaṃ", _MAR), ("kālakiriyā", "ကွယ်လွန်ခြင်း"),
                     ("khandhānaṃ bhedo", f"{F.KHANDHA}တို့၏ {_BHEDO}"),
                     ("kaḷevarassa nikkhepo", "ကိုယ်ခန္ဓာကို စွန့်ပစ်ခြင်း"),
                     ("jīvitindriyassupacchedo", f"{P.NAMES['jīvitindriyaṃ']} ပြတ်စဲခြင်း")])
newlist("soka", [("soko", NOUN6["soko"][0]), ("socanā", "စိုးရိမ်နေခြင်း"), ("socitattaṃ", "စိုးရိမ်ထားသော အဖြစ်"),
                 ("antosoko", "အတွင်း စိုးရိမ်ခြင်း"), ("antoparisoko", "အတွင်း ပြင်းစွာ စိုးရိမ်ခြင်း"),
                 ("cetaso parijjhāyanā", "စိတ်၏ လောင်မြိုက်ခြင်း"), ("domanassaṃ", NOUN6["domanassaṃ"][0]),
                 ("sokasallaṃ", "စိုးရိမ်ခြင်းဟူသော ငြောင့်")])
newlist("parideva", [("ādevo", "ငိုခြင်း"), ("paridevo", NOUN6["paridevo"][0]), ("ādevanā", "ငိုနေခြင်း"),
                     ("paridevanā", "ငိုကြွေးနေခြင်း"), ("ādevitattaṃ", "ငိုထားသော အဖြစ်"),
                     ("paridevitattaṃ", "ငိုကြွေးထားသော အဖြစ်"), ("vācā palāpo", "စကား ပေါက်ကရ ပြောခြင်း"),
                     ("vippalāpo", "အမျိုးမျိုး ပေါက်ကရ ပြောခြင်း"), ("lālappo", "ညည်းတွားခြင်း"),
                     ("lālappanā", "ညည်းတွားနေခြင်း"), ("lālappitattaṃ", "ညည်းတွားထားသော အဖြစ်")])
newlist("upāyāsa", [("āyāso", "ပူပန်ခြင်း"), ("upāyāso", NOUN6["upāyāso"][0]), ("āyāsitattaṃ", "ပူပန်ထားသော အဖြစ်"),
                    ("upāyāsitattaṃ", "ပြင်းစွာ ပူပန်ထားသော အဖြစ်")])
newlist("adhimokkha", [("cittassa adhimokkho", f"စိတ်၏ {FACT['adhimokkha']}"), ("adhimuccanā", "ဆုံးဖြတ်ခြင်း"),
                       ("tadadhimuttatā", "ထိုအာရုံ၌ ဆုံးဖြတ်ထားသော အဖြစ်")])
OCC_ALIAS = {"akusamūlaṃ": "akusalamūlaṃ", "abhinibbati": "abhinibbatti"}     # source slips (read as)
LIST_GEN = {    # «Yā tesaṃ tesaṃ …» heads
    "tesaṃ tesaṃ sattānaṃ tamhi tamhi sattanikāye":
        F.YE_GEN["tesaṃ tesaṃ sattānaṃ"] + " " + new("tamhi tamhi sattanikāye", "ထိုထို သတ္တဝါ အမျိုးအစား၌"),
    "tesaṃ tesaṃ sattānaṃ tamhā tamhā sattanikāyā":
        F.YE_GEN["tesaṃ tesaṃ sattānaṃ"] + " " + new("tamhā tamhā sattanikāyā", "ထိုထို သတ္တဝါ အမျိုးအစားမှ"),
    "tesaṃ tesaṃ dhammānaṃ": new("tesaṃ tesaṃ dhammānaṃ", f"ထိုထို {DH}တို့၏"),
}
SAMAYA = " ရှိသမျှ"                                     # Yo / Yā / Yaṃ … (pi-1 frame)
LIST_USED = []                                           # (list name, Pāli keys) of every list occurrence (check)


def _tokens(text):
    """Pāli list text -> tokens: words, «PE», variant brackets «[..]» (commas dropped)."""
    out = []
    for t in re.findall(r"\[[^\]]+\]|…pe…|[^\s,…\[\]]+", text):
        out.append(OCC_ALIAS.get(t, t))
    return out


def list_my(text):
    toks = _tokens(text)
    for name, items in LISTS.items():
        keys = [k.split(" ") for k, _ in items]
        res, pos, i, ok, seg_start = [], 0, 0, True, True
        while i < len(toks):
            t = toks[i]
            if t == "…pe…":
                res.append(("PE", None))
                i += 1
                seg_start = True
                continue
            if t.startswith("["):
                if not res or res[-1][0] == "PE":
                    ok = False
                    break
                res[-1] = (res[-1][0], res[-1][1] + " " + var_my(t))
                i += 1
                continue
            # next item: at pos (inside a segment) or searched forward (start of a later segment)
            cands = [pos] if not (seg_start and res) else list(range(pos, len(keys)))
            hit = None
            for j in cands:
                k = keys[j] if j < len(keys) else None
                if k and toks[i:i + len(k)] == k:
                    hit = j
                    break
            if hit is None:
                ok = False
                break
            res.append((" ".join(keys[hit]), items[hit][1]))
            i += len(keys[hit])
            pos = hit + 1
            seg_start = False
        if ok and res and res[0][0] != "PE" and (res[0][0] == items[0][0]):
            out = ""
            for n, (k, my) in enumerate(res):
                if k == "PE":
                    out += PE + " "
                    continue
                out += my
                if n + 1 < len(res) and res[n + 1][0] != "PE":
                    out += C + " "
            LIST_USED.append((name, [k for k, _ in res if k != "PE"]))
            return out
    raise Miss("definition list: " + text[:80])


# ===================================================================================== item runs (no «Yo»)
ITEM6 = {}
for _k in ("vedanākkhandho", "saññākkhandho", "saṅkhārakkhandho", "viññāṇakkhandho"):
    ITEM6[_k] = F.KH[_k][0]
for _s in list(F.SENSE) + ["mano"]:
    ITEM6[_s + "viññāṇaṃ"] = F.ITEM[_s + "viññāṇaṃ"]
    ITEM6[_s + "samphasso"] = new(_s + "samphasso", f"{F.SRC[_s]}၏ {P.PHASSA}")
    ITEM6[_s + "samphassajā vedanā"] = F.ITEM[_s + "samphassajā vedanā"]
for _s, _a in (("cakkhu", "cakkhāyatanaṃ"), ("sota", "sotāyatanaṃ"), ("ghāna", "ghānāyatanaṃ"),
               ("jivhā", "jivhāyatanaṃ"), ("kāya", "kāyāyatanaṃ")):
    ITEM6[_a] = F.ITEM[_a]
    ITEM6[_a[:-1] + "ssa upacayo"] = new(_a[:-1] + "ssa upacayo", f"{F.ITEM[_a]}၏ တိုးပွားခြင်း")
ITEM6["manāyatanaṃ"] = dict(LISTS["citta"])["manāyatanaṃ"]
p1_has("ရုပ်၏ တိုးပွားခြင်း")
for _o in ("rūpa", "sadda", "gandha", "rasa", "phoṭṭhabba", "dhamma"):
    ITEM6[_o + "taṇhā"] = new(_o + "taṇhā", f"{P.ARAMMANA[_o[:-1] + 'ārammaṇaṃ']}ကို {FACT['taṇhā']}")
for _k, _v in (("kāmupādānaṃ", "ကာမ စွဲလမ်းမှု"), ("diṭṭhupādānaṃ", "အယူ စွဲလမ်းမှု"),
               ("sīlabbatupādānaṃ", "သီလ အကျင့်ဝတ် စွဲလမ်းမှု"), ("attavādupādānaṃ", "အတ္တဟူသော ဝါဒ စွဲလမ်းမှု")):
    ITEM6[_k] = p1_has(_v)
for _k in ("puññābhisaṅkhāro", "apuññābhisaṅkhāro", "āneñjābhisaṅkhāro", "kāyasaṅkhāro", "vacīsaṅkhāro",
           "cittasaṅkhāro"):
    ITEM6[_k] = NOUN6[_k][0]
_BH = "ဘဝ"
for _k, _v in (("kāmabhavo", f"{T['kāmāvacarā'].replace('နှင့် ဆိုင်သော', '')}၌ ဖြစ်သော {_BH}"),
               ("rūpabhavo", f"{T['rūpāvacarā'].replace('နှင့် ဆိုင်သော', '')}၌ ဖြစ်သော {_BH}"),
               ("arūpabhavo", f"{T['arūpāvacarā'].replace('နှင့် ဆိုင်သော', '')}၌ ဖြစ်သော {_BH}"),
               ("saññābhavo", f"{P.SANNA} ရှိသော {_BH}"), ("asaññābhavo", f"{P.SANNA} မရှိသော {_BH}"),
               ("nevasaññānāsaññābhavo", f"{P.SANNA} ရှိသည်လည်း မဟုတ်{C} {P.SANNA} မရှိသည်လည်း မဟုတ်သော {_BH}"),
               ("ekavokārabhavo", f"{P.count_my(F.KHANDHA, 'eka')} ရှိသော {_BH}"),
               ("catuvokārabhavo", f"{P.count_my(F.KHANDHA, 'catu')} ရှိသော {_BH}"),
               ("pañcavokārabhavo", f"{P.count_my(F.KHANDHA, 'pañca')} ရှိသော {_BH}")):
    ITEM6[_k] = new(_k, _v)
p1_has(f"{P.SANNA} ရှိသည်လည်း မဟုတ်{C} {P.SANNA} မရှိသည်လည်း မဟုတ်သော")
ITEM6["alobho"] = LISTS["alobha"][0][1]
ITEM6["adoso"] = LISTS["adosa"][0][1]
ITEM6["amoho"] = dict(LISTS["paññā"])["amoho"]
for _p, _m in _DUKKHE:
    ITEM6[F._low(_p)] = _m
_ITEM_ALT = F._alt(ITEM6)
ITEMRUN_RE = re.compile(r"(?:" + _ITEM_ALT + r")(?:(?:, | )(?:" + _ITEM_ALT + r"))*(?= – |, yaṃ vā|\.|$|…)")


def r_itemrun(m):
    toks = re.split(r", | ", m[0])
    out, i = [], 0
    while i < len(toks):
        for k in (4, 3, 2, 1):
            key = F._low(" ".join(toks[i:i + k]))
            if len(toks[i:i + k]) == k and key in ITEM6:
                out.append(ITEM6[key])
                i += k
                break
        else:
            raise Miss("item: " + toks[i])
    return f"{C} ".join(out)


# ===================================================================================== cittuppāda openings
QUAL6 = {   # pi-1 qualifiers of the openings (read from the pi-1 rails text, checked below)
    "somanassasahagataṃ": P.QUAL["somanassasahagataṃ"], "upekkhāsahagataṃ": P.QUAL["upekkhāsahagataṃ"],
    "ñāṇasampayuttaṃ": P.QUAL["ñāṇasampayuttaṃ"], "ñāṇavippayuttaṃ": P.QUAL["ñāṇavippayuttaṃ"],
    "diṭṭhigatasampayuttaṃ": "အယူမှား" + SAMP, "diṭṭhigatavippayuttaṃ": "အယူမှား" + P.VIPP,
    "domanassasahagataṃ": "စိတ်ဆင်းရဲမှု" + P.TOGETHER, "paṭighasampayuttaṃ": FACT["paṭigha"] + SAMP,
    "vicikicchāsampayuttaṃ": FACT["vicikicchā"] + SAMP, "uddhaccasampayuttaṃ": FACT["uddhacca"] + SAMP,
    "sukhasahagataṃ": T["sukhasahagatā"], "dukkhasahagataṃ": T["dukkhasahagatā"],
}
for _v in QUAL6.values():
    p1_has(_v)
KIND6 = {
    "akusalaṃ cittaṃ": p1_has(T["akusalā"] + P.MIND + "သည်")[:-3],
    "kāmāvacaraṃ kusalaṃ cittaṃ": P.CITTA_KIND["kāmāvacaraṃ kusalaṃ cittaṃ"],
    "manodhātu": F.SRC["manodhātu"], "manoviññāṇadhātu": P.NAMES["manoviññāṇadhātu"],
}
for _s in F.SENSE:
    KIND6[_s + "viññāṇaṃ"] = F.ITEM[_s + "viññāṇaṃ"]
CAUSE6 = {
    "kāmāvacarassa kusalassa kammassa katattā upacitattā": p1_has("ကာမဘုံနှင့် ဆိုင်သော ကုသိုလ်ကံကို ပြုခဲ့၍ ဆည်းပူးခဲ့သောကြောင့်"),
    "akusalassa kammassa katattā upacitattā": p1_has("အကုသိုလ်ကံကို ပြုခဲ့၍ ဆည်းပူးခဲ့သောကြောင့်"),
}
VIPAKA = p1_has("ကံ၏ အကျိုး ဖြစ်သော")
KIRIYA6 = p1_has(f"ပြုရုံမျှသာ ဖြစ်သော{C} {T['kusalā']}လည်း မဟုတ်{C} {T['akusalā']}လည်း မဟုတ်{C} ကံ၏ အကျိုးလည်း မဟုတ်သော")
OBJ_VA, OBJ_ONE = P.ARAMMANA_VA, "ကို အာရုံပြုသော"
p1_has("အဆင်းအရောင်" + OBJ_ONE + C)
_KIND_RE = re.compile(r"(?P<k>" + "|".join(re.escape(k) for k in sorted(KIND6, key=len, reverse=True))
                      + r") uppann(?:aṃ|ā) hoti(?: |$)")
_KIRIYA_P = "kiriyā neva kusalā nākusalā na ca kammavipākā"


def _fem(w):
    return w[:-1] + "aṃ" if w.endswith("ā") else w


def _parse_part(s):
    """One «…pe…»-free part of an opening -> dict(kind, kiriya, quals, adv, objs [(Burmese, single)], yam)."""
    g = dict(kind=None, kiriya=False, quals=[], adv=None, objs=[], yam=False)
    m = _KIND_RE.match(s)
    if m:
        g["kind"] = m["k"]
        s = s[m.end():]
    if s.startswith(_KIRIYA_P):
        g["kiriya"] = True
        s = s[len(_KIRIYA_P):].lstrip()
    if s.endswith("yaṃ yaṃ vā panārabbha"):
        g["yam"] = True
        s = s[:-len("yaṃ yaṃ vā panārabbha")].rstrip()
    words = s.split(" ") if s else []
    i = 0
    while i < len(words) and _fem(words[i]) in QUAL6:
        g["quals"].append(QUAL6[_fem(words[i])])
        i += 1
    if i < len(words) and words[i] == "sasaṅkhārena":
        g["adv"] = P.QUAL_ADV["sasaṅkhārena"]
        i += 1
    while i < len(words):
        o = _fem(words[i])
        if o not in P.ARAMMANA:
            raise Miss("opening word: " + words[i])
        if i + 1 < len(words) and words[i + 1] == "vā":
            g["objs"].append([P.ARAMMANA[o], False, False])          # [object, single (no vā), «…pe…» after]
            i += 2
        else:
            g["objs"].append([P.ARAMMANA[o], True, False])
            i += 1
    return g


def _objs(objs, pe_after_last, yam):
    """Objects: «Xကို အာရုံပြု၍ဖြစ်စေ» joined by «၊ » or «… »; a single object without vā = «Xကို အာရုံပြုသော၊ »."""
    if len(objs) == 1 and objs[0][1] and not objs[0][2]:
        return objs[0][0] + OBJ_ONE + C + " "
    s = ""
    for n, (o, _single, pe) in enumerate(objs):
        s += o + OBJ_VA
        if pe or (n == len(objs) - 1 and pe_after_last):
            s += PE + " "
        elif n < len(objs) - 1 or yam:
            s += C + " "
        else:
            s += " "
    if yam:
        s += P.YAM_YAM + " "
    return s


def opening(o):
    """«Yasmiṃ samaye O, tasmiṃ samaye»: O -> Burmese up to «အချိန်၌» (pi-1 cittuppāda forms)."""
    if o in JH:
        return JH[o]
    cause, vip = "", False
    for k, v in CAUSE6.items():
        if o.startswith(k + " vipāk"):
            cause = v + " "
            o = o[len(k) + 1:]
            o = re.sub(r"^vipāk(?:aṃ|ā) ", "", o)
            vip = True
            break
    raw = re.split(r"\s*…pe…\s*", o)
    groups = []
    for part in raw:
        g = _parse_part(part)
        if groups and g["kind"] is None and not g["quals"] and not g["kiriya"] and (g["objs"] or g["yam"]):
            prev = groups[-1]                      # objects continued after an internal «…pe…»
            prev["objs"][-1][2] = True
            prev["objs"] += g["objs"]
            prev["yam"] = g["yam"]
            continue
        groups.append(g)
    if groups[0]["kind"] is None:
        raise Miss("opening kind: " + o)
    multi_kind = any(g["kind"] for g in groups[1:]) or len(groups) == 1
    if multi_kind:
        out = []
        for n, g in enumerate(groups):
            if g["kind"] is None:
                raise Miss("opening group without kind: " + o)
            last = n == len(groups) - 1
            s = (cause if n == 0 else "") + _objs(g["objs"], False, g["yam"]) if g["objs"] else (cause if n == 0 else "")
            if g["kiriya"]:
                s += KIRIYA6 + C + " "
            s += f"{C} ".join(g["quals"]) + " "
            if vip and n == 0:
                s += VIPAKA + " "
            s += KIND6[g["kind"]] + "သည် " + (g["adv"] + " " if g["adv"] else "") + P.UPPANNA
            out.append(s)
        return (PE + " ").join(out) + " " + P.YASMIM
    g0 = groups[0]
    head = cause + (VIPAKA + " " if vip else "") + KIND6[g0["kind"]] + "သည် " + (KIRIYA6 + C + " " if g0["kiriya"] else "")
    out = []
    for n, g in enumerate(groups):
        last = n == len(groups) - 1
        s = f"{C} ".join(g["quals"])
        if g["adv"]:
            s += " " + g["adv"]
        if g["objs"]:
            s += " " + _objs(g["objs"], False, g["yam"]).rstrip()
        out.append(s)
    return head + (PE + " ").join(out) + " " + P.UPPANNA + " " + P.YASMIM


# jhāna / path openings: the pi-1 Burmese of the same Pāli (P1_OPEN), three near-variants derived and logged
JH = {}
for _o in ("rūpūpapattiyā maggaṃ bhāveti vivicceva kāmehi…pe… paṭhamaṃ jhānaṃ upasampajja viharati pathavīkasiṇaṃ",
           "arūpūpapattiyā maggaṃ bhāveti sabbaso ākiñcaññāyatanaṃ samatikkamma "
           "nevasaññānāsaññāyatanasaññāsahagataṃ sukhassa ca pahānā…pe… catutthaṃ jhānaṃ upasampajja viharati",
           "lokuttaraṃ jhānaṃ bhāveti niyyānikaṃ apacayagāmiṃ diṭṭhigatānaṃ pahānāya paṭhamāya bhūmiyā pattiyā "
           "vivicceva kāmehi…pe… paṭhamaṃ jhānaṃ upasampajja viharati dukkhapaṭipadaṃ dandhābhiññaṃ",
           "rūpāvacaraṃ jhānaṃ bhāveti kiriyaṃ neva kusalaṃ nākusalaṃ na ca kammavipākaṃ diṭṭhadhammasukhavihāraṃ "
           "vivicceva kāmehi…pe… paṭhamaṃ jhānaṃ upasampajja viharati pathavīkasiṇaṃ",
           "arūpāvacaraṃ jhānaṃ bhāveti kiriyaṃ neva kusalaṃ nākusalaṃ na ca kammavipākaṃ diṭṭhadhammasukhavihāraṃ "
           "sabbaso ākiñcaññāyatanaṃ samatikkamma nevasaññānāsaññāyatanasaññāsahagataṃ sukhassa ca pahānā…pe… "
           "catutthaṃ jhānaṃ upasampajja viharati"):
    _v = P1_OPEN.get("Yasmiṃ samaye " + _o)
    if not _v or len(_v) != 1:
        raise SystemExit("pi-1 jhāna opening: " + _o[:60])
    JH[_o] = next(iter(_v))
for _o in ("rūpāvacarassa kusalassa kammassa katattā upacitattā vipākaṃ vivicceva kāmehi…pe… paṭhamaṃ jhānaṃ "
           "upasampajja viharati pathavīkasiṇaṃ",
           "arūpāvacarassa kusalassa kammassa katattā upacitattā vipākaṃ sabbaso ākiñcaññāyatanaṃ samatikkamma "
           "nevasaññānāsaññāyatanasaññāsahagataṃ sukhassa ca pahānā…pe… catutthaṃ jhānaṃ upasampajja viharati",
           "lokuttarassa kusalassa jhānassa katattā bhāvitattā vipākaṃ vivicceva kāmehi…pe… paṭhamaṃ jhānaṃ "
           "upasampajja viharati dukkhapaṭipadaṃ dandhābhiññaṃ suññataṃ"):
    _v = P1_OPEN.get("Tasseva " + _o)
    if not _v or len(_v) != 1:
        raise SystemExit("pi-1 Tasseva opening: " + _o[:60])
    JH["Tasseva " + _o] = next(iter(_v))
_K1 = "rūpūpapattiyā maggaṃ bhāveti vivicceva kāmehi…pe… paṭhamaṃ jhānaṃ upasampajja viharati pathavīkasiṇaṃ"
_KAS = "မြေ ကသိုဏ်း"
if JH[_K1].count(_KAS) != 1:
    raise SystemExit("kasiṇa")
JH[_K1 + " [paṭhavīkasiṇaṃ (sī. syā.)]"] = JH[_K1].replace(_KAS, _KAS + " " + var_my("[paṭhavīkasiṇaṃ (sī. syā.)]"))
JH[_K1.replace("kāmehi…pe…", "kāmehi …pe…")] = JH[_K1]                 # stray space before …pe… (source)
_T3 = ("Tasseva lokuttarassa kusalassa jhānassa katattā bhāvitattā vipākaṃ vivicceva kāmehi…pe… paṭhamaṃ jhānaṃ "
       "upasampajja viharati dukkhapaṭipadaṃ dandhābhiññaṃ")
_SUN = f"{C} ဆိတ်သုဉ်းသော"
if JH[_T3 + " suññataṃ"].count(_SUN) != 1:
    raise SystemExit("suññata")
JH[_T3] = JH[_T3 + " suññataṃ"].replace(_SUN, "")                     # the same opening without «suññataṃ»
PHASSO_PE = p1_has(f"{P.PHASSA} ရှိသည်{PE} စိတ် မပျံ့လွင့်ခြင်း ရှိသည်")   # phasso hoti…pe… avikkhepo hoti

# ===================================================================================== headings, colophons, fixed
NIDDESA = "အကျယ် ဖော်ပြချက်"                    # niddeso (pi-1 termbase)
CATUKKA = new("-catukkaṃ (set of four)", "လေးမျိုးတွဲ")   # as pi-1 duka နှစ်မျိုးတွဲ / tika သုံးမျိုးတွဲ
MULAKA = "ကို အခြေခံသော"                        # -mūlaka (sample Dukamūlakaṃ)
HEAD6 = {
    "Paṭiccasamuppādavibhaṅgo": f"{PS}ကို {F.TITLE}",
    "Suttantabhājanīyaṃ": F.HEAD["Suttantabhājanīyaṃ"], "Abhidhammabhājanīyaṃ": F.HEAD["Abhidhammabhājanīyaṃ"],
    "Paccayacatukkaṃ": new("Paccayacatukkaṃ", f"အကြောင်း {CATUKKA}"),
    "Hetucatukkaṃ": new("Hetucatukkaṃ", f"အကြောင်းပြုခြင်း {CATUKKA}"),
    "Sampayuttacatukkaṃ": new("Sampayuttacatukkaṃ", f"ယှဉ်တွဲခြင်း {CATUKKA}"),
    "Aññamaññacatukkaṃ": new("Aññamaññacatukkaṃ", f"အချင်းချင်း အကြောင်းဖြစ်ခြင်း {CATUKKA}"),
    "Mātikā": P.MATIKA,
    "Akusalaniddeso": new("Akusalaniddeso", f"{T['akusalā']}ကို {NIDDESA}"),
    "Kusalaniddeso": new("Kusalaniddeso", f"{T['kusalā']}ကို {NIDDESA}"),
    "Abyākataniddeso": new("Abyākataniddeso", f"{T['abyākatā']} {DH}ကို {NIDDESA}"),
    "Avijjāmūlakakusalaniddeso": new("Avijjāmūlakakusalaniddeso",
                                     f"{FACT['avijjā']}{MULAKA} {T['kusalā']}ကို {NIDDESA}"),
    "Kusalamūlakavipākaniddeso": new("Kusalamūlakavipākaniddeso",
                                     f"{FACT['kusalamūla']}{MULAKA} ကံ၏ အကျိုးကို {NIDDESA}"),
    "Akusalamūlakavipākaniddeso": new("Akusalamūlakavipākaniddeso",
                                      f"{FACT['akusalamūla']}{MULAKA} ကံ၏ အကျိုးကို {NIDDESA}"),
}
new("Paṭiccasamuppādavibhaṅgo", HEAD6["Paṭiccasamuppādavibhaṅgo"])
PART = {"Suttantabhājanīyaṃ": "sut", "Abhidhammabhājanīyaṃ": "abh"}
COLO6 = dict(HEAD6)
COLO6["Mātikā"] = p1_has(P.MATIKA + END)[:-1]
_VAR6 = "[paccayākāravibhaṅgo (sī. syā.)]"
COLO6[f"Paṭiccasamuppādavibhaṅgo {_VAR6} niṭṭhito"] = f"“{HEAD6['Paṭiccasamuppādavibhaṅgo']}” {var_my(_VAR6)} {P.NITTHITA}"

FIXED6 = {  # phrases (from the start of a clause) not built from a frame
    "Kusalā cetanā kāmāvacarā rūpāvacarā dānamayā sīlamayā bhāvanāmayā": new(
        "Kusalā cetanā kāmāvacarā rūpāvacarā dānamayā sīlamayā bhāvanāmayā",
        f"{T['kāmāvacarā']}{C} {T['rūpāvacarā']}{C} ဒါနမှ ဖြစ်သော{C} သီလမှ ဖြစ်သော{C} ဘာဝနာမှ ဖြစ်သော "
        f"{T['kusalā']} {P.CETANA}"),
    "Akusalā cetanā kāmāvacarā": new("Akusalā cetanā kāmāvacarā", f"{T['kāmāvacarā']} {T['akusalā']} {P.CETANA}"),
    "Kusalā cetanā arūpāvacarā": new("Kusalā cetanā arūpāvacarā", f"{T['arūpāvacarā']} {T['kusalā']} {P.CETANA}"),
    "Kāyasañcetanā kāyasaṅkhāro, vacīsañcetanā vacīsaṅkhāro, manosañcetanā cittasaṅkhāro": new(
        "Kāyasañcetanā kāyasaṅkhāro, vacīsañcetanā vacīsaṅkhāro, manosañcetanā cittasaṅkhāro",
        f"ကိုယ်ဖြင့် {LISTS['cetanā'][1][1]}သည် {NOUN6['kāyasaṅkhāro'][0]} ဖြစ်သည်{C} "
        f"နှုတ်ဖြင့် {LISTS['cetanā'][1][1]}သည် {NOUN6['vacīsaṅkhāro'][0]} ဖြစ်သည်{C} "
        f"{P.MANO}ဖြင့် {LISTS['cetanā'][1][1]}သည် {NOUN6['cittasaṅkhāro'][0]} ဖြစ်သည်"),
    "Cattāro mahābhūtā, catunnañca mahābhūtānaṃ upādāya rūpaṃ": F.MAHABHUTA2,
    "Yaṃ rūpaṃ nissāya manoviññāṇadhātu vattati": new(
        "Yaṃ rūpaṃ nissāya manoviññāṇadhātu vattati",
        f"{P.NAMES['manoviññāṇadhātu']}သည် မှီ၍ ဖြစ်ပေါ်ရာ {F.RUPA}{SAMAYA}"),
    "Cattāro ca mahābhūtā, yañca rūpaṃ nissāya manoviññāṇadhātu vattati": new(
        "Cattāro ca mahābhūtā, yañca rūpaṃ nissāya manoviññāṇadhātu vattati",
        f"{F.MAHABHUTA2.split(C)[0]}{C} {P.NAMES['manoviññāṇadhātu']}သည် မှီ၍ ဖြစ်ပေါ်ရာ {F.RUPA}လည်းကောင်း"),
    "yaṃ vā panaññampi atthi rūpaṃ cittajaṃ cittahetukaṃ cittasamuṭṭhānaṃ":
        p1_has(f"စိတ်မှ မွေးဖွားသော{C} စိတ်ကို အကြောင်းပြုသော{C} စိတ်မှ ဖြစ်ပေါ်လာသော {F.YAM_VA} {F.RUPA} ရှိသမျှ")
        + "လည်း",
    "Bhavo duvidhena": f"{F.VIDHA['duvidhena']} {F.LOOK} {FACT['bhava']}",
    "Sabbampi bhavagāmikammaṃ kammabhavo": new(
        "Sabbampi bhavagāmikammaṃ kammabhavo",
        f"ဘဝသို့ ဦးတည်သော ကံ အားလုံးသည်လည်း {NOUN6['kammabhavo'][0]} ဖြစ်သည်"),
    "phasso hoti…pe… avikkhepo hoti": PHASSO_PE,
    "ime dhammā kusalā": P.IME_KUSALA,
    "Ñātibyasanena vā phuṭṭhassa, bhogabyasanena vā phuṭṭhassa, rogabyasanena vā phuṭṭhassa, sīlabyasanena vā "
    "phuṭṭhassa, diṭṭhibyasanena vā phuṭṭhassa, aññataraññatarena byasanena samannāgatassa, aññataraññatarena "
    "dukkhadhammena phuṭṭhassa": new(
        "Ñātibyasanena vā phuṭṭhassa … dukkhadhammena phuṭṭhassa",
        f"ဆွေမျိုး ပျက်စီးခြင်းဖြင့် ထိခိုက်ခံရသူ၏ဖြစ်စေ{C} စည်းစိမ် ပျက်စီးခြင်းဖြင့် ထိခိုက်ခံရသူ၏ဖြစ်စေ{C} "
        f"ကျန်းမာရေး ပျက်စီးခြင်းဖြင့် ထိခိုက်ခံရသူ၏ဖြစ်စေ{C} သီလ ပျက်စီးခြင်းဖြင့် ထိခိုက်ခံရသူ၏ဖြစ်စေ{C} "
        f"အယူ ပျက်စီးခြင်းဖြင့် ထိခိုက်ခံရသူ၏ဖြစ်စေ{C} တစ်ခုခုသော ပျက်စီးခြင်းနှင့် ကြုံတွေ့နေရသူ၏{C} "
        f"တစ်ခုခုသော ဆင်းရဲဖွယ်ရာဖြင့် ထိခိုက်ခံရသူ၏"),
}
p1_has(F.MAHABHUTA2)
p1_has(P.IME_KUSALA)
_FIXED_ALT = "(?:" + "|".join(re.escape(k) for k in sorted(FIXED6, key=len, reverse=True)) + ")"

# ===================================================================================== the engine
STATE = {}
W = r"[\wāīūṃṅñṭḍṇḷ]"


def r_katame(m):
    return f"{T[m['k']]} {DHP} {P.CU_Q['pl']}"


def r_open(m):
    return opening(m["o"]) + f"{C} {P.TASMIM} "


def r_tasseva(m):
    k = "Tasseva " + m["o"]
    if k not in JH:
        raise Miss("Tasseva: " + m["o"][:60])
    return JH[k] + f"{C} {P.TASMIM} "


def r_question(m):
    STATE["qnp"] = False
    np_, pl = np_my(m["x"])
    pl = pl or m["g"] == "e"
    return f"ထိုတို့အနက် {np_} {P.CU_Q['pl' if pl else 'sg']}"


def r_question_pe(m):
    STATE["qnp"] = True
    np_, pl = np_my(m["x"])
    return f"ထိုတို့အနက် {np_} {P.CU_Q['pl' if pl or m['g'] == 'e' else 'sg']}"


def r_vuccati(m):
    STATE["qnp"] = False
    np_, _ = np_my(m["x"])
    return (f"ဤသည်{'တို့' if m['v'] == 'vuccanti' else ''}ကို{' –' if m['dash'] else ''} "
            f"{'“' if m['o'] else ''}{np_}{'”' if m['c'] else ''}{CALLED}")


def r_lemma(m):
    x = m["x"] + ("ṃ" if m["t"] == "nti" else "")
    mm = CLAUSE_RE.fullmatch(x)
    if not mm:
        raise Miss("lemma: " + x)
    return LEMMA.format(clause_stmt(mm))


def r_evam_lemma(m):
    return LEMMA.format(EVAM_DH if "esaṃ" in m[0] else EVAM)


def r_tena(m):
    x = EVAM_DH if "evametesaṃ" in m["x"].lower() else EVAM
    return TENA.format(("“" if m["o"] else "") + x + "”")


def r_evam(m):
    return EVAM_DH if "esaṃ" in m[0] else EVAM


def r_sangati(m):
    head = (EVAM_DH if "esaṃ" in m[0] else EVAM).removesuffix(" ဖြစ်ပေါ်ခြင်း ရှိသည်")
    return f"{head} {SANGATI['saṅgati']} ရှိသည်{C} {SANGATI['samāgamo']} ရှိသည်{C} {SANGATI['samodhānaṃ']} ရှိသည်{C} " \
           f"{SANGATI['pātubhāvo']} ရှိသည်"


def r_list(m):
    head = (LIST_GEN[m["g"]] + " ") if m["g"] else ""
    return head + list_my(m["l"]) + SAMAYA


def r_list_bare(m):
    return list_my(m["l"]) + SAMAYA


def r_fixed(m):
    return FIXED6[m[0]]


def r_thapetva(m):
    x = m["x"]
    k = {"phassaṃ": "phassa", "upādānaṃ": "upādāna", "adhimokkhaṃ": "adhimokkha", "vicikicchaṃ": "vicikicchā",
         "vedanaṃ": "vedanā"}.get(x)
    if not k:
        raise Miss("ṭhapetvā " + x)
    return FACT[k] + P.THAPETVA


def r_atthi(m):
    return f"{noun6(m['x'])[0]} {F.HOTI}"


def r_iti(m):
    a, b = noun6(m["x"])[0], noun6(m["y"])[0]
    return f"ဤသို့ ဤသည်မှာ {a} {P.CU_COP['sg']}{C} ဤသည်မှာ {b} {P.CU_COP['sg']}"


def r_final(m):
    return FINAL


def r_clause(m):
    return clause_np(m) if STATE.get("qnp") else clause_stmt(m)


_GEN_ALT = "|".join(re.escape(k) for k in sorted(LIST_GEN, key=len, reverse=True))
_EV = r"[Ee]vamet(?:assa kevalassa dukkhakkhandhassa|esaṃ dhammānaṃ)"
RULES = [
    (r"Katame dhammā (?P<k>akusalā|kusalā|abyākatā)(?=\?)", r_katame),
    (r"Yasmiṃ samaye (?P<o>.+?), tasmiṃ samaye ", r_open),
    (r"Tasseva (?P<o>.+?), tasmiṃ samaye ", r_tasseva),
    (r"Tasmiṃ samaye ", lambda m: P.TASMIM + " "),
    (_FIXED_ALT + r"(?=[,.;?]| |…|$)", r_fixed),
    (r"Tattha katam(?P<g>o|ā|aṃ|e) (?P<x>[^?.]+?)(?=\?)", r_question),
    (r"Tattha katam(?P<g>o|ā|aṃ|e) (?P<x>[^?]+?)(?=…pe…)", r_question_pe),
    (r"(?:[Aa]yaṃ|[Ii]daṃ|[Ii]me) (?P<v>vuccati|vuccanti)(?P<dash> –)? (?P<o>\"?)(?P<x>[^\"…]+?)(?P<c>\"?)"
     r"(?=\.|…|$| …)", r_vuccati),
    (_EV + r" samudayo hotīti", r_evam_lemma),
    (r"[Tt]ena vuccati (?P<o>\"?)(?P<x>" + _EV + r" samudayo hot[iī])\"ti", r_tena),
    (_EV + r" saṅgati hoti, samāgamo hoti, samodhānaṃ hoti, pātubhāvo hoti", r_sangati),
    (_EV + r" samudayo hoti(?=\.|$)", r_evam),
    (r"(?P<x>[A-ZÑṬ]\w*?paccayā(?:pi)? \w+?(?: \w+?){0,2})(?P<t>nti|ti)(?=\.)", r_lemma),
    (r"(?:Yo|Yā|Yaṃ) (?:(?P<g>" + _GEN_ALT + r") )?(?P<l>[^–]+?)(?= – )", r_list),
    (r"(?<=phuṭṭhassa )(?P<l>[^–]+?)(?= – )", r_list_bare),
    (r"Ṭhapetvā (?P<x>\w+)(?=,)", r_thapetva),
    (r"[Aa]tthi (?P<x>nāmaṃ|rūpaṃ|jarā|maraṇaṃ|kammabhavo|upapattibhavo)(?=[,.]|$)", r_atthi),
    (r"Iti (?:ayañca|idañca) (?P<x>\w+), (?:ayañca|idañca) (?P<y>\w+)(?=\.)", r_iti),
    (r"jātipaccayā jarāmaraṇaṃ sokaparidevadukkhadomanassupāyāsā sambhavanti", r_final),
    (CLAUSE + r"(?=, |; |\.|…| …| " + W + r"+paccayā|$)", r_clause),
    (ITEMRUN_RE.pattern, lambda m: r_itemrun(m)),
]
RULES = [(re.compile(p), f) for p, f in RULES]
SEP = [("…pe…. ", PE + END + " "), ("…pe….", PE + END), (" …pe… ", PE + " "), ("…pe… ", PE + " "), ("…pe…", PE),
       ("? ", END + " "), ("?", END), ("; ", C + " "), (", ", C + " "), (" – ", " – "), (". ", END + " "),
       (".", END), (" ", " ")]


def clauses_my(s):
    pos, out = 0, []
    while pos < len(s):
        for p, my in SEP:
            if s.startswith(p, pos):
                if my.startswith(END):
                    STATE["qnp"] = False
                out.append(my)
                pos += len(p)
                break
        else:
            for rx, f in RULES:
                m = rx.match(s, pos)
                if m and m.end() > pos:
                    r = f(m)
                    if r is None:
                        continue
                    out.append(r)
                    pos = m.end()
                    break
            else:
                raise Miss("no frame: " + s[pos:pos + 100])
    return "".join(out).replace("  ", " ")


HEAD_RE = re.compile(r"(?P<h>#+) (?P<t>.+?)$")


def line_my(body):
    STATE["qnp"] = False
    m = HEAD_RE.fullmatch(body)
    if m:
        if m["t"] not in HEAD6:
            raise Miss("heading: " + body)
        if m["t"] in PART:
            STATE["part"] = PART[m["t"]]
        return f"{m['h']} {HEAD6[m['t']]}"
    if body.endswith(".") and body[:-1] in COLO6:
        return COLO6[body[:-1]] + END
    return clauses_my(body)


def translate_line(line):
    if not line.strip():
        return ""
    m = F.ID_RE.search(line)
    body = line[:m.start()] if m else line
    return line_my(body) + (" " + m.group(1) if m else "")


def chapter():
    lines = (PALI / NAME).read_text(encoding="utf-8-sig").splitlines()
    done = []
    STATE.clear()
    for i, line in enumerate(lines):
        try:
            done.append(translate_line(line))
        except Miss as e:
            print(f"STOP {NAME} line {i + 1}: {e}\n  {line[:200]}")
            sys.exit(1)
    txt = unicodedata.normalize("NFC", "\n".join(done).rstrip("\n") + "\n")
    (OUT / NAME).write_text(txt, encoding="utf-8")
    print(f"wrote {NAME}: {sum(1 for l in txt.splitlines() if l)} lines")


if __name__ == "__main__":
    chapter()
    if "--new" in sys.argv:
        for p, m in NEW.items():
            print(f"{p} = {m}")
