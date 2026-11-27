"""Check the Burmese zero-shot of pi-6 group ch9-10a (9-01 … 9-03 Dhammayamaka, 10-01 … 10-04 Indriyayamaka) line by
line (adapted from check_sample.py / check_ch2-02-4-5.py).

usage: python3 -I -X utf8 check_ch9-10a.py [chapter ...] [--mutate]
  A. rebuild: make_ch9-10a.py regenerates the files byte for byte (nothing written here);
  B. per line: B1 structure (equal non-empty lines, dashes, ellipses, «[», item numbers, labels (Ka) … = (က) …, block
     IDs, heading levels, no «?» «।» «:-», final «။», NFC, no U+1050-U+109F, no double blank line); B2 POLARITY: every
     Pāli negation (na, no, nuppajjati, nappajahati, Natthi) is one Burmese negative (မဟုတ် / မရှိ / မ + verb); fixed
     terms masked (abyākata, ahetuka, arūpa, a-X-ka «X မရှိဘဲ», vinā «မပါဘဲ», «သို့မဟုတ်»); B3 VERBS: the sequence of
     uppajj- / nirujjh- verbs of each line with tense (present / past -ittha / future -issati), polarity and «no ca …
     na V» double negative equals the Burmese sequence; the same for bhāveti / pajahati; Āmantā = «ဟုတ်ပါသည်»,
     Natthi = «မရှိပါ။»; plural subjects (kusalā dhammā …) take «ကြ» on every verb, singular ones (the faculties) none;
     B4 (Ka) / (Kha) labels in order, «vā pana» = «တစ်ဖန်»; B5 digits and number words; B6 every recurring Pāli
     sentence (labels off, «-ti?» = «?») has one Burmese, TOGETHER WITH the finished pi-6 chapters (sample, ch2-02-4-5,
     ch3, ch6-8: read only); B7 headings / colophons / table lines = their table value; B8 quotes nested “…” ‘…’;
     B9 women frames: «tāsaṃ» = «ထိုမိန်းမတို့အား» / «…မိန်းမတို့အား», every itthīnaṃ / purisānaṃ / na itthīnaṃ … has its
     Burmese;
  C. reuse test against the FINAL pi-1 … pi-5 rails texts, read here independently of my6_formulas:
     C1 the 22 faculty names (pi-2 ^2-221) on every line whose Pāli has the name; C2 whole lines / answers that also
     occur in pi-1 … pi-5; C3 every reused term of REUSE (a rails segment has the Pāli and the Burmese; every line of
     this group whose Pāli has the term has that Burmese). Documented exceptions (EXCEPT) are listed, not counted.
  --mutate: mutation test (a dropped «မ», a dropped «ခဲ့», a dropped «ကြ», «ထိုမိန်းမတို့» -> «ထိုသူတို့», a changed faculty
     name, a dropped «တစ်ဖန်», «ဟုတ်ပါသည်» -> «မဟုတ်ပါ», future -> present): each must be caught.
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
_spec = importlib.util.spec_from_file_location("make_ch9_10a", HERE / "make_ch9-10a.py")
MS = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(MS)                   # tables only; the generator writes files only under __main__
F = MS.F
ROOT = HERE.parents[3]
NAMES = [a for a in sys.argv[1:] if not a.startswith("-")] or MS.NAMES_OUT
FINISHED = ["1-mulayamaka.md", "2-01-khandhayamaka.md", "2-02-khandhayamaka.md", "4-dhatuyamaka.md",
            "5-01-saccayamaka.md", "5-02-saccayamaka.md", "5-03-saccayamaka.md", "6-01-sankharayamaka.md",
            "6-02-sankharayamaka.md", "8-cittayamaka.md"] + [f"3-0{i}-ayatanayamaka.md" for i in range(1, 7)]


def nonempty(p):
    return [l for l in p.read_text(encoding="utf-8-sig").splitlines() if l.strip()]


def body(l):
    return F.strip_id(l).strip()


def nobr(s):
    return re.sub(r" ?\[[^\]]*\]", "", s)


HEAD = re.compile(r"^#+ ")
ID_RE = re.compile(r" (\^[0-9A-Za-z-]+)\s*$")


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


# ===================================================================================== FINAL pi-1 … pi-5 (read here)
FIN, FIN_LINE = {}, {}
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
IND_FIN = dict(zip(*[[x.strip() for x in nobr(body(FIN["2"]["^2-221"][j][0])).split(" – ")[1].rstrip(".။").split(sep)]
                     for j, sep in ((0, ","), (1, "၊"))]))

# ===================================================================================== masks, regexes
MASK = [F.ABY, F.AHETUKA, F.PLACES["arūpa"], MS.VINA, "သို့မဟုတ်"]
MASK += [v for k, v in MS.IND_ATTR.items() if re.match(r"^a(?!ñ)", k)]          # a-X-ka «X မရှိဘဲ»
MASK.sort(key=len, reverse=True)
P_VERB = re.compile(r"(?P<noca>no ca (?:tesaṃ tattha|tāsaṃ tattha|tesaṃ|tāsaṃ|tattha) (?:\S+ ){1,2}?)?(?P<na>na )?(?P<n>n)?"
                    r"(?P<r>uppajj|nirujjh)(?P<e>issanti|issantīti|issati|issatīti|ittha|itthāti|anti|antīti|ati|atīti)"
                    r"(?![\w])", re.I)
P_END = {"issanti": "fut", "issantīti": "fut", "issati": "fut", "issatīti": "fut", "ittha": "past", "itthāti": "past",
         "anti": "pres", "antīti": "pres", "ati": "pres", "atīti": "pres"}
M_VERB = re.compile(r"(?<!ပြန်လည် )(?P<neg>မ)?(?P<r>ဖြစ်ပေါ်|ချုပ်ငြိမ်း)(?!လာ|ခြင်း|ပြီး|ဆဲ)(?P<k1>ကြ)?"
                    r"(?P<t>ခဲ့|လိမ့်မည်|မည့်)?(?P<k2>ကြ)?(?P<ns>(?:သည်)?ကား မဟုတ်)?")
M_ROOT = {"ဖြစ်ပေါ်": "uppajj", "ချုပ်ငြိမ်း": "nirujjh"}
M_T = {None: "pres", "ခဲ့": "past", "လိမ့်မည်": "fut", "မည့်": "fut"}
B_VERB = re.compile(r"(?P<na>na |nap)?(?P<r>bhāvet|pajah|ppajah)")
BM_VERB = re.compile(r"(?P<n>မ)?(?P<r>ပွားများ(?!ခြင်း)|ပယ်)")
PLURAL_P = re.compile(r"\b(?:kusalā|akusalā|abyākatā)(?: ca)? dhammā\b", re.I)
NUMW = [(r"pañca(?=vokār)|Pañca(?=vokār)", "ငါးပါး"), (r"[Cc]atu(?=vokār)", "လေးပါး"), (r"\bBāvīsat", "နှစ်ဆယ့်နှစ်ပါး"),
        (r"\b[Dd]utiye\b", "ဒုတိယ")]
NEG_MY = ["မဟုတ်", "မရှိ", "မဖြစ်ပေါ်", "မချုပ်ငြိမ်း", "မပယ်", "မပွားများ"]


def p_neg(p):
    s = nobr(body(p))
    return (len(re.findall(r"(?<![\w])(?:na|no|No|Na)(?![\w])", s)) + len(re.findall(r"nuppajj|nappajah", s))
            + len(re.findall(r"\b[Nn]atthi\b", s)))


def m_neg(m):
    s = nobr(body(m))
    for t in MASK:
        s = s.replace(t, "")
    return sum(s.count(w) for w in NEG_MY)


def canon(s):
    s = F.LABEL_RE.sub("", s.strip())
    s = re.sub(r"nti\?$", "ṃ?", s)
    s = re.sub(r"(?<=[āaoe])ti\?$", "?", s)
    s = re.sub(r"īti\?$", "i?", s)
    s = re.sub(r"āti\?$", "a?", s)
    return s.replace("ti. ", "? ") if s.endswith("ti.") else s


REUSE = [   # (regex on the Pāli line, Burmese, book, block id, Pāli witness in that rails segment)
    (r"(?<![\w])[Kk]usalā(?: ca)? dhammā", "ကုသိုလ် သဘောတရားများ", "1", "^1-M1-1", "(Ka) kusalā dhammā"),
    (r"\b[Aa]kusalā(?: ca)? dhammā", "အကုသိုလ် သဘောတရားများ", "1", "^1-M1-1", "(Kha) akusalā dhammā"),
    (r"[Aa]byākat", F.ABY, "1", "^1-M1-1", "abyākatā dhammā"),
    (r"kusalākusalānaṃ", "ကုသိုလ်နှင့် အကုသိုလ် သဘောတရားတို့", "1", "^1-583", "Kusalākusalānaṃ dhammānaṃ"),
    (r"(?<![\w])akusalānaṃ", "အကုသိုလ် သဘောတရားတို့", "1", "^1-30", "akusalānaṃ dhammānaṃ"),
    (r"\bahetuk", "အမြစ် မရှိ", "1", "^1-M2-2", "ahetukā dhammā"),
    (r"\bsahetuk", "အမြစ် ရှိ", "1", "^1-M2-2", "sahetukā dhammā"),
    (r"ñāṇasampayutt", "ဉာဏ်နှင့် ယှဉ်တွဲ", "1", "^1-1", "ñāṇasampayuttaṃ"),
    (r"ñāṇavippayutt", "ဉာဏ်နှင့် ကင်းကွာ", "1", "^1-147", "ñāṇavippayuttaṃ"),
    (r"\bavases", "ကြွင်းကျန်သော", "2", "^2-796", "avasesā paññā"),
    (r"ṭhapetvā", "ချန်ထား၍", "2", "^2-796", "ṭhapetvā"),
    (r"(?<![\w])n?uppajj(?!antīnaṃ)", "ဖြစ်ပေါ်", "2", "^2-203", "uppajjamānā uppajjati"),
    (r"nirujjh", "ချုပ်ငြိမ်း", "2", "^2-204", "nirujjhamānā nirujjhati"),
    (r"upapajj", "ပြန်လည် ဖြစ်ပေါ်", "2", "^2-1024", "kattha upapajjanti"),
    (r"\bcavant", "စုတေ", "2", "^2-1029", "cavanti āyusaṅkhayā"),
    (r"pañcavokār", "အစုအဝေး ငါးပါး ရှိသော ဘဝ", "2", "^2-234", "pañcavokārabhavo"),
    (r"catuvokār", "အစုအဝေး လေးပါး ရှိသော ဘဝ", "2", "^2-234", "catuvokārabhavo"),
    (r"asaññasatt", "အသညသတ်", "2", "^2-18-4-3-0", "Asaññasattā"),
    (r"\barūp(?:aṃ|e|ā|ānaṃ)\b|arūpāvacar", "ရုပ်မရှိသော ဘုံ", "2", "^2-234", "arūpabhavo"),
    (r"\bkāmāvacare", "ကာမဘုံ", "1", "^1-M2-93", "kāmāvacarā"),
    (r"\b[Rr]ūpāvacare", "သိမ်မွေ့သော ရုပ်ဘုံ", "1", "^1-M2-94", "rūpāvacarā"),
    (r"okās", "နေရာ", "4", "^4-M-11", "okās"),
    (r"\b[Aa]tīt", "အတိတ်", "1", "^1-M1-18", "atītā dhammā"),
    (r"\b[Aa]nāgat", "အနာဂတ်", "1", "^1-M1-18", "anāgatā dhammā"),
    (r"[Pp]accuppann", "ပစ္စုပ္ပန်", "1", "^1-M1-18", "paccuppannā dhammā"),
    (r"\buddes", "အကျဉ်း ဖော်ပြချက်", "3", "^3-1-0", "Uddeso"),
    (r"niddes", "အကျယ် ဖော်ပြချက်", "1", "^1-2-3-1-0", "Ekakaniddeso"),
    (r"[Ss]uddha(?!vās)", "ရိုးရိုး", "5", "^5-1-1-0", "Suddh"),
    (r"[Pp]aṇṇatti", "သတ်မှတ်ချက်", "1", "^1-M2-108", "paññatti"),
    (r"puggal", "ပုဂ္ဂိုလ်", "1", "^1-1050", "puggal"),
    (r"[Uu]ppāda(?!kkhaṇ)", "ဖြစ်ပေါ်ခြင်း", "1", "^1-1-0", "Cittuppādakaṇḍaṃ"),
    (r"[Nn]irodha(?!samāp)", "ချုပ်ငြိမ်းခြင်း", "1", "^1-1063", "nirodh"),
    (r"vāro\b", "ဖော်ပြချက်", "2", "^2-15-1-2-0", "Saccavāro"),
    (r"\byassa\b(?! cittassa)", "အကြင်သူအား", "2", "^2-199", "Idha yassa te honti"),
    (r"niṭṭhit", "” ပြီးဆုံးပြီ။", "2", "^2-153", "Khandhavibhaṅgo niṭṭhito"),
    (r"aggamagg", "အမြတ်ဆုံး မဂ်", "2", "^2-1029", "agga"),
    (r"arahant", "ရဟန္တာ", "5", "^5-546", "arahantānaṃ"),
    (r"samaṅgī", "နှင့် ပြည့်စုံသူ", "1", "^1-1039", "Ariyamaggasamaṅgissa"),
    (r"paṭilabh", "ရရှိ", "2", "^2-974", "paṭilabhati"),
    (r"uppādakkhaṇe", "ဖြစ်ခြင်း ခဏ၌", "5", "^5-366", "Uppādakkhaṇe"),
    (r"bhaṅgakkhaṇe", "ပြိုပျက်ခြင်း ခဏ၌", "5", "^5-366", "bhaṅgakkhaṇe"),
    (r"citte vattamāne", "စိတ် ဖြစ်နေစဉ်", "5", "^5-556", "citte vattamāne"),
    (r"anantarā", "ချက်ချင်း နောက်၌", "2", "^2-751", "samanantarā"),
    (r"[Dd]ibbacakkhu", "နတ်မျက်စိ", "5", "^5-374", "dibbacakkhuṃ"),
    (r"paññācakkhu", "ပညာမျက်စိ", "5", "^5-374", "paññācakkhu"),
    (r"[Dd]ibbasot", "နတ်နား", "5", "^5-375", "dibbasotaṃ"),
    (r"\bindriy(?:aṃ|anti|añca|añceva|ā|e)(?![\w])", "စွမ်းရည်", "1", "^1-1", "indriy"),
    (r"[Ii]ndriyayamak", "စွမ်းရည်များကို အတွဲလိုက် မေးဖြေခြင်း", "1", "^1-1", "indriy"),
    (r"[Bb]hāvet", "ပွားများ", "5", "^5-390", "maggaṃ bhāvetīti"),
    (r"pajah", "ပယ်", "5", "^5-317", "pajahaṃ"),
    (r"[Bb]hāvanā", "ဘာဝနာ ပွားများခြင်း", "1", "^1-M1-8", "bhāvanāya pahātabbā"),
    (r"(?<![\w])itthīnaṃ", "မိန်းမ", "2", "^2-219", "itthindriyaṃ"),
    (r"(?<![\w])purisānaṃ", "ယောက်ျား", "2", "^2-219", "purisindriyaṃ"),
    (r"(?<![\w])somanass(?:ena|a)", "ဝမ်းမြောက်မှု", "2", "^2-219", "somanassindriyaṃ"),
    (r"(?<![\w])upekkhā(?:ya|sampayutt|vippayutt)", "ဥပေက္ခာ", "2", "^2-219", "upekkhindriyaṃ"),
    (r"saddhā(?:sampayutt|vippayutt)", "ယုံကြည်မှု", "2", "^2-219", "saddhindriyaṃ"),
    (r"(?<![Vv]inā )\b(?:[Ss]omanassena|[Uu]pekkhāya) (?:upapajj|\w+kānaṃ)", "နှင့်အတူ", "1", "^1-M1-7", "upekkhāsahagatā"),
    (r"\bvinā\b", "မပါဘဲ", "5", "^5-227", "vinā rūpena"),
]
REUSE += [(rf"(?<![\w]){k[:-1]}(?:ṃ|nti|ñca|ñceva)(?![\w])", v, "2", "^2-221", k) for k, v in MS.IND.items()]
EXCEPT = [
    (r"anuloma|paccanīka", "pi-5 «အစဉ်အတိုင်း» / «ပြောင်းပြန်» (debate order)", "«အဟုတ်ပြ ပုံစံ» / «အငြင်းပြ ပုံစံ» "
     "(sample decision)"),
    (r"\bcavant", "pi-2 termbase cavati «သေသည်»", "pi-5 termbase and pi-2 ^2-1029 «စုတေ» (sample decision)"),
    (r"\bNatthi\.", "pi-3 ^3-410 Natthi «မရှိ။»", "«မရှိပါ။» (answer register, coordinator 2026-11-22)"),
    (r"[Dd]ibbasotaṃ taṇhāsotaṃ", "bare sotaṃ «နား»", "«“သောတ”» in these two sentences (as ch. 3 / ch2-02-4-5)"),
    (r"uppādakkhaṇe", "pi-6 uppāda «ဖြစ်ပေါ်ခြင်း» (headings)", "pi-5 ^5-366 «ဖြစ်ခြင်း ခဏ၌» (as ch2-02-4-5 / ch6-8)"),
    (r"[Aa]naññātaññassāmīti(?!ndriy|ñ)|[Aa]naññātaññāssāmīti", "pi-2 indriya «မသိရသေးသည်ကို သိရတော့မည်ဟူသော စွမ်းရည်»",
     "bare word = the name without «ဟူသော စွမ်းရည်», quoted «“မသိရသေးသည်ကို သိရတော့မည်”» (NEW)"),
]


SA_FORMS = {k: v for k, v in MS.IND_ATTR.items() if MS.SA_RE.match(k)}


def check(PAIRS, rebuild=True, verbose=True):
    bad, cnt = [], {}
    # A. rebuild
    if rebuild:
        for name in PAIRS:
            text, nbad = MS.run(name)
            if nbad or text != (MS.OUT / name).read_text(encoding="utf-8"):
                bad.append(f"A {name}: regenerated text differs")
    # B1 structure
    n = 0
    for name, (P, M) in PAIRS.items():
        if len(P) != len(M):
            bad.append(f"B1 {name}: {len(P)} vs {len(M)} lines")
            continue
        if rebuild:
            raw = (MS.OUT / name).read_text(encoding="utf-8")
            if "\n\n\n" in raw:
                bad.append(f"B1 {name}: double blank line")
            if unicodedata.normalize("NFC", raw) != raw:
                bad.append(f"B1 {name}: not NFC")
            if any(0x1050 <= ord(c) <= 0x109F for c in raw):
                bad.append(f"B1 {name}: code point U+1050-U+109F")
        for i, (p, m) in enumerate(zip(P, M), 1):
            n += 1
            e = MS.line_check(p, m)
            if e:
                bad.append(f"B1 {name}:{i} {e}")
    cnt["B1"] = n
    # B2 polarity
    n = 0
    for name, (P, M) in PAIRS.items():
        for i, (p, m) in enumerate(zip(P, M), 1):
            if HEAD.match(p):
                continue
            a, b = p_neg(p), m_neg(m)
            n += a
            if a != b:
                bad.append(f"B2 {name}:{i} negations Pāli {a} vs Burmese {b}")
    cnt["B2"] = n
    # B3 verbs, plural, answers
    nv = nb = na = 0
    for name, (P, M) in PAIRS.items():
        dh = name.startswith("9-")
        for i, (p, m) in enumerate(zip(P, M), 1):
            if HEAD.match(p):
                continue
            s = nobr(body(p))
            exp = []
            for x in P_VERB.finditer(s):
                neg = bool(x["na"] or x["n"])
                short = (x.start() == 0 or s[x.start() - 2:x.start()] == "? ") and s[x.end():x.end() + 1] == "." \
                    and not x["noca"]                         # a bare short answer «Uppajjittha.»: number of the verb form
                pl = x["e"] in ("anti", "antīti", "issanti", "issantīti") or (dh and not short)
                exp.append((x["r"].lower(), P_END[x["e"]], neg or bool(x["noca"]), neg and bool(x["noca"]), pl))
            got = [(M_ROOT[y["r"]], M_T[y["t"]], bool(y["neg"]), bool(y["ns"]), bool(y["k1"] or y["k2"]))
                   for y in M_VERB.finditer(nobr(body(m)))]
            nv += len(exp)
            if exp != got:
                bad.append(f"B3 {name}:{i} verbs Pāli {exp} vs Burmese {got}")
            bexp = [("bh" if "bhāv" in x["r"] else "pa", bool(x["na"])) for x in B_VERB.finditer(s)]
            bgot = [("bh" if y["r"].startswith("ပွား") else "pa", bool(y["n"])) for y in BM_VERB.finditer(nobr(body(m)))]
            if not re.search(r"[Bb]hāvanā", s):
                nb += len(bexp)
                if bexp != bgot:
                    bad.append(f"B3 {name}:{i} bhāveti / pajahati Pāli {bexp} vs Burmese {bgot}")
            for pa, my in (("Āmantā", F.YES), ("Natthi.", F.NATTHI), ("No.", F.NO)):
                k = len(re.findall("[Āā]mantā", s)) if pa == "Āmantā" else len(re.findall(r"(?:^|\? )" + re.escape(pa), s))
                na += k
                got = body(m).count(F.YES[:-1]) if pa == "Āmantā" else len(
                    re.findall(r"(?:^|လော။ |^\([က-အ]\) )" + my, body(m)))
                if k != got:
                    bad.append(f"B3 {name}:{i} «{pa}» {k}x vs «{my}» {got}x")
    cnt["B3"] = (nv, nb, na)
    # B4 pairs
    n = 0
    for name, (P, M) in PAIRS.items():
        lp = [F.LABEL_RE.match(p)[1] for p in P if F.LABEL_RE.match(p)]
        lm = [re.match(r"^\(([က-အ])\) ", m)[1] for m in M if re.match(r"^\(([က-အ])\) ", m)]
        n += len(lp)
        if [F.AKKHARA[x] for x in lp] != lm:
            bad.append(f"B4 {name}: label sequence differs")
        for i, (p, m) in enumerate(zip(P, M), 1):
            if p.count("vā pana") != m.count(F.VA_PANA):
                bad.append(f"B4 {name}:{i} vā pana vs «{F.VA_PANA}»")
    cnt["B4"] = n
    # B5 numbers
    n = 0
    for name, (P, M) in PAIRS.items():
        for i, (p, m) in enumerate(zip(P, M), 1):
            s = nobr(body(p))
            if re.findall(r"\d", re.sub(r"\^\S+", "", p)) != re.findall(r"\d", re.sub(r"\^\S+", "", m)):
                bad.append(f"B5 {name}:{i} digits")
            for rx, my in NUMW:
                k = len(re.findall(rx, s))
                n += k
                if k != nobr(m).count(my):
                    bad.append(f"B5 {name}:{i} «{rx}» {k}x vs «{my}» {nobr(m).count(my)}x")
    cnt["B5"] = n
    # B6 recurring sentences (with the finished pi-6 chapters, read only)
    occ = {}
    allp = dict(PAIRS)
    for f in FINISHED:
        if (MS.OUT / f).exists():
            allp[f] = (nonempty(MS.PALI / f), nonempty(MS.OUT / f))
    shared = 0
    for name, (P, M) in allp.items():
        mine = name in PAIRS
        for i, (p, m) in enumerate(zip(P, M), 1):
            b, mb = body(p), body(m)
            if HEAD.match(b) or "…" in b or b in F.COLO or nobr(b) in F.LINES or F.BRACKET.sub("⟦v⟧", b) in F.LINES:
                continue
            lab = F.LABEL_RE.match(b)
            b = F.LABEL_RE.sub("", b)
            mb = re.sub(r"^\([က-အ]\) ", "", mb)
            ps = F.SPLIT.split(nobr(b))
            ms = [x if x.endswith(("။", "။)")) else x + "။" for x in re.split(r"(?<=။) |(?<=။\)) ", nobr(mb))]
            if len(ps) != len(ms):
                if mine:
                    bad.append(f"B6 {name}:{i} {len(ps)} Pāli vs {len(ms)} Burmese sentences")
                continue
            for j, (x, y) in enumerate(zip(ps, ms)):
                k = canon(x)
                if j == 0 and lab and "vā pana" in x:
                    y = y.replace(F.VA_PANA + " ", "", 1)
                occ.setdefault(k, {}).setdefault(y, set()).add("mine" if mine else name)
    nrec = 0
    for k, v in occ.items():
        srcs = set().union(*v.values())
        if "mine" not in srcs:
            continue
        nrec += 1
        if len(srcs) > 1:
            shared += 1
        if len(v) > 1:
            bad.append(f"B6 «{k[:70]}» has {len(v)} Burmese renderings: {[(y[:60], sorted(z)) for y, z in v.items()]}")
    cnt["B6"] = (nrec, shared)
    # B7 table values
    n = 0
    for name, (P, M) in PAIRS.items():
        for i, (p, m) in enumerate(zip(P, M), 1):
            b, mb = body(p), body(m)
            h = re.match(r"^(#+) (.*)$", b)
            if h:
                n += 1
                if mb != f"{h[1]} {F.heading(h[2])}":
                    bad.append(f"B7 {name}:{i} heading")
                continue
            bl = F.LABEL_RE.sub("", b)
            mbl = re.sub(r"^\([က-အ]\) ", "", mb)
            if bl in F.COLO:
                n += 1
                if mbl != F.COLO[bl]:
                    bad.append(f"B7 {name}:{i} colophon")
            elif bl in F.LINES:
                n += 1
                if mbl != F.LINES[bl]:
                    bad.append(f"B7 {name}:{i} line table")
            elif F.BRACKET.sub("⟦v⟧", bl) in F.LINES:
                n += 1
                if nobr(mbl) != nobr(F.LINES[F.BRACKET.sub("⟦v⟧", bl)].format(v="")):
                    bad.append(f"B7 {name}:{i} line table")
    cnt["B7"] = n
    # B8 quotes
    n = 0
    for name, (P, M) in PAIRS.items():
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
            n += "“" in t
            if not ok or depth:
                bad.append(f"B8 {name}:{i} quote nesting")
    cnt["B8"] = n
    # B9 women / men / attributes
    n = 0
    for name, (P, M) in PAIRS.items():
        for i, (p, m) in enumerate(zip(P, M), 1):
            s = nobr(body(p))
            for rx, my in ((r"\bno ca tāsaṃ\b", f"{F.BUT} {MS.PRO['tāsaṃ']}"), (r"\btāsaṃ\b", f"{MS.ITTHI}တို့အား"),
                           (r"\bupapajjantīnaṃ\b|\buppajjantīnaṃ\b", f"{MS.REBORN} {MS.ITTHI}တို့"),
                           (r"\b[Nn]a (?:itthīnaṃ)", MS.IND_ATTR["na itthīnaṃ"]),
                           (r"\b[Nn]a (?:purisānaṃ)", MS.IND_ATTR["na purisānaṃ"]),
                           (r"(?<![Nn]a )\b[Pp]urisānaṃ", f"{MS.PURISA}တို့"),
                           (r"\b[Vv]inā somanassena", MS.IND_ATTR["vinā somanassena"]),
                           (r"(?<![Vv]inā )\b[Ss]omanassena", MS.IND_ATTR["somanassena"]),
                           (r"\b[Vv]inā upekkhāya", MS.IND_ATTR["vinā upekkhāya"]),
                           (r"(?<![Vv]inā )\b[Uu]pekkhāya", MS.IND_ATTR["upekkhāya"]),
                           (r"\b[Ññ]āṇasampayuttānaṃ", MS.IND_ATTR["ñāṇasampayuttānaṃ"]),
                           (r"\b[Ññ]āṇavippayuttānaṃ", MS.IND_ATTR["ñāṇavippayuttānaṃ"])):
                k = len(re.findall(rx, s))
                if k:
                    n += k
                    if nobr(body(m)).count(my) < k:
                        bad.append(f"B9 {name}:{i} «{rx}» {k}x vs «{my}» {nobr(body(m)).count(my)}x")
            for key, my in SA_FORMS.items():          # sa-X-ka «X ရှိလျက်» / a-X-ka «X မရှိဘဲ»: equal counts
                k = len(re.findall(rf"(?<![\w]){key}(?![\w])", s, re.I))
                n += k
                if k != nobr(body(m)).count(my):
                    bad.append(f"B9 {name}:{i} «{key}» {k}x vs «{my}» {nobr(body(m)).count(my)}x")
    cnt["B9"] = n
    # C. reuse
    nc1 = sc1 = 0
    for name, (P, M) in PAIRS.items():
        for i, (p, m) in enumerate(zip(P, M), 1):
            s = nobr(body(p))
            for k, my in IND_FIN.items():
                if re.search(rf"(?<![\w]){k[:-1]}(?:ṃ|nti|ñca|ñceva|ā)(?![\w])", s, re.I):
                    nc1 += 1
                    if my in m:
                        sc1 += 1
                    else:
                        bad.append(f"C1 {name}:{i} «{k}» -> «{my}» missing")
    nc2 = sc2 = 0
    for name, (P, M) in PAIRS.items():
        for i, (p, m) in enumerate(zip(P, M), 1):
            k = F.LABEL_RE.sub("", re.sub(r"^#+ ", "", body(p)))
            if k in FIN_LINE:
                nc2 += 1
                if re.sub(r"^\([က-အ]\) ", "", re.sub(r"^#+ ", "", body(m))) in FIN_LINE[k]:
                    sc2 += 1
                else:
                    bad.append(f"C2 {name}:{i} «{k[:50]}»: «{body(m)[:50]}» vs final {sorted(FIN_LINE[k])[:2]}")
            c = len(re.findall("[Āā]mantā", nobr(body(p))))
            if c:
                nc2 += c
                got = min(c, body(m).count(F.YES[:-1]))
                sc2 += got
                if got < c:
                    bad.append(f"C2 {name}:{i} Āmantā")
    nc3 = sc3 = 0
    for rx, my, bk, bid, wit in REUSE:
        pl, ml = FIN[bk][bid]
        if wit.lower() not in " ".join(pl).lower() or my not in " ".join(ml) + " " + MS.IND_H + " " + F.H.get(
                "Indriyayamakaṃ", ""):
            bad.append(f"C3 witness pi-{bk} {bid}: «{wit}» / «{my}»")
            continue
        for name, (P, M) in PAIRS.items():
            for i, (p, m) in enumerate(zip(P, M), 1):
                # the suddhadhammavāra questions «(Ka) kusalā dhammā?» have two terms (kusalā / dhammā), not the subject
                sp = " ".join(x for x in F.SPLIT.split(nobr(body(p))) if not MS.DH_SUDDHA.match(F.LABEL_RE.sub("", x)))
                if re.search(rx, sp):
                    nc3 += 1
                    if my in m:
                        sc3 += 1
                    else:
                        bad.append(f"C3 {name}:{i} «{rx}» -> «{my}» missing")
    cnt["C"] = (sc1, nc1, sc2, nc2, sc3, nc3)
    return bad, cnt


def pairs(names):
    return {n: (nonempty(MS.PALI / n), nonempty(MS.OUT / n)) for n in names}


def report(bad, cnt):
    nv, nb, na = cnt["B3"]
    sc1, nc1, sc2, nc2, sc3, nc3 = cnt["C"]
    print(f"A. rebuild: {len(NAMES)} / {len(NAMES)} files regenerated identical" if not any(
        b.startswith("A ") for b in bad) else "A. rebuild: FAILED")
    print(f"B1 structure: {cnt['B1']} lines")
    print(f"B2 polarity: {cnt['B2']} negations, each one Burmese negative")
    print(f"B3 verbs: {nv} uppajj / nirujjh verbs (root, tense, polarity, double negative, plural «ကြ») and {nb} "
          f"bhāveti / pajahati in order; {na} answers")
    print(f"B4 pairs: {cnt['B4']} labelled lines in order, every «vā pana» = «{F.VA_PANA}»")
    print(f"B5 numbers: digits per line equal; {cnt['B5']} number words")
    print(f"B6 recurring sentences: {cnt['B6'][0]} distinct Pāli sentences of this group, each with one Burmese "
          f"rendering; {cnt['B6'][1]} of them shared with the finished pi-6 chapters and identical there")
    print(f"B7 table values: {cnt['B7']} headings / colophons / table lines")
    print(f"B8 quotes: {cnt['B8']} lines with quotes, nested right")
    print(f"B9 women / men / indriya attributes: {cnt['B9']} occurrences, each with its Burmese")
    tot_s, tot_n = sc1 + sc2 + sc3, nc1 + nc2 + nc3
    print(f"C. reuse test: {tot_s} / {tot_n} identical (C1 the 22 faculty names {sc1}/{nc1}, C2 whole lines and "
          f"answers {sc2}/{nc2}, C3 {len(REUSE)} reused terms {sc3}/{nc3} line occurrences)")
    n_ex = sum(1 for rx, _, _ in EXCEPT for P, M in PAIRS.values() for p in P if re.search(rx, nobr(body(p))))
    print(f"   documented exceptions / notes: {len(EXCEPT)} terms on {n_ex} lines")
    for rx, fin, ours in EXCEPT:
        print(f"   - {rx}: final {fin}; here {ours}")
    for name in NAMES:
        b1, c1 = check({name: PAIRS[name]}, rebuild=False)
        s = c1["C"]
        print(f"   {name}: {len([x for x in b1])} mismatches, reuse {s[0] + s[2] + s[4]} / {s[1] + s[3] + s[5]}")


MUTANTS = [   # (name, from, to) applied once to the first line that has «from»
    ("dropped «မ»", "မဖြစ်ပေါ်", "ဖြစ်ပေါ်"),
    ("dropped «ခဲ့»", "ဖြစ်ပေါ်ခဲ့", "ဖြစ်ပေါ်"),
    ("dropped «ကြ»", "ဖြစ်ပေါ်ကြသည်", "ဖြစ်ပေါ်သည်"),
    ("tāsaṃ «ထိုမိန်းမတို့» -> «ထိုသူတို့»", "ထိုမိန်းမတို့အား", "ထိုသူတို့အား"),
    ("changed faculty name", "နား၏ စွမ်းရည်", "နှာခေါင်း၏ စွမ်းရည်"),
    ("dropped «တစ်ဖန်»", "တစ်ဖန် ", ""),
    ("«ဟုတ်ပါသည်» -> «မဟုတ်ပါ»", "ဟုတ်ပါသည်။", "မဟုတ်ပါ။"),
    ("future -> present", "ဖြစ်ပေါ်ကြလိမ့်မည်", "ဖြစ်ပေါ်ကြသည်"),
    ("dropped «ကား မဟုတ်»", "သည်ကား မဟုတ်", "သည်"),
    ("changed attribute", "မရှိဘဲ", "ရှိလျက်"),
]


def mutate(PAIRS):
    ok = 0
    for label, a, b in MUTANTS:
        done = False
        for name, (P, M) in PAIRS.items():
            for i, m in enumerate(M):
                if a in m and not done:
                    M2 = list(M)
                    M2[i] = m.replace(a, b, 1)
                    bad, _ = check({name: (P, M2)}, rebuild=False)
                    print(f"   mutation {label}: {'caught' if bad else 'NOT CAUGHT'} ({name}:{i + 1})")
                    ok += bool(bad)
                    done = True
            if done:
                break
        if not done:
            print(f"   mutation {label}: no line to mutate")
    print(f"mutation test: {ok} / {len(MUTANTS)} caught")


if __name__ == "__main__":
    PAIRS = pairs(NAMES)
    bad, cnt = check(PAIRS)
    report(bad, cnt)
    if "--mutate" in sys.argv:
        mutate(PAIRS)
    print(f"\nmismatches: {len(bad)}")
    import collections
    print("   by test:", dict(collections.Counter(b.split()[0] for b in bad)))
    for b in bad[:60]:
        print("  ", b)
    sys.exit(1 if bad else 0)
