"""Check the Burmese zero-shot of pi-6 ch. 7 group a (7-01 … 7-05 Anusayayamaka) line by line (adapted from
check_ch3.py / check_sample.py).

usage: python3 -I -X utf8 check_ch7a.py [--mutate]
  A. rebuild: make_ch7a.py regenerates the five files byte for byte (nothing written here);
  B. per line: B1 structure (equal non-empty lines, dashes, ellipses, «[», item numbers, labels, block IDs, heading
     levels, no «?» «।» «:-», final «။», NFC, no U+1050-U+109F, no double blank line); B2 POLARITY: every Pāli negation
     (no, No., Natthi, nānuseti / nānusenti, nappajahati, nir- of niranusaya, the privative a- of apariyāpanna) is one
     Burmese negative (မဟုတ် / မရှိ / မကိန်းအောင်း / မပယ် / အကျုံးမဝင်), the place name «ရုပ်မရှိသော ဘုံ» masked;
     B3 VERBS: the sequence of anuset- / sānusaya-niranusaya / pajah- predicates of each line, with polarity, number
     and the «no ca …» negation (double negative included), equals the Burmese sequence; Āmantā = «ဟုတ်ပါသည်»,
     Natthi = «မရှိပါ», No = «မဟုတ်ပါ»; B4 (Ka) / (Kha) labels in order per file, every «vā pana» = «တစ်ဖန်»;
     B5 digits per line equal and number words (dvīsu, tīsu, satta, eka- … chakka-mūlaka, dvinnaṃ / dve, tiṇṇaṃ /
     tayo, catunnaṃ / cattāro, aṭṭhamaka); B6 every recurring Pāli sentence (labels off, «-ti?» = «?», notes off) has
     one and the same Burmese at every occurrence (also in the approved sample files and ch. 3); B7 table values:
     headings, colophons, notes and the seven-tendency list come out as their table value;
  C. reuse test against the FINAL pi-1 … pi-5 rails texts, read here independently of my6_formulas:
     C1 the seven anusaya names (pi-2 ^2-816); C2 whole lines / headings and Āmantā that also occur in pi-1 … pi-5;
     C3 every reused term of REUSE (witness segment, then every line whose Pāli has it). Documented exceptions
     (EXCEPT, the sample's departures) are listed apart, not counted.
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
import make_ch7a as MC  # noqa: E402
F = MC.F
ROOT = HERE.parents[3]
NAMES = MC.NAMES_OUT
HEAD = re.compile(r"^#+ ")


def nonempty(p):
    return [l for l in p.read_text(encoding="utf-8-sig").splitlines() if l.strip()]


def body(l):
    return F.strip_id(l).strip()


NOTE_K = sorted(MC.NOTES, key=len, reverse=True)


def p_clean(p):
    """Pāli body: slips applied, notes out, «…pe…» = «…»."""
    s = MC.unslip(body(p))
    for k in NOTE_K:
        s = s.replace(k, " ")
    return s.replace("…pe…", "…").replace("…Pe…", "…")


def m_clean(m):
    s = body(m)
    for k in NOTE_K:
        s = s.replace(MC.NOTES[k], " ")
    return s


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

# C1: the seven names, read from pi-2 ^2-816 here (not from make_ch7a)
_p = re.search(r"Sattānusayā – (.+?)\. ", FIN["2"]["^2-816"][0][0])[1].split(", ")
_m = re.search(r"ကိန်းအောင်းခြင်း ခုနစ်ပါး – (.+?)။", FIN["2"]["^2-816"][1][0])[1].split("၊ ")
SEVEN = dict(zip(_p, _m))
C1 = [(k[:-1], v) for k, v in SEVEN.items()]        # 'kāmarāgānusay' -> «ကာမရာဂ ကိန်းအောင်းခြင်း»

REUSE = [   # (regex on the Pāli line, Burmese, book, block id, Pāli witness in that rails segment)
    (r"(?<![\w])(?:a|nā)nuse(?:t|nt)", "ကိန်းအောင်း", "2", "^2-816", "anuseti"),
    (r"sānusay|niranusay", "ရှိသူ", "5", "^5-606", "sānusayo"),
    (r"pajah", "ပယ်", "5", "^5-390", "pajahati"),
    (r"(?<![\w])[Aa]nāgām", "အနာဂါမ်", "4", "^4-M-7", "Anāgāmī"),
    (r"(?<![\w])[Aa]rah(?:ā|ato)(?![\w])", "ရဟန္တာ", "4", "^4-M-7", "Arahā"),
    (r"[Pp]uthujjan", "ပုထုဇဉ်", "1", "^1-1007", "puthujjan"),
    (r"[Aa]ṭṭhamak", "အဋ္ဌမ ပုဂ္ဂိုလ်", "5", "^5-368", "Aṭṭhamakassa puggalassa"),
    (r"[Aa]ggamagg", "အမြတ်ဆုံး", "2", "^2-1029", "agga"),
    (r"samaṅg", "ပြည့်စုံ", "2", "^2-809", "samaṅgī"),
    (r"puggal", "ပုဂ္ဂိုလ်", "1", "^1-1050", "puggal"),
    (r"[Dd]vinnaṃ puggal|(?<![\w])[Dd]ve puggal", "ပုဂ္ဂိုလ် နှစ်ယောက်", "4", "^4-M-8", "Dve puggalā"),
    (r"[Tt]iṇṇaṃ puggal|(?<![\w])[Tt]ayo puggal", "ပုဂ္ဂိုလ် သုံးယောက်", "4", "^4-M-9", "Tayo puggalā"),
    (r"[Cc]atunnaṃ puggal|[Cc]attāro puggal", "ပုဂ္ဂိုလ် လေးယောက်", "4", "^4-M-10", "Cattāro puggalā"),
    (r"[Ss]veva|[Tt]eva puggal|[Tt]asseva|[Tt]esaññeva", "ပင်", "5", "^5-241", "arahattaṃyeva"),
    (r"[Kk]āmadhātu", "ကာမဘုံ", "2", "^2-991", "Kāmadhātuyā"),
    (r"(?<![\w])[Rr]ūpadhātu", "သိမ်မွေ့သော ရုပ်ဘုံ", "2", "^2-993", "Rūpadhātuyā"),
    (r"[Aa]rūpadhātu", "ရုပ်မရှိသော ဘုံ", "2", "^2-995", "Arūpadhātuyā"),
    (r"[Dd]ukkhāya vedanāya", "နာကျင်သော ခံစားမှု", "1", "^1-M1-2", "dukkhāya vedanāya"),
    (r"vedan", "ခံစားမှု", "1", "^1-1044", "vedanā"),
    (r"dvīsu", "နှစ်ပါး", "1", "^1-1441", "dvīsu"),
    (r"tīsu", "သုံးပါး", "1", "^1-1475", "tīsu bhūmīsu"),
    (r"(?<![\w])[Aa]pariyāpann", "ဘဝဘုံတို့၌ အကျုံးမဝင်သော", "1", "^1-M2-96", "apariyāpannā"),
    (r"sakkāyapariyāpann", "၌ အကျုံးဝင်သော", "1", "^1-283", "maggapariyāpannaṃ"),
    (r"sakkāya", "ကိုယ်", "1", "^1-1007", "sakkāyadiṭṭhi"),
    (r"[Ss]abbasakk", "အားလုံး", "5", "^5-334", "sabbe te"),
    (r"dhammesu", "သဘောတရား", "1", "^1-M1-1", "dhammā"),
    (r"[Tt]adekaṭṭh", "ထိုအရာနှင့် တစ်နေရာတည်း တည်ရှိ", "2", "^2-816", "Tadekaṭṭho"),
    (r"(?<![\w])[Kk]attha(?![\w])", "မည်သည့်နေရာ၌", "2", "^2-1024", "kattha upapajjanti"),
    (r"(?<![\w])[Yy]assa(?![\w])", "အကြင်သူအား", "2", "^2-199", "Idha yassa te honti"),
    (r"okās", "နေရာ", "4", "^4-M-11", "okās"),
    (r"vāro|vāra|vāre", "ဖော်ပြချက်", "2", "^2-15-1-2-0", "Saccavāro"),
    (r"[Aa]nusayayamak", "ကိန်းအောင်းခြင်း", "1", "^1-1065", "anusay"),
    (r"Sattānusayā", "ကိန်းအောင်းခြင်း ခုနစ်ပါး", "2", "^2-816", "Sattānusayā"),
]
EXCEPT = [   # the sample's documented departures that occur here (notes-sample.md), not counted as identical
    (r"anuloma", "pi-5 «အစဉ်အတိုင်း» (debate order)", "«အဟုတ်ပြ ပုံစံ» (sample, coordinator 2026-11-22); paṭiloma "
     "«အငြင်းပြ ပုံစံ» as paccanīka (no pi-1 … pi-5 occurrence)"),
    (r"\bNatthi\.", "pi-3 ^3-410 Natthi «မရှိ။»", "«မရှိပါ။» (answer register; coordinator 2026-11-22)"),
]

# ===================================================================================== the checks
MASK = [MC.ARUPA_B]                         # «ရုပ်မရှိသော ဘုံ» (the plane's name) is no negation
LINE_EXCEPT = {}
TOKW = re.compile(r"[^\s…,.?]+")


def p_neg(s):
    w = [x.lower() for x in TOKW.findall(s)]
    n = sum(1 for x in w if x == "no")                                   # no ca / No.
    n += sum(1 for x in w if x == "natthi")
    n += sum(1 for x in w if x.startswith(("nānuse", "nappajah", "niranusay", "apariyāpann")))
    return n


def m_neg(s):
    for t in MASK:
        s = s.replace(t, "")
    return (s.count("မဟုတ်") + s.count("မရှိ") + s.count("မကိန်းအောင်း") + s.count("မပယ်") + s.count("အကျုံးမဝင်"))


M_VERB = re.compile(r"(?P<an>(?P<an_n>မ)?ကိန်းအောင်း(?!ခြင်း)(?P<an_p>ကြ)?(?P<an_e>သည်|၏|သလော|သနည်း)?(?P<an_s>ကား မဟုတ်)?)"
                    r"|(?P<pa>(?P<pa_n>မ)?ပယ်(?!ခြင်း)(?P<pa_p>ကြ)?(?P<pa_e>သည်|၏|သလော)?(?P<pa_s>ကား မဟုတ်)?)"
                    r"|(?P<sa>(?P<sa_n>မ)?ရှိသူ(?P<sa_p>များ)? (?P<sa_c>ဖြစ်|မဟုတ်)(?:ကြ)?(?P<sa_e>သည်|၏|သလော)?)")
M_FORM = {"သလော": "q", "သနည်း": "wh", "၏": "cl", "သည်": "st", None: "st"}


def p_verbs(s):
    """[(family, negative word, plural, «no ca», form)] in order; form 'q' (question verb «-ti?»), 'cl' (the first
    verb of a question), 'wh' (kattha), 'st' (statement)."""
    out = []
    for sent in F.SPLIT.split(s):
        w = [x.lower() for x in TOKW.findall(sent)]
        question, wh = sent.rstrip().endswith("?"), bool(w) and w[0] == "kattha"
        noca = False
        for i, x in enumerate(w):
            if x == "no" and i + 1 < len(w) and w[i + 1] == "ca":
                noca = True
                continue
            v = MC.verb_parse(x)
            if v:
                fam, neg, pl, q = v
                form = "wh" if wh else ("q" if q else ("cl" if question else "st"))
                out.append((fam, neg, pl, noca, form))
                noca = False
    return out


def expect(v):
    fam, neg, pl, noca, form = v
    if form == "cl" and (neg and fam != "sa"):
        form = "st"                                   # a negative first clause is the bare «မV» (as a statement)
    if fam == "sa":
        return (fam, neg, pl, noca, "st" if noca else form)      # «(မ)ရှိသူ(များ) ဖြစ်… / မဟုတ်»
    return (fam, neg or noca, pl, neg and noca, form)            # «(မ)Vကြ … (သည်ကား မဟုတ်)»


def m_verbs(s):
    out = []
    for y in M_VERB.finditer(s):
        for fam in ("an", "pa", "sa"):
            if y[fam]:
                f2 = {"an": "anu", "pa": "pa", "sa": "sa"}[fam]
                last = bool(y[f"{fam}_s"]) if fam != "sa" else y["sa_c"] == "မဟုတ်"
                out.append((f2, bool(y[f"{fam}_n"]), bool(y[f"{fam}_p"]), last, M_FORM[y[f"{fam}_e"]]))
    return out


NUMW = [  # (Pāli regex, Burmese number word)
    (r"(?<![\w])dvīsu", "နှစ်ပါး"), (r"(?<![\w])tīsu", "သုံးပါး"), (r"Sattānusay", "ခုနစ်ပါး"),
    (r"\(Ekamūlak", "တစ်ပါး"), (r"\(Dukamūlak", "နှစ်ပါး"), (r"\(Tikamūlak", "သုံးပါး"), (r"\(Catukkamūlak", "လေးပါး"),
    (r"\(Pañcakamūlak", "ငါးပါး"), (r"\(Chakkamūlak", "ခြောက်ပါး"),
    (r"(?<![\w])(?:[Dd]vinnaṃ|[Dd]ve) puggal", "နှစ်ယောက်"), (r"(?<![\w])(?:[Tt]iṇṇaṃ|[Tt]ayo) puggal", "သုံးယောက်"),
    (r"(?<![\w])(?:[Cc]atunnaṃ|[Cc]attāro) puggal", "လေးယောက်"), (r"[Aa]ṭṭhamak", "အဋ္ဌမ"),
]


def canon(s):
    s = F.LABEL_RE.sub("", s.strip())
    s = re.sub(r"(?<=[āaoeū])ti\?$", "?", s)
    s = re.sub(r"īti\?$", "i?", s)
    return s


def split_m(mb):
    return [x.strip() for x in re.split(r"(?<=။) ", mb) if x.strip() not in ("", "။")]


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
    say(f"B2 polarity: {n_pol} negations (no, Natthi, nānuseti, nir-, apariyāpanna), each one Burmese negative")
    # B3
    n_verb = n_ans = 0
    for name, (P, M, _) in PAIRS.items():
        for i, (p, m) in enumerate(zip(P, M), 1):
            if HEAD.match(p):
                continue
            s, ms = p_clean(p), m_clean(m)
            exp = [expect(v) for v in p_verbs(s)]
            got = m_verbs(ms)
            n_verb += len(exp)
            if exp != got:
                bad.append(f"B3 {name}:{i} verbs Pāli {exp[:4]} vs Burmese {got[:4]}")
            for pa, my, rx in (("Āmantā", F.YES[:-1], r"\bĀmantā\b"), ("Natthi", F.NATTHI[:-1], r"\bNatthi\b"),
                               ("No", F.NO[:-1], r"(?<![\w])No(?![\w])")):
                k = len(re.findall(rx, s))
                n_ans += k
                if k != ms.count(my):
                    bad.append(f"B3 {name}:{i} «{pa}» {k}x vs «{my}» {ms.count(my)}x")
    say(f"B3 verbs: {n_verb} anuseti / sānusaya-niranusaya / pajahati predicates (family, polarity, number, «no ca», "
        f"double negative) in order; {n_ans} answers")
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
            s = MC.unslip(body(p))
            want = {}
            for rx, my in NUMW:
                k = len(re.findall(rx, s))
                n_num += k
                want[my] = want.get(my, 0) + k
            for my, k in want.items():
                if k != m.count(my):
                    bad.append(f"B5 {name}:{i} «{my}» Pāli {k}x vs Burmese {m.count(my)}x")
    say(f"B5 numbers: digits per line equal; {n_num} number words")
    # B6
    occ = {}
    for name, (P, M, _) in PAIRS.items():
        for i, (p, m) in enumerate(zip(P, M), 1):
            b = body(p)
            if HEAD.match(b) or b in MC.COLO or b in MC.LINES:
                continue
            b, mb = p_clean(p), m_clean(m)
            lab = F.LABEL_RE.match(b)
            b = F.LABEL_RE.sub("", b).strip()
            mb = re.sub(r"^\([က-အ]\) ", "", mb).strip()
            if not b:
                continue
            ps = [x for x in F.SPLIT.split(b) if x.strip() not in ("", ".")]
            ms = split_m(mb)
            if len(ps) != len(ms):
                bad.append(f"B6 {name}:{i} {len(ps)} Pāli vs {len(ms)} Burmese sentences")
                continue
            for j, (x, y) in enumerate(zip(ps, ms)):
                k = canon(x)
                if j == 0 and lab and "vā pana" in x:
                    y = y.replace(F.VA_PANA + " ", "", 1)
                occ.setdefault(k, set()).add(y)
    n_x = 0
    others = ["1-mulayamaka.md", "2-01-khandhayamaka.md"] + [f"3-0{i}-ayatanayamaka.md" for i in range(1, 7)]
    for name in others:
        if not (MC.OUT / name).exists():
            continue
        P, M = nonempty(MC.PALI / name), nonempty(MC.OUT / name)
        for p, m in zip(P, M):
            b = body(p)
            if HEAD.match(b) or "…" in b or b in F.COLO or "[" in b or "(" in b[4:]:
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
        f"(also {n_x} occurrences in the approved sample files and ch. 3)")
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
            if b.startswith("Sattānusayā – "):
                n_tab += 1
                if mb != "ကိန်းအောင်းခြင်း ခုနစ်ပါး – " + "၊ ".join(SEVEN[k] for k in re.findall(r"\w+ānusayo", b)) + "။":
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
            s = MC.unslip(body(p)).lower()
            for st, my in C1:
                k = s.count(st)
                if k:
                    n_c1 += k
                    got = min(k, m.count(my))
                    s_c1 += got
                    if got < k:
                        bad.append(f"C1 {name}:{i} «{st}» {k}x -> «{my}» {m.count(my)}x")
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
                if re.search(rx, MC.unslip(body(p))):
                    n_c3 += 1
                    if my in m:
                        s_c3 += 1
                    else:
                        bad.append(f"C3 {name}:{i} «{rx}» -> «{my}» missing")
    n_ex = sum(1 for rx, _, _ in EXCEPT for P, M, _ in PAIRS.values() for p in P if re.search(rx, body(p), re.I))
    tn, ts = n_c1 + n_c2 + n_c3, s_c1 + s_c2 + s_c3
    say(f"C. reuse test: {ts} / {tn} identical (C1 anusaya names {s_c1}/{n_c1}, C2 whole lines and answers "
        f"{s_c2}/{n_c2}, C3 {len(REUSE)} reused terms {s_c3}/{n_c3} line occurrences)")
    say(f"   documented exceptions (not counted): {len(EXCEPT)} terms on {n_ex} lines")
    for rx, fin, ours in EXCEPT:
        say(f"   - {rx}: final {fin}; here {ours}")
    return bad, (ts, tn)


def load():
    return {n: (nonempty(MC.PALI / n), nonempty(MC.OUT / n), (MC.OUT / n).read_text(encoding="utf-8")) for n in NAMES}


if __name__ == "__main__":
    PAIRS = load()
    if "--mutate" in sys.argv:
        muts = [("dropped «မ»", "မကိန်းအောင်း။", "ကိန်းအောင်း။"), ("nir- dropped", "မရှိသူ", "ရှိသူ"),
                ("«ဟုတ်ပါသည်» changed", "ဟုတ်ပါသည်။", "မဟုတ်ပါ။"),
                ("anusaya name changed", "မာန ကိန်းအောင်းခြင်း", "ဘဝရာဂ ကိန်းအောင်းခြင်း"),
                ("plural «ကြ» dropped", "ကိန်းအောင်းကြသည်", "ကိန်းအောင်းသည်"),
                ("double negative dropped", "မကိန်းအောင်းသည်ကား မဟုတ်", "မကိန်းအောင်း"),
                ("label", "(ခ) ", "(က) "), ("number", "သုံးယောက်", "လေးယောက်"),
                ("place", "သိမ်မွေ့သော ရုပ်ဘုံ", "ကာမဘုံ"), ("pajahati polarity", "ကို မပယ်", "ကို ပယ်"),
                ("question verb", "ကိန်းအောင်းသလော", "ကိန်းအောင်းသည်လော")]
        for desc, a, b in muts:
            for nm in NAMES:
                Pn, Mn, rawn = PAIRS[nm]
                idx = next((i for i, l in enumerate(Mn) if a in l), None)
                if idx is not None:
                    M2 = list(Mn)
                    M2[idx] = M2[idx].replace(a, b, 1)
                    bad, _ = run_checks({nm: (Pn, M2, rawn)}, rebuild=False, quiet=True)
                    print(f"mutation {desc} ({nm}:{idx + 1}): {'CAUGHT' if bad else 'MISSED'} ({len(bad)}: "
                          f"{(bad or [''])[0][:80]})")
                    break
        sys.exit(0)
    bad, (ts, tn) = run_checks(PAIRS)
    for (nm, ln, ck), why in LINE_EXCEPT.items():
        print(f"   line exception {ck} {nm}:{ln}: {why}")
    print(f"\nmismatches: {len(bad)}")
    for b in bad[:60]:
        print("  ", b)
    sys.exit(1 if bad else 0)
