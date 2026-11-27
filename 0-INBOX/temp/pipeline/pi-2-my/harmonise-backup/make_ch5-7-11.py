"""Burmese zero-shot of pi-2 (Vibhaṅga, «ခွဲခြမ်းစိတ်ဖြာခြင်း»): chapters 5, 7, 8, 9, 10, 11.

usage: python3 -I -X utf8 make_ch5-7-11.py [chapter ...]
Model: make_sample.py (approved sample). Every line is generated from the Pāli by frames and tables; a text no frame
or table entry matches stops the run (F.Miss), nothing is guessed. A chapter is written only when every line passed.
  * my2_formulas.py (F) is imported read-only; its tables are extended IN MEMORY only (KH subjects, NOUN, HEAD, COLO,
    TERM_IRREG, EXTRA_RULES); nothing in pi-1-my or my2_formulas.py is written.
  * pi-1 FINAL Burmese (rails text) is binding for identical Pāli: the synonym lists, the lokuttara jhāna and vipāka
    openings, the four jhāna formulas, the sammappadhāna formula, the root / aggregate / kamma sentences are READ from
    the pi-1 rails text (aligned sentence by sentence) and asserted, not retyped.
  * the Pañhāpucchaka goes through F's engine (subjects, siyā, na vattabbo, kati, ceva) with the new subjects.
  * the suttanta / abhidhamma prose goes through this file's own clause engine (RULES, PH, lists).
Every string new in pi-2 is logged (NEWLOG) and written to notes-ch5-7-11.md (section «New strings»).
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
DH, DHP = F.DH, F.DHP
ROOT = HERE.parents[3]
PALI = ROOT / "AI_translation/pali/pi-2_split_chapters"
OUT = ROOT / "AI_translation/burmese/pi-2-burmese-plain-zeroshot_split_chapters"
NOTES = HERE / "notes-ch5-7-11.md"
CHAPTERS = ["5-indriyavibhango.md", "7-satipatthanavibhango.md", "8-sammappadhanavibhango.md",
            "9-iddhipadavibhango.md", "10-bojjhangavibhango.md", "11-maggangavibhango.md"]
Miss = F.Miss
NEWLOG = {}           # Pāli -> Burmese, every string new in pi-2 (for the notes)


def new(p, m):
    if p in NEWLOG and NEWLOG[p] != m:
        raise SystemExit(f"new string conflict {p}: {NEWLOG[p]} / {m}")
    NEWLOG[p] = m
    return m


# ===================================================================================== pi-1 final text, aligned
ID_RE = F.ID_RE


def _ps(l):
    l = ID_RE.sub("", l)
    l = re.sub(r"\[[^\]]*\]", lambda m: m[0].replace(". ", ".\x00"), l)
    return [s.replace("\x00", " ") for s in re.split(r"(?<=[.?])(?:\"|”)? (?=\S)", l) if s]


def _bs(l):
    return [s for s in re.split(r"(?<=။) ", ID_RE.sub("", l)) if s]


P1S = []              # (file, pāli sentence, burmese sentence)
for _p in sorted(F.P1_PALI.glob("*.md")):
    _pl = _p.read_text(encoding="utf-8-sig").split("\n")
    _bl = (F.P1_RAILS / _p.name).read_text(encoding="utf-8").split("\n")
    for _x, _y in zip(_pl, _bl):
        if not _x.strip() or _x.startswith("#"):
            continue
        _a, _b = _ps(_x), _bs(_y)
        if len(_a) == len(_b):
            P1S.extend((_p.name, s, t) for s, t in zip(_a, _b))


def p1(rx):
    """First pi-1 (Pāli, final Burmese) sentence pair whose Pāli matches rx."""
    r = re.compile(rx)
    for f, s, t in P1S:
        if r.search(s):
            return s, t
    raise SystemExit("pi-1 sentence not found: " + rx)


def in_p1(rx, *mys):
    """Assert that every Burmese string occurs in the pi-1 sentence (the string is pi-1's final wording)."""
    _, t = p1(rx)
    for m in mys:
        if m not in t:
            raise SystemExit(f"not in pi-1 ({rx}): {m}")
    return mys[0] if len(mys) == 1 else mys


# ===================================================================================== synonym lists (pi-1 final)
SYN2 = {}             # Pāli list item -> Burmese
SYN_SRC = {}


def learn(p, m, src):
    if p in SYN2 and SYN2[p] != m:
        raise SystemExit(f"list item conflict {p}: {SYN2[p]} / {m} ({src})")
    SYN2[p] = m
    SYN_SRC.setdefault(p, src)


def p1list(rx, items, head_rx=None, partial=False):
    """Read a pi-1 synonym list: Pāli items (|-separated) zipped with the Burmese items of the aligned sentence."""
    pali, my = p1(rx)
    b = my.removeprefix(P1.TASMIM + " ")
    head = ""
    if head_rx:
        m = re.match(head_rx, b)
        if not m:
            raise SystemExit("pi-1 list head: " + rx)
        head, b = m[0], b[m.end():]
    b = b.split(" ရှိသမျှ")[0].split(" – ")[0]
    b = re.sub(r" \[[^\]]*\]", "", b)
    parts = b.split(C + " ")
    its = items.split("|")
    if len(parts) < len(its) or (not partial and len(parts) != len(its)):
        raise SystemExit(f"pi-1 list {rx}: {len(its)} Pāli / {len(parts)} Burmese")
    for p, m in zip(its, parts):
        learn(p, m, rx)
    return head


TAJJA_MANO = p1list(r"^Yaṃ tasmiṃ samaye tajjāmanoviññāṇadhātusamphassajaṃ cetasikaṃ sātaṃ",
                    "cetasikaṃ sātaṃ|cetasikaṃ sukhaṃ|cetosamphassajaṃ sātaṃ sukhaṃ vedayitaṃ|"
                    "cetosamphassajā sātā sukhā vedanā", r"^.*?ဖြစ်ပေါ်သော (?=စိတ်ပိုင်းဆိုင်ရာ)")
p1list(r"^Yaṃ tasmiṃ samaye tajjāmanoviññāṇadhātusamphassajaṃ cetasikaṃ asātaṃ",
       "cetasikaṃ asātaṃ|cetasikaṃ dukkhaṃ|cetosamphassajaṃ asātaṃ dukkhaṃ vedayitaṃ|"
       "cetosamphassajā asātā dukkhā vedanā", r"^.*?ဖြစ်ပေါ်သော (?=စိတ်ပိုင်းဆိုင်ရာ)")
p1list(r"^Yaṃ tasmiṃ samaye tajjāmanoviññāṇadhātusamphassajaṃ cetasikaṃ neva sātaṃ",
       "cetasikaṃ neva sātaṃ nāsātaṃ|cetosamphassajaṃ adukkhamasukhaṃ vedayitaṃ|cetosamphassajā adukkhamasukhā vedanā",
       r"^.*?ဖြစ်ပေါ်သော (?=စိတ်ပိုင်းဆိုင်ရာ)")
p1list(r"^Yaṃ tasmiṃ samaye tajjākāyaviññāṇadhātusamphassajaṃ kāyikaṃ sātaṃ",
       "kāyikaṃ sātaṃ|kāyikaṃ sukhaṃ|kāyasamphassajaṃ sātaṃ sukhaṃ vedayitaṃ|kāyasamphassajā sātā sukhā vedanā",
       r"^.*?ဖြစ်ပေါ်သော (?=ကိုယ်ပိုင်းဆိုင်ရာ)")
p1list(r"^Yaṃ tasmiṃ samaye tajjākāyaviññāṇadhātusamphassajaṃ kāyikaṃ asātaṃ",
       "kāyikaṃ asātaṃ|kāyikaṃ dukkhaṃ|kāyasamphassajaṃ asātaṃ dukkhaṃ vedayitaṃ|kāyasamphassajā asātā dukkhā vedanā",
       r"^.*?ဖြစ်ပေါ်သော (?=ကိုယ်ပိုင်းဆိုင်ရာ)")
p1list(r"^Yaṃ tasmiṃ samaye cittaṃ mano mānasaṃ", "cittaṃ|mano|mānasaṃ|hadayaṃ|paṇḍaraṃ|mano|manāyatanaṃ|"
       "manindriyaṃ|viññāṇaṃ|viññāṇakkhandho|tajjāmanoviññāṇadhātu")
p1list(r"^Yo tasmiṃ samaye takko vitakko saṅkappo appanā byappanā cetaso abhiniropanā sammāsaṅkappo –",
       "takko|vitakko|saṅkappo|appanā|byappanā|cetaso abhiniropanā|sammāsaṅkappo")
p1list(r"^Yā tasmiṃ samaye pīti pāmojjaṃ .* pītisambojjhaṅgo –",
       "pīti|pāmojjaṃ|āmodanā|pamodanā|hāso|pahāso|vitti|odagyaṃ|attamanatā cittassa|pītisambojjhaṅgo")
p1list(r"^Yā tasmiṃ samaye cittassa ṭhiti .* samādhisambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ –",
       "cittassa ṭhiti|saṇṭhiti|avaṭṭhiti|avisāhāro|avikkhepo|avisāhaṭamānasatā|samatho|samādhindriyaṃ|samādhibalaṃ|"
       "sammāsamādhi|samādhisambojjhaṅgo|maggaṅgaṃ|maggapariyāpannaṃ")
p1list(r"^Yo tasmiṃ samaye cetasiko vīriyārambho .* vīriyasambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ –",
       "cetasiko vīriyārambho|nikkamo|parakkamo|uyyāmo|vāyāmo|ussāho|ussoḷhī|thāmo|dhiti|asithilaparakkamatā|"
       "anikkhittachandatā|anikkhittadhuratā|dhurasampaggāho|vīriyaṃ|vīriyindriyaṃ|vīriyabalaṃ|sammāvāyāmo|"
       "vīriyasambojjhaṅgo|maggaṅgaṃ|maggapariyāpannaṃ")
p1list(r"^Yā tasmiṃ samaye sati anussati .* satisambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ –",
       "sati|anussati|paṭissati|sati|saraṇatā|dhāraṇatā|apilāpanatā|asammussanatā|sati|satindriyaṃ|satibalaṃ|"
       "sammāsati|satisambojjhaṅgo|maggaṅgaṃ|maggapariyāpannaṃ")
p1list(r"^Yā tasmiṃ samaye saddhā saddahanā", "saddhā|saddahanā|okappanā|abhippasādo|saddhā|saddhindriyaṃ|saddhābalaṃ")
_PANNA = ("paññā|pajānanā|vicayo|pavicayo|dhammavicayo|sallakkhaṇā|upalakkhaṇā|paccupalakkhaṇā|paṇḍiccaṃ|kosallaṃ|"
          "nepuññaṃ|vebhabyā|cintā|upaparikkhā|bhūrī|medhā|pariṇāyikā|vipassanā|sampajaññaṃ|patodo|paññā|paññindriyaṃ|"
          "paññābalaṃ|paññāsatthaṃ|paññāpāsādo|paññāāloko|paññāobhāso|paññāpajjoto|paññāratanaṃ|amoho|dhammavicayo|"
          "sammādiṭṭhi|dhammavicayasambojjhaṅgo|maggaṅgaṃ|maggapariyāpannaṃ")
H_ANANNATA = p1list(r"^Yā tesaṃ dhammānaṃ anaññātānaṃ", _PANNA, r"^.*?မျက်မှောက်ပြုရန် ဖြစ်သော ")
H_ANNA = p1list(r"^Yā tesaṃ dhammānaṃ ñātānaṃ", _PANNA, r"^.*?မျက်မှောက်ပြုရန် ဖြစ်သော ")
_VIR = "ārati|virati|paṭivirati|veramaṇī|akiriyā|akaraṇaṃ|anajjhāpatti|velāanatikkamo|setughāto"
H_VACA = p1list(r"^Yā tasmiṃ samaye catūhi vacīduccaritehi", _VIR + "|sammāvācā|maggaṅgaṃ|maggapariyāpannaṃ",
                r"^.*?လေးပါးမှ ")
H_KAMMANTA = p1list(r"^Yā tasmiṃ samaye tīhi kāyaduccaritehi", _VIR + "|sammākammanto|maggaṅgaṃ|maggapariyāpannaṃ",
                    r"^.*?သုံးပါးမှ ")
H_AJIVA = p1list(r"^Yā tasmiṃ samaye micchāājīvā", _VIR + "|sammāājīvo|maggaṅgaṃ|maggapariyāpannaṃ",
                 r"^.*?အသက်မွေးမှုမှ ")
H_PASS3 = p1list(r"^Yā tasmiṃ samaye vedanākkhandhassa saññākkhandhassa saṅkhārakkhandhassa passaddhi .* "
                 r"passaddhisambojjhaṅgo –",
                 "passaddhi|paṭipassaddhi|passambhanā|paṭipassambhanā|paṭipassambhitattaṃ|passaddhisambojjhaṅgo",
                 r"^.*?တို့၏ ")
H_RUPAJIV = p1list(r"^Yo tesaṃ rūpīnaṃ dhammānaṃ āyu", "āyu|ṭhiti|yapanā|yāpanā|iriyanā|vattanā|pālanā|jīvitaṃ|"
                   "jīvitindriyaṃ", r"^.*?တို့၏ ")
H_ARUPAJIV = p1list(r"^Yo tesaṃ arūpīnaṃ dhammānaṃ āyu", "āyu|ṭhiti|yapanā|yāpanā|iriyanā|vattanā|pālanā|jīvitaṃ|"
                    "jīvitindriyaṃ", r"^.*?တို့၏ ")
H_ITTHI = p1list(r"^Yaṃ itthiyā itthiliṅgaṃ", "itthiliṅgaṃ|itthinimittaṃ|itthikuttaṃ|itthākappo|itthattaṃ|itthibhāvo",
                 r"^မိန်းမ၏ ")
H_PURISA = p1list(r"^Yaṃ purisassa purisaliṅgaṃ", "purisaliṅgaṃ|purisanimittaṃ|purisakuttaṃ|purisākappo|purisattaṃ|"
                  "purisabhāvo", r"^ယောက်ျား၏ ")
p1list(r"^Yo rāgo sārāgo anunayo", "rāgo|sārāgo|anunayo|anurodho|nandī|nandīrāgo|cittassa sārāgo", partial=True)
assert TAJJA_MANO.startswith("သက်ဆိုင်ရာ မနော")
for _a, _b in (("paṭippassaddhi", "paṭipassaddhi"), ("paṭippassambhanā", "paṭipassambhanā"),
               ("paṭippassambhitattaṃ", "paṭipassambhitattaṃ")):
    learn(_a, SYN2[_b], "Vb spelling of the same word")        # Vb «paṭipp-» = Dhs «paṭip-» (spelling only)
learn("ṭhiti", P1.SYN["ṭhiti"], "pi-1 SYN (the jīvita list ṭhiti)")
learn("maggariyāpannaṃ", SYN2["maggapariyāpannaṃ"], "source slip (ch9 ^2-459): read as maggapariyāpannaṃ")
assert SYN2["ṭhiti"] == "တည်တံ့ခြင်း"

# names of the indriyas from the pi-1 closers («– idaṃ tasmiṃ samaye X hoti» / «… rūpaṃ X»)
_CLOSE = re.compile(r"ဤသည်မှာ (?:ထိုအချိန်၌ ရှိသော )?(.+?) ဖြစ်(?:သော ရုပ် ဖြစ်)?သည်")


def p1name(rx):
    _, t = p1(rx)
    m = _CLOSE.search(t)
    if not m:
        raise SystemExit("pi-1 closer: " + rx)
    return m[1]


NAME = {}             # Pāli name (definiendum / subject / list item) -> Burmese
for _k in ("cakkhundriyaṃ", "sotindriyaṃ", "ghānindriyaṃ", "jivhindriyaṃ", "kāyindriyaṃ", "manindriyaṃ",
           "itthindriyaṃ", "purisindriyaṃ", "jīvitindriyaṃ", "sukhindriyaṃ", "dukkhindriyaṃ", "somanassindriyaṃ",
           "domanassindriyaṃ", "upekkhindriyaṃ", "saddhindriyaṃ", "vīriyindriyaṃ", "satindriyaṃ", "samādhindriyaṃ",
           "paññindriyaṃ"):
    NAME[_k] = F.term_my(_k).removesuffix(" ဖြစ်သော") if _k in F.INDR else P1.NAMES.get(_k) or F.C3["NOUN"][_k]
NAME["anaññātaññassāmītindriyaṃ"] = p1name(r"^Yā tesaṃ dhammānaṃ anaññātānaṃ")
NAME["aññindriyaṃ"] = p1name(r"^Yā tesaṃ dhammānaṃ ñātānaṃ")
NAME["aññātāvindriyaṃ"] = p1name(r"^Yā tesaṃ aññātāvīnaṃ dhammānaṃ")
assert NAME["itthindriyaṃ"] == p1name(r"^Yaṃ itthiyā itthiliṅgaṃ") and NAME["jīvitindriyaṃ"] == p1name(r"^Yo tesaṃ rūpīnaṃ")
INDR22 = list(NAME)
for _k in INDR22:
    SYN2.setdefault(_k, NAME[_k])
_, _t = p1(r"^Yā tesaṃ aññātāvīnaṃ dhammānaṃ")                  # «အပြည့်အဝ သိမြင်ပြီးသော ထို သဘောတရားတို့၏ …»
_ANNATAVI = _t.split("သော ", 1)[0]                                   # aññātāvī = «အပြည့်အဝ သိမြင်ပြီး»
assert _ANNATAVI == "အပြည့်အဝ သိမြင်ပြီး" and H_ANNA.startswith("သိပြီး၊ မြင်ပြီး၊")
H_ANNATAVI = new("tesaṃ dhammānaṃ aññātāvīnaṃ diṭṭhānaṃ pattānaṃ viditānaṃ sacchikatānaṃ sacchikiriyāya",
                 H_ANNA.replace("သိပြီး၊", _ANNATAVI + "၊", 1))

# the six bojjhaṅgas known in pi-1 (list items) + the seventh (new)
BOJ = {"sati": "satisambojjhaṅgo", "dhammavicaya": "dhammavicayasambojjhaṅgo", "vīriya": "vīriyasambojjhaṅgo",
       "pīti": "pītisambojjhaṅgo", "passaddhi": "passaddhisambojjhaṅgo", "samādhi": "samādhisambojjhaṅgo"}
BOJJHANGA = SYN2["satisambojjhaṅgo"].split(" ")[-1]
assert BOJJHANGA == "ဗောဇ္ဈင်"
learn("upekkhāsambojjhaṅgo", new("upekkhāsambojjhaṅgo", f"{P1.NAMES['upekkhā']} {BOJJHANGA}"), "new")
BOJ["upekkhā"] = "upekkhāsambojjhaṅgo"
for _k, _v in BOJ.items():
    NAME[_v] = SYN2[_v]
NAME["satta bojjhaṅgā"] = new("satta bojjhaṅgā", P1.count_my(BOJJHANGA, "satta"))
NAME["cha bojjhaṅgā"] = new("cha bojjhaṅgā", P1.count_my(BOJJHANGA, "cha"))
# the path factors (pi-1)
PATH8 = ["sammādiṭṭhi", "sammāsaṅkappo", "sammāvācā", "sammākammanto", "sammāājīvo", "sammāvāyāmo", "sammāsati",
         "sammāsamādhi"]
for _k in PATH8:
    NAME[_k] = SYN2[_k]
NAME["aṭṭhaṅgiko maggo"] = in_p1(r"aṭṭhaṅgiko maggo hoti", f"{P1.count_my(P1._ANGA, 'aṭṭha')} ရှိသော {P1.MAGGA}")
NAME["pañcaṅgiko maggo"] = P1.NAMES["pañcaṅgiko maggo"]
MAGGANGA = SYN2["maggaṅgaṃ"]                                        # မဂ်၏ အင်္ဂါ
NAME["satta maggaṅgā"] = new("satta maggaṅgā", P1.count_my(MAGGANGA, "satta"))
NAME["aṭṭha maggaṅgā"] = new("aṭṭhannaṃ maggaṅgānaṃ", P1.count_my(MAGGANGA, "aṭṭha"))
ARIYA_MAGGA = new("ariyo aṭṭhaṅgiko maggo", NAME["aṭṭhaṅgiko maggo"].removesuffix(" " + P1.MAGGA) + " အရိယာ " + P1.MAGGA)

# ===================================================================================== headings, colophons
HEAD_NEW = {
    "Indriyavibhaṅgo": f"{P1.INDRIYA}များကို {F.TITLE}",
    "Satipaṭṭhānavibhaṅgo": f"သတိပဋ္ဌာန်များကို {F.TITLE}",
    "Sammappadhānavibhaṅgo": f"{P1.SAMMA} {P1.PADHANA}များကို {F.TITLE}",
    "Iddhipādavibhaṅgo": f"ဣဒ္ဓိပါဒ်များကို {F.TITLE}",
    "Bojjhaṅgavibhaṅgo": f"{BOJJHANGA}များကို {F.TITLE}",
    "Maggaṅgavibhaṅgo": f"{MAGGANGA}များကို {F.TITLE}",
}
# the pi-1 words: «သတိပဋ္ဌာန်», «မှန်ကန်သော ကြိုးပမ်းအားထုတ်ခြင်း», «ဣဒ္ဓိပါဒ်», «ဗောဇ္ဈင်» (pi-1 ^ lokuttara series)
in_p1(r"lokuttaraṃ satipaṭṭhānaṃ bhāveti", "သတိပဋ္ဌာန်ကို", f"{P1.SAMMA} {P1.PADHANA}ကို", "ဣဒ္ဓိပါဒ်ကို",
      f"{BOJJHANGA}ကို")
SATIPATTHANA, SAMMAPPADHANA, IDDHIPADA = "သတိပဋ္ဌာန်", f"{P1.SAMMA} {P1.PADHANA}", "ဣဒ္ဓိပါဒ်"
VIMAMSA = P1.VIMAMSA                                                   # စုံစမ်းဆင်ခြင်မှု (pi-1 vīmaṃsā)
NIDDESA = new("-niddeso", "ကို ဖွင့်ဆိုချက်")
ANUP = new("anupassī", "အဖန်ဖန် ရှုသူ")
ANUPANA = new("anupassanā", "အဖန်ဖန် ရှုခြင်း")
CONT = {"kāya": "ကိုယ်", "vedanā": P1.FEEL, "citta": P1.MIND, "dhamma": DH}          # the four objects
for _k, _v in {"Kāyānupassanāniddeso": "kāya", "Vedanānupassanāniddeso": "vedanā", "Cittānupassanāniddeso": "citta",
               "Dhammānupassanāniddeso": "dhamma"}.items():
    HEAD_NEW[_k] = new(_k, f"{CONT[_v]}ကို {ANUPANA}{NIDDESA}")
SAMADHI = P1.NAMES["samādhindriyaṃ"].split("၏")[0]                    # သမာဓိ
PS = new("padhānasaṅkhāro", f"{P1.PADHANA} {P1.SANKHARA}")             # effort-formation
IDP = {"chanda": "ဆန္ဒ", "vīriya": SYN2["vīriyaṃ"], "citta": P1.MIND, "vīmaṃsā": VIMAMSA}
for _k, _v in IDP.items():
    NAME[_k + ("" if _k == "vīmaṃsā" else "") + "samādhi"] = new(_k + "samādhi", f"{_v} {SAMADHI}")
    st = {"chanda": "chand", "vīriya": "vīriy", "citta": "citt", "vīmaṃsā": "vīmaṃs"}[_k]
    NAME[st + "iddhipādo"] = new(st + "iddhipādo", f"{_v} {IDDHIPADA}")
    HEAD_NEW[(st + "iddhipādo").capitalize()] = NAME[st + "iddhipādo"]
NAME["vīmaṃsāsamādhi"] = NAME.pop("vīmaṃsāsamādhi")
F.HEAD.update(HEAD_NEW)
for _k, _v in HEAD_NEW.items():
    new(_k, _v)
COLO_NEW = {k: v for k, v in HEAD_NEW.items() if k.endswith("niddeso")}
for _k in ("Indriyavibhaṅgo", "Satipaṭṭhānavibhaṅgo", "Sammappadhānavibhaṅgo", "Iddhipādavibhaṅgo", "Bojjhaṅgavibhaṅgo",
           "Maggaṅgavibhaṅgo"):
    COLO_NEW[_k + " niṭṭhito"] = f"“{HEAD_NEW[_k]}” {F.NITTHITA}"
F.COLO.update(COLO_NEW)

# ===================================================================================== variants
LEK, PAT = P1.LEKHANA, P1.PATHA
VKIND = {"viriyindriyaṃ": LEK, "nahāru": LEK, "aṭṭhimiñjā": LEK, "thīnamiddhaṃ": LEK, "viriyasambojjhaṅgaṃ": LEK,
         "katamaṃ ātāpaṃ": PAT, "chandīkatā": LEK, "cittassa ekaggataṃ": LEK, "saṅkhaṃ": LEK, "kāyappassaddhi": LEK,
         "cittappassaddhi": LEK, "odaggaṃ": LEK, "uṭṭhāpeti samuṭṭhāpeti": LEK}
SIGLA = dict(P1.SIGLA, **{"sabbattha": "Sabbattha"})
VEXTRA = {"evamuparipi": new("evamuparipi (variant note)", "နောက်ပိုင်း၌လည်း ဤနည်းတူ"),
          "dha. sa. 9": new("dha. sa. 9 (variant note)", f"“{P1.TITLE}” 9")}


def var2(br):
    m = re.fullmatch(r"\[(?P<t>[^\[\]()]+?) \((?P<s>[^()]+)\)(?: (?P<x>[^\]]+))?\]", br)
    if not m or m["t"] not in VKIND:
        raise Miss("variant: " + br)
    sig = ", ".join(SIGLA[s] for s in m["s"].split())
    x = f"{C} {VEXTRA[m['x']]}" if m["x"] else ""
    return f"[{VKIND[m['t']]} ({sig}): {m['t']}{x}]"


# ===================================================================================== new list items (pi-2)
_NEW_SYN = {
    # chanda
    "chando": "ဆန္ဒ", "chandikatā": "ဆန္ဒ ပြုခြင်း", "kattukamyatā": "ပြုလုပ်လိုခြင်း",
    "kusalo dhammacchando": f"{T['kusalā']} {DH}ကို လိုလားသော ဆန္ဒ",
    # upekkhā (bojjhaṅga)
    "upekkhā": P1.NAMES["upekkhā"], "upekkhanā": "ဥပေက္ခာဖြင့် ရှုခြင်း", "ajjhupekkhanā": "ဥပေက္ခာဖြင့် လွန်စွာ ရှုခြင်း",
    "majjhattatā cittassa": "စိတ်၏ အလယ်အလတ်၌ တည်ခြင်း",
    # iddhi
    "iddhi": "ဣဒ္ဓိ", "samiddhi": "ကောင်းစွာ ပြည့်စုံခြင်း", "ijjhanā": "ပြီးမြောက်ခြင်း",
    "samijjhanā": "ကောင်းစွာ ပြီးမြောက်ခြင်း", "lābho": "ရခြင်း", "paṭilābho": "ထပ်မံ ရခြင်း", "patti": "ရောက်ခြင်း",
    "sampatti": "ကောင်းစွာ ရောက်ခြင်း", "phusanā": P1.SYN["phusanā"], "sacchikiriyā": "မျက်မှောက်ပြုခြင်း",
    "upasampadā": "ပြည့်စုံစွာ ရရှိခြင်း",
}
for _k, _v in _NEW_SYN.items():
    if _k not in SYN2:
        learn(_k, new(_k, _v) if _k not in ("phusanā", "upekkhā") else _v, "new")
SYN2["avikkhepo"] = SYN2["avikkhepo"]
for _k in ("phasso", "paggāho", "vedanākkhandho", "saññākkhandho", "saṅkhārakkhandho", "viññāṇakkhandho"):
    SYN2.setdefault(_k, P1.NAMES[_k])
LHEAD = {   # heads of a definition list (between «Yo / Yā / Yaṃ [tasmiṃ samaye]» and the items)
    "tesaṃ dhammānaṃ anaññātānaṃ adiṭṭhānaṃ appattānaṃ aviditānaṃ asacchikatānaṃ sacchikiriyāya": H_ANANNATA,
    "tesaṃ dhammānaṃ ñātānaṃ diṭṭhānaṃ pattānaṃ viditānaṃ sacchikatānaṃ sacchikiriyāya": H_ANNA,
    "tesaṃ dhammānaṃ aññātāvīnaṃ diṭṭhānaṃ pattānaṃ viditānaṃ sacchikatānaṃ sacchikiriyāya": H_ANNATAVI,
    "catūhi vacīduccaritehi": H_VACA, "tīhi kāyaduccaritehi": H_KAMMANTA, "micchāājīvā": H_AJIVA,
    "tesaṃ rūpīnaṃ dhammānaṃ": H_RUPAJIV, "tesaṃ arūpīnaṃ dhammānaṃ": H_ARUPAJIV,
    "itthiyā": H_ITTHI, "purisassa": H_PURISA,
    "vedanākkhandhassa saññākkhandhassa saṅkhārakkhandhassa viññāṇakkhandhassa": new(
        "vedanākkhandhassa saññākkhandhassa saṅkhārakkhandhassa viññāṇakkhandhassa",
        H_PASS3.replace(f"နှင့် {P1.NAMES['saṅkhārakkhandho']}တို့၏ ",
                        f"{C} {P1.NAMES['saṅkhārakkhandho']}နှင့် {P1.NAMES['viññāṇakkhandho']}တို့၏ ")),
    "tesaṃ dhammānaṃ": new("tesaṃ dhammānaṃ (iddhi list)", f"ထို {DH}တို့၏ "),
}
assert H_PASS3 == f"{P1.NAMES['vedanākkhandho']}{C} {P1.NAMES['saññākkhandho']}နှင့် {P1.NAMES['saṅkhārakkhandho']}တို့၏ "
REL = "ရှိသမျှ"                                     # Yo / Yā / Yaṃ (pi-1 L02)
SYN_MAX = 6

# ===================================================================================== pi-1 formulas (read)
_, _LOK = p1(r"^Yasmiṃ samaye lokuttaraṃ jhānaṃ bhāveti niyyānikaṃ apacayagāmiṃ diṭṭhigatānaṃ pahānāya paṭhamāya "
             r"bhūmiyā pattiyā vivicceva kāmehi…pe… paṭhamaṃ jhānaṃ upasampajja viharati dukkhapaṭipadaṃ dandhābhiññaṃ, "
             r"tasmiṃ samaye phasso hoti, vedanā")
_JH1 = f"{P1.ORD['paṭhama']} {P1.JHANA}ကို ဝင်စား၍ "
LOK_A, _rest = _LOK.split(_JH1, 1)
assert _rest.startswith("နေသော " + P1.YASMIM)
_, _VIP = p1(r"^Tasseva lokuttarassa kusalassa jhānassa katattā bhāvitattā vipākaṃ vivicceva kāmehi…pe… paṭhamaṃ jhānaṃ "
             r"upasampajja viharati dukkhapaṭipadaṃ dandhābhiññaṃ suññataṃ, tasmiṃ samaye phasso hoti…pe…")
VIP_A = _VIP.split(_JH1, 1)[0]
SUNNATA = f"{C} ဆိတ်သုဉ်းသော"
assert VIP_A.endswith(SUNNATA + " ") and VIP_A.startswith("ထို လောကကို ကျော်လွန်သော")
NOW = f"နေသော {P1.YASMIM}"                                              # … upasampajja viharati (yasmiṃ samaye)
IDHA = in_p1(r"Saṃviggassa ca yoniso padhānanti – idha bhikkhu", "ဤသာသနာ၌ ရဟန်းသည်")
PHASSA_AVIK = in_p1(r"^Yasmiṃ samaye lokuttaraṃ cittaṃ|lokuttaraṃ cittaṃ bhāveti",
                    f"{P1.TASMIM} {P1.NAMES['phasso']} {P1.CU_HOTI['sg']}{PE} {P1.NAMES['avikkhepo']} {P1.CU_HOTI['sg']}")
# the sammappadhāna formula (pi-1 4-03 «Saṃviggassa ca yoniso padhānaṃ»)
_AK, _KU = T["akusalā"], T["kusalā"]
SP_V = "ဆန္ဒကို ဖြစ်စေ၏၊ အားထုတ်၏၊ ဝီရိယကို စတင်၏၊ စိတ်ကို မြှင့်တင်၏၊ ကြိုးပမ်း၏"
_, _t = p1(r"Saṃviggassa ca yoniso padhānanti – idha bhikkhu")
_seg = _t.split(IDHA + " ", 1)[1].split(" " + SP_V)                  # the four purposes, read from pi-1 final text
assert len(_seg) == 5 and _seg[4] == END, _seg
SP_P = dict(zip(["anuppannānaṃ pāpakānaṃ akusalānaṃ dhammānaṃ anuppādāya",
                 "uppannānaṃ pāpakānaṃ akusalānaṃ dhammānaṃ pahānāya",
                 "anuppannānaṃ kusalānaṃ dhammānaṃ uppādāya",
                 "uppannānaṃ kusalānaṃ dhammānaṃ ṭhitiyā asammosāya bhiyyobhāvāya vepullāya bhāvanāya pāripūriyā"],
                [x.removeprefix(C + " ") for x in _seg[:4]]))
assert SP_P["anuppannānaṃ kusalānaṃ dhammānaṃ uppādāya"].startswith(T["anuppannā"] + " " + _KU)
# roots, aggregates, kamma (pi-1 4-01 «Tīṇi kusalamūlāni / akusalamūlāni»)
ROOTS = {"Tīṇi akusalamūlāni": f"{_AK}၏ {P1.ROOT} {P1.NUM['ti']}{P1.CL}", "Tīṇi kusalamūlāni": f"{_KU}၏ {P1.ROOT} "
         f"{P1.NUM['ti']}{P1.CL}", "lobho": "လောဘ", "doso": "ဒေါသ", "moho": "မောဟ", "alobho": P1.NAMES["alobho"],
         "adoso": P1.NAMES["adoso"], "amoho": P1.NAMES["amoho"],
         "Tadekaṭṭhā ca kilesā": f"ထိုတို့နှင့် တစ်နေရာတည်း တည်ရှိသော {P1.KIL}များလည်း",
         "Taṃsampayutto": "ထိုတို့နှင့် ယှဉ်တွဲသော", "taṃsamuṭṭhānaṃ": "ထိုတို့မှ ဖြစ်ပေါ်လာသော",
         "Taṃsamuṭṭhānaṃ": "ထိုတို့မှ ဖြစ်ပေါ်လာသော",
         "kāyakammaṃ": "ကိုယ်ဖြင့် ပြုသော ကံ", "vacīkammaṃ": "နှုတ်ဖြင့် ပြုသော ကံ", "manokammaṃ": "မနောဖြင့် ပြုသော ကံ"}
in_p1(r"^Tīṇi akusalamūlāni – lobho", *[v for k, v in ROOTS.items() if k not in ("alobho", "adoso", "amoho",
                                                                                   "Tīṇi kusalamūlāni")])
in_p1(r"^Tīṇi kusalamūlāni – alobho", ROOTS["Tīṇi kusalamūlāni"], ROOTS["alobho"], ROOTS["adoso"], ROOTS["amoho"])
# the four jhānas (pi-1 2-02, without the kasiṇa; the «ācikkhanti –» dash dropped: Vb has none)
J = P1.JH_FORM
_JORD = {"paṭhamaṃ": "paṭhama", "dutiyaṃ": "dutiya", "tatiyaṃ": "tatiya", "catutthaṃ": "catuttha"}
JHANAS = {}
for _pl, _keys in (
        ("vivicceva kāmehi vivicca akusalehi dhammehi savitakkaṃ savicāraṃ vivekajaṃ pītisukhaṃ paṭhamaṃ",
         ["vivicceva kāmehi", "vivicca akusalehi dhammehi", "savitakkaṃ", "savicāraṃ", "vivekajaṃ pītisukhaṃ"]),
        ("vitakkavicārānaṃ vūpasamā ajjhattaṃ sampasādanaṃ cetaso ekodibhāvaṃ avitakkaṃ avicāraṃ samādhijaṃ pītisukhaṃ "
         "dutiyaṃ", ["vitakkavicārānaṃ vūpasamā", "ajjhattaṃ sampasādanaṃ", "cetaso ekodibhāvaṃ", "avitakkaṃ", "avicāraṃ",
                     "samādhijaṃ pītisukhaṃ"]),
        ("pītiyā ca virāgā upekkhako ca viharati sato ca sampajāno sukhañca kāyena paṭisaṃvedeti, yaṃ taṃ ariyā ācikkhanti "
         "\"upekkhako satimā sukhavihārī\"ti tatiyaṃ", ["pītiyā ca virāgā", "upekkhako ca viharati", "sato ca sampajāno",
                                                     "sukhañca kāyena paṭisaṃvedeti",
                                                     "yaṃ taṃ ariyā ācikkhanti – \"upekkhako satimā sukhavihārī\"ti"]),
        ("sukhassa ca pahānā dukkhassa ca pahānā pubbeva somanassadomanassānaṃ atthaṅgamā adukkhamasukhaṃ "
         "upekkhāsatipārisuddhiṃ catutthaṃ", ["sukhassa ca pahānā", "dukkhassa ca pahānā",
                                              "pubbeva somanassadomanassānaṃ atthaṅgamā", "adukkhamasukhaṃ",
                                              "upekkhāsatipārisuddhiṃ"])):
    _ord = _pl.rsplit(" ", 1)[1]
    _my = f"{C} ".join(J[k] for k in _keys).replace("က – “", "က “")
    _rx = r"^Yasmiṃ samaye rūpūpapattiyā maggaṃ bhāveti " + re.escape(_pl.rsplit(" ", 1)[0].split(" ")[0])
    in_p1(_rx, *[J[k] for k in _keys])
    JHANAS[_pl + " jhānaṃ upasampajja viharati"] = f"{_my} {P1.ORD[_JORD[_ord]]} {P1.JHANA}ကို ဝင်စား၍ နေ၏"
for _k, _v in JHANAS.items():
    new(_k + " (pi-1 pieces; finite verb)", _v)
# the cakkhu / kāya definitions (pi-1 3-02), with «…pe…»: first clause up to the organ, last item
_CAK = {}
for _o, _rx in (("cakkhu", r"^Yaṃ cakkhu catunnaṃ mahābhūtānaṃ upādāya pasādo"),
                ("kāyo", r"^Yo kāyo catunnaṃ mahābhūtānaṃ upādāya pasādo")):
    _, _t = p1(_rx)
    _first = _t.split(f"{C} ", 1)[0]                                # «… ကြည်လင်မှု ဖြစ်သည့်»
    _last = _t.split(" – ")[0].rsplit(f"{C} ", 1)[1]                 # «ဆိတ်သုဉ်းသော ရွာလည်း ဤသည်ပင်»
    _organ = F.SENSE["cakkhu" if _o == "cakkhu" else "kāya"]
    _CAK[_o] = f"{_first} {_organ}{PE} {_last}"
    assert _first.endswith("ဖြစ်သည့်") and _last.startswith("ဆိတ်သုဉ်းသော ရွာ"), (_first, _last)

# ===================================================================================== definienda / names
NAME.update({k: P1.NAMES[k] for k in ("vedanākkhandho", "saññākkhandho", "saṅkhārakkhandho", "viññāṇakkhandho")})
NAME.update({k: P1.NAMES[k] for k in ("phasso", "paggāho", "avikkhepo")})
NAME["viññāṇakhandho"] = NAME["viññāṇakkhandho"]                        # source slip (ch9, ^2-443 block)
NAME.update({
    "anupassanā": ANUPANA, "ātāpo": new("ātāpo", "ထက်သန်သော လုံ့လ"), "sampajaññaṃ": P1.NAMES["sampajaññaṃ"],
    "sati": P1.NAMES["sati"], "loko": new("loko", "လောက"), "abhijjhā": new("abhijjhā", "သူ့ဥစ္စာကို လိုချင်ခြင်း"),
    "domanassaṃ": new("domanassaṃ", "စိတ်ဆင်းရဲမှု"), "chando": SYN2["chando"], "vāyāmo": SYN2["vāyāmo"],
    "vīriyaṃ": SYN2["vīriyaṃ"], "cittaṃ": P1.MIND, "padhānaṃ": P1.PADHANA, "sammappadhānaṃ": SAMMAPPADHANA,
    "satipaṭṭhānaṃ": SATIPATTHANA, "samādhi": SAMADHI, "padhānasaṅkhāro": PS, "vīmaṃsā": VIMAMSA,
    "padhānasaṅkhārā": new("padhānasaṅkhārā", PS + "များ"),
    "rūpajīvitindriyaṃ": new("rūpajīvitindriyaṃ", f"{T['rūpino']} {NAME['jīvitindriyaṃ']}"),
    "arūpajīvitindriyaṃ": new("arūpajīvitindriyaṃ", f"{T['arūpino']} {NAME['jīvitindriyaṃ']}"),
    "anuppannā pāpakā akusalā dhammā": f"{T['anuppannā']} ယုတ်မာသော {_AK} {DHP}",
    "uppannā pāpakā akusalā dhammā": f"{T['uppannā']} ယုတ်မာသော {_AK} {DHP}",
    "anuppannā kusalā dhammā": f"{T['anuppannā']} {_KU} {DHP}", "uppannā kusalā dhammā": f"{T['uppannā']} {_KU} {DHP}",
    "iddhipādo": IDDHIPADA,
})
NAME["arūpajīvatindriyaṃ"] = NAME["arūpajīvitindriyaṃ"]              # source slip ^2-219 block (line 18)
for _k in IDP:
    _n = {"chanda": "chanda", "vīriya": "vīriya", "citta": "citta", "vīmaṃsā": "vīmaṃsā"}[_k]
    NAME[_n + "samādhipadhānasaṅkhāro"] = new(_n + "samādhipadhānasaṅkhāro", f"{IDP[_k]} {SAMADHI}နှင့် {PS}")
    NAME[_n + "samādhipadhānasaṅkhārasamannāgato"] = new(
        _n + "samādhipadhānasaṅkhārasamannāgato", f"{IDP[_k]} {SAMADHI}နှင့် {PS}တို့ဖြင့် အပြည့်အဝ ပြည့်စုံသူ")
PL_NAMES = {"anuppannā pāpakā akusalā dhammā", "uppannā pāpakā akusalā dhammā", "anuppannā kusalā dhammā",
            "uppannā kusalā dhammā", "satta bojjhaṅgā", "padhānasaṅkhārā"}


def nm(p):
    if p not in NAME:
        raise Miss("name: " + p)
    return NAME[p]


# glosses «X-ti.» (the word explained) -> Burmese (the form used in the formula)
ATAPI = new("ātāpī", "ထက်သန်သော လုံ့လ ရှိသူ")
SAMPAJANO = new("sampajāno", f"{P1.NAMES['sampajaññaṃ'].removesuffix('ခြင်း')}သူ")
SATIMA = in_p1(r"upekkhako satimā sukhavihārī", "သတိ ရှိသူ")
VIHARATI = new("viharati", "နေ၏")
VINEYYA = new("vineyya loke abhijjhādomanassaṃ",
              f"{NAME['loko']}၌ {NAME['abhijjhā']}နှင့် {NAME['domanassaṃ']}ကို ပယ်ဖျောက်၍")
ATAPI_CHAIN = f"{ATAPI}{C} {SAMPAJANO}{C} {SATIMA} ဖြစ်လျက် {VINEYYA} {VIHARATI}"
SP_GL = dict(zip(["chandaṃ janetī", "vāyamatī", "vīriyaṃ ārabhatī", "cittaṃ paggaṇhātī", "padahatī"],
                 SP_V.split(C + " ")))
GL = {"anupassī": ANUP, "viharatī": VIHARATI, "ātāpī": ATAPI, "sampajāno": SAMPAJANO, "satimā": SATIMA,
      "vineyya loke abhijjhādomanassa": VINEYYA, "ṭhitiyā": "တည်တံ့ရန်", "iddhī": "ဣဒ္ဓိ", "iddhipādo": IDDHIPADA,
      "iddhipādaṃ bhāvetī": f"{IDDHIPADA}ကို ပွားများ၏", **SP_GL}
for _k in NAME:
    if _k.endswith("samannāgato"):
        GL[_k] = NAME[_k]
TI = " ဟူသည်"                                         # «X-ti.» heading word (pi-1 make_ch4 «Saṃvegoti» = «… ဟူသည်»)

# ===================================================================================== phrases (fixed)
QA = {"ajjhattaṃ": T["ajjhattā"], "bahiddhā": T["bahiddhā"], "ajjhattabahiddhā": T["ajjhattabahiddhā"]}
LOC = {"kāye": "kāya", "vedanāsu": "vedanā", "citte": "citta", "dhammesu": "dhamma"}
LOCMY = {"kāya": CONT["kāya"] + "၌", "vedanā": P1.FEEL + "တို့၌", "citta": P1.MIND + "၌", "dhamma": P1.DHAMMA_LOC}
ANUPA = {"kāya": "kāyānupassī", "vedanā": "vedanānupassī", "citta": "cittānupassī", "dhamma": "dhammānupassī"}


def contemp(q, loc):
    """«[ajjhattaṃ] kāye kāyānupassī» = «[မိမိ၌ ရှိသော] ကိုယ်၌ ကိုယ်ကို အဖန်ဖန် ရှုသူ ဖြစ်လျက်»."""
    o = LOC[loc]
    return f"{QA[q] + ' ' if q else ''}{LOCMY[o]} {CONT[o]}ကို {ANUP} ဖြစ်လျက်"


new("kāye kāyānupassī", contemp(None, "kāye"))
BODY32 = {"kesā": "ဆံပင်", "lomā": "မွေးညင်း", "nakhā": "ခြေသည်းလက်သည်း", "dantā": "သွား", "taco": "အရေ",
          "maṃsaṃ": "အသား", "nhāru": "အကြော", "aṭṭhi": "အရိုး", "aṭṭhimiñjaṃ": "ရိုးတွင်းခြင်ဆီ", "vakkaṃ": "ကျောက်ကပ်",
          "hadayaṃ": "နှလုံး", "yakanaṃ": "အသည်း", "kilomakaṃ": "အမြှေး", "pihakaṃ": "အဖျဉ်း", "papphāsaṃ": "အဆုတ်",
          "antaṃ": "အူမ", "antaguṇaṃ": "အူသိမ်", "udariyaṃ": "အစာသစ်", "karīsaṃ": "အစာဟောင်း", "pittaṃ": "သည်းခြေ",
          "semhaṃ": "သလိပ်", "pubbo": "ပြည်", "lohitaṃ": "သွေး", "sedo": "ချွေး", "medo": "အဆီခဲ", "assu": "မျက်ရည်",
          "vasā": "အဆီကြည်", "kheḷo": "တံတွေး", "siṅghāṇikā": "နှပ်", "lasikā": "အစေး", "mutta": "ဆီး"}
for _k, _v in BODY32.items():
    new(_k + " (body part)", _v)
assert len(set(BODY32.values())) == len(BODY32)
NIMITTA = f"ထို{P1.SUT['samathanimitta'].split(' ')[-1]}"               # ထိုအမှတ်အသား (nimitta = pi-1 အမှတ်အသား)
ASEV = ["အလေ့အကျင့် ပြု", "ပွားများ", "အကြိမ်ကြိမ် ပြု", "ကောင်းစွာ ပိုင်းခြား သတ်မှတ်"]      # āsevati … vavatthapeti
SO = "ထိုရဟန်းသည်"
FEELQ = {"sukh": f"{P1.SUKHA}သော", "dukkh": f"{P1.DUKKHA}သော", "adukkhamasukh": f"မ{P1.DUKKHA} မ{P1.SUKHA}သော"}
assert F.ITEM["adukkhamasukhā vedanā"] == f"{FEELQ['adukkhamasukh']} {P1.FEEL}"
AMISA = {"sāmis": new("sāmisa", "ကာမဂုဏ်နှင့် စပ်သော"), "nirāmis": new("nirāmisa", "ကာမဂုဏ်နှင့် မစပ်သော")}
VA = "ဖြစ်စေ"                                             # «X vā» = «Xဖြစ်စေ» (pi-1 TAIL form)
PAJANATI = new("pajānāti", "ကွဲပြားစွာ သိ၏")               # pajānanā = pi-1 «ကွဲပြားစွာ သိခြင်း»
CQ = {"sarāgaṃ": "ရာဂ ရှိသော", "vītarāgaṃ": "ရာဂ ကင်းသော", "sadosaṃ": "ဒေါသ ရှိသော", "vītadosaṃ": "ဒေါသ ကင်းသော",
      "samohaṃ": "မောဟ ရှိသော", "vītamohaṃ": "မောဟ ကင်းသော", "saṃkhittaṃ": "တွန့်ဆုတ်နေသော",
      "vikkhittaṃ": "ပျံ့လွင့်နေသော", "mahaggataṃ": T["mahaggatā"], "amahaggataṃ": "မ" + T["mahaggatā"],
      "sauttaraṃ": T["sauttarā"], "anuttaraṃ": T["anuttarā"], "samāhitaṃ": "တည်ကြည်သော", "asamāhitaṃ": "မတည်ကြည်သော",
      "vimuttaṃ": "လွတ်မြောက်သော", "avimuttaṃ": "မလွတ်မြောက်သော"}
for _k, _v in CQ.items():
    if _k not in ("mahaggataṃ", "sauttaraṃ", "anuttaraṃ"):
        new(_k + " cittaṃ", _v + " " + P1.MIND)
NIV = {"kāmacchand": "ကာမကို လိုလားမှု", "byāpād": "ဖျက်ဆီးလိုစိတ်", "thinamiddh": "ထိုင်းမှိုင်းမှုနှင့် ငိုက်မျဉ်းမှု",
       "uddhaccakukkucc": "ယောက်ယက်ခတ်မှုနှင့် နောင်တ ပူပန်မှု", "vicikicch": "ယုံမှားမှု"}
in_p1(r"^Cha nīvaraṇā \[", *NIV.values())
NIV.update({"satisambojjhaṅg": NAME["satisambojjhaṅgo"], "dhammavicayasambojjhaṅg": NAME["dhammavicayasambojjhaṅgo"],
            "vīriyasambojjhaṅg": NAME["vīriyasambojjhaṅgo"], "pītisambojjhaṅg": NAME["pītisambojjhaṅgo"],
            "passaddhisambojjhaṅg": NAME["passaddhisambojjhaṅgo"], "samādhisambojjhaṅg": NAME["samādhisambojjhaṅgo"],
            "upekkhāsambojjhaṅg": NAME["upekkhāsambojjhaṅgo"]})
UPETO = ["ယှဉ်သူ", "ကောင်းစွာ ယှဉ်သူ", "ချဉ်းကပ်သူ", "ကောင်းစွာ ချဉ်းကပ်သူ", "ရောက်ရှိသူ", "ပြည့်စုံသူ", "အပြည့်အဝ ပြည့်စုံသူ"]
new("upeto hoti samupeto upāgato samupāgato upapanno sampanno samannāgato", f"{C} ".join(UPETO) + " ဖြစ်၏")
INSTR = {"anupassanāya": ANUPANA, "ātāpena": NAME["ātāpo"], "sampajaññena": NAME["sampajaññaṃ"], "satiyā": NAME["sati"],
         "vāyāmena": NAME["vāyāmo"], "padhānena": P1.PADHANA, "chandena": "ဆန္ဒ", "samādhinā": SAMADHI,
         "padhānasaṅkhārena": PS, "vīriyena": NAME["vīriyaṃ"], "cittena": P1.MIND, "vīmaṃsāya": VIMAMSA}
VINITA = ["ပယ်ဖျောက်ပြီး", "လုံးဝ ပယ်ဖျောက်ပြီး", "ငြိမ်းပြီး", "ငြိမ်သက်ပြီး", "ကောင်းစွာ ငြိမ်သက်ပြီး",
          DEFV := F.DEF["atthaṅgat"].removesuffix("သော"), F.DEF["abbhatthaṅgat"].removesuffix("သော"),
          "ချုပ်ငြိမ်းစေပြီး", "အပြီးတိုင် ချုပ်ငြိမ်းစေပြီး", "ခြောက်ခန်းစေပြီး", "လုံးဝ ခြောက်ခန်းစေပြီး", "အဆုံးသတ်ပြီး"]
assert len(set(VINITA)) == 12 and DEFV == "ကွယ်ပျောက်ပြီး"
SAMV = new("abhiññāya sambodhāya nibbānāya saṃvattati",
           f"{P1.ABHINNA}{C} ကောင်းစွာ သိမြင်ခြင်း{C} နိဗ္ဗာန်အတွက် ဖြစ်၏")
NISSITA = new("vivekanissitaṃ virāganissitaṃ nirodhanissitaṃ vossaggapariṇāmiṃ",
              "ကင်းဆိတ်ခြင်းကို မှီသော၊ ပြယ်ပျောက်ခြင်းကို မှီသော၊ ချုပ်ငြိမ်းခြင်းကို မှီသော၊ စွန့်လွှတ်ခြင်းသို့ ညွတ်သော")
ACC = {}                                                  # accusative objects of «bhāveti» (bojjhaṅga / path factors)
for _k, _v in BOJ.items():
    ACC[_v[:-1] + "aṃ"] = NAME[_v]
for _k in PATH8:
    ACC[{"sammādiṭṭhi": "sammādiṭṭhiṃ", "sammāsati": "sammāsatiṃ", "sammāsamādhi": "sammāsamādhiṃ",
         "sammāvācā": "sammāvācaṃ"}.get(_k, _k[:-1] + "aṃ")] = NAME[_k]
SAMP_DAT = {"sammādiṭṭhiyā": NAME["sammādiṭṭhi"], "sammāsaṅkappena": NAME["sammāsaṅkappo"],
            "sammāvāyāmena": NAME["sammāvāyāmo"], "sammāsatiyā": NAME["sammāsati"],
            "sammāsamādhinā": NAME["sammāsamādhi"], "aṭṭhaṅgikena maggena": NAME["aṭṭhaṅgiko maggo"],
            "pañcaṅgikena maggena": NAME["pañcaṅgiko maggo"], "sattahi bojjhaṅgehi": NAME["satta bojjhaṅgā"]}
AVASESA = new("avasesā dhammā", f"ကြွင်းသော {DHP}")
GROUPS = {"Bāvīsatindriyāni": new("Bāvīsatindriyāni", f"{P1.INDRIYA} နှစ်ဆယ့်နှစ်{P1.CL}"),
          "Cattāro satipaṭṭhānā": new("Cattāro satipaṭṭhānā", P1.count_my(SATIPATTHANA, "catu")),
          "Cattāro sammappadhānā": new("Cattāro sammappadhānā", P1.count_my(SAMMAPPADHANA, "catu")),
          "Cattāro iddhipādā": new("Cattāro iddhipādā", P1.count_my(IDDHIPADA, "catu")),
          "Satta bojjhaṅgā": NAME["satta bojjhaṅgā"], "Aṭṭhaṅgiko maggo": NAME["aṭṭhaṅgiko maggo"],
          "Pañcaṅgiko maggo": NAME["pañcaṅgiko maggo"]}
KATI_HEAD = {"bāvīsatīnaṃ indriyānaṃ": GROUPS["Bāvīsatindriyāni"], "catunnaṃ satipaṭṭhānānaṃ": GROUPS["Cattāro satipaṭṭhānā"],
             "catunnaṃ sammappadhānānaṃ": GROUPS["Cattāro sammappadhānā"], "catunnaṃ iddhipādānaṃ": GROUPS["Cattāro iddhipādā"],
             "sattannaṃ bojjhaṅgānaṃ": NAME["satta bojjhaṅgā"], "aṭṭhannaṃ maggaṅgānaṃ": NAME["aṭṭha maggaṅgā"]}

PH = {}               # Pāli phrase -> Burmese (whole clauses)


def ph(d, log=True):
    for k, v in d.items():
        if k in PH and PH[k] != v:
            raise SystemExit("phrase conflict " + k)
        PH[k] = new(k, v) if log else v


ph(SP_P, False)
ph({"chandaṃ janeti vāyamati vīriyaṃ ārabhati cittaṃ paggaṇhāti padahati": SP_V}, False)
ph(JHANAS, False)
ph({k: v for k, v in ROOTS.items()}, False)
ph({
    "Iti imesaṃ": "ဤသို့ ဤ", "Idha bhikkhu": IDHA, "idha bhikkhu": IDHA, "So": SO, "Evaṃ bhikkhu": "ဤသို့ ရဟန်းသည်",
    "Kathañca bhikkhu": "", "pajānāti": PAJANATI, "tañca pajānāti": "ကိုလည်း " + PAJANATI,
    "seyyathidaṃ": "ဆိုလိုသည်မှာ", "Ariyo aṭṭhaṅgiko maggo": ARIYA_MAGGA,
    "kāyaṃ uddhaṃ pādatalā adho kesamatthakā tacapariyantaṃ pūraṃ nānappakārassa asucino paccavekkhati":
        "ကိုယ်ကို ခြေဖဝါးမှ အထက်၊ ဆံပင်ဖျားမှ အောက်၊ အရေဖြင့် ဝန်းရံထားသော၊ အမျိုးမျိုးသော မစင်ကြယ်သည့်အရာတို့ဖြင့် "
        "ပြည့်နေသည်ဟု ဆင်ခြင်၏",
    "taṃ nimittaṃ āsevati bhāveti bahulīkaroti svāvatthitaṃ vavatthapeti":
        f"{NIMITTA}ကို " + f"{C} ".join(a + "၏" for a in ASEV),
    "taṃ nimittaṃ āsevitvā bhāvetvā bahulīkaritvā svāvatthitaṃ vavatthapetvā":
        f"{NIMITTA}ကို " + f"{C} ".join(a + "၍" for a in ASEV),
    "cittaṃ upasaṃharati": "စိတ်ကို ညွှတ်ဆောင်၏",
    "Iriyati vattati pāleti yapeti yāpeti carati viharati":
        f"{C} ".join(SYN2[k].removesuffix("ခြင်း") + "၏" for k in ("iriyanā", "vattanā", "pālanā", "yapanā", "yāpanā"))
        + f"{C} ကျင်လည်၏{C} {VIHARATI}",
    "Sveva kāyo loko": f"ထို{CONT['kāya']}ပင် {NAME['loko']} ဖြစ်၏", "Sāyeva vedanā loko": f"ထို{P1.FEEL}ပင် {NAME['loko']} ဖြစ်၏",
    "Taṃyeva cittaṃ loko": f"ထို{P1.MIND}ပင် {NAME['loko']} ဖြစ်၏", "Teva dhammā loko": f"ထို{DHP}ပင် {NAME['loko']} ဖြစ်၏",
    "Pañcapi upādānakkhandhā loko":
        f"{P1.UPA}၏ အာရုံ ဖြစ်သော {P1.count_my(P1.KHANDHA, 'pañca')}လည်း {NAME['loko']} ဖြစ်၏",
    "Iti ayañca abhijjhā idañca domanassaṃ imamhi loke vinītā honti paṭivinītā santā samitā vūpasantā atthaṅgatā "
    "abbhatthaṅgatā appitā byappitā sositā visositā byantīkatā":
        f"ဤသို့ ဤ {NAME['abhijjhā']}လည်း၊ ဤ{NAME['domanassaṃ']}လည်း ဤ{NAME['loko']}၌ " + f"{C} ".join(VINITA) + " ဖြစ်ကြ၏",
    # chanda / vīriya / citta verbs (ch8)
    "Imaṃ chandaṃ janeti sañjaneti uṭṭhapeti samuṭṭhapeti": "ဤဆန္ဒကို ဖြစ်စေ၏၊ ကောင်းစွာ ဖြစ်စေ၏၊ ထပေါ်စေ၏၊ ကောင်းစွာ ထပေါ်စေ၏",
    "nibbatteti abhinibbatteti": "ပေါ်ထွက်စေ၏၊ ထင်ရှားစွာ ပေါ်ထွက်စေ၏",
    "Imaṃ vīriyaṃ ārabhati samārabhati āsevati bhāveti bahulīkaroti":
        f"ဤ{NAME['vīriyaṃ']}ကို စတင်၏၊ ကောင်းစွာ စတင်၏၊ " + f"{C} ".join(a + "၏" for a in ASEV[:3]),
    "Imaṃ cittaṃ paggaṇhāti sampaggaṇhāti upatthambheti paccupatthambheti":
        f"ဤ{P1.MIND}ကို မြှင့်တင်၏၊ ကောင်းစွာ မြှင့်တင်၏၊ ထောက်ပံ့၏၊ အထပ်ထပ် ထောက်ပံ့၏",
    "Yā ṭhiti so asammoso, yo asammoso so bhiyyobhāvo, yo bhiyyobhāvo taṃ vepullaṃ, yaṃ vepullaṃ sā bhāvanā, "
    "yā bhāvanā sā pāripūrī":
        "အကြင် တည်တံ့ခြင်းသည် ထို မပျောက်ပျက်ခြင်း ဖြစ်၏၊ အကြင် မပျောက်ပျက်ခြင်းသည် ထို ပိုမို တိုးပွားခြင်း ဖြစ်၏၊ "
        "အကြင် ပိုမို တိုးပွားခြင်းသည် ထို ပြန့်ပြောခြင်း ဖြစ်၏၊ အကြင် ပြန့်ပြောခြင်းသည် ထို ပွားများခြင်း ဖြစ်၏၊ "
        "အကြင် ပွားများခြင်းသည် ထို ပြည့်စုံခြင်း ဖြစ်၏",
    "Te dhamme āsevati bhāveti bahulīkaroti": f"ထို{DH}တို့ကို " + f"{C} ".join(a + "၏" for a in ASEV[:3]),
    "Tathābhūtassa": "ထိုသို့ ဖြစ်သူ၏", "Tathābhūtasa": "ထိုသို့ ဖြစ်သူ၏",
    "ime ca padhānasaṅkhārā": f"ဤ{NAME['padhānasaṅkhārā']}လည်း",
    "taṃsamuṭṭhānaṃ kāyakammaṃ vacīkammaṃ manokammaṃ":
        f"{ROOTS['taṃsamuṭṭhānaṃ']} {ROOTS['kāyakammaṃ']}{C} {ROOTS['vacīkammaṃ']}{C} {ROOTS['manokammaṃ']}",
    "Tadekajjhaṃ abhisaññahitvā abhisaṅkhipitvā": F.SUMMARY_END, "tadekajjhaṃ abhisaññūhitvā abhisaṅkhipitvā": F.SUMMARY_END,
    "saṅkhyaṃ": "ဟူ၍သာ အမည်", "gacchati": "ရ၏",
    "ce bhikkhu": "", "adhipatiṃ karitvā labhati samādhiṃ": f"ကို အကြီးအမှူး ပြု၍ {SAMADHI}ကို ရ၏",
    "labhati cittassekaggataṃ": f"{P1.NAMES['cittassekaggatā']}ကို ရ၏",
    "Iti": "ဤသို့",
    # bojjhaṅga suttanta (ch10)
    "satimā hoti paramena satinepakkena samannāgato": f"{SATIMA} ဖြစ်၏၊ အမြတ်ဆုံးသော {NAME['sati']}နှင့် ရင့်ကျက်သော "
                                                       f"ဉာဏ်ဖြင့် {UPETO[-1]} ဖြစ်၏",
    "cirakatampi cirabhāsitampi saritā hoti anussaritā":
        f"ကြာမြင့်စွာ ပြုခဲ့သည်ကိုလည်း၊ ကြာမြင့်စွာ ပြောခဲ့သည်ကိုလည်း အောက်မေ့သူ၊ {SYN2['anussati'].removesuffix('ခြင်း')}သူ ဖြစ်၏",
    "So tathā sato viharanto taṃ dhammaṃ paññāya pavicinati pavicarati parivīmaṃsamāpajjati":
        f"{SO} ထိုသို့ {NAME['sati']} ရှိလျက် နေစဉ် ထို{DH}ကို {SYN2['paññā']}ဖြင့် "
        f"{SYN2['pavicayo'].removesuffix('ခြင်း')}၏၊ သေချာစွာ သုံးသပ်၏၊ ပတ်လည် စူးစမ်းဆန်းစစ်ခြင်းသို့ ရောက်၏",
    "Tassa taṃ dhammaṃ paññāya pavicinato pavicarato parivīmaṃsamāpajjato āraddhaṃ hoti vīriyaṃ asallīnaṃ":
        f"ထို{DH}ကို {SYN2['paññā']}ဖြင့် {SYN2['pavicayo'].removesuffix('ခြင်း')}နေ၊ သေချာစွာ သုံးသပ်နေ၊ ပတ်လည် "
        f"စူးစမ်းဆန်းစစ်ခြင်းသို့ ရောက်နေသော ထိုရဟန်း၌ မတွန့်ဆုတ်သော {NAME['vīriyaṃ']}ကို စတင်ပြီး ဖြစ်၏",
    "Āraddhavīriyassa uppajjati pīti nirāmisā":
        f"{NAME['vīriyaṃ']}ကို စတင်ပြီးသူ၌ {AMISA['nirāmis']} {SYN2['pīti']} ဖြစ်ပေါ်၏",
    "Pītimanassa kāyopi passambhati, cittampi passambhati":
        f"{SYN2['pīti']} ရှိသော စိတ် ရှိသူ၏ {CONT['kāya']}လည်း {SYN2['passaddhi'].removesuffix('ခြင်း')}၏၊ "
        f"{P1.MIND}လည်း {SYN2['passaddhi'].removesuffix('ခြင်း')}၏",
    "Passaddhakāyassa sukhino cittaṃ samādhiyati":
        f"{CONT['kāya']} {SYN2['passaddhi'].removesuffix('ခြင်း')}ပြီး {P1.SUKHA}မှု ရှိသူ၏ {P1.MIND}သည် တည်ကြည်၏",
    "So tathā samāhitaṃ cittaṃ sādhukaṃ ajjhupekkhitā hoti":
        f"{SO} ထိုသို့ တည်ကြည်သော {P1.MIND}ကို ကောင်းစွာ {SYN2['ajjhupekkhanā'].removesuffix('ခြင်း')}သူ ဖြစ်၏",
    "kāyikaṃ vīriyaṃ": f"{SYN2['kāyikaṃ sukhaṃ'].split(' ')[0]} {NAME['vīriyaṃ']}",
    "cetasikaṃ vīriyaṃ": f"{P1.CETASIKA_ADJ} {NAME['vīriyaṃ']}",
    "savitakkasavicārā pīti": f"{T['savitakkasavicārā']} {SYN2['pīti']}",
    "avitakkaavicārā pīti": f"{T['avitakkaavicārā']} {SYN2['pīti']}",
    "kāyapassaddhi": P1.NAMES["kāyapassaddhi"], "cittapassaddhi": P1.NAMES["cittapassaddhi"],
    "savitakko savicāro samādhi": f"{J['savitakkaṃ']}{C} {J['savicāraṃ']} {SAMADHI}",
    "avitakko avicāro samādhi": f"{J['avitakkaṃ']}{C} {J['avicāraṃ']} {SAMADHI}",
    "bhāveti": "ကို ပွားများ၏", "Idha ariyasāvako micchāājīvaṃ pahāya sammāājīvena jīvikaṃ kappeti":
        f"ဤသာသနာ၌ အရိယာ တပည့်သည် {H_AJIVA.removesuffix('မှ ')}ကို ပယ်၍ {NAME['sammāājīvo']}ဖြင့် အသက်မွေး၏",
    # the path (ch11)
    "Dukkhe ñāṇaṃ, dukkhasamudaye ñāṇaṃ, dukkhanirodhe ñāṇaṃ, dukkhanirodhagāminiyā paṭipadāya ñāṇaṃ":
        f"{C} ".join(p1(r"^Dukkhe ñāṇaṃ, dukkhasamudaye ñāṇaṃ")[1].split(f"{C} ")[:4]),
    "Nekkhammasaṅkappo, abyāpādasaṅkappo, avihiṃsāsaṅkappo":
        f"ကာမမှ ထွက်မြောက်ခြင်းဆိုင်ရာ {SYN2['saṅkappo']}{C} {P1.NAMES['abyāpādo']}ခြင်းဆိုင်ရာ {SYN2['saṅkappo']}{C} "
        f"ညှဉ်းဆဲလိုစိတ် မရှိခြင်းဆိုင်ရာ {SYN2['saṅkappo']}".replace("ခြင်းခြင်း", "ခြင်း"),
    "Musāvādā veramaṇī, pisuṇāya vācāya veramaṇī, pharusāya vācāya veramaṇī, samphappalāpā veramaṇī":
        f"{C} ".join(x + " " + SYN2["veramaṇī"] for x in ("မုသာ ပြောခြင်းမှ", "ကုန်းချောသော စကားမှ", "ကြမ်းတမ်းသော စကားမှ",
                                                           "အကျိုးမဲ့ ပြောခြင်းမှ")),
    "Pāṇātipātā veramaṇī, adinnādānā veramaṇī, kāmesumicchācārā veramaṇī":
        f"{C} ".join(x + " " + SYN2["veramaṇī"] for x in ("သူ့အသက်ကို သတ်ခြင်းမှ", "မပေးသည်ကို ယူခြင်းမှ",
                                                           "ကာမတို့၌ မှားယွင်းစွာ ကျင့်ခြင်းမှ")),
    "Jīvitindriyaṃ duvidhena": f"{NAME['jīvitindriyaṃ']}ကို {F.VIDHA['duvidhena']} {F.LOOK}",
    "atthi rūpajīvitindriyaṃ": f"{NAME['rūpajīvitindriyaṃ']} {F.HOTI}",
    "atthi arūpajīvitindriyaṃ": f"{NAME['arūpajīvitindriyaṃ']} {F.HOTI}",
    "phassasampayuttaṃ": f"{T['phassasampayuttā']} {DH} {F.COP[False]}",
})
assert PH["Dukkhe ñāṇaṃ, dukkhasamudaye ñāṇaṃ, dukkhanirodhe ñāṇaṃ, dukkhanirodhagāminiyā paṭipadāya ñāṇaṃ"].endswith(
    "ကျင့်စဉ်ကို သိသော ဉာဏ်")
# the four «yathā ca …» clauses of the dhammānupassanā (hindrances: uppāda, pahāna, āyatiṃ anuppāda; bojjhaṅga: bhāvanā)
for _st, _my in NIV.items():
    _g = {"vicikicch": "āya"}.get(_st, "assa")
    for _a, _am in (("anuppann", T["anuppannā"]), ("uppann", T["uppannā"]), ("pahīn", "ပယ်ပြီးသော")):
        for _v, _vm in (("uppādo", "ဖြစ်ပေါ်ခြင်း"), ("pahānaṃ", "ပယ်ခြင်း"), ("āyatiṃ anuppādo", "နောင်အခါ၌ မဖြစ်ပေါ်ခြင်း"),
                        ("bhāvanāya pāripūrī", "ပွားများခြင်းဖြင့် ပြည့်စုံခြင်း")):
            PH[f"yathā ca {_a}{_g} {_st}{_g} {_v} hoti"] = f"{_am} {_my}၏ {_vm} ဖြစ်ပုံ"
    _n = _st + ("ā" if _st == "vicikicch" else "o")
    _acc = _st + "aṃ"
    for _q, _qm in (("vā ajjhattaṃ ", f"{QA['ajjhattaṃ'][:-3]}နေသော "), ("vāssa ", "ထိုသူ၌ ရှိနေသော "), ("vā ", "ရှိနေသော ")):
        PH[f"santaṃ {_q}{_acc}"] = f"{_qm}{_my}ကို{VA}"
        PH[f"Santaṃ {_q}{_acc}"] = f"{_qm}{_my}ကို{VA}"
        PH[f"asantaṃ {_q}{_acc}"] = f"{_qm.replace('ရှိနေသော', 'မရှိနေသော')}{_my}ကို{VA}"
    for _q, _qm in (("atthi me ajjhattaṃ ", "ငါ၏ အတွင်း၌ "), ("atthissa ", "ထိုသူ၌ "), ("atthi ", "")):
        PH[f"{_q}{_n}"] = f"{_qm}{_my} ရှိ၏"
        PH[f"n{_q}{_n}"] = f"{_qm}{_my} မရှိ"
# vedanā and citta contemplation phrases
for _q, _qm in FEELQ.items():
    for _a, _am in [("", "")] + [(k, v + " ") for k, v in AMISA.items()]:
        _np = f"{_am}{_qm} {P1.FEEL}"
        _pa = (_a + "aṃ " if _a else "") + _q + "aṃ vedanaṃ"
        _pv = (_a + "aṃ vā " if _a else "") + _q + "aṃ vedanaṃ"
        PH[_pv + " vedayamāno"] = f"{_np}ကို{VA if _a else ''} ခံစားရလျှင်".replace("ကိုဖြစ်စေ ခံစား", "ကိုဖြစ်စေ ခံစား")
        PH[_pv + " vedayamānaṃ"] = f"{_np}ကို ခံစားနေသူကို{VA if _a else ''}"
        PH[_pv] = f"{_np}ကို{VA if _a else ''}"
        PH[_pa + " vedayāmī"] = f"{_np}ကို ငါ ခံစားရ၏"
        PH[_pa + " vedayatī"] = f"{_np}ကို ခံစား၏"
        PH[(_a + "ā " if _a else "") + _q + "ā vedanā"] = _np
for _k, _v in CQ.items():
    _b = _k[:-1]
    PH[f"{_k} vā cittaṃ"] = f"{_v} {P1.MIND}ကို{VA}"
    PH[f"{_k} vāssa cittaṃ"] = f"ထိုသူ၏ {_v} {P1.MIND}ကို{VA}"
    PH[f"{_k} me citta"] = f"ငါ၏ {P1.MIND}သည် {_v} {P1.MIND} ဖြစ်၏"
    PH[f"{_b}massa citta"] = f"ထိုသူ၏ {P1.MIND}သည် {_v} {P1.MIND} ဖြစ်၏"
    PH[f"{_k} citta"] = f"{_v} {P1.MIND}"

# ===================================================================================== the clause engine (prose)
W = r"[\wāīūṃṅñṭḍṇḷ]"
NW = r"(?![\wāīūṃṅñṭḍṇḷ])"


def esc_alt(keys):
    return "(?:" + "|".join(re.escape(k) for k in sorted(keys, key=len, reverse=True)) + ")"


def cap_alt(keys):
    return "(?:" + "|".join(f"[{k[0].upper()}{k[0]}]" + re.escape(k[1:]) for k in sorted(keys, key=len, reverse=True)) + ")"


def lowf(s):
    return s[0].lower() + s[1:]


def list_items(text):
    """Synonym list (with «…pe…» and variants) -> Burmese «A၊ B… C» (pi-1 items_my form)."""
    toks = re.findall(r"\[[^\]]*\]|…pe…|[^\s\[…]+", text)
    items, i = [], 0
    while i < len(toks):
        t = toks[i]
        if t.startswith("["):
            items[-1][2] = var2(t)
            i += 1
            continue
        if t == "…pe…":
            items[-1][3] = True
            i += 1
            continue
        for k in range(SYN_MAX, 0, -1):
            ws = toks[i:i + k]
            if len(ws) == k and not any(w.startswith("[") or w == "…pe…" for w in ws) and " ".join(ws) in SYN2:
                items.append([" ".join(ws), SYN2[" ".join(ws)], "", False])
                i += k
                break
        else:
            raise Miss("list item: " + t + " in " + text[:80])
    seen = {}
    for p, my, _, _ in items:
        if my in seen and seen[my] != p:
            raise Miss(f"two items share {my}: {seen[my]} / {p}")
        seen[my] = p
    out = ""
    for j, (p, my, v, pe) in enumerate(items):
        out += my + (" " + v if v else "")
        if j < len(items) - 1:
            out += (PE + " ") if pe else (C + " ")
        elif pe:
            out += PE
    return out


LIST_RE = re.compile(r"(?P<rel>[Yy]o|[Yy]ā|[Yy]aṃ)(?P<ts> tasmiṃ samaye)? (?:(?P<h>" + esc_alt(LHEAD) + r") )?")


def r_list(s, pos):
    m = LIST_RE.match(s, pos)
    if not m:
        return None
    end = s.find(" – ", m.end())
    if end < 0:
        end = len(s) - 1 if s.endswith(".") else len(s)
    body = s[m.end():end]
    first = body.split(" ")[0].split("…")[0]
    if not any(k == first or k.startswith(first + " ") for k in SYN2) and first.split("[")[0] not in SYN2:
        return None
    parts = [P1.TASMIM] if m["ts"] else []
    if m["h"]:
        parts.append(LHEAD[m["h"]].rstrip(" "))
        if LHEAD[m["h"]].endswith(" "):
            parts[-1] += " "
    head = " ".join(p for p in parts if not p.endswith(" ")) + (" " if parts and not parts[-1].endswith(" ") else "")
    head = (P1.TASMIM + " " if m["ts"] else "") + (LHEAD[m["h"]] if m["h"] else "")
    return head + list_items(body) + " " + REL, end


def q_out(q):
    """Burmese of a quoted text (without the quote marks)."""
    if q in GL:
        return GL[q]
    if q in NAME:
        return NAME[q]
    return prose(q)


def r_vuccati_q(m):
    pl = m["v"] == "vuccanti"
    return f"ဤသည်{'တို့' if pl else ''}ကို “{nm(m['q'])}”ဟု ခေါ်သည်"


def r_vuccati(m):
    pl = m["v"] == "vuccanti"
    return f"ဤသည်{'တို့' if pl else ''}ကို {nm(m['q'])}ဟု ခေါ်သည်"


def r_tena(m):
    return f"ထို့ကြောင့် “{q_out(m['q'])}”ဟု ဆိုသည်"


def r_katamo(m):
    pl = m["k"] == "katame" or m["n"] in PL_NAMES
    return f"ထိုတို့အနက် {nm(m['n'])} ဟူသည် အဘယ်{'တို့' if pl else ''}နည်း"


def r_katamo_seq(m):
    return "ထိုတို့အနက် " + f"{PE} ".join(nm(x) for x in m["l"].split("…pe… ")) + " ဟူသည် အဘယ်နည်း"


def r_gloss(m):
    return GL[lowf(m["w"])] + TI


def r_gloss_q(m):
    return f"“{GL[lowf(m['w'])]}”{TI}"


def r_quote(m):
    return f"“{q_out(m['q'])}”" + ("ဟု" if m["t"] else "")


def r_katham(m):
    """«Kathañca bhikkhu X?» = «ရဟန်းသည် အဘယ်သို့ X-သနည်း» (finite «…၏» -> question «…သနည်း»)."""
    x = prose(m["x"])
    if not x.endswith("၏"):
        raise Miss("Kathañca: " + m["x"])
    return "ရဟန်းသည် အဘယ်သို့ " + x[:-1].replace("၏" + C, C) + "သနည်း"


def r_contemp(m):
    out = contemp(m["q"], m["loc"])
    if m["v"]:
        out += " " + VIHARATI
    if m["a"]:
        out += f"{C} {ATAPI_CHAIN}"
    return out


def r_lok(m):
    """The pi-1 lokuttara opening (bhikkhu as subject; «suññataṃ», a contemplation inserted before «နေသော အချိန်၌»)."""
    a = (IDHA + " ") if m["idha"] else ""
    x = (contemp(None, m["loc"]) + " ") if m["loc"] else ""
    if m["kind"] == "vip":
        base = VIP_A if m["s"] else VIP_A.removesuffix(SUNNATA + " ") + " "
    else:
        base = LOK_A
    return f"{a}{base}{_JH1}{x}{NOW}"


def r_bodyparts(m):
    out = []
    for t in re.findall(r"\[[^\]]*\]|\S+", m["l"]):
        if t.startswith("["):
            out[-1] += " " + var2(t)
        elif t in BODY32:
            out.append(BODY32[t])
        else:
            raise Miss("body part: " + t)
    loc = "ထိုသူ၏ ကိုယ်" if m["a"] == "atthissa" else "ဤကိုယ်"
    return f"“{loc}၌ " + f"{C} ".join(out) + f" ရှိ၏”ဟု"


def r_avasesa(m):
    o = m["o"]
    obj = SAMP_DAT.get(o) or next((NAME[x] for x in (o, o[:-1] + "o", o + "ṃ") if x in NAME), None)
    if obj is None:
        raise Miss("sampayutta: " + o)
    return f"{AVASESA}သည် {obj}{F.SAMP} {DHP} {F.COP[True]}"


def r_bhavana(m):
    q = (NISSITA + " ") if m["q"] else ""
    return f"{q}{ACC[m['o']]}ကို ပွားများ၏"


def r_yadapi(m):
    x = prose(m["x"])
    return f"{x} ဖြစ်သည့်အရာသည်လည်း {nm(m['b'])} ဖြစ်၍ {SAMV}"


def r_atthi_dh(m):
    return f"{prose(m['x'])} {F.HOTI}"


def r_hoti_group(m):
    n = m["n"]
    v = P1.CU_HOTI["pl" if m["v"] == "honti" else "sg"]
    return f"{P1.TASMIM} {nm(n)} {v}"


def r_iddhipada(m):
    k = m["k"]
    return f"{IDP[k]} {SAMADHI}နှင့် {PS}တို့ဖြင့် {UPETO[-1].removesuffix('သူ')}သော {IDDHIPADA}ကို ပွားများ၏"


def r_iddhi_frag(m):
    return nm(m["k"] + "samādhi")


def r_chanda_ce(m):
    k = {"Chandaṃ": "chanda", "Vīriyaṃ": "vīriya", "Cittaṃ": "citta", "Vīmaṃsaṃ": "vīmaṃsā"}[m["k"]]
    return f"အကယ်၍ ရဟန်းသည် {IDP[k]}"


def r_instr(m):
    parts = [f"ဤ{INSTR[x.split(' ')[-1]]}နှင့်လည်းကောင်း" for x in re.split(r", ", m["l"])]
    return ("ဤသို့ " if m["iti"] else "") + f"{C} ".join(parts)


def r_upeto(m):
    if m["pe"]:
        return f"{UPETO[0]}{PE} {UPETO[-1]} ဖြစ်၏"
    return f"{C} ".join(UPETO) + " ဖြစ်၏"


def r_instr1(m):
    return f"ဤ{INSTR[m['n']]}နှင့်"


def r_dhammesu(m):
    return f"{QA[m['q']]} {P1.DHAMMA_LOC} {SYN2[m['x']]}"


def r_tveva(m):
    return f"“{nm(m['n'])}”"


def r_groups(m):
    return GROUPS[m[0]]


def r_name(m):
    return nm(lowf(m[0])) if lowf(m[0]) in NAME else nm(m[0])


def r_ph(m):
    return PH[m[0]]


def r_var(m):
    return var2(m[0])


def r_upasamharati(m):
    return f"{QA[m['q']]} {LOCMY[LOC[m['loc']]]} စိတ်ကို ညွှတ်ဆောင်၏"


def r_q_kaya(m):
    return QA[m["q"]] + " "


SEP2 = [("…pe…. ", PE + END + " "), ("…pe….", PE + END), ("…pe… ", PE + " "), ("…pe…", PE), ("… ", PE + " "),
        ("…", PE), ("? ", END + " "), ("?", END), ("; ", C + " "), (", ", C + " "), (" – ", " – "), (". ", END + " "),
        (".", END), (" ", " ")]
RULES = []


def build():
    names = cap_alt(NAME)
    loc = "(?P<loc>" + "|".join(LOC) + ")"
    anu = "(?:" + "|".join(ANUPA.values()) + ")"
    rules = [
        (r"(?P<idha>[Ii]dha bhikkhu )?yasmiṃ samaye lokuttaraṃ jhānaṃ bhāveti niyyānikaṃ apacayagāmiṃ diṭṭhigatānaṃ "
         r"pahānāya paṭhamāya bhūmiyā pattiyā vivicceva kāmehi…pe… paṭhamaṃ jhānaṃ upasampajja viharati "
         r"dukkhapaṭipadaṃ dandhābhiññaṃ(?P<s>)(?: " + loc + " " + anu + r")?(?P<kind>)(?=,)", r_lok),
        (r"(?P<idha>)Tasseva lokuttarassa kusalassa jhānassa katattā bhāvitattā vipākaṃ vivicceva kāmehi…pe… paṭhamaṃ "
         r"jhānaṃ upasampajja viharati dukkhapaṭipadaṃ dandhābhiññaṃ(?P<s> suññataṃ)?(?: " + loc + " " + anu
         + r")?(?P<kind>vip|)(?=,)", lambda m: r_lok(_Kind(m, "vip"))),
        (r"(?:yo )?tasmiṃ samaye phasso hoti…pe… avikkhepo hoti", lambda m: PHASSA_AVIK),
        (r"[Ii]me dhammā kusalā", lambda m: P1.IME_KUSALA),
        (r"tasmiṃ samaye (?P<n>satta bojjhaṅgā|aṭṭhaṅgiko maggo|pañcaṅgiko maggo) (?P<v>honti|hoti)", r_hoti_group),
        (r"tasmiṃ samaye(?= )", lambda m: P1.TASMIM),
        (r"(?:[Aa]yaṃ|[Ii]daṃ|[Ii]me) (?P<v>vuccati|vuccanti) \"(?P<q>[^\"]+)\"", r_vuccati_q),
        (r"(?:[Aa]yaṃ|[Ii]daṃ|[Ii]me) (?P<v>vuccati|vuccanti) (?P<q>[^\".…]+?)(?=\.|…|$)", r_vuccati),
        (r"Tena vuccati \"(?P<q>[^\"]+)\"n?ti", r_tena),
        (r"Tattha katamaṃ (?P<l>(?:" + names + r")(?:…pe… (?:" + names + r"))+)(?=\?)", r_katamo_seq),
        (r"[Tt]attha (?P<k>katamo|katamā|katamaṃ|katame) (?P<n>" + names + r")(?=\?| \[)", r_katamo),
        (r"\"(?P<w>" + cap_alt(GL) + r")\"n?ti(?=\.)", r_gloss_q),
        (r"(?P<w>" + cap_alt(GL) + r")n?ti(?=\.|…| …|$)", r_gloss),
        (r"Kathañca bhikkhu (?P<x>[^?]+)(?=\?)", r_katham),
        (r"\"(?P<a>atthi imasmiṃ|atthissa) kāye (?P<l>[^\"]+?) mutta\"nti", r_bodyparts),
        (r"(?P<q>ajjhattaṃ|bahiddhā|ajjhattabahiddhā) (?=kāyaṃ uddhaṃ)", r_q_kaya),
        (r"(?P<q>bahiddhā|ajjhattabahiddhā) " + loc + r" cittaṃ upasaṃharati", r_upasamharati),
        (r"(?:(?P<q>ajjhattaṃ|bahiddhā|ajjhattabahiddhā) )?" + loc + " " + anu + r"(?P<v> viharati)?"
         r"(?P<a> ātāpī sampajāno satimā vineyya loke abhijjhādomanassaṃ)?" + NW, r_contemp),
        (r"\"(?P<q>[^\"]+)\"(?P<t>n?ti)?", r_quote),
        (r"(?P<k>chanda|vīriya|citta|vīmaṃsā)samādhipadhānasaṅkhārasamannāgataṃ iddhipādaṃ bhāveti", r_iddhipada),
        (r"(?P<k>chanda|vīriya|citta|vīmaṃsā)samādhi(?=…)", r_iddhi_frag),
        (r"(?P<k>Chandaṃ|Vīriyaṃ|Cittaṃ|Vīmaṃsaṃ) ce bhikkhu", r_chanda_ce),
        (r"Iti ayañca (?P<n>\S+samādhi)(?=, ime ca)", lambda m: f"ဤသို့ ဤ{nm(m['n'])}လည်း"),
        (r"(?P<n>(?:chanda|vīriya|citta|vīmaṃsā)samādhipadhānasaṅkhāro)tveva", r_tveva),
        (r"(?P<iti>Iti )?(?P<l>(?:imāya|iminā) ca \S+(?:, (?:imāya|iminā) ca \S+)+)(?= upeto hoti)", r_instr),
        (r"(?P<q>ajjhattaṃ|bahiddhā) dhammesu (?P<x>sati|pavicayo|upekkhā)", r_dhammesu),
        (r"(?:Imāya|Iminā) (?P<n>\S+)(?= upeto hoti)", r_instr1),
        (r"upeto hoti(?P<pe>…pe… samannāgato)?(?: samupeto upāgato samupāgato upapanno sampanno samannāgato)?", r_upeto),
        (r"[Aa]vasesā dhammā (?P<o>" + esc_alt(SAMP_DAT) + r") sampayuttā", r_avasesa),
        (r"[Aa]vasesā dhammā (?P<o>\S+?)sampayuttā", r_avasesa),
        (r"(?P<o>" + esc_alt(ACC) + r") bhāveti(?P<q> vivekanissitaṃ virāganissitaṃ nirodhanissitaṃ vossaggapariṇāmiṃ)?",
         r_bhavana),
        (r"Yadapi (?P<x>.+?) tadapi (?P<b>\S+) abhiññāya sambodhāya nibbānāya saṃvattati", r_yadapi),
        (r"Atthi (?P<x>(?:[^,.\[]|\[[^\]]*\])+?)(?=, atthi )", r_atthi_dh),
        (r"atthi (?P<x>(?:[^,.\[]|\[[^\]]*\])+?)(?=\.)", r_atthi_dh),
        (r"Yaṃ cakkhu catunnaṃ mahābhūtānaṃ upādāya pasādo…pe… suñño gāmopeso", lambda m: _CAK["cakkhu"]),
        (r"Yo kāyo catunnaṃ mahābhūtānaṃ upādāya pasādo…pe… suñño gāmopeso", lambda m: _CAK["kāyo"]),
        (esc_alt(PH) + NW, r_ph),
        ("LIST", None),
        (esc_alt(GROUPS) + NW, r_groups),
        (r"(?:" + names + r")(?: (?:" + names + r"))+" + NW, lambda m: f"{C} ".join(r_name(_M(x)) for x in m[0].split(" "))),
        (names + NW, r_name),
        (r"\[[^\]]+\]", r_var),
    ]
    RULES[:] = [(p if p == "LIST" else re.compile(p), f) for p, f in rules]


class _M:
    def __init__(self, x):
        self.x = x

    def __getitem__(self, k):
        return self.x


class _Kind:
    def __init__(self, m, kind):
        self.m, self.kind = m, kind

    def __getitem__(self, k):
        return self.kind if k == "kind" else self.m[k]


def prose(s):
    pos, out = 0, []
    while pos < len(s):
        for p, my in SEP2:
            if s.startswith(p, pos):
                out.append(my)
                pos += len(p)
                break
        else:
            for rx, f in RULES:
                if rx == "LIST":
                    r = r_list(s, pos)
                    if r:
                        out.append(r[0])
                        pos = r[1]
                        break
                    continue
                m = rx.match(s, pos)
                if m and m.end() > pos:
                    r = f(m)
                    if r.startswith("ကို") and not r.startswith("ကိုယ်") and out and out[-1] == " ":
                        out[-1] = ""                       # «… ဖြစ်ပုံကိုလည်း», «ဆန္ဒကို …» (particle joins the noun)
                    out.append(r)
                    pos = m.end()
                    break
            else:
                raise Miss("no frame: " + s[pos:pos + 100])
    out = "".join(out).replace("  ", " ")
    return re.sub(r"(ဖြစ်လျက် နေ၏) (?=\S)", r"\1၊ ", out)     # consecutive «… viharati» clauses


# ===================================================================================== the Pañhāpucchaka (F engine)
NUMW = {"dv": 2, "tīṇ": 3, "cattār": 4, "pañc": 5, "cha ": 6, "satt": 7, "aṭṭh": 8, "nav": 9, "das": 10,
        "ekādas": 11, "dvādas": 12, "teras": 13, "cuddas": 14, "pannaras": 15, "soḷas": 16, "sattaras": 17,
        "aṭṭhāras": 18, "ekavīsat": 21}
NUM_MY = {2: "နှစ်", 3: "သုံး", 4: "လေး", 5: "ငါး", 6: "ခြောက်", 7: "ခုနစ်", 8: "ရှစ်", 9: "ကိုး", 10: "ဆယ်",
          11: "ဆယ့်တစ်", 12: "ဆယ့်နှစ်", 13: "ဆယ့်သုံး", 14: "ဆယ့်လေး", 15: "ဆယ့်ငါး", 16: "ဆယ့်ခြောက်",
          17: "ဆယ့်ခုနစ်", 18: "ဆယ့်ရှစ်", 21: "နှစ်ဆယ့်တစ်", 22: "နှစ်ဆယ့်နှစ်"}
for _k, _v in P1.NUM.items():
    _n = {"eka": 1, "dvi": 2, "ti": 3, "catu": 4, "pañca": 5, "cha": 6, "satta": 7, "aṭṭha": 8, "nava": 9, "dasa": 10}[_k]
    assert _n == 1 or NUM_MY[_n] == _v
for _p, _n in NUMW.items():
    _key = (_p + "indriyā") if not _p.endswith(" ") else "cha indriyā"
    F.KH[_key] = (new(_key, f"{P1.INDRIYA} {NUM_MY[_n]}{P1.CL}"), None, True)
for _k in INDR22:
    F.KH[_k] = (NAME[_k], None, False)
for _k in ("pītisambojjhaṅgo", "dhammavicayasambojjhaṅgo", "sammāsaṅkappo", "sammādiṭṭhi"):
    F.KH[_k] = (NAME[_k], None, False)
for _k in ("cha bojjhaṅgā", "satta maggaṅgā"):
    F.KH[_k] = (NAME[_k], None, True)
for _k, _n in (("vīmaṃsiddhipādo", False), ("cittiddhipādo", False)):
    F.KH[_k] = (NAME[_k], None, _n)
F.KH["tayo iddhipādā"] = (new("tayo iddhipādā", P1.count_my(IDDHIPADA, "ti")), None, True)
F.KH["manindriyaṃ"] = (NAME["manindriyaṃ"], "manindriya", False)
F.NOUN["manindriya"] = dict(my=NAME["manindriyaṃ"], pl=False, forms=set())
F.TERM_IRREG.update({"arūpaṃ": "arūpino", "rūpā": "rūpino", "rūpaṃ": "rūpino"})
for _v in ("sampayutt", "vippayutt", "saṃsaṭṭh", "visaṃsaṭṭh"):
    F.TERM_IRREG["cittena " + _v + "aṃ"] = F.TERM_IRREG["cittena " + _v + "o"]          # neuter subject (indriyaṃ)
_term_my0 = F.term_my


def term_my2(p):
    p = re.sub(r"ñc[aā]$", "ṃ cā", p)                      # «…sampayuttañcā» = «…sampayuttaṃ cā»
    p = re.sub(r"ñceva (?=n[oa] ca )", "ṃ ceva ", p)        # «…sampayuttañceva no ca X»
    try:
        return _term_my0(p)
    except Miss:
        m = re.fullmatch(r"na (?P<x>.+)", p)
        if not m:
            raise
        k = "na " + F.term_key(m["x"])
        if k not in T:
            T[k] = new(k, P1.no_(T[F.term_key(m["x"])]))      # free «na» before a term (pi-1 no_())
        return T[k]


F.term_my = term_my2


def r_kati_head2(m):
    F.STATE["pl"] = True
    return KATI_HEAD[lowf(m["h"])] + "တို့အနက်"


def r_yeva(m):
    return f"{F.term_my(m['t'])} {F._dh()}သာ {F.COP[F.STATE.get('pl', False)]}"


def r_siya_ns(m):
    return f"{F.SIYA} {F.term_my(m['t'])} {F._dh()} {F.COP[F.STATE.get('pl', False)]}{C}"


def r_nv_dash(m):
    F.STATE["nv"] = True
    return (F.SIYA + " " if m["s"] else "") + "– "


def r_nv_bare(m):
    """«[siyā] na vattabbā A-tipi, B-tipi» (no quotes, no dash): «A သဘောတရားဟုလည်းကောင်း၊ … ခေါ်ဆို၍ မရ»; an item
    without «ti» is a statement («၊ B သဘောတရား ဖြစ်သည်»)."""
    parts = []
    for it in m["l"].split(", "):
        if it.endswith("tipi"):
            parts.append((it[:-4], F.TIPI))
        elif it.endswith("ti"):
            parts.append((it[:-2], F.TI))
        else:
            parts.append((it, None))
    out = (F.SIYA + " ") if m["s"] else ""
    first = True
    for i, (x, w) in enumerate(parts):
        if w is None:
            if first:
                raise Miss("na vattabbā: " + m[0])
            out += f"{C} {F.term_my(x)} {F._dh()} {F.COP[F.STATE.get('pl', False)]}"
            continue
        if not first and parts[i - 1][1] is not None:
            out += f"{C} "
        out += f"{F.term_my(x)} {F._dh()}{w}"
        first = False
        if i == len(parts) - 1 or parts[i + 1][1] is None:
            if m["nv"] is not None:
                out += " " + F.NVATT
    return out


def r_quotes_only(m):
    """Source slip (^2-484 block, ch10 line 74): «Āsavā ceva … cātipi, … āsavātipi.» without «na vattabbā»."""
    return r_nv_bare(_Kind2(m))


class _Kind2:
    def __init__(self, m):
        self.m = m

    def __getitem__(self, k):
        return {"s": None, "nv": None, "l": self.m["l"]}.get(k) if k in ("s", "nv", "l") else self.m[k]


F.EXTRA_RULES[:] = [
    (r"(?P<h>" + cap_alt(KATI_HEAD) + r")(?= kati)", r_kati_head2),
    (r"(?P<t>" + W + r"+?)yeva(?=\.)", r_yeva),
    (r"(?P<s>siyā )?na vattabb(?:o|ā|aṃ) – ", r_nv_dash),
    (r"(?P<s>siyā )?(?P<nv>na vattabb(?:o|ā|aṃ)) (?P<l>[^\"–.;]+?)(?=\.|;|$)", r_nv_bare),
    (r"(?P<l>āsavā ceva āsavasampayuttā cātipi, āsavasampayuttā ceva no ca āsavātipi)(?=\.)", r_quotes_only),
    (r"siyā (?P<t>(?!atthi |siyā )" + W + r"+)(?= siyā )", r_siya_ns),
    (r"anāsavā āsavavippayuttā(?=\.)",                    # source slip (ch10 ^2-485 block): two terms, one sentence
     lambda m: f"{T['anāsavā']}{C} {T['āsavavippayuttā']} {DHP} {F.COP[True]}"),
    (r"phassasampayuttaṃ(?=\.)", lambda m: f"{T['phassasampayuttā']} {DH} {F.COP[False]}"),
    (r"(?:[Aa]yaṃ|[Ii]daṃ) vuccati \"(?P<q>[^\"]+)\"", lambda m: r_vuccati_q(_Kind3(m))),
]


class _Kind3:
    def __init__(self, m):
        self.m = m

    def __getitem__(self, k):
        return "vuccati" if k == "v" else self.m[k]


F.EXTRA_RULES[:] = [(re.compile(p), f) for p, f in F.EXTRA_RULES]
F.rebuild()
F.RULES[:] = list(F.EXTRA_RULES) + [r for r in F.RULES if r not in F.EXTRA_RULES]
SLIPS = {   # source slips, corrected only where the engine needs the standard form (logged in the notes)
    '"mahaggatārammaṇa"nti pi': '"mahaggatārammaṇa"ntipi',
    '"gantho ceva ganthasampayutta"ñcāti': '"gantho ceva ganthasampayuttañcā"ti',
    "sāsavācātipi": "sāsavā cātipi", "āsavasampayuttācātipi": "āsavasampayuttā cātipi",
}
GROUP_START = re.compile(r"^(?:Bāvīsatindriyāni|Cattāro|Satta bojjhaṅgā|Ariyo|Aṭṭhaṅgiko|Pañcaṅgiko) ")


def pan_line(body):
    out = []
    for s in re.split(r"(?<=\.) (?=\S)", body):
        F.STATE["pl"] = True
        F.STATE.pop("nv", None)
        out.append(F.clauses_my(lowf(s)))
    return " ".join(out)


def line_my(body):
    for a, b in SLIPS.items():
        body = body.replace(a, b)
    body = body.replace(" …pe…", "…pe…").replace("kāmehi …pe…", "kāmehi…pe…")
    if body.startswith("#") or (body.endswith(".") and body[:-1] in F.COLO):
        return F.line_my(body)
    part = F.STATE.get("part")
    if part == "pan" and not GROUP_START.match(body):
        return pan_line(body)
    if re.match(r"^(?:Tattha katamaṃ manindriyaṃ\?|\S+vidhena manindriyaṃ)", body):
        F.STATE.pop("pl", None)
        return F.clauses_my(body)
    return prose(body)


def translate_line(line):
    if not line.strip():
        return ""
    m = ID_RE.search(line)
    body = line[:m.start()] if m else line
    my = line_my(body)
    if body.rstrip().endswith('"ti') and my.endswith(END):
        pass
    return my + (" " + m.group(1) if m else "")


def write(name, txt):
    txt = unicodedata.normalize("NFC", txt)
    (OUT / name).write_text(txt, encoding="utf-8")
    print(f"wrote {name}: {sum(1 for l in txt.splitlines() if l)} lines")


def chapter(name):
    lines = (PALI / name).read_text(encoding="utf-8-sig").splitlines()
    F.STATE.clear()
    done = []
    for i, line in enumerate(lines):
        try:
            done.append(translate_line(line))
        except Miss as e:
            print(f"STOP {name} line {i + 1}: {e}\n  {line[:200]}")
            return False
    write(name, "\n".join(done).rstrip("\n") + "\n")
    return True


def write_new_strings():
    txt = NOTES.read_text(encoding="utf-8") if NOTES.exists() else ""
    head = txt.split("\n## New strings")[0].rstrip("\n")
    lines = ["", "## New strings («Pāli = Burmese»; generated by make_ch5-7-11.py)", ""]
    lines += [f"{p} = {m}" for p, m in NEWLOG.items()]
    NOTES.write_text(unicodedata.normalize("NFC", head + "\n" + "\n".join(lines) + "\n"), encoding="utf-8")
    print(f"notes: {len(NEWLOG)} new strings")


build()

if __name__ == "__main__":
    names = [a for a in sys.argv[1:] if not a.startswith("--")] or CHAPTERS
    OUT.mkdir(parents=True, exist_ok=True)
    ok = all([chapter(n) for n in names])
    write_new_strings()
    sys.exit(0 if ok else 1)
