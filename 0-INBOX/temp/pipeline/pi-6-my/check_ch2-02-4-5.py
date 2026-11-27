"""Check the Burmese zero-shot of pi-6 chapters 2-02, 4, 5-01, 5-02, 5-03 line by line (adapted from check_sample.py).

usage: python3 -I -X utf8 check_ch2-02-4-5.py [chapter ...]
  A. rebuild: make_ch2-02-4-5.py regenerates the files byte for byte (nothing written here);
  Added to the sample's tests: the pariññā verbs (parijānāti «ပိုင်းခြား သိ», pajahati «ပယ်») in B2 / B3 (tense,
  polarity, «no ca» double negative), «na paṭilabhissanti» «မရရှိ», «na kātabbaṃ» «မပြု», lowercase «natthi»; masks
  for the a-X-ka attributes («… မရှိသော»); number words aṭṭhārasa / cattāri / dutiya; the dhātu and sacca names and
  this script's reused terms in C3; the documented exceptions of notes-ch2-02-4-5.md.
  B. per line: B1 structure (equal non-empty lines, dashes, ellipses, «[», item numbers, labels (Ka) … = (က) …, block
     IDs, heading levels, no «?» «।» «:-», final «။», NFC, no U+1050-U+109F); B2 POLARITY per line: every Pāli
     negation (na, no, nuppajjati, Natthi) is one Burmese negative (မဟုတ် / မရှိ / မအခြေခံ / မ + verb), fixed
     terms masked (abyākata, ahetuka, arūpa); B3 VERBS: the sequence of uppajj- / nirujjh- verbs of each line, with
     its tense (present / past -ittha / future -issati) and polarity, equals the Burmese sequence (no ca + negative
     verb = «… မVသည်ကား မဟုတ်»); Āmantā = «ဟုတ်ပါသည်», Natthi = «မရှိ။»; B4 (Ka) / (Kha) pairs: labels in order per
     segment, «vā pana» = «တစ်ဖန်»; B5 numbers: digits and number words (tīṇi / tayo, nava, pañca-, catu-);
     B6 every recurring Pāli sentence (labels off, «-ti?» = «?») has one and the same Burmese at every occurrence;
     B7 table values: headings, colophons and whole lines come out as their table value;
  C. reuse test against the FINAL pi-1 … pi-5 rails texts, read here independently of my6_formulas:
     C1 the khandha names and the bare terms rūpa / vedanā / saññā / saṅkhārā / viññāṇa (pi-2 ^2-1, pi-1 ^1-1044);
     C2 whole lines / headings / answer sentences of the sample that also occur in pi-1 … pi-5;
     C3 every reused term of REUSE: a rails segment has the Pāli and the Burmese (witness), and every sample line whose
     Pāli has the term has that Burmese. Documented exceptions (EXCEPT) are listed apart, not counted as identical.
Prints the mismatches (0 expected) and the counts; exit 1 on any mismatch.
"""
import pathlib
import re
import sys
import unicodedata

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import importlib.util  # noqa: E402
_spec = importlib.util.spec_from_file_location("make_ch2_02_4_5", HERE / "make_ch2-02-4-5.py")
MS = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(MS)                   # tables only; the generator writes files only under __main__
F = MS.F
ROOT = HERE.parents[3]
NAMES = [a for a in sys.argv[1:] if not a.startswith("-")] or MS.NAMES_OUT
bad = []


def nonempty(p):
    return [l for l in p.read_text(encoding="utf-8-sig").splitlines() if l.strip()]


def body(l):
    return F.strip_id(l).strip()


def nobr(s):
    return re.sub(r" ?\[[^\]]*\]", "", s)


PAIRS = {name: (nonempty(MS.PALI / name), nonempty(MS.OUT / name)) for name in NAMES}
HEAD = re.compile(r"^#+ ")

# ===================================================================================== A. rebuild
for name in NAMES:
    text, nbad = MS.run(name)
    if nbad or text != (MS.OUT / name).read_text(encoding="utf-8"):
        bad.append(f"A {name}: regenerated text differs")
print(f"A. rebuild: {len(NAMES)} / {len(NAMES)} files regenerated identical" if not bad else "A. rebuild: FAILED")

# ===================================================================================== B1 structure
n_lines = 0
for name, (P, M) in PAIRS.items():
    if len(P) != len(M):
        bad.append(f"B1 {name}: {len(P)} vs {len(M)} lines")
        continue
    raw = (MS.OUT / name).read_text(encoding="utf-8")
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
print(f"B1 structure: {n_lines} lines")

# ===================================================================================== B2 polarity
MASK = [F.ABY, F.AHETUKA, F.PLACES["arūpa"]] + [v + "သော" for k, v in MS.ATTR.items() if k.startswith("a") and
                                                 not k.startswith("abhi")] + [v + F.THEM for k, v in MS.ATTR.items()
                                                                              if k.startswith("a") and not k.startswith("abhi")]
MASK += [v for k, v in MS.SA_ATTR.items() if k.startswith("a")] + ["သို့မဟုတ်"]   # a-X-ka «X မရှိဘဲ»; «or»
MASK.sort(key=len, reverse=True)


def p_neg(p):
    s = nobr(body(p))
    return (len(re.findall(r"(?<![\w])(?:na|no|No|Na)(?![\w])", s)) + len(re.findall(r"nuppajj|nappajah", s))
            + len(re.findall(r"\b[Nn]atthi\b", s)))


def m_neg(m):
    s = nobr(body(m))
    for t in MASK:
        s = s.replace(t, "")
    return (s.count("မဟုတ်") + s.count("မရှိ") + s.count("မအခြေခံ") + s.count("မဖြစ်ပေါ်") + s.count("မချုပ်ငြိမ်း")
            + s.count("ပိုင်းခြား မသိ") + s.count("မပယ်") + s.count("မရရှိ") + s.count("မပြု"))


n_pol = 0
for name, (P, M) in PAIRS.items():
    for i, (p, m) in enumerate(zip(P, M), 1):
        if HEAD.match(p):
            continue
        a, b = p_neg(p), m_neg(m)
        n_pol += a
        if a != b:
            bad.append(f"B2 {name}:{i} negations Pāli {a} vs Burmese {b}")
print(f"B2 polarity: {n_pol} negations, each one Burmese negative")

# ===================================================================================== B3 verbs, tense, answers
P_VERB = re.compile(r"(?P<noca>no ca (?:tesaṃ tattha|tesaṃ|tattha) \S+ )?(?P<na>na )?(?P<n>n)?(?P<r>uppajj|nirujjh)"
                    r"(?P<e>issanti|issati|issatīti|ittha|itthāti|attha|anti|ati|atīti|iti)\b", re.I)
P_END = {"issanti": "fut", "issati": "fut", "issatīti": "fut", "ittha": "past", "itthāti": "past", "attha": "past",
         "anti": "pres", "ati": "pres", "atīti": "pres",
         "iti": "pres"}   # «nirujjhiti» ^6-5-125: source slip for nirujjhati
M_VERB = re.compile(r"(?<!ပြန်လည် )(?P<neg>မ)?(?P<r>ဖြစ်ပေါ်|ချုပ်ငြိမ်း)(?!လာ|ခြင်း|ပြီး)(?:ကြ)?(?P<t>ခဲ့|လိမ့်မည်|မည့်)?"
                    r"(?P<ns>(?:သည်)?ကား မဟုတ်)?")
M_ROOT = {"ဖြစ်ပေါ်": "uppajj", "ချုပ်ငြိမ်း": "nirujjh"}
M_T = {None: "pres", "ခဲ့": "past", "လိမ့်မည်": "fut", "မည့်": "fut"}
PP_VERB = re.compile(r"(?P<noca>no ca (?:te )?\S+ )?(?P<na>na |nap)?(?P<r>parijān|pajah)"
                     r"(?P<e>issanti|issati|issatīti|ittha|itthāti|anti|āti|ātīti|ati|atīti)\b")
PP_END = {"issanti": "fut", "issati": "fut", "issatīti": "fut", "ittha": "past", "itthāti": "past", "anti": "pres",
          "āti": "pres", "ātīti": "pres", "ati": "pres", "atīti": "pres"}
PM_VERB = re.compile(r"(?P<r>ပိုင်းခြား (?P<n1>မ)?သိ(?!ခြင်း|မြင်)|(?<!နယ်)(?P<n2>မ)?ပယ်)(?:ကြ)?(?P<t>ခဲ့|လိမ့်မည်)?(?:ကြ)?"
                     r"(?P<ns>(?:သည်)?ကား မဟုတ်)?")
n_pverb = 0
n_verb = n_ans = 0
for name, (P, M) in PAIRS.items():
    for i, (p, m) in enumerate(zip(P, M), 1):
        if HEAD.match(p):
            continue
        s = nobr(body(p))
        exp = []
        for x in P_VERB.finditer(s):
            neg = bool(x["na"] or x["n"])
            exp.append((x["r"].lower(), P_END[x["e"]], neg or bool(x["noca"]), neg and bool(x["noca"])))
        got = [(M_ROOT[y["r"]], M_T[y["t"]], bool(y["neg"]), bool(y["ns"])) for y in M_VERB.finditer(nobr(body(m)))]
        n_verb += len(exp)
        if exp != got:
            bad.append(f"B3 {name}:{i} verbs Pāli {exp} vs Burmese {got}")
        pexp = []
        for x in PP_VERB.finditer(s):
            neg = bool(x["na"])
            pexp.append((x["r"], PP_END[x["e"]], neg or bool(x["noca"]), neg and bool(x["noca"])))
        pgot = [("parijān" if y["r"].startswith("ပိုင်း") else "pajah", M_T[y["t"]], bool(y["n1"] or y["n2"]),
                 bool(y["ns"])) for y in PM_VERB.finditer(nobr(body(m)))]
        n_pverb += len(pexp)
        if pexp != pgot:
            bad.append(f"B3 {name}:{i} pariññā verbs Pāli {pexp} vs Burmese {pgot}")
        for pa, my in (("Āmantā", F.YES), ("Natthi.", F.NATTHI)):
            k = len(re.findall("[Āā]mantā", s)) if pa == "Āmantā" else s.count(pa)
            n_ans += k
            got = body(m).count(F.YES[:-1]) if pa == "Āmantā" else len(re.findall(r"(?:^|လော။ |^\([က-အ]\) )" + my, body(m)))
            if k != got:
                bad.append(f"B3 {name}:{i} «{pa}» {k}x vs «{my}» {got}x")
print(f"B3 verbs: {n_verb} uppajj / nirujjh + {n_pverb} parijān / pajah verbs (root, tense, polarity, double "
      f"negative) in order; {n_ans} answers")

# ===================================================================================== B4 pairs
n_pair = 0
for name, (P, M) in PAIRS.items():
    lp = [F.LABEL_RE.match(p)[1] for p in P if F.LABEL_RE.match(p)]
    lm = [re.match(r"^\(([က-အ])\) ", m)[1] for m in M if re.match(r"^\(([က-အ])\) ", m)]
    n_pair += len(lp)
    if [F.AKKHARA[x] for x in lp] != lm:
        bad.append(f"B4 {name}: label sequence differs")
    for i, (p, m) in enumerate(zip(P, M), 1):
        if p.count("vā pana") != m.count(F.VA_PANA):
            bad.append(f"B4 {name}:{i} vā pana vs «{F.VA_PANA}»")
print(f"B4 pairs: {n_pair} labelled lines in order, every «vā pana» = «{F.VA_PANA}»")

# ===================================================================================== B5 numbers
NUMW = [(r"\b(?:Tīṇeva|Tayo eva)\b", "သုံးပါး"), (r"\bNaveva\b", "ကိုးပါး"), (r"pañca(?=kkhandh|vokār)|Pañca(?=kkhandh|vokār)",
                                                                   "ငါးပါး"),
        (r"[Cc]atu(?=vokār)|\bCattāri\b", "လေးပါး"), (r"[Ee]ka(?=vokār)", "တစ်ပါး"), (r"\bAṭṭhārasa\b", "ဆယ့်ရှစ်ပါး"),
        (r"\bdutiye\b", "ဒုတိယ")]
n_num = 0
for name, (P, M) in PAIRS.items():
    for i, (p, m) in enumerate(zip(P, M), 1):
        s = nobr(body(p))
        if re.findall(r"\d", re.sub(r"\^\S+", "", p)) != re.findall(r"\d", re.sub(r"\^\S+", "", m)):
            bad.append(f"B5 {name}:{i} digits")
        for rx, my in NUMW:
            k = len(re.findall(rx, s))
            n_num += k
            if k != nobr(m).count(my):
                bad.append(f"B5 {name}:{i} «{rx}» {k}x vs «{my}» {nobr(m).count(my)}x")
print(f"B5 numbers: digits per line equal; {n_num} number words")


# ===================================================================================== B6 recurring sentences
def canon(s):
    s = F.LABEL_RE.sub("", s.strip())
    s = re.sub(r"nti\?$", "ṃ?", s)
    s = re.sub(r"(?<=[āaoe])ti\?$", "?", s)
    s = re.sub(r"īti\?$", "i?", s)
    s = re.sub(r"āti\?$", "a?", s)
    return s.replace("ti. ", "? ") if s.endswith("ti.") else s


occ = {}
# B6 also reads the approved sample chapters (read only), so a sentence shared with 1 / 2-01 must have their Burmese
SAMPLE_NAMES = ["1-mulayamaka.md", "2-01-khandhayamaka.md"]
B6_PAIRS = dict(PAIRS)
B6_PAIRS.update({n: (nonempty(MS.PALI / n), nonempty(MS.OUT / n)) for n in SAMPLE_NAMES})
for name, (P, M) in B6_PAIRS.items():
    for i, (p, m) in enumerate(zip(P, M), 1):
        b, mb = body(p), body(m)
        if HEAD.match(b) or "…" in b or b in F.COLO or nobr(b) in F.LINES or F.BRACKET.sub("⟦v⟧", b) in F.LINES:
            continue
        lab = F.LABEL_RE.match(b)
        b = F.LABEL_RE.sub("", b)
        mb = re.sub(r"^\([က-အ]\) ", "", mb)
        ps = F.SPLIT.split(nobr(b))
        ms = [x if x.endswith("။") else x + "။" for x in re.split(r"(?<=။) ", nobr(mb))]
        if len(ps) != len(ms):
            bad.append(f"B6 {name}:{i} {len(ps)} Pāli vs {len(ms)} Burmese sentences")
            continue
        for j, (x, y) in enumerate(zip(ps, ms)):
            k = canon(x)
            if j == 0 and lab:
                y = y.replace(F.VA_PANA + " ", "", 1) if "vā pana" in x else y
            occ.setdefault(k, set()).add(y)
n_rec = sum(1 for v in occ.values())
for k, v in occ.items():
    if len(v) > 1:
        bad.append(f"B6 «{k[:70]}» has {len(v)} Burmese renderings")
print(f"B6 recurring sentences: {n_rec} distinct Pāli sentences (with the sample's 1 / 2-01), each with one Burmese "
      f"rendering")

# ===================================================================================== B7 table values
n_tab = 0
for name, (P, M) in PAIRS.items():
    for i, (p, m) in enumerate(zip(P, M), 1):
        b, mb = body(p), body(m)
        h = re.match(r"^(#+) (.*)$", b)
        if h:
            n_tab += 1
            if mb != f"{h[1]} {F.heading(h[2])}":
                bad.append(f"B7 {name}:{i} heading")
            continue
        if b in F.COLO:
            n_tab += 1
            if mb != F.COLO[b]:
                bad.append(f"B7 {name}:{i} colophon")
        elif b in F.LINES:
            n_tab += 1
            if mb != F.LINES[b]:
                bad.append(f"B7 {name}:{i} line table")
        elif F.BRACKET.sub("⟦v⟧", b) in F.LINES:
            n_tab += 1
            if nobr(mb) != nobr(F.LINES[F.BRACKET.sub("⟦v⟧", b)].format(v="")):
                bad.append(f"B7 {name}:{i} line table")
print(f"B7 table values: {n_tab} headings / colophons / table lines")

# ===================================================================================== B8 quotes
n_q = 0
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
                ok &= depth == 1                 # inner quotes only inside outer ones
        if "“" in t:
            n_q += 1
        if not ok or depth:
            bad.append(f"B8 {name}:{i} quote nesting")
print(f"B8 quotes: {n_q} lines with quotes, “…” outer / ‘…’ inner, balanced")

# ===================================================================================== C. reuse test
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


FIN = {}        # book -> {id: (pāli lines, burmese lines)}, read here (not through my6_formulas)
FIN_LINE = {}   # whole Pāli line (no ID, no #) -> set of Burmese lines
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

# C1 topic names and bare terms
ITEMS = dict(zip(*[[x.strip() for x in nobr(body(FIN["2"]["^2-1"][j][0])).split(" – ")[1].rstrip(".။").split(sep)]
                   for j, sep in ((0, ","), (1, "၊"))]))
BARE = dict(zip(["rūpaṃ", "vedanā", "saññā", "saṅkhārā", "viññāṇaṃ"],
                [x.strip() for x in re.search(r"ရုပ်၊ ခံစားမှု၊ မှတ်သိမှု၊ ပြုပြင်ဖန်တီးမှုများ၊ သိစိတ်",
                                              " ".join(FIN["1"]["^1-1044"][1]))[0].split("၊")]))
C1 = [(rf"\b{k[:-1]}", v) for k, v in ITEMS.items()]                    # rūpakkhandh… -> «ရုပ် အစုအဝေး»
C1 += [(r"\brūpa(?:ṃ|nti|ñca|ñceva)(?![\w])", BARE["rūpaṃ"]), (r"\bvedan(?:ā|aṃ|añca|āti)(?![\w])", BARE["vedanā"]),
       (r"\bsaññ(?:ā|aṃ|añca|āti)(?![\w])", BARE["saññā"]), (r"\bsaṅkhār(?:ā|e|āti)(?![\w])", BARE["saṅkhārā"]),
       (r"\bviññāṇ(?:aṃ|anti|añca)(?![\w])", BARE["viññāṇaṃ"])]
n_c1 = s_c1 = 0
for name, (P, M) in PAIRS.items():
    for i, (p, m) in enumerate(zip(P, M), 1):
        s = nobr(body(p))
        for rx, my in C1:
            k = len(re.findall(rx, s, re.I))
            if k:
                n_c1 += 1
                if my in m:
                    s_c1 += 1
                else:
                    bad.append(f"C1 {name}:{i} «{rx}» -> «{my}» missing")
# C2 whole lines / headings / answer sentences
n_c2 = s_c2 = 0
for name, (P, M) in PAIRS.items():
    for i, (p, m) in enumerate(zip(P, M), 1):
        k = re.sub(r"^#+ ", "", body(p))
        k = F.LABEL_RE.sub("", k)
        if k in FIN_LINE:
            n_c2 += 1
            if re.sub(r"^\([က-အ]\) ", "", re.sub(r"^#+ ", "", body(m))) in FIN_LINE[k]:
                s_c2 += 1
            else:
                bad.append(f"C2 {name}:{i} «{k[:50]}»: «{body(m)[:50]}» vs final {sorted(FIN_LINE[k])[:2]}")
FIN_SENT = {"Āmantā.": ("5", "^5-1", "ဟုတ်ပါသည်။")}   # Natthi: explained exception (answer register), see EXCEPT
for sent, (bk, bid, my) in FIN_SENT.items():
    if sent not in " ".join(FIN[bk][bid][0]) or my not in " ".join(FIN[bk][bid][1]):
        bad.append(f"C2 witness {sent}")
    for name, (P, M) in PAIRS.items():
        for i, (p, m) in enumerate(zip(P, M), 1):
            k = nobr(body(p)).count(sent.rstrip(".")) if sent == "Āmantā." else nobr(body(p)).count(sent)
            if k:
                n_c2 += k
                got = min(k, body(m).count(my[:-1] if sent == "Āmantā." else my))
                s_c2 += got
                if got < k:
                    bad.append(f"C2 {name}:{i} «{sent}»")

# C3 reused terms: (regex on the sample Pāli line, Burmese, book, block id, Pāli witness in that rails segment)
REUSE = [
    (r"(?<!a)\bkusalā dhammā", "ကုသိုလ် သဘောတရား", "1", "^1-M1-1", "(Ka) kusalā dhammā"),
    (r"\bakusalā dhammā", "အကုသိုလ် သဘောတရား", "1", "^1-M1-1", "(Kha) akusalā dhammā"),
    (r"abyākat", F.ABY, "1", "^1-M1-1", "abyākatā dhammā"),
    (r"(?<![\w])kusalamūl", "ကုသိုလ်၏ အမြစ်", "1", "^1-32", "kusalamūlaṃ"),
    (r"akusalamūl", "အကုသိုလ်၏ အမြစ်", "1", "^1-389", "akusalamūl"),
    (r"\bnām(?:a|ā)", "စိတ်ပိုင်း", "1", "^1-M2-109", "nāmañca"),
    (r"\bahetuk", "အမြစ် မရှိသော", "1", "^1-M2-2", "ahetukā dhammā"),
    (r"\bsahetuk", "အမြစ် ရှိသော", "1", "^1-M2-2", "sahetukā dhammā"),
    (r"sahajāt", "နှင့်အတူ ပေါ်ပေါက်သော", "5", "^5-473", "sahajātā"),
    (r"samuṭṭhānaṃ rūpaṃ", "မှ ဖြစ်ပေါ်လာသော", "1", "^1-M2-60", "cittasamuṭṭhānā"),
    (r"\bekato\b", "တစ်ပြိုင်နက်", "1", "^1-1447", "ekato"),
    (r"aññamañña", "အချင်းချင်း", "1", "^1-1083", "aññamañña"),
    (r"\bavasesā\b", "ကြွင်းကျန်သော", "2", "^2-796", "avasesā paññā"),
    (r"ṭhapetvā", "ချန်ထား၍", "2", "^2-796", "ṭhapetvā"),
    (r"(?<![\w])n?uppajj", "ဖြစ်ပေါ်", "2", "^2-203", "uppajjamānā uppajjati"),
    (r"nirujjh", "ချုပ်ငြိမ်း", "2", "^2-204", "nirujjhamānā nirujjhati"),
    (r"upapajj", "ပြန်လည် ဖြစ်ပေါ်", "2", "^2-1024", "kattha upapajjanti"),
    (r"\bcavant", "စုတေ", "2", "^2-1029", "cavanti āyusaṅkhayā"),
    (r"parinibb", "ပရိနိဗ္ဗာန် ပြု", "4", "^4-M-7", "parinibbāyī"),
    (r"pañcavokār", "အစုအဝေး ငါးပါး ရှိသော ဘဝ", "2", "^2-234", "pañcavokārabhavo"),
    (r"catuvokār", "အစုအဝေး လေးပါး ရှိသော ဘဝ", "2", "^2-234", "catuvokārabhavo"),
    (r"asaññasatt", "အသညသတ်", "2", "^2-18-4-3-0", "Asaññasattā"),
    (r"\barūp(?:aṃ|e|ā|ānaṃ)\b", "ရုပ်မရှိသော ဘုံ", "2", "^2-234", "arūpabhavo"),
    (r"piyarūpaṃ sātarūpaṃ", F.PIYA, "2", "^2-203", "Kiñca loke piyarūpaṃ sātarūpaṃ"),
    (r"diṭṭhi", "အယူ", "1", "^1-M2-111", "diṭṭhi"),
    (r"āhār", "အာဟာရ", "1", "^1-70", "tayo āhārā"),
    (r"ārammaṇ", "အာရုံ", "1", "^1-M1-13", "ārammaṇ"),
    (r"paccay", "အထောက်အပံ့", "1", "^1-1344", "paccay"),
    (r"samuday", "ဖြစ်ပေါ်ခြင်း", "1", "^1-1063", "samuday"),
    (r"okās", "နေရာ", "4", "^4-M-11", "okās"),
    (r"\batīt", "အတိတ်", "1", "^1-M1-18", "atītā dhammā"),
    (r"\banāgat", "အနာဂတ်", "1", "^1-M1-18", "anāgatā dhammā"),
    (r"paccuppann", "ပစ္စုပ္ပန်", "1", "^1-M1-18", "paccuppannā dhammā"),
    (r"\buddes", "အကျဉ်း ဖော်ပြချက်", "3", "^3-1-0", "Uddeso"),
    (r"niddes", "အကျယ် ဖော်ပြချက်", "1", "^1-2-3-1-0", "Ekakaniddeso"),
    (r"(?<!āyata)naya", "ခွဲနည်း", "3", "^3-1-1-0", "Naya"),
    (r"suddha(?!vās)", "ရိုးရိုး", "5", "^5-1-1-0", "Suddh"),
    (r"paṇṇatti", "သတ်မှတ်ချက်", "1", "^1-M2-108", "paññatti"),
    (r"puggal", "ပုဂ္ဂိုလ်", "1", "^1-1050", "puggal"),
    (r"vārādi", "စသည်", "3", "^3-15-1-1-0", "Khandhādi"),
    (r"uppāda(?!kkhaṇ)", "ဖြစ်ပေါ်ခြင်း", "1", "^1-1-0", "Cittuppādakaṇḍaṃ"),
    (r"nirodha", "ချုပ်ငြိမ်းခြင်း", "1", "^1-1063", "nirodh"),
    (r"vāro\b|vāra(?!ṃ)", "ဖော်ပြချက်", "2", "^2-15-1-2-0", "Saccavāro"),
    (r"evamuparipi", F.EVAM_UPARI, "2", "^2-718", "evamuparipi"),
    (r"\byassa\b(?! cittassa)", "အကြင်သူအား", "2", "^2-199", "Idha yassa te honti"),
    (r"(?<![\w])khandhā(?![\w])", "အစုအဝေးတို့", "5", "^5-212", "Khandhā"),
    (r"(?<![\w])mūla(?:ṃ|vāro|nayo)", "အမြစ်", "1", "^1-32", "kusalamūlaṃ"),
    (r"niṭṭhit", "” ပြီးဆုံးပြီ။", "2", "^2-153", "Khandhavibhaṅgo niṭṭhito"),
    # --- reused in chapters 2-02, 4, 5 (this script)
    (r"\bdhātu(?!yamak)|\bdhātū", "ဓာတ်", "1", "^1-M2-121", "dhātu"),
    (r"\bsacc", "သစ္စာ", "2", "^2-206", "Cattāri saccāni"),
    (r"dukkhasacc", "ဒုက္ခ သစ္စာ", "4", "^4-M-5", "dukkhasaccaṃ"),
    (r"samudayasacc", "ဖြစ်ပေါ်ခြင်း သစ္စာ", "4", "^4-M-5", "samudayasaccaṃ"),
    (r"nirodhasacc", "ချုပ်ငြိမ်းခြင်း သစ္စာ", "4", "^4-M-5", "nirodhasaccaṃ"),
    (r"maggasacc", "မဂ် သစ္စာ", "4", "^4-M-5", "maggasaccaṃ"),
    (r"(?<![\w])dukkh(?:aṃ|añca|añceva|anti)(?![\w])", "နာကျင်မှု", "1", "^1-559", "dukkhaṃ hoti"),
    (r"[Kk]āyikaṃ dukkhaṃ", "ကိုယ်ပိုင်းဆိုင်ရာ နာကျင်မှု", "1", "^1-559", "kāyikaṃ dukkhaṃ"),
    (r"(?<![\w])magg(?:o|aṃ|añca|assa)(?![\w])|aggamagg", "မဂ်", "1", "^1-1039", "maggahetukā"),
    (r"phal", "ဖိုလ်", "1", "^1-996", "maggaphalāni"),
    (r"\bagga", "အမြတ်ဆုံး", "2", "^2-1029", "agga"),
    (r"[Aa]rah", "ရဟန္တာ", "4", "^4-M-7", "Arahā"),
    (r"puthujjan", "ပုထုဇဉ်", "1", "^1-1007", "puthujjano"),
    (r"samaṅgī", "နှင့် ပြည့်စုံသူ", "1", "^1-1039", "Ariyamaggasamaṅgissa"),
    (r"paṭilabh", "ရရှိ", "2", "^2-974", "paṭilabhati"),
    (r"taṇh", "တပ်မက်မှု", "2", "^2-834", "tisso taṇhā"),
    (r"parijān", "ပိုင်းခြား", "5", "^5-317", "parijānaṃ"),
    (r"pajah", "ပယ်", "5", "^5-317", "pajahaṃ"),
    (r"pariññā", "ပိုင်းခြား သိ", "5", "^5-317", "parijānaṃ"),
    (r"uppādakkhaṇe", "ဖြစ်ခြင်း ခဏ၌", "5", "^5-366", "Uppādakkhaṇe"),
    (r"bhaṅgakkhaṇe", "ပြိုပျက်ခြင်း ခဏ၌", "5", "^5-366", "bhaṅgakkhaṇe"),
    (r"citte vattamāne", "စိတ် ဖြစ်နေစဉ်", "5", "^5-556", "citte vattamāne"),
    (r"anantarā", "ချက်ချင်း နောက်၌", "2", "^2-751", "samanantarā"),
    (r"abhisametāv", "ထင်ထင်ရှားရှား", "5", "^5-431", "abhisametu"),
    (r"[Aa]pāy", "အပါယ်", "5", "^5-317", "Catūhapāyehi"),
    (r"[Dd]ibbacakkhu", "နတ်မျက်စိ", "5", "^5-374", "dibbacakkhuṃ"),
    (r"paññācakkhu", "ပညာမျက်စိ", "5", "^5-374", "paññācakkhu"),
    (r"[Dd]ibbasot", "နတ်နား", "5", "^5-375", "dibbasotaṃ"),
    (r"pucchā", "အမေး", "5", "^5-652", "pucchā"),
    (r"(?<![\w])(?:[Cc]akkhu)(?:ṃ|ñca|ūti| ceva)?(?![\w])", "မျက်စိ", "2", "^2-183", "cakkhudhātu"),
]
# the 18 dhātu names (pi-2 ^2-183) and the khandha names are tested in C1 below as well
REUSE += [(rf"\b{k[:-1]}(?:u|uṃ|ū|uñca)(?![\w])", v, "2", "^2-183", k) for k, v in MS.DH.items()]
# documented exceptions (not counted as identical; see notes-sample.md «Departures from pi-1 … pi-5»)
EXCEPT = [
    (r"kusalahetū|nāmahetū", "pi-1 ^1-1059 kusalahetu «ကုသိုလ် အမြစ်» (hetu = root)", "«ကုသိုလ်၏ အကြောင်း» (hetu = cause, "
     "kept apart from mūla «အမြစ်» in the Yamaka synonym list)"),
    (r"anuloma|paccanīka", "pi-5 «အစဉ်အတိုင်း» / «ပြောင်းပြန်» (debate order)", "«အဟုတ်ပြ ပုံစံ» / «အငြင်းပြ ပုံစံ» "
     "(affirmative / negated form of a question: another sense)"),
    (r"\bcavant", "pi-2 termbase cavati «သေသည်»", "pi-5 termbase and pi-2 ^2-1029 «စုတေ» used"),
    (r"\bNatthi\.", "pi-3 ^3-410 Natthi «မရှိ။»", "«မရှိပါ။» (explained: answer register, as Āmantā «ဟုတ်ပါသည်။» "
     "and pi-5 ^5-355 Natthi «မရှိပါ။»; coordinator 2026-11-22)"),
    (r"[Dd]ibbasotaṃ taṇhāsotaṃ", "bare sotaṃ «နား» (pi-2 ^2-183)", "«“သောတ”» in these two sentences (the ear / stream "
     "word play; see notes)"),
    (r"uppādakkhaṇe", "pi-6 uppāda «ဖြစ်ပေါ်ခြင်း» (headings, sample)", "pi-5 ^5-366 uppādakkhaṇe «ဖြစ်ခြင်း ခဏ၌» "
     "(identical Pāli word; counted in C3 as identical with pi-5)"),
    (r"(?<![\w])dukkh(?:aṃ|añca|anti)(?![\w])", "pi-5 termbase dukkhaṃ «ဒုက္ခ» (truth sense)", "pi-1 ^1-559 "
     "«နာကျင်မှု» (painful feeling: what kāyika / cetasika dukkha names; counted in C3 as identical with pi-1)"),
]
n_c3 = s_c3 = 0
for rx, my, bk, bid, wit in REUSE:
    pl, ml = FIN[bk][bid]
    if wit.lower() not in " ".join(pl).lower() or my not in " ".join(ml):
        bad.append(f"C3 witness pi-{bk} {bid}: «{wit}» / «{my}»")
        continue
    for name, (P, M) in PAIRS.items():
        for i, (p, m) in enumerate(zip(P, M), 1):
            if re.search(rx, nobr(body(p)), re.I):
                n_c3 += 1
                if my in m:
                    s_c3 += 1
                else:
                    bad.append(f"C3 {name}:{i} «{rx}» -> «{my}» missing")
n_ex = 0
for rx, fin, ours in EXCEPT:
    k = sum(1 for P, M in PAIRS.values() for p in P if re.search(rx, nobr(body(p)), re.I))
    n_ex += k
total_n, total_s = n_c1 + n_c2 + n_c3, s_c1 + s_c2 + s_c3
print(f"C. reuse test: {total_s} / {total_n} identical (C1 khandha names and bare terms {s_c1}/{n_c1}, C2 whole lines "
      f"and answers {s_c2}/{n_c2}, C3 {len(REUSE)} reused terms {s_c3}/{n_c3} line occurrences)")
print(f"   documented exceptions / notes: {len(EXCEPT)} terms on {n_ex} lines")
for rx, fin, ours in EXCEPT:
    print(f"   - {rx}: final {fin}; sample {ours}")

print(f"\nmismatches: {len(bad)}")
for b in bad[:60]:
    print("  ", b)
sys.exit(1 if bad else 0)
