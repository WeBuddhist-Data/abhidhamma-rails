"""Check the Burmese zero-shot of pi-6 ch. 3 (3-01 … 3-06 Āyatanayamaka) line by line (adapted from check_sample.py).

usage: python3 -I -X utf8 check_ch3.py [--mutate]
  A. rebuild: make_ch3.py regenerates the six files byte for byte (nothing written here);
  B. per line: B1 structure (equal non-empty lines, dashes, ellipses, «[», item numbers, labels, block IDs, heading
     levels, no «?» «।» «:-», final «။», NFC, no U+1050-U+109F, no double blank line); B2 POLARITY: every Pāli negation
     (na, no, nuppajj-, nāyatana = na āyatana, Natthi, and the privative a-X-ka of acakkhuka / asotaka / aghānaka /
     arūpaka / acittaka) is one Burmese negative (မဟုတ် / မရှိ / မ + verb, «ပိုင်းခြား မသိ», «မရရှိ»), fixed terms
     masked (arūpa place, abyākata, ahetuka) and the editorial notes masked (they are table values, B7); B3 VERBS:
     the sequence of uppajj- / nirujjh- and of parijān- verbs of each line, with tense, polarity and the «no ca … na V»
     double negative, equals the Burmese sequence; Āmantā = «ဟုတ်ပါသည်။», Natthi = «မရှိပါ။», No = «မဟုတ်ပါ»;
     B4 (Ka) / (Kha) labels in order per file, every «vā pana» = «တစ်ဖန်»; B5 digits per line equal (=93 included)
     and number words (dvādasa, pañca-, catu-, dve, tividha, tīsu); B6 every recurring Pāli sentence (labels off,
     «-ti?» = «?», notes off) has one and the same Burmese at every occurrence; B7 table values: headings, colophons,
     notes and the twelve-base list come out as their table value;
  C. reuse test against the FINAL pi-1 … pi-5 rails texts, read here independently of my6_formulas:
     C1 the twelve āyatana names (pi-2 ^2-154) and the bare words; C2 whole lines / headings / Āmantā that also occur
     in pi-1 … pi-5; C3 every reused term of REUSE (witness segment, then every line whose Pāli has it). Documented
     exceptions (EXCEPT, the sample's departures) are listed apart, not counted.
--mutate: applies single mutations to the generated Burmese in memory and shows that each is caught.
Prints the mismatches (0 expected) and the counts; exit 1 on any mismatch.
"""
import pathlib
import re
import sys
import unicodedata

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import make_ch3 as MC  # noqa: E402
F = MC.F
ROOT = HERE.parents[3]
NAMES = MC.NAMES_OUT
HEAD = re.compile(r"^#+ ")


def nonempty(p):
    return [l for l in p.read_text(encoding="utf-8-sig").splitlines() if l.strip()]


def body(l):
    return F.strip_id(l).strip()


def nobr(s):
    return re.sub(r" ?\[[^\]]*\]", "", s)


NOTE_K = sorted(MC.NOTES, key=len, reverse=True)


def p_clean(p):
    """Pāli body: slips applied, notes and variant brackets out."""
    s = MC.unslip(body(p))
    for k in NOTE_K:
        s = s.replace(k, " ")
    return nobr(s)


def m_clean(m):
    s = body(m)
    for k in NOTE_K:
        s = s.replace(MC.NOTES[k], " ")
    return nobr(s)


# ===================================================================================== the FINAL index (independent)
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

_p, _m = (nobr(body(FIN["2"]["^2-154"][j][0])).split(" – ")[1].rstrip(".။") for j in (0, 1))
AYN = dict(zip([x.strip() for x in _p.split(",")], [x.strip() for x in _m.split("၊")]))

# C1: āyatana names (stem regex -> Burmese) and bare words
C1 = [(rf"\b{k[:-1]}", v) for k, v in AYN.items()]
BARE_RX = [(r"(?<![\w])cakkhu(?:ṃ|ñca|ū|ti)?(?![\w])", "cakkhāyatanaṃ"),
           (r"(?<![\w])sot(?:aṃ|añca|añceva|anti)(?![\w])", "sotāyatanaṃ"),
           (r"(?<![\w])ghān(?:aṃ|anti)(?![\w])", "ghānāyatanaṃ"), (r"(?<![\w])jivh(?:ā|aṃ|āti)(?![\w])", "jivhāyatanaṃ"),
           (r"(?<![\w])kāy(?:o|aṃ|añca|oti)(?![\w])", "kāyāyatanaṃ"),
           (r"(?<![\w])sadd(?:o|aṃ|oti)(?![\w])", "saddāyatanaṃ"),
           (r"(?<![\w])gandh(?:o|aṃ|añca|oti)(?![\w])", "gandhāyatanaṃ"),
           (r"(?<![\w])ras(?:o|aṃ|añca|oti)(?![\w])", "rasāyatanaṃ"),
           (r"(?<![\w])phoṭṭhabb(?:o|aṃ|oti)(?![\w])", "phoṭṭhabbāyatanaṃ"),
           (r"(?<![\w])man(?:o|aṃ|añca|oti)(?![\w])", "manāyatanaṃ"),
           (r"(?<![\w])dhamm(?:o|aṃ|añca|oti)(?![\w])", "dhammāyatanaṃ")]
C1 += [(rx, AYN[k].replace(" အာရုံခံ နယ်ပယ်", "")) for rx, k in BARE_RX]
C1 += [(r"(?<![\w])rūpa(?:ṃ|nti|ñca|ñceva)(?![\w])",
        re.search(r"ရုပ်(?=၊ ခံစားမှု)", " ".join(FIN["1"]["^1-1044"][1]))[0])]

REUSE = [   # (regex on the Pāli line, Burmese, book, block id, Pāli witness in that rails segment)
    (r"(?<![\w])n?uppajj", "ဖြစ်ပေါ်", "2", "^2-203", "uppajjamānā uppajjati"),
    (r"nirujjh", "ချုပ်ငြိမ်း", "2", "^2-204", "nirujjhamānā nirujjhati"),
    (r"upapajj", "ပြန်လည် ဖြစ်ပေါ်", "2", "^2-1024", "kattha upapajjanti"),
    (r"\bcavant", "စုတေ", "2", "^2-1029", "cavanti āyusaṅkhayā"),
    (r"parinibb", "ပရိနိဗ္ဗာန် ပြု", "4", "^4-M-7", "parinibbāyī"),
    (r"pañcavokār", "အစုအဝေး ငါးပါး ရှိသော ဘဝ", "2", "^2-234", "pañcavokārabhavo"),
    (r"catuvokār", "အစုအဝေး လေးပါး ရှိသော ဘဝ", "2", "^2-234", "catuvokārabhavo"),
    (r"asaññasatt", "အသညသတ်", "2", "^2-18-4-3-0", "Asaññasattā"),
    (r"\barūp(?:aṃ|e|ā|ānaṃ)\b", "ရုပ်မရှိသော ဘုံ", "2", "^2-234", "arūpabhavo"),
    (r"kāmāvacar", "ကာမဘုံ", "1", "^1-M2-93", "kāmāvacarā"),
    (r"(?<![\w])rūpāvacar", "သိမ်မွေ့သော ရုပ်ဘုံ", "1", "^1-M2-94", "rūpāvacarā"),
    (r"arūpāvacar", "ရုပ်မရှိသော ဘုံ", "1", "^1-M2-95", "arūpāvacarā"),
    (r"\bavases", "ကြွင်းကျန်သော", "2", "^2-796", "avasesā paññā"),
    (r"ṭhapetvā", "ချန်ထား၍", "2", "^2-796", "ṭhapetvā"),
    (r"\byassa\b", "အကြင်သူအား", "2", "^2-199", "Idha yassa te honti"),
    (r"okās", "နေရာ", "4", "^4-M-11", "okās"),
    (r"\batīt", "အတိတ်", "1", "^1-M1-18", "atītā dhammā"),
    (r"\banāgat", "အနာဂတ်", "1", "^1-M1-18", "anāgatā dhammā"),
    (r"paccuppann", "ပစ္စုပ္ပန်", "1", "^1-M1-18", "paccuppannā dhammā"),
    (r"\buddes", "အကျဉ်း ဖော်ပြချက်", "3", "^3-1-0", "Uddeso"),
    (r"niddes", "အကျယ် ဖော်ပြချက်", "1", "^1-2-3-1-0", "Ekakaniddeso"),
    (r"paṇṇatti", "သတ်မှတ်ချက်", "1", "^1-M2-108", "paññatti"),
    (r"puggal", "ပုဂ္ဂိုလ်", "1", "^1-1050", "puggal"),
    (r"suddhā(?!vās)", "ရိုးရိုး", "5", "^5-1-1-0", "Suddh"),
    (r"uppāda", "ဖြစ်ပေါ်ခြင်း", "1", "^1-1-0", "Cittuppādakaṇḍaṃ"),
    (r"nirodha", "ချုပ်ငြိမ်းခြင်း", "1", "^1-1063", "nirodh"),
    (r"vāro\b|vāra(?!ṃ)", "ဖော်ပြချက်", "2", "^2-15-1-2-0", "Saccavāro"),
    (r"niṭṭhit", "” ပြီးဆုံးပြီ။", "2", "^2-153", "Khandhavibhaṅgo niṭṭhito"),
    (r"(?<![\w])āyatan|nāyatan|(?<![\w])Āyatan", "အာရုံခံ နယ်ပယ်", "1", "^1-M2-122", "āyatan"),
    (r"(?<![\w])[Dd]vādas", "ဆယ့်နှစ်ပါး", "2", "^2-154", "Dvādasāyatanāni"),
    (r"cittak", "စိတ်", "1", "^1-6", "cittaṃ"),
    (r"parijān", "ပိုင်းခြား", "5", "^5-390", "parijānāti"),
    (r"pariññ", "ပိုင်းခြား သိ", "2", "^2-1029", "pariññāya"),
    (r"(?<![\w])[Aa]rah(?:ā|ant)", "ရဟန္တာ", "4", "^4-M-7", "Arahā"),
    (r"puthujjan", "ပုထုဇဉ်", "1", "^1-1007", "puthujjan"),
    (r"magg", "မဂ်", "1", "^1-M1-16", "magg"),
    (r"paṭilabh", "ရရှိ", "2", "^2-768", "paṭilabh"),
    (r"(?<![\w])agga", "အမြတ်ဆုံး", "2", "^2-1029", "agga"),
    (r"samaṅg", "ပြည့်စုံ", "2", "^2-809", "samaṅgī"),
    (r"Dibbacakkhu", "နတ်မျက်စိ", "5", "^5-11-7-1-0", "Dibbacakkhu"),
    (r"paññācakkhu", "ပညာမျက်စိ", "5", "^5-374", "paññācakkhu"),
    (r"Dibbasot", "နတ်နား", "5", "^5-11-8-1-0", "Dibbasot"),
    (r"taṇhā", "တပ်မက်မှု", "1", "^1-1065", "taṇhā"),
    (r"Sīla", "သီလ", "1", "^1-M2-135", "sīla"),
    (r"samādhi", "သမာဓိ", "1", "^1-1", "samādhi"),
    (r"paññāgandh", "ပညာ", "2", "^2-796", "paññā"),
    (r"vimutti", "လွတ်မြောက်မှု", "1", "^1-M2-141", "vimutti"),
    (r"(?<![\w])[Aa]ttharas", "အနက်", "2", "^2-718", "atthapaṭisambhid"),
    (r"pucchā", "အမေး", "5", "^5-1", "pucchā"),
    (r"vitthār", "အကျယ် ချဲ့", "5", "^5-839", "vitthāretabb"),
    (r"vibha", "ခွဲခြား", "2", "^2-33", "vibhaj"),
]
EXCEPT = [   # the sample's documented departures that occur in ch. 3 (notes-sample.md), not counted as identical
    (r"anuloma|paccanīka", "pi-5 «အစဉ်အတိုင်း» / «ပြောင်းပြန်» (debate order)", "«အဟုတ်ပြ ပုံစံ» / «အငြင်းပြ ပုံစံ» "
     "(sample, coordinator 2026-11-22)"),
    (r"\bcavant", "pi-2 termbase cavati «သေသည်»", "pi-5 termbase and pi-2 ^2-1029 «စုတေ» (sample)"),
    (r"\bNatthi\.", "pi-3 ^3-410 Natthi «မရှိ။»", "«မရှိပါ။» (answer register; coordinator 2026-11-22)"),
]

# ===================================================================================== the checks
MASK = [F.ABY, F.AHETUKA, F.PLACES["arūpa"], MC.SOTA_PUN]    # SOTA_PUN: «… သို့မဟုတ် …» (or) is no negation
# documented line exceptions: (file, line) -> reason (not counted as a mismatch, listed in the output)
LINE_EXCEPT = {("3-06-ayatanayamaka.md", 189, "B2"): "«no ca tesaṃ tattha…pe…»: the negated verb is cut by the «…»; the Burmese «သို့သော် ထိုသူတို့အား ထိုနေရာ၌…» has no verb to negate"}
PRIV = re.compile(r"(?<![\w])a(?:cakkhuk|sotak|ghānak|rūpak|cittak)ānaṃ", re.I)
P_VERB = re.compile(r"(?P<noca>no ca (?:tesaṃ tattha|tesaṃ|tattha) \S+ )?(?P<na>na )?(?P<n>n)?(?P<r>uppajj|nirujjh)"
                    r"(?P<e>issanti|issati|issatīti|ittha|itthāti|attha|anti|ati|atīti)\b", re.I)
P_END = {"issanti": "fut", "issati": "fut", "issatīti": "fut", "ittha": "past", "itthāti": "past", "attha": "past",
         "anti": "pres", "ati": "pres", "atīti": "pres"}
M_VERB = re.compile(r"(?<!ပြန်လည် )(?P<neg>မ)?(?P<r>ဖြစ်ပေါ်|ချုပ်ငြိမ်း)(?!လာ|ခြင်း|ပြီး)(?:ကြ)?(?P<t>ခဲ့|လိမ့်မည်|မည့်)?"
                    r"(?P<ns>(?:သည်)?ကား မဟုတ်)?")
M_ROOT = {"ဖြစ်ပေါ်": "uppajj", "ချုပ်ငြိမ်း": "nirujjh"}
M_T = {None: "pres", "ခဲ့": "past", "လိမ့်မည်": "fut", "မည့်": "fut"}
P_PJ = re.compile(r"(?P<noca>no ca \S+ )?(?P<na>na )?parijān(?P<e>issanti|issati|issatīti|ittha|itthāti|anti|āti|ātīti)\b")
PJ_END = {"issanti": "fut", "issati": "fut", "issatīti": "fut", "ittha": "past", "itthāti": "past", "anti": "pres",
          "āti": "pres", "ātīti": "pres"}
M_PJ = re.compile(r"ပိုင်းခြား (?P<neg>မ)?သိ(?!ခြင်း)(?:ကြ)?(?P<t>ခဲ့|လိမ့်မည်)?(?:ကြ)?(?P<ns>(?:သည်)?ကား မဟုတ်)?")
NUMW = [(r"(?<![\w])[Dd]vādas", "ဆယ့်နှစ်ပါး"), (r"[Pp]añca(?=vokār)", "ငါးပါး"), (r"[Cc]atu(?=vokār)", "လေးပါး"),
        (r"(?<![\w])dve(?![\w])", "နှစ်ပါး"), (r"tividh", "သုံးမျိုး"), (r"tīsu", "သုံးပါး")]


def p_neg(s):
    s = re.sub(r"(?<![\w])([Nn])āyatan", r"\1a āyatan", s)
    return (len(re.findall(r"(?<![\w])(?:na|no|No|Na)(?![\w])", s)) + len(re.findall(r"nuppajj", s))
            + len(re.findall(r"\bNatthi\b", s)) + len(PRIV.findall(s)))


def m_neg(s):
    for t in MASK:
        s = s.replace(t, "")
    return (s.count("မဟုတ်") + s.count("မရှိ") + s.count("မအခြေခံ") + s.count("မဖြစ်ပေါ်") + s.count("မချုပ်ငြိမ်း")
            + s.count("ပိုင်းခြား မသိ") + s.count("မရရှိ"))


def canon(s):
    s = F.LABEL_RE.sub("", s.strip())
    s = re.sub(r"nti\?$", "ṃ?", s)
    s = re.sub(r"(?<=[āaoeū])ti\?$", "?", s)
    s = re.sub(r"īti\?$", "i?", s)
    s = re.sub(r"āti\?$", "a?", s)
    return s


def run_checks(PAIRS, rebuild=True, quiet=False):
    bad = []
    say = (lambda *a: None) if quiet else print
    # A
    if rebuild:
        for name in NAMES:
            text, nbad = MC.run(name)
            if nbad or text != (MC.OUT / name).read_text(encoding="utf-8"):
                bad.append(f"A {name}: regenerated text differs")
        say(f"A. rebuild: {len(NAMES)} / {len(NAMES)} files regenerated identical" if not bad else "A. rebuild: FAILED")
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
            e = MC.line_check(p, m)
            if e:
                bad.append(f"B1 {name}:{i} {e}")
    say(f"B1 structure: {n_lines} lines")
    # B2
    n_pol = 0
    for name, (P, M, _) in PAIRS.items():
        for i, (p, m) in enumerate(zip(P, M), 1):
            if HEAD.match(p):
                continue
            a, b = p_neg(p_clean(p)), m_neg(m_clean(m))
            n_pol += a
            if a != b and (name, i, "B2") not in LINE_EXCEPT:
                bad.append(f"B2 {name}:{i} negations Pāli {a} vs Burmese {b}")
    say(f"B2 polarity: {n_pol} negations (incl. privative a-X-ka), each one Burmese negative")
    # B3
    n_verb = n_pj = n_ans = 0
    for name, (P, M, _) in PAIRS.items():
        for i, (p, m) in enumerate(zip(P, M), 1):
            if HEAD.match(p):
                continue
            s, ms = p_clean(p), m_clean(m)
            exp = []
            for x in P_VERB.finditer(s):
                neg = bool(x["na"] or x["n"])
                exp.append((x["r"].lower(), P_END[x["e"]], neg or bool(x["noca"]), neg and bool(x["noca"])))
            got = [(M_ROOT[y["r"]], M_T[y["t"]], bool(y["neg"]), bool(y["ns"])) for y in M_VERB.finditer(ms)]
            n_verb += len(exp)
            if exp != got:
                bad.append(f"B3 {name}:{i} verbs Pāli {exp} vs Burmese {got}")
            exp = [(PJ_END[x["e"]], bool(x["na"]) or bool(x["noca"]), bool(x["na"]) and bool(x["noca"]))
                   for x in P_PJ.finditer(s)]
            got = [(M_T[y["t"]], bool(y["neg"]), bool(y["ns"])) for y in M_PJ.finditer(ms)]
            n_pj += len(exp)
            if exp != got:
                bad.append(f"B3 {name}:{i} parijān- Pāli {exp} vs Burmese {got}")
            for pa, my, rx in (("Āmantā", F.YES[:-1], r"\bĀmantā\b"), ("Natthi", F.NATTHI[:-1], r"\bNatthi\b"),
                               ("No", F.NO[:-1], r"(?<![\w])No(?![\w])")):
                k = len(re.findall(rx, s))
                n_ans += k
                if k != ms.count(my):
                    bad.append(f"B3 {name}:{i} «{pa}» {k}x vs «{my}» {ms.count(my)}x")
    say(f"B3 verbs: {n_verb} uppajj- / nirujjh- and {n_pj} parijān- verbs (root, tense, polarity, double negative) "
        f"in order; {n_ans} answers")
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
    n_num = 0
    for name, (P, M, _) in PAIRS.items():
        for i, (p, m) in enumerate(zip(P, M), 1):
            if re.findall(r"\d", re.sub(r"\^\S+", "", p)) != re.findall(r"\d", re.sub(r"\^\S+", "", m)):
                bad.append(f"B5 {name}:{i} digits")
            s = nobr(body(p))
            for rx, my in NUMW:
                k = len(re.findall(rx, s))
                n_num += k
                if k != nobr(m).count(my) - (nobr(m).count("ဆယ့်နှစ်ပါး") if my == "နှစ်ပါး" else 0):
                    bad.append(f"B5 {name}:{i} «{rx}» {k}x vs «{my}»")
    say(f"B5 numbers: digits per line equal; {n_num} number words")
    # B6
    occ = {}
    for name, (P, M, _) in PAIRS.items():
        for i, (p, m) in enumerate(zip(P, M), 1):
            b = body(p)
            if HEAD.match(b) or "…" in b or b in MC.COLO or b.startswith("Dvādas") or any(k in b for k in MC.SLIP_POST):
                continue
            b, mb = p_clean(p), m_clean(m)
            lab = F.LABEL_RE.match(b)
            b = F.LABEL_RE.sub("", b).strip()
            mb = re.sub(r"^\([က-အ]\) ", "", mb).strip()
            if not b:
                continue
            ps = [x for x in F.SPLIT.split(b) if x.strip() not in ("", ".")]
            ms = [x.strip() for x in re.split(r"(?<=။) ", mb) if x.strip() not in ("", "။")]
            if len(ps) != len(ms):
                bad.append(f"B6 {name}:{i} {len(ps)} Pāli vs {len(ms)} Burmese sentences")
                continue
            for j, (x, y) in enumerate(zip(ps, ms)):
                k = canon(x)
                if j == 0 and lab and "vā pana" in x:
                    y = y.replace(F.VA_PANA + " ", "", 1)
                occ.setdefault(k, set()).add(y)
    # the same Pāli sentence in the approved sample (1-mulayamaka, 2-01-khandhayamaka): the same Burmese
    n_x = 0
    for name in ("1-mulayamaka.md", "2-01-khandhayamaka.md"):
        P, M = nonempty(MC.PALI / name), nonempty(MC.OUT / name)
        for p, m in zip(P, M):
            b = body(p)
            if HEAD.match(b) or "…" in b or b in F.COLO or "[" in b:
                continue
            ps = F.SPLIT.split(F.LABEL_RE.sub("", b).strip())
            ms = [x.strip() for x in re.split(r"(?<=။) ", re.sub(r"^\([က-အ]\) ", "", body(m)).strip())]
            if len(ps) != len(ms):
                continue
            for j, (x, y) in enumerate(zip(ps, ms)):
                k = canon(x)
                if k in occ:
                    if j == 0 and F.LABEL_RE.match(b) and "vā pana" in x:
                        y = y.replace(F.VA_PANA + " ", "", 1)
                    n_x += 1
                    occ[k].add(y)
    for k, v in occ.items():
        if len(v) > 1:
            bad.append(f"B6 «{k[:70]}» has {len(v)} Burmese renderings {sorted(v)[:2]}")
    say(f"B6 recurring sentences: {len(occ)} distinct Pāli sentences, each with one Burmese rendering "
        f"(also {n_x} occurrences in the approved sample files)")
    # B7
    n_tab = 0
    for name, (P, M, _) in PAIRS.items():
        for i, (p, m) in enumerate(zip(P, M), 1):
            b, mb = body(p), body(m)
            h = re.match(r"^(#+) (.*)$", b)
            if h:
                n_tab += 1
                if mb != f"{h[1]} {F.heading(h[2])}":
                    bad.append(f"B7 {name}:{i} heading")
                continue
            if b in MC.COLO:
                n_tab += 1
                if mb != MC.COLO[b]:
                    bad.append(f"B7 {name}:{i} colophon")
            if b.startswith("Dvādasāyatanāni – "):
                n_tab += 1
                if mb != f"{MC.AY_H} – " + "၊ ".join(AYN[k] for k in re.findall(r"\w+āyatanaṃ", b)) + "။":
                    bad.append(f"B7 {name}:{i} list")
            for k in NOTE_K:
                c = MC.unslip(b).count(k)
                if c:
                    n_tab += c
                    if mb.count(MC.NOTES[k]) < c:
                        bad.append(f"B7 {name}:{i} note «{k[:30]}»")
    say(f"B7 table values: {n_tab} headings / colophons / notes / list lines")
    # C
    n_c1 = s_c1 = 0
    for name, (P, M, _) in PAIRS.items():
        for i, (p, m) in enumerate(zip(P, M), 1):
            s = nobr(MC.unslip(body(p)))
            for rx, my in C1:
                if re.search(rx, s, re.I):
                    n_c1 += 1
                    if my in m:
                        s_c1 += 1
                    else:
                        bad.append(f"C1 {name}:{i} «{rx}» -> «{my}» missing")
    n_c2 = s_c2 = 0
    for name, (P, M, _) in PAIRS.items():
        for i, (p, m) in enumerate(zip(P, M), 1):
            k = F.LABEL_RE.sub("", re.sub(r"^#+ ", "", body(p)))
            if k in FIN_LINE:
                n_c2 += 1
                if re.sub(r"^\([က-အ]\) ", "", re.sub(r"^#+ ", "", body(m))) in FIN_LINE[k]:
                    s_c2 += 1
                else:
                    bad.append(f"C2 {name}:{i} «{k[:50]}»: «{body(m)[:50]}» vs final {sorted(FIN_LINE[k])[:2]}")
    if "Āmantā" not in " ".join(FIN["5"]["^5-1"][0]) or "ဟုတ်ပါသည်။" not in " ".join(FIN["5"]["^5-1"][1]):
        bad.append("C2 witness Āmantā")
    for name, (P, M, _) in PAIRS.items():
        for i, (p, m) in enumerate(zip(P, M), 1):
            k = len(re.findall(r"\bĀmantā\b", p_clean(p)))
            if k:
                n_c2 += k
                got = min(k, body(m).count(F.YES[:-1]))
                s_c2 += got
                if got < k:
                    bad.append(f"C2 {name}:{i} «Āmantā»")
    n_c3 = s_c3 = 0
    for rx, my, bk, bid, wit in REUSE:
        pl, ml = FIN[bk][bid]
        if wit.lower() not in " ".join(pl).lower() or my not in " ".join(ml):
            bad.append(f"C3 witness pi-{bk} {bid}: «{wit}» / «{my}»")
            continue
        for name, (P, M, _) in PAIRS.items():
            for i, (p, m) in enumerate(zip(P, M), 1):
                if re.search(rx, nobr(MC.unslip(body(p))), re.I):
                    n_c3 += 1
                    if my in m:
                        s_c3 += 1
                    else:
                        bad.append(f"C3 {name}:{i} «{rx}» -> «{my}» missing")
    n_ex = sum(1 for rx, _, _ in EXCEPT for P, M, _ in PAIRS.values() for p in P if re.search(rx, nobr(body(p)), re.I))
    tn, ts = n_c1 + n_c2 + n_c3, s_c1 + s_c2 + s_c3
    say(f"C. reuse test: {ts} / {tn} identical (C1 āyatana names and bare words {s_c1}/{n_c1}, C2 whole lines and "
        f"answers {s_c2}/{n_c2}, C3 {len(REUSE)} reused terms {s_c3}/{n_c3} line occurrences)")
    say(f"   documented exceptions (not counted): {len(EXCEPT)} terms on {n_ex} lines")
    for rx, fin, ours in EXCEPT:
        say(f"   - {rx}: final {fin}; here {ours}")
    return bad, (ts, tn)


def load():
    return {n: (nonempty(MC.PALI / n), nonempty(MC.OUT / n), (MC.OUT / n).read_text(encoding="utf-8")) for n in NAMES}


if __name__ == "__main__":
    PAIRS = load()
    if "--mutate" in sys.argv:
        name = NAMES[0]
        P, M, raw = PAIRS[name]
        muts = [("dropped «မ»", "မဖြစ်ပေါ်", "ဖြစ်ပေါ်"), ("dropped «ခဲ့»", "ဖြစ်ပေါ်ခဲ့", "ဖြစ်ပေါ်"),
                ("«ဟုတ်ပါသည်» changed", "ဟုတ်ပါသည်။", "မဟုတ်ပါ။"), ("base name changed", "နား အာရုံခံ", "နှာခေါင်း အာရုံခံ"),
                ("attribute polarity", "မျက်စိ မရှိဘဲ", "မျက်စိ ရှိလျက်"), ("tense swap", "ဖြစ်ပေါ်လိမ့်မည်", "ဖြစ်ပေါ်ခဲ့"),
                ("double negative dropped", "မဖြစ်ပေါ်သည်ကား မဟုတ်", "မဖြစ်ပေါ်"), ("label", "(ခ) ", "(က) ")]
        for desc, a, b in muts:
            for nm in NAMES:
                Pn, Mn, rawn = PAIRS[nm]
                idx = next((i for i, l in enumerate(Mn) if a in l), None)
                if idx is not None:
                    M2 = list(Mn)
                    M2[idx] = M2[idx].replace(a, b, 1)
                    bad, _ = run_checks({nm: (Pn, M2, rawn)}, rebuild=False, quiet=True)
                    print(f"mutation {desc} ({nm}:{idx + 1}): {'CAUGHT' if bad else 'MISSED'} ({len(bad)}: "
                          f"{(bad or [''])[0][:70]})")
                    break
        sys.exit(0)
    bad, (ts, tn) = run_checks(PAIRS)
    for (nm, ln, ck), why in LINE_EXCEPT.items():
        print(f"   line exception {ck} {nm}:{ln}: {why}")
    print(f"\nmismatches: {len(bad)}")
    for b in bad[:60]:
        print("  ", b)
    sys.exit(1 if bad else 0)
