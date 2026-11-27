"""Check the Burmese zero-shot of pi-6 10-05 … 10-09-indriyayamaka line by line (adapted from check_sample.py /
check_ch2-02-4-5.py).

usage: python3 -I -X utf8 check_ch10b.py [chapter ...] [--mutate]
  A. rebuild: make_ch10b.py regenerates the files byte for byte (nothing written here);
  B. per line: B1 structure (equal non-empty lines, dashes, ellipses, «[», item numbers, labels (Ka) … = (က) …, block
     IDs, heading levels, no «?» «।» «:-», final «။», NFC, no U+1050-U+109F, no double blank line); B2 POLARITY: every
     Pāli negation (na, no, nuppajj-, Natthi) is one Burmese negative (မဟုတ် / မရှိ / မ + verb), fixed terms masked
     (arūpa place, the privative a-X-ka «X မရှိဘဲ»); B3 VERBS: the sequence of uppajj- verbs of each line (tense,
     polarity, «no ca … na V» double negative «… မVသည်ကား မဟုတ်») equals the Burmese sequence; Āmantā = «ဟုတ်ပါသည်»,
     Natthi = «မရှိပါ။»; B4 (Ka) / (Kha) labels in order, «vā pana» = «တစ်ဖန်»; B5 digits and number words (pañca-,
     catu-, dutiye); B6 every recurring Pāli sentence has one Burmese, in my files and in the finished pi-6 files where
     the same Pāli sentence occurs; B7 headings; B8 quote nesting; B9 FACULTIES: the ordered sequence of faculty words
     of each line (any case form, the «(Xmūlakaṃ)» notes too) equals the ordered sequence of Burmese faculty names;
     B10 PERSONS: per line, each person attribute / head noun / citta qualifier occurs as often as its Burmese
     (sa-/a-X-ka, sahetuka, ñāṇasampayutta, somanassena, upekkhāya, na itthīnaṃ / na purisānaṃ, itthī / purisa, the
     X-sampayutta / X-vippayutta minds, pacchimacitta, upapatticitta, nirodhasamāpanna, eteneva bhāvena …);
  C. reuse test: C1 the 22 faculty names (pi-2 ^2-219, read here independently of my6_formulas); C2 whole lines and
     answers that also occur in pi-1 … pi-5 FINAL; C3 reused terms (witness segment + every line); C4 pi-6: every lead
     (persons / moments / places before tesaṃ / tattha) of my chapters that also occurs in a finished pi-6 chapter
     (not the groups still running: ch. 7, 9, 10) has the same Burmese there. Documented exceptions (EXCEPT) listed apart, not counted.
  --mutate: single mutations of the generated Burmese (in memory) must each be caught.
Prints the mismatches (0 expected) and the counts; exit 1 on any mismatch.
"""
import importlib.util
import pathlib
import re
import sys
import unicodedata

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
_spec = importlib.util.spec_from_file_location("make_ch10b", HERE / "make_ch10b.py")
MS = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(MS)                   # tables only; the generator writes files only under __main__
F = MS.F
ROOT = HERE.parents[3]
NAMES = [a for a in sys.argv[1:] if not a.startswith("-")] or MS.NAMES_OUT
NAMES = [n for n in MS.NAMES_OUT if any(n.startswith(a) for a in NAMES)]
HEAD = re.compile(r"^#+ ")
ID_RE = re.compile(r" (\^[0-9A-Za-z-]+)\s*$")


def nonempty_text(t):
    return [l for l in t.splitlines() if l.strip()]


def nonempty(p):
    return nonempty_text(p.read_text(encoding="utf-8-sig"))


def body(l):
    return F.strip_id(l).strip()


def nobr(s):
    return re.sub(r" ?\[[^\]]*\]", "", s)


def pal(p):
    """Pāli line as the generator reads it (source slips of make_ch10b.SLIPS applied), no ID."""
    return MS.unslip(nobr(body(p)))


# ===================================================================================== FINAL pi-1 … pi-5 (independent)
def blocks(text):
    res, cur = {}, []
    for line in text.splitlines():
        if not line.strip():
            continue
        cur.append(line)
        mm = ID_RE.search(line)
        if mm:
            res[mm.group(1)] = cur
            cur = []
    return res


FIN = {}
FIN_LINE = {}
for bk in "12345":
    pd = ROOT / f"AI_translation/pali/pi-{bk}_split_chapters"
    bd = ROOT / f"AI_translation/burmese/pi-{bk}-burmese-plain-rails_split_chapters"
    d = {}
    for f in sorted(pd.glob("*.md")):
        if not (bd / f.name).exists():
            continue
        pb = blocks(f.read_text(encoding="utf-8-sig"))
        bb = blocks(unicodedata.normalize("NFC", (bd / f.name).read_text(encoding="utf-8-sig")))
        for k, v in pb.items():
            d[k] = (v, bb.get(k, []))
            for x, y in zip(v, bb.get(k, [])):
                FIN_LINE.setdefault(re.sub(r"^#+ ", "", body(x)), set()).add(re.sub(r"^#+ ", "", body(y)))
    FIN[bk] = d

# the 22 faculties, read from the pi-2 ^2-219 list here (not through my6_formulas)
_p = nobr(body(FIN["2"]["^2-219"][0][0])).split(" – ")[1].rstrip(".")
_m = nobr(body(FIN["2"]["^2-219"][1][0])).split(" – ")[1].rstrip("။")
FAC = dict(zip([x.strip() for x in _p.split(",")], [x.strip() for x in _m.split("၊")]))
FAC_STEM = {k[:-1]: v for k, v in FAC.items()}                 # cakkhundriya -> «မျက်စိ၏ စွမ်းရည်»
FAC_SLIP = {"ghānandriya": "ghānindriya"}                      # 10-08 «(Ghānandriyamūlakaṃ)»
P_FAC = re.compile(r"(?<![\w])(" + "|".join(sorted(list(FAC_STEM) + list(FAC_SLIP), key=len, reverse=True))
                   + r")(?=ṃ|ñca|mūlakaṃ)", re.I)
M_FAC = re.compile("|".join(re.escape(v) for v in sorted(FAC.values(), key=len, reverse=True)))

# ===================================================================================== finished pi-6 (not ch. 10)
IN_PROGRESS = ("7-", "9-", "10-")      # groups still running when this group was made (ch7a / ch7b, ch9-10a, ch10c)
P6 = ROOT / "AI_translation/pali/pi-6_split_chapters"
B6 = ROOT / "AI_translation/burmese/pi-6-burmese-plain-zeroshot_split_chapters"
OTHERS = {f.name: (nonempty(P6 / f.name), nonempty(f)) for f in sorted(B6.glob("*.md")) if not f.name.startswith(IN_PROGRESS)}

# ===================================================================================== B2 / B3 / B10 tables
MASK = sorted([F.PLACES["arūpa"]] + [v for k, v in MS.ATTR.items() if k.startswith("a") and "မရှိဘဲ" in v],
              key=len, reverse=True)


def p_neg(s):
    return (len(re.findall(r"(?<![\w])(?:na|no|No|Na)(?![\w])", s)) + len(re.findall(r"nuppajj", s))
            + len(re.findall(r"\b[Nn]atthi\b", s)))


def m_neg(s):
    for t in MASK:
        s = s.replace(t, "")
    return s.count("မဟုတ်") + s.count("မရှိ") + s.count("မဖြစ်ပေါ်") + s.count("မချုပ်ငြိမ်း")


P_VERB = re.compile(r"(?P<noca>no ca (?:tesaṃ tattha|tāsaṃ tattha|tesaṃ|tāsaṃ|tattha) \S+ )?(?P<na>na )?(?P<n>n)?"
                    r"(?P<r>uppajj|nirujjh)(?P<e>issanti|issati|issatīti|ittha|itthāti|anti|ati|atīti)\b", re.I)
P_END = {"issanti": "fut", "issati": "fut", "issatīti": "fut", "ittha": "past", "itthāti": "past",
         "anti": "pres", "ati": "pres", "atīti": "pres"}
M_VERB = re.compile(r"(?<!ပြန်လည် )(?P<neg>မ)?(?P<r>ဖြစ်ပေါ်|ချုပ်ငြိမ်း)(?!လာ|ခြင်း|ပြီး)(?:ကြ)?(?P<t>ခဲ့|လိမ့်မည်|မည့်)?"
                    r"(?P<ns>(?:သည်)?ကား မဟုတ်)?")
M_ROOT = {"ဖြစ်ပေါ်": "uppajj", "ချုပ်ငြိမ်း": "nirujjh"}
M_T = {None: "pres", "ခဲ့": "past", "လိမ့်မည်": "fut", "မည့်": "fut"}
# B10: (Pāli regex, Burmese string) counted per line
B10 = [(rf"\b{k}\b", v) for k, v in MS.ATTR.items() if k.endswith("ānaṃ") and k not in ("ñāṇasampayuttānaṃ",
                                                                                     "ñāṇavippayuttānaṃ")]
B10 += [(r"\bñāṇasampayuttānaṃ\b", MS.ATTR["ñāṇasampayuttānaṃ"]),
        (r"(?<![\w])(?:somanassena|Somanassena)\b", MS.ATTR["somanassena"]),
        (r"(?<![\w])(?:upekkhāya|Upekkhāya)\b", MS.ATTR["upekkhāya"]),
        (r"\b[Nn]a itthīnaṃ\b", MS.NEG_NOUN["itthīnaṃ"]), (r"\b[Nn]a purisānaṃ\b", MS.NEG_NOUN["purisānaṃ"]),
        (r"(?<!na )(?<!Na )\b(?:[Ii]tthīnaṃ|itthiyo)\b", f"{MS.ITTHI}{MS.PL}"),
        (r"(?<!na )(?<!Na )\b(?:[Pp]urisānaṃ|purisā)\b", f"{MS.PURISA}{MS.PL}"),
        (r"\bsacakkhukā\b", MS.ATTR["sacakkhukānaṃ"]), (r"\bsaghānakā\b", MS.ATTR["saghānakānaṃ"]),
        (r"eteneva bhāvena katici bhave dassetvā", MS.BHAVA),
        (r"[Pp]acchimacitt", MS.PACCHIMA_CITTA), (r"upapatticittassa", MS.GEN["upapatticittassa"]),
        (r"nirodhasamāpannānaṃ", MS.NAMED["nirodhasamāpannānaṃ"]),
        (r"[Pp]avatte\b", MS.PAVATTE), (r"\banantarā\b", MS.ANANTARA),
        (r"\b(?:itaresaṃ|itarāsaṃ)\b", "အခြား"),
        (r"\bno ca tāsaṃ\b|(?:kkhaṇe|vattamāne) tāsaṃ\b", "ထိုမိန်းမတို့")]     # harmonise B3: the pronoun tāsaṃ «ထိုမိန်းမတို့»
for q, qm in MS.QUAL.items():
    B10 += [(rf"(?i)\b{q}sampayutta(?:cittassa|pacchimacitta)", qm + MS.SAMP),
            (rf"(?i)\b{q}vippayuttacittassa", qm + MS.VIPP)]
B10G = {}
for _rx, _my in B10:
    B10G.setdefault(_my, []).append(_rx)


def canon(s):
    s = F.LABEL_RE.sub("", s.strip())
    s = re.sub(r"īti\?$", "i?", s)
    s = re.sub(r"āti\?$", "a?", s)
    return s


def sentences(b, mb):
    lab = F.LABEL_RE.match(b)
    b = F.LABEL_RE.sub("", b)
    mb = re.sub(r"^\([က-အ]\) ", "", mb)
    ps = F.SPLIT.split(nobr(b))
    ms = [x if x.endswith("။") else x + "။" for x in re.split(r"(?<=။) ", nobr(mb))]
    if len(ps) != len(ms):
        return None
    if lab and "vā pana" in ps[0]:
        ms[0] = ms[0].replace(F.VA_PANA + " ", "", 1)
    return list(zip(ps, ms))


LEAD_RE = re.compile(rf"^(?P<who>.+?) (?P<pro>{MS.PROR}) \S+ (?:ca )?(?:{F.VB})")


def leads(p_line):
    """(who, pro) of each answer sentence of a Pāli line."""
    out = []
    for s in F.SPLIT.split(nobr(body(p_line))):
        m = LEAD_RE.match(s)
        if m and not F.LABEL_RE.match(s) and not s.lower().startswith(("yassa", "yattha")):
            out.append((m["who"], m["pro"]))
    return out


REUSE = [   # (regex on the Pāli line, Burmese, book, block id, Pāli witness in that rails segment)
    (r"(?<![\w])n?uppajj", "ဖြစ်ပေါ်", "2", "^2-203", "uppajjamānā uppajjati"),
    (r"upapajj", "ပြန်လည် ဖြစ်ပေါ်", "2", "^2-1024", "kattha upapajjanti"),
    (r"\bcavant", "စုတေ", "2", "^2-1029", "cavanti āyusaṅkhayā"),
    (r"parinibb", "ပရိနိဗ္ဗာန် ပြု", "4", "^4-M-7", "parinibbāyī"),
    (r"pañcavokār", "အစုအဝေး ငါးပါး ရှိသော ဘဝ", "2", "^2-234", "pañcavokārabhavo"),
    (r"catuvokār", "အစုအဝေး လေးပါး ရှိသော ဘဝ", "2", "^2-234", "catuvokārabhavo"),
    (r"asaññasatt", "အသညသတ်", "2", "^2-18-4-3-0", "Asaññasattā"),
    (r"\barūp(?:aṃ|e|ā|ānaṃ)\b|arūpāvacar", "ရုပ်မရှိသော ဘုံ", "2", "^2-234", "arūpabhavo"),
    (r"(?<![\w])kāmāvacar", "ကာမဘုံ", "1", "^1-M2-93", "kāmāvacarā"),
    (r"(?<![\w])rūpāvacar", "သိမ်မွေ့သော ရုပ်ဘုံ", "1", "^1-M2-94", "rūpāvacarā"),
    (r"okās", "နေရာ", "4", "^4-M-11", "okās"),
    (r"\batīt", "အတိတ်", "1", "^1-M1-18", "atītā dhammā"),
    (r"\banāgat", "အနာဂတ်", "1", "^1-M1-18", "anāgatā dhammā"),
    (r"paccuppann", "ပစ္စုပ္ပန်", "1", "^1-M1-18", "paccuppannā dhammā"),
    (r"puggal", "ပုဂ္ဂိုလ်", "1", "^1-1050", "puggal"),
    (r"vāro\b", "ဖော်ပြချက်", "2", "^2-15-1-2-0", "Saccavāro"),
    (r"\byassa\b(?! cittassa)", "အကြင်သူအား", "2", "^2-199", "Idha yassa te honti"),
    (r"uppādakkhaṇe", "ဖြစ်ခြင်း ခဏ၌", "5", "^5-366", "Uppādakkhaṇe"),
    (r"bhaṅgakkhaṇe", "ပြိုပျက်ခြင်း ခဏ၌", "5", "^5-366", "bhaṅgakkhaṇe"),
    (r"citte vattamāne", "စိတ် ဖြစ်နေစဉ်", "5", "^5-556", "citte vattamāne"),
    (r"anantarā", "ချက်ချင်း နောက်၌", "2", "^2-751", "samanantarā"),
    (r"samaṅgī", "နှင့် ပြည့်စုံသူ", "1", "^1-1039", "Ariyamaggasamaṅgissa"),
    (r"[Ss]ahetuk", "အမြစ် ရှိ", "1", "^1-M2-2", "sahetukā dhammā"),
    (r"ñāṇa", "ဉာဏ်", "1", "^1-1", "ñāṇasampayuttaṃ"),
    (r"sampayutt", "နှင့် ယှဉ်တွဲ", "1", "^1-1", "ñāṇasampayuttaṃ"),
    (r"vippayutt", "နှင့် ကင်းကွာသော", "2", "^2-767", "upekkhāvippayuttā"),
    (r"(?i)somanass(?!indriy)", "ဝမ်းမြောက်မှု", "1", "^1-1", "somanassasahagataṃ"),
    (r"(?i)upekkh(?!indriy)", "ဥပေက္ခာ", "2", "^2-767", "Upekkhāsampayuttā"),
    (r"saddhāsamp|saddhāvipp", "ယုံကြည်မှု", "2", "^2-219", "saddhindriyaṃ"),
    (r"(?i)(?<![\w])itth(?!indriy)", "မိန်းမ", "2", "^2-219", "itthindriyaṃ"),
    (r"(?i)(?<![\w])puris(?!indriy)", "ယောက်ျား", "2", "^2-219", "purisindriyaṃ"),
    (r"(?i)\b(?:sa|a)cakkhuk", "မျက်စိ", "2", "^2-154", "cakkhāyatanaṃ"),
    (r"(?i)\b(?:sa|a)ghānak", "နှာခေါင်း", "2", "^2-154", "ghānāyatanaṃ"),
    (r"(?<![\w])citt", "စိတ်", "1", "^1-6", "cittaṃ"),
]
EXCEPT = [
    (r"anuloma|paccanīka", "pi-5 «အစဉ်အတိုင်း» / «ပြောင်းပြန်» (debate order)", "«အဟုတ်ပြ ပုံစံ» / «အငြင်းပြ ပုံစံ» (sample)"),
    (r"\bcavant", "pi-2 termbase cavati «သေသည်»", "pi-5 termbase and pi-2 ^2-1029 «စုတေ» (sample)"),
    (r"\bNatthi\b", "pi-3 ^3-410 Natthi «မရှိ။»", "«မရှိပါ။» (answer register; coordinator 2026-11-22)"),
    (r"uppādakkhaṇe", "pi-6 uppāda «ဖြစ်ပေါ်ခြင်း» (headings, sample)", "pi-5 ^5-366 «ဖြစ်ခြင်း ခဏ၌» (identical Pāli word; "
     "counted in C3 with pi-5), as ch. 5 / ch. 6-8"),
]


# ===================================================================================== the checks
def run_checks(PAIRS, rebuild=True, quiet=False):
    bad = []
    out = []

    def say(s):
        out.append(s)

    # A. rebuild
    if rebuild:
        for name in PAIRS:
            text, nbad = MS.run(name)
            if nbad or text != (MS.OUT / name).read_text(encoding="utf-8"):
                bad.append(f"A {name}: regenerated text differs")
        say(f"A. rebuild: {len(PAIRS)} / {len(PAIRS)} files regenerated identical" if not bad else "A. rebuild: FAILED")
    # B1
    n_lines = 0
    for name, (P, M, raw) in PAIRS.items():
        if len(P) != len(M):
            bad.append(f"B1 {name}: {len(P)} vs {len(M)} lines")
            continue
        if "\n\n\n" in raw:
            bad.append(f"B1 {name}: double blank line")
        if unicodedata.normalize("NFC", raw) != raw:
            bad.append(f"B1 {name}: not NFC")
        if any(0x1050 <= ord(c) <= 0x109F for c in raw):
            bad.append(f"B1 {name}: code point U+1050-U+109F")
        for i, (p, m) in enumerate(zip(P, M), 1):
            n_lines += 1
            e = MS.line_check(p, m)
            if e:
                bad.append(f"B1 {name}:{i} {e}")
    say(f"B1 structure: {n_lines} lines")
    # B2
    n_pol = 0
    for name, (P, M, _) in PAIRS.items():
        for i, (p, m) in enumerate(zip(P, M), 1):
            if HEAD.match(p):
                continue
            a, b = p_neg(pal(p)), m_neg(nobr(body(m)))
            n_pol += a
            if a != b:
                bad.append(f"B2 {name}:{i} negations Pāli {a} vs Burmese {b}")
    say(f"B2 polarity: {n_pol} negations, each one Burmese negative")
    # B3
    n_verb = n_ans = 0
    for name, (P, M, _) in PAIRS.items():
        for i, (p, m) in enumerate(zip(P, M), 1):
            if HEAD.match(p):
                continue
            s = pal(p)
            exp = []
            for x in P_VERB.finditer(s):
                neg = bool(x["na"] or x["n"])
                exp.append((x["r"].lower(), P_END[x["e"]], neg or bool(x["noca"]), neg and bool(x["noca"])))
            got = [(M_ROOT[y["r"]], M_T[y["t"]], bool(y["neg"]), bool(y["ns"])) for y in M_VERB.finditer(nobr(body(m)))]
            n_verb += len(exp)
            if exp != got:
                bad.append(f"B3 {name}:{i} verbs Pāli {exp} vs Burmese {got}")
            for pa, my in (("Āmantā", F.YES), ("Natthi", F.NATTHI)):
                k = len(re.findall(rf"\b{pa}\b", s))
                n_ans += k
                got = body(m).count(my[:-1])
                if k != got:
                    bad.append(f"B3 {name}:{i} «{pa}» {k}x vs «{my}» {got}x")
    say(f"B3 verbs: {n_verb} uppajj- verbs (root, tense, polarity, double negative) in order; {n_ans} answers")
    # B4
    n_pair = 0
    for name, (P, M, _) in PAIRS.items():
        lp = [F.LABEL_RE.match(p)[1] for p in P if F.LABEL_RE.match(p)]
        lm = [re.match(r"^\(([က-အ])\) ", m)[1] for m in M if re.match(r"^\(([က-အ])\) ", m)]
        n_pair += len(lp)
        if [F.AKKHARA[x] for x in lp] != lm:
            bad.append(f"B4 {name}: label sequence differs")
        for i, (p, m) in enumerate(zip(P, M), 1):
            if p.count("vā pana") != m.count(F.VA_PANA):
                bad.append(f"B4 {name}:{i} vā pana vs «{F.VA_PANA}»")
    say(f"B4 pairs: {n_pair} labelled lines in order, every «vā pana» = «{F.VA_PANA}»")
    # B5
    numw = [(r"[Pp]añca(?=vokār)", "ငါးပါး"), (r"[Cc]atu(?=vokār)", "လေးပါး"), (r"\bdutiye\b", "ဒုတိယ")]
    n_num = 0
    for name, (P, M, _) in PAIRS.items():
        for i, (p, m) in enumerate(zip(P, M), 1):
            if re.findall(r"\d", re.sub(r"\^\S+", "", p)) != re.findall(r"\d", re.sub(r"\^\S+", "", m)):
                bad.append(f"B5 {name}:{i} digits")
            for rx, my in numw:
                k = len(re.findall(rx, pal(p)))
                n_num += k
                if k != nobr(m).count(my):
                    bad.append(f"B5 {name}:{i} «{rx}» {k}x vs «{my}» {nobr(m).count(my)}x")
    say(f"B5 numbers: digits per line equal; {n_num} number words")
    # B6
    occ = {}
    for name, (P, M, _) in PAIRS.items():
        for i, (p, m) in enumerate(zip(P, M), 1):
            b, mb = body(p), body(m)
            if HEAD.match(b) or "…" in b:
                continue
            sp = sentences(b, mb)
            if sp is None:
                bad.append(f"B6 {name}:{i} sentence count differs")
                continue
            for x, y in sp:
                occ.setdefault(canon(x), {}).setdefault(y, name)
    n_shared = 0
    for name, (P, M) in OTHERS.items():
        for p, m in zip(P, M):
            b, mb = body(p), body(m)
            if HEAD.match(b) or "…" in b:
                continue
            sp = sentences(b, mb)
            for x, y in (sp or []):
                if canon(x) in occ:
                    n_shared += 1
                    occ[canon(x)].setdefault(y, name)
    for k, v in occ.items():
        if len(v) > 1:
            bad.append(f"B6 «{k[:70]}» has {len(v)} Burmese renderings ({sorted(set(v.values()))[:3]})")
    say(f"B6 recurring sentences: {len(occ)} distinct Pāli sentences, one Burmese each (also {n_shared} occurrences in "
        f"the finished pi-6 files)")
    # B7
    n_tab = 0
    for name, (P, M, _) in PAIRS.items():
        for i, (p, m) in enumerate(zip(P, M), 1):
            h = re.match(r"^(#+) (.*)$", body(p))
            if h:
                n_tab += 1
                if body(m) != f"{h[1]} {F.heading(h[2])}":
                    bad.append(f"B7 {name}:{i} heading")
    say(f"B7 table values: {n_tab} headings")
    # B8
    n_q = 0
    for name, (P, M, _) in PAIRS.items():
        for i, m in enumerate(M, 1):
            t = nobr(body(m))
            depth, ok = 0, True
            for ch in t:
                if ch == "“":
                    depth += 1
                    ok &= depth == 1
                elif ch == "”":
                    depth -= 1
                    ok &= depth == 0
                elif ch in "‘’":
                    ok &= depth == 1
            n_q += "“" in t
            if not ok or depth:
                bad.append(f"B8 {name}:{i} quote nesting")
    say(f"B8 quotes: {n_q} lines with quotes, nesting right")
    # B9
    n_fac = 0
    for name, (P, M, _) in PAIRS.items():
        for i, (p, m) in enumerate(zip(P, M), 1):
            if HEAD.match(p):
                continue
            exp = [FAC_STEM[FAC_SLIP.get(x.lower(), x.lower())] for x in P_FAC.findall(pal(p))]
            got = M_FAC.findall(nobr(body(m)))
            n_fac += len(exp)
            if exp != got:
                bad.append(f"B9 {name}:{i} faculties Pāli {len(exp)} vs Burmese {len(got)} (or order)")
    say(f"B9 faculties: {n_fac} faculty words in order, each its pi-2 name")
    # B10
    n_att = 0
    for name, (P, M, _) in PAIRS.items():
        for i, (p, m) in enumerate(zip(P, M), 1):
            s, t = pal(p), nobr(body(m))
            for my, rxs in B10G.items():
                k = sum(len(re.findall(rx, s, re.I)) for rx in rxs)
                n_att += k
                tc = (t.replace("ထိုမိန်းမတို့", "") if my == f"{MS.ITTHI}{MS.PL}" else t).count(my)   # B3
                if k != tc:
                    bad.append(f"B10 {name}:{i} «{rxs[0]}» {k}x vs «{my}» {tc}x")
    say(f"B10 persons / minds: {n_att} attributes, head nouns and qualifiers, each its Burmese")
    # C1
    n_c1 = s_c1 = 0
    for name, (P, M, _) in PAIRS.items():
        for i, (p, m) in enumerate(zip(P, M), 1):
            for st, my in FAC_STEM.items():
                if re.search(rf"(?<![\w]){st}(?=ṃ|ñca|mūlakaṃ)", pal(p), re.I):
                    n_c1 += 1
                    if my in m:
                        s_c1 += 1
                    else:
                        bad.append(f"C1 {name}:{i} «{st}» -> «{my}» missing")
    # C2
    n_c2 = s_c2 = 0
    for name, (P, M, _) in PAIRS.items():
        for i, (p, m) in enumerate(zip(P, M), 1):
            k = F.LABEL_RE.sub("", re.sub(r"^#+ ", "", body(p)))
            if k in FIN_LINE:
                n_c2 += 1
                if re.sub(r"^\([က-အ]\) ", "", re.sub(r"^#+ ", "", body(m))) in FIN_LINE[k]:
                    s_c2 += 1
                else:
                    bad.append(f"C2 {name}:{i} «{k[:50]}»")
            ka = len(re.findall(r"\bĀmantā\b", body(p)))
            n_c2 += ka
            got = min(ka, body(m).count("ဟုတ်ပါသည်"))
            s_c2 += got
            if got < ka:
                bad.append(f"C2 {name}:{i} Āmantā")
    if "Āmantā" not in " ".join(FIN["5"]["^5-1"][0]) or "ဟုတ်ပါသည်" not in " ".join(FIN["5"]["^5-1"][1]):
        bad.append("C2 witness Āmantā")
    # C3
    n_c3 = s_c3 = 0
    for rx, my, bk, bid, wit in REUSE:
        pl, ml = FIN[bk][bid]
        if wit.lower() not in " ".join(pl).lower() or my not in " ".join(ml):
            bad.append(f"C3 witness pi-{bk} {bid}: «{wit}» / «{my}»")
            continue
        for name, (P, M, _) in PAIRS.items():
            for i, (p, m) in enumerate(zip(P, M), 1):
                if re.search(rx, pal(p)):
                    n_c3 += 1
                    if my in m:
                        s_c3 += 1
                    else:
                        bad.append(f"C3 {name}:{i} «{rx}» -> «{my}» missing")
    # C4 pi-6 leads shared with the finished chapters
    mine = {}
    for name, (P, M, _) in PAIRS.items():
        for p, m in zip(P, M):
            for w, pr in leads(p):
                mine.setdefault((w, pr), F.who_my(w, pr))
    shared = {k for P, _ in OTHERS.values() for p in P for k in leads(p) if k in mine}
    for name, (P, M, _) in PAIRS.items():           # my own lines carry that Burmese at every occurrence
        for i, (p, m) in enumerate(zip(P, M), 1):
            for k in leads(p):
                if k in shared and mine[k] not in m:
                    bad.append(f"C4 {name}:{i} lead «{k[0][:60]}»: «{mine[k][:60]}» missing")
    n_c4 = s_c4 = 0
    for oname, (P, M) in OTHERS.items():
        for i, (p, m) in enumerate(zip(P, M), 1):
            for w, pr in leads(p):
                if (w, pr) in mine:
                    n_c4 += 1
                    if mine[(w, pr)] in nobr(m):          # a variant bracket of the finished line taken out
                        s_c4 += 1
                    else:
                        bad.append(f"C4 {oname}:{i} lead «{w[:60]}» {pr}: «{mine[(w, pr)][:60]}» not in the finished line")
    n_lead_shared = len(shared)
    total_n, total_s = n_c1 + n_c2 + n_c3 + n_c4, s_c1 + s_c2 + s_c3 + s_c4
    say(f"C. reuse test: {total_s} / {total_n} identical (C1 faculty names {s_c1}/{n_c1}, C2 whole lines and answers "
        f"{s_c2}/{n_c2}, C3 {len(REUSE)} reused terms {s_c3}/{n_c3}, C4 pi-6 leads shared with finished chapters "
        f"{s_c4}/{n_c4} occurrences" + (f", {n_lead_shared} distinct leads)" if not quiet else ")"))
    n_ex = sum(1 for rx, _, _ in EXCEPT for P, _, _ in PAIRS.values() for p in P if re.search(rx, pal(p)))
    say(f"   documented exceptions: {len(EXCEPT)} terms on {n_ex} lines")
    for rx, fin, ours in EXCEPT:
        say(f"   - {rx}: final {fin}; here {ours}")
    if not quiet:
        print("\n".join(out))
    return bad


def load(names):
    res = {}
    for n in names:
        raw = (MS.OUT / n).read_text(encoding="utf-8")
        res[n] = (nonempty(MS.PALI / n), nonempty_text(raw), raw)
    return res


def mutate():
    """Single mutations of the generated Burmese; each must raise at least one new mismatch."""
    base = load(NAMES)
    muts = [
        ("dropped «မ»", "မဖြစ်ပေါ်", "ဖြစ်ပေါ်"),
        ("dropped «ခဲ့»", "ဖြစ်ပေါ်ခဲ့သည်", "ဖြစ်ပေါ်သည်"),
        ("future -> present", "ဖြစ်ပေါ်လိမ့်မည်လော", "ဖြစ်ပေါ်သလော"),
        ("dropped double negative", "သည်ကား မဟုတ်", "သည်"),
        ("Āmantā -> No", "ဟုတ်ပါသည်။", "မဟုတ်ပါ။"),
        ("Natthi changed", "မရှိပါ။", "မရှိ။"),
        ("faculty swapped", "ဝမ်းမြောက်မှု၏ စွမ်းရည်", "ဥပေက္ခာ၏ စွမ်းရည်"),
        ("faculty dropped", "ယုံကြည်မှု၏ စွမ်းရည်… ", ""),
        ("attribute polarity", "မျက်စိ ရှိလျက်", "မျက်စိ မရှိဘဲ"),
        ("na itthīnaṃ dropped", "မိန်းမ မဟုတ်ဘဲ ", ""),
        ("head noun changed", "မိန်းမတို့", "ယောက်ျားတို့"),
        ("qualifier flipped", "ဉာဏ်နှင့် ယှဉ်တွဲသော", "ဉာဏ်နှင့် ကင်းကွာသော"),
        ("dropped «တစ်ဖန်»", "တစ်ဖန် ", ""),
        ("label changed", "(ခ) ", "(ဂ) "),
        ("lead changed", "ကာမဘုံ၌ ရှိသော အခြားသူတို့", "ကာမဘုံ၌ ရှိသူတို့"),
        ("bhāva phrase changed", "ဤ အဖြစ်ဖြင့်ပင်", "ဤ အဖြစ်ဖြင့်"),
    ]
    ok = True
    for label, a, b in muts:
        for n in NAMES:
            P, M, raw = base[n]
            idx = next((i for i, m in enumerate(M) if a in m), None)
            if idx is None:
                continue
            M2 = list(M)
            M2[idx] = M2[idx].replace(a, b, 1)
            pairs = dict(base)
            pairs[n] = (P, M2, raw.replace(M[idx], M2[idx], 1))
            bad = run_checks(pairs, rebuild=False, quiet=True)
            caught = [x for x in bad if not x.startswith("C4")] or bad
            print(f"  mutation «{label}» in {n}:{idx + 1}: {'caught' if bad else 'NOT CAUGHT'} "
                  f"({caught[0][:80] if bad else ''})")
            ok &= bool(bad)
            break
        else:
            print(f"  mutation «{label}»: no line to mutate")
    print("mutation test:", "all caught" if ok else "FAILED")
    return ok


if __name__ == "__main__":
    if "--mutate" in sys.argv:
        sys.exit(0 if mutate() else 1)
    bad = run_checks(load(NAMES))
    print(f"\nmismatches: {len(bad)}")
    for b in bad[:60]:
        print("  ", b)
    sys.exit(1 if bad else 0)
