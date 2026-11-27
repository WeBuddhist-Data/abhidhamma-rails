"""Check the Burmese zero-shot of pi-6 ch. 7 group b (7-06 … 7-11 Anusayayamaka) line by line (adapted from
check_ch7a.py / check_sample.py).

usage: python3 -I -X utf8 check_ch7b.py [--mutate]
  A. rebuild: make_ch7b.py regenerates the six files byte for byte (nothing written here);
  B. per line: B1 structure (equal non-empty lines, dashes, ellipses, «[», item numbers, labels, block IDs, heading
     levels, no «?» «।» «:-», final «။», NFC, no U+1050-U+109F, no double blank line, quotes «“ ”» paired and one
     pair per Pāli «"…"»); B2 POLARITY: every Pāli negation (no, No., Natthi / natthi, na (na parijānāti, na vattabbo,
     na + plane), nānusenti, nappajahati, nuppajjati, appahīna, nir-, the privative a- of apariyāpanna) is one Burmese
     negative (မဟုတ် / မရှိ / မရ / မကိန်းအောင်း / မပယ် / မသိ / မဖြစ်ပေါ် / အကျုံးမဝင်); the names «ရုပ်မရှိသော ဘုံ» and
     «အမှန်ကို မသိမှု» masked, variant brackets out; B3 VERBS: the sequence of anuseti / sānusaya / pajahati /
     parijānāti / pahīna / uppajjati predicates of each line, with polarity, number, «no ca» negation (double negative
     included) and form (first clause «၏», question «သလော», kati / kattha «သနည်း», statement), equals the Burmese
     sequence; every «pahīnā / vattabbā» (plural) has two or more «ca» members, every singular one; Āmantā / Natthi /
     No answers; B4 (Ka) / (Kha) labels in order, every «vā pana» = «တစ်ဖန်»; B5 digits and number words; B6 every
     recurring Pāli sentence has one Burmese (also against 7-01 … 7-05, the sample files and ch. 3); B7 table values
     (headings, colophons, notes, the variant);
  C. reuse test against the FINAL pi-1 … pi-5 rails texts, read here independently of my6_formulas:
     C1 the seven anusaya names (pi-2 ^2-816); C2 whole lines / headings and Āmantā that also occur in pi-1 … pi-5;
     C3 every reused term of REUSE (witness segment, then every line whose Pāli has it). Documented exceptions
     (EXCEPT) are listed apart, not counted.
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
import make_ch7b as MC  # noqa: E402
A = MC.A
F = MC.F
ROOT = HERE.parents[3]
NAMES = MC.NAMES_OUT
HEAD = re.compile(r"^#+ ")


def nonempty(p):
    return [l for l in p.read_text(encoding="utf-8-sig").splitlines() if l.strip()]


def body(l):
    return F.strip_id(l).strip()


NOTE_K = sorted(MC.NOTES, key=len, reverse=True)
VITTH_MY = MC.NOTES["(vitthāretabbaṃ)"]


def p_clean(p):
    """Pāli body: slips applied, variant brackets out, notes out, «…pe…» = «…»."""
    s = MC.unslip(body(p))
    s = re.sub(r" \[[^\]]*\]", "", s)
    s = re.sub(r"\. \(Vitthāretabbaṃ\)\.$", ".", s)
    s = re.sub(r" \(vitthāretabbaṃ\)\.$", ".", s)
    for k in NOTE_K:
        s = s.replace(k, " ")
    return s.replace("…pe…", "…").replace("…Pe…", "…")


def m_clean(m):
    s = re.sub(r" \[[^\]]*\]", "", body(m))
    s = s.replace(f"။ {VITTH_MY}။", "။").replace(f" {VITTH_MY}။", "။")
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

_p = re.search(r"Sattānusayā – (.+?)\. ", FIN["2"]["^2-816"][0][0])[1].split(", ")
_m = re.search(r"ကိန်းအောင်းခြင်း ခုနစ်ပါး – (.+?)။", FIN["2"]["^2-816"][1][0])[1].split("၊ ")
SEVEN = dict(zip(_p, _m))
C1 = [(k[:-1], v) for k, v in SEVEN.items()]

REUSE = [   # (regex on the Pāli line, Burmese, book, block id, Pāli witness in that rails segment)
    (r"(?<![\w])(?:a|nā)nuse(?:t|nt)", "ကိန်းအောင်း", "2", "^2-816", "anuseti"),
    (r"pajah", "ပယ်", "5", "^5-390", "pajahati"),
    (r"parijān", "ပိုင်းခြား ", "5", "^5-390", "parijānāti"),
    (r"(?<![\wa])pahīn[oā](?:ti)?(?![\w\"])", "ပယ်ပြီး ဖြစ်", "4", "^4-65", "pahīno"),
    (r"(?<![\w\"])appahīn[oā](?:ti)?(?![\w\"])", "မပယ်ရသေး", "4", "^4-45", "appahīno"),
    (r"\"(?:pahīn|appahīn)[oā]\"ti", "ဟူ၍ဖြစ်စေ", "5", "^5-386", "\"saññā atthī\"ti vā \"natthī\"ti vāti"),
    (r"na vattabb", "ခေါ်ဆို၍ မရ", "2", "^2-641", "na vattabbā"),
    (r"(?<![\w])n?uppajj", "ဖြစ်ပေါ်", "2", "^2-203", "uppajjamānā uppajjati"),
    (r"upapajj", "ပြန်လည် ဖြစ်ပေါ်", "2", "^2-1017", "upapattikkhaṇe"),
    (r"(?<![\w])[Aa]nāgām", "အနာဂါ", "4", "^4-M-7", "Anāgāmī"),
    (r"[Aa]nāgāmimagg", "အနာဂါမိမဂ်", "5", "^5-339", "anāgāmimaggaṃ"),
    (r"(?<![\w])[Aa]rah(?:ā|ato)(?![\w])", "ရဟန္တာ", "4", "^4-M-7", "Arahā"),
    (r"[Pp]uthujjan", "ပုထုဇဉ်", "1", "^1-1007", "puthujjan"),
    (r"[Aa]ṭṭhamak", "အဋ္ဌမ ပုဂ္ဂိုလ်", "5", "^5-368", "Aṭṭhamakassa puggalassa"),
    (r"[Aa]ggamagg", "အမြတ်ဆုံး", "2", "^2-1029", "agga"),
    (r"samaṅg", "ပြည့်စုံ", "2", "^2-809", "samaṅgī"),
    (r"ṭhapetvā", "ချန်ထား၍", "2", "^2-796", "ṭhapetvā"),
    (r"avasesā puggalā", "ကြွင်းကျန်သော", "2", "^2-796", "avasesā paññā"),
    (r"puggal", "ပုဂ္ဂိုလ်", "1", "^1-1050", "puggal"),
    (r"[Dd]vinnaṃ puggal", "ပုဂ္ဂိုလ် နှစ်ယောက်", "4", "^4-M-8", "Dve puggalā"),
    (r"[Tt]iṇṇaṃ puggal", "ပုဂ္ဂိုလ် သုံးယောက်", "4", "^4-M-9", "Tayo puggalā"),
    (r"[Cc]atunnaṃ puggal", "ပုဂ္ဂိုလ် လေးယောက်", "4", "^4-M-10", "Cattāro puggalā"),
    (r"[Ss]veva|[Tt]eva puggal|[Tt]asseva|[Tt]esaññeva|satteva|ṃyeva", "ပင်", "5", "^5-241", "arahattaṃyeva"),
    (r"[Kk]āmadhātu", "ကာမဘုံ", "2", "^2-991", "Kāmadhātuyā"),
    (r"(?<![\wa])[Rr]ūpadhātu", "သိမ်မွေ့သော ရုပ်ဘုံ", "2", "^2-993", "Rūpadhātuyā"),
    (r"[Aa]rūpadhātu", "ရုပ်မရှိသော ဘုံ", "2", "^2-995", "Arūpadhātuyā"),
    (r"[Dd]ukkhāya vedanāya", "နာကျင်သော ခံစားမှု", "1", "^1-M1-2", "dukkhāya vedanāya"),
    (r"vedan", "ခံစားမှု", "1", "^1-1044", "vedanā"),
    (r"dvīsu", "နှစ်ပါး", "1", "^1-1441", "dvīsu"),
    (r"tīsu", "သုံးပါး", "1", "^1-1475", "tīsu bhūmīsu"),
    (r"(?<![\w])[Aa]pariyāpann", "ဘဝဘုံတို့၌ အကျုံးမဝင်သော", "1", "^1-M2-96", "apariyāpannā"),
    (r"[Tt]adekaṭṭh", "ထိုအရာနှင့် တစ်နေရာတည်း တည်ရှိ", "2", "^2-816", "Tadekaṭṭho"),
    (r"(?<![\w])[Yy]assa(?![\w])", "အကြင်သူအား", "2", "^2-199", "Idha yassa te honti"),
    (r"kassaci", "အချို့", "2", "^2-1007", "kassaci"),
    (r"(?<![\w])kati(?![\w])", "မည်မျှ", "2", "^2-151", "kati kusalā"),
    (r"(?<![\w])satta anusayā|satteva", "ခုနစ်ပါး", "2", "^2-838", "Satta anusayā"),
    (r"bhaṅg", "ပြိုပျက်", "5", "^5-366", "bhaṅgakkhaṇe"),
    (r"heṭṭhā", "အောက်၌", "1", "^1-1287", "Heṭṭhato"),
    (r"vitthāretabb", "အကျယ် ချဲ့", "5", "^5-839", "vitthāretabb"),
    (r"pucchā", "အမေး", "5", "^5-652", "pucchā"),
    (r"okās", "နေရာ", "4", "^4-M-11", "okās"),
    (r"vāro|vāra|vāre", "ဖော်ပြချက်", "2", "^2-15-1-2-0", "Saccavāro"),
    (r"[Aa]nusayayamak", "ကိန်းအောင်းခြင်း", "1", "^1-1065", "anusay"),
]
EXCEPT = [   # documented departures (not counted as identical)
    (r"anuloma|paṭiloma", "pi-5 «အစဉ်အတိုင်း» (debate order)", "«အဟုတ်ပြ / အငြင်းပြ ပုံစံ» (sample, coordinator 2026-11-22)"),
    (r"\bNatthi\.", "pi-3 ^3-410 Natthi «မရှိ။»", "«မရှိပါ။» (answer register; coordinator 2026-11-22)"),
    (r"cutassa", "pi-5 ^5-65 cuto «… မှ သေ၍»", "«… မှ စုတေ၍ / စုတေသူ» (the sample's cavati «စုတေ»; notes-ch7b Unsure)"),
]

# ===================================================================================== the checks
MASK = [A.ARUPA_B, "အမှန်ကို မသိမှု"]          # plane name / avijjā name: no negation
LINE_EXCEPT = {}
TOKW = re.compile(r"[^\s…,.?;]+")


def p_neg(s):
    w = [x.lower().strip('"') for x in TOKW.findall(s)]
    n = sum(1 for x in w if x in ("no", "na", "natthi"))
    n += sum(1 for x in w if re.match(r"(?:nānuse|nappajah|niranusay|apariyāpann|nuppajj|appahīn)", x))
    return n


NEG_MY = re.compile(r"မဟုတ်|မရှိ|(?<=၍ )မရ(?!ှ)|မကိန်းအောင်း|မပယ်|မသိ|မဖြစ်ပေါ်|အကျုံးမဝင်")


def m_neg(s):
    for t in MASK:
        s = s.replace(t, "")
    return len(NEG_MY.findall(s))


M_VERB = re.compile(
    r"(?P<an>(?P<an_n>မ)?ကိန်းအောင်း(?!ခြင်း)(?P<an_p>ကြ)?(?P<an_e>သည်|၏|သလော|သနည်း)?(?P<an_s>ကား မဟုတ်)?)"
    r"|(?P<ph>ပယ်ပြီး ဖြစ်(?P<ph_e>သည်|၏|သလော))"
    r"|(?P<pn>မပယ်ရသေး(?!”)(?P<pn_e>သလော)?(?P<pn_s>သည်ကား မဟုတ်)?)"
    r"|(?P<pa>(?P<pa_n>မ)?ပယ်(?!ခြင်း|ပြီး|ရသေး)(?P<pa_p>ကြ)?(?P<pa_e>သည်|၏|သလော)?(?P<pa_s>ကား မဟုတ်)?)"
    r"|(?P<pj>ပိုင်းခြား (?P<pj_n>မ)?သိ(?!ခြင်း)(?P<pj_p>ကြ)?(?P<pj_e>သည်|၏|သလော)?(?P<pj_s>ကား မဟုတ်)?)"
    r"|(?<!ပြန်လည် )(?P<up>(?P<up_n>မ)?ဖြစ်ပေါ်(?!ခြင်း|ဆဲ)(?P<up_p>ကြ)?(?P<up_e>သည်|၏|သလော)?(?P<up_s>ကား မဟုတ်)?)"
    r"|(?P<sa>(?P<sa_n>မ)?ရှိသူ(?P<sa_p>များ)? (?P<sa_c>ဖြစ်|မဟုတ်)(?:ကြ)?(?P<sa_e>သည်|၏|သလော)?)")
M_FORM = {"သလော": "q", "သနည်း": "wh", "၏": "cl", "သည်": "st", None: "st", "သည်ကား မဟုတ်": "st"}


def p_verbs(s):
    """[(family, negative word, plural, «no ca», form)] in order; form 'q' / 'cl' / 'wh' (kattha, kati) / 'st'."""
    out = []
    for sent in F.SPLIT.split(s):
        w = [x.lower() for x in TOKW.findall(sent)]
        question = sent.rstrip().endswith("?") or (bool(w) and "kati" in w)
        wh = bool(w) and (w[0] == "kattha" or "kati" in w)
        noca = False
        for i, x in enumerate(w):
            if x == "no" and i + 1 < len(w) and w[i + 1] == "ca":
                noca = True
                continue
            v = MC.verb_parse(x)
            if v:
                fam, neg, pl, q = v
                if fam == "pj" and i and w[i - 1] == "na":
                    neg = True
                form = "wh" if wh else ("q" if q else ("cl" if question else "st"))
                out.append((fam, neg, pl, noca, form))
                noca = False
    return out


def expect(v):
    fam, neg, pl, noca, form = v
    if form == "cl" and neg and fam != "sa":
        form = "st"                                   # a negative first clause is the bare «မV»
    if fam == "sa":
        return (fam, neg, pl, noca, "st" if noca else form)
    if fam == "pah":
        pl = False                                     # pahīnā: no «ကြ» (pi-4); number checked apart (B3b)
    return (fam, neg or noca, pl, neg and noca, form)


def m_verbs(s):
    out = []
    for y in M_VERB.finditer(s):
        if y["ph"]:
            out.append(("pah", False, False, False, M_FORM[y["ph_e"]]))
        elif y["pn"]:
            out.append(("pah", True, False, bool(y["pn_s"]), M_FORM[y["pn_e"]]))
        for fam in ("an", "pa", "pj", "up", "sa"):
            if y[fam]:
                f2 = {"an": "anu", "pa": "pa", "pj": "pj", "up": "up", "sa": "sa"}[fam]
                last = bool(y[f"{fam}_s"]) if fam != "sa" else y["sa_c"] == "မဟုတ်"
                out.append((f2, bool(y[f"{fam}_n"]), bool(y[f"{fam}_p"]), last, M_FORM[y[f"{fam}_e"]]))
    return out


def p_number(s):
    """B3b: every pahīna / vattabba predicate: plural (-ā) iff two or more anusaya terms in its clause."""
    bad = []
    for sent in F.SPLIT.split(s):
        n = 0
        for x in re.findall(r'"[^"]*"ti|…|[^\s…,.?;]+|[,;.?]', sent):
            xl = x.lower()
            if A.TERM_RE.match(xl):
                n += 1
            elif re.fullmatch(r"(?:ap)?pahīn[oā](?:ti)?|vattabb[oā]", xl):
                pl = re.fullmatch(r"(?:ap)?pahīnā(?:ti)?|vattabbā", xl) is not None
                if (pl != (n >= 2) or n == 0) and not (n == 0 and xl.startswith("vattabb")):
                    bad.append(f"{x} with {n} term(s)")    # «Na vattabbo / vattabbā …» alone: no subject
                n = 0
            elif MC.verb_parse(xl) or xl in (",", ";", ".", "?"):
                n = 0
            elif x == "…" and n:
                n -= 1                                 # «X…pe… Y»: alternatives, one subject
    return bad


NUMW = [  # (Pāli regex, Burmese number word)
    (r"(?<![\w])dvīsu", "နှစ်ပါး"), (r"(?<![\w])tīsu", "သုံးပါး"),
    (r"(?<![\w])satta anusayā|satteva", "ခုနစ်ပါး"), (r"(?<![\w])pañca anusayā", "ငါးပါး"),
    (r"(?<![\w])tayo anusayā", "သုံးပါး"),
    (r"\(Ekamūlak", "တစ်ပါး"), (r"\(Dukamūlak", "နှစ်ပါး"), (r"\(Tikamūlak", "သုံးပါး"), (r"\(Catukkamūlak", "လေးပါး"),
    (r"\(Pañcakamūlak", "ငါးပါး"), (r"\(Chakkamūlak", "ခြောက်ပါး"),
    (r"(?<![\w])(?:[Dd]vinnaṃ|[Dd]ve) (?:puggal|maggasamaṅgīn)", "နှစ်ယောက်"),
    (r"(?<![\w])(?:[Tt]iṇṇaṃ|[Tt]ayo) puggal", "သုံးယောက်"),
    (r"(?<![\w])(?:[Cc]atunnaṃ|[Cc]attāro) puggal", "လေးယောက်"), (r"[Aa]ṭṭhamak", "အဋ္ဌမ"),
    (r"(?<![\w])kati(?![\w])", "မည်မျှ"), (r"(?<![\w])kassaci(?![\w])", "အချို့"),
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
    n_lines = n_q = 0
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
            k = p.count('"') // 2 + MC.COLO.get(MC.unslip(body(p)), "").count("“")   # «X niṭṭhitaṃ.» «“X” …»
            n_q += k
            if m.count("“") != k or m.count("”") != k or re.search(r"“[^”]*“", m):
                bad.append(f"B1 {name}:{i} quotes Pāli {k} pairs vs «“» {m.count('“')} «”» {m.count('”')}")
    say(f"B1 structure: {n_lines} lines; {n_q} quotation pairs paired and not nested")
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
    say(f"B2 polarity: {n_pol} negations (no, na, Natthi / natthi, nānusenti, nappajahati, nuppajjati, appahīna, "
        f"apariyāpanna), each one Burmese negative")
    # B3
    n_verb = n_ans = n_num = 0
    for name, (P, M, _) in PAIRS.items():
        for i, (p, m) in enumerate(zip(P, M), 1):
            if HEAD.match(p):
                continue
            s, ms = p_clean(p), m_clean(m)
            exp = [expect(v) for v in p_verbs(s)]
            got = m_verbs(ms)
            n_verb += len(exp)
            if exp != got:
                k = next((j for j, (x, y) in enumerate(zip(exp, got)) if x != y), min(len(exp), len(got)))
                bad.append(f"B3 {name}:{i} verbs (#{k}) Pāli {exp[k:k + 2]} vs Burmese {got[k:k + 2]} "
                           f"({len(exp)} vs {len(got)})")
            nb = p_number(s)
            n_num += len(re.findall(r'(?<![\w"])(?:ap)?pahīn[oā](?:ti)?(?![\w"])|vattabb[oā]', s))
            if nb:
                bad.append(f"B3b {name}:{i} number: {nb[:2]}")
            for pa, my, rx in (("Āmantā", F.YES[:-1], r"\bĀmantā\b"), ("Natthi", F.NATTHI[:-1], r"\bNatthi\b"),
                               ("No", F.NO[:-1], r"(?<![\w])No(?![\w])")):
                k = len(re.findall(rx, s))
                n_ans += k
                if k != ms.count(my):
                    bad.append(f"B3 {name}:{i} «{pa}» {k}x vs «{my}» {ms.count(my)}x")
    say(f"B3 verbs: {n_verb} anuseti / sānusaya / pajahati / parijānāti / pahīna / uppajjati predicates (family, "
        f"polarity, number, «no ca», double negative, form) in order; B3b {n_num} pahīna / vattabba numbers; "
        f"{n_ans} answers")
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
            if HEAD.match(b) or b in MC.COLO or MC.unslip(b) in MC.COLO or b in MC.LINES:
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
    others = (["1-mulayamaka.md", "2-01-khandhayamaka.md"] + [f"3-0{i}-ayatanayamaka.md" for i in range(1, 7)]
              + [f"7-0{i}-anusayayamaka.md" for i in range(1, 6)])
    for name in others:
        if not (MC.OUT / name).exists():
            continue
        P, M = nonempty(MC.PALI / name), nonempty(MC.OUT / name)
        for p, m in zip(P, M):
            b = body(p)
            if HEAD.match(b) or "…" in b or b in F.COLO or "[" in b or "(" in b[4:]:
                continue
            b = A.unslip(b)
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
        f"(also {n_x} occurrences in 7-01 … 7-05, the approved sample files and ch. 3)")
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
            ub = MC.unslip(b)
            if ub in MC.COLO:
                n_tab += 1
                if mb != MC.COLO[ub]:
                    bad.append(f"B7 {name}:{i} colophon")
            for k in NOTE_K:
                c = ub.count(k)
                if c:
                    n_tab += c
                    if mb.count(MC.NOTES[k]) < c:
                        bad.append(f"B7 {name}:{i} note «{k[:30]}»")
            for inner in re.findall(r"\[([^\]]*)\]", ub):
                n_tab += 1
                if MC.VARIANT.get(inner, "\0") not in mb:
                    bad.append(f"B7 {name}:{i} variant «{inner[:30]}»")
    say(f"B7 table values: {n_tab} headings / colophons / notes / variants")
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
        muts = [("dropped «မ» (nappajahati)", "ကို မပယ်၊", "ကို ပယ်၊"),
                ("double negative dropped", "မပယ်သည်ကား မဟုတ်", "မပယ်"),
                ("na parijānāti polarity", "ပိုင်းခြား မသိသလော", "ပိုင်းခြား သိသလော"),
                ("plural «ကြ» dropped", "ပိုင်းခြား မသိကြ", "ပိုင်းခြား မသိ"),
                ("pahīno polarity", "ကို ပယ်ပြီး ဖြစ်သည်", "ကို မပယ်ရသေး"),
                ("appahīno double negative", "မပယ်ရသေးသည်ကား မဟုတ်", "မပယ်ရသေး"),
                ("vattabba negation dropped", "ခေါ်ဆို၍ မရ", "ခေါ်ဆို၍ ရ"),
                ("quote swapped", "“မပယ်ရသေး”", "“ပယ်ပြီး”"),
                ("uppajjati polarity", "ဖြစ်ပေါ်သလော", "မဖြစ်ပေါ်သလော"),
                ("«ဟုတ်ပါသည်» changed", "ဟုတ်ပါသည်။", "မဟုတ်ပါ။"),
                ("anusaya name changed", "မာန ကိန်းအောင်းခြင်း", "ဘဝရာဂ ကိန်းအောင်းခြင်း"),
                ("label", "(ခ) ", "(က) "), ("person count", "နှစ်ယောက်", "သုံးယောက်"),
                ("place", "သိမ်မွေ့သော ရုပ်ဘုံ", "ကာမဘုံ"), ("plane negation", "ကာမဘုံ မဟုတ်သော ဘုံ၌", "ကာမဘုံ၌"),
                ("number of tendencies", "ကိန်းအောင်းခြင်း ငါးပါး", "ကိန်းအောင်းခြင်း သုံးပါး"),
                ("kati question verb", "မကိန်းအောင်းကြသနည်း", "ကိန်းအောင်းကြသနည်း"),
                ("question verb form", "ပိုင်းခြား သိသလော", "ပိုင်းခြား သိသည်"),
                ("ṭhapetvā member", "အဋ္ဌမ ပုဂ္ဂိုလ်ကို ချန်ထား၍", "ရဟန္တာကို ချန်ထား၍")]
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
            else:
                print(f"mutation {desc}: not applicable")
        sys.exit(0)
    bad, (ts, tn) = run_checks(PAIRS)
    for (nm, ln, ck), why in LINE_EXCEPT.items():
        print(f"   line exception {ck} {nm}:{ln}: {why}")
    print(f"\nmismatches: {len(bad)}")
    for b in bad[:60]:
        print("  ", b)
    sys.exit(1 if bad else 0)
