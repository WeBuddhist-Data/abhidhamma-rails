"""Burmese zero-shot of pi-2 (Vibhaṅga, «ခွဲခြမ်းစိတ်ဖြာခြင်း») chapters 12 (Jhāna), 13 (Appamaññā), 14 (Sikkhāpada).

usage: python3 -I -X utf8 make_ch12-14.py [12 | 13 | 14 ...] [--selftest]
Model: the approved sample (make_sample.py / my2_formulas.py, imported read-only; nothing in it or in pi-1-my is
written). Every line is generated from the Pāli, sentence by sentence:
  1. a Pāli sentence identical with a pi-1 sentence takes pi-1's FINAL Burmese (rails text), word for word;
  2. a jhāna / citta opening («Yasmiṃ samaye … , tasmiṃ samaye») identical with a pi-1 opening takes pi-1's Burmese;
     other openings are built by open_jh() / open_citta() from the pi-1 tables (my2_formulas.P1.JH_*), with the pi-1
     joining rules (phrases «၊ », «…pe…» = «… », the jhāna qualifiers before the jhāna noun); --selftest rebuilds
     every pi-1 opening the builder can read and compares it with pi-1's Burmese;
  3. frames (regex -> Burmese) and tables below; the synonym lists are read from the pi-1 Burmese lines (item counts
     asserted) or are new (logged in notes-ch12-14.md);
  4. the pañhāpucchaka goes through the sample engine (my2_formulas.clauses_my) with a few added rules.
A sentence nothing matches stops the run (Miss); nothing is guessed. A chapter is written only when every line passed.
"""
import pathlib
import re
import sys
import unicodedata

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import my2_formulas as F  # noqa: E402

P1 = F.P1
T = F.T
C, END, PE = F.C, F.END, F.PE
Miss = F.Miss
ROOT = HERE.parents[3]
PALI = ROOT / "AI_translation/pali/pi-2_split_chapters"
OUT = ROOT / "AI_translation/burmese/pi-2-burmese-plain-zeroshot_split_chapters"
NAMES_OUT = {"12": "12-jhanavibhango.md", "13": "13-appamannavibhango.md", "14": "14-sikkhapadavibhango.md"}
NEW = {}       # section -> {pāli: burmese}: every string new in pi-2 (for the notes)
SLIPS = []


def new(sec, d):
    NEW.setdefault(sec, {}).update(d)
    return d


# ===================================================================================== pi-1 (final) read-only
ID = F.ID_RE
VAR = re.compile(r" \[[^\]]*\]")


def psplit(l):
    l = ID.sub("", l)
    l = re.sub(r"\[[^\]]*\]", lambda m: m[0].replace(". ", ".\x00"), l)
    return [s.replace("\x00", " ") for s in re.split(r"(?<=[.?])(?:\"|”)? (?=\S)", l) if s]


def bsplit(l):
    return [s for s in re.split(r"(?<=။) ", ID.sub("", l)) if s]


SENT1, OPEN1, HEAD1, PAIRS1 = {}, {}, {}, []
OPEN_PI = re.compile(r"(?:Yasmiṃ samaye |(?=Tasseva ))(.+?)(?:,| –) tasmiṃ samaye")
OPEN_MY = re.compile(r"(.+? အချိန်၌)(?:၊| –) ထိုအချိန်၌")
for _p in sorted(F.P1_PALI.glob("*.md")):
    for _a, _b in zip(_p.read_text(encoding="utf-8-sig").split("\n"), (F.P1_RAILS / _p.name).read_text(
            encoding="utf-8").split("\n")):
        if _a.startswith("#"):
            HEAD1.setdefault(ID.sub("", _a).split(" ", 1)[1], ID.sub("", _b).split(" ", 1)[1])
            continue
        _ps, _bs = psplit(_a), bsplit(_b)
        if len(_ps) != len(_bs):
            continue
        for _x, _y in zip(_ps, _bs):
            SENT1.setdefault(_x.replace("upādinn", "upādiṇṇ"), _y)
            PAIRS1.append((_x, _y))
            _m, _n = OPEN_PI.match(_x), OPEN_MY.match(_y)
            if _m and _n:
                OPEN1.setdefault(VAR.sub("", _m[1]), VAR.sub("", _n[1]))


def p1_items(pali_start, items, my_prefix=""):
    """(pāli item, burmese item) pairs of a pi-1 synonym list: the pi-1 sentence that starts with pali_start; its
    Burmese after my_prefix up to «ရှိသမျှ», variants removed, split at «၊ »; the item count is asserted."""
    items = items.split("|")
    for x, y in PAIRS1:
        if x.startswith(pali_start):
            y = VAR.sub("", y)
            if not y.startswith(my_prefix):
                raise SystemExit(f"pi-1 list {pali_start}: prefix «{my_prefix}» not in «{y[:60]}»")
            body = y[len(my_prefix):].split(" ရှိသမျှ")[0].removesuffix(END)
            my = body.split(f"{C} ")
            if len(my) < len(items):
                raise SystemExit(f"pi-1 list {pali_start}: {len(items)} Pāli / {len(my)} Burmese items")
            return list(zip(items, my[:len(items)]))
    raise SystemExit("pi-1 list not found: " + pali_start)


# ===================================================================================== list items
ITEMS = {}      # pāli item (one or more words) -> burmese
ITEM_SRC = {}


def add_items(pairs, src):
    for p, m in pairs:
        if ITEMS.get(p, m) != m:
            raise SystemExit(f"item conflict {p}: «{ITEMS[p]}» / «{m}» ({src})")
        ITEMS[p] = m
        ITEM_SRC.setdefault(p, src)


_TS = "ထိုအချိန်၌ "
for _start, _items, _pre in [
    ("Yā sati anussati paṭissati sati saraṇatā", "sati|anussati|paṭissati|sati|saraṇatā|dhāraṇatā|apilāpanatā|"
     "asammusanatā|sati|satindriyaṃ|satibalaṃ|sammāsati", ""),
    ("Yā tasmiṃ samaye paññā pajānanā vicayo pavicayo dhammavicayo sallakkhaṇā upalakkhaṇā paccupalakkhaṇā "
     "paṇḍiccaṃ kosallaṃ nepuññaṃ vebhabyā cintā upaparikkhā bhūrī medhā pariṇāyikā vipassanā sampajaññaṃ patodo "
     "paññā paññindriyaṃ paññābalaṃ paññāsatthaṃ paññāpāsādo paññāāloko paññāobhāso paññāpajjoto paññāratanaṃ amoho "
     "dhammavicayo sammādiṭṭhi – ayaṃ tasmiṃ samaye vipassanā",
     "paññā|pajānanā|vicayo|pavicayo|dhammavicayo|sallakkhaṇā|upalakkhaṇā|paccupalakkhaṇā|paṇḍiccaṃ|kosallaṃ|"
     "nepuññaṃ|vebhabyā|cintā|upaparikkhā|bhūrī|medhā|pariṇāyikā|vipassanā|sampajaññaṃ|patodo|paññā|paññindriyaṃ|"
     "paññābalaṃ|paññāsatthaṃ|paññāpāsādo|paññāāloko|paññāobhāso|paññāpajjoto|paññāratanaṃ|amoho|dhammavicayo|"
     "sammādiṭṭhi", _TS),
    ("Yo tasmiṃ samaye cetasiko vīriyārambho nikkamo parakkamo uyyāmo vāyāmo ussāho ussoḷhī thāmo dhiti "
     "asithilaparakkamatā anikkhittachandatā anikkhittadhuratā dhurasampaggāho vīriyaṃ vīriyindriyaṃ vīriyabalaṃ – idaṃ",
     "cetasiko vīriyārambho|nikkamo|parakkamo|uyyāmo|vāyāmo|ussāho|ussoḷhī|thāmo|dhiti|asithilaparakkamatā|"
     "anikkhittachandatā|anikkhittadhuratā|dhurasampaggāho|vīriyaṃ|vīriyindriyaṃ|vīriyabalaṃ", _TS),
    ("Yaṃ tasmiṃ samaye cittaṃ mano mānasaṃ hadayaṃ paṇḍaraṃ mano manāyatanaṃ manindriyaṃ viññāṇaṃ viññāṇakkhandho "
     "tajjāmanodhātu – idaṃ", "cittaṃ|mano|mānasaṃ|hadayaṃ|paṇḍaraṃ|mano|manāyatanaṃ|manindriyaṃ|viññāṇaṃ|"
     "viññāṇakkhandho|tajjāmanodhātu", _TS),
    ("Yo adoso adussanā adussitattaṃ metti", "adoso|adussanā|adussitattaṃ|metti|mettāyanā|mettāyitattaṃ", ""),
    ("Yo evarūpo cittassa āghāto paṭighāto", "cittassa āghāto|paṭighāto|paṭighaṃ|paṭivirodho|kopo|pakopo|sampakopo|"
     "doso|padoso|sampadoso|cittassa byāpatti|manopadoso|kodho|kujjhanā|kujjhitattaṃ|doso|dussanā|dussitattaṃ|"
     "byāpatti|byāpajjanā|byāpajjitattaṃ|virodho|paṭivirodho|caṇḍikkaṃ|asuropo|anattamanatā cittassa",
     "ဤသို့ သဘောရှိသော "),
    ("Yā cittassa akallatā akammaññatā olīyanā", "cittassa akalyatā|akammaññatā|olīyanā|sallīyanā|līnaṃ|līyanā|"
     "līyitattaṃ|thinaṃ|thiyanā|thiyitattaṃ cittassa", ""),
    ("Yā kāyassa akallatā akammaññatā onāho", "kāyassa akalyatā|akammaññatā|onāho|pariyonāho|antosamorodho|middhaṃ|"
     "suppaṃ|pacalāyikā|suppaṃ|suppanā|suppitattaṃ", ""),
    ("Yaṃ cittassa uddhaccaṃ avūpasamo", "cittassa uddhaccaṃ|avūpasamo|cetaso vikkhepo|bhantattaṃ cittassa", ""),
    ("Akappiye kappiyasaññitā, kappiye", "akappiye kappiyasaññitā|kappiye akappiyasaññitā|avajje vajjasaññitā|"
     "vajje avajjasaññitā", ""),
    ("Yā evarūpā kaṅkhā kaṅkhāyanā", "kaṅkhā|kaṅkhāyanā|kaṅkhāyitattaṃ|vimati|vicikicchā|dveḷhakaṃ|dvidhāpatho|"
     "saṃsayo|anekaṃsaggāho|āsappanā|parisappanā|apariyogāhaṇā|chambhitattaṃ cittassa|manovilekho",
     "ဤသို့ သဘောရှိသော "),
    ("Yo tasmiṃ samaye takko vitakko saṅkappo appanā byappanā cetaso abhiniropanā – ayaṃ",
     "takko|vitakko|saṅkappo|appanā|byappanā|cetaso abhiniropanā", _TS),
    ("Yo tasmiṃ samaye cāro vicāro anuvicāro upavicāro", "cāro|vicāro|anuvicāro|upavicāro|cittassa anusandhanatā|"
     "anupekkhanatā", _TS),
    ("Yā tasmiṃ samaye pīti pāmojjaṃ", "pīti|pāmojjaṃ|āmodanā|pamodanā|hāso|pahāso|vitti|odagyaṃ|"
     "attamanatā cittassa", _TS),
    ("Yaṃ tasmiṃ samaye cetasikaṃ sātaṃ cetasikaṃ sukhaṃ", "cetasikaṃ sātaṃ|cetasikaṃ sukhaṃ|"
     "cetosamphassajaṃ sātaṃ sukhaṃ vedayitaṃ|cetosamphassajā sātā sukhā vedanā", _TS),
    ("Yaṃ tasmiṃ samaye kāyikaṃ sātaṃ kāyikaṃ sukhaṃ", "kāyikaṃ sātaṃ|kāyikaṃ sukhaṃ|"
     "kāyasamphassajaṃ sātaṃ sukhaṃ vedayitaṃ|kāyasamphassajā sātā sukhā vedanā", _TS),
    ("Yaṃ tasmiṃ samaye kāyikaṃ asātaṃ kāyikaṃ dukkhaṃ", "kāyikaṃ asātaṃ|kāyikaṃ dukkhaṃ|"
     "kāyasamphassajaṃ asātaṃ dukkhaṃ vedayitaṃ|kāyasamphassajā asātā dukkhā vedanā", _TS),
    ("Yaṃ tasmiṃ samaye cetasikaṃ asātaṃ cetasikaṃ dukkhaṃ", "cetasikaṃ asātaṃ|cetasikaṃ dukkhaṃ|"
     "cetosamphassajaṃ asātaṃ dukkhaṃ vedayitaṃ|cetosamphassajā asātā dukkhā vedanā", _TS),
    ("Yaṃ tasmiṃ samaye cetasikaṃ neva sātaṃ nāsātaṃ", "cetasikaṃ neva sātaṃ nāsātaṃ|"
     "cetosamphassajaṃ adukkhamasukhaṃ vedayitaṃ|cetosamphassajā adukkhamasukhā vedanā", _TS),
    ("Yā tasmiṃ samaye cittassa ṭhiti saṇṭhiti", "cittassa ṭhiti|saṇṭhiti|avaṭṭhiti|avisāhāro|avikkhepo|"
     "avisāhaṭamānasatā|samatho|samādhindriyaṃ|samādhibalaṃ", _TS),
    ("Yā tasmiṃ samaye saddhā saddahanā", "saddhā|saddahanā|okappanā|abhippasādo", _TS),
    ("Yā tasmiṃ samaye saññā sañjānanā", "saññā|sañjānanā|sañjānitattaṃ", _TS),
    ("Yo ākāso ākāsagataṃ", "ākāso|ākāsagataṃ|aghaṃ|aghagataṃ|vivaro|vivaragataṃ|asamphuṭṭhaṃ catūhi mahābhūtehi", ""),
    ("Yā tasmiṃ samaye catūhi vacīduccaritehi ārati", "catūhi vacīduccaritehi ārati|virati|paṭivirati|veramaṇī|"
     "akiriyā|akaraṇaṃ|anajjhāpatti|velāanatikkamo|setughāto", _TS),
    ("Yā imesaṃ channaṃ indriyānaṃ agutti", "imesaṃ channaṃ indriyānaṃ agutti|agopanā|anārakkho|asaṃvaro", ""),
    ("Yā imesaṃ channaṃ indriyānaṃ gutti", "imesaṃ channaṃ indriyānaṃ gutti|gopanā|ārakkho|saṃvaro", ""),
    ("Yā tattha asantuṭṭhitā", "tattha asantuṭṭhitā|amattaññutā|appaṭisaṅkhā bhojane", ""),
    ("Yā tattha santuṭṭhitā", "tattha santuṭṭhitā|mattaññutā|paṭisaṅkhā bhojane", ""),
]:
    if _items == "x":
        continue
    _pairs = p1_items(_start, _items, _pre)
    add_items([(p, m) for p, m in _pairs if p != "x"], "pi-1")
# the rāga list (lobha, ^1-1065): first seven items
for _x, _y in PAIRS1:
    if _x.startswith("Yo rāgo sārāgo anunayo anurodho nandī nandīrāgo"):
        _b = VAR.sub("", _y).split(f"{C} ")
        add_items(list(zip("rāgo|sārāgo|anunayo|anurodho|nandī|nandīrāgo|cittassa sārāgo".split("|"), _b[:7])), "pi-1")
        break
else:
    raise SystemExit("pi-1 rāga list not found")
# the cetanā list: the cetanā item comes after the genitive head (^1-5)
for _x, _y in PAIRS1:
    if _x.startswith("Yā tasmiṃ samaye tajjāmanoviññāṇadhātusamphassajā cetanā sañcetanā cetayitattaṃ"):
        _b = VAR.sub("", _y).split(" ရှိသမျှ")[0].split(f"{C} ")
        add_items([("cetanā", P1.CETANA), ("sañcetanā", _b[1]), ("cetayitattaṃ", _b[2])], "pi-1")
        break
# the kukkucca list (4-0x «Yaṃ evarūpaṃ kukkuccaṃ …»)
for _x, _y in PAIRS1:
    if _x.startswith("Yaṃ evarūpaṃ kukkuccaṃ kukkuccāyanā"):
        _b = _y.removeprefix("ဤသို့ သဘောရှိသော ").split(" ရှိသမျှ")[0].split(f"{C} ")
        add_items(list(zip("kukkuccaṃ|kukkuccāyanā|kukkuccāyitattaṃ|cetaso vippaṭisāro|manovilekho".split("|"), _b)),
                  "pi-1")
        break
else:
    raise SystemExit("pi-1 kukkucca list not found")
add_items([("sammāvāyāmo", P1.NAMES["sammāvāyāmo"]), ("sammāsaṅkappo", P1.NAMES["sammāsaṅkappo"]),
           ("sammāsamādhi", P1.NAMES["sammāsamādhi"]), ("tajjāmanoviññāṇadhātu", P1.SYN["tajjāmanoviññāṇadhātu"]),
           ("phasso", P1.NAMES["phasso"]), ("paggāho", P1.NAMES["paggāho"])], "pi-1")
add_items([("evarūpaṃ", "ဤသို့ သဘောရှိသော")], "pi-1")
# Vb spellings of pi-1 items (same word, same Burmese)
for _a, _b in (("manovilekhā", "manovilekho"), ("cittassa anusandhānatā", "cittassa anusandhanatā"),
               ("sañcetayitattaṃ", "cetayitattaṃ")):
    ITEMS[_a] = ITEMS[_b]
    ITEM_SRC[_a] = "pi-1 (spelling)"

# new items (pi-2)
BV = {"mettā": "မေတ္တာ", "karuṇā": "ကရုဏာ", "muditā": "မုဒိတာ", "upekkhā": "ဥပေက္ခာ"}
VIMUTTI = "စိတ်လွတ်မြောက်မှု"            # cetovimutti (vimutti = လွတ်မြောက်မှု, pi-1)
_new_items = {
    "anucāro": "လိုက်၍ သုံးသပ်ခြင်း",            # ^2-576 (Vb only)
    "bhūrīmedhā": "ကျယ်ပြန့်သော ဉာဏ်ထက်မြက်ခြင်း",  # Vb one word (Dhs «bhūrī medhā» = two items)
    "upekkhā": BV["upekkhā"], "upekkhanā": "တည်ငြိမ်စွာ ရှုခြင်း", "ajjhupekkhanā": "အလွန် တည်ငြိမ်စွာ ရှုခြင်း",
    "majjhattatā cittassa": "စိတ်၏ အလယ်၌ တည်ခြင်း",
    "sattesu": "သတ္တဝါတို့အပေါ်၌",
}
for _b, _m in BV.items():
    _new_items[f"{_b}cetovimutti"] = f"{_m}ဖြင့် {VIMUTTI}"
    if _b != "mettā":       # metti / mettāyanā / mettāyitattaṃ: pi-1 ^1-1062; the others on the same pattern
        _new_items.update({_b: _m, f"{_b}yanā": f"{_m} ထားခြင်း", f"{_b}yitattaṃ": f"{_m} ထားသော အဖြစ်"})
_new_items["muditāyatanā"] = _new_items["muditāyanā"]      # ^2-688 source slip (read as muditāyanā)
SLIPS.append("^2-688 «muditāyatanā» (once) read as muditāyanā")
add_items(new("List items (new)", _new_items).items(), "new")
assert (ITEMS["metti"], ITEMS["mettāyanā"], ITEMS["mettāyitattaṃ"]) == ("မေတ္တာ", "မေတ္တာ ထားခြင်း", "မေတ္တာ ထားသော အဖြစ်")
ITEM_MAX = 6

# ===================================================================================== nouns (topics) and names
JH = P1.JHANA
ORDJ = {f"{o}ṃ jhānaṃ": f"{P1.ORD[o]} {JH}" for o in P1.ORD}
NOUNS = {   # pāli -> (burmese, plural)
    "sati": (P1.SUT["sati"], False), "sampajaññaṃ": (P1.SUT["sampajañña"], False),
    "vitakko": (P1.NAMES["vitakko"], False), "vicāro": (P1.NAMES["vicāro"], False), "pīti": (P1.NAMES["pīti"], False),
    "sukhaṃ": (P1.NAMES["sukhaṃ"], False), "upekkhā": (BV["upekkhā"], False), "cittaṃ": (P1.MIND, False),
    "saññā": (P1.SANNA, False), "thinaṃ": (ITEMS["thinaṃ"], False), "middhaṃ": (ITEMS["middhaṃ"], False),
    "uddhaccaṃ": (P1.UDDHACCA, False), "kukkuccaṃ": (P1.KUKKUCCA, False), "vicikicchā": (P1.VICIKICCHA, False),
    "mettā": (BV["mettā"], False), "karuṇā": (BV["karuṇā"], False), "muditā": (BV["muditā"], False),
}
for _k, _v in ORDJ.items():
    NOUNS[_k] = (_v, False)
CITTA = P1.MIND


def noun(p):
    k = p[0].lower() + p[1:]
    if k not in NOUNS:
        raise Miss("noun: " + p)
    return NOUNS[k]


# ===================================================================================== the precepts (ch14)
SIKKHAPADA = "သိက္ခာပုဒ်"
VERAMANI = ITEMS["veramaṇī"]                               # ကင်းဝေးခြင်း (pi-1 virati list)
ABST = new("Precepts (new)", {
    "pāṇātipātā": "သူ့အသက်ကို သတ်ခြင်း", "adinnādānā": "မပေးသောအရာကို ယူခြင်း",
    "kāmesumicchācārā": "ကာမတို့၌ မှားယွင်းစွာ ကျင့်ခြင်း", "musāvādā": "မုသားစကား ပြောခြင်း",
    "surāmerayamajjapamādaṭṭhānā": "သေရည် အရက် မူးယစ်ဖွယ်ဟူသော မေ့လျော့ခြင်း၏ အကြောင်း"})
for _k, _v in ABST.items():
    NOUNS[f"{_k} veramaṇī sikkhāpadaṃ"] = (f"{_v}မှ {VERAMANI} {SIKKHAPADA}", False)
    ITEMS[f"{_k} ārati"] = f"{_v}မှ {ITEMS['catūhi vacīduccaritehi ārati'].split('မှ ')[-1]}"
    ITEM_SRC[f"{_k} ārati"] = "new (pi-1 virati list)"
new("Precepts (new)", {"veramaṇī sikkhāpadaṃ": f"…မှ {VERAMANI} {SIKKHAPADA}", "sikkhā": "သိက္ခာ",
                       "X viramantassa": "Xမှ ရှောင်ကြဉ်နေသူ၏"})
SIKKHA = "သိက္ခာ"
VIRAMANTASSA = "မှ ရှောင်ကြဉ်နေသူ၏"

# ===================================================================================== headings, colophons
APP = "အပ္ပမညာ"
HEAD = {
    "Jhānavibhaṅgo": f"{JH}များကို {F.TITLE}", "Appamaññāvibhaṅgo": f"{APP}များကို {F.TITLE}",
    "Sikkhāpadavibhaṅgo": f"{SIKKHAPADA}များကို {F.TITLE}",
    "Lokuttaravipākā": f"{T['lokuttarā']} ကံ၏ အကျိုး",
    "Rūpārūpāvacarakiriyā": f"{T['rūpāvacarā'].removesuffix('နှင့် ဆိုင်သော')}နှင့် "
                            f"{T['arūpāvacarā'].removesuffix('နှင့် ဆိုင်သော')}တို့နှင့် ဆိုင်သော {P1.KIRIYA} {CITTA}",
    "Mettā": BV["mettā"], "Karuṇā": BV["karuṇā"], "Muditā": BV["muditā"], "Upekkhā": BV["upekkhā"],
}
new("Headings and colophons (new)", HEAD)
HEAD_ALL = {**F.HEAD, **HEAD1, **HEAD}
COLO = {f"{k} niṭṭhito": f"“{HEAD[k]}” {F.NITTHITA}" for k in ("Jhānavibhaṅgo", "Appamaññāvibhaṅgo",
                                                              "Sikkhāpadavibhaṅgo")}
new("Headings and colophons (new)", COLO)
COLO.update({k: F.COLO[k] for k in ("Suttantabhājanīyaṃ", "Abhidhammabhājanīyaṃ", "Pañhāpucchakaṃ")})
COLO.update({k: SENT1[k + "."].removesuffix(END) for k in ("Catukkaṃ", "Pañcakaṃ")})

# ===================================================================================== jhāna openings
JH_UPAS = P1.JH_UPAS                       # ဝင်စား၍ နေသော
JH_UPAS_FIN = "ဝင်စား၍ နေ၏"                 # upasampajja viharati as a statement
YASMIM = P1.YASMIM                         # အချိန်၌
KATA_UPACITA = "ပြုခဲ့၍ ဆည်းပူးခဲ့သောကြောင့်"      # pi-1 make_ch2-04-05 (^1-499)
KATA_BHAVITA = "ပြုခဲ့၍ ပွားများခဲ့သောကြောင့်"      # (^1-505)
VIPAKA_ADV = "ကံ၏ အကျိုး အဖြစ်ဖြင့်"
DDSV = "မျက်မှောက်ဘဝ၌ပင် သာယာစွာ နေထိုင်ရန် ဖြစ်သော"   # diṭṭhadhammasukhavihāraṃ (^1-577)
_KK = f"{T['kusalā']}ကံ"
ROLE = {}


def _role(d, r):
    for k, v in d.items():
        ROLE[k] = (r, v)


_role(P1.JH_HEADS, "H")
_role({
    "tasseva rūpāvacarassa kusalassa kammassa katattā upacitattā vipākaṃ":
        f"ထို {T['rūpāvacarā']} {_KK}ကိုပင် {KATA_UPACITA} {VIPAKA_ADV}",
    "tasseva arūpāvacarassa kusalassa kammassa katattā upacitattā vipākaṃ":
        f"ထို {T['arūpāvacarā']} {_KK}ကိုပင် {KATA_UPACITA} {VIPAKA_ADV}",
    "tasseva lokuttarassa kusalassa jhānassa katattā bhāvitattā vipākaṃ":
        f"ထို {T['lokuttarā']} {T['kusalā']} {JH}ကိုပင် {KATA_BHAVITA} {VIPAKA_ADV}",
    "rūpāvacaraṃ jhānaṃ bhāveti kiriyaṃ neva kusalaṃ nākusalaṃ na ca kammavipākaṃ diṭṭhadhammasukhavihāraṃ":
        f"{P1.KIRIYA_ATTR}၊ {DDSV} {T['rūpāvacarā']} {JH}{P1.JH_BHAVETI}",
    "arūpāvacaraṃ jhānaṃ bhāveti kiriyaṃ neva kusalaṃ nākusalaṃ na ca kammavipākaṃ diṭṭhadhammasukhavihāraṃ":
        f"{P1.KIRIYA_ATTR}၊ {DDSV} {T['arūpāvacarā']} {JH}{P1.JH_BHAVETI}",
}, "H")
_role({"lokuttaraṃ jhānaṃ bhāveti niyyānikaṃ apacayagāmiṃ": f"{P1.JH_NIYY_APAC}၊ {P1.JH_LOK} {JH}{P1.JH_BHAVETI}"}, "L")
_role(P1.JH_PURPOSE, "U")
_role(P1.JH_FORM, "F")
_role(P1.JH_QADJ, "A")
_role(ORDJ, "J")
_role({"upasampajja viharati": JH_UPAS}, "V")
_Q = dict(P1.JH_Q)
_Q.update({f"{b}sahagataṃ": BV[b] + P1.TOGETHER for b in ("mettā", "karuṇā", "muditā")})
_Q["upekkhāsahagataṃ"] = T["upekkhāsahagatā"]
_role(_Q, "Q")
ROLE_MAX = max(len(k.split()) for k in ROLE)


def _tokens(seg):
    w, i, out = seg.replace(", ", " ").split(" "), 0, []     # «, » between phrases = « » (both «၊ », pi-1 2-02)
    while i < len(w):
        for k in range(ROLE_MAX, 0, -1):
            key = " ".join(w[i:i + k])
            key = key[:1].lower() + key[1:]
            if i + k <= len(w) and key in ROLE:
                out.append((ROLE[key][0], ROLE[key][1], key))
                i += k
                break
        else:
            raise Miss("opening word: " + w[i] + " in: " + seg[:100])
    return out


def open_jh(body):
    """A jhāna opening (without «Yasmiṃ samaye»), up to «, tasmiṃ samaye»: pi-1's Burmese when the Pāli is a pi-1
    opening, else built with the pi-1 rules."""
    key = VAR.sub("", body)
    if key in OPEN1:
        return OPEN1[key]
    return build_jh(body)


def build_jh(body, finite=False):
    """finite: «… ဈာန်ကို ဝင်စား၍ နေ၏» (a statement, ^2-508 / ^2-638) instead of the time clause."""
    segs = [_tokens(s) for s in re.split(r" ?…pe… ?", body)]
    # purpose first (pi-1 2-03): «lokuttaraṃ jhānaṃ bhāveti niyyānikaṃ apacayagāmiṃ PURPOSE» -> PURPOSE၊ HEAD
    for t in segs:
        for i in range(len(t) - 1):
            if t[i][0] == "L" and t[i + 1][0] == "U":
                t[i], t[i + 1] = t[i + 1], t[i]
    outs, pend = [], []
    for t in segs:
        roles = "".join(r for r, _, _ in t)
        if not re.fullmatch(r"[UHLF]*A*F*(?:J(?:VQ*)?)?", roles):
            raise Miss("jhāna segment order: " + " ".join(k for _, _, k in t))
        pend += [m for r, m, _ in t if r == "A"]
        parts = [m for r, m, _ in t if r in "UHLF"]
        j = [m for r, m, _ in t if r == "J"]
        has_v = "V" in roles
        qs = (pend if has_v else []) + [m for r, m, _ in t if r == "Q"]
        x = ""
        if j:
            x = (f"{C} ".join(qs) + " " if qs else "") + j[0] + (
                (f"ကို {JH_UPAS_FIN}" if finite else f"ကို {JH_UPAS}") if has_v else "")
            if has_v:
                pend = []
        out = f"{C} ".join(parts)
        if x:
            out = (out + (f"{C} " if qs else " ") if out else "") + x
        outs.append(out)
    if pend:
        raise Miss("«…saññāsahagataṃ» without a jhāna: " + body[:80])
    out = (PE + " ").join(outs)
    if finite:
        return out
    return out + (" " if out.endswith("သော") else " ဖြစ်သော ") + YASMIM


# ===================================================================================== citta openings (ch14)
QUAL = dict(P1.QUAL)
QUAL.update({k: v for k, v in _Q.items() if k.endswith("ādhipateyyaṃ")})
QUAL.update({"hīnaṃ": T["hīnā"], "majjhimaṃ": T["majjhimā"], "paṇītaṃ": T["paṇītā"]})
ADV = dict(P1.QUAL_ADV)
KIND_KK = P1.CITTA_KIND["kāmāvacaraṃ kusalaṃ cittaṃ"]


def open_citta(body):
    """«kāmāvacaraṃ kusalaṃ cittaṃ uppannaṃ hoti Q … [objects] [X viramantassa]» (without «Yasmiṃ samaye»)."""
    key = VAR.sub("", body)
    if key in OPEN1:
        return OPEN1[key]
    m = re.fullmatch(r"kāmāvacar(?P<e>aṃ|e) kusalaṃ cittaṃ uppannaṃ hoti (?P<r>.+?)(?: (?P<g>\S+) viramantassa)?", body)
    if not m:
        raise Miss("citta opening: " + body[:80])
    if m["e"] == "e":
        SLIPS.append("^2-711 «kāmāvacare kusalaṃ cittaṃ» read as kāmāvacaraṃ")
    gen = f"{ABST[m['g']]}{VIRAMANTASSA} " if m["g"] else ""
    rest = m["r"]
    mo = re.fullmatch(r"(?P<q>.+?) (?P<o>rūpārammaṇaṃ vā…pe… dhammārammaṇaṃ vā) yaṃ yaṃ vā panārabbha", rest)
    obj = ""
    if mo:
        rest = mo["q"]
        obj = (f"{P1.ARAMMANA['rūpārammaṇaṃ']}{P1.ARAMMANA_VA}{PE} {P1.ARAMMANA['dhammārammaṇaṃ']}"
               f"{P1.ARAMMANA_VA}{C} {P1.YAM_YAM} ")
    segs = [s.split(" ") for s in re.split(r" ?…(?:pe…)? ?", rest)]
    outs = []
    tail_adv = ""
    for si, seg in enumerate(segs):
        parts = []
        for wi, w in enumerate(seg):
            if w in QUAL:
                parts.append(QUAL[w])
            elif w in ADV:
                if si == len(segs) - 1 and wi == len(seg) - 1:
                    tail_adv = ADV[w] + " "          # a final «sasaṅkhārena»: after «KIND-သည်», as r_open
                else:
                    parts.append(ADV[w])
            else:
                raise Miss("citta qualifier: " + w)
        outs.append(f"{C} ".join(parts))
    q = (PE + " ").join(outs)
    return f"{gen}{obj}{q} {KIND_KK}သည် {tail_adv}{P1.UPPANNA} {YASMIM}"


# ===================================================================================== sentence frames
SENT = {}        # Pāli sentence prefix -> Burmese (unique prose); the prefix must identify one sentence only
_SENT_SEEN = {}


def vuccati(dem, x):
    """«idaṃ / ayaṃ / ime / imā vuccati(nti) "X"(ti)» -> «ဤသည်(တို့)ကို “X”ဟု ခေါ်သည်»."""
    pl = dem in ("ime", "imā", "Ime", "Imā")
    m = re.fullmatch(r'"(?P<a>[^"]+)"(?:ti)?|(?P<b>[^"]+)', x)
    q = bool(m["a"])
    x = m["a"] or m["b"]
    my = lemma(x) if q else noun(x)[0]
    return f"ဤသည်{'တို့' if pl else ''}ကို {'“' + my + '”' if q else my}ဟု ခေါ်သည်"


LEM = {}         # quoted words (the commented phrases) -> Burmese


def lemma(x):
    k = x[:1].lower() + x[1:]
    for c in (k, k[:-1] + {"ī": "i", "ā": "a", "ū": "u"}.get(k[-1:], k[-1:])):
        if c in LEM:
            return LEM[c]
        if c in NOUNS:
            return NOUNS[c][0]
    raise Miss("lemma: " + x)


def list_my(text):
    """A synonym list (pāli words, «…pe…», «, », variants) -> Burmese items joined with «၊ » / «… »."""
    toks = re.findall(r"\[[^\]]*\]|…pe…|, |[^\s\[…,]+", text)
    words, var_after, pe_after, comma_after = [], {}, set(), set()
    for t in toks:
        if t.startswith("["):
            var_after.setdefault(len(words) - 1, []).append(t)
        elif t == "…pe…":
            pe_after.add(len(words) - 1)
        elif t == ", ":
            comma_after.add(len(words) - 1)
        else:
            words.append(t)
    out, i, seen = "", 0, {}
    while i < len(words):
        for k in range(ITEM_MAX, 0, -1):
            key = " ".join(words[i:i + k])
            key = key[:1].lower() + key[1:]
            if i + k <= len(words) and key in ITEMS and not any(j in pe_after for j in range(i, i + k - 1)):
                break
        else:
            raise Miss("list item: " + words[i] + "  in: " + text[:100])
        my = ITEMS[key]
        if my in seen and seen[my] != key:
            raise Miss(f"two items share «{my}»: {seen[my]} / {key}")
        seen[my] = key
        vs = [v for j in range(i, i + k) for v in var_after.get(j, [])]
        out += my + "".join(" " + F.var_my(v) for v in vs)
        last = i + k - 1
        i += k
        if i < len(words):
            out += (PE + " ") if last in pe_after else (C + " ")
        elif last in pe_after:
            out += PE
    return out


REL = "ရှိသမျှ"


def deflist(gen, lst):
    """«Yo / Yā / Yaṃ [tasmiṃ samaye] LIST» -> «[ထိုအချိန်၌] LIST ရှိသမျှ»."""
    return (_TS if gen else "") + list_my(lst) + " " + REL


SANTA = ["santā", "samitā", "vūpasantā", "atthaṅgatā", "abbhatthaṅgatā", "appitā", "byappitā", "sositā", "visositā",
         "byantīkatā"]
SANTA_MY = new("Calmed (santā … byantīkatā; new predicate list)", dict(zip(SANTA, [
    "ငြိမ်သက်သွား", "ငြိမ်းသွား", "ကောင်းစွာ ငြိမ်သက်သွား", F.DEF["atthaṅgat"].removesuffix("ပြီးသော") + "သွား",
    F.DEF["abbhatthaṅgat"].removesuffix("ပြီးသော") + "သွား", "ဆုံးခန်းတိုင်သွား", "လုံးဝ ဆုံးခန်းတိုင်သွား",
    "ခြောက်ခန်းသွား", "လုံးဝ ခြောက်ခန်းသွား", "အဆုံးသတ်သွား"])))
UPETO = ["upeto hoti", "samupeto", "upāgato", "samupāgato", "upapanno", "sampanno", "samannāgato"]
UPETO_MY = new("Endowed (upeto hoti … samannāgato; new)", dict(zip(UPETO, [
    "ပြည့်စုံ၏", "ကောင်းစွာ ပြည့်စုံ၏", "ရောက်ရှိ၏", "ကောင်းစွာ ရောက်ရှိ၏", "ရရှိ၏", "ပြည့်ဝ၏",
    "အညီအညွတ် ပြည့်စုံ၏"])))
SODHETI = ["sodheti", "visodheti", "parisodheti", "moceti", "vimoceti", "parimoceti"]
SODHETI_MY = new("Cleanses (sodheti … parimoceti; new)", dict(zip(SODHETI, [
    "သန့်စင်စေ၏", "အထူး သန့်စင်စေ၏", "အကြွင်းမဲ့ သန့်စင်စေ၏", "လွတ်စေ၏", "အထူး လွတ်စေ၏", "အကြွင်းမဲ့ လွတ်စေ၏"])))
IRIYATI = ["iriyati", "vattati", "pāleti", "yapeti", "yāpeti", "carati", "viharati"]
IRIYATI_MY = new("Dwells (iriyati … viharati; new)", dict(zip(IRIYATI, [
    "ဣရိယာပုထ်ကို ပြု၏", "လည်ပတ်၏", "စောင့်ရှောက်၏", "မျှတ၏", "မျှတစေ၏", "ကျင့်လည်၏", "နေ၏"])))
VIRATA = new("Verbs (new)", {"viharati": IRIYATI_MY["viharati"]})


def seq_my(text, table, pl=False):
    """A run of synonym verbs / predicates (with «…pe…») -> Burmese joined with «၊ » / «… »."""
    toks = re.split(r"( ?…pe… ?| )", text)
    out, i = "", 0
    words = [t for t in toks if t.strip() and "…" not in t]
    seps = [t for t in toks[1::2]]
    # rebuild with multiword keys
    s = text
    pos = 0
    res = []
    while pos < len(s):
        for k in sorted(table, key=len, reverse=True):
            if s.startswith(k, pos) and (pos + len(k) == len(s) or s[pos + len(k)] in " …"):
                res.append(table[k])
                pos += len(k)
                break
        else:
            raise Miss("verb: " + s[pos:pos + 40])
        m = re.match(r" ?…pe… ?| ", s[pos:])
        if m:
            res.append(PE + " " if "…" in m[0] else f"{C} ")
            pos += len(m[0])
    return "".join(res)



# ===================================================================================== variant readings (new)
for _k, _v in {"catutthiṃ": P1.LEKHANA, "abyāpajjhena": P1.LEKHANA, "abyāpajjho": P1.LEKHANA,
               "sammiñjite": P1.LEKHANA, "manussarāhaseyyakaṃ": P1.LEKHANA, "muggasuppatāya": P1.LEKHANA,
               "pādena pādaṃ": P1.PATHA, "bimbohanampi": P1.LEKHANA, "bhiṃsanakānametaṃ": P1.LEKHANA,
               "paññāpenti": P1.LEKHANA, "thīnaṃ": P1.LEKHANA, "thīyanā thīyitattaṃ": P1.LEKHANA,
               "dūsanā dūsitattaṃ": P1.LEKHANA}.items():
    F.VAR_KIND.setdefault(_k, _v)
EDNOTE = new("Editorial notes (new)", {
    "[gaṇanānupubbato (syā.) evamuparipi]":
        f"[{P1.LEKHANA} (Syā.): gaṇanānupubbato{C} အောက်တွင်လည်း ဤနည်းအတိုင်း]",
    "[ayaṃ pāṭho mātikāyaṃ natthi, niddese pana sabbapotthakesu dissati]":
        f"[ဤပါဌ်သည် ခေါင်းစဉ်စာရင်း၌ မရှိ{C} အကျယ်ဖွင့်ပြချက်၌မူ စာမူ အားလုံး၌ တွေ့ရသည်]"})


def var(v):
    return EDNOTE[v] if v in EDNOTE else F.var_my(v)


# ===================================================================================== the sentence engine
IDHA = "ဤသာသနာ၌"                         # idha (Vb ^2-509: in this view … in this dispensation)
BHIKKHU = "ရဟန်း"
IDHA_BH = f"{IDHA} {BHIKKHU}သည်"
AVASESA = "ကြွင်းကျန်သော"
new("Frames (new)", {"Idha bhikkhu": IDHA_BH, "avasesā dhammā X-sampayuttā": f"{AVASESA} {F.DHP}သည် Xနှင့် ယှဉ်တွဲကြသည်",
                     "Tena vuccati \"Q\"ti": "ထို့ကြောင့် “Q”ဟု ဆိုသည်", "\"Q\"ti (gloss)": "“Q”ဟူသည်",
                     "\"Q\"ti (before tattha / atthi)": "“Q”ဟူရာ၌"})
ANGA = {"pañc": "pañca", "catur": "catu", "tiv": "ti", "duv": "dvi"}
ANGA_MY = {k: f"{P1.count_my(P1._ANGA, v)} ရှိသော {JH}" for k, v in ANGA.items()}
new("Jhāna factors (counts)", {f"{k}aṅgikaṃ jhānaṃ": v for k, v in ANGA_MY.items()})
FACTOR = {"vitakko": P1.NAMES["vitakko"], "vicāro": P1.NAMES["vicāro"], "pīti": P1.NAMES["pīti"],
          "sukhaṃ": P1.NAMES["sukhaṃ"], "cittassekaggatā": P1.NAMES["cittassekaggatā"],
          "upekkhā": BV["upekkhā"], "sati": P1.SUT["sati"], "sampajaññaṃ": P1.SUT["sampajañña"],
          "sampasādo": "ကြည်လင်မှု", "pītisukhaṃ": f"ပီတိနှင့် {P1.NAMES['sukhaṃ']}"}
new("Jhāna factors (new)", {k: FACTOR[k] for k in ("sampasādo", "pītisukhaṃ")})
SAMP_INST = {"jhāna": JH, "veramaṇiyā": VERAMANI, "cetanāya": P1.CETANA, "mettāya": BV["mettā"],
             "karuṇāya": BV["karuṇā"], "muditāya": BV["muditā"], "upekkhāya": BV["upekkhā"]}
COUNT = {"Cattāri jhānāni": P1.count_my(JH, "catu"), "Catasso appamaññāyo": P1.count_my(APP, "catu"),
         "Pañca sikkhāpadāni": P1.count_my(SIKKHAPADA, "pañca")}
new("Frames (new)", COUNT)


def names_my(text):
    out = []
    for x in re.split(r", |…pe… ?", text):
        out.append(noun(x)[0])
    return f"{C} ".join(out)


def question(x):
    """«Tattha katamā X? / X…pe… Y?» -> «ထိုတို့အနက် X ဟူသည် အဘယ်နည်း»."""
    pieces = re.split(r" ?…pe… ?", x)
    out, pl = [], False
    for i, p in enumerate(pieces):
        m = re.fullmatch(r"(?:[Tt]attha )?(?:katam\w+ )?(?P<n>.+)", p)
        my, pl = noun(m["n"])
        lead = "ထိုတို့အနက် " if re.match(r"[Tt]attha katam", p) or i == 0 else ""
        hu = " ဟူသည်" if (lead or i == len(pieces) - 1) else ""
        out.append(f"{lead}{my}{hu}")
    return f"{PE} ".join(out) + f" အဘယ်{'တို့' if pl else ''}နည်း"


def rest_my(r):
    """What follows an opening: «tasmiṃ samaye …», «yā / yo tasmiṃ samaye LIST – idaṃ vuccati X», «phasso…»."""
    if r == "tasmiṃ samaye phasso hoti…pe… avikkhepo hoti":
        return f"{_TS}{P1.NAMES['phasso']} {F.HOTI}{PE} {P1.NAMES['avikkhepo']} {F.HOTI}"
    m = re.fullmatch(r"tasmiṃ samaye (?P<n>pañc|catur|tiv|duv)aṅgikaṃ jhānaṃ hoti(?P<d> –)? (?P<l>.+)", r)
    if m:
        fac = f"{C} ".join(FACTOR[x] for x in re.split(r",? ", m["l"]))
        if not m["d"]:
            SLIPS.append("^2-629 «caturaṅgikaṃ jhānaṃ hoti vicāro pīti sukhaṃ cittassekaggatā»: no dash, no commas")
        return f"{_TS}{ANGA_MY[m['n']]} {F.HOTI}{' –' if m['d'] else C} {fac}"
    m = re.fullmatch(r"(?:(?P<g>yā|yo) tasmiṃ samaye )?(?P<l>.+?) – (?P<dem>idaṃ|ayaṃ|ime|imā) vucca(?:ti|nti) (?P<x>.+)", r)
    if m:
        return f"{_TS if m['g'] else ''}{list_my(m['l'])}{' ' + REL if m['g'] else ''} – {vuccati(m['dem'], m['x'])}"
    raise Miss("after the opening: " + r[:100])


OPEN_RE = re.compile(r"(?P<idha>Idha bhikkhu )?(?:[Yy]asmiṃ samaye (?P<o>.+?)|(?P<t>Tasseva .+?))"
                     r"(?P<sep>, (?=(?:yā |yo )?tasmiṃ samaye)| (?=phasso…pe…))(?P<rest>.+)")


def opening_sentence(core):
    m = OPEN_RE.fullmatch(core)
    if not m:
        return None
    o = m["o"] or m["t"]
    om = open_citta(o) if o.startswith("kāmāvacar") else open_jh(o)
    return (IDHA_BH + " " if m["idha"] else "") + om + (f"{C} " if m["sep"].startswith(",") else " ") + \
        rest_my(m["rest"])


def core_my(s):
    """A Pāli sentence without its end mark -> Burmese without «။»."""
    r = opening_sentence(s)
    if r is not None:
        return r
    for rx, f in FRAMES:
        m = rx.fullmatch(s)
        if m:
            r = f(m)
            if r is not None:
                return r
    keys = [k for k in SENT if s.startswith(k)]
    if keys:
        k = max(keys, key=len)
        if _SENT_SEEN.setdefault(k, s) != s:
            raise Miss(f"SENT prefix «{k}» matches two sentences")
        return SENT[k]
    raise Miss("sentence: " + s[:140])


def sent_my(s):
    if s in SENT1:
        return SENT1[s]
    m = re.fullmatch(r"(?P<c>.*?)(?P<v>(?: \[[^\]]+\])*)(?P<pe>…pe…)?(?P<e>[.?])?", s)
    vs = "".join(" " + var(v) for v in re.findall(r"\[[^\]]+\]", m["v"]))
    return core_my(m["c"]) + vs + (PE if m["pe"] else "") + (END if m["e"] else "")


QT_RE = re.compile(r'"(?P<q>[^"]+)"(?P<n>n)?ti(?P<r>.*)')


def r_quoted(m):
    """«"Q"ti REST»: the commented word, then its explanation."""
    q = m["q"] + ("ṃ" if m["n"] else "")
    lm = "“" + lemma(q) + "”"
    r = m["r"]
    if r == "":
        return lm + "ဟူရာ၌"
    if r.lstrip().startswith("…pe… "):
        return lm + "ဟူသည်" + PE + " " + core_my(r.lstrip()[5:])
    r = r.removeprefix(",").removeprefix(" ")
    if re.match(r"(?:[Tt]attha |[Aa]tthi )", r):
        return lm + "ဟူရာ၌ " + core_my(r)
    return lm + "ဟူသည် " + core_my(r)


def r_tena(m):
    return f"ထို့ကြောင့် “{lemma(m['q'] + ('ṃ' if m['n'] else ''))}”ဟု ဆိုသည်"


def r_question(m):
    return question(m["x"])


def r_qpe_close(m):
    return question(m["x"]) + f"{PE} " + vuccati(m["dem"], m["v"])


BODY_FULL = {"Idhekacco veḷudānena", "Idhekacco na veḷudānena", "Idhekacco vesiyāgocaro", "Idhekacco na vesiyāgocaro",
             "tāni vajjāni appamattakāni", "Pañcupādānakkhandhā loko", "Chando kāmo"}
BODY = {}       # definitions that are not (only) synonym lists: pāli prefix -> (burmese prefix, «ရှိသမျှ» after)


def body_my(lst, y):
    keys = [k for k in BODY if lst.startswith(k)]
    if keys:
        k = max(keys, key=len)
        pre, rel = BODY[k]
        rest = lst[len(k):].strip()
        if k in BODY_FULL:                         # a whole sentence: the prefix names it (one sentence only)
            if _SENT_SEEN.setdefault("BODY " + k, lst) != lst:
                raise Miss(f"BODY prefix «{k}» matches two sentences")
            rest = ""
        out = pre + ((" " if not pre.endswith(C) else " ") + list_my(rest) if rest else "")
        return out + (" " + REL if rel else "")
    return list_my(lst) + (" " + REL if y else "")


def r_def(m):
    return f"{body_my(m['l'], m['y'])} – {vuccati(m['dem'], m['v'])}"


def r_idam(m):
    return vuccati(m["dem"], m["v"])


def r_avasesa(m):
    return f"{AVASESA} {F.DHP}သည် {SAMP_INST[m['x']]}နှင့် ယှဉ်တွဲကြသည်"


def r_count(m):
    return f"{COUNT[m['n']]} – {names_my(m['l'])}"


def r_atthi(m):
    return f"{FACTOR_N(m['a'])} {F.HOTI}{C} {FACTOR_N(m['b'])} {F.HOTI}"


def FACTOR_N(x):
    return noun(x)[0] if x[:1].lower() + x[1:] in NOUNS else lemma(x)


def r_santa(m):
    pl = m["h"] == "honti"
    k = "ကြ" if pl else ""
    seq = [SANTA_MY[w] + f"{k}သည်" for w in SANTA]
    pre = "ရှေးဦးကပင် " if m["pb"] else ""
    return f"{subj_my(m['s'])} {pre}" + f"{C} ".join(seq)


SUBJ = {}       # «X santā honti …», «Idaṃ cittaṃ …» subjects -> Burmese (with «သည်»)


def subj_my(s):
    if s not in SUBJ:
        raise Miss("subject: " + s)
    return SUBJ[s]


def r_sahagata(m):
    return f"ဤ{noun(m['s'])[0]}သည် ဤ{INST[m['x']]}နှင့်အတူ ဖြစ်၏{C} အတူ ဖြစ်ပေါ်၏{C} ရောနှော၏{C} ယှဉ်တွဲ၏"


INST = {"mettāya": BV["mettā"], "karuṇāya": BV["karuṇā"], "muditāya": BV["muditā"], "upekkhāya": BV["upekkhā"],
        "pītiyā": P1.NAMES["pīti"]}
new("Frames (new)", {"Idaṃ X imāya Y sahagataṃ hoti sahajātaṃ saṃsaṭṭhaṃ sampayuttaṃ":
                     f"ဤXသည် ဤYနှင့်အတူ ဖြစ်၏{C} အတူ ဖြစ်ပေါ်၏{C} ရောနှော၏{C} ယှဉ်တွဲ၏"})


def r_sodheti(m):
    return f"ဤ{P1.MIND}ကို ဤ{SODH_X[m['x']]}မှ " + seq_my(m["v"], SODHETI_MY)


SODH_X = {}


def r_upeto(m):
    return f"{UPETO_X[m['x']]} " + seq_my(m["v"], UPETO_MY)


UPETO_X = {}


def r_iriyati(m):
    return seq_my(m[0], IRIYATI_MY)


def r_kusala(m):
    return P1.IME_KUSALA


def r_sikkha(m):
    return f"ဤ{F.DHP}သည် {SIKKHA} {F.COP[True]}"


def r_katame_sikkha(m):
    return f"{SIKKHA} ဖြစ်သော {F.DHP} ဟူသည် အဘယ်တို့နည်း"


def _AV(s):
    mm = re.fullmatch(r"[Aa]vasesā dhammā (?P<x>\S+?) ?sampayuttā", s)
    return r_avasesa(mm)


def r_colo(m):
    return COLO[m["c"]]


def r_sq_tail(m):
    """«Tattha katamaṃ SP, yasmiṃ samaye …» (^2-706: a comma for the question mark)."""
    SLIPS.append("^2-706 «Tattha katamaṃ … sikkhāpadaṃ, yasmiṃ samaye …»: comma for «?»")
    return question(m["x"]) + f"{C} " + opening_sentence(m["o"])


FRAMES_SRC = [
    (r"(?P<c>Suttantabhājanīyaṃ|Abhidhammabhājanīyaṃ|Pañhāpucchakaṃ|Catukkaṃ|Pañcakaṃ|\S+vibhaṅgo niṭṭhito)", r_colo),
    (r"(?P<a>Avasesā dhammā \S+ sampayuttā) ?…pe… (?P<b>avasesā dhammā \S+ sampayuttā) ?…pe… (?P<c>phasso…pe… .+)",
     lambda m: f"{_AV(m['a'])}{PE} {_AV(m['b'])}{PE} {rest_my(m['c'])}"),
    (r"Tattha katamaṃ (?P<x>surāmerayamajjapamādaṭṭhānā veramaṇī sikkhāpadaṃ), (?P<o>yasmiṃ samaye .+)", r_sq_tail),
    (r"[Tt]attha katam\w+ (?P<x>[^?]+?)…pe… (?P<dem>idaṃ|ayaṃ|ime|imā) vucca(?:ti|nti) (?P<v>\"[^\"]+\")", r_qpe_close),
    (r"(?P<x>[Tt]attha katam\w+ [^?]+)", r_question),
    (r'"(?P<q>[^"]+)"(?P<n>n)?ti(?P<r>.*)', r_quoted),
    (r'[Tt]ena vuccati "(?P<q>[^"]+)"(?P<n>n)?ti', r_tena),
    (r"(?P<y>(?:Yo|Yā|Yaṃ|Ye|Yāni) )?(?P<l>.+?) – (?P<dem>idaṃ|ayaṃ|ime|imā) vucca(?:ti|nti) (?P<v>.+)", r_def),
    (r"(?P<dem>Idaṃ|Ayaṃ|Ime|Imā) vucca(?:ti|nti) (?P<v>\"[^\"]+\")", r_idam),
    (r"[Aa]vasesā dhammā (?P<x>\S+?) ?sampayuttā(?:ti)?", r_avasesa),
    (r"(?P<n>Cattāri jhānāni|Catasso appamaññāyo|Pañca sikkhāpadāni) – (?P<l>[^–]+)", r_count),
    (r"Ime dhammā kusalā", r_kusala),
    (r"Ime dhammā sikkhā", r_sikkha),
    (r"Katame dhammā sikkhā", r_katame_sikkha),
    (r"[Aa]tthi (?P<a>[^\s,]+)(?P<v> \[[^\]]+\])?,? atthi (?P<b>[^\s,]+)",
     lambda m: r_atthi(m).replace(f" {F.HOTI}{C}", (f" {var(m['v'][1:])}" if m["v"] else "") + f" {F.HOTI}{C}", 1)),
    (r"(?P<s>.+?) (?P<pb>pubbeva )?santā (?P<h>hoti|honti) samitā vūpasantā atthaṅgatā abbhatthaṅgatā appitā byappitā "
     r"sositā visositā byantīkatā", r_santa),
    (r"Idaṃ (?P<s>cittaṃ|sukhaṃ) imāya (?P<x>\S+) sahagataṃ hoti sahajātaṃ saṃsaṭṭhaṃ sampayuttaṃ", r_sahagata),
    (r"Idaṃ cittaṃ (?P<x>.+?) (?P<v>sodheti visodheti parisodheti moceti vimoceti parimoceti)", r_sodheti),
    (r"(?P<x>.+?) (?P<v>upeto hoti.*samannāgato)", r_upeto),
    (r"iriyati vattati pāleti yapeti yāpeti carati viharati", r_iriyati),
]
FRAMES = []


def rebuild_frames():
    FRAMES[:] = [(re.compile(p), f) for p, f in FRAMES_SRC]




# ===================================================================================== chapter 13 (Appamaññā)
TOG = P1.TOGETHER
DISA = "အရပ်"
EKAM_DISAM = f"{DISA} တစ်မျက်နှာ"
PHARITVA = "ပျံ့နှံ့စေ၍"
VIHARATI = IRIYATI_MY["viharati"]                       # နေ၏
TATHA = "ထို့အတူ"
TATHA_N = {o: f"{TATHA} {P1.ORD[o]} {DISA}ကို" for o in ("dutiya", "tatiya", "catuttha")}
ITI_UDDHAM = "ဤသို့ အထက်၊ အောက်၊ ဖီလာ၊ နေရာတိုင်း၌ ခပ်သိမ်းသော သဘောဖြင့် အားလုံး ပါဝင်သော လောကကို"
SABBADHI = "နေရာတိုင်း၌ ခပ်သိမ်းသော သဘောဖြင့် အားလုံး ပါဝင်သော လောက"
VIPULA = "ပြန့်ပြောသော"
AVERA, ABYAPAJJA = "ရန်ငြိုး မရှိ", "ညှဉ်းဆဲလိုမှု မရှိ"
VIPULA5 = f"{VIPULA}{C} {T['mahaggatā']}{C} {T['appamāṇā']}{C} {AVERA}သော{C} {ABYAPAJJA}သော"


def saha_cetasa(b):
    return f"{BV[b]}{TOG} {CITTA}ဖြင့်"


for _b in BV:
    LEM[f"{_b}sahagatena cetasā"] = saha_cetasa(_b)
LEM.update({"ekaṃ disaṃ": EKAM_DISAM, "pharitvā": PHARITVA, "viharati": VIHARATI, "tathā dutiyaṃ": TATHA_N["dutiya"],
            "sabbadhi sabbattatāya sabbāvantaṃ lokaṃ": SABBADHI, "vipulena": VIPULA})
B_ALT = "(?P<b>mettā|karuṇā|muditā|upekkhā)"


def b_ekam(m):
    b = m["b"].lower()
    sep = f"{C} " if m["c"] else f"{C} "
    return (f"{saha_cetasa(b)} {EKAM_DISAM}ကို {PHARITVA} {VIHARATI}{C} {TATHA_N['dutiya']}{C} {TATHA_N['tatiya']}"
            f"{C} {TATHA_N['catuttha']}")


def b_iti(m):
    return f"{ITI_UDDHAM} {VIPULA5}{(' ' + var(m['v'])) if m['v'] else ''} {saha_cetasa(m['b'].lower())} {PHARITVA} {VIHARATI}"


EKAM_RX = r"(?P<b>[Mm]ettā|[Kk]aruṇā|[Mm]uditā|[Uu]pekkhā)sahagatena cetasā ekaṃ disaṃ pharitvā viharati(?P<c>,)? tathā " \
          r"dutiyaṃ,? tathā tatiyaṃ,? tathā catutthaṃ"
ITI_RX = r"[Ii]ti uddhamadho tiriyaṃ sabbadhi sabbattatāya sabbāvantaṃ lokaṃ (?P<b>mettā|karuṇā|muditā|upekkhā)sahagatena " \
         r"cetasā vipulena mahaggatena appamāṇena averena abyāpajjena(?: (?P<v>\[[^\]]+\]))? pharitvā viharati"


def b_long(m):
    """^2-699: the four in one sentence («…; …»), each «X…, iti …»."""
    parts = []
    for p in m["body"].split("; "):
        a, b = p.split(", iti ")
        ma = re.fullmatch(r"(?:idha bhikkhu )?" + EKAM_RX, a)
        mb = re.fullmatch(ITI_RX, "iti " + b)
        if not ma or not mb:
            raise Miss("appamaññā clause: " + p[:80])
        parts.append((IDHA_BH + " " if a.startswith("idha") else "") + b_ekam(ma) + f"{C} " + b_iti(mb))
    return f"{COUNT['Catasso appamaññāyo']} – " + f"{C} ".join(parts)


SEYYATHA = {"piyaṃ manāpaṃ": f"ချစ်ရသော{C} {P1.MANAPA if hasattr(P1, 'MANAPA') else F.C3['MANAPA']}",
            "duggataṃ durūpetaṃ": f"ဆင်းရဲ ဒုက္ခရောက်နေသော{C} ကံဆိုးသော",
            "neva manāpaṃ na amanāpaṃ": f"{F.C3['MANAPA'].removesuffix('သော')}သည်လည်း မဟုတ်{C} "
                                        f"{F.C3['AMANAPA'].removesuffix('သော')}သည်လည်း မဟုတ်သော"}
SEYY_V = {"mettāyeyya": f"{BV['mettā']} ထားသကဲ့သို့", "karuṇāyeyya": f"{BV['karuṇā']} ထားသကဲ့သို့",
          "mudito assa": f"{BV['muditā']} ရှိသူ ဖြစ်ရာသကဲ့သို့", "upekkhako assa": f"{BV['upekkhā']} ရှိသူ ဖြစ်ရာသကဲ့သို့"}
new("Appamaññā (new)", {**LEM, "Iti uddhamadho tiriyaṃ …": ITI_UDDHAM, "vipulena … abyāpajjena": VIPULA5,
                        **SEYYATHA, **SEYY_V})


def r_seyy(m):
    return (f"ဥပမာအားဖြင့် {SEYYATHA[m['o']]} ပုဂ္ဂိုလ် တစ်ယောက်ကို မြင်၍ {SEYY_V[m['v']]}{C} ထို့အတူပင် "
            f"သတ္တဝါ အားလုံးကို {INST[m['b']]}ဖြင့် {PHARITVA.removesuffix('၍')}၏")


FRAMES_SRC[:0] = [
    (r"Catasso appamaññāyo – (?P<body>idha bhikkhu .+; .+)", b_long),
    (r"Catasso appamaññāyo – idha bhikkhu " + EKAM_RX, lambda m: f"{COUNT['Catasso appamaññāyo']} – {IDHA_BH} {b_ekam(m)}"),
    (EKAM_RX, b_ekam),
    (ITI_RX, b_iti),
    (r"Kathañca bhikkhu (?P<b>mettā|karuṇā|muditā|upekkhā)sahagatena cetasā ekaṃ disaṃ pharitvā viharati",
     lambda m: f"{BHIKKHU}သည် {saha_cetasa(m['b'])} {EKAM_DISAM}ကို အဘယ်သို့ {PHARITVA} နေသနည်း"),
    (r"Seyyathāpi nāma ekaṃ puggalaṃ (?P<o>.+?) disvā (?P<v>mettāyeyya|karuṇāyeyya|mudito assa|upekkhako assa), "
     r"evameva sabbe satte (?P<b>mettāya|karuṇāya|muditāya|upekkhāya) pharati", r_seyy),
    (r"yaṃ vipulaṃ taṃ mahaggataṃ, yaṃ mahaggataṃ taṃ appamāṇaṃ, yaṃ appamāṇaṃ so avero, yo avero so abyāpajjo",
     lambda m: (f"အကြင်စိတ်သည် {VIPULA.removesuffix('သော')}၏{C} ထိုစိတ်သည် {T['mahaggatā'].removesuffix('သော')}၏{C} "
                f"အကြင်စိတ်သည် {T['mahaggatā'].removesuffix('သော')}၏{C} ထိုစိတ်သည် {T['appamāṇā'].removesuffix('သော')}{C} "
                f"အကြင်စိတ်သည် {T['appamāṇā'].removesuffix('သော')}{C} ထိုစိတ်သည် {AVERA}{C} "
                f"အကြင်စိတ်သည် {AVERA}{C} ထိုစိတ်သည် {ABYAPAJJA}")),
]
SENT.update({
    "puratthimaṃ vā disaṃ pacchimaṃ vā disaṃ uttaraṃ vā disaṃ dakkhiṇaṃ vā disaṃ uddhaṃ vā adho vā tiriyaṃ vā vidisaṃ vā":
        f"အရှေ့ {DISA}ကိုဖြစ်စေ{C} အနောက် {DISA}ကိုဖြစ်စေ{C} မြောက် {DISA}ကိုဖြစ်စေ{C} တောင် {DISA}ကိုဖြစ်စေ{C} "
        f"အထက်ကိုဖြစ်စေ{C} အောက်ကိုဖြစ်စေ{C} ဖီလာကိုဖြစ်စေ{C} {DISA}ကြားကိုဖြစ်စေ ဆိုလိုသည်",
    "pharitvā adhimuccitvā": f"{PHARITVA}{C} စိတ်ကို ညွတ်စေ၍ ဟု ဆိုလိုသည်",
    "yatheva ekaṃ disaṃ tathā dutiyaṃ disaṃ tathā tatiyaṃ disaṃ tathā catutthaṃ disaṃ tathā uddhaṃ tathā adho tathā "
    "tiriyaṃ tathā vidisaṃ":
        f"{EKAM_DISAM}ကို {PHARITVA.removesuffix('၍')}သကဲ့သို့ {TATHA_N['dutiya']}{C} {TATHA_N['tatiya']}{C} "
        f"{TATHA_N['catuttha']}{C} {TATHA} အထက်ကို{C} {TATHA} အောက်ကို{C} {TATHA} ဖီလာကို{C} {TATHA} {DISA}ကြားကို "
        f"{PHARITVA.removesuffix('၍')}ခြင်းကို ဆိုလိုသည်",
    "sabbena sabbaṃ sabbathā sabbaṃ asesaṃ nissesaṃ":
        f"အားလုံးကို အားလုံးဖြင့်{C} အားလုံးကို အလုံးစုံဖြင့်{C} အကြွင်းအကျန် မရှိ{C} အကုန်အစင် ဆိုလိုသည်",
    "Pariyādāyavacanametaṃ – \"sabbadhi sabbattatāya sabbāvantaṃ loka\"nti":
        f"ဤသည်မှာ အကုန် သိမ်းကျုံး၍ ဆိုသော စကား ဖြစ်သည် – “{SABBADHI}”ဟူ၍",
})
SUBJ.update({})



# ===================================================================================== chapter 12 (Jhāna)
JF = P1.JH_FORM
AB = P1.JH_ARUPA_BASE
SO = f"ထို{BHIKKHU}သည်"                                   # So (that monk)
ABHIJJHA = P1.SYN.get("abhijjhā") or ITEMS.get("abhijjhā") or "သူ့ဥစ္စာကို လိုချင်ခြင်း"
BYAPADA, PADOSA = P1.JH_BYAPADA, ITEMS["padoso"]
THINA, MIDDHA = ITEMS["thinaṃ"], ITEMS["middhaṃ"]
UDDH, KUKK, VIC = P1.UDDHACCA, P1.KUKKUCCA, P1.VICIKICCHA
SAMPAJ = P1.SUT["sampajañña"]                             # ကောင်းစွာ ဆင်ခြင်သိမြင်ခြင်း
SAMPAJ_L = SAMPAJ.removesuffix("ခြင်း") + "လျက်"
SATI = P1.SUT["sati"]
SENA = "အိပ်ရာ နေရာ"                                       # senāsana (bed and seat)
SODH_MY = SODHETI_MY["parisodheti"]
PATI = "ပါတိမောက်"
NIVARANA5 = f"ဤ{P1.count_my('အတားအဆီး', 'pañca')}"
SKARI = f"{SAMPAJ_L} ပြုလေ့ရှိသူ ဖြစ်၏"                    # sampajānakārī hoti
SATO_SAMPAJANO = f"{SATI} ရှိလျက် {SAMPAJ_L}"
UPAKK = ITEMS.get("upakkileso", "ညစ်နွမ်းစေတတ်သော အညစ်အကြေး")
G_ACT = {   # the activities of ^2-508 / 523 / 525
    "abhikkante paṭikkante": "ရှေ့သို့ တိုးရာ၊ နောက်သို့ ဆုတ်ရာ၌", "ālokite vilokite": "ရှေ့သို့ ကြည့်ရာ၊ ဘေးသို့ ကြည့်ရာ၌",
    "samiñjite pasārite": "ကွေးရာ၊ ဆန့်ရာ၌", "saṅghāṭipattacīvaradhāraṇe": "ဒုကုဋ်၊ သပိတ်၊ သင်္ကန်းကို ဆောင်ရာ၌",
    "asite pīte khāyite sāyite": "စားရာ၊ သောက်ရာ၊ ခဲရာ၊ လျက်ရာ၌", "uccārapassāvakamme": "ကျင်ကြီး ကျင်ငယ် စွန့်ရာ၌",
    "gate ṭhite nisinne sutte jāgarite bhāsite tuṇhībhāve":
        "သွားရာ၊ ရပ်ရာ၊ ထိုင်ရာ၊ အိပ်ရာ၊ နိုးရာ၊ ပြောဆိုရာ၊ ဆိတ်ဆိတ်နေရာ၌"}
V_ACT = {"abhikkamati": "ရှေ့သို့ တိုး၏", "paṭikkamati": "နောက်သို့ ဆုတ်၏", "āloketi": "ရှေ့သို့ ကြည့်၏",
         "viloketi": "ဘေးသို့ ကြည့်၏", "samiñjeti": "ကွေး၏", "pasāreti": "ဆန့်၏"}
new("Jhāna chapter: activities (new)", {**G_ACT, **V_ACT, "sampajānakārī hoti": SKARI})
SENA_ITEMS = {"mañco": "ညောင်စောင်း", "pīṭhaṃ": "ခုံ", "bhisi": "မွေ့ရာ", "bibbohanaṃ": "ခေါင်းအုံး",
              "vihāro": "ကျောင်း", "aḍḍhayogo": "တစ်ခြမ်းမိုး ကျောင်း", "pāsādo": "ပြာသာဒ်", "aṭṭo": "ရဲတိုက်",
              "māḷo": "ဝန်းဝိုင်း အဆောင်", "leṇaṃ": "လှိုဏ်ဂူ", "guhā": "ဂူ", "rukkhamūlaṃ": "သစ်ပင်ရင်း",
              "veḷugumbo": "ဝါးရုံ"}
PLACE = {"araññaṃ": "တော", "rukkhamūlaṃ": "သစ်ပင်ရင်း", "pabbataṃ": "တောင်", "kandaraṃ": "ချောက်",
         "giriguhaṃ": "တောင်ဂူ", "susānaṃ": "သုသာန်", "vanapatthaṃ": "တောအုပ်ကြီး", "abbhokāsaṃ": "လွင်တီးခေါင်",
         "palālapuñjaṃ": "ကောက်ရိုးပုံ"}
QUIET = {"appasaddaṃ": "အသံ နည်း", "appanigghosaṃ": "ဆူညံသံ နည်း", "vijanavātaṃ": "လူသူ ကင်း",
         "manussarāhasseyyakaṃ": "လူတို့ လျှို့ဝှက်စွာ နေရာ ဖြစ်", "paṭisallānasāruppaṃ": "တစ်ယောက်တည်း ကိန်းအောင်းရန် သင့်လျော်"}
new("Jhāna chapter: dwellings (new)", {**SENA_ITEMS, **PLACE, **{k: v + "သော" for k, v in QUIET.items()}})
BOJJH = {"satisambojjhaṅgo": f"{SATI} ဗောဇ္ဈင်", "dhammavicayasambojjhaṅgo": f"{P1.SYN['dhammavicayo']} ဗောဇ္ဈင်",
         "vīriyasambojjhaṅgo": f"{P1.SYN['vīriyaṃ']} ဗောဇ္ဈင်", "pītisambojjhaṅgo": f"{P1.NAMES['pīti']} ဗောဇ္ဈင်",
         "passaddhisambojjhaṅgo": f"{P1.SYN['passaddhi']} ဗောဇ္ဈင်", "samādhisambojjhaṅgo": "သမာဓိ ဗောဇ္ဈင်",
         "upekkhāsambojjhaṅgo": f"{BV['upekkhā']} ဗောဇ္ဈင်"}
add_items(BOJJH.items(), "pi-1 pattern (make_ch2-02-03)")
VIT = {"kāyiko vītikkamo": "ကိုယ်ဖြင့် ကျူးလွန်ခြင်း", "vācasiko vītikkamo": "နှုတ်ဖြင့် ကျူးလွန်ခြင်း",
       "kāyikavācasiko vītikkamo": "ကိုယ်နှုတ်ဖြင့် ကျူးလွန်ခြင်း"}
VIT.update({k.replace("vītikkamo", "avītikkamo"): v.replace("ကျူးလွန်ခြင်း", "မကျူးလွန်ခြင်း") for k, v in list(VIT.items())})
add_items(new("Jhāna chapter: list items (new)", {
    **VIT, "kāmacchando": "ကာမကို လိုလားမှု", "byāpādo": BYAPADA, "uddhaccaṃ": UDDH,
    "rūpasaññā": "အဆင်းအရောင်ဟု မှတ်သိမှု", "saddasaññā": "အသံဟု မှတ်သိမှု", "phoṭṭhabbasaññā": "အထိအတွေ့ဟု မှတ်သိမှု",
    "saññākkhandho": P1.NAMES["saññākkhandho"], "saṅkhārakkhandho": P1.NAMES["saṅkhārakkhandho"],
    "viññāṇakkhandho": P1.NAMES["viññāṇakkhandho"], "evarūpaṃ kukkuccaṃ": f"ဤသို့ သဘောရှိသော {KUKK}"}).items(), "new")
NOUNS.update({
    "anācāro": ("မသင့်တော်သော အကျင့်", False), "ācāro": ("အကျင့်", False), "agocaro": ("မကျက်စားသင့်ရာ", False),
    "gocaro": ("ကျက်စားရာ", False), "aṇumattā vajjā": ("အနည်းငယ်မျှသော အပြစ်", True), "sikkhā": (SIKKHA, False),
    "indriyesu aguttadvāratā": (ITEMS and "အာရုံခံ အင်္ဂါတို့၏ တံခါးကို မစောင့်ထိန်းခြင်း", False),
    "indriyesu guttadvāratā": ("အာရုံခံ အင်္ဂါတို့၏ တံခါးကို စောင့်ထိန်းခြင်း", False),
    "bhojane amattaññutā": ("အစားအစာ၌ အတိုင်းအရှည်ကို မသိခြင်း", False),
    "bhojane mattaññutā": ("အစားအစာ၌ အတိုင်းအရှည်ကို သိခြင်း", False),
    "bodhipakkhikā dhammā": ("ဗောဓိပက္ခိယ သဘောတရား", True), "abhijjhā": (ABHIJJHA, False), "loko": ("လောက", False),
    "byāpādo": (BYAPADA, False), "padoso": (PADOSA, False), "kāmā": ("ကာမ", True),
    "akusalā dhammā": (f"{T['akusalā']} {F.DH}", True), "kāyo": (P1.KAYA, False), "ariyā": ("အရိယာ", True),
    "dukkhaṃ": (P1.DUKKHA + "မှု", False), "somanassaṃ": (P1.SOMANASSA, False), "domanassaṃ": ("စိတ်ဆင်းရဲမှု", False),
    "rūpasaññā": ("ရုပ်ဟု မှတ်သိမှု", False), "paṭighasaññā": (f"{P1.IMPACT}ဟု မှတ်သိမှု", False),
    "nānattasaññā": ("အမျိုးမျိုး ကွဲပြားမှုဟု မှတ်သိမှု", False), "ākāso": ("ဟင်းလင်းပြင်", False),
    "paṭighasaññāyo": (f"{P1.IMPACT}ဟု မှတ်သိမှုတို့", True), "vicāro": (P1.NAMES["vicāro"], False),
})
SAMP_PRED = f"{SAMPAJ.removesuffix('ခြင်း')}သူ"
LEM.update({
    "idha": IDHA, "bhikkhū": BHIKKHU, "pātimokkhaṃ": PATI, "viharati": VIHARATI,
    "pātimokkhasaṃvarasaṃvuto": f"{PATI} စောင့်စည်းမှုဖြင့် စောင့်စည်းသူ",
    "ācāragocarasampanno": "အကျင့်နှင့် ကျက်စားရာ ပြည့်စုံသူ", "gocaro": "ကျက်စားရာ",
    "aṇumattesu vajjesu bhayadassāvī": "အနည်းငယ်မျှသော အပြစ်တို့၌ ဘေးကို မြင်လေ့ရှိသူ",
    "samādāya sikkhati sikkhāpadesu": f"{SIKKHAPADA}တို့၌ ဆောက်တည်၍ ကျင့်၏",
    "sikkhāyo": f"{SIKKHA}များ",
    "indriyesu guttadvāro": "အာရုံခံ အင်္ဂါတို့၏ တံခါးကို စောင့်ထိန်းသူ",
    "bhojane mattaññū": "အစားအစာ၌ အတိုင်းအရှည်ကို သိသူ",
    "pubbarattāpararattaṃ jāgariyānuyogamanuyutto": "ညဉ့်ဦးယံ ညဉ့်နောက်ယံ၌ နိုးကြားမှုကို အားထုတ်သူ",
    "sātaccaṃ": "အစဉ်တစိုက် ဖြစ်ခြင်း", "nepakkaṃ": "ပညာ ရင့်ကျက်ခြင်း",
    "bodhipakkhikānaṃ dhammānaṃ bhāvanānuyogamanuyutto": "ဗောဓိပက္ခိယ သဘောတရားတို့ကို ပွားများခြင်း၌ အားထုတ်သူ",
    "sampajāno": SAMP_PRED, "vivittaṃ": "ဆိတ်ငြိမ်သော", "senāsanaṃ": SENA,
    "vivittaṃ senāsanaṃ bhajati": f"ဆိတ်ငြိမ်သော {SENA}ကို မှီဝဲ၏", "araññaṃ": PLACE["araññaṃ"],
    "rukkhamūlaṃ": PLACE["rukkhamūlaṃ"], "vanapatthaṃ": PLACE["vanapatthaṃ"], "appasaddaṃ": QUIET["appasaddaṃ"] + "သော",
    "appanigghosaṃ": QUIET["appanigghosaṃ"] + "သော",
    "araññagato vā rukkhamūlagato vā suññāgāragato vā": "တောသို့ ရောက်သည်ဖြစ်စေ၊ သစ်ပင်ရင်းသို့ ရောက်သည်ဖြစ်စေ၊ "
                                                         "ဆိတ်ငြိမ်ရာ အိမ်သို့ ရောက်သည်ဖြစ်စေ",
    "nisīdati pallaṅkaṃ ābhujitvā": "ထက်ဝယ်ဖွဲ့ခွေ၍ ထိုင်၏", "ujuṃ kāyaṃ paṇidhāya": "ကိုယ်ကို ဖြောင့်မတ်စွာ ထား၍",
    "parimukhaṃ satiṃ upaṭṭhapetvā": f"ရှေ့မှောက်၌ {SATI}ကို ထင်စေ၍",
    "abhijjhaṃ loke pahāya": f"လောက၌ {ABHIJJHA}ကို ပယ်၍", "vigatābhijjhena cetasā": f"{ABHIJJHA} ကင်းသော {CITTA}ဖြင့်",
    "abhijjhāya cittaṃ parisodheti": f"{ABHIJJHA}မှ {CITTA}ကို {SODH_MY}",
    "byāpādapadosaṃ pahāya": f"{BYAPADA}နှင့် {PADOSA}ကို ပယ်၍",
    "abyāpannacitto": f"{BYAPADA} မရှိသော {CITTA} ရှိသူ",
    "byāpādapadosā cittaṃ parisodheti": f"{BYAPADA}နှင့် {PADOSA}မှ {CITTA}ကို {SODH_MY}",
    "thinamiddhaṃ pahāya": f"{THINA}နှင့် {MIDDHA}ကို ပယ်၍", "vigatathinamiddho": f"{THINA}နှင့် {MIDDHA} ကင်းသူ",
    "ālokasaññī": "အလင်းဟု မှတ်သိသူ", "sato sampajāno": SATO_SAMPAJANO,
    "thinamiddhā cittaṃ parisodheti": f"{THINA}နှင့် {MIDDHA}မှ {CITTA}ကို {SODH_MY}",
    "uddhaccakukkuccaṃ pahāya": f"{UDDH}နှင့် {KUKK}ကို ပယ်၍", "anuddhato": "မယောက်ယက်ခတ်သူ",
    "vūpasantacitto": f"ကောင်းစွာ ငြိမ်သက်သော {CITTA} ရှိသူ",
    "ajjhattaṃ vūpasantacitto": f"မိမိ၌ ကောင်းစွာ ငြိမ်သက်သော {CITTA} ရှိသူ",
    "uddhaccakukkuccā cittaṃ parisodheti": f"{UDDH}နှင့် {KUKK}မှ {CITTA}ကို {SODH_MY}",
    "vicikicchaṃ pahāya": f"{VIC}ကို ပယ်၍", "tiṇṇavicikiccho": f"{VIC}ကို ကူးမြောက်သူ",
    "akathaṃkathī kusalesu dhammesu": f"{T['kusalā']} {F.DH}တို့၌ ‘အဘယ်သို့နည်း’ဟု မတွေးတောသူ",
    "vicikicchāya cittaṃ parisodheti": f"{VIC}မှ {CITTA}ကို {SODH_MY}",
    "ime pañca nīvaraṇe pahāya": f"{NIVARANA5}တို့ကို ပယ်၍",
    "cetaso upakkilese": f"{CITTA}ကို ညစ်နွမ်းစေတတ်သော အညစ်အကြေးများ",
    "paññāya dubbalīkaraṇe": "ပညာကို အားနည်းစေတတ်ကုန်သော",
    "vivicceva kāmehi vivicca akusalehi dhammehi": f"{JF['vivicceva kāmehi']}{C} {JF['vivicca akusalehi dhammehi']}",
    "savitakkaṃ savicāraṃ": f"{JF['savitakkaṃ']}{C} {JF['savicāraṃ']}", "vivekajaṃ": "ကင်းဆိတ်ခြင်းမှ ဖြစ်ပေါ်သော",
    "pītisukhaṃ": FACTOR["pītisukhaṃ"], "jhānaṃ": JH, "upasampajja": "ဝင်စား၍",
    "ajjhattaṃ": "မိမိ၌", "sampasādanaṃ": FACTOR["sampasādo"], "samādhijaṃ": "သမာဓိမှ ဖြစ်ပေါ်သော",
    "avitakkaṃ avicāraṃ": f"{JF['avitakkaṃ']}{C} {JF['avicāraṃ']}", "upekkhako": f"{BV['upekkhā']} ရှိသူ",
    "yaṃ taṃ ariyā ācikkhanti": "အရိယာတို့ ပြောကြားကြသော",
    "upekkhako satimā sukhavihārī": f"{BV['upekkhā']} ရှိသူ၊ {SATI} ရှိသူ၊ သာယာစွာ နေသူ",
    "sukhassa ca pahānā dukkhassa ca pahānā": f"{JF['sukhassa ca pahānā']}{C} {JF['dukkhassa ca pahānā']}",
    "ananto ākāso": "ဟင်းလင်းပြင်သည် အဆုံး မရှိ", "anantaṃ viññāṇaṃ": f"{P1.VINNANA}သည် အဆုံး မရှိ",
    "natthi kiñci": "ဘာမျှ မရှိ",
    "rūpasaññāyo": "ရုပ်ဟု မှတ်သိမှုများ", "nānattasaññāyo": "အမျိုးမျိုး ကွဲပြားမှုဟု မှတ်သိမှုများ",
    "nevasaññīnāsaññī": f"{P1.SANNA} ရှိသူလည်း မဟုတ်{C} {P1.SANNA} မရှိသူလည်း မဟုတ်",
})
for _k in ("cetaso ekodibhāvaṃ", "pītiyā ca virāgā", "sato ca sampajāno", "sukhañca kāyena paṭisaṃvedeti",
           "pubbeva somanassadomanassānaṃ atthaṅgamā", "adukkhamasukhaṃ", "upekkhāsatipārisuddhiṃ",
           "sabbaso rūpasaññānaṃ samatikkamā", "paṭighasaññānaṃ atthaṅgamā", "nānattasaññānaṃ amanasikārā",
           "vitakkavicārānaṃ vūpasamā"):
    LEM[_k] = JF[_k]
for _k in AB:
    LEM[_k + "ṃ"] = AB[_k]
    if _k != "nevasaññānāsaññāyatana":
        LEM[f"sabbaso {_k}ṃ samatikkamma"] = JF[f"sabbaso {_k}ṃ samatikkamma"]
for _o in ("paṭhama", "dutiya", "tatiya", "catuttha"):
    LEM[_o + "ṃ"] = P1.ORD[_o]
# roles for the immaterial clauses of ^2-508 (finite statements)
_role({'"ananto ākāso"ti': f"“{LEM['ananto ākāso']}”ဟု", '"anantaṃ viññāṇa"nti': f"“{LEM['anantaṃ viññāṇaṃ']}”ဟု",
       '"natthi kiñcī"ti': f"“{LEM['natthi kiñci']}”ဟု"}, "F")
_role({f"{k}ṃ": v for k, v in AB.items()}, "J")
_role({"ākiñcāyatanaṃ": AB["ākiñcaññāyatana"]}, "J")
ROLE_MAX = max(len(k.split()) for k in ROLE)
SUBJ.update({
    "Ayaṃ abhijjhā imamhi loke": f"ဤလောက၌ ဤ{ABHIJJHA}သည်",
    "Iti ayañca byāpādo ayañca padoso": f"ဤသို့ ဤ{BYAPADA}လည်း{C} ဤ{PADOSA}လည်း",
    "Iti idañca thinaṃ idañca middhaṃ": f"ဤသို့ ဤ{THINA}လည်း{C} ဤ{MIDDHA}လည်း",
    "Iti idañca uddhaccaṃ idañca kukkuccaṃ": f"ဤသို့ ဤ{UDDH}လည်း{C} ဤ{KUKK}လည်း",
    "Ayaṃ vicikicchā": f"ဤ{VIC}သည်", "ime pañca nīvaraṇā": f"{NIVARANA5}တို့သည်",
    "Iti ayañca vitakko ayañca vicāro": f"ဤသို့ ဤ{P1.NAMES['vitakko']}လည်း{C} ဤ{P1.NAMES['vicāro']}လည်း",
    "Ayaṃ pīti": f"ဤ{P1.NAMES['pīti']}သည်",
    "Iti idañca sukhaṃ idañca dukkhaṃ": f"ဤသို့ ဤ{P1.NAMES['sukhaṃ']}လည်း{C} ဤ{P1.DUKKHA}မှုလည်း",
    "Iti idañca somanassaṃ idañca domanassaṃ": f"ဤသို့ ဤ{P1.SOMANASSA}လည်း{C} ဤစိတ်ဆင်းရဲမှုလည်း",
    "Imā paṭighasaññāyo": f"ဤ{P1.IMPACT}ဟု မှတ်သိမှုတို့သည်",
})
SODH_X.update({"imāya abhijjhāya": ABHIJJHA, "imamhā byāpādapadosā": f"{BYAPADA}နှင့် {PADOSA}",
               "imamhā thinamiddhā": f"{THINA}နှင့် {MIDDHA}", "imamhā uddhaccakukkuccā": f"{UDDH}နှင့် {KUKK}",
               "imāya vicikicchāya": VIC})
UPETO_X.update({
    "Iminā pātimokkhasaṃvarena": f"ဤ{PATI} စောင့်စည်းမှုဖြင့်",
    "Iti iminā ca ācārena iminā ca gocarena": "ဤသို့ ဤအကျင့်ဖြင့်လည်းကောင်း၊ ဤကျက်စားရာဖြင့်လည်းကောင်း",
    "Imāya indriyesu guttadvāratāya": "ဤအာရုံခံ အင်္ဂါတို့၏ တံခါးကို စောင့်ထိန်းခြင်းဖြင့်",
    "Imāya bhojane mattaññutāya": "ဤအစားအစာ၌ အတိုင်းအရှည်ကို သိခြင်းဖြင့်",
    "Iti imāya ca satiyā iminā ca sampajaññena": f"ဤသို့ ဤ{SATI}ဖြင့်လည်းကောင်း၊ ဤ{SAMPAJ}ဖြင့်လည်းကောင်း",
    "Iti iminā ca vitakkena iminā ca vicārena": f"ဤသို့ ဤ{P1.NAMES['vitakko']}ဖြင့်လည်းကောင်း၊ "
                                                f"ဤ{P1.NAMES['vicāro']}ဖြင့်လည်းကောင်း",
    "Imāya upekkhāya": f"ဤ{BV['upekkhā']}ဖြင့်",
})
_GIVE = ["veḷu", "patta", "puppha", "phala", "sināna", "dantakaṭṭha"]
_GIVE_MY = ["ဝါးကို", "သစ်ရွက်ကို", "ပန်းကို", "သစ်သီးကို", "ရေချိုးမှုန့်ကို", "ဒန်ပူကို"]
_WAY = {"cāṭukamyatāya": "ချော့မော့ ပြောဆိုခြင်းဖြင့်", "muggasūpyatāya": "ပဲဟင်းကဲ့သို့ အမှန်အမှား ရောနှော ပြောဆိုခြင်းဖြင့်",
        "pāribhaṭayatāya": "ကလေးထိန်းကဲ့သို့ ပြုစုခြင်းဖြင့်", "jaṅghapesanikena": "ခြေလျင် စေခိုင်းမှုကို ခံခြင်းဖြင့်",
        "aññataraññatarena": "အခြား တစ်ခုခုသော"}
_MICCHA = "မြတ်စွာဘုရား ကဲ့ရဲ့တော်မူအပ်သော မှားယွင်းသော အသက်မွေးမှုဖြင့်"
_KUL_BAD = ["ယုံကြည်မှု မရှိသော", "ကြည်ညိုမှု မရှိသော", "မှီခိုရာ မဖြစ်သော", "ဆဲရေး ပုတ်ခတ်တတ်သော",
            "အကျိုး မရှိခြင်းကို လိုလားသော", "စီးပွား မဖြစ်ခြင်းကို လိုလားသော", "ချမ်းသာ မရှိခြင်းကို လိုလားသော",
            "ဘေးကင်းရာ မရောက်ခြင်းကို လိုလားသော"]
_KUL_GOOD = ["ယုံကြည်မှု ရှိသော", "ကြည်ညိုမှု ရှိသော", "ရေတွင်းကဲ့သို့ မှီခိုရာ ဖြစ်သော", "ဖန်ရည်စွန်း သင်္ကန်းတို့ဖြင့် "
             "ထိန်လင်းသော", "ရသေ့တို့၏ လေ တိုက်ခတ်ရာ ဖြစ်သော", "အကျိုးကို လိုလားသော", "စီးပွားကို လိုလားသော",
             "ချမ်းသာကို လိုလားသော", "ဘေးကင်းရာကို လိုလားသော"]
_FOUR = "ရဟန်းတို့၊ ဘိက္ခုနီတို့၊ ဥပါသကာတို့၊ ဥပါသိကာတို့အား"
_SEV = "ထိုသို့သော အမျိုးတို့ကို မှီဝဲ၏၊ ဆည်းကပ်၏၊ ချဉ်းကပ် ခစား၏"
_PLACES6 = ["ပြည့်တန်ဆာ", "ခင်ပွန်း သေဆုံးသူ", "အပျိုကြီး", "ပဏ္ဍုက်", "ဘိက္ခုနီ", "သေရည်ဆိုင်"]
_ROYAL = "ဘုရင်တို့၊ ဘုရင်၏ အမတ်ကြီးတို့၊ အယူဝါဒ ခြားနားသူတို့၊ အယူဝါဒ ခြားနားသူတို့၏ တပည့်တို့နှင့် လျော်ညီမှု မရှိသော ပေါင်းသင်းခြင်းဖြင့်"
IDHEK = "ဤလောက၌ အချို့သော သူသည်"                     # Idhekacco (pi-1 ^1-1352 …)
BODY.update({
    "Idhekacco veḷudānena": (IDHEK + " " + "၊ ".join(f"{g} ပေးခြင်းဖြင့်ဖြစ်စေ" for g in _GIVE_MY) + "၊ " +
                             "၊ ".join(f"{_WAY[w]}ဖြစ်စေ" + (f" {F.var_my('[muggasuppatāya (sī.)]')}" if w == "muggasūpyatāya" else "")
                                      for w in list(_WAY)[:4]) +
                             f"၊ {_WAY['aññataraññatarena']} {_MICCHA}ဖြစ်စေ အသက်မွေး၏", False),
    "Idhekacco na veḷudānena": (IDHEK + " " + "၊ ".join(f"{g} ပေးခြင်းဖြင့် မဟုတ်" for g in _GIVE_MY) + "၊ " +
                                "၊ ".join(f"{_WAY[w]} မဟုတ်" for w in list(_WAY)[:4]) +
                                f"၊ {_WAY['aññataraññatarena']} {_MICCHA} မဟုတ် အသက်မွေး၏", False),
    "Idhekacco vesiyāgocaro": (IDHEK + " " + "၊ ".join(f"{x}{'သို့' if x.endswith('ဆိုင်') else 'တို့ထံ'} ကျက်စားသူဖြစ်စေ"
                                                        for x in _PLACES6) +
                               f" ဖြစ်၏၊ {_ROYAL} ရောနှော၍ နေ၏၊ သို့မဟုတ် {_FOUR} " + "၊ ".join(_KUL_BAD) +
                               f" ထိုအမျိုးတို့ ရှိ၏၊ {_SEV}", False),
    "Idhekacco na vesiyāgocaro": (IDHEK + " " + "၊ ".join(f"{x}{'သို့' if x.endswith('ဆိုင်') else 'တို့ထံ'} ကျက်စားသူ မဟုတ်"
                                                           for x in _PLACES6) +
                                  f"၊ {_ROYAL} မရောနှောဘဲ နေ၏၊ သို့မဟုတ် {_FOUR} " + "၊ ".join(_KUL_GOOD) +
                                  f" ထိုအမျိုးတို့ ရှိ၏၊ {_SEV}", False),
    "tāni vajjāni appamattakāni": ("အလွန် နည်းသော၊ အနည်းငယ်မျှ ဖြစ်သော၊ ပေါ့သော၊ ပေါ့သည်ဟု သတ်မှတ်ထားသော၊ "
                                   "ထိန်းချုပ်ခြင်းဖြင့် ပြုပြင်ရမည့်၊ စောင့်စည်းခြင်းဖြင့် ပြုပြင်ရမည့်၊ စိတ် ဖြစ်ပေါ်ခြင်းဖြင့် "
                                   "ပြုပြင်ရမည့်၊ နှလုံးသွင်းခြင်းနှင့် ဆက်စပ်သော ထိုအပြစ်တို့", True),
    "Pañcupādānakkhandhā loko": (f"{T['upādāniyā']} {P1.count_my(P1.KHANDHA, 'pañca')}သည် လောက ဖြစ်သည်", False),
    "Chando kāmo": ("၊ ".join(f"{x}သည် ကာမ ဖြစ်သည်" for x in ("ဆန္ဒ", "ရာဂ", "ဆန္ဒရာဂ", "ကြံစည်မှု", "ရာဂ",
                                                             "ကြံစည်မှု ရာဂ")), False),
    "Akappiye kappiyasaññitā, kappiye akappiyasaññitā, avajje vajjasaññitā, vajje avajjasaññitā, yaṃ":
        (list_my("Akappiye kappiyasaññitā, kappiye akappiyasaññitā, avajje vajjasaññitā, vajje avajjasaññitā") + C,
         True),
    "Rūpāvacarasamāpattiṃ samāpannassa vā upapannassa vā diṭṭhadhammasukhavihārissa vā":
        (f"{T['rūpāvacarā']} {JH}ကို ဝင်စားသူ၏ဖြစ်စေ၊ ထိုဘုံ၌ ဖြစ်ပေါ်ပြီးသူ၏ဖြစ်စေ၊ {DDSV.removesuffix('ရန် ဖြစ်သော')}သူ၏ဖြစ်စေ",
         False),
    "Asamāpannassa manodhātu samaṅgissa vā manoviññāṇadhātu samaṅgissa vā":
        (f"ဈာန် မဝင်စားသူ၊ {P1.MANO} ဓာတ်နှင့် ပြည့်စုံသူ၏ဖြစ်စေ၊ {P1.NAMES['manoviññāṇadhātu']}နှင့် ပြည့်စုံသူ၏ဖြစ်စေ",
         False),
})
SAMAPANNA = (f"ကို ဝင်စားသူ၏ဖြစ်စေ၊ ထိုဘုံ၌ ဖြစ်ပေါ်ပြီးသူ၏ဖြစ်စေ၊ {DDSV.removesuffix('ရန် ဖြစ်သော')}သူ၏ဖြစ်စေ "
             f"{CITTA}နှင့် {CITTA}၏ အဖော် {F.DHP} ဖြစ်သည်")
LABHA = "ရခြင်း၊ ပြန်လည် ရခြင်း၊ ရောက်ခြင်း၊ ကောင်းစွာ ရောက်ခြင်း၊ ထိတွေ့ခြင်း၊ မျက်မှောက် ပြုခြင်း၊ ဝင်စားခြင်း ရှိသမျှကို ဆိုလိုသည်"
ATIKK = "ကို ကျော်လွန်ပြီး ဖြစ်၏၊ လွန်မြောက်ပြီး ဖြစ်၏၊ ကောင်းစွာ ကျော်လွန်ပြီး ဖြစ်၏"
JATA = f"ထိုသဘောတရားတို့သည် ဤ{{x}}၌ " + "၊ ".join(F.DEF[k].removesuffix("ပြီးသော") + "ကြ၏" for k in
                                                   ("jāt", "sañjāt", "nibbatt", "abhinibbatt", "pātubhūt"))
CATTA = ("ကို စွန့်ပြီးသောကြောင့်၊ အန်ထုတ်ပြီးသောကြောင့်၊ လွှတ်ပြီးသောကြောင့်၊ ပယ်ပြီးသောကြောင့်၊ "
         "ပြန်လည် စွန့်လွှတ်ပြီးသောကြောင့်၊ ပယ်၍ ပြန်လည် စွန့်လွှတ်ပြီးသောကြောင့် ဖြစ်သည်")
new("Jhāna chapter: frames (new)", {"X samāpannassa vā upapannassa vā diṭṭhadhammasukhavihārissa vā cittacetasikā dhammā":
                                    "X" + SAMAPANNA, "yo X-assa lābho … upasampadā": "Xကို " + LABHA,
                                    "imaṃ X atikkanto hoti vītikkanto samatikkanto": "ဤX" + ATIKK,
                                    "te imasmiṃ X jātā honti … pātubhūtā": JATA, "tassa X cattattā … pahīnapaṭinissaṭṭhattā":
                                    "ထိုX" + CATTA})
ARUPA_GEN = {f"{k}ṃ": v for k, v in AB.items()}
LABHA_X = {f"{o}ssa jhānassa": f"{P1.ORD[o]} {JH}" for o in ("paṭhama", "dutiya", "tatiya", "catuttha")}
LABHA_X.update({f"{k}ssa": v for k, v in AB.items()})


def _try(f):
    try:
        return f()
    except Miss:
        return None


def finite_jh(text):
    return f"{C} ".join(build_jh(part, finite=True) for part in text.split("; "))


def sampaj_clauses(text):
    """«G sampajānakārī hoti, … / sato sampajāno V, …» (^2-508, 523, 525)."""
    out = []
    for cl in re.split(r", |; ", text):
        if cl.endswith("hotīti"):                 # the closing «ti» of the passage
            cl = cl[:-6] + "hoti"
        m = re.fullmatch(r"(?P<g>(?!sato )\S.*? )?(?P<s>sato )?sampajānakārī hoti", cl)
        if m:
            g = ""
            if m["g"]:
                gv = re.search(r" (\[[^\]]+\])", m["g"])
                g = G_ACT[re.sub(r" \[[^\]]+\]", "", m["g"]).strip()]
                if gv:                                 # the variant after the first verb of the pair
                    g = g.replace("ရာ", "ရာ " + var(gv[1]), 1)
                g += " "
            out.append(g + (SATI + " ရှိလျက် " if m["s"] else "") + SKARI)
            continue
        m = re.fullmatch(r"sato sampajāno (?P<v>\S+)", cl)
        if not m:
            raise Miss("sampajāna clause: " + cl)
        out.append(f"{SATO_SAMPAJANO} {V_ACT[m['v']]}")
    return f"{C} ".join(out)


def r_kathanca_sampaj(m):
    s = sampaj_clauses(m["c"])
    return f"{BHIKKHU}သည် အဘယ်သို့ " + s.removesuffix("ဖြစ်၏") + "ဖြစ်သနည်း"


def r_upasampada(m):
    return f"{LABHA_X[m['x']]}ကို {LABHA}"


FRAMES_SRC[:0] = [
    (r"So ime pañca nīvaraṇe pahāya cetaso upakkilese paññāya dubbalīkaraṇe (?P<r>.+)",
     lambda m: f"{SO} {CITTA}ကို ညစ်နွမ်းစေတတ်သော အညစ်အကြေးများ ဖြစ်ကုန်သော၊ {LEM['paññāya dubbalīkaraṇe']} "
               f"{NIVARANA5}တို့ကို ပယ်၍ {finite_jh(m['r'])}"),
    (r"Cattāri jhānāni – idha bhikkhu (?P<r>vivicceva .+)", lambda m: f"{COUNT['Cattāri jhānāni']} – {IDHA_BH} "
                                                                    f"{finite_jh(m['r'])}"),
    (r"(?P<p>So |Idha bhikkhu |Evaṃ bhikkhu )(?P<c>(?:abhikkante|sato sampajāno abhikkamati).+)",
     lambda m: {"So ": SO, "Idha bhikkhu ": IDHA_BH, "Evaṃ bhikkhu ": f"ဤသို့ {BHIKKHU}သည်"}[m["p"]] + " " +
               sampaj_clauses(m["c"])),
    (r"Kathañca bhikkhu (?P<c>abhikkante .+)", r_kathanca_sampaj),
    (r"yo (?P<x>\S+?(?:assa jhānassa|ssa)) lābho paṭilābho patti sampatti phusanā sacchikiriyā upasampadā", r_upasampada),
    (r"(?P<x>\S+) samāpannassa vā upapannassa vā diṭṭhadhammasukhavihārissa vā cittacetasikā dhammā",
     lambda m: ARUPA_GEN[m["x"]] + SAMAPANNA),
    (r"(?P<x>imaṃ \S+|Imā rūpasaññāyo) atikkanto hoti vītikkanto samatikkanto",
     lambda m: "ဤ" + (NOUNS["rūpasaññā"][0] + "တို့" if m["x"] == "Imā rūpasaññāyo" else ARUPA_GEN[m["x"][5:]]) + ATIKK),
    (r"(?P<l>[^\"]+?) – te imasmiṃ (?P<x>viveke|samādhimhi) jātā honti sañjātā nibbattā abhinibbattā pātubhūtā",
     lambda m: f"{f'{C} '.join(FACTOR[w] for w in re.split(r',? ', m['l']))} – " +
               JATA.format(x={"viveke": "ကင်းဆိတ်ခြင်း", "samādhimhi": "သမာဓိ"}[m["x"]])),
    (r"[Tt]assa (?P<x>thinamiddhassa|uddhaccakukkuccassa) cattattā vantattā muttattā pahīnattā paṭinissaṭṭhattā "
     r"pahīnapaṭinissaṭṭhattā",
     lambda m: "ထို" + {"thinamiddhassa": f"{THINA}နှင့် {MIDDHA}", "uddhaccakukkuccassa": f"{UDDH}နှင့် {KUKK}"}[m["x"]]
               + CATTA),
    (r"gaṇanānupubbatā(?P<v> \[[^\]]+\])? (?P<o>paṭhama|dutiya|tatiya|catuttha)ṃ(?P<c>, idaṃ \w+ samāpajjatīti \w+)?",
     lambda m: f"ရေတွက်ခြင်း၏ အစဉ်အားဖြင့်{(' ' + var(m['v'][1:])) if m['v'] else ''} {P1.ORD[m['o']]} ဖြစ်သည်" +
               (f"{C} ဤဈာန်ကို {P1.ORD[m['o']]} ဝင်စား၏ဟူ၍ {P1.ORD[m['o']]} ဖြစ်သည်" if m["c"] else "")),
    (r"Idaṃ (?P<o>paṭhama|dutiya|tatiya|catuttha)ṃ samāpajjatīti (?P=o)ṃ",
     lambda m: f"ဤဈာန်ကို {P1.ORD[m['o']]} ဝင်စား၏ဟူ၍ {P1.ORD[m['o']]} ဖြစ်သည်"),
    (r"(?P<l>(?:vitakko|vicāro|pīti|sukhaṃ|cittassekaggatā|upekkhā|sati|sampajaññaṃ|sampasādo|pītisukhaṃ)"
     r"(?:, (?:vitakko|vicāro|pīti|sukhaṃ|cittassekaggatā|upekkhā|sati|sampajaññaṃ|sampasādo|pītisukhaṃ))+)",
     lambda m: f"{C} ".join(FACTOR[w] for w in m["l"].split(", ")) + " ဖြစ်သည်"),
    (r"(?P<y>[Yy]o|[Yy]ā|[Yy]aṃ) (?P<l>(?!tasmiṃ )[^–]+)", lambda m: _try(lambda: f"{list_my(m['l'])} {REL}ကို ဆိုလိုသည်")),
    (r'"Vanapattha"nti (?P<x>na manussūpacārān|\w+?ān)ametaṃ(?P<v> \[[^\]]+\])? senāsanānaṃ adhivacanaṃ',
     lambda m: f"“{PLACE['vanapatthaṃ']}”ဟူသည် ဤသည်မှာ {VANA[m['x']]}{(' ' + var(m['v'][1:])) if m['v'] else ''} "
               f"{SENA}တို့၏ အမည် ဖြစ်သည်"),
    (r"(?P<x>\w+?)(?:pi|mpi) senāsanaṃ", None),
    (r"[Yy]adeva taṃ (?P<a>\w+) tadeva taṃ (?P<b>\w+)", lambda m: f"အကြင်နေရာသည် {QUIET[m['a']]}၏{C} ထိုနေရာသည်ပင် "
                                                            f"{QUIET[m['b']]}၏"),
    (r"(?P<x>\w+?)(?:yeva|ṃyeva) (?P=x)", None),
]
VANA = {"dūrān": "ဝေးကွာသော", "vanasaṇḍān": "တောအုပ်တို့ဖြင့် ဖုံးလွှမ်းသော", "bhīsanakān": "ကြောက်မက်ဖွယ်ကောင်းသော",
        "salomahaṃsān": "ကြက်သီး ထဖွယ်ကောင်းသော", "pariyantān": "အစွန်အဖျား၌ ရှိသော",
        "na manussūpacārān": "လူတို့ ကျက်စားရာ မဟုတ်သော", "durabhisambhavān": "ရောက်ရန် ခဲယဉ်းသော"}
new("Jhāna chapter: forest dwellings (new)", VANA)
FRAMES_SRC[:] = [x for x in FRAMES_SRC if x[1] is not None]
SENT.update(new("Jhāna chapter: sentences (new)", {
    "Idha bhikkhu pātimokkhasaṃvarasaṃvuto viharati":
        f"{IDHA_BH} {LEM['pātimokkhasaṃvarasaṃvuto']} ဖြစ်၍ {VIHARATI}၊ {LEM['ācāragocarasampanno']}၊ "
        f"{LEM['aṇumattesu vajjesu bhayadassāvī']} ဖြစ်၏၊ {LEM['samādāya sikkhati sikkhāpadesu']}၊ "
        f"{LEM['indriyesu guttadvāro']}၊ {LEM['bhojane mattaññū']}၊ "
        f"{LEM['pubbarattāpararattaṃ jāgariyānuyogamanuyutto']}၊ {LEM['sātaccaṃ']}၊ {LEM['nepakkaṃ']}ဖြင့် "
        f"{LEM['bodhipakkhikānaṃ dhammānaṃ bhāvanānuyogamanuyutto']} ဖြစ်၏",
    "So vivittaṃ senāsanaṃ bhajati":
        f"{SO} " + "၊ ".join(PLACE.values()) + " ဖြစ်သော၊ " +
        "၊ ".join(QUIET[k] + "သော" + (" " + F.var_my("[manussarāhaseyyakaṃ (sī. syā.)]") if k == "manussarāhasseyyakaṃ"
                                      else "") for k in QUIET) + f" ဆိတ်ငြိမ်သော {SENA}ကို မှီဝဲ၏",
    "So araññagato vā":
        f"{SO} {LEM['araññagato vā rukkhamūlagato vā suññāgāragato vā']} ထက်ဝယ်ဖွဲ့ခွေ၍ {LEM['ujuṃ kāyaṃ paṇidhāya']} "
        f"{LEM['parimukhaṃ satiṃ upaṭṭhapetvā']} ထိုင်၏",
    "So abhijjhaṃ loke pahāya": f"{SO} {LEM['abhijjhaṃ loke pahāya']} {LEM['vigatābhijjhena cetasā']} {VIHARATI}၊ "
                                f"{LEM['abhijjhāya cittaṃ parisodheti']}",
    "Byāpādapadosaṃ pahāya": f"{LEM['byāpādapadosaṃ pahāya']} {LEM['abyāpannacitto']} ဖြစ်လျက် ခပ်သိမ်းသော "
                             f"သတ္တဝါတို့၏ အကျိုးကို စာနာလျက် {VIHARATI}၊ {LEM['byāpādapadosā cittaṃ parisodheti']}",
    "Thinamiddhaṃ pahāya": f"{LEM['thinamiddhaṃ pahāya']} {LEM['vigatathinamiddho']} ဖြစ်လျက်၊ အလင်းဟု မှတ်သိလျက်၊ "
                           f"{SATI} ရှိလျက်၊ {SAMPAJ_L} {VIHARATI}၊ {LEM['thinamiddhā cittaṃ parisodheti']}",
    "Uddhaccakukkuccaṃ pahāya": f"{LEM['uddhaccakukkuccaṃ pahāya']} မယောက်ယက်ခတ်ဘဲ မိမိ၌ ကောင်းစွာ ငြိမ်သက်သော "
                                f"{CITTA} ရှိလျက် {VIHARATI}၊ {LEM['uddhaccakukkuccā cittaṃ parisodheti']}",
    "Vicikicchaṃ pahāya": f"{LEM['vicikicchaṃ pahāya']} {VIC}ကို ကူးမြောက်လျက်၊ {T['kusalā']} {F.DH}တို့၌ "
                          f"‘အဘယ်သို့နည်း’ဟု မတွေးတောဘဲ {VIHARATI}၊ {LEM['vicikicchāya cittaṃ parisodheti']}",
    "imissā diṭṭhiyā": "ဤအယူ၌၊ ဤလက်ခံမှု၌၊ ဤနှစ်သက်မှု၌၊ ဤယူဆောင်ထားမှု၌၊ ဤတရား၌၊ ဤဝိနည်း၌၊ ဤတရားနှင့် ဝိနည်း၌၊ "
                       "ဤဒေသနာတော်၌၊ ဤမြင့်မြတ်သော အကျင့်၌၊ ဤဆရာ၏ အဆုံးအမ၌ ဟု ဆိုလိုသည်",
    "samaññāya bhikkhu": "အမည်အားဖြင့် ရဟန်း၊ ဝန်ခံခြင်းအားဖြင့် ရဟန်း၊ တောင်းခံ၏ဟူ၍ ရဟန်း၊ တောင်းခံသူဟူ၍ ရဟန်း၊ "
                         "ဆွမ်းခံ ကျင့်ဝတ်သို့ ကပ်ရောက်ပြီးသူဟူ၍ ရဟန်း၊ ကွဲပြဲသော အဝတ်ကို ဆောင်သူဟူ၍ ရဟန်း၊ "
                         f"ယုတ်မာသော {T['akusalā']} {F.DH}တို့ကို ဖြိုခွဲ၏ဟူ၍ ရဟန်း၊ ယုတ်မာသော {T['akusalā']} "
                         f"{F.DH}တို့ ကွဲပြီးသောကြောင့် ရဟန်း၊ ကိလေသာတို့ကို အပိုင်းအခြားဖြင့် ပယ်ပြီးသောကြောင့် ရဟန်း၊ "
                         "ကိလေသာတို့ကို အပိုင်းအခြား မရှိ ပယ်ပြီးသောကြောင့် ရဟန်း၊ ကျင့်ကြံဆဲသူ ရဟန်း၊ "
                         "ကျင့်ကြံမှု ပြီးဆုံးသူ ရဟန်း၊ ကျင့်ကြံဆဲသူလည်း မဟုတ်၊ ကျင့်ကြံမှု ပြီးဆုံးသူလည်း မဟုတ်သော ရဟန်း၊ "
                         "အမြတ်ဆုံး ရဟန်း၊ ကောင်းမြတ်သော ရဟန်း၊ အဖိုးတန်သော ရဟန်း၊ အနှစ်သာရ ဖြစ်သော ရဟန်း၊ "
                         "ညီညွတ်သော သံဃာက ဉတ်လေးကြိမ်မြောက် ကံဖြင့်၊ မပျက်စီးသော၊ အကြောင်းနှင့် လျော်သော ကံဖြင့် "
                         "ပဉ္စင်းခံပြီးသော ရဟန်း ဆိုလိုသည်",
    "sīlaṃ patiṭṭhā ādi": f"{T['kusalā']} {F.DH}တို့ကို ရောက်ရှိရန် သီလ၊ တည်ရာ၊ အစ၊ အကျင့်၊ ထိန်းချုပ်မှု၊ စောင့်စည်းမှု၊ "
                          "မျက်နှာ၊ အထွတ်အထိပ် ဖြစ်သည်",
    "Saṃvaroti": "စောင့်စည်းမှုဟူရာ၌", "Saṃvutoti": "စောင့်စည်းသူဟူရာ၌",
    "Kāyiko avītikkamo, vācasiko avītikkamo, kāyikavācasiko avītikkamo":
        list_my("kāyiko avītikkamo, vācasiko avītikkamo, kāyikavācasiko avītikkamo") + " ဖြစ်သည်",
    "Sabbampi dussīlyaṃ anācāro": "သီလ ပျက်ခြင်း အားလုံးသည်လည်း မသင့်တော်သော အကျင့် ဖြစ်သည်",
    "Sabbopi sīlasaṃvaro ācāro": "သီလ စောင့်စည်းမှု အားလုံးသည်လည်း အကျင့် ဖြစ်သည်",
    "Iti imesu aṇumattesu vajjesu": "ဤသို့ ဤအနည်းငယ်မျှသော အပြစ်တို့၌ အပြစ်ဟု မြင်လေ့ရှိသူလည်း ဖြစ်၏၊ ဘေးဟု "
                                    "မြင်လေ့ရှိသူလည်း ဖြစ်၏၊ အပြစ်ဒဏ်ကို မြင်လေ့ရှိသူလည်း ဖြစ်၏၊ ထွက်မြောက်ရာကို "
                                    "မြင်လေ့ရှိသူလည်း ဖြစ်၏",
    "Catasso sikkhā": f"{P1.count_my(SIKKHA, 'catu')} – ရဟန်းတို့၏ ရဟန်း {SIKKHA}၊ ဘိက္ခုနီတို့၏ ဘိက္ခုနီ {SIKKHA}၊ "
                      f"ဥပါသကာတို့၏ ဥပါသကာ {SIKKHA}၊ ဥပါသိကာတို့၏ ဥပါသိကာ {SIKKHA}",
    "Iti imāsu sikkhāsu": f"ဤသို့ ဤ{SIKKHA}တို့ကို အားလုံးကို အားလုံးဖြင့်၊ အားလုံးကို အလုံးစုံဖြင့်၊ အကြွင်းအကျန် မရှိ၊ "
                          "အကုန်အစင် ဆောက်တည်၍ ကျင့်၏",
    "atthi indriyesu guttadvāratā": f"{NOUNS['indriyesu guttadvāratā'][0]} ရှိသည်၊ "
                                    f"{NOUNS['indriyesu aguttadvāratā'][0]} ရှိသည်",
    "atthi bhojane mattaññutā": f"{NOUNS['bhojane mattaññutā'][0]} ရှိသည်၊ {NOUNS['bhojane amattaññutā'][0]} ရှိသည်",
    "Kathañca bhikkhu pubbarattāpararattaṃ": f"{BHIKKHU}သည် ညဉ့်ဦးယံ ညဉ့်နောက်ယံ၌ နိုးကြားမှုကို အဘယ်သို့ "
                                             "အားထုတ်သူ ဖြစ်သနည်း",
    "Idha bhikkhu divasaṃ caṅkamena":
        f"{IDHA_BH} နေ့အခါ စင်္ကြံ လျှောက်ခြင်း၊ ထိုင်ခြင်းဖြင့် ပိတ်ပင်တတ်သော {F.DH}တို့မှ {CITTA}ကို {SODH_MY}၊ "
        f"ညဉ့်ဦးယံ၌ စင်္ကြံ လျှောက်ခြင်း၊ ထိုင်ခြင်းဖြင့် ပိတ်ပင်တတ်သော {F.DH}တို့မှ {CITTA}ကို {SODH_MY}၊ "
        f"သန်းခေါင်ယံ၌ ခြေတစ်ဖက်ပေါ်၌ ခြေတစ်ဖက်ကို {F.var_my('[pādena pādaṃ (syā.)]')} ထပ်၍ {SATO_SAMPAJANO} "
        f"ထမည်ဟု မှတ်သိမှုကို နှလုံးသွင်း၍ ညာဘက် နံပါးဖြင့် ခြင်္သေ့ အိပ်ခြင်းကို ပြု၏၊ မိုးသောက်ယံ၌ ထ၍ စင်္ကြံ "
        f"လျှောက်ခြင်း၊ ထိုင်ခြင်းဖြင့် ပိတ်ပင်တတ်သော {F.DH}တို့မှ {CITTA}ကို {SODH_MY}",
    "Evaṃ bhikkhu pubbarattāpararattaṃ": f"ဤသို့ {BHIKKHU}သည် {LEM['pubbarattāpararattaṃ jāgariyānuyogamanuyutto']} ဖြစ်၏",
    "Satta bojjhaṅgā": f"{P1.count_my('ဗောဇ္ဈင်', 'satta')} – " + "၊ ".join(BOJJH.values()),
    "Iti te bodhipakkhike dhamme": "ဤသို့ ထိုဗောဓိပက္ခိယ သဘောတရားတို့ကို မှီဝဲ၏၊ ပွားများ၏၊ အဖန်ဖန် ပြု၏",
    "santike cepi senāsanaṃ hoti": f"အနီး၌ ရှိသော {SENA} ဖြစ်စေကာမူ ထိုနေရာသည် လူဝတ်ကြောင်တို့၊ ရဟန်းအဖြစ် "
                                   "ထွက်သူတို့ဖြင့် မပြည့်ကျပ်",
    "Dūre cepi senāsanaṃ hoti": f"အဝေး၌ ရှိသော {SENA} ဖြစ်စေကာမူ ထိုနေရာသည် လူဝတ်ကြောင်တို့၊ ရဟန်းအဖြစ် "
                                "ထွက်သူတို့ဖြင့် မပြည့်ကျပ်",
    "Tena taṃ vivittaṃ": "ထို့ကြောင့် ထိုနေရာသည် ဆိတ်ငြိမ်၏", "Tena taṃ appasaddaṃ": "ထို့ကြောင့် ထိုနေရာသည် အသံ နည်း၏",
    "mañcopi senāsanaṃ": "၊ ".join(f"{v}သည်လည်း {SENA} ဖြစ်သည်" + (" " + F.var_my("[bimbohanampi (sī. syā.)]")
                                                                  if k == "bibbohanaṃ" else "")
                                  for k, v in SENA_ITEMS.items()),
    "Yattha vā pana bhikkhū": f"သို့မဟုတ် ရဟန်းတို့ ဆုတ်နားရာ မည်သည့်နေရာမဆို ထိုအားလုံးသည် {SENA} ဖြစ်သည်",
    "imaṃ vivittaṃ senāsanaṃ bhajati": f"ဤဆိတ်ငြိမ်သော {SENA}ကို မှီဝဲ၏၊ ကောင်းစွာ မှီဝဲ၏၊ ဆည်းကပ်၏၊ အမြဲ ဆည်းကပ်၏၊ "
                                       "ကောင်းစွာ ဆည်းကပ်၏",
    "nikkhamitvā bahi indakhīlā": "မြို့တံခါး တိုင်ကြီးမှ အပြင်သို့ ထွက်ပြီးသော နေရာ အားလုံးသည် တော ဖြစ်သည်",
    "rukkhamūlaṃyeva rukkhamūlaṃ": "သစ်ပင်ရင်းသည်ပင် သစ်ပင်ရင်း ဖြစ်သည်",
    "Pabbatoyeva pabbato": "တောင်သည်ပင် တောင် ဖြစ်သည်", "Kandarāyeva kandarā": "ချောက်သည်ပင် ချောက် ဖြစ်သည်",
    "Giriguhāyeva giriguhā": "တောင်ဂူသည်ပင် တောင်ဂူ ဖြစ်သည်", "Susānaṃyeva susānaṃ": "သုသာန်သည်ပင် သုသာန် ဖြစ်သည်",
    "Abbhokāsoyeva abbhokāso": "လွင်တီးခေါင်သည်ပင် လွင်တီးခေါင် ဖြစ်သည်",
    "Palālapuñjoyeva palālapuñjo": "ကောက်ရိုးပုံသည်ပင် ကောက်ရိုးပုံ ဖြစ်သည်",
    "araññagato vā hoti": "တောသို့ ရောက်သူဖြစ်စေ၊ သစ်ပင်ရင်းသို့ ရောက်သူဖြစ်စေ၊ ဆိတ်ငြိမ်ရာ အိမ်သို့ ရောက်သူဖြစ်စေ ဖြစ်၏",
    "nisinno hoti pallaṅkaṃ ābhujitvā": "ထက်ဝယ်ဖွဲ့ခွေ၍ ထိုင်နေသူ ဖြစ်၏",
    "ujuko hoti kāyo": "ကိုယ်သည် ဖြောင့်မတ်၏၊ တည်ငြိမ်၏၊ ကောင်းစွာ ထားအပ်၏",
    "Ayaṃ sati upaṭṭhitā hoti": f"ဤ{SATI}သည် နှာသီးဖျား၌ဖြစ်စေ၊ နှုတ်ခမ်းအထက် အမှတ်၌ဖြစ်စေ ထင်၏၊ ကောင်းစွာ ထင်၏",
    "Idaṃ cittaṃ vigatābhijjhaṃ hoti": f"ဤ{CITTA}သည် {ABHIJJHA} ကင်း၏",
    "Yo byāpādo so padoso": f"အကြင် {BYAPADA}သည် ထို{PADOSA} ဖြစ်သည်၊ အကြင် {PADOSA}သည် ထို{BYAPADA} ဖြစ်သည်",
    "Idaṃ cittaṃ abyāpannaṃ hoti": f"ဤ{CITTA}သည် {BYAPADA} မရှိ",
    "Ayaṃ saññā ālokā hoti": f"ဤ{P1.SANNA}သည် အလင်း ဖြစ်၏၊ ပွင့်လင်း၏၊ စင်ကြယ်၏၊ ဖြူစင်၏",
    "Idaṃ cittaṃ ajjhattaṃ santaṃ hoti": f"ဤ{CITTA}သည် မိမိ၌ ငြိမ်သက်၏၊ ငြိမ်း၏၊ ကောင်းစွာ ငြိမ်သက်၏",
    "imaṃ vicikicchaṃ tiṇṇo hoti": f"ဤ{VIC}ကို ကူးမြောက်သူ ဖြစ်၏၊ အထက်သို့ ကူးမြောက်၏၊ လုံးဝ ကူးမြောက်၏၊ "
                                   "တစ်ဖက်ကမ်းသို့ ရောက်၏၊ တစ်ဖက်ကမ်းသို့ ရောက်ရှိပြီး ဖြစ်၏",
    "imāya vicikicchāya kusalesu dhammesu": f"ဤ{VIC}ကြောင့် {T['kusalā']} {F.DH}တို့၌ သံသယ မဖြစ်၊ မယုံမှား၊ "
                                            "‘အဘယ်သို့နည်း’ဟု မတွေးတောသူ ဖြစ်၏၊ တွေးတောမှု ကင်းသူ၊ တွေးတောမှု ပြတ်သူ ဖြစ်၏",
    "ime pañca nīvaraṇā cittassa upakkilesā": f"{NIVARANA5}တို့သည် {CITTA}ကို ညစ်နွမ်းစေတတ်သော အညစ်အကြေးများ ဖြစ်ကြသည်",
    "imehi pañcahi nīvaraṇehi": f"{NIVARANA5}တို့ကြောင့် မဖြစ်ပေါ်ရသေးသော ပညာလည်း မဖြစ်ပေါ်၊ ဖြစ်ပေါ်ပြီးသော ပညာလည်း "
                                "ချုပ်ပျောက်၏",
    "Iti imehi ca kāmehi": f"ဤသို့ ဤကာမတို့မှလည်းကောင်း၊ ဤ{T['akusalā']} {F.DH}တို့မှလည်းကောင်း ကင်းဆိတ်၏",
    "yaṃ ajjhattaṃ paccattaṃ": f"{F.DEF['ajjhatt']}၊ {F.DEF['paccatt']} အရာ ရှိသမျှကို ဆိုလိုသည်",
    "Idaṃ sukhaṃ iminā kāyena": f"ဤ{P1.NAMES['sukhaṃ']}ကို ဤ{P1.KAYA}ဖြင့် ခံစား၏",
    "Ariyā vuccanti buddhā ca": "အရိယာဟူသည် ဘုရားရှင်တို့နှင့် ဘုရားရှင်၏ တပည့်သာဝကတို့ကို ဆိုသည်",
    "Te imaṃ ācikkhanti": f"ထိုအရိယာတို့သည် ဤဈာန်ကို ပြောကြားကြ၏၊ ဟောကြ၏၊ သိစေကြ၏ {F.var_my('[paññāpenti (sī. syā.)]')}၊ "
                          "ထူထောင်ကြ၏၊ ဖွင့်လှစ်ကြ၏၊ ခွဲခြားပြကြ၏၊ ပေါ်လွင်အောင် ပြုကြ၏၊ ထင်ရှားစေကြ၏",
    "Iti imāya ca upekkhāya imāya ca satiyā": f"ဤသို့ ဤ{BV['upekkhā']}၊ ဤ{SATI}၊ ဤ{P1.NAMES['sukhaṃ']}တို့နှင့် "
                                              "အညီအညွတ် ပြည့်စုံလျက် " + seq_my(" ".join(IRIYATI), IRIYATI_MY),
    "Ayaṃ sati imāya upekkhāya": f"ဤ{SATI}သည် ဤ{BV['upekkhā']}ကြောင့် ပွင့်လင်း၏၊ စင်ကြယ်၏၊ ဖြူစင်၏",
    "Imā nānattasaññāyo na manasi karoti": f"ဤ{NOUNS['nānattasaññā'][0]}တို့ကို နှလုံး မသွင်း",
    "Tasmiṃ ākāse cittaṃ ṭhapeti": f"ထိုဟင်းလင်းပြင်၌ {CITTA}ကို ထား၏၊ ကောင်းစွာ ထား၏၊ အဆုံး မရှိ {PHARITVA.removesuffix('၍')}၏",
    "taṃyeva ākāsaṃ viññāṇena": f"ထိုဟင်းလင်းပြင်ကိုပင် {P1.VINNANA}ဖြင့် ပျံ့နှံ့၍ နှလုံးသွင်း၏၊ အဆုံး မရှိ "
                                f"{PHARITVA.removesuffix('၍')}၏",
    "taṃyeva viññāṇaṃ bhāveti": f"ထို{P1.VINNANA}ကိုပင် ပွားများ၏၊ ပျောက်ကွယ်စေ၏၊ ကွယ်ပျောက်စေ၏၊ “ဘာမျှ မရှိ”ဟု ရှု၏",
    "taṃyeva ākiñcaññāyatanaṃ santato": f"ထို{AB['ākiñcaññāyatana']}ကိုပင် ငြိမ်သက်သည်ဟု နှလုံးသွင်း၏၊ "
                                        f"{P1.SANKHARA} အကြွင်းအကျန်သာ ရှိသော ဈာန်ကို ပွားများ၏",
    "Idhekacco cakkhunā rūpaṃ disvā na nimittaggāhī hoti nānubyañjanaggāhī":
        SENT1["Idhekacco cakkhunā rūpaṃ disvā na nimittaggāhī hoti na anubyañjanaggāhī."].removesuffix(END),
}))
_k = [x for x in SENT1 if x.startswith("Yatvādhikaraṇamenaṃ manindriyaṃ") and "saṃvarāya paṭipajjati" in x
      and "na paṭipajjati" not in x]
SENT["Ñatvādhikaraṇamenaṃ manindriyaṃ"] = SENT1[_k[0]].removesuffix(END)
SLIPS += ["^2-517 «Ñatvādhikaraṇamenaṃ» read as Yatvādhikaraṇamenaṃ (pi-1's sentence)",
          "^2-508 «ākiñcāyatanaṃ» read as ākiñcaññāyatanaṃ", "^2-576 «santā hoti» (two subjects): singular kept"]
# the ^2-518 food reflection: pi-1's Burmese (^1-1355) with the Vb quotation marks
_food = [y for x, y in PAIRS1 if x.startswith("Idhekacco paṭisaṅkhā yoniso āhāraṃ āhāreti – neva davāya")][0]
SENT["Idhekacco paṭisaṅkhā yoniso āhāraṃ āhāreti – \"neva davāya"] = _food.replace(" – ", " – “", 1).replace(
    "ဖြစ်လိမ့်မည်ဟူ၍။", "ဖြစ်လိမ့်မည်”ဟူ၍")


# ===================================================================================== pañhāpucchaka (sample engine)
for _k, _v in {"tīṇi jhānāni": (P1.count_my(JH, "ti"), None, True), "dve jhānāni": (P1.count_my(JH, "dvi"), None, True),
               "catutthaṃ jhānaṃ": (ORDJ["catutthaṃ jhānaṃ"], None, False),
               "paṭhamaṃ jhānaṃ": (ORDJ["paṭhamaṃ jhānaṃ"], None, False),
               "tisso appamaññāyo": (P1.count_my(APP, "ti"), None, True), "upekkhā": (BV["upekkhā"], None, False),
               "mettā": (BV["mettā"], None, False)}.items():
    F.KH.setdefault(_k, _v)
new("Pañhāpucchaka subjects (new)", {k: F.KH[k][0] for k in ("tīṇi jhānāni", "dve jhānāni", "tisso appamaññāyo")})
KATI_HEAD = {"Catunnaṃ jhānānaṃ": f"{COUNT['Cattāri jhānāni']}တို့အနက်",
             "Catunnaṃ appamaññānaṃ": f"{COUNT['Catasso appamaññāyo']}တို့အနက်",
             "Pañcannaṃ sikkhāpadānaṃ": f"{COUNT['Pañca sikkhāpadāni']}တို့အနက်"}
new("Pañhāpucchaka (new)", KATI_HEAD)
ETTHA = f"ယင်း၌ {T['uppannā']}"                # etthuppanna (arisen therein)
ETTHA_OBJ = {"sukhaṃ vedanaṃ": f"{P1.SUKHA}သော {P1.FEEL}", "adukkhamasukhaṃ vedanaṃ": f"မ{P1.DUKKHA} မ{P1.SUKHA}သော {P1.FEEL}",
             "vitakkavicāre": f"{P1.NAMES['vitakko']}နှင့် {P1.NAMES['vicāro']}တို့", "pītiṃ": P1.NAMES["pīti"],
             "sukhaṃ": P1.NAMES["sukhaṃ"], "upekkhaṃ": BV["upekkhā"], "vitakkaṃ": P1.NAMES["vitakko"],
             "vicāraṃ": P1.NAMES["vicāro"]}
new("Pañhāpucchaka (new)", {"etthuppannaṃ X ṭhapetvā": f"{ETTHA} Xကို ချန်ထား၍"})
F.TERM_IRREG.update({"savitakkaṃ savicāraṃ": "savitakkasavicārā", "na hetu sahetūkā": "na hetū sahetukā",
                     "āsavavippayuttā sāsavā": "āsavavippayuttasāsavā", "āsavavippayuttā anāsavā": "āsavavippayuttaanāsavā",
                     "paccuppannāramaṇaṃ": "paccuppannārammaṇā", "na bhāvanāyapahātabbā": "na bhāvanāya pahātabbā"})
_NA_TERMS = {"na maggārammaṇā": T["maggārammaṇā"].removesuffix("သော") + "သည် မဟုတ်သော"}   # free na (pi-1 pattern)
for _k, _v in _NA_TERMS.items():
    T.setdefault(_k, _v)
new("Pañhāpucchaka terms (new, pi-1 pattern)", _NA_TERMS)
NV_ITEM = r'"?[^",;.?"]+?(?:"ntipi|"nti|"tipi|"ti|ti"pi|ntipi|tipi|nti|ti)(?=, |\.|;|$| )'


def r_nv(m):
    out = []
    for it in re.findall(r'("?)([^",;.?"]+?)("ntipi|"nti|"tipi|"ti|ti"pi|ntipi|tipi|nti|ti)(?=, |\.|;|$| )', m["q"]):
        oq, t, tail = it
        t = t.strip()
        if tail.lstrip('"').startswith("n"):
            t += "ṃ"
        quoted = bool(oq) or '"' in tail
        word = F.TIPI if tail.endswith("pi") else F.TI
        dh = F.DHP if F.STATE.get("pl", False) else F.DH
        body = f"{F.term_my(t)} {dh}"
        out.append((f"“{body}”" if quoted else body) + word)
    if not out:
        raise Miss("na vattabbā: " + m[0])
    return (F.SIYA + " " if m["s"] else "") + f"{C} ".join(out) + " " + F.NVATT


def r_kati_head2(m):
    F.STATE["pl"] = True
    return KATI_HEAD[m[0][0].upper() + m[0][1:]]


F.EXTRA_RULES[:] = [
    (r"(?:[Cc]atunnaṃ jhānānaṃ|[Cc]atunnaṃ appamaññānaṃ|[Pp]añcannaṃ sikkhāpadānaṃ)(?= kati)", r_kati_head2),
    (r"etthuppann(?:aṃ|e) (?P<o>.+?) ṭhapetvā", lambda m: f"{ETTHA} {ETTHA_OBJ[m['o']]}ကို ချန်ထား၍"),
    (r"(?P<s>[Ss]iyā )?[Nn]a vattabb(?:ā|aṃ|o) (?P<q>" + NV_ITEM + r"(?:(?:, | )" + NV_ITEM + r")*)", r_nv),
    (r"[Kk]usalāyeva", lambda m: f"{T['kusalā']} {F.DHP}သာ {F.COP[True]}"),
]
F.rebuild()
new("Pañhāpucchaka (new)", {"Kusalāyeva": f"{T['kusalā']} {F.DHP}သာ {F.COP[True]}",
                            "S na vattabbā A-tipi, B-tipi (no dash, no quotes)": f"Sသည် A {F.DH}{F.TIPI}{C} "
                            f"B {F.DH}{F.TIPI} {F.NVATT}"})


def pan_line(body):
    """A term line of the pañhāpucchaka: the sample engine, sentence by sentence (the subject of a sentence without
    one is the chapter's set of items: plural)."""
    body = body.replace("upādinn", "upādiṇṇ").replace(" …pe…", "…pe…")      # stray space before «…pe…»
    out = []
    for sent in re.split(r"(?<=\.) (?=[A-ZĀĪŪ\"])", body):
        F.STATE.pop("nv", None)
        F.STATE["pl"] = True
        F.STATE["part"] = "pan"
        out.append(F.clauses_my(sent[:1].lower() + sent[1:]))
    return " ".join(out)


# ===================================================================================== lines and chapters
SENT_SPLIT = re.compile(r"(?<=[.?])(?:\"|”)? (?=\S)")


def split_sents(body):
    body = re.sub(r"\[[^\]]*\]", lambda m: m[0].replace(". ", ".\x00"), body)
    return [x.replace("\x00", " ") for x in SENT_SPLIT.split(body) if x]


PART = {}


def line_my(body):
    m = F.HEAD_RE.fullmatch(body)
    if m:
        t = m["t"]
        if t in F.PART:
            PART["p"] = F.PART[t]
            F.STATE["part"] = F.PART[t]
        if t not in HEAD_ALL:
            raise Miss("heading: " + t)
        return f"{m['h']} {HEAD_ALL[t]}"
    if PART.get("p") == "pan" and not re.match(r"(?:Cattāri jhānāni|Catasso appamaññāyo|Pañca sikkhāpadāni) – ",
                                               body) and not re.fullmatch(r"\S+\.|\S+ niṭṭhito\.", body):
        return pan_line(body)
    return " ".join(sent_my(x) for x in split_sents(body))


def translate_line(line):
    if not line.strip():
        return ""
    m = ID.search(line)
    body = line[:m.start()] if m else line
    return line_my(body) + (" " + m.group(1) if m else "")


def write(name, txt):
    txt = unicodedata.normalize("NFC", txt)
    (OUT / name).write_text(txt, encoding="utf-8")
    print(f"wrote {name}: {sum(1 for l in txt.splitlines() if l)} lines")


def chapter(name):
    PART.clear()
    F.STATE.clear()
    done = []
    for i, line in enumerate((PALI / name).read_text(encoding="utf-8-sig").splitlines()):
        try:
            done.append(translate_line(line))
        except Miss as e:
            print(f"STOP {name} line {i + 1}: {e}\n  {line[:200]}")
            return False
    write(name, "\n".join(done).rstrip("\n") + "\n")
    return True


def write_notes_terms():
    """Rewrite the generated term section of notes-ch12-14.md (from the marker on)."""
    notes = HERE / "notes-ch12-14.md"
    mark = "## New strings (generated by make_ch12-14.py; «Pāli = Burmese»)"
    head = notes.read_text(encoding="utf-8").split(mark)[0] if notes.exists() else ""
    L = [mark, ""]
    for sec, d in NEW.items():
        L += [f"### {sec}", ""] + [f"{k} = {v}" for k, v in d.items()] + [""]
    L += ["### Lemmas (quoted words)", ""] + [f"{k} = {v}" for k, v in LEM.items()] + [""]
    L += ["### Source slips seen in this run", ""] + [f"- {x}" for x in dict.fromkeys(SLIPS)] + [""]
    notes.write_text(unicodedata.normalize("NFC", head + "\n".join(L)), encoding="utf-8")


def selftest():
    """Rebuild every pi-1 jhāna opening the builder can read; compare with pi-1's Burmese."""
    n = ok = 0
    bad = []
    for k, v in OPEN1.items():
        if k.startswith("kāmāvacar") or "ārammaṇaṃ" in k:
            continue
        try:
            b = build_jh(k)
        except Miss:
            continue
        n += 1
        if b == v:
            ok += 1
        else:
            bad.append((k, v, b))
    print(f"selftest: {ok} / {n} pi-1 jhāna openings rebuilt identically")
    for k, v, b in bad[:6]:
        print("  P:", k[:150], "\n  1:", v[:300], "\n  2:", b[:300])
    return not bad


if __name__ == "__main__":
    rebuild_frames()
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    keys = [a for a in sys.argv[1:] if not a.startswith("--")] or list(NAMES_OUT)
    ok = all([chapter(NAMES_OUT[k]) for k in keys])
    if "--notes" in sys.argv:
        write_notes_terms()
    sys.exit(0 if ok else 1)
