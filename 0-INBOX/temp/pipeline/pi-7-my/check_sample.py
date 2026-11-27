"""Per-line check of the Burmese pi-7 sample against the Pāli (independent of the generator's frames).

usage: python3 -I -X utf8 check_sample.py [chapter ...]
Checks, line by line (Pāli line i <-> Burmese line i):
  S  structure: equal non-empty lines, heading #-level, block IDs, no «?» «।» «:-», no Latin left outside variants;
  P  polarity: «မဟုတ်» count and the «မ…» negatives expected from the Pāli tokens (TABLE NEG_*);
  C  conditions: the sequence of conditions (stem + polarity) named in the Pāli = the sequence of
     «Nဟူသော အကြောင်း» (and the bare names of the ghaṭanā lists) in the Burmese;
  O  term order: the sequence of triad terms (kusala / vedanā) in the Pāli = the sequence in the Burmese
     (conditioning before conditioned, e.g. «X dhammo Yassa dhammassa» -> «X … သည် Y … အား»);
  N  numbers: counts «… ခု», khandha numbers «… ပါး», group numbers «… မျိုးတွဲ», digits «(n)»;
  I  identity: identical Pāli sentences (book-wide in the sample) have identical Burmese sentences;
  T  tables: the condition names and triad terms of my7_formulas equal this checker's own copy;
  R  reuse: every value my7_formulas took from pi-1 … pi-6 (WITNESS) is re-read from the FINAL rails and found
     in every sample line whose Pāli contains its Pāli; sample sentences that occur in pi-1 … pi-6 are identical.
Prints the mismatches and a summary; exit 1 on any mismatch.
"""
import pathlib
import re
import sys

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
ROOT = HERE.parents[3]
PALI = ROOT / "AI_translation/pali/pi-7_split_chapters"
OUT = ROOT / "AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters"
_args = sys.argv[1:]
if "--out" in _args:                      # check a copy elsewhere (chk_mutate.py)
    OUT = pathlib.Path(_args[_args.index("--out") + 1])
    del _args[_args.index("--out"):_args.index("--out") + 2]
NAMES = _args or ["1-00-paccaya.md", "1-02-vedanattika.md"]
ID = re.compile(r"\s*(\^[0-9A-Za-z-]+)\s*$")

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
TERMS_MY = {"kiriyābyākat": "ပြုရုံမျှသာ ဖြစ်သော " + ABY, "abyākat": ABY, "akusal": "အကုသိုလ်", "kusal": "ကုသိုလ်",
            "adukkhamasukhāya vedanāya": "မနာကျင် မသာယာသော ခံစားမှု", "dukkhāya vedanāya": "နာကျင်သော ခံစားမှု",
            "sukhāya vedanāya": "သာယာသော ခံစားမှု"}
NUM_MY = {1: "တစ်", 2: "နှစ်", 3: "သုံး", 4: "လေး", 5: "ငါး", 6: "ခြောက်", 7: "ခုနစ်", 8: "ရှစ်", 9: "ကိုး", 10: "ဆယ်",
          23: "နှစ်ဆယ့်သုံး", 24: "နှစ်ဆယ့်လေး"}
MY_NUM = {v: k for k, v in NUM_MY.items()}
COUNT_PI = {"ekaṃ": 1, "dve": 2, "tīṇi": 3, "cattāri": 4, "pañca": 5, "cha": 6, "satta": 7, "aṭṭha": 8, "nava": 9,
            "dasa": 10}
KH_PI = {"eko": 1, "ekaṃ": 1, "ekassa": 1, "dve": 2, "dvinnaṃ": 2, "tayo": 3, "cattāro": 4}
GROUP_PI = {"catukk": 4, "pañcak": 5, "chakk": 6, "sattak": 7, "navak": 9, "dasak": 10, "tevīsak": 23,
            "catuvīsak": 24}
MULA_PI = {"ekamūlak": 1, "dumūlak": 2, "timūlak": 3, "catumūlak": 4, "pañcamūlak": 5, "tevīsatimūlak": 23}
# notes in which the Pāli names conditions without «paccay»: Pāli -> [(stem, neg)]
NOTE_CONDS = {"(adhipatiyā paṭisandhi natthi)": [("adhipati", False)],
              "(nādhipati paripuṇṇaṃ paṭisandhikaṃ)": [("adhipati", True)],
              "(napacchājātampi naāsevanampi": [("pacchājāta", True), ("āsevana", True)],
              "(aññamaññampi nissayampi": [("aññamañña", False), ("nissaya", False)],
              "(anantarasadisaṃ)": [("anantara", False)], "Samanantarapaccayā (anantarasadisaṃ)": []}
HEAD_CONDS = {"Saindriya-maggaghaṭanā": [("indriya", False), ("magga", False)],
              "Sādhipati-indriya-maggaghaṭanā": [("adhipati", False), ("indriya", False), ("magga", False)],
              "(saupanissayaṃ)": [("upanissaya", False)], "(sakammaṃ)": [("kamma", False)]}
# negation: Pāli token regex -> number of «မဟုတ်» / number of «မ…» negatives expected in the Burmese
NEG_SANDHI = "|".join(x[:-1] for x in STEMS if x.endswith("a"))
_LOCS = ["hetuyā", "adhipatiyā", "atthiyā", "natthiyā"] + [x[:-1] + "e" for x in STEMS
                                                         if x not in ("hetu", "adhipati", "atthi", "natthi")]
NEG_NOT = [(r"(?i)(?<![\wāīūṃṅñṭḍṇḷ])(?:na|no)(?:" + "|".join(sorted(STEMS + _LOCS, key=len, reverse=True)) + "|(?:"
            + NEG_SANDHI + r")(?=ādi))", 1),
           (r"(?<=samanantara)nasahajāta|(?<=vipāka)naāhāra", 1),      # source slips: missing hyphens (logged)
           (r"(?<![\wāīūṃṅñṭḍṇḷ])na (?=§C§|\w+paccayena paccayo)", 1),
           (r"(?i)(?<!kiriy)ābyākat|(?<![\wāīūṃṅñṭḍṇḷ])[Aa]byākat", 2),
           (r"(?i)(?<![\wāīūṃṅñṭḍṇḷ])arūp(?:ino|īnaṃ)", 1), (r"(?i)kiriyābyākat", 2),
           (r"(?i)nevasaññānāsaññāyatan", 2), (r"(?i)anattato", 1), (r"nādhipati", 1)]
NEG_MA = [(r"(?i)adukkhamasukh", 2), (r"(?i)(?<![\wāīūṃṅñṭḍṇḷ])(?:no)?natthi(?:paccay|yā|\b)", 1),
          (r"(?i)(?<![\wāīūṃṅñṭḍṇḷ])(?:no)?avigat", 1), (r"(?i)ahetuk", 1), (r"(?i)aniccato", 1),
          (r"asammuyhantena", 1), (r"na labbhati", 1), (r"na kātabbaṃ", 1),
          (r"(?<![\wāīūṃṅñṭḍṇḷ])arūpe(?![\wāīūṃṅñṭḍṇḷ])", 1), (r"(?i)ākāsānañcāyatan", 1), (r"(?i)viññāṇañcāyatan", 1),
          (r"(?i)ākiñcaññāyatan", 1), (r"(?i)nevasaññānāsaññāyatan", 1)]
MA_MY = re.compile(r"မ(?:နာကျင်|သာယာ|ရှိ|ပျောက်ကွယ်|မြဲ|ရောထွေး|တွေ့ရ|ထည့်ရ)")
W_ = r"[\wāīūṃṅñṭḍṇḷ]"


def nonempty(p):
    return [l for l in p.read_text(encoding="utf-8-sig").splitlines() if l.strip()]


def strip_var(s):
    return re.sub(r"\{[^{}]*\}", "", s)


# ----------------------------------------------------------------------------- C: conditions
def pali_conds(line):
    s = strip_var(ID.sub("", line))
    found = []
    head = s.startswith("#")
    for k, v in NOTE_CONDS.items():
        i = s.find(k)
        while i >= 0:
            found += [(i + j / 10, st, ng) for j, (st, ng) in enumerate(v)]
            i = s.find(k, i + 1)
    for k, v in HEAD_CONDS.items():
        if k in s:
            found += [(s.find(k) + j / 10, st, ng) for j, (st, ng) in enumerate(v)]
    stems = "|".join(STEMS)
    # «…paccay…» words and counting locatives
    for m in re.finditer(r"(?i)(?<!" + W_ + r")(na|no)?(" + stems + r")paccay", s):
        found.append((m.start(), m.group(2).lower(), bool(m.group(1))))
    loc = {"hetuyā": "hetu", "adhipatiyā": "adhipati", "atthiyā": "atthi", "natthiyā": "natthi"}
    loc.update({x[:-1] + "e": x for x in STEMS if x not in loc})
    for m in re.finditer(r"(?i)(?<!" + W_ + r")(na|no)?(" + "|".join(sorted(loc, key=len, reverse=True))
                         + r") (?:" + "|".join(COUNT_PI) + r")(?!" + W_ + ")", s):
        if (m.group(1) or "") + m.group(2) in ("adhipatiyā",) and False:
            continue
        found.append((m.start(), loc[m.group(2).lower()], bool(m.group(1))))
    sandhi = "|".join(x[:-1] if x.endswith("a") else x for x in STEMS)
    look = r"(?=ādi|sabhāg|mūlak|ghaṭan|duk" + ("|-" if head else "") + ")"
    for m in re.finditer(r"(?i)(?<![\wāīūṃṅñṭḍṇḷ-])(na|no)?(" + sandhi + r")a?" + look, s):
        stem = next(x for x in STEMS if x == m.group(2).lower() or x[:-1] == m.group(2).lower())
        if any(abs(f[0] - m.start()) < 1 for f in found):
            continue
        found.append((m.start(), stem, bool(m.group(1))))
    # ghaṭanā compounds «A-B-…nti N» and the hyphenated negated compound
    for m in re.finditer(r"(?i)(?<!" + W_ + r")([\wāīūṃṅñṭḍṇḷ][\wāīūṃṅñṭḍṇḷ -]*?)(?:nti|īti) (?:(?:"
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
    m = re.search(r"\((" + NAME_ALT + r")နှင့် တူသည်\)", s)             # «(anantarasadisaṃ)»
    if m:
        found.append((m.start(), MY_NAME[m.group(1)], False))
    found.sort()
    return [(st, ng) for _, st, ng in found]


# ----------------------------------------------------------------------------- O: triad terms
T_PI = re.compile(r"(?i)(kiriyābyākat|abyākat|ābyākat|akusal|ākusal|kusal|adukkhamasukhāya vedanāya|"
                  r"dukkhāya vedanāya|sukhāya vedanāya)")
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
    for m in re.finditer(r"(?i)(?<!" + W_ + r")(?:\w+?(?:e|yā)|\S+?(?:nti|īti)) (" + "|".join(COUNT_PI) + r")(?!" + W_ + ")", s):
        cnt.append((m.start(), COUNT_PI[m.group(1)]))
    for m in re.finditer(r"(?i)(?<!" + W_ + r")(" + "|".join(MULA_PI) + r")", s):
        cnt.append((m.start(), MULA_PI[m.group(1).lower()]))
    if "ekekassa padassa" in s.lower():
        cnt.append((s.lower().find("ekekassa"), 1))
    for m in re.finditer(r"(?i)(?<!" + W_ + r")(" + "|".join(KH_PI) + r") (?:\S+ )?(?:khandh|mahābhūt)|catuviññāṇ", s):
        kh.append(KH_PI[m.group(1).lower()] if m.group(1) else 4)
    if re.search(r"cattāro (?:khandhā|mahābhūtā)", s):
        pass
    if "tevīsatipaccayā" in s:
        kh.append(23)
    if "Cha " in s and "nayā" in s:
        kh.append(6)
    if "saddhāpañcamakesu" in s:
        kh.append(5)
    for m in re.finditer(r"(?i)(t?tik|duk)(?=[aāu])|(" + "|".join(GROUP_PI) + r")", s):
        grp.append(3 if m.group(1) and "tik" in m.group(1).lower() else (2 if m.group(1) else GROUP_PI[m.group(2).lower()]))
    digits = re.findall(r"\((\d+)\.?\)", s)
    return [v for _, v in sorted(cnt)], kh, grp, digits


def my_numbers(line):
    s = strip_var(ID.sub("", line))
    alt = "|".join(sorted(MY_NUM, key=len, reverse=True))
    cnt = [MY_NUM[m.group(1)] for m in re.finditer(r"(" + alt + r")ခု", s)]
    kh = [MY_NUM[m.group(1)] for m in re.finditer(r"(?<!သူ)(" + alt + r")ပါး", s)]   # not «သူတစ်ပါး» (another)
    grp = [MY_NUM[m.group(1)] for m in re.finditer(r"(" + alt + r")မျိုးတွဲ", s)]
    digits = re.findall(r"\((\d+)\.?\)", s)
    return cnt, kh, grp, digits


# ----------------------------------------------------------------------------- run
def main():
    import my7_formulas as F
    import make_sample  # noqa: F401  (registers the sample's own witnessed values)
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
            # S
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
            # P
            stats["P"] += 1
            ps = strip_var(p)
            exp_not = sum(len(re.findall(rx, ps)) * n for rx, n in NEG_NOT)
            exp_ma = sum(len(re.findall(rx, ps)) * n for rx, n in NEG_MA)
            got_not = strip_var(m).count("မဟုတ်")
            got_ma = len(MA_MY.findall(strip_var(m)))
            if exp_not != got_not or exp_ma != got_ma:
                bad.append(("P", name, i, f"negation မဟုတ် {exp_not}/{got_not}, မ… {exp_ma}/{got_ma}"))
            # C
            stats["C"] += 1
            pc, mc = pali_conds(p), my_conds(m)
            if pc != mc:
                bad.append(("C", name, i, f"conditions {pc[:6]}… vs {mc[:6]}… ({len(pc)}/{len(mc)})"))
            # O
            stats["O"] += 1
            pt, mt = pali_terms(p), my_terms(m)
            if pt != mt:
                bad.append(("O", name, i, f"terms {pt[:6]} vs {mt[:6]} ({len(pt)}/{len(mt)})"))
            # N
            stats["N"] += 1
            pn, mn = pali_numbers(p), my_numbers(m)
            for lab, a, b in zip(("counts", "khandha", "groups", "digits"), pn, mn):
                if a != b:
                    bad.append(("N", name, i, f"{lab} {a} vs {b}"))
    # I: identity of sentences
    seen = {}
    for name, i, p, m in pairs_all:
        ps = re.split(r"(?<=[.?])\s+(?=\S)", ID.sub("", p).strip())
        ms = re.split(r"(?<=။)\s+(?=\S)", ID.sub("", m).strip())
        if len(ps) != len(ms):
            continue
        for a, b in zip(ps, ms):
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
    for k, my in (("sukhāya vedanāya sampayutt", "သာယာသော ခံစားမှုနှင့် ယှဉ်တွဲသော"),
                  ("dukkhāya vedanāya sampayutt", "နာကျင်သော ခံစားမှုနှင့် ယှဉ်တွဲသော"),
                  ("adukkhamasukhāya vedanāya sampayutt", "မနာကျင် မသာယာသော ခံစားမှုနှင့် ယှဉ်တွဲသော")):
        stats["T"] += 1
        if F.TRIADS["vedana"][k] != my:
            bad.append(("T", "-", 0, f"term {k}"))
    for w, n in COUNT_PI.items():
        stats["T"] += 1
        if F.COUNT[w] != NUM_MY[n] + "ခု":
            bad.append(("T", "-", 0, f"count {w}"))
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
    import reuse_index as RI
    idx = RI.index()
    sent_n = sent_ok = 0
    for name, i, p, m in pairs_all:
        ps = re.split(r"(?<=[.?])\s+(?=\S)", ID.sub("", p).strip())
        ms = re.split(r"(?<=။)\s+(?=\S)", ID.sub("", m).strip())
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
    sys.exit(1 if bad else 0)


main()
