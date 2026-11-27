"""Per-line check of the Burmese pi-7 chapters 4-02 … 4-09 (the first DUKATIKA chapters: a dyad term combined with a
triad term on one noun) against the Pāli (adapted from check_ch3-01-02.py; independent of the generator's frames: the
condition, count and negation tables and the term regexes are typed here again; the dyad / triad / name values are
a frozen copy, compared with the generator's (T); the active dyad-triad pair of a line is read from the Pāli headings).

usage: python3 -I -X utf8 check_ch4-02-09.py [chapter ...] [--out DIR] [--mutate] [--sample] [--pe] [--groups]
Checks, line by line (Pāli line i <-> Burmese line i):
  S  structure: equal non-empty lines, heading #-level, block IDs, no «?» «।» «:-», no Latin left outside variants;
  P  polarity: «မဟုတ်» count and the «မ…» negatives expected from the Pāli tokens (NEG_*);
  C  conditions: the sequence of conditions (stem + polarity) named in the Pāli = the sequence in the Burmese;
  O  term order: the sequence of combined terms (dyad term + triad term) in the Pāli = the sequence in the Burmese
     (conditioning -> conditioned); the dyad-triad headings, the pada headings and the colophons carry their names;
  N  numbers: counts «… ခု», khandha numbers «… ပါး», group numbers «… မျိုးတွဲ», digits «(n)»;
  I  identity: identical Pāli sentences have identical Burmese sentences (these chapters and the approved sample);
     against the finished pi-7 groups the agreement is counted (G) and the differences listed with --groups;
  T  tables: the module's condition names and counts, and the generator's terms and names = this checker's copy;
  R  reuse: every value taken from pi-1 … pi-6 (WITNESS) is re-read from the FINAL rails and found in every line
     whose Pāli contains its Pāli; sentences that occur in pi-1 … pi-6 are identical.
--sample  regenerates the approved sample (1-00, 1-02) in memory with this generator's extensions (world A) and
          requires it to be identical to the files on disk.
--mutate  plants errors in copies (pi-7-my/chk-mut-ch4-02-09/, deleted afterwards); each must be caught.
--pe      runs pi-3-mr/check_text.py on a «…Pe…»-folded copy of the Pāli in pi-7-my/chk-pe/ch4-02-09/ (deleted).
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
SAMPLE = ["1-00-paccaya.md", "1-02-vedanattika.md"]
MINE = ["4-02-dukatika-hetuduka.md", "4-03-dukatika-sahetukaduka.md", "4-04-dukatika-sappaccayaduka.md",
        "4-05-dukatika-asavaduka.md", "4-06-dukatika-sannojanaduka.md", "4-07-dukatika-ganthaduka.md",
        "4-08-dukatika-nivaranaduka.md", "4-09-dukatika-paramasaduka.md"]
# the finished groups (identity, informational): every pi-7 chapter on disk except these and 4-01 (in progress)
GROUPS = sorted(p.name for p in (ROOT / "AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters").glob("*.md")
                if p.name[:4] not in ("4-01", "4-02", "4-03", "4-04", "4-05", "4-06", "4-07", "4-08", "4-09")
                and p.name not in ("1-00-paccaya.md", "1-02-vedanattika.md", "preamble.md"))
_args = sys.argv[1:]
FLAGS = {a for a in _args if a in ("--mutate", "--sample", "--pe", "--groups")}
_args = [a for a in _args if a not in FLAGS]
if "--out" in _args:
    OUT = pathlib.Path(_args[_args.index("--out") + 1]).resolve()
    del _args[_args.index("--out"):_args.index("--out") + 2]
NAMES = _args or MINE
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
            "tīṇipi": 3, "navapi": 9, "dvīsu": 2, "dvīsupi": 2, "tīsupi": 3, "dvinnampi": 2, "ekāyeva": 1, "ekoyeva": 1}
KH_PI = {"eko": 1, "ekaṃ": 1, "ekassa": 1, "dve": 2, "dvinnaṃ": 2, "tayo": 3, "tiṇṇannaṃ": 3, "tiṇṇaṃ": 3,
         "cattāro": 4, "pañcannaṃ": 5}
GROUP_PI = {"catukk": 4, "pañcak": 5, "chakk": 6, "sattak": 7, "aṭṭhak": 8, "navak": 9, "dasak": 10, "ekādasak": 11,
            "dvādasak": 12, "terasak": 13, "tevīsak": 23, "catuvīsak": 24}
MULA_PI = {"ekamūlak": 1, "dumūlak": 2, "timūlak": 3, "catumūlak": 4, "pañcamūlak": 5, "tevīsatimūlak": 23}
# notes / headings whose conditions the regexes below cannot see: Pāli -> (Burmese, [(stem, neg)])
# notes / headings whose conditions the regexes cannot see: Pāli -> (Burmese, [(stem, neg)])
NOTE_PAIRS = {
    "*Hetu-ārammaṇapaccayādi*": ("*အမြစ်ဟူသော အကြောင်းနှင့် အာရုံဟူသော အကြောင်း စသည်*",
                                 [("hetu", False), ("ārammaṇa", False)]),
    "*Nahetu-naārammaṇapaccayādi*": ("*အမြစ်ဟူသော အကြောင်း မဟုတ်ခြင်းနှင့် အာရုံဟူသော အကြောင်း မဟုတ်ခြင်း စသည်*",
                                     [("hetu", True), ("ārammaṇa", True)]),
    "*Nahetunaārammaṇapaccayādi*": ("*အမြစ်ဟူသော အကြောင်း မဟုတ်ခြင်းနှင့် အာရုံဟူသော အကြောင်း မဟုတ်ခြင်း စသည်*",
                                    [("hetu", True), ("ārammaṇa", True)]),     # source slip: no hyphen
    # source slips «kamma nava», «avigata nava» (read as «kamme / avigate nava»)
    "kamma nava": ("ကံဟူသော အကြောင်း၌ ကိုးခု", [("kamma", False)]),
    "avigata nava": ("မပျောက်ကွယ်ခြင်းဟူသော အကြောင်း၌ ကိုးခု", [("avigata", False)]),
}
NOTE_CONDS_SAMPLE = {}
HEAD_CONDS = {}
# negation: Pāli token regex -> number of «မဟုတ်» / of «မ…» negatives expected in the Burmese
NEG_SANDHI = "|".join(x[:-1] for x in STEMS if x.endswith("a"))
_LOCS = ["hetuyā", "adhipatiyā", "atthiyā", "natthiyā"] + [x[:-1] + "e" for x in STEMS
                                                         if x not in ("hetu", "adhipati", "atthi", "natthi")]
NEG_NOT = [(r"(?i)(?<![\wāīūṃṅñṭḍṇḷ])(?:na|no)(?:" + "|".join(sorted(STEMS + _LOCS, key=len, reverse=True)) + "|(?:"
            + NEG_SANDHI + r")(?=ādi))", 1),
           (r"(?<=samanantara)nasahajāta|(?<=vipāka)naāhāra", 1),
           (r"(?<![\wāīūṃṅñṭḍṇḷ])na (?=§C§|\w+paccayena paccayo)", 1),
           (r"(?<![\wāīūṃṅñṭḍṇḷ])na (?=(?:" + "|".join(_LOCS) + r") \w|\w+paccayā)", 1),   # «na adhipatiyā …» apart
           (r"(?i)(?<!kiriy)ābyākat|(?<![\wāīūṃṅñṭḍṇḷ])[Aa]byākat", 2),
           (r"(?i)(?<![\wāīūṃṅñṭḍṇḷ])arūp(?:ino|īnaṃ)", 1), (r"(?i)kiriyābyākat", 2),
           (r"(?i)nevasaññānāsaññāyatan", 2), (r"(?i)anattato", 1), (r"(?<![\wāīūṃṅñṭḍṇḷ])nādhipati", 1),
           (r"(?i)nevavipākanavipākadhamma", 2),
           (r"(?i)nevadassanena nabhāvanāya", 2), (r"(?i)nevadassanena(?=…)", 2),
           (r"(?i)nevācayagāmināpacayagām|nevācayagāmīnāpacayagām", 2), (r"(?i)nevasekkhanāsekkh|nevasekkhānāsekkh", 2),
           # the dyads of 3-01 … 3-02: nahetū (the long ū is not the condition stem), «… ceva na ca hetu», arūpī
           (r"(?i)(?<![\wāīūṃṅñṭḍṇḷ])nahetū", 1), (r"(?<![\wāīūṃṅñṭḍṇḷ])na ca het", 1),
           (r"(?i)(?<![\wāīūṃṅñṭḍṇḷ])arūp(?:ī|iṃ|iñca|issa|inā|icittasamaṅgissa)(?![\wāīūṃṅñṭḍṇḷ])", 1),
           (r"(?i)arūpameva|arūpapañh", 1),
           # 3-03 … 3-08 clusters: «no X» (term), «… ceva no ca X»
           (r"(?i)(?<![\wāīūṃṅñṭḍṇḷ])no(?:āsav|saññojan|ganth|nīvaraṇ|parāmās)", 1),
           (r"(?<![\wāīūṃṅñṭḍṇḷ])no ca (?:āsav|saññojan|ganth|nīvaraṇ|parāmās)", 1),
           # 4-02: the pada heading written as one word; the heading slip «Nahetunaārammaṇa-» (no hyphen)
           (r"(?i)nevadassanenanabhāvanāya", 2), (r"(?<=[Nn]ahetu)naārammaṇ", 1)]
NEG_MA = [(r"(?i)adukkhamasukh", 2), (r"(?i)(?<![\wāīūṃṅñṭḍṇḷ])(?:no)?natthi(?:paccay|yā|\b)", 1),
          (r"(?i)(?<![\wāīūṃṅñṭḍṇḷ])(?:no)?avigat", 1), (r"(?i)(?<![\wāīūṃṅñṭḍṇḷ])ahetuk", 1), (r"(?i)aniccato", 1),
          (r"(?i)asamm(?:uyh|oh)antena", 1), (r"(?<=vigat)āvigat", 1), (r"na labbhati", 1), (r"(?<![\wāīūṃṅñṭḍṇḷ])na kātabbaṃ", 1), (r"(?i)natthi(?=vigat)", 1),
          (r"(?i)(?<![\wāīūṃṅñṭḍṇḷ])arūpe(?![\wāīūṃṅñṭḍṇḷ])", 1), (r"(?i)ākāsānañcāyatan", 1), (r"(?i)viññāṇañcāyatan", 1),
          (r"(?i)ākiñcaññāyatan", 1), (r"(?i)nevasaññānāsaññāyatan", 1),
          (r"(?i)anupādinnupādāniy", 1), (r"(?i)anupādinnaanupādāniy", 2),
          (r"(?i)asaṃkiliṭṭhasaṃkilesik|asaṅkiliṭṭhasaṃkilisik", 1), (r"(?i)asaṃkiliṭṭhaasaṃkilesik", 2),
          (r"(?i)anuppann", 1), (r"(?i)ṭhānāṭhān", 1), (r"\(Avipākaṃ", 1),
          (r"(?i)ninnānaṃ", 1), (r"na likhitā", 1), (r"na samenti", 1),
          # the dyads of 3-01 … 3-02 and their nouns: alobha / adosa / amoha «… မရှိခြင်း», nahetu ahetuka,
          # appaccaya / asaṅkhata / appaṭigha «… မရှိ», anidassana «မမြင်…», kenaci naviññeyya «မသိ…»
          (r"(?i)(?<![\wāīūṃṅñṭḍṇḷ])a(?:lobh|dos|moh)", 1), (r"(?i)nahetuahetuk", 1),
          (r"(?i)(?<![\wāīūṃṅñṭḍṇḷ])(?:appaccay|asaṅkhat|appaṭigh|anidassan)", 1), (r"(?i)na ?viññeyy", 1),
          (r"(?i)arūpeyeva", 1), (r"(?i)ninnānākaraṇ", 1),
          # 3-03 … 3-08 clusters: a-S «… မဖြစ်နိုင်သော»
          (r"(?i)(?<![\wāīūṃṅñṭḍṇḷ])(?:anāsav|asaññojaniy|aganthaniy|anīvaraṇiy|aparāmaṭṭh)", 1),
          # the triads of 2-01 … 2-17 (as their checkers): avitakka-, appamāṇa, aniyata, anidassana-appaṭigha
          (r"(?i)avitakkavicāramatt", 1), (r"(?i)avitakkaavicār", 2),
          (r"(?i)(?:(?<![\wāīūṃṅñṭḍṇḷ])|(?<=ṇa))appamāṇ", 1), (r"(?i)(?<![\wāīūṃṅñṭḍṇḷ])aniyat", 1),
          (r"(?i)anidassanaappaṭigh", 1), (r"na labbhanti", 1),
          (r"(?i)(?<![\wāīūṃṅñṭḍṇḷ])avijjā", 1)]                # avijjā «အမှန်ကို မသိမှု» (3-03 … 3-08)
MA_MY = re.compile(r"မ(?:နာကျင်|သာယာ|ရှိ|ပျောက်ကွယ်|မြဲ|ရောထွေး|တွေ့ရ|ထည့်ရ|ဖြစ်|ညစ်နွမ်း|ပါဝင်|ရေးထား|ညီ|မြင်|သိ|ကျိန်းသေ)")


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
    # the dyad-triad names (headings, colophons) and the dyad / cluster names inside notes are not conditions
    s = re.sub(r"(?<![\wāīūṃṅñṭḍṇḷ])\w+duka-?\w*ttik\w*|\w+gocchaka\w*|\w+duk(?:a|e)\w*", lambda m: " " * len(m[0]), s)
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
    # a bare locative (or a run of them) ending a counting fragment before «…» («kamme…pe… magge cattāri»)
    for m in re.finditer(r"(?i)(?:(?<=, )|^)((?:(?:na|no)?(?:" + _la + r") )*(?:na|no)?(?:" + _la + r"))(?=…)", s):
        for w_ in re.finditer(r"\S+", m.group(1)):
            wd, pos = w_.group(0), m.start() + w_.start()
            neg = bool(re.match(r"(?i)n[ao]", wd)) and wd.lower()[2:] in loc
            st = loc[wd.lower()[2:] if neg else wd.lower()]
            if not any(abs(f[0] - pos) < 1 for f in found):
                found.append((pos, st, neg))
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
    for m in re.finditer(r"(?<![^\s(“*…])(" + NAME_ALT + r")ဟူသော အကြောင်း((?:ကြောင့်)? မဟုတ်)?", s):
        found.append((m.start(), MY_NAME[m.group(1)], bool(m.group(2))))
    for m in GH_MY.finditer(s):
        for k, nm in enumerate(m.group(1).split("၊ ")):
            found.append((m.start() + k / 100, MY_NAME[nm], False))
    for m in re.finditer(r"(?<![^\s(])(" + NAME_ALT + r")((?: မဟုတ်ခြင်း)?)နှင့် တူ(?:ကြ)?(?:သည်|သော|အောင်)", s):
        found.append((m.start(), MY_NAME[m.group(1)], bool(m.group(2))))
    found.sort()
    return [(st, ng) for _, st, ng in found]



# ----------------------------------------------------------------------------- frozen term tables (Burmese)
DYAD_MY = {'Ganthadukaṃ': [('ganthdk', 'အထုံး ဖြစ်သော'), ('noganth', 'အထုံး မဟုတ်သော')],
 'Ganthaganthaniyadukaṃ': [('ganthganthaniydk', 'အထုံးလည်း ဖြစ်၊ အထုံး၏ အာရုံလည်း ဖြစ်နိုင်သော'),
                           ('ganthaniynoganthdk', 'အထုံး၏ အာရုံ ဖြစ်နိုင်သော်လည်း အထုံး မဟုတ်သော')],
 'Ganthaganthasampayuttadukaṃ': [('ganthganthsampdk', 'အထုံးလည်း ဖြစ်၊ အထုံးနှင့်လည်း ယှဉ်တွဲသော'),
                                 ('ganthsampnoganthdk', 'အထုံးနှင့် ယှဉ်တွဲသော်လည်း အထုံး မဟုတ်သော')],
 'Ganthaniyadukaṃ': [('ganthaniy', 'အထုံး၏ အာရုံ ဖြစ်နိုင်သော'), ('aganthaniy', 'အထုံး၏ အာရုံ မဖြစ်နိုင်သော')],
 'Ganthasampayuttadukaṃ': [('ganthasampayutt', 'အထုံးနှင့် ယှဉ်တွဲသော'),
                           ('ganthavippayutt', 'အထုံးနှင့် ကင်းကွာသော')],
 'Ganthavippayuttaganthaniyadukaṃ': [('ganthvippganthaniydk', 'အထုံးနှင့် ကင်းကွာသော်လည်း အထုံး၏ အာရုံ ဖြစ်နိုင်သော'),
                                     ('ganthvippaganthaniydk', 'အထုံးနှင့် ကင်းကွာ၊ အထုံး၏ အာရုံ မဖြစ်နိုင်သော')],
 'Hetudukaṃ': [('hetudk', 'အမြစ် ဖြစ်သော'), ('nahetudk', 'အမြစ် မဟုတ်သော')],
 'Hetuhetusampayuttadukaṃ': [('hetuhetusampdk', 'အမြစ်လည်း ဖြစ်၊ အမြစ်နှင့်လည်း ယှဉ်တွဲသော'),
                             ('hetusampnahetudk', 'အမြစ်နှင့် ယှဉ်တွဲသော်လည်း အမြစ် မဟုတ်သော')],
 'Hetusahetukadukaṃ': [('hetusahetukdk', 'အမြစ်လည်း ဖြစ်၊ အမြစ်လည်း ရှိသော'),
                       ('sahetukanahetudk', 'အမြစ် ရှိသော်လည်း အမြစ် မဟုတ်သော')],
 'Hetusampayuttadukaṃ': [('hetusampayutt', 'အမြစ်နှင့် ယှဉ်တွဲသော'), ('hetuvippayutt', 'အမြစ်နှင့် ကင်းကွာသော')],
 'Kenaciviññeyyadukaṃ': [('kenaci viññeyy', 'တစ်စုံတစ်ခုသော စိတ်ဖြင့် သိနိုင်သော'),
                         ('kenaci naviññeyy', 'တစ်စုံတစ်ခုသော စိတ်ဖြင့် မသိနိုင်သော')],
 'Lokiyadukaṃ': [('lokiy', 'လောကနှင့် သက်ဆိုင်သော'), ('lokuttar', 'လောကကို ကျော်လွန်သော')],
 'Nahetusahetukadukaṃ': [('nahetusahetuk', 'အမြစ် မဟုတ်သော်လည်း အမြစ် ရှိသော'),
                         ('nahetuahetuk', 'အမြစ် မဟုတ်၊ အမြစ် မရှိသော')],
 'Nīvaraṇadukaṃ': [('nīvaraṇdk', 'အတားအဆီး ဖြစ်သော'), ('nonīvaraṇ', 'အတားအဆီး မဟုတ်သော')],
 'Nīvaraṇanīvaraṇasampayuttadukaṃ': [('nīvaraṇanīvaraṇasampdk', 'အတားအဆီးလည်း ဖြစ်၊ အတားအဆီးနှင့်လည်း ယှဉ်တွဲသော'),
                                     ('nīvaraṇasampnonīvaraṇdk', 'အတားအဆီးနှင့် ယှဉ်တွဲသော်လည်း အတားအဆီး မဟုတ်သော')],
 'Nīvaraṇanīvaraṇiyadukaṃ': [('nīvaraṇanīvaraṇiydk', 'အတားအဆီးလည်း ဖြစ်၊ အတားအဆီး၏ အာရုံလည်း ဖြစ်နိုင်သော'),
                             ('nīvaraṇiyanonīvaraṇdk', 'အတားအဆီး၏ အာရုံ ဖြစ်နိုင်သော်လည်း အတားအဆီး မဟုတ်သော')],
 'Nīvaraṇasampayuttadukaṃ': [('nīvaraṇasampayutt', 'အတားအဆီးနှင့် ယှဉ်တွဲသော'),
                             ('nīvaraṇavippayutt', 'အတားအဆီးနှင့် ကင်းကွာသော')],
 'Nīvaraṇavippayuttanīvaraṇiyadukaṃ': [('nīvaraṇavippnīvaraṇiy',
                                        'အတားအဆီးနှင့် ကင်းကွာသော်လည်း အတားအဆီး၏ အာရုံ ဖြစ်နိုင်သော'),
                                       ('nīvaraṇavippanīvaraṇiy',
                                        'အတားအဆီးနှင့် ကင်းကွာ၊ အတားအဆီး၏ အာရုံ မဖြစ်နိုင်သော')],
 'Nīvaraṇiyadukaṃ': [('nīvaraṇiy', 'အတားအဆီး၏ အာရုံ ဖြစ်နိုင်သော'), ('anīvaraṇiy', 'အတားအဆီး၏ အာရုံ မဖြစ်နိုင်သော')],
 'Parāmaṭṭhadukaṃ': [('parāmaṭṭh', 'မှားယွင်းသော ယူဆမှု၏ အာရုံ ဖြစ်နိုင်သော'),
                     ('aparāmaṭṭh', 'မှားယွင်းသော ယူဆမှု၏ အာရုံ မဖြစ်နိုင်သော')],
 'Parāmāsadukaṃ': [('parāmāsdk', 'မှားယွင်းသော ယူဆမှု ဖြစ်သော'), ('noparāmās', 'မှားယွင်းသော ယူဆမှု မဟုတ်သော')],
 'Parāmāsaparāmaṭṭhadukaṃ': [('parāmāsaparāmaṭṭhdk',
                              'မှားယွင်းသော ယူဆမှုလည်း ဖြစ်၊ မှားယွင်းသော ယူဆမှု၏ အာရုံလည်း ဖြစ်နိုင်သော'),
                             ('parāmaṭṭhanoparāmāsdk',
                              'မှားယွင်းသော ယူဆမှု၏ အာရုံ ဖြစ်နိုင်သော်လည်း မှားယွင်းသော ယူဆမှု မဟုတ်သော')],
 'Parāmāsasampayuttadukaṃ': [('parāmāsasampayutt', 'မှားယွင်းသော ယူဆမှုနှင့် ယှဉ်တွဲသော'),
                             ('parāmāsavippayutt', 'မှားယွင်းသော ယူဆမှုနှင့် ကင်းကွာသော')],
 'Parāmāsavippayuttaparāmaṭṭhadukaṃ': [('parāmāsavippparāmaṭṭh',
                                        'မှားယွင်းသော ယူဆမှုနှင့် ကင်းကွာသော်လည်း မှားယွင်းသော ယူဆမှု၏ အာရုံ '
                                        'ဖြစ်နိုင်သော'),
                                       ('parāmāsavippaparāmaṭṭh',
                                        'မှားယွင်းသော ယူဆမှုနှင့် ကင်းကွာ၊ မှားယွင်းသော ယူဆမှု၏ အာရုံ '
                                        'မဖြစ်နိုင်သော')],
 'Rūpīdukaṃ': [('rūpdk', 'ရုပ် ဖြစ်သော'), ('arūpdk', 'ရုပ် မဟုတ်သော')],
 'Sahetukadukaṃ': [('sahetuk', 'အမြစ် ရှိသော'), ('ahetuk', 'အမြစ် မရှိသော')],
 'Sanidassanadukaṃ': [('sanidassan', 'မြင်နိုင်သော'), ('anidassan', 'မမြင်နိုင်သော')],
 'Sappaccayadukaṃ': [('sappaccay', 'အကြောင်း ရှိသော'), ('appaccay', 'အကြောင်း မရှိသော')],
 'Sappaṭighadukaṃ': [('sappaṭigh', 'ထိခိုက်မှု ရှိသော'), ('appaṭigh', 'ထိခိုက်မှု မရှိသော')],
 'Saññojanadukaṃ': [('saññojandk', 'နှောင်ကြိုး ဖြစ်သော'), ('nosaññojan', 'နှောင်ကြိုး မဟုတ်သော')],
 'Saññojanasampayuttadukaṃ': [('saññojanasampayutt', 'နှောင်ကြိုးနှင့် ယှဉ်တွဲသော'),
                              ('saññojanavippayutt', 'နှောင်ကြိုးနှင့် ကင်းကွာသော')],
 'Saññojanasaññojanasampayuttadukaṃ': [('saññojansaññojansampdk',
                                        'နှောင်ကြိုးလည်း ဖြစ်၊ နှောင်ကြိုးနှင့်လည်း ယှဉ်တွဲသော'),
                                       ('saññojansampnosaññojandk',
                                        'နှောင်ကြိုးနှင့် ယှဉ်တွဲသော်လည်း နှောင်ကြိုး မဟုတ်သော')],
 'Saññojanasaññojaniyadukaṃ': [('saññojansaññojaniydk', 'နှောင်ကြိုးလည်း ဖြစ်၊ နှောင်ကြိုး၏ အာရုံလည်း ဖြစ်နိုင်သော'),
                               ('saññojaniynosaññojandk',
                                'နှောင်ကြိုး၏ အာရုံ ဖြစ်နိုင်သော်လည်း နှောင်ကြိုး မဟုတ်သော')],
 'Saññojanavippayuttasaññojaniyadukaṃ': [('saññojanvippsaññojaniydk',
                                          'နှောင်ကြိုးနှင့် ကင်းကွာသော်လည်း နှောင်ကြိုး၏ အာရုံ ဖြစ်နိုင်သော'),
                                         ('saññojanvippasaññojaniydk',
                                          'နှောင်ကြိုးနှင့် ကင်းကွာ၊ နှောင်ကြိုး၏ အာရုံ မဖြစ်နိုင်သော')],
 'Saññojaniyadukaṃ': [('saññojaniy', 'နှောင်ကြိုး၏ အာရုံ ဖြစ်နိုင်သော'),
                      ('asaññojaniy', 'နှောင်ကြိုး၏ အာရုံ မဖြစ်နိုင်သော')],
 'Saṅkhatadukaṃ': [('saṅkhat', 'ပြုပြင်ဖန်တီးထားသော'), ('asaṅkhat', 'ပြုပြင်ဖန်တီးထားခြင်း မရှိသော')],
 'Sāsavadukaṃ': [('sāsav', 'စိတ်အစွန်းအထင်း၏ အာရုံ ဖြစ်နိုင်သော'),
                 ('anāsav', 'စိတ်အစွန်းအထင်း၏ အာရုံ မဖြစ်နိုင်သော')],
 'Āsavadukaṃ': [('āsavdk', 'စိတ်အစွန်းအထင်း ဖြစ်သော'), ('noāsav', 'စိတ်အစွန်းအထင်း မဟုတ်သော')],
 'Āsavasampayuttadukaṃ': [('āsavasampayutt', 'စိတ်အစွန်းအထင်းနှင့် ယှဉ်တွဲသော'),
                          ('āsavavippayutt', 'စိတ်အစွန်းအထင်းနှင့် ကင်းကွာသော')],
 'Āsavasāsavadukaṃ': [('āsavsāsavdk', 'စိတ်အစွန်းအထင်းလည်း ဖြစ်၊ စိတ်အစွန်းအထင်း၏ အာရုံလည်း ဖြစ်နိုင်သော'),
                      ('sāsavnoāsavdk', 'စိတ်အစွန်းအထင်း၏ အာရုံ ဖြစ်နိုင်သော်လည်း စိတ်အစွန်းအထင်း မဟုတ်သော')],
 'Āsavavippayuttasāsavadukaṃ': [('āsavvippsāsavdk',
                                 'စိတ်အစွန်းအထင်းနှင့် ကင်းကွာသော်လည်း စိတ်အစွန်းအထင်း၏ အာရုံ ဖြစ်နိုင်သော'),
                                ('āsavvippanāsavdk',
                                 'စိတ်အစွန်းအထင်းနှင့် ကင်းကွာ၊ စိတ်အစွန်းအထင်း၏ အာရုံ မဖြစ်နိုင်သော')],
 'Āsavaāsavasampayuttadukaṃ': [('āsavāsavsampdk', 'စိတ်အစွန်းအထင်းလည်း ဖြစ်၊ စိတ်အစွန်းအထင်းနှင့်လည်း ယှဉ်တွဲသော'),
                               ('āsavsampnoāsavdk', 'စိတ်အစွန်းအထင်းနှင့် ယှဉ်တွဲသော်လည်း စိတ်အစွန်းအထင်း မဟုတ်သော')]}
TRIAD_MY = {'Ajjhattattikaṃ': [('ajjhatt', 'မိမိ၌ ရှိသော'),
                    ('bahiddh', 'မိမိ၏ ပြင်ပ၌ ရှိသော'),
                    ('ajjhattabahiddh', 'မိမိ၌နှင့် မိမိ၏ ပြင်ပ၌ ရှိသော')],
 'Ajjhattārammaṇattikaṃ': [('ajjhattārammaṇ', 'မိမိ၌ ရှိသည်ကို အာရုံပြုသော'),
                           ('bahiddhārammaṇ', 'မိမိ၏ ပြင်ပ၌ ရှိသည်ကို အာရုံပြုသော'),
                           ('ajjhattabahiddhārammaṇ', 'မိမိ၌နှင့် မိမိ၏ ပြင်ပ၌ ရှိသည်ကို အာရုံပြုသော')],
 'Atītattikaṃ': [('atīt', 'အတိတ်'), ('anāgat', 'အနာဂတ်'), ('paccuppann', 'ပစ္စုပ္ပန်')],
 'Atītārammaṇattikaṃ': [('atītārammaṇ', 'အတိတ်ကို အာရုံပြုသော'),
                        ('anāgatārammaṇ', 'အနာဂတ်ကို အာရုံပြုသော'),
                        ('paccuppannārammaṇ', 'ပစ္စုပ္ပန်ကို အာရုံပြုသော')],
 'Dassanenapahātabbahetukattikaṃ': [('dassanena pahātabbahetuk', 'သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ရမည့် အမြစ် ရှိသော'),
                                    ('bhāvanāya pahātabbahetuk', 'ဘာဝနာ ပွားများခြင်းဖြင့် ပယ်ရမည့် အမြစ် ရှိသော'),
                                    ('nevadassanena nabhāvanāya pahātabbahetuk',
                                     'သစ္စာကို မြင်ခြင်းဖြင့်လည်း ပယ်ရမည့် အမြစ် ရှိသည် မဟုတ်၊ ဘာဝနာ '
                                     'ပွားများခြင်းဖြင့်လည်း ပယ်ရမည့် အမြစ် ရှိသည် မဟုတ်သော')],
 'Dassanenapahātabbattikaṃ': [('dassanena pahātabb', 'သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ရမည့်'),
                              ('bhāvanāya pahātabb', 'ဘာဝနာ ပွားများခြင်းဖြင့် ပယ်ရမည့်'),
                              ('nevadassanena nabhāvanāya pahātabb',
                               'သစ္စာကို မြင်ခြင်းဖြင့်လည်း ပယ်ရမည် မဟုတ်၊ ဘာဝနာ ပွားများခြင်းဖြင့်လည်း ပယ်ရမည် '
                               'မဟုတ်သော')],
 'Hīnattikaṃ': [('hīn', 'ယုတ်ညံ့သော'), ('majjhim', 'အလယ်အလတ်'), ('paṇīt', 'မွန်မြတ်သော')],
 'Kusalattikaṃ': [('kusal', 'ကုသိုလ်'),
                  ('akusal', 'အကုသိုလ်'),
                  ('abyākat', 'ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော')],
 'Maggārammaṇattikaṃ': [('maggārammaṇ', 'မဂ်ကို အာရုံပြုသော'),
                        ('maggahetuk', 'မဂ်ကို အမြစ်ပြုသော'),
                        ('maggādhipat', 'မဂ်ကို အကြီးအမှူးပြုသော')],
 'Micchattaniyatattikaṃ': [('micchattaniyat', 'မှားယွင်းမှု၌ ကျိန်းသေသော'),
                           ('sammattaniyat', 'မှန်ကန်မှု၌ ကျိန်းသေသော'),
                           ('aniyat', 'မကျိန်းသေသော')],
 'Parittattikaṃ': [('paritt', 'အကန့်အသတ် ရှိသော'), ('mahaggat', 'ကြီးမြတ်သော'), ('appamāṇ', 'အတိုင်းအဆ မရှိသော')],
 'Parittārammaṇattikaṃ': [('parittārammaṇ', 'အကန့်အသတ် ရှိသည်ကို အာရုံပြုသော'),
                          ('mahaggatārammaṇ', 'ကြီးမြတ်သည်ကို အာရုံပြုသော'),
                          ('appamāṇārammaṇ', 'အတိုင်းအဆ မရှိသည်ကို အာရုံပြုသော')],
 'Pītittikaṃ': [('pītisahagat', 'ပီတိနှင့်အတူ ဖြစ်သော'),
                ('sukhasahagat', 'သာယာမှုနှင့်အတူ ဖြစ်သော'),
                ('upekkhāsahagat', 'ဥပေက္ခာနှင့်အတူ ဖြစ်သော')],
 'Sanidassanasappaṭighattikaṃ': [('sanidassanasappaṭigh', 'မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိသော'),
                                 ('anidassanasappaṭigh', 'မမြင်နိုင်သော်လည်း ထိခိုက်မှု ရှိသော'),
                                 ('anidassanaappaṭigh', 'မမြင်နိုင်၊ ထိခိုက်မှုလည်း မရှိသော')],
 'Saṃkiliṭṭhattikaṃ': [('saṃkiliṭṭhasaṃkilesik', 'ကိလေသာဖြင့် ညစ်နွမ်း၍ ကိလေသာ၏ အာရုံလည်း ဖြစ်နိုင်သော'),
                       ('asaṃkiliṭṭhasaṃkilesik', 'ကိလေသာဖြင့် မညစ်နွမ်းသော်လည်း ကိလေသာ၏ အာရုံ ဖြစ်နိုင်သော'),
                       ('asaṃkiliṭṭhaasaṃkilesik', 'ကိလေသာဖြင့်လည်း မညစ်နွမ်း၊ ကိလေသာ၏ အာရုံလည်း မဖြစ်နိုင်သော')],
 'Sekkhattikaṃ': [('sekkh', 'ကျင့်ကြံဆဲသူ၏'),
                  ('asekkh', 'ကျင့်ကြံမှု ပြီးဆုံးသူ၏'),
                  ('nevasekkhanāsekkh', 'ကျင့်ကြံဆဲသူ၏လည်း မဟုတ်၊ ကျင့်ကြံမှု ပြီးဆုံးသူ၏လည်း မဟုတ်သော')],
 'Uppannattikaṃ': [('uppann', 'ဖြစ်ပေါ်ပြီးသော'), ('anuppann', 'မဖြစ်ပေါ်သေးသော'), ('uppād', 'ဖြစ်ပေါ်လာမည့်')],
 'Upādinnattikaṃ': [('upādinnupādāniy', 'ကံကြောင့် ဖြစ်၍ စွဲလမ်းမှု၏ အာရုံလည်း ဖြစ်နိုင်သော'),
                    ('anupādinnupādāniy', 'ကံကြောင့် မဖြစ်သော်လည်း စွဲလမ်းမှု၏ အာရုံ ဖြစ်နိုင်သော'),
                    ('anupādinnaanupādāniy', 'ကံကြောင့်လည်း မဖြစ်၊ စွဲလမ်းမှု၏ အာရုံလည်း မဖြစ်နိုင်သော')],
 'Vedanāttikaṃ': [('sukhāya vedanāya sampayutt', 'သာယာသော ခံစားမှုနှင့် ယှဉ်တွဲသော'),
                  ('dukkhāya vedanāya sampayutt', 'နာကျင်သော ခံစားမှုနှင့် ယှဉ်တွဲသော'),
                  ('adukkhamasukhāya vedanāya sampayutt', 'မနာကျင် မသာယာသော ခံစားမှုနှင့် ယှဉ်တွဲသော')],
 'Vipākattikaṃ': [('vipāk', 'ကံ၏ အကျိုး ဖြစ်သော'),
                  ('vipākadhammadhamm', 'အကျိုး ပေးတတ်သော'),
                  ('nevavipākanavipākadhammadhamm', 'ကံ၏ အကျိုးလည်း မဟုတ်၊ အကျိုး ပေးတတ်သည်လည်း မဟုတ်သော')],
 'Vitakkattikaṃ': [('savitakkasavicār', 'စတင်ကြံစည်မှုနှင့် ဆက်လက်သုံးသပ်မှု ရှိသော'),
                   ('avitakkavicāramatt', 'စတင်ကြံစည်မှု မရှိဘဲ ဆက်လက်သုံးသပ်မှုသာ ရှိသော'),
                   ('avitakkaavicār', 'စတင်ကြံစည်မှုလည်း မရှိ၊ ဆက်လက်သုံးသပ်မှုလည်း မရှိသော')],
 'Ācayagāmittikaṃ': [('ācayagām', 'စုပုံခြင်းဆီသို့ ဦးတည်သော'),
                     ('apacayagām', 'လျော့ပါးခြင်းဆီသို့ ဦးတည်သော'),
                     ('nevācayagāmināpacayagām',
                      'စုပုံခြင်းဆီသို့ ဦးတည်သည်လည်း မဟုတ်၊ လျော့ပါးခြင်းဆီသို့ ဦးတည်သည်လည်း မဟုတ်သော')]}
TIKA_MY = {'Ajjhattattikaṃ': 'မိမိ၌ ရှိခြင်း သုံးမျိုးတွဲ',
 'Ajjhattārammaṇattikaṃ': 'မိမိ၌ ရှိသည်ကို အာရုံပြုခြင်း သုံးမျိုးတွဲ',
 'Atītattikaṃ': 'အတိတ် သုံးမျိုးတွဲ',
 'Atītārammaṇattikaṃ': 'အတိတ်ကို အာရုံပြုခြင်း သုံးမျိုးတွဲ',
 'Dassanenapahātabbahetukattikaṃ': 'သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ရမည့် အမြစ် သုံးမျိုးတွဲ',
 'Dassanenapahātabbattikaṃ': 'သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ခြင်း သုံးမျိုးတွဲ',
 'Hīnattikaṃ': 'ယုတ်ညံ့ခြင်း သုံးမျိုးတွဲ',
 'Kusalattikaṃ': 'ကုသိုလ် သုံးမျိုးတွဲ',
 'Maggārammaṇattikaṃ': 'မဂ်ကို အာရုံပြုခြင်း သုံးမျိုးတွဲ',
 'Micchattaniyatattikaṃ': 'မှားယွင်းမှု၌ ကျိန်းသေခြင်း သုံးမျိုးတွဲ',
 'Parittattikaṃ': 'အကန့်အသတ် ရှိခြင်း သုံးမျိုးတွဲ',
 'Parittārammaṇattikaṃ': 'အကန့်အသတ် ရှိသည်ကို အာရုံပြုခြင်း သုံးမျိုးတွဲ',
 'Pītittikaṃ': 'ပီတိ သုံးမျိုးတွဲ',
 'Sanidassanasappaṭighattikaṃ': 'မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိခြင်း သုံးမျိုးတွဲ',
 'Saṃkiliṭṭhattikaṃ': 'ကိလေသာဖြင့် ညစ်နွမ်းခြင်း သုံးမျိုးတွဲ',
 'Sekkhattikaṃ': 'ကျင့်ကြံဆဲသူ သုံးမျိုးတွဲ',
 'Uppannattikaṃ': 'ဖြစ်ပေါ်ပြီးခြင်း သုံးမျိုးတွဲ',
 'Upādinnattikaṃ': 'ကံကြောင့် ဖြစ်ခြင်း သုံးမျိုးတွဲ',
 'Vedanāttikaṃ': 'ခံစားမှု သုံးမျိုးတွဲ',
 'Vipākattikaṃ': 'ကံ၏ အကျိုး သုံးမျိုးတွဲ',
 'Vitakkattikaṃ': 'စတင်ကြံစည်မှု သုံးမျိုးတွဲ',
 'Ācayagāmittikaṃ': 'စုပုံခြင်းဆီသို့ ဦးတည်ခြင်း သုံးမျိုးတွဲ'}
DUKA_MY = {'Ganthadukaṃ': 'အထုံး နှစ်မျိုးတွဲ',
 'Ganthaganthaniyadukaṃ': 'အထုံး ဖြစ်ခြင်းနှင့် အထုံး၏ အာရုံ ဖြစ်နိုင်ခြင်း နှစ်မျိုးတွဲ',
 'Ganthaganthasampayuttadukaṃ': 'အထုံး ဖြစ်ခြင်းနှင့် အထုံးနှင့် ယှဉ်တွဲခြင်း နှစ်မျိုးတွဲ',
 'Ganthaniyadukaṃ': 'အထုံး၏ အာရုံ ဖြစ်နိုင်ခြင်း နှစ်မျိုးတွဲ',
 'Ganthasampayuttadukaṃ': 'အထုံးနှင့် ယှဉ်တွဲခြင်း နှစ်မျိုးတွဲ',
 'Ganthavippayuttaganthaniyadukaṃ': 'အထုံးနှင့် ကင်းကွာခြင်းနှင့် အထုံး၏ အာရုံ ဖြစ်နိုင်ခြင်း နှစ်မျိုးတွဲ',
 'Hetudukaṃ': 'အမြစ် နှစ်မျိုးတွဲ',
 'Hetuhetusampayuttadukaṃ': 'အမြစ် ဖြစ်ခြင်းနှင့် အမြစ်နှင့် ယှဉ်တွဲခြင်း နှစ်မျိုးတွဲ',
 'Hetusahetukadukaṃ': 'အမြစ် ဖြစ်ခြင်းနှင့် အမြစ် ရှိခြင်း နှစ်မျိုးတွဲ',
 'Hetusampayuttadukaṃ': 'အမြစ်နှင့် ယှဉ်တွဲခြင်း နှစ်မျိုးတွဲ',
 'Kenaciviññeyyadukaṃ': 'တစ်စုံတစ်ခုသော စိတ်ဖြင့် သိနိုင်ခြင်း နှစ်မျိုးတွဲ',
 'Lokiyadukaṃ': 'လောကနှင့် သက်ဆိုင်ခြင်း နှစ်မျိုးတွဲ',
 'Nahetusahetukadukaṃ': 'အမြစ် မဟုတ်ခြင်းနှင့် အမြစ် ရှိခြင်း နှစ်မျိုးတွဲ',
 'Nīvaraṇadukaṃ': 'အတားအဆီး နှစ်မျိုးတွဲ',
 'Nīvaraṇanīvaraṇasampayuttadukaṃ': 'အတားအဆီး ဖြစ်ခြင်းနှင့် အတားအဆီးနှင့် ယှဉ်တွဲခြင်း နှစ်မျိုးတွဲ',
 'Nīvaraṇanīvaraṇiyadukaṃ': 'အတားအဆီး ဖြစ်ခြင်းနှင့် အတားအဆီး၏ အာရုံ ဖြစ်နိုင်ခြင်း နှစ်မျိုးတွဲ',
 'Nīvaraṇasampayuttadukaṃ': 'အတားအဆီးနှင့် ယှဉ်တွဲခြင်း နှစ်မျိုးတွဲ',
 'Nīvaraṇavippayuttanīvaraṇiyadukaṃ': 'အတားအဆီးနှင့် ကင်းကွာခြင်းနှင့် အတားအဆီး၏ အာရုံ ဖြစ်နိုင်ခြင်း နှစ်မျိုးတွဲ',
 'Nīvaraṇiyadukaṃ': 'အတားအဆီး၏ အာရုံ ဖြစ်နိုင်ခြင်း နှစ်မျိုးတွဲ',
 'Parāmaṭṭhadukaṃ': 'မှားယွင်းသော ယူဆမှု၏ အာရုံ ဖြစ်နိုင်ခြင်း နှစ်မျိုးတွဲ',
 'Parāmāsadukaṃ': 'မှားယွင်းသော ယူဆမှု နှစ်မျိုးတွဲ',
 'Parāmāsaparāmaṭṭhadukaṃ': 'မှားယွင်းသော ယူဆမှု ဖြစ်ခြင်းနှင့် မှားယွင်းသော ယူဆမှု၏ အာရုံ ဖြစ်နိုင်ခြင်း '
                            'နှစ်မျိုးတွဲ',
 'Parāmāsasampayuttadukaṃ': 'မှားယွင်းသော ယူဆမှုနှင့် ယှဉ်တွဲခြင်း နှစ်မျိုးတွဲ',
 'Parāmāsavippayuttaparāmaṭṭhadukaṃ': 'မှားယွင်းသော ယူဆမှုနှင့် ကင်းကွာခြင်းနှင့် မှားယွင်းသော ယူဆမှု၏ အာရုံ '
                                      'ဖြစ်နိုင်ခြင်း နှစ်မျိုးတွဲ',
 'Rūpīdukaṃ': 'ရုပ် ဖြစ်ခြင်း နှစ်မျိုးတွဲ',
 'Sahetukadukaṃ': 'အမြစ် ရှိခြင်း နှစ်မျိုးတွဲ',
 'Sanidassanadukaṃ': 'မြင်နိုင်ခြင်း နှစ်မျိုးတွဲ',
 'Sappaccayadukaṃ': 'အကြောင်း ရှိခြင်း နှစ်မျိုးတွဲ',
 'Sappaṭighadukaṃ': 'ထိခိုက်မှု ရှိခြင်း နှစ်မျိုးတွဲ',
 'Saññojanadukaṃ': 'နှောင်ကြိုး နှစ်မျိုးတွဲ',
 'Saññojanasampayuttadukaṃ': 'နှောင်ကြိုးနှင့် ယှဉ်တွဲခြင်း နှစ်မျိုးတွဲ',
 'Saññojanasaññojanasampayuttadukaṃ': 'နှောင်ကြိုး ဖြစ်ခြင်းနှင့် နှောင်ကြိုးနှင့် ယှဉ်တွဲခြင်း နှစ်မျိုးတွဲ',
 'Saññojanasaññojaniyadukaṃ': 'နှောင်ကြိုး ဖြစ်ခြင်းနှင့် နှောင်ကြိုး၏ အာရုံ ဖြစ်နိုင်ခြင်း နှစ်မျိုးတွဲ',
 'Saññojanavippayuttasaññojaniyadukaṃ': 'နှောင်ကြိုးနှင့် ကင်းကွာခြင်းနှင့် နှောင်ကြိုး၏ အာရုံ ဖြစ်နိုင်ခြင်း '
                                        'နှစ်မျိုးတွဲ',
 'Saññojaniyadukaṃ': 'နှောင်ကြိုး၏ အာရုံ ဖြစ်နိုင်ခြင်း နှစ်မျိုးတွဲ',
 'Saṅkhatadukaṃ': 'ပြုပြင်ဖန်တီးထားခြင်း နှစ်မျိုးတွဲ',
 'Sāsavadukaṃ': 'စိတ်အစွန်းအထင်း၏ အာရုံ ဖြစ်နိုင်ခြင်း နှစ်မျိုးတွဲ',
 'Āsavadukaṃ': 'စိတ်အစွန်းအထင်း နှစ်မျိုးတွဲ',
 'Āsavasampayuttadukaṃ': 'စိတ်အစွန်းအထင်းနှင့် ယှဉ်တွဲခြင်း နှစ်မျိုးတွဲ',
 'Āsavasāsavadukaṃ': 'စိတ်အစွန်းအထင်း ဖြစ်ခြင်းနှင့် စိတ်အစွန်းအထင်း၏ အာရုံ ဖြစ်နိုင်ခြင်း နှစ်မျိုးတွဲ',
 'Āsavavippayuttasāsavadukaṃ': 'စိတ်အစွန်းအထင်းနှင့် ကင်းကွာခြင်းနှင့် စိတ်အစွန်းအထင်း၏ အာရုံ ဖြစ်နိုင်ခြင်း '
                               'နှစ်မျိုးတွဲ',
 'Āsavaāsavasampayuttadukaṃ': 'စိတ်အစွန်းအထင်း ဖြစ်ခြင်းနှင့် စိတ်အစွန်းအထင်းနှင့် ယှဉ်တွဲခြင်း နှစ်မျိုးတွဲ'}
GOC_MY = {'Ganthagocchaka': 'အထုံးတို့၏ အစု',
 'Nīvaraṇagocchaka': 'အတားအဆီးတို့၏ အစု',
 'Oghagocchaka': 'ရေအလျဉ်တို့၏ အစု',
 'Parāmāsagocchaka': 'မှားယွင်းသော ယူဆမှုတို့၏ အစု',
 'Saññojanagocchaka': 'နှောင်ကြိုးတို့၏ အစု',
 'Upādānagocchaka': 'စွဲလမ်းမှုတို့၏ အစု',
 'Yogagocchaka': 'ထမ်းပိုးတို့၏ အစု',
 'Āsavagocchaka': 'စိတ်အစွန်းအထင်းတို့၏ အစု'}


# ----------------------------------------------------------------------------- Pāli term regexes (typed here)
def _ci(s):
    return f"[{s[0].upper()}{s[0]}]" + re.escape(s[1:])


_W = r"[\wāīūṃṅñṭḍṇḷ]*"
_CV = r"(?:ñceva| ceva)"


def _two(a, b):        # «A-ñceva B-ñca» / «A-o ceva B-o ca» (the closing ca may be missing: a slip)
    return (_ci(a) + _W + "?" + _CV + " " + re.escape(b) + r"(?:" + _W + r"?ñca|" + _W
            + r"? ca(?![\wāīūṃṅñṭḍṇḷ])|" + _W + ")")


def _noca(a, b, neg="no"):  # «A-ñceva no ca B-aṃ»
    return _ci(a) + _W + "?" + _CV + f" {neg} ca " + re.escape(b) + _W


DYAD_PI = {
    "Hetudukaṃ": [_ci("het") + _W, _ci("nahet") + _W],
    "Sahetukadukaṃ": [_ci("sahetuk") + _W, _ci("ahetuk") + _W],
    "Hetusampayuttadukaṃ": [_ci("hetusampayutt") + _W, _ci("hetuvippayutt") + _W],
    "Hetusahetukadukaṃ": [_two("het", "sahetuk"), _noca("sahetuk", "het", "na")],
    "Hetuhetusampayuttadukaṃ": [_two("het", "hetusampayutt"), _noca("hetusampayutt", "het", "na")],
    "Nahetusahetukadukaṃ": [_ci("nahet") + _W + " sahetuk" + _W, _ci("nahet") + _W + " ahetuk" + _W],
    "Sappaccayadukaṃ": [_ci("sappaccay") + _W, _ci("appaccay") + _W],
    "Saṅkhatadukaṃ": [_ci("saṅkhat") + _W, _ci("asaṅkhat") + _W],
    "Sanidassanadukaṃ": [_ci("sanidassan") + _W, _ci("anidassan") + _W],
    "Sappaṭighadukaṃ": [_ci("sappaṭigh") + _W, _ci("appaṭigh") + _W],
    "Rūpīdukaṃ": [_ci("rūp") + _W, _ci("arūp") + _W],
    "Lokiyadukaṃ": [_ci("lokiy") + _W, _ci("lokuttar") + _W],
    "Kenaciviññeyyadukaṃ": [_ci("kenaci viññeyy") + _W, _ci("kenaci naviññeyy") + _W],
}
for _x, _s, _as, _samp in (("āsav", "sāsav", "anāsav", "āsavasampayutt"),
                           ("saññojan", "saññojaniy", "asaññojaniy", "saññojanasampayutt"),
                           ("ganth", "ganthaniy", "aganthaniy", "ganthasampayutt"),
                           ("nīvaraṇ", "nīvaraṇiy", "anīvaraṇiy", "nīvaraṇasampayutt"),
                           ("parāmās", "parāmaṭṭh", "aparāmaṭṭh", "parāmāsasampayutt")):
    _vipp = _samp.replace("sampayutt", "vippayutt")
    _X, _S = _x[0].upper() + _x[1:] + "a", _s[0].upper() + _s[1:] + "a"
    DYAD_PI[f"{_X}dukaṃ"] = [_ci(_x) + _W, _ci("no" + _x) + _W]
    DYAD_PI[f"{_S}dukaṃ"] = [_ci(_s) + _W, _ci(_as) + _W]
    DYAD_PI[f"{_X}sampayuttadukaṃ"] = [_ci(_samp) + _W, _ci(_vipp) + _W]
    DYAD_PI[f"{_X}{_s}adukaṃ"] = [_two(_x, _s), _noca(_s, _x)]
    if _x != "parāmās":
        DYAD_PI[f"{_X}{_x}asampayuttadukaṃ"] = [_two(_x, _samp), _noca(_samp, _x)]
    DYAD_PI[f"{_X}vippayutta{_s}adukaṃ"] = [_ci(_vipp) + _W + " " + re.escape(_s) + _W,
                                            _ci(_vipp) + _W + " " + re.escape(_as) + _W]
# Pāli spots the term regexes cannot see: (regex, [(dyad term index, triad stem)]) (slips and readings, logged)
TERM_SPECIAL = [(r"kenaci viññeyyakusala", [(0, "kusal")]), (r"[Nn]ahetu asakkho", [(1, "asekkh")]),
                (r"nīvaraṇo ca nīvaraṇiyo ca akusal" + _W, [(0, "akusal")]),
                (r"Nīvaraṇañca nonīvaraṇañca akusalaṃ", [(0, "akusal"), (1, "akusal")])]
PART_RE = re.compile(r"^(#{5,6}) (\d+-\d+\.?) (\S+?)duka-(\S+?)ttikaṃ \^")


def parts_of(name):
    """the active (dyad head, triad head) of each non-empty Pāli line"""
    cur, out = None, []
    for l in nonempty(PALI / name):
        m = PART_RE.match(l)
        if m:
            cur = (m[3] + "dukaṃ", m[4][0].upper() + m[4][1:] + "ttikaṃ")
        out.append(cur)
    first = next(p for p in out if p)
    return [p or first for p in out]


def pali_terms(line, part):
    dh, th = part
    s = strip_var(ID.sub("", line))
    found = []
    for rx, items in TERM_SPECIAL:
        for m in re.finditer(rx, s):
            for j, (di, st) in enumerate(items):
                found.append((m.start() + j / 10, m.end(), (di, st)))
    stems = sorted((st for st, _ in TRIAD_MY[th]), key=len, reverse=True)
    for di, drx in enumerate(DYAD_PI[dh]):
        for st in stems:
            for m in re.finditer(r"(?<![\wāīūṃṅñṭḍṇḷ])(?:" + drx + ") " + re.escape(st) + _W, s):
                if not any(a <= m.start() < b for a, b, _ in found):
                    found.append((m.start(), m.end(), (di, st)))
    found.sort()
    return [k for _, _, k in found]


def my_terms(line, part):
    dh, th = part
    vals = {}
    for di, (_, dv) in enumerate(DYAD_MY[dh]):
        for st, tv in TRIAD_MY[th]:
            vals[f"{dv}၊ {tv}"] = (di, st)
    rx = re.compile("(" + "|".join(re.escape(v) for v in sorted(vals, key=len, reverse=True)) + ")")
    return [vals[m.group(1)] for m in rx.finditer(strip_var(ID.sub("", line)))]


def names_ok(p, m, part):
    """the dyad-triad heading, the pada headings and the colophons carry the right names (None: not such a line)"""
    dh, th = part
    mh = PART_RE.match(p)
    if mh:
        want = (f"{mh[1]} {mh[2]} {DUKA_MY[mh[3] + 'dukaṃ']}နှင့် "
                f"{TIKA_MY[mh[4][0].upper() + mh[4][1:] + 'ttikaṃ']}")
        return m.split(" ^")[0] == want
    mp = re.match(r"^#+ (\S+)padaṃ \^", p)
    if mp:
        for st, tv in TRIAD_MY[th]:
            key = st.replace(" ", "").replace("dhammadhamm", "dhamm").lower()
            if mp[1].lower().startswith(key) and len(mp[1]) - len(key) <= 1:
                return m.split(" ^")[0].split(" ", 1)[1] == f"{tv} ပုဒ်"
        return None
    mc = re.search(r"(\S+?)(duka|gocchaka)(\S+?)ttikaṃ niṭṭhitaṃ\.", p)
    if mc:
        first = DUKA_MY.get(mc[1] + "dukaṃ") if mc[2] == "duka" else GOC_MY.get(mc[1] + "gocchaka")
        return f"“{first}နှင့် {TIKA_MY[mc[3][0].upper() + mc[3][1:] + 'ttikaṃ']}” ပြီးဆုံးပြီ။" in m
    return None


# ----------------------------------------------------------------------------- N: numbers
KH_NOUN = r"(?:khandh|mahābhūt|viññāṇ)"


def pali_numbers(line):
    s = strip_var(ID.sub("", line))
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
    for m in re.finditer(r"(?i)(pañca|catu)viññāṇ", s):
        kh.append((m.start(), 5 if m.group(1).lower() == "pañca" else 4))
    for m in re.finditer(r"(?i)tevīsatipaccayā|catuvīsatipaccayā", s):
        kh.append((m.start(), 23 if m.group(0).lower().startswith("tev") else 24))
    for m in re.finditer(r"tayokhandh", s):                       # source slip «tayokhandhā»
        kh.append((m.start(), 3))
    if "Cha " in s and "nayā" in s:
        kh.append((s.find("Cha "), 6))
    for m in re.finditer(r"(?i)pañcāyatanāni", s):
        kh.append((m.start(), 5))
    if "saddhāpañcamakesu" in s:
        kh.append((s.find("saddhāpañcamakesu"), 5))
    for m in re.finditer(r"(?i)((?<!ghā)(?<!ajjha)(?<!ajjhat)(?<!mā)(?<!ka)t?tik|duk)(?=[aāue])|(" + "|".join(GROUP_PI) + r")", s):
        grp.append((m.start(), 3 if m.group(1) and "tik" in m.group(1).lower() else (2 if m.group(1) else GROUP_PI[m.group(2).lower()])))
    for m in re.finditer(r"(?i)dukatik", s):              # «dukatika» = a dyad with a triad (the lookbehind above)
        grp.append((m.start() + 3, 3))
    if "majjhe tiṇṇaṃ" in s:                              # «majjhe tiṇṇaṃ» «အလယ် သုံးခု၌»
        cnt.append((s.find("majjhe tiṇṇaṃ"), 3))
    if "imesaṃ tiṇṇannaṃ" in s:                           # «imesaṃ tiṇṇannaṃ» «ဤ သုံးခုတို့၌»
        cnt.append((s.find("imesaṃ tiṇṇannaṃ"), 3))
    digits = re.findall(r"\((\d+)\.?\)", s)
    return [v for _, v in sorted(cnt)], [v for _, v in sorted(kh)], [v for _, v in sorted(grp)], digits


def my_numbers(line):
    s = strip_var(ID.sub("", line)).replace("တစ်စုံတစ်ခုသော", "")     # kenaci «တစ်စုံတစ်ခုသော» (not a count)
    alt = "|".join(sorted(MY_NUM, key=len, reverse=True))
    cnt = [MY_NUM[m.group(1)] for m in re.finditer(r"(?<!ဆယ့်)(?<!နှစ်ဆယ့်)(" + alt + r")ခု", s)]
    kh = [MY_NUM[m.group(1)] for m in re.finditer(r"(?<!သူ)(?<!ဆယ့်)(" + alt + r")ပါး", s)]
    grp = [MY_NUM[m.group(1)] for m in re.finditer(r"(?<!ဆယ့်)(" + alt + r")မျိုးတွဲ", s)]
    digits = re.findall(r"\((\d+)\.?\)", s)
    return cnt, kh, grp, digits



# ----------------------------------------------------------------------------- run
def load_make():
    import importlib.util
    spec = importlib.util.spec_from_file_location("make_ch4_02_09", HERE / "make_ch4-02-09.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


GROUP_DIFF = []


def _sents(p, m):
    ps = re.split(r"(?<=[.?])\s+(?=\S)", ID.sub("", p).strip())
    ms = re.split(r"(?<=။)\s+(?=\S)", ID.sub("", m).strip())
    return list(zip(ps, ms)) if len(ps) == len(ms) else []


def check(names, out):
    mk = load_make()
    bad = []
    stats = {k: 0 for k in "SPCONIT"}
    pairs_all = []
    for name in names:
        pl, ml = nonempty(PALI / name), nonempty(out / name)
        parts = parts_of(name)
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
            if re.search(r"[ၠ-႟]|[ꩠ-ꩿ]", m):
                bad.append(("S", name, i, "non-Burmese Myanmar block code point"))
            stats["P"] += 1
            ps = strip_var(p)
            exp_not = sum(len(re.findall(rx, ps)) * n for rx, n in NEG_NOT)
            exp_ma = sum(len(re.findall(rx, ps)) * n for rx, n in NEG_MA)
            got_not = strip_var(m).count("မဟုတ်")
            got_ma = len(MA_MY.findall(strip_var(m)))
            if exp_not != got_not or exp_ma != got_ma:
                bad.append(("P", name, i, f"negation မဟုတ် {exp_not}/{got_not}, မ… {exp_ma}/{got_ma}"))
            stats["C"] += 1
            pc, mc = pali_conds(p), my_conds(m, p)
            if mc is None:
                bad.append(("C", name, i, "a note's Burmese differs from the checker's table"))
            elif pc != mc:
                bad.append(("C", name, i, f"conditions {pc[:6]}… vs {mc[:6]}… ({len(pc)}/{len(mc)})"))
            stats["O"] += 1
            pt, mt = pali_terms(p, parts[i - 1]), my_terms(m, parts[i - 1])
            if pt != mt:
                bad.append(("O", name, i, f"terms {pt[:4]} vs {mt[:4]} ({len(pt)}/{len(mt)})"))
            if names_ok(p, m, parts[i - 1]) is False:
                bad.append(("O", name, i, "dyad-triad / pada / colophon name"))
            stats["N"] += 1
            pn, mn = pali_numbers(p), my_numbers(m)
            for lab, a, b in zip(("counts", "khandha", "groups", "digits"), pn, mn):
                if a != b:
                    bad.append(("N", name, i, f"{lab} {a} vs {b}"))
    # I: identity (these chapters + the approved sample on disk)
    seen = {}
    extra = []
    disk = ROOT / "AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters"
    for n in SAMPLE:
        extra += [(n, i, p, m) for i, (p, m) in enumerate(zip(nonempty(PALI / n), nonempty(disk / n)), 1)]
    for name, i, p, m in pairs_all + extra:
        for a, b in _sents(p, m):
            if name in names:
                stats["I"] += 1
            seen.setdefault(a[:1].lower() + a[1:], {}).setdefault(b, (name, i))
    for k, v in seen.items():
        if len(v) > 1 and any(x[0] in names for x in v.values()):
            bad.append(("I", "-", 0, f"«{k[:70]}» has {len(v)} renderings: {list(v.values())[:3]}"))
    grp = {}
    for n in GROUPS:
        for i, (p, m) in enumerate(zip(nonempty(PALI / n), nonempty(disk / n)), 1):
            for a, b in _sents(p, m):
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
    for w in (mk.WA, mk.WB):
        for st, my in CONDS_MY.items():
            stats["T"] += 1
            if w.F.N.get(st) != my:
                bad.append(("T", "-", 0, f"condition {st}: module «{w.F.N.get(st)}» vs checker «{my}»"))
        for wd, n in COUNT_PI.items():
            if wd in w.F.COUNT:
                stats["T"] += 1
                if w.F.COUNT[wd] != NUM_MY[n] + "ခု":
                    bad.append(("T", "-", 0, f"count {wd}"))
    for h, v in DYAD_MY.items():
        stats["T"] += 2
        if [(t, mk.dyad_value(h, t)) for _, t, _ in mk.DYAD_SURF[h]] != v:
            bad.append(("T", "-", 0, f"dyad {h}"))
        if mk.DUKA_NAME[h] != DUKA_MY[h]:
            bad.append(("T", "-", 0, f"dyad name {h}"))
    for h, v in TRIAD_MY.items():
        stats["T"] += 2
        if list(mk.TRIADS[h].items()) != v or mk.TIKA_NAME[h] != TIKA_MY[h]:
            bad.append(("T", "-", 0, f"triad {h}"))
    for g, v in GOC_MY.items():
        stats["T"] += 1
        if mk.GOC_NAME.get(g) != v:
            bad.append(("T", "-", 0, f"cluster name {g}"))
    for k, tab in mk.COMBO.items():
        for key, val in tab.items():
            stats["T"] += 1
            dh, dt, th, tt = mk.COMBO_PALI[key]
            if val != f"{dict(DYAD_MY[dh])[dt]}၊ {dict(TRIAD_MY[th])[tt]}":
                bad.append(("T", "-", 0, f"combined term {key}"))
    # R: reuse
    reuse_n = reuse_ok = 0
    wit = {}
    for w in (mk.WA, mk.WB):
        wit.update(w.F.WITNESS)
    F0 = mk.WA.F
    for pali, (book, bid, my) in wit.items():
        f_, pseg, mseg = F0.FINAL.SEG[book][bid]
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
    import reuse_index as RI
    idx = RI.index()
    sent_n = sent_ok = 0
    for name, i, p, m in pairs_all:
        for a, b in _sents(p, m):
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
    print("checked:", ", ".join(f"{k} {v}" for k, v in stats.items() if k != "G"))
    print(f"reuse test: terms {reuse_ok} / {reuse_n} identical (of {len(wit)} witnessed values); "
          f"sentences {sent_ok} / {sent_n} identical")
    print(f"identity with the finished pi-7 groups: {stats['G']} sentences identical (differences: --groups)")
    if "--groups" in sys.argv:
        for k, a, b in GROUP_DIFF:
            print("G |", k[:110], "\n    mine:", a[0][:200], a[1], "\n    grp: ", b[0][:200], b[1])
    print(f"{len(bad)} mismatches")
    return mk, bad


def sample_identity(mk):
    """the approved sample, regenerated through world A with this generator's extensions, equals the files on disk"""
    bad = 0
    disk = ROOT / "AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters"
    w = mk.WA
    mk.set_terms(w, {})
    w.FG.translate("")
    for n in SAMPLE:
        src = (PALI / n).read_text(encoding="utf-8-sig")
        for label, txt in (("raw", src), ("prep", w.D.prep(src, None))):
            same = w.F.translate(txt) == (disk / n).read_text(encoding="utf-8")
            print(f"sample identity {n} ({label}): {'identical' if same else 'DIFFERS'}")
            bad += not same
    return bad


MUT = [  # (file, old, new, what)
    ("4-02-dukatika-hetuduka.md", "အမြစ်ဟူသော အကြောင်း၌ ကိုးခု၊ အာရုံဟူသော", "အမြစ်ဟူသော အကြောင်း၌ ရှစ်ခု၊ အာရုံဟူသော", "count"),
    ("4-02-dukatika-hetuduka.md", "အကြီးအမှူးဟူသော အကြောင်းကြောင့် မဟုတ်ဘဲ ဖြစ်ပေါ်သည်",
     "အကြီးအမှူးဟူသော အကြောင်းကြောင့် ဖြစ်ပေါ်သည်", "polarity"),
    ("4-02-dukatika-hetuduka.md", "အမြစ် ဖြစ်သော၊ ကုသိုလ် သဘောတရားကို မှီ၍ အမြစ် မဟုတ်သော၊ ကုသိုလ် သဘောတရားသည်",
     "အမြစ် မဟုတ်သော၊ ကုသိုလ် သဘောတရားကို မှီ၍ အမြစ် ဖြစ်သော၊ ကုသိုလ် သဘောတရားသည်", "term order"),
    ("4-02-dukatika-hetuduka.md", "ကုသိုလ် သဘောတရားသည် အမြစ်ဟူသော အကြောင်းကြောင့်",
     "ကုသိုလ် သဘောတရားသည် အာရုံဟူသော အကြောင်းကြောင့်", "condition"),
    ("4-05-dukatika-asavaduka.md", "စိတ်အစွန်းအထင်း မဟုတ်သော၊ ကုသိုလ်", "စိတ်အစွန်းအထင်း ဖြစ်သော၊ ကုသိုလ်", "dyad term"),
    ("4-02-dukatika-hetuduka.md", "အမြစ် ဖြစ်သော၊ အကုသိုလ် သဘောတရားကို", "အမြစ် ဖြစ်သော၊ ကုသိုလ် သဘောတရားကို", "triad term"),
    ("4-02-dukatika-hetuduka.md", "(3) ^7-36-1", "(2) ^7-36-1", "digits"),
    ("4-03-dukatika-sahetukaduka.md", "(အမြစ်ဟူသော အကြောင်း မရှိ။", "(အမြစ်ဟူသော အကြောင်း ရှိ။", "note"),
    ("4-02-dukatika-hetuduka.md", "1-2. အမြစ် နှစ်မျိုးတွဲနှင့် ခံစားမှု သုံးမျိုးတွဲ",
     "1-2. အမြစ် နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ", "part name"),
    ("4-08-dukatika-nivaranaduka.md", "အတားအဆီး မဟုတ်သော၊ ကုသိုလ်", "အတားအဆီး မဟုတ်သော၊ အကုသိုလ်", "B world term"),
    ("4-02-dukatika-hetuduka.md", "###### သာယာသော ခံစားမှုနှင့် ယှဉ်တွဲသော ပုဒ်",
     "###### နာကျင်သော ခံစားမှုနှင့် ယှဉ်တွဲသော ပုဒ်", "pada name"),
]


def mutate():
    tmp = HERE / "chk-mut-ch4-02-09"
    caught = 0
    for f, old, new, what in MUT:
        if tmp.exists():
            shutil.rmtree(tmp)
        tmp.mkdir()
        for n in MINE:
            shutil.copy(OUT / n, tmp / n)
        t = (tmp / f).read_text(encoding="utf-8")
        if old not in t:
            print("mutation not applicable:", what)
            continue
        (tmp / f).write_text(t.replace(old, new, 1), encoding="utf-8")
        r = subprocess.run([sys.executable, "-I", "-X", "utf8", str(HERE / "check_ch4-02-09.py"), f, "--out", str(tmp)],
                           capture_output=True, text=True)
        last = r.stdout.strip().splitlines()[-1] if r.stdout.strip() else r.stderr[-200:]
        ok = r.returncode != 0
        caught += ok
        print(f"{what:14} -> {'caught' if ok else 'MISSED'} ({last})")
    shutil.rmtree(tmp)
    print(f"{caught} / {len(MUT)} planted errors caught")
    return len(MUT) - caught


def pe_check(names):
    tmp = HERE / "chk-pe" / "ch4-02-09"
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
    if "--sample" in FLAGS:
        fail |= bool(sample_identity(mk))
    if "--pe" in FLAGS:
        fail |= bool(pe_check(NAMES))
    if "--mutate" in FLAGS:
        fail |= bool(mutate())
    sys.exit(1 if fail else 0)
