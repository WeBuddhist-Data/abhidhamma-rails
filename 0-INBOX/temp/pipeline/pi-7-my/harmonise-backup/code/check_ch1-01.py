"""Per-line check of the Burmese pi-7 1-01-kusalattika against the Pāli (independent of the generator's frames).

usage: python3 -I -X utf8 check_ch1-01.py [--out DIR] [chapter ...]   (default: 1-01-kusalattika.md)
       python3 -I -X utf8 check_ch1-01.py --mutate                   (planted errors must be caught)
       python3 -I -X utf8 check_ch1-01.py --pe                       (check_text with a folded Pāli copy in
                                                                      pi-7-my/chk-pe/ch1-01/, deleted afterwards)
Adapted from check_sample.py. Checks, line by line (Pāli line i <-> Burmese line i):
  S  structure: equal non-empty lines, heading #-level, block IDs, no «?» «।» «:-», no Latin left outside variants;
  P  polarity: «မဟုတ်» count and the «မ…» negatives expected from the Pāli tokens (tables NEG_*);
  C  conditions: the sequence of conditions (stem + polarity) named in the Pāli (also in the notes: «-sadisaṃ»,
     «-mūlake», «-mpi», «sa-X» / «a-X», bare names in brackets …) = the sequence of «Nဟူသော အကြောင်း» (and the bare
     names of the ghaṭanā lists) in the Burmese;
  O  term order: the sequence of triad terms in the Pāli = the sequence in the Burmese (conditioning first);
  N  numbers: counts «… ခု» (also above ten), khandha / mahābhūta numbers «… ပါး», group numbers «… မျိုးတွဲ»,
     digits «(n)»;
  I  identity: identical Pāli sentences have identical Burmese, within this chapter AND with the approved sample;
  T  tables: the condition names, terms, counts of my7_formulas / make_ch1-01 equal this checker's own copy;
  R  reuse: every value taken from pi-1 … pi-6 (WITNESS, module + this chapter) is re-read from the FINAL rails and
     found in every line whose Pāli contains its Pāli; sentences that occur in pi-1 … pi-6 are identical.
Prints the mismatches and a summary; exit 1 on any mismatch.
"""
import importlib.util
import pathlib
import re
import shutil
import subprocess
import sys

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
ROOT = HERE.parents[3]
PALI = ROOT / "AI_translation/pali/pi-7_split_chapters"
OUT = ROOT / "AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters"
SAMPLE = ["1-00-paccaya.md", "1-02-vedanattika.md"]
_args = sys.argv[1:]
if "--out" in _args:
    OUT = pathlib.Path(_args[_args.index("--out") + 1])
    del _args[_args.index("--out"):_args.index("--out") + 2]
MODE = None
for _m in ("--mutate", "--pe"):
    if _m in _args:
        MODE = _m
        _args.remove(_m)
NAMES = _args or ["1-01-kusalattika.md"]
ID = re.compile(r"\s*(\^[0-9A-Za-z-]+)\s*$")
W_ = r"[\wāīūṃṅñṭḍṇḷ]"

# ----------------------------------------------------------------------------- this checker's own tables
CONDS_MY = {"hetu": "အမြစ်", "ārammaṇa": "အာရုံ", "adhipati": "အကြီးအမှူး", "anantara": "ချက်ချင်း နောက်၌ ဖြစ်စေခြင်း",
            "samanantara": "ကောင်းစွာ ချက်ချင်း နောက်၌ ဖြစ်စေခြင်း", "sahajāta": "အတူ ပေါ်ပေါက်ခြင်း",
            "aññamañña": "အချင်းချင်း ထောက်ပံ့ခြင်း", "nissaya": "အမှီ", "upanissaya": "အားကြီးသော အမှီ",
            "purejāta": "ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်း", "pacchājāta": "နောက်မှ ဖြစ်ပေါ်ခြင်း",
            "āsevana": "အလေ့အကျင့် ပြုခြင်း", "kamma": "ကံ", "vipāka": "ကံ၏ အကျိုး", "āhāra": "အာဟာရ",
            "indriya": "စွမ်းရည်", "jhāna": "ဈာန်", "magga": "မဂ်", "sampayutta": "ယှဉ်တွဲခြင်း",
            "vippayutta": "ကင်းကွာခြင်း", "atthi": "ရှိခြင်း", "natthi": "မရှိခြင်း", "vigata": "ပျောက်ကွယ်ခြင်း",
            "avigata": "မပျောက်ကွယ်ခြင်း"}
STEMS = sorted(CONDS_MY, key=len, reverse=True)
ABY = "ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော"
TERMS_MY = {"kiriyābyākat": "ပြုရုံမျှသာ ဖြစ်သော " + ABY, "abyākat": ABY, "akusal": "အကုသိုလ်", "kusal": "ကုသိုလ်"}
NUM_MY = {1: "တစ်", 2: "နှစ်", 3: "သုံး", 4: "လေး", 5: "ငါး", 6: "ခြောက်", 7: "ခုနစ်", 8: "ရှစ်", 9: "ကိုး", 10: "ဆယ်",
          11: "ဆယ့်တစ်", 12: "ဆယ့်နှစ်", 13: "ဆယ့်သုံး", 14: "ဆယ့်လေး", 15: "ဆယ့်ငါး", 16: "ဆယ့်ခြောက်",
          17: "ဆယ့်ခုနစ်", 18: "ဆယ့်ရှစ်", 20: "နှစ်ဆယ်", 21: "နှစ်ဆယ့်တစ်", 22: "နှစ်ဆယ့်နှစ်", 23: "နှစ်ဆယ့်သုံး",
          24: "နှစ်ဆယ့်လေး"}
MY_NUM = {v: k for k, v in NUM_MY.items()}
COUNT_PI = {"ekaṃ": 1, "dve": 2, "tīṇi": 3, "cattāri": 4, "pañca": 5, "cha": 6, "satta": 7, "aṭṭha": 8, "nava": 9,
            "dasa": 10, "ekādasa": 11, "dvādasa": 12, "terasa": 13, "cuddasa": 14, "pannarasa": 15, "soḷasa": 16,
            "sattarasa": 17, "aṭṭhārasa": 18}
CNT_ALT = "|".join(sorted(COUNT_PI, key=len, reverse=True))
KH_PI = {"eko": 1, "ekaṃ": 1, "ekassa": 1, "dve": 2, "dvinnaṃ": 2, "tayo": 3, "tiṇṇannaṃ": 3, "tiṇṇaṃ": 3,
         "cattāro": 4}
GROUP_PI = {"catukk": 4, "pañcak": 5, "chakk": 6, "sattak": 7, "aṭṭhak": 8, "navak": 9, "dasak": 10,
            "ekādasak": 11, "dvādasak": 12, "terasak": 13, "cuddasak": 14, "pannarasak": 15, "soḷasak": 16,
            "sattarasak": 17, "aṭṭhārasak": 18, "vīsak": 20, "ekavīsak": 21, "bāvīsak": 22, "tevīsak": 23,
            "catuvīsak": 24}
MULA_PI = {"ekamūlak": 1, "dumūlak": 2, "timūlak": 3, "catumūlak": 4, "pañcamūlak": 5, "tevīsatimūlak": 23}
# extra numbers of the editorial notes (Pāli regex -> value, for the counts list)
EXTRA_CNT = [(r"(?<![\wāīūṃṅñṭḍṇḷ])tīṇeva pañhā", 3), (r"(?:imāni|padesu) tīṇi", 3), (r"eko pañho", 1),
             (r"pañca pañhā", None), (r", sattarasa\.\)", 17)]
# notes / headings in which the Pāli names conditions without a pattern of this checker: Pāli -> [(stem, neg)]
NOTE_CONDS = {"(adhipatiyā paṭisandhi natthi)": [("adhipati", False)],
              "(nādhipati paripuṇṇaṃ paṭisandhikaṃ)": [("adhipati", True)],
              "(adhipati paṭisandhikkhaṇe natthi.)": [("adhipati", False)],
              "yāvāsevanā": [("āsevana", False)]}
HEAD_OVERRIDE = {"Sahajāta-chandādhipatighaṭanā (6)": [], "Sahajātachandādhipatighaṭanā (6)": [],
                 "Naadhipatyādi": [("adhipati", True)]}
# negation: Pāli token regex -> number of «မဟုတ်» / number of «မ…» negatives expected in the Burmese
NEG_SANDHI = "|".join(x[:-1] for x in STEMS if x.endswith("a"))
_LOCS = ["hetuyā", "adhipatiyā", "atthiyā", "natthiyā"] + [x[:-1] + "e" for x in STEMS
                                                         if x not in ("hetu", "adhipati", "atthi", "natthi")]
NEG_NOT = [(r"(?i)(?<![\wāīūṃṅñṭḍṇḷ])(?:na|no)(?:" + "|".join(sorted(STEMS + _LOCS, key=len, reverse=True)) + "|(?:"
            + NEG_SANDHI + r")(?=ādi))", 1),
           (r"(?i)(?<![\wāīūṃṅñṭḍṇḷ])naadhipatyādi", 1),
           (r"(?<=samanantara)nasahajāta|(?<=vipāka)naāhāra", 1),      # source slips: missing hyphens (logged)
           (r"(?<![\wāīūṃṅñṭḍṇḷ])na (?=§C§|\w+paccayena paccayo)", 1),
           (r"(?i)(?<!kiriy)ābyākat|(?<![\wāīūṃṅñṭḍṇḷ])[Aa]byākat", 2),
           (r"(?i)(?<![\wāīūṃṅñṭḍṇḷ])arūp(?:ino|īnaṃ)", 1), (r"(?i)kiriyābyākat", 2),
           (r"(?i)nevasaññānāsaññāyatan", 2), (r"(?i)anattato", 1), (r"nādhipati", 1)]
NEG_MA = [(r"(?i)adukkhamasukh", 2), (r"(?i)natthi", 1), (r"(?i)natthīti", 1), (r"(?i)avigat", 1), (r"(?i)ahetuk", 1), (r"(?i)aniccato", 1),
          (r"asammuyhantena", 1), (r"na labbhati", 1), (r"na kātabbaṃ", 1),
          (r"(?<![\wāīūṃṅñṭḍṇḷ])arūpe(?![\wāīūṃṅñṭḍṇḷ])", 1), (r"(?i)ākāsānañcāyatan", 1), (r"(?i)viññāṇañcāyatan", 1),
          (r"(?i)ākiñcaññāyatan", 1), (r"(?i)nevasaññānāsaññāyatan", 1), (r"(?i)anuppann", 1),
          (r"(?i)\(avipāk", 1), (r"(?i)alikhit", 1), (r"(?i)ṭhānāṭhān", 1), (r"(?i)adinn", 1)]
MA_MY = re.compile(r"မ(?:နာကျင်|သာယာ|ရှိ|ပျောက်ကွယ်|မြဲ|ရောထွေး|တွေ့ရ|ထည့်ရ|ဖြစ်ပေါ်သေး|ပါဝင်|ရေး|ဖြစ်နိုင်|ပေး)")


def nonempty(p):
    return [l for l in p.read_text(encoding="utf-8-sig").splitlines() if l.strip()]


def strip_var(s):
    return re.sub(r"\{[^{}]*\}", "", s)


def paren_spans(s):
    spans, depth, start = [], 0, 0
    for i, ch in enumerate(s):
        if ch == "(":
            if depth == 0:
                start = i
            depth += 1
        elif ch == ")" and depth:
            depth -= 1
            if depth == 0:
                spans.append((start, i))
    if depth:
        spans.append((start, len(s)))
    if not spans and s.rstrip().endswith(")"):           # a note that opened on an earlier unit of the line
        spans.append((0, len(s)))
    return spans


# ----------------------------------------------------------------------------- C: conditions
SEG_ALL = sorted(STEMS, key=len, reverse=True)


def seg(comp):
    out = []
    comp = re.sub(r"(?i)(ārammaṇ|anantar)ūpanissaya", lambda m: m.group(1) + "a-upanissaya", comp)
    for part in comp.replace(" -", "-").replace("- ", "-").split("-"):
        p = part.lower()
        if p.endswith("ṃ") and p[:-1] in CONDS_MY:
            p = p[:-1]
        if p.endswith(("adhipat", "ādhipat", "atth")):
            p += "i"
        while p:
            for st in SEG_ALL:
                for cand in ([st, st[:-1] + "ā"] if st.endswith(("a", "u")) else [st]):
                    if p.startswith(cand):
                        out.append(st)
                        p = p[len(cand):]
                        if cand != st:
                            p = "a" + p
                        break
                else:
                    continue
                break
            else:
                raise ValueError("seg: " + part)
    return out


BARE_PI = {}
for _st in STEMS:
    BARE_PI[_st + "ṃ"] = _st
    BARE_PI[_st + "mpi"] = _st
    BARE_PI[_st[:-1] + "e" if _st.endswith("a") else _st + "mhi"] = _st
LOC_PI = {"hetuyā": "hetu", "adhipatiyā": "adhipati", "atthiyā": "atthi", "natthiyā": "natthi"}
LOC_PI.update({x[:-1] + "e": x for x in STEMS if x not in LOC_PI})


PALI_SLIPS = [(r"(?<![\wāīūṃṅñṭḍṇḷ])([Nn][ao])[ -](?=(?:" + "|".join(sorted(STEMS + _LOCS, key=len, reverse=True))
               + r")(?!\w*paccayena))", r"\1"),                                                # «na X», «na-X»
              (r"Nadhipati", "Naadhipati"), (r"naṃindriye", "naindriye"), (r"(?<= )sattaṃ(?=,)", "satta"),
              (r"adhipati paccayena", "adhipatipaccayena"), (r"Avigata āhāra-", "Avigata-āhāra-"),
              (r"naaññamañña-paccayā", "naaññamaññapaccayā")]


def pali_norm(s):
    for rx, rep_ in PALI_SLIPS:
        s = re.sub(rx, rep_, s)
    return s


def pali_conds(line):
    s = pali_norm(strip_var(ID.sub("", line)))
    found = {}
    head = s.startswith("#")
    htext = re.sub(r"^#+ \*?|\*?$", "", s).strip()

    def add(pos, st, ng):
        found.setdefault(round(pos, 3), (st, ng))
    if head and htext in HEAD_OVERRIDE:
        return list(HEAD_OVERRIDE[htext])
    sl = s.lower()
    for k, v in NOTE_CONDS.items():
        i = sl.find(k.lower())
        while i >= 0:
            for j, (st, ng) in enumerate(v):
                add(i + j / 10, st, ng)
            i = sl.find(k.lower(), i + 1)
    stems = "|".join(STEMS)
    for m in re.finditer(r"(?i)(?<!" + W_ + r")(na|no)?(" + stems + r")paccay", s):
        add(m.start(), m.group(2).lower(), bool(m.group(1)))
    for m in re.finditer(r"(?i)(?<!" + W_ + r")(na|no)?(" + "|".join(sorted(LOC_PI, key=len, reverse=True))
                         + r") (?:" + CNT_ALT + r")(?!" + W_ + ")", s):
        add(m.start(), LOC_PI[m.group(2).lower()], bool(m.group(1)))
    sandhi = "|".join(x[:-1] if x.endswith("a") else x for x in STEMS)
    look = r"(?=ādi|sabhāg|mūlak|ghaṭan|duk|tik|sāmañña|missak|pakiṇṇak|yādi" + ("|-" if head else "") + ")"
    lb = r"(?<![\wāīūṃṅñṭḍṇḷ])" if head else r"(?<![\wāīūṃṅñṭḍṇḷ-])"
    for m in re.finditer(r"(?i)" + lb + r"(na|no)?(" + sandhi + r")a?" + look, s):
        stem = next(x for x in STEMS if x == m.group(2).lower() or x[:-1] == m.group(2).lower())
        if any(abs(f - m.start()) < 1 for f in found):
            continue
        add(m.start(), stem, bool(m.group(1)))
    # sa-X / a-X (headings and «(Savipākaṃ – 5)»), sa-X-Y ghaṭanā headings
    for m in re.finditer(r"(?i)\((s|)(a|ā)(vipāk|sevan|hār|indriy|upanissay|kamm)aṃ", s):
        st = {"vipāk": "vipāka", "sevan": "āsevana", "hār": "āhāra", "indriy": "indriya", "upanissay": "upanissaya",
              "kamm": "kamma"}[m.group(3).lower()]
        add(m.start(), st, False)
    if head:
        m = re.match(r"S(a|ā)([\wāīūṃṅñṭḍṇḷ-]+?)ghaṭanā", htext)
        if m:
            for cand in ([m.group(2)] if m.group(1) == "a" else ["ā" + m.group(2), "a" + m.group(2)]):
                try:
                    sts = seg(cand.replace("hetādhipati", "hetu-adhipati"))
                except ValueError:
                    continue
                found = {k: v for k, v in found.items() if not (m.start() <= k < m.end() + 10)}
                for j, st in enumerate(sts):
                    add(m.start() + j / 100, st, False)
                break
    # bare condition words inside editorial brackets («(Navipākaṃ namaggaṃ …)», «(Vipākamūlake āsevanaṃ natthi)»)
    for a, b in paren_spans(s):
        for m in re.finditer(r"(?<![\wāīūṃṅñṭḍṇḷ])(na|no)?([\wāīūṃṅñṭḍṇḷ]+)", sl[a:b + 1]):
            w = m.group(2)
            pos = a + m.start()
            if w in BARE_PI and w not in COUNT_PI:
                nxt = s[a + m.end():a + m.end() + 12]
                if re.match(r" (?:" + CNT_ALT + r")(?!" + W_ + ")", nxt):
                    continue
                add(pos, BARE_PI[w], bool(m.group(1)))
            elif w in LOC_PI and re.match(r" ṭhitena", sl[a + m.end():]):
                add(pos, LOC_PI[w], bool(m.group(1)))
    # «nonatthiyā ca, novigate ca» / «nahetuyā ṭhitena» outside brackets
    for m in re.finditer(r"(?<![\wāīūṃṅñṭḍṇḷ])(na|no)?(" + "|".join(sorted(LOC_PI, key=len, reverse=True))
                         + r")(?= ca\b| ṭhitena)", sl):
        add(m.start(), LOC_PI[m.group(2)], bool(m.group(1)))
    # ghaṭanā compounds «A-B-…nti N» and the hyphenated negated compound
    for m in re.finditer(r"(?i)(?<!" + W_ + r")((?:[\wāīūṃṅñṭḍṇḷ]+ ?- ?)+[\wāīūṃṅñṭḍṇḷ]+?)(?:nti|īti) (?:(?:"
                         + CNT_ALT + r")(?!" + W_ + ")|(?=na|no))", s):
        for k, st in enumerate(seg(m.group(1))):
            add(m.start() + k / 100, st, False)
    for m in re.finditer(r"(?i)((?:n[ao][\wāīūṃṅñṭḍṇḷ]+-)+)(?=n[ao][\wāīūṃṅñṭḍṇḷ]+paccayā)", s):
        k = 0
        found = {f: v for f, v in found.items() if not (m.start() <= f < m.end())}
        for part in m.group(1).strip("-").split("-"):
            p = part.lower()
            while p:
                pre, p = p[:2], p[2:]
                st = next(x for x in STEMS if p.startswith(x))
                add(m.start() + k / 100, st, True)
                p = p[len(st):]
                k += 1
    return [found[k] for k in sorted(found)]


NAME_ALT = "|".join(re.escape(CONDS_MY[s]) for s in sorted(CONDS_MY, key=lambda x: len(CONDS_MY[x]), reverse=True))
MY_NAME = {v: k for k, v in CONDS_MY.items()}
GH_MY = re.compile(r"((?:(?:" + NAME_ALT + r")၊ )*(?:" + NAME_ALT + r")) ဟူသော ပေါင်းစပ်ချက်")


def my_conds(line):
    s = strip_var(ID.sub("", line))
    found = []
    for m in re.finditer(r"(?<![^\s(“*])(" + NAME_ALT + r")ဟူသော အကြောင်း((?:ကြောင့်)? မဟုတ်)?", s):
        found.append((m.start(), MY_NAME[m.group(1)], bool(m.group(2))))
    for m in GH_MY.finditer(s):
        for k, nm in enumerate(m.group(1).split("၊ ")):
            found.append((m.start() + k / 100, MY_NAME[nm], False))
    for m in re.finditer(r"\((" + NAME_ALT + r")နှင့် တူသည်\)", s):             # «(anantarasadisaṃ)»
        found.append((m.start(), MY_NAME[m.group(1)], False))
    found.sort()
    return [(st, ng) for _, st, ng in found]


# ----------------------------------------------------------------------------- O: triad terms
T_PI = re.compile(r"(?i)(kiriyābyākat|(?<![\wāīūṃṅñṭḍṇḷ])abyākat|ābyākat|(?<![\wāīūṃṅñṭḍṇḷ])akusal|ākusal|kusal)")
T_MY = re.compile("(" + "|".join(re.escape(v) for v in sorted(TERMS_MY.values(), key=len, reverse=True)) + ")")
MY_T = {v: k for k, v in TERMS_MY.items()}


def pali_terms(line):
    out = []
    for m in T_PI.finditer(strip_var(line)):
        k = m.group(1).lower()
        k = {"ābyākat": "abyākat", "ākusal": "akusal"}.get(k, k)
        out.append(k)
    return out


def my_terms(line):
    return [MY_T[m.group(1)] for m in T_MY.finditer(strip_var(line))]


# ----------------------------------------------------------------------------- N: numbers
def pali_numbers(line):
    s = strip_var(ID.sub("", line))
    cnt, kh, grp = [], [], []
    for m in re.finditer(r"(?i)(?<!" + W_ + r")(?:\w+?(?:e|yā)|\S+?(?:nti|īti)) (" + CNT_ALT + r")(?!" + W_
                         + r")(?! (?:\S+ )?(?:khandh|mahābhūt))", s):
        cnt.append((m.start(), COUNT_PI[m.group(1)]))
    for m in re.finditer(r"(?:…|pe…) (" + CNT_ALT + r")(?=\.)", s):            # «…pe… tīṇi.» (the answer count)
        cnt.append((m.start(), COUNT_PI[m.group(1)]))
    for m in re.finditer(r"\(sabbattha (" + CNT_ALT + r")\)", s):
        cnt.append((m.start(), COUNT_PI[m.group(1)]))
    for rx, v in EXTRA_CNT:
        for m in re.finditer(rx, s):
            if v is not None:
                cnt.append((m.start(), v))
    for m in re.finditer(r"(?i)(?<!" + W_ + r")(" + "|".join(MULA_PI) + r")", s):
        cnt.append((m.start(), MULA_PI[m.group(1).lower()]))
    if "ekekassa padassa" in s.lower():
        cnt.append((s.lower().find("ekekassa"), 1))
    if "ekekaṃ paccayaṃ" in s.lower():
        cnt.append((s.lower().find("ekekaṃ"), 1))
    for m in re.finditer(r"(?i)(?<!" + W_ + r")(" + "|".join(KH_PI) + r") (?:\S+ )?(?:khandh|mahābhūt)|catuviññāṇ|"
                         r"pañcaviññāṇ", s):
        kh.append(KH_PI[m.group(1).lower()] if m.group(1) else (4 if "catu" in m.group(0) else 5))
    if "tevīsatipaccayā" in s:
        kh.append(23)
    if "Cha " in s and "nayā" in s:
        kh.append(6)
    if "saddhāpañcamakesu" in s:
        kh.append(5)
    galt = "|".join(sorted(GROUP_PI, key=len, reverse=True))
    for m in re.finditer(r"(?i)(?<!ghā)(t?tik|duk)(?=[aāu])|(?<![\wāīūṃṅñṭḍṇḷ])(" + galt + r")", s):
        grp.append(3 if m.group(1) and "tik" in m.group(1).lower() else
                   (2 if m.group(1) else GROUP_PI[m.group(2).lower()]))
    digits = re.findall(r"\((\d+)\.?\)", s)
    return [v for _, v in sorted(cnt)], kh, grp, digits


def my_numbers(line):
    s = strip_var(ID.sub("", line))
    alt = "|".join(sorted(MY_NUM, key=len, reverse=True))
    cnt = [MY_NUM[m.group(1)] for m in re.finditer(r"(" + alt + r")ခု", s)]
    kh = [MY_NUM[m.group(1)] for m in re.finditer(r"(?<!သူ)(" + alt + r")ပါး", s)]
    grp = [MY_NUM[m.group(1)] for m in re.finditer(r"(" + alt + r")မျိုးတွဲ", s)]
    digits = re.findall(r"\((\d+)\.?\)", s)
    return cnt, kh, grp, digits


# ----------------------------------------------------------------------------- run
def load_generator():
    spec = importlib.util.spec_from_file_location("make_ch1_01", HERE / "make_ch1-01.py")
    K = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(K)          # registers every table and witness (writes nothing)
    return K


def split_sent(p, m):
    ps = re.split(r"(?<=[.?])\s+(?=\S)", ID.sub("", p).strip())
    ms = re.split(r"(?<=။)\s+(?=\S)", ID.sub("", m).strip())
    return ps, ms


def main():
    K = load_generator()
    F = K.F
    bad = []
    stats = {k: 0 for k in "SPCONITR"}
    pairs_all = []
    for name in NAMES:
        pl, ml = nonempty(PALI / name), nonempty(OUT / name)
        if len(pl) != len(ml):
            bad.append(("S", name, 0, f"line count {len(pl)} vs {len(ml)}"))
            continue
        for i, (p, m) in enumerate(zip(pl, ml), 1):
            pairs_all.append((name, i, p, m))
            stats["S"] += 1
            pid, mid = ID.search(p), ID.search(m)
            if (pid and pid.group(1)) != (mid and mid.group(1)):
                bad.append(("S", name, i, "block id"))
            if p.startswith("#") and p.split(" ")[0] != m.split(" ")[0]:
                bad.append(("S", name, i, "heading level"))
            if any(x in m for x in ("?", "।", ":-")):
                bad.append(("S", name, i, "forbidden mark"))
            body = re.sub(r"\{[^{}]*\}", "", ID.sub("", m))
            if re.search(r"[A-Za-zāīūṃṅñṭḍṇḷ]{2,}", body):
                bad.append(("S", name, i, "Latin left: " + re.findall(r"[A-Za-zāīūṃṅñṭḍṇḷ]{2,}", body)[0]))
            stats["P"] += 1
            ps = pali_norm(strip_var(p))
            exp_not = sum(len(re.findall(rx, ps)) * n for rx, n in NEG_NOT)
            exp_ma = sum(len(re.findall(rx, ps)) * n for rx, n in NEG_MA)
            got_not = strip_var(m).count("မဟုတ်")
            got_ma = len(MA_MY.findall(strip_var(m)))
            if exp_not != got_not or exp_ma != got_ma:
                bad.append(("P", name, i, f"negation မဟုတ် {exp_not}/{got_not}, မ… {exp_ma}/{got_ma}"))
            stats["C"] += 1
            pc, mc = pali_conds(p), my_conds(m)
            if pc != mc:
                k = next((j for j, (a, b) in enumerate(zip(pc, mc)) if a != b), min(len(pc), len(mc)))
                bad.append(("C", name, i, f"conditions differ at {k}: {pc[k:k + 3]} vs {mc[k:k + 3]} "
                                          f"({len(pc)}/{len(mc)})"))
            stats["O"] += 1
            pt, mt = pali_terms(p), my_terms(m)
            if pt != mt:
                bad.append(("O", name, i, f"terms {pt[:6]} vs {mt[:6]} ({len(pt)}/{len(mt)})"))
            stats["N"] += 1
            pn, mn = pali_numbers(pali_norm(p)), my_numbers(m)
            for lab, a, b in zip(("counts", "khandha", "groups", "digits"), pn, mn):
                if a != b:
                    bad.append(("N", name, i, f"{lab} {a[:8]} vs {b[:8]} ({len(a)}/{len(b)})"))
    # I: identity of sentences (this chapter + the approved sample)
    seen = {}
    pool = list(pairs_all)
    for name in SAMPLE:
        sp, sm = nonempty(PALI / name), nonempty(ROOT / "AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_"
                                                 "chapters" / name)
        pool += [(name, i, p, m) for i, (p, m) in enumerate(zip(sp, sm), 1)]
    for name, i, p, m in pool:
        ps, ms = split_sent(p, m)
        if len(ps) != len(ms):
            continue
        for a, b in zip(ps, ms):
            if name in NAMES:
                stats["I"] += 1
            key = a[:1].lower() + a[1:]
            seen.setdefault(key, {}).setdefault(b, (name, i))
    for k, v in seen.items():
        if len(v) > 1:
            bad.append(("I", "-", 0, f"«{k[:70]}» has {len(v)} renderings: {list(v.values())[:3]}"))
    # T: tables
    for st, my in CONDS_MY.items():
        stats["T"] += 1
        if F.N.get(st) != my:
            bad.append(("T", "-", 0, f"condition {st}: module «{F.N.get(st)}» vs checker «{my}»"))
    for k, my in (("kusal", "ကုသိုလ်"), ("akusal", "အကုသိုလ်"), ("abyākat", ABY)):
        stats["T"] += 1
        if F.TRIADS["kusala"][k] != my:
            bad.append(("T", "-", 0, f"term {k}"))
    for w, n in COUNT_PI.items():
        stats["T"] += 1
        if F.COUNT.get(w) != NUM_MY[n] + "ခု":
            bad.append(("T", "-", 0, f"count {w}"))
    for g, n in GROUP_PI.items():
        stats["T"] += 1
        key = g + "a"
        if key in F.GROUP and F.GROUP[key] != NUM_MY[n] + "မျိုးတွဲ":
            bad.append(("T", "-", 0, f"group {g}"))
    for k, my in (("VIPAKABY", "ကံ၏ အကျိုး ဖြစ်သော " + ABY), ("KIRIYABY", "ပြုရုံမျှသာ ဖြစ်သော " + ABY)):
        stats["T"] += 1
        if getattr(K, k) != my:
            bad.append(("T", "-", 0, k))
    # R: reuse
    reuse_n = reuse_ok = 0
    for pali, (book, bid, my) in F.WITNESS.items():
        f_, pseg, mseg = F.FINAL.SEG[book][bid]
        if my not in " ".join(mseg):
            bad.append(("R", "-", 0, f"witness «{pali}» no longer in pi-{book} {bid}"))
            continue
        rx = re.compile(r"(?i)(?<![\wāīūṃṅñṭḍṇḷ])" + re.escape(pali) + r"(?![\wāīūṃṅñṭḍṇḷ])")
        hits = [(n_, i, p, m) for n_, i, p, m in pairs_all if rx.search(strip_var(p))]
        if not hits:
            continue
        reuse_n += 1
        miss = [(n_, i) for n_, i, p, m in hits if my not in m]
        if miss:
            bad.append(("R", miss[0][0], miss[0][1], f"«{pali}» = «{my}» (pi-{book} {bid}) not used: {len(miss)} lines"))
        else:
            reuse_ok += 1
    stats["R"] = reuse_n
    import reuse_index as RI
    idx = RI.index()
    sent_n = sent_ok = 0
    for name, i, p, m in pairs_all:
        ps, ms = split_sent(p, m)
        if len(ps) != len(ms):
            continue
        for a, b in zip(ps, ms):
            k = RI.norm(a)
            if k in idx:
                sent_n += 1
                if b in idx[k]:
                    sent_ok += 1
                else:
                    bad.append(("R", name, i, f"sentence «{a[:50]}» differs from pi-1 … pi-6 {list(idx[k])[:1]}"))
    src = {(n_, i): p for n_, i, p, m in pairs_all}
    for b_ in bad:
        print(*b_, "|", src.get((b_[1], b_[2]), "")[:90])
    print("checked:", ", ".join(f"{k} {v}" for k, v in stats.items() if k != "R"))
    print(f"reuse test: terms {reuse_ok} / {reuse_n} identical (of {len(F.WITNESS)} witnessed values); "
          f"sentences {sent_ok} / {sent_n} identical")
    print(f"{len(bad)} mismatches")
    return 1 if bad else 0


# ----------------------------------------------------------------------------- --mutate
MUT = [  # (old, new, what): each planted error must make the check fail
    ("အမြစ်ဟူသော အကြောင်း၌ ခုနစ်ခု၊ အာရုံဟူသော အကြောင်း၌ ကိုးခု", "အမြစ်ဟူသော အကြောင်း၌ ခုနစ်ခု၊ အာရုံဟူသော အကြောင်း၌ ရှစ်ခု",
     "count"),
    ("အမြစ်ဟူသော အကြောင်းကြောင့် မဟုတ်ဘဲ ဖြစ်ပေါ်သည်", "အမြစ်ဟူသော အကြောင်းကြောင့် ဖြစ်ပေါ်သည်", "polarity"),
    ("ကုသိုလ် သဘောတရားသည် အကုသိုလ် သဘောတရားအား", "အကုသိုလ် သဘောတရားသည် ကုသိုလ် သဘောတရားအား", "term order"),
    ("အာရုံဟူသော အကြောင်းဖြင့် အကြောင်း ဖြစ်သည် – ပေးလှူခြင်း", "အကြီးအမှူးဟူသော အကြောင်းဖြင့် အကြောင်း ဖြစ်သည် – ပေးလှူခြင်း",
     "condition"),
    ("ကုသိုလ် အစုအဝေး တစ်ပါးကို မှီ၍ အစုအဝေး သုံးပါး၊", "ကုသိုလ် အစုအဝေး တစ်ပါးကို မှီ၍ အစုအဝေး နှစ်ပါး၊", "khandha count"),
    ("ဆယ့်သုံးခု", "ဆယ့်လေးခု", "count above ten"),
    ("(1) ^7-2-53", "(2) ^7-2-53", "digits"),
    ("ကံ၏ အကျိုးဟူသော အကြောင်း မပါဝင်သော", "ကံ၏ အကျိုးဟူသော အကြောင်း ပါဝင်သော", "sa-X / a-X"),
    ("ဆယ့်တစ်မျိုးတွဲ", "ဆယ့်နှစ်မျိုးတွဲ", "group number"),
]


def mutate():
    tmp = HERE / "chk-ch1-01" / "mut"
    caught = 0
    for old, new, what in MUT:
        if tmp.exists():
            shutil.rmtree(tmp)
        tmp.mkdir(parents=True)
        t = (OUT / NAMES[0]).read_text(encoding="utf-8")
        if old not in t:
            print("mutation not applicable:", what)
            continue
        (tmp / NAMES[0]).write_text(t.replace(old, new, 1), encoding="utf-8")
        r = subprocess.run([sys.executable, "-I", "-X", "utf8", str(HERE / "check_ch1-01.py"), "--out", str(tmp)]
                           + NAMES, capture_output=True, text=True)
        last = r.stdout.strip().splitlines()[-1] if r.stdout.strip() else r.stderr[-200:]
        ok = r.returncode != 0
        caught += ok
        print(f"{what:16} -> {'caught' if ok else 'MISSED'} ({last})")
    if tmp.exists():
        shutil.rmtree(tmp)
    print(f"{caught} / {len(MUT)} planted errors caught")
    return 0 if caught == len(MUT) else 1


def text_pe():
    """pi-3-mr/check_text.py on a «…Pe…»-folded copy of the Pāli in pi-7-my/chk-pe/ch1-01/ (deleted afterwards)."""
    tmp = HERE / "chk-pe" / "ch1-01"
    tmp.mkdir(parents=True, exist_ok=True)
    call = []
    for n in NAMES:
        (tmp / n).write_text((PALI / n).read_text(encoding="utf-8-sig").replace("…Pe…", "…pe…"), encoding="utf-8")
        call += [str(tmp / n), str(OUT / n)]
    r = subprocess.run([sys.executable, "-I", "-X", "utf8", str(HERE.parent / "pi-3-mr/check_text.py")] + call)
    shutil.rmtree(tmp)
    try:
        (HERE / "chk-pe").rmdir()          # only if no other agent's folder is in it
    except OSError:
        pass
    return r.returncode


if __name__ == "__main__":
    if MODE == "--mutate":
        sys.exit(mutate())
    if MODE == "--pe":
        sys.exit(text_pe())
    sys.exit(main())
