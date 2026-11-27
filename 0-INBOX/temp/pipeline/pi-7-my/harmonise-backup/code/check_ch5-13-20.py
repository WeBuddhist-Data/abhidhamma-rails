"""Per-line check of the Burmese pi-7 part 5 chapters 5-13 … 5-20 (the mixed orders anulomapaccanīya /
paccanīyānuloma: tikatika, dukaduka, tika, duka, dukatika, tikaduka) against the Pāli (adapted from check_ch5-01-04.py,
itself from check_ch4-01.py / check_sample.py; the condition, number and structure tests are check_ch4-01's, typed
tables included; the term test reads the Pāli term chains itself and composes their Burmese with this checker's own
rules from the atom values, each of which is witnessed in a finished chapter's published text or derived by this
checker's own negation rule; the terms named in the hand-written notes are read from this checker's own table).

usage: python3 -I -X utf8 check_ch5-13-20.py [chapter ...] [--out DIR] [--mutate] [--pe] [--groups]
Checks, line by line (Pāli line i <-> Burmese line i):
  S  structure: equal non-empty lines, heading #-level, block IDs, no «?» «।» «:-», no Latin left;
  C  conditions: the sequence of conditions (stem + polarity) in the Pāli = the sequence in the Burmese;
  O  term order: every Pāli term chain (conditioning -> conditioned, in Pāli order) has its expected Burmese phrase,
     found in the Burmese line in the same order;
  P  polarity: «မဟုတ်» in the line = «မဟုတ်» of the expected term phrases + the negated conditions;
  N  numbers: counts «… ခု», khandha numbers «… ပါး», group numbers «… မျိုးတွဲ», digits «(n)»;
  I  identity: identical Pāli sentences have identical Burmese sentences (these chapters and the approved sample);
     against the finished groups (1-00 … 4-01) the agreement is counted and every difference listed;
  T  tables: the condition names and counts equal this checker's copy; every «na-X» atom = this checker's negation
     of X; every stacked / known value = this checker's composition;
  R  reuse: every atom value is witnessed in a finished chapter (Pāli «X dhamma» <-> Burmese «… သဘောတရား»);
     the WITNESS values of the engines are re-read from the FINAL rails; sentences that occur in pi-1 … pi-6 are
     identical.
  R2 combined terms: every term chain of these chapters whose Pāli also occurs in a finished chapter (as «… dhamm»)
     has the same Burmese there (5-01 … 5-04, 4-02 … 4-14 dukatika, …);
--mutate  plants errors in copies (pi-7-my/chk-mut-ch5-13-20/, deleted afterwards); each must be caught.
--pe      runs pi-3-mr/check_text.py on a «…Pe…»-folded copy of the Pāli in pi-7-my/chk-pe/ch5-13-20/ (deleted).
Exit 1 on any mismatch.
"""
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
DISK = OUT
SAMPLE = ["1-00-paccaya.md", "1-02-vedanattika.md"]
MINE = ["5-13-anulomapaccaniya-tikatika.md", "5-14-anulomapaccaniya-dukaduka.md", "5-15-paccaniyanuloma-tika.md",
        "5-16-paccaniyanuloma-duka.md", "5-17-paccaniyanuloma-dukatika.md", "5-18-paccaniyanuloma-tikaduka.md",
        "5-19-paccaniyanuloma-tikatika.md", "5-20-paccaniyanuloma-dukaduka.md"]
# the finished groups (written and approved before this group; not 4-15 … 4-21 and 5-05 … 5-12, in progress)
_DONE4 = tuple(f"4-{i:02d}" for i in range(1, 15))
_DONE5 = ("5-01", "5-02", "5-03", "5-04")
GROUPS = sorted(p.name for p in DISK.glob("*.md")
                if p.name[:2] in ("1-", "2-", "3-") or p.name.startswith(_DONE4 + _DONE5))
_args = sys.argv[1:]
FLAGS = {a for a in _args if a in ("--mutate", "--pe", "--groups")}
_args = [a for a in _args if a not in FLAGS]
if "--out" in _args:
    OUT = pathlib.Path(_args[_args.index("--out") + 1]).resolve()
    del _args[_args.index("--out"):_args.index("--out") + 2]
NAMES = [next(n for n in MINE if n.startswith(a)) for a in _args] or MINE
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

NUM_MY = {1: "တစ်", 2: "နှစ်", 3: "သုံး", 4: "လေး", 5: "ငါး", 6: "ခြောက်", 7: "ခုနစ်", 8: "ရှစ်", 9: "ကိုး", 10: "ဆယ်",
          11: "ဆယ့်တစ်", 12: "ဆယ့်နှစ်", 13: "ဆယ့်သုံး", 14: "ဆယ့်လေး", 15: "ဆယ့်ငါး", 16: "ဆယ့်ခြောက်",
          17: "ဆယ့်ခုနစ်", 18: "ဆယ့်ရှစ်", 19: "ဆယ့်ကိုး", 20: "နှစ်ဆယ်", 21: "နှစ်ဆယ့်တစ်", 22: "နှစ်ဆယ့်နှစ်",
          23: "နှစ်ဆယ့်သုံး", 24: "နှစ်ဆယ့်လေး"}
MY_NUM = {v: k for k, v in NUM_MY.items()}
COUNT_PI = {"ekaṃ": 1, "ekā": 1, "dve": 2, "tīṇi": 3, "tisso": 3, "cattāri": 4, "pañca": 5, "cha": 6, "satta": 7,
            "aṭṭha": 8, "nava": 9, "dasa": 10, "ekādasa": 11, "dvādasa": 12, "terasa": 13, "cuddasa": 14,
            "pannarasa": 15, "soḷasa": 16, "sattarasa": 17, "aṭṭhārasa": 18, "ekūnavīsati": 19, "vīsati": 20,
            "ekavīsati": 21, "dvāvīsati": 22, "bāvīsati": 22, "tevīsati": 23, "tevīsa": 23, "catuvīsati": 24,
            "ekavīsa": 21, "sattārasa": 17, "dvepi": 2, "cattāripi": 4,
            # 3-01 … 3-02 notes: «-pi» (all N «…ခုလုံး»), locatives «dvīsu / tīsupi», «ekāyeva» «တစ်ခုတည်း»
            "tīṇipi": 3, "navapi": 9, "dvīsu": 2, "dvīsupi": 2, "tīsupi": 3, "dvinnampi": 2, "ekāyeva": 1, "ekoyeva": 1,
            # 3-07 … 3-10 notes: «tīsu (padesu)», «catūsupi», «ekaṃyeva»
            "tīsu": 3, "catūsupi": 4, "ekaṃyeva": 1,
            # 4-01 notes: «pañcapi» «ငါးခုလုံး», «tīṇiyeva» «သုံးခုသာ»
            "pañcapi": 5, "tīṇiyeva": 3}
KH_PI = {"eko": 1, "ekaṃ": 1, "ekassa": 1, "dve": 2, "dvinnaṃ": 2, "tayo": 3, "tiṇṇannaṃ": 3, "tiṇṇaṃ": 3,
         "cattāro": 4, "pañcannaṃ": 5}
GROUP_PI = {"catukk": 4, "pañcak": 5, "chakk": 6, "sattak": 7, "aṭṭhak": 8, "navak": 9, "dasak": 10, "ekādasak": 11,
            "dvādasak": 12, "terasak": 13, "tevīsak": 23, "catuvīsak": 24}
MULA_PI = {"ekamūlak": 1, "dumūlak": 2, "timūlak": 3, "catumūlak": 4, "pañcamūlak": 5, "tevīsatimūlak": 23}


# numbers of these chapters (in addition to check_ch4-01's)
NUM_MY.update({29: "နှစ်ဆယ့်ကိုး", 30: "သုံးဆယ်", 34: "သုံးဆယ့်လေး", 35: "သုံးဆယ့်ငါး", 36: "သုံးဆယ့်ခြောက်",
               37: "သုံးဆယ့်ခုနစ်"})
MY_NUM = {v: k for k, v in NUM_MY.items()}
COUNT_PI.update({"catuvīsa": 24, "ekūnatiṃsa": 29, "tiṃsa": 30, "catuttiṃsa": 34, "pañcatiṃsa": 35,
                 "chattiṃsa": 36, "sattatiṃsa": 37})
NUM_MY.update({26: "နှစ်ဆယ့်ခြောက်", 28: "နှစ်ဆယ့်ရှစ်", 49: "လေးဆယ့်ကိုး"})
MY_NUM = {v: k for k, v in NUM_MY.items()}
COUNT_PI.update({"aṭṭhavīsa": 28, "chabbīsa": 26, "chabbīsati": 26, "ekūnapaññāsa": 49, "dvāvīsa": 22,
                 "tīṇimeva": 3, "ekameva": 1, "sattameva": 7, "ekavīsatimeva": 21, "dveyeva": 2, "navapañhaṃ": 9,
                 "navapañhameva": 9})
NOTE_PAIRS = {}
NOTE_CONDS_SAMPLE = {"vipākaṃ natthi": [("vipāka", False)]}             # «(Sabbattha nava, vipākaṃ natthi.)»
HEAD_CONDS = {"Hetuārammaṇapaccayādi": [("hetu", False), ("ārammaṇa", False)],
              "Nahetunaārammaṇapaccayādi": [("hetu", True), ("ārammaṇa", True)]}
NEG_WORD = "မဟုတ်"


def neg_my(v):
    """this checker's negation of an attributive (free na = «… မဟုတ်»; pi-1 «na hetū» / «na pītisahagatā»)"""
    m = re.fullmatch(r"(.+) ဖြစ်သော", v)
    if m and " " not in m[1].replace("မှားယွင်းသော ", "").replace("စိတ်၏ ", "").replace("ကံ၏ ", "") and \
            not m[1].endswith(("ကြောင့်", "၍", "နှင့်အတူ", "မှ", "၌", "သို့", "ဖြင့်")):
        return m[1] + " မဟုတ်သော"
    if v.endswith("မည့်"):
        return v[:-4] + "မည် မဟုတ်သော"
    if v.endswith("သော"):
        return v[:-3] + "သည် မဟုတ်သော"
    return v + " မဟုတ်သော"

def nonempty(p):
    return [l for l in p.read_text(encoding="utf-8-sig").splitlines() if l.strip()]


def strip_var(s):
    return re.sub(r"\{[^{}]*\}", "", s)


# ----------------------------------------------------------------------------- C: conditions
def seg(comp):
    out = []
    for part in comp.replace(" -", "-").replace("- ", "-").split("-"):
        p = part.lower()
        if p.endswith("ṃ") and p[:-1] in CONDS_MY:
            p = p[:-1]
        if p.endswith("adhipat"):
            p += "i"
        while p:
            for st in STEMS:
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


def pali_conds(line):
    s = strip_var(ID.sub("", line))
    s = re.sub(r"(?i)(?<![\wāīūṃṅñṭḍṇḷ*])hetuduk[\wāīūṃṅñṭḍṇḷ]*", lambda m: " " * len(m[0]), s)   # «Hetuduka-…» (a dyad name)
    found = []
    for k, (_, v) in NOTE_PAIRS.items():
        if k in s:
            found += [(s.find(k) + j / 10, st, ng) for j, (st, ng) in enumerate(v)]
            s = s.replace(k, " " * len(k))
    for k, v in NOTE_CONDS_SAMPLE.items():
        i = s.find(k)
        while i >= 0:
            found += [(i + j / 10, st, ng) for j, (st, ng) in enumerate(v)]
            i = s.find(k, i + 1)
    for k, v in HEAD_CONDS.items():
        if k in s:
            found += [(s.find(k) + j / 10, st, ng) for j, (st, ng) in enumerate(v)]
    head = s.startswith("#")
    stems = "|".join(STEMS)
    for m in re.finditer(r"(?i)(?<!" + W_ + r")(na |na|no)?(" + stems + r")paccay", s):
        found.append((m.start(), m.group(2).lower(), bool(m.group(1))))
    loc = {"hetuyā": "hetu", "adhipatiyā": "adhipati", "atthiyā": "atthi", "natthiyā": "natthi"}
    loc.update({x[:-1] + "e": x for x in STEMS if x not in loc})
    _la = "|".join(sorted(loc, key=len, reverse=True))
    for m in re.finditer(r"(?i)(?<!" + W_ + r")(na |no |na|no)?(" + _la + r")(?= (?:(?:na|no)?(?:" + _la + r") )*"
                         r"(?:sabbattha )?(?:" + "|".join(COUNT_PI) + r")(?!" + W_ + r")(?! (?:\S+ )?khandh))", s):
        found.append((m.start(), loc[m.group(2).lower()], bool(m.group(1))))
    sandhi = "|".join(x[:-1] if x.endswith("a") else x for x in STEMS)
    look = r"(?=ādi|sabhāg|mūlak|ghaṭan|duk|sadis" + ("|-" if head else "") + ")"
    for m in re.finditer(r"(?i)(?<![\wāīūṃṅñṭḍṇḷ-])(na|no)?(" + sandhi + r")a?" + look, s):
        stem = next(x for x in STEMS if x == m.group(2).lower() or x[:-1] == m.group(2).lower())
        if any(abs(f[0] - m.start()) < 1 for f in found):
            continue
        found.append((m.start(), stem, bool(m.group(1))))
    for m in re.finditer(r"(?i)(?<!" + W_ + r")([\wāīūṃṅñṭḍṇḷ]+(?: ?- ?[\wāīūṃṅñṭḍṇḷ]+)+)(?:nti|īti) (?:(?:"
                         + "|".join(COUNT_PI) + r")(?!" + W_ + ")|(?=na|no))", s):
        for k, st in enumerate(seg(m.group(1))):
            found.append((m.start() + k / 100, st, False))
    for m in re.finditer(r"(?i)((?:n[ao][\wāīūṃṅñṭḍṇḷ]+-)+)(?=n[ao][\wāīūṃṅñṭḍṇḷ]+paccayā)", s):
        k = 0
        found = [f for f in found if not (m.start() <= f[0] < m.end())]
        for part in m.group(1).strip("-").split("-"):
            p = part.lower()
            while p:
                pre, p = p[:2], p[2:]
                st = next(x for x in STEMS if p.startswith(x))
                found.append((m.start() + k / 100, st, True))
                p = p[len(st):]
                k += 1
    found.sort()
    return [(st, ng) for _, st, ng in found]


NAME_ALT = "|".join(re.escape(CONDS_MY[s]) for s in sorted(CONDS_MY, key=lambda x: len(CONDS_MY[x]), reverse=True))
MY_NAME = {v: k for k, v in CONDS_MY.items()}
GH_MY = re.compile(r"((?:(?:" + NAME_ALT + r")၊ )*(?:" + NAME_ALT + r")) ဟူသော ပေါင်းစပ်ချက်")


def my_conds(line, pline):
    s = strip_var(ID.sub("", line))
    found = []
    for k, (my, v) in NOTE_PAIRS.items():
        if k in strip_var(pline):
            if my not in s:
                return None                              # the note's Burmese is not the checker's
            found += [(s.find(my) + j / 10, st, ng) for j, (st, ng) in enumerate(v)]
            s = s.replace(my, " " * len(my))
    for m in re.finditer(r"(?<![^\s(“*…])(" + NAME_ALT + r")ဟူသော အကြောင်း((?:ကြောင့်)? မဟုတ်|ဖြင့် အကြောင်း ဖြစ်သည် မဟုတ်)?", s):
        found.append((m.start(), MY_NAME[m.group(1)], bool(m.group(2))))
    for m in GH_MY.finditer(s):
        for k, nm in enumerate(m.group(1).split("၊ ")):
            found.append((m.start() + k / 100, MY_NAME[nm], False))
    for m in re.finditer(r"(?<![^\s(])(" + NAME_ALT + r")((?: မဟုတ်ခြင်း)?)နှင့် တူ(?:ကြ)?(?:သည်|သော|အောင်)", s):
        found.append((m.start(), MY_NAME[m.group(1)], bool(m.group(2))))
    found.sort()
    return [(st, ng) for _, st, ng in found]



KH_NOUN = r"(?:khandh|mahābhūt|viññāṇ|upādānā(?![\wāīūṃṅñṭḍṇḷ]))"


def pali_numbers(line):
    s = strip_var(ID.sub("", line)).replace("tikatika", "tika-tika").replace("dukaduka", "duka-duka").replace("dukatika", "duka-tika")
    s = s.replace("catukkhattuṃ", "catu-khattuṃ")          # «four times» (the verse of 3-07: not a group of four)
    # «tīṇi tīṇi / cattāri cattāri» (N each) = one count «Nခုစီ»; «ekekassa mūle» «… တစ်ခုစီ၌»
    s = re.sub(r"(?<![\wāīūṃṅñṭḍṇḷ])([Tt]īṇi|[Cc]attāri|dve) (?:tīṇi|cattāri|dve)(?![\wāīūṃṅñṭḍṇḷ])", r"\1", s).replace("ekekassa mūle", "ekaṃ mūle")
    cnt, kh, grp = [], [], []
    for m in re.finditer(r"(?i)(?<!" + W_ + r")(" + "|".join(sorted(COUNT_PI, key=len, reverse=True)) + r")(?!" + W_
                         + r")(?! (?:\S+ )?" + KH_NOUN + r")", s):
        if m.group(1) in ("ekaṃ", "dve") and re.match(r" (?:\S+ )?" + KH_NOUN, s[m.end():]):
            continue
        if s[max(0, m.start() - 9):m.start()] == "ahetukaṃ ":       # «ahetukaṃ ekaṃ…» (one aggregate)
            continue
        cnt.append((m.start(), COUNT_PI[m.group(1).lower()]))
    for m in re.finditer(r"(?i)(?<!" + W_ + r")(" + "|".join(MULA_PI) + r")", s):
        cnt.append((m.start(), MULA_PI[m.group(1).lower()]))
    if "ekekassa padassa" in s.lower():
        cnt.append((s.lower().find("ekekassa"), 1))
    if "tiṇṇannaṃ kātabbā" in s:
        cnt.append((s.find("tiṇṇannaṃ kātabbā"), 3))
    for m in re.finditer(r"(?i)(?<!" + W_ + r")(" + "|".join(KH_PI) + r")(?!" + W_ + r")(?= (?:\S+ )?" + KH_NOUN
                         + r"|(?:…pe…)?…|\.\.\.|(?:…pe…)?[.,]| (?:\S+ )?§)", s):
        w = m.group(1).lower()
        if (w in ("ekaṃ", "dve") and not re.match(r" (?:\S+ )?" + KH_NOUN, s[m.end():])
                and s[max(0, m.start() - 9):m.start()] != "ahetukaṃ "):
            continue
        kh.append((m.start(), KH_PI[w]))
    for m in re.finditer(r"(?i)ajjhattattiko(?!" + W_ + ")", s):     # «Ajjhattattiko» (nominative -o)
        grp.append(3)
    for m in re.finditer(r"ttikadvay", s):                        # «X-ttikadvaya» «… သုံးမျိုးတွဲ နှစ်ခု»
        cnt.append((m.start(), 2))
    for m in re.finditer(r"ādichagocchak", s):                    # «… စသည်တို့၏ အစု ခြောက်ခု»
        cnt.append((m.start(), 6))
    for m in re.finditer(r"(?i)(pañca|catu) ?viññāṇ", s):
        kh.append((m.start(), 5 if m.group(1).lower() == "pañca" else 4))
    for m in re.finditer(r"(?i)tevīsatipaccayā|catuvīsatipaccayā", s):
        kh.append((m.start(), 23 if m.group(0).lower().startswith("tev") else 24))
    for m in re.finditer(r"tayokhandh", s):                       # source slip «tayokhandhā»
        kh.append((m.start(), 3))
    if "Cha " in s and "nayā" in s:
        kh.append((s.find("Cha "), 6))
    if "ubhopete" in s:                                     # «both of these» «ထိုနှစ်ပါးလုံး» (the verse of 3-07)
        kh.append((s.find("ubhopete"), 2))
    for m in re.finditer(r"(?i)pañcāyatan", s):
        kh.append((m.start(), 5))
    if "saddhāpañcamakesu" in s:
        kh.append((s.find("saddhāpañcamakesu"), 5))
    for m in re.finditer(r"(?i)((?<!ghā)(?<!ajjha)(?<!ajjhat)(?<!mā)(?<!ka)(?<!pī)t?tik|duk)(?=[aāue])|(" + "|".join(GROUP_PI) + r")", s):
        grp.append(3 if m.group(1) and "tik" in m.group(1).lower() else (2 if m.group(1) else GROUP_PI[m.group(2).lower()]))
    digits = re.findall(r"\((\d+)\.?\)", s)
    return [v for _, v in sorted(cnt)], [v for _, v in sorted(kh)], grp, digits


def my_numbers(line):
    s = strip_var(ID.sub("", line)).replace("တစ်စုံတစ်ခုသော", "")     # kenaci «တစ်စုံတစ်ခုသော» (not a count)
    alt = "|".join(sorted(MY_NUM, key=len, reverse=True))
    cnt = [MY_NUM[m.group(1)] for m in re.finditer(r"(?<!ဆယ့်)(?<!နှစ်ဆယ့်)(" + alt + r")ခု", s)]
    kh = [MY_NUM[m.group(1)] for m in re.finditer(r"(?<!သူ)(?<!ဆယ့်)(" + alt + r")ပါး", s)]
    grp = [MY_NUM[m.group(1)] for m in re.finditer(r"(?<!ဆယ့်)(" + alt + r")မျိုးတွဲ", s)]
    digits = re.findall(r"\((\d+)\.?\)", s)
    return cnt, kh, grp, digits




# ----------------------------------------------------------------------------- O / P: term chains
def load_make():
    import importlib.util
    spec = importlib.util.spec_from_file_location("make_ch5_13_20", HERE / "make_ch5-13-20.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


class Terms:
    """the Pāli term chains of a line, read with the atom surfaces (Pāli strings) of the generator"""

    def __init__(self, mk):
        self.mk = mk
        self.ends = {"a": "añceva|ānañca|añca|assa|ānaṃ|aṃ|ena|o|ā|e", "u": "uñceva|ūnaṃ|uñca|ussa|uṃ|ū|u",
                     "i": "iñceva|īnaṃ|iñca|issa|ino|iṃ|ī|i", "d": "ā"}
        alts = []
        for s in sorted(mk.ATOM, key=len, reverse=True):
            pat = f"[{s[0].upper()}{s[0]}]" + re.escape(s[1:]).replace(r"\ ", " ")
            alts.append(f"(?P<a{len(alts)}>{pat})(?:{self.ends[mk.ATOM[s][0]]})")
        self.surf = sorted(mk.ATOM, key=len, reverse=True)
        self.rx = re.compile(r"(?<![\wāīūṃṅñṭḍṇḷ])(?:" + "|".join(alts) + r")(?![\wāīūṃṅñṭḍṇḷ])")

    def atoms(self, line):
        out = []
        for m in self.rx.finditer(line):
            g = next(k for k, v in m.groupdict().items() if v)
            out.append((m.start(), m.end(), self.surf[int(g[1:])], m[0]))
        return out

    def chains(self, line, closer_links):
        """[(pali, expected Burmese)] in Pāli order"""
        mk = self.mk
        occ = self.atoms(line)
        terms, i = [], 0
        while i < len(occ):
            if i + 1 < len(occ):
                gap = line[occ[i][1]:occ[i + 1][0]]
                if gap == " ceva " or (gap == " " and occ[i][3].endswith("ñceva")):
                    terms.append([occ[i], occ[i + 1]])
                    i += 2
                    continue
            terms.append([occ[i]])
            i += 1
        def tail_ca(t):
            return line[t[-1][1]:t[-1][1] + 3] == " ca"
        chains, cur = [], []
        for t in terms:
            if cur:
                prev = cur[-1]
                end = prev[-1][1] + (3 if tail_ca(prev) else 0)
                ok = line[end:t[0][0]] == " "
                w = prev[-1][3]
                if len(prev) == 1:
                    ok = ok and not w.endswith("ñca") and not tail_ca(prev)
                else:
                    ok = ok and (closer_links or not (w.endswith("ñca") or tail_ca(prev)))
                if ok:
                    ok = self._same_case(prev[-1], t[0])
                if ok:
                    cur.append(t)
                    continue
                chains.append(cur)
            cur = [t]
        if cur:
            chains.append(cur)
        out = []
        for ch in chains:
            end = ch[-1][-1][1]
            lone = len(ch) == 1 and len(ch[0]) == 1
            if lone:
                rest = line[end:end + 30]
                surf = ch[0][0][2]
                if not (re.match(r" (?:ca )?(?:dhamm|khandh|(?:ekaṃ|eko|ekassa|dve|tayo) khandh|kaṭattārūp)", rest)
                        or ch[0][0][3].endswith("ñca") or rest.startswith(" ca ") or surf.endswith("dhammadhamm")):
                    continue
            out.append((line[ch[0][0][0]:end], self.value(ch)))
        return out

    def _same_case(self, a, b):
        ca, cb = self._case(a), self._case(b)
        return ca is None or cb is None or ca == cb

    def _case(self, o):
        cls = self.mk.ATOM[o[2]][0]
        e = o[3][len(o[2]):]
        e = e[0].lower() + e[1:] if e else e
        if o[3][:1].isupper():
            e = o[3][len(o[2]):]
        table = {"añceva": "aṃ", "ānañca": "ānaṃ", "añca": "aṃ", "aṃ": "aṃ", "assa": "assa", "ānaṃ": "ānaṃ", "o": "o",
                 "ā": "ā", "e": "e", "ena": "ena", "uñceva": "aṃ", "uñca": "aṃ", "uṃ": "aṃ", "ussa": "assa", "u": "o",
                 "ūnaṃ": "ānaṃ", "iñceva": "aṃ", "iñca": "aṃ", "iṃ": "aṃ", "issa": "assa", "ino": "ā", "īnaṃ": "ānaṃ"}
        return None if cls == "d" else table.get(e)

    def value(self, ch):
        mk = self.mk
        items = []
        for t in ch:
            s = tuple(o[2] for o in t)
            if len(t) == 2:
                items.append(("v", mk.KNOWN.get(s, "၊ ".join(mk.ATOM[x][1] for x in s))))
            else:
                items.append(("a", s[0]))
        vals, k = [], 0
        while k < len(items):
            if k + 1 < len(items) and items[k][0] == items[k + 1][0] == "a" and (items[k][1], items[k + 1][1]) in mk.KNOWN_ADJ:
                vals.append(mk.KNOWN_ADJ[(items[k][1], items[k + 1][1])])
                k += 2
                continue
            vals.append(mk.ATOM[items[k][1]][1] if items[k][0] == "a" else items[k][1])
            k += 1
        return "၊ ".join(vals)


def my_term_order(line, phrases):
    """every expected phrase is found, in order (each after the previous one)"""
    pos, miss = 0, []
    for p, v in phrases:
        j = line.find(v, pos)
        if j < 0:
            miss.append((p, v))
            continue
        pos = j + len(v)
    return miss


# ----------------------------------------------------------------------------- terms named in notes / sentences
# this checker's own reading of the terms the hand-written notes and sentences name (atom surfaces; a tuple = one
# stacked term «A၊ B»), independent of the generator's tables
NOTE_TERMS = {
    "(Kusale pañca, akusale pañca, abyākate tīṇi.)": [("kusal",), ("akusal",), ("abyākat",)],
    "(Uppādī anuppannasadisaṃ.)": [("uppād",), ("anuppann",)],
    "(Anāgataṃ atītasadisaṃ.)": [("anāgat",), ("atīt",)],
    "(Dukkhāya vedanāya sampayuttaabyākatamūlaṃ adukkhamasukhāya vedanāya sampayuttaabyākatamūlampi kātabbaṃ.)":
        [("dukkhāya vedanāya sampayutt", "abyākat"), ("adukkhamasukhāya vedanāya sampayutt", "abyākat")],
    "(Sahetukasadisaṃ.)": [("sahetuk",)],
    "(Asaṅkhataṃ appaccayasadisaṃ.)": [("asaṅkhat",), ("appaccay",)],
    "(Lokiyasadisaṃ.)": [("lokiy",)],
    "(Saṅkhataṃ sappaccayasadisaṃ)": [("saṅkhat",), ("sappaccay",)],
    "(Saṅkhataṃ sappaccayasadisaṃ.)": [("saṅkhat",), ("sappaccay",)],
    "(Naakusale tīṇi. Naabyākate tīṇi. Saṃkhittaṃ.)": [("naakusal",), ("naabyākat",)],
    "(Ajjhattabahiddhārammaṇaṃ natthi.)": [("ajjhattabahiddhārammaṇ",)],
    "(Nahetunaanidassanasappaṭighamūlepi tīṇiyeva.)": [("nahet", "naanidassanasappaṭigh")],
    "(Nasahetukanaanidassanasappaṭighamūlepi tīṇiyeva.)": [("nasahetuk", "naanidassanasappaṭigh")],
    "(Nahetusampayuttaṃ nasanidassanasappaṭighaṃ sahetukadukasadisaṃ. Tīṇi pañhā. Hetusahetukaduke ca "
    "hetuhetusampayuttaduke ca pañhā no labbhati.)": [("nahetusampayutt", "nasanidassanasappaṭigh")],
    "(Naappaccayanaanidassanaappaṭighamūlepi ekameva.)": [("naappaccay", "naanidassanaappaṭigh")],
    "(Nasaṅkhataṃ nasappaccayasadisaṃ.)": [("nasaṅkhat",), ("nasappaccay",)],
    "(Nasāsavaṃ naanidassanasappaṭighamūlassa purimanayena tīṇi pañhā.)": [("nasāsav", "naanidassanasappaṭigh")],
    "(Naāsavasampayuttanaanidassanasappaṭighamūle tīṇiyeva.)": [("naāsavasampayutt", "naanidassanasappaṭigh")],
    "(Naāsavañceva naanāsavaṃ naanidassanasappaṭighamūlepi purimanayena tīṇiyeva.)":
        [("naāsav", "naanāsav", "naanidassanasappaṭigh")],
    "(Āsavavippayuttanasāsavanaanidassanasappaṭighamūlepi purimanayeneva tīṇi pañhā.)":
        [("āsavavippayutt", "nasāsav", "naanidassanasappaṭigh")],
    "(Anidassanasappaṭighe tīṇiyeva.)": [("anidassanasappaṭigh",)],
    "(Ahetukasadisaṃ, saṃkhittaṃ.)": [("ahetuk",)],
    "(Naakusale dve, naabyākate dve. Paṭhamaṃ gaṇitakena ekaṃ, dutiyaṃ gaṇitakena ekaṃ, tatiyaṃ gaṇitakena ekaṃ, "
    "sabbattha nava pañhā.)": [("naakusal",), ("naabyākat",)],
    "(Akusalamūle dve, dukamūle dve.)": [("akusal",)],
    "(apariyāpannasadisaṃ cha pañhā)": [("apariyāpann",)],
    "(Nahetu nanahetu ovattā, tīṇi mūlāni, ekavīsati pañhā kātabbā.)": [("nahet",), ("nanahet",)],
    "(Akusalāneva tīṇi.)": [("akusal",)],
    "(Naakusalaṃ naabyākataṃ natthi.)": [("naakusal",), ("naabyākat",)],
    "(Naanidassanasappaṭighanaabyākatamūlāni sattameva, dukamūlāni sattameva, sabbaṃ ekavīsatimeva.)":
        [("naanidassanasappaṭigh", "naabyākat")],
    # sentences outside brackets
    "Akusale tīṇi.": [("akusal",)],
    "Abyākataṃ anupādinnupādāniye tīṇiyeva…pe….": [("abyākat",), ("anupādinnupādāniy",)],
    "Nahetu nadukkhāya vedanāya sampayuttamūlaṃ tīṇiyeva.": [("nahet", "nadukkhāya vedanāya sampayutt")],
    "Nakenaci viññeyyaṃ naanidassanasappaṭighassa purimasadisaṃ navapañhaṃ kātabbaṃ.":
        [("nakenaci viññeyy", "naanidassanasappaṭigh")],
    "Nakenaci viññeyyaṃ naanidassanaappaṭighamūlassa navapañhameva.": [("nakenaci viññeyy", "naanidassanaappaṭigh")],
    "Naasaṅkhataṃ…pe… (sappaccayadukasadisaṃ).": [("naasaṅkhat",)],
}
TWO_SETS = ("5-13", "5-14", "5-17", "5-18", "5-19", "5-20")


def note_terms(line, Qm):
    """the expected Burmese of the terms the notes / sentences of a Pāli line name, and the line without them"""
    out = []
    for k in sorted(NOTE_TERMS, key=len, reverse=True):
        rx = re.compile(("" if k.startswith("(") else r"(?<![\wāīūṃṅñṭḍṇḷ(])") + re.escape(k))
        while True:
            mm = rx.search(line)
            if not mm:
                break
            for t in NOTE_TERMS[k]:
                out.append((k, "၊ ".join(Qm.ATOM[a][1] for a in t)))
            line = line[:mm.start()] + " " * len(k) + line[mm.end():]
    return out, line


# ----------------------------------------------------------------------------- run
GROUP_DIFF = []


def split_p(s):
    return re.split(r"(?<=[.?])\s+(?=\S)", ID.sub("", s).strip())


def split_m(s):
    return re.split(r"(?<=။)\s+(?=\S)", ID.sub("", s).strip())


PI1_TEXT = "\n".join(f.read_text(encoding="utf-8") for f in
                     sorted((ROOT / "AI_translation/burmese/pi-1-burmese-plain-rails_split_chapters").glob("*.md")))


def check(names, out):
    mk = load_make()
    Qm = mk.Q
    F = Qm.F
    TT = Terms(Qm)
    bad = []
    stats = {k: 0 for k in "SCOPNITR"}
    pairs_all = []
    for name in names:
        pl, ml = nonempty(PALI / name), nonempty(out / name)
        if len(pl) != len(ml):
            bad.append(("S", name, 0, f"line count {len(pl)} vs {len(ml)}"))
            continue
        closer = name.startswith(TWO_SETS)
        for i, (p, m) in enumerate(zip(pl, ml), 1):
            for a, b in Qm.SLIP_FIX.items():              # the logged source slips, read as the generator reads them
                p = p.replace(a, b)
            pairs_all.append((name, i, p, m))
            stats["S"] += 1
            pid, mid = ID.search(p), ID.search(m)
            if (pid and pid.group(1)) != (mid and mid.group(1)):
                bad.append(("S", name, i, "block id"))
            if p.startswith("#") and p.split(" ")[0] != m.split(" ")[0]:
                bad.append(("S", name, i, "heading level"))
            if any(x in m for x in ("?", "।", ":-")):
                bad.append(("S", name, i, "forbidden mark"))
            body = strip_var(ID.sub("", m))                  # variants keep their Pāli reading (approved)
            if re.search(r"[A-Za-zāīūṃṅñṭḍṇḷ]{2,}", body):
                bad.append(("S", name, i, "Latin left: " + re.findall(r"[A-Za-zāīūṃṅñṭḍṇḷ]{2,}", body)[0]))
            if re.search(r"[ၠ-႟]|[ꩠ-ꩿ]", m):
                bad.append(("S", name, i, "non-Burmese Myanmar block code point"))
            if p.count("–") != m.count("–") or p.count("—") != m.count("—"):
                bad.append(("S", name, i, "dash count"))
            stats["C"] += 1
            pc, mc = pali_conds(p), my_conds(m, p)
            if mc is None or pc != mc:
                bad.append(("C", name, i, f"conditions {pc[:6]}… vs {(mc or [])[:6]}… ({len(pc)}/{len(mc or [])})"))
            if not p.startswith("#"):
                stats["O"] += 1
                nt, p_rest = note_terms(ID.sub("", p), Qm)
                p_rest = re.sub(r"\([^()]*\)", lambda x: " " * len(x[0]), p_rest)   # notes: their terms are in nt
                ph = TT.chains(p_rest, closer)
                miss = my_term_order(m, ph)
                if miss:
                    bad.append(("O", name, i, f"term phrase missing / out of order: {miss[0][0]} = «{miss[0][1]}»"))
                groups_ = {}
                for k, v in nt:
                    groups_.setdefault(k, []).append((k, v))
                for k, g_ in groups_.items():                 # the terms of one note: present and in Pāli order
                    miss_ = my_term_order(m, g_)
                    if miss_:
                        bad.append(("O", name, i, f"note term missing / out of order: {k[:40]} = «{miss_[0][1]}»"))
                stats["P"] += 1
                exp = sum(v.count(NEG_WORD) for _, v in ph + nt) + sum(1 for _, ng in pc if ng)
                # the engine's «vipākābyākata / kiriyābyākata» «… ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော» (not atoms)
                exp += 2 * len(re.findall(r"(?i)(?:vipākā|kiriyā)byākat", p_rest))
                got = m.count(NEG_WORD)
                if exp != got:
                    bad.append(("P", name, i, f"«မဟုတ်» expected {exp}, found {got}"))
            stats["N"] += 1
            pn, mn = pali_numbers(p), my_numbers(m)
            for lab, a, b in zip(("counts", "khandha", "groups", "digits"), pn, mn):
                if a != b:
                    bad.append(("N", name, i, f"{lab} {a} vs {b}"))
    # I: identity (these chapters + the approved sample)
    seen = {}
    extra = []
    for n in SAMPLE:
        pl, ml = nonempty(PALI / n), nonempty(DISK / n)
        extra += [(n, i, p, m) for i, (p, m) in enumerate(zip(pl, ml), 1)]
    for name, i, p, m in pairs_all + extra:
        ps, ms = split_p(p), split_m(m)
        if len(ps) != len(ms):
            continue
        for a, b in zip(ps, ms):
            if name in names:
                stats["I"] += 1
            seen.setdefault(a[:1].lower() + a[1:], {}).setdefault(b, (name, i))
    for k, v in seen.items():
        if len(v) > 1 and any(x[0] in names for x in v.values()):
            bad.append(("I", "-", 0, f"«{k[:70]}» has {len(v)} renderings: {list(v.values())[:3]}"))
    grp = {}
    for n in GROUPS:
        pl, ml = nonempty(PALI / n), nonempty(DISK / n)
        for i, (p, m) in enumerate(zip(pl, ml), 1):
            ps, ms = split_p(p), split_m(m)
            if len(ps) == len(ms):
                for a, b in zip(ps, ms):
                    grp.setdefault(a[:1].lower() + a[1:], {}).setdefault(b, (n, i))
    g_n = g_ok = 0
    GROUP_DIFF.clear()
    for k, v in seen.items():
        mine = {b: x for b, x in v.items() if x[0] in names}
        if mine and k in grp:
            g_n += 1
            if set(mine) & set(grp[k]):
                g_ok += 1
            else:
                GROUP_DIFF.append((k, list(mine.items())[0], list(grp[k].items())[0]))
    stats["G"] = f"{g_ok} / {g_n}"
    # T: tables
    for st, my in CONDS_MY.items():
        stats["T"] += 1
        if F.N.get(st) != my:
            bad.append(("T", "-", 0, f"condition {st}: module «{F.N.get(st)}» vs checker «{my}»"))
    for w, n in COUNT_PI.items():
        if w in F.COUNT:
            stats["T"] += 1
            if F.COUNT[w] != NUM_MY[n] + "ခု":
                bad.append(("T", "-", 0, f"count {w}"))
    pos_of = {}

    for n_, v in Qm.NEG_LOG.items():
        stats["T"] += 1
        base = n_[2:]
        if base not in Qm.ATOM or v != neg_my(Qm.ATOM[base][1]):
            bad.append(("T", "-", 0, f"negated atom {n_}: «{v}» vs checker «{neg_my(Qm.ATOM.get(base, ('', ''))[1])}»"))
    for my_, k in Qm.KEYS.items():
        stats["T"] += 1
        if "zqw" in my_ or not my_:
            bad.append(("T", "-", 0, f"key value {k}"))
    # R: every positive atom value used in these chapters is witnessed in a finished chapter (or pi-1 FINAL)
    used = set()
    for name, i, p, m in pairs_all:
        for _, _, s, _ in TT.atoms(ID.sub("", p)):
            used.add(s)
    wit_lines = []
    for n in GROUPS:
        wit_lines += list(zip(nonempty(PALI / n), nonempty(DISK / n)))
    final_vals = set()                                 # the values the engines read from the pi-1 … pi-6 FINAL rails
    for w in (Qm.WA, Qm.WB):
        for pali, (book, bid, my) in w.F.WITNESS.items():
            final_vals.add(re.sub(r" သဘောတရား(?:များ)?$", "", my))
    reuse_n = reuse_ok = 0
    for s in sorted(used):
        if s in Qm.NEG_LOG or (s.startswith("na ") and s[3:] in Qm.ATOM):
            continue                                   # a «na-» atom: checked by T (the negation rule)
        cls, v = Qm.ATOM[s]
        rx = re.compile(r"(?<![\wāīūṃṅñṭḍṇḷ])[" + s[0].upper() + s[0] + "]" + re.escape(s[1:]).replace(r"\ ", " ")
                        + r"(?:" + TT.ends[cls] + r") (?:ca )?dhamm")
        hit = any(rx.search(pp) and (v + " သဘောတရား" in mm or v + "၊ " in mm) for pp, mm in wit_lines)
        if not hit and s.endswith("dhammadhamm"):        # the noun is inside the compound
            rx2 = re.compile(r"(?<![\wāīūṃṅñṭḍṇḷ])[" + s[0].upper() + s[0] + "]" + re.escape(s[1:]) + r"(?:" + TT.ends[cls] + r")")
            hit = any(rx2.search(pp) and v + " သဘောတရား" in mm for pp, mm in wit_lines)
        if not hit:
            hit = v in final_vals                          # a pi-1 FINAL Mātikā value (WITNESS)
        if not hit:                                        # the pi-1 FINAL rails text («… သဘောတရား»)
            hit = (v + " သဘောတရား") in PI1_TEXT
        reuse_n += 1
        if hit:
            reuse_ok += 1
        else:
            bad.append(("R", "-", 0, f"atom «{s}» = «{v}» not witnessed in a finished chapter"))
    for w in (Qm.WA, Qm.WB):
        for pali, (book, bid, my) in w.F.WITNESS.items():
            f_, pseg, mseg = w.F.FINAL.SEG[book][bid]
            if my not in " ".join(mseg):
                bad.append(("R", "-", 0, f"witness «{pali}» no longer in pi-{book} {bid}"))
    # R2: the term chains of these chapters whose Pāli also stands in a finished chapter («… dhamm»)
    gl = {}
    for n in GROUPS:
        for pp, mm in zip(nonempty(PALI / n), nonempty(DISK / n)):
            for w_ in set(re.findall(r"[\wāīūṃṅñṭḍṇḷ]+", pp.lower())):
                gl.setdefault(w_, []).append((pp.lower(), mm))
    comb, comb_n, comb_ok = {}, 0, 0
    for name, i, p, m in pairs_all:
        if p.startswith("#"):
            continue
        for pal, v in TT.chains(re.sub(r"\([^()]*\)", "", ID.sub("", p)), name.startswith(TWO_SETS)):
            if " " in pal and "၊" in v:
                comb.setdefault(pal.lower(), v)
    for pal, v in sorted(comb.items()):
        ws = re.findall(r"[\wāīūṃṅñṭḍṇḷ]+", pal)
        cands = min((gl.get(w_, []) for w_ in ws), key=len)
        rx = re.compile(r"(?<![\wāīūṃṅñṭḍṇḷ])" + re.escape(pal) + r" (?:ca )?dhamm")
        hits = [mm for pp, mm in cands
                if any(not re.search(r"(?:\bca|ceva) $", pp[:x.start()]) for x in rx.finditer(pp))]
        if not hits:
            continue
        comb_n += 1
        if any(v in mm for mm in hits):
            comb_ok += 1
        else:
            bad.append(("R", "-", 0, f"combined term «{pal}» = «{v}» differs from the finished chapters"))
    stats["R2"] = f"{comb_ok} / {comb_n}"
    import reuse_index as RI
    idx = RI.index()
    sent_n = sent_ok = 0
    for name, i, p, m in pairs_all:
        ps, ms = split_p(p), split_m(m)
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
    stats["R"] = reuse_n
    src = {(n_, i): p for n_, i, p, m in pairs_all}
    for b_ in bad:
        print(*b_, "|", src.get((b_[1], b_[2]), "")[:90])
    print("checked:", ", ".join(f"{k} {v}" for k, v in stats.items() if k not in ("R", "G", "R2")))
    print(f"reuse test: terms {reuse_ok} / {reuse_n} witnessed in the finished chapters; "
          f"sentences {sent_ok} / {sent_n} identical with pi-1 … pi-6")
    print(f"combined terms (stacked chains) identical with the finished chapters: {stats['R2']}")
    print(f"identity with the finished groups 1-00 … 4-14, 5-01 … 5-04: {stats['G']} sentences identical "
          f"(the differences are listed with --groups)")
    if "--groups" in sys.argv:
        for k, a, b in GROUP_DIFF:
            print("G |", k[:110], "\n    mine:", a[0][:200], a[1], "\n    grp: ", b[0][:200], b[1])
    print(f"{len(bad)} mismatches")
    return mk, bad


F1, F2, F3, F4, F5, F6, F7, F8 = MINE
MUT = [  # (file, old, new, what)
    (F1, "အမြစ်ဟူသော အကြောင်း၌ ဆယ့်သုံးခု", "အမြစ်ဟူသော အကြောင်း၌ ဆယ့်နှစ်ခု", "count"),
    (F4, "အမြစ် ရှိသည် မဟုတ်သော သဘောတရားကို မှီ၍ အမြစ် ရှိသော သဘောတရားသည်",
     "အမြစ် ရှိသော သဘောတရားကို မှီ၍ အမြစ် ရှိသော သဘောတရားသည်", "polarity"),
    (F1, "ကုသိုလ်၊ သာယာသော ခံစားမှုနှင့် ယှဉ်တွဲသော သဘောတရားကို မှီ၍ ကုသိုလ် မဟုတ်သော၊",
     "သာယာသော ခံစားမှုနှင့် ယှဉ်တွဲသော၊ ကုသိုလ် သဘောတရားကို မှီ၍ ကုသိုလ် မဟုတ်သော၊", "stack order"),
    (F4, "အမြစ် ရှိသည် မဟုတ်သော သဘောတရားကို မှီ၍ အမြစ် ရှိသော သဘောတရားသည်",
     "အမြစ် ရှိသော သဘောတရားကို မှီ၍ အမြစ် ရှိသည် မဟုတ်သော သဘောတရားသည်", "term order"),
    (F4, "အမြစ်ဟူသော အကြောင်းကြောင့်", "အာရုံဟူသော အကြောင်းကြောင့်", "condition"),
    (F3, "အစုအဝေး တစ်ပါးကို မှီ၍ အစုအဝေး သုံးပါး", "အစုအဝေး တစ်ပါးကို မှီ၍ အစုအဝေး နှစ်ပါး", "khandha count"),
    (F4, "(3) ^7-70-57", "(2) ^7-70-57", "digits"),
    (F8, "အမြစ် မဟုတ်သည် မဟုတ်သော", "အမြစ် မဟုတ်သော", "double negation"),
    (F5, "##### 1-1. အမြစ် နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ", "##### 1-1. အမြစ် နှစ်မျိုးတွဲနှင့် ကုသိုလ် နှစ်မျိုးတွဲ",
     "heading name"),
    (F8, "အမြစ် ဖြစ်ခြင်းနှင့် အမြစ် ရှိခြင်း နှစ်မျိုးတွဲ", "အမြစ် ဖြစ်ခြင်းနှင့် အမြစ် ရှိခြင်း သုံးမျိုးတွဲ", "dyad name"),
    (F1, "(အကျဉ်းချုပ်။)", "(အကျဉ်းချုပ်)", "recurring note"),
    (F2, "မှီ၍ ", "မှီ၍ – ", "dash"),
    (F5, "(မမြင်နိုင်သော်လည်း ထိခိုက်မှု ရှိသော သဘောတရား၌ သုံးခုသာ။)",
     "(မမြင်နိုင်သော်လည်း ထိခိုက်မှု ရှိသည် မဟုတ်သော သဘောတရား၌ သုံးခုသာ။)", "note term"),
    (F2, "ပြုပြင်ဖန်တီးထားခြင်း မရှိသော သဘောတရားသည် အကြောင်း မရှိသော သဘောတရားနှင့် တူသည်",
     "အကြောင်း မရှိသော သဘောတရားသည် ပြုပြင်ဖန်တီးထားခြင်း မရှိသော သဘောတရားနှင့် တူသည်", "note term swap"),
]


def mutate():
    """each planted error in its own copy (pi-7-my/chk-mut-ch5-13-20/<n>/), checked in parallel batches of 7"""
    root = HERE / "chk-mut-ch5-13-20"
    if root.exists():
        shutil.rmtree(root)
    caught = 0
    jobs = []
    for k, (f, old, new, what) in enumerate(MUT):
        tmp = root / str(k)
        tmp.mkdir(parents=True)
        for n in MINE:
            shutil.copy(OUT / n, tmp / n)
        t = (tmp / f).read_text(encoding="utf-8")
        if old not in t:
            print("mutation not applicable:", what)
            continue
        (tmp / f).write_text(t.replace(old, new, 1), encoding="utf-8")
        jobs.append((what, [sys.executable, "-I", "-X", "utf8", str(HERE / "check_ch5-13-20.py"), f[:4], "--out",
                            str(tmp)]))
    for i in range(0, len(jobs), 7):
        procs = [(w, subprocess.Popen(c, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True))
                 for w, c in jobs[i:i + 7]]
        for what, pr in procs:
            so, se = pr.communicate()
            last = so.strip().splitlines()[-1] if so.strip() else se[-200:]
            bad_lines = [l for l in so.splitlines() if l[:2] in ("S ", "C ", "O ", "P ", "N ", "I ", "T ", "R ")]
            ok = pr.returncode != 0
            caught += ok
            print(f"{what:16} -> {'caught' if ok else 'MISSED'} ({last}; {bad_lines[0][:90] if bad_lines else ''})")
    shutil.rmtree(root)
    print(f"{caught} / {len(MUT)} planted errors caught")
    return len(MUT) - caught


def pe_check(names):
    tmp = HERE / "chk-pe" / "ch5-13-20"
    tmp.mkdir(parents=True, exist_ok=True)
    call = []
    for n in names:
        folded = tmp / n
        folded.write_text((PALI / n).read_text(encoding="utf-8-sig").replace("…Pe…", "…pe…"), encoding="utf-8")
        call += [str(folded), str(OUT / n)]
    r = subprocess.run([sys.executable, "-I", "-X", "utf8", str(HERE.parent / "pi-3-mr/check_text.py")] + call)
    shutil.rmtree(tmp)
    try:
        (HERE / "chk-pe").rmdir()                    # only if no other agent's folder is in it
    except OSError:
        pass
    return r.returncode


if __name__ == "__main__":
    mk, bad = check(NAMES, OUT)
    fail = bool(bad)
    if "--pe" in FLAGS:
        fail |= bool(pe_check(NAMES))
    if "--mutate" in FLAGS:
        fail |= bool(mutate())
    sys.exit(1 if fail else 0)
