"""Check of the pi-3 Burmese zero-shot sample (preamble, 1-uddeso, 2-pathamanayo) against the Pāli.

usage: python3 -I -X utf8 check_sample.py
  A. regeneration: my3_formulas.translate_line() on every Pāli line gives exactly the written file.
  B. per line (2-pathamanayo): the saṅgahita / asaṅgahita polarity of every verb (questions too), the verb number
     (-o / -aṃ singular, -āni plural, -ā by the subject), every count of every answer (kind and number, in order,
     with the polarity of its verb; «na kehici / na kāhici» = 0), the questions, «asaṅkhataṃ khandhato ṭhapetvā»,
     the colophons; uddeso: the item numbers and the mātikā items against the tables.
     The Pāli side is parsed here with its own number words and patterns (not those of my3_formulas).
  C. reuse test: every topic name / mātikā term used, every heading and colophon, and every whole Pāli line of the
     sample that also occurs in pi-1 or pi-2 has exactly their FINAL (rails) Burmese. The occurrences are searched
     here independently in the pi-1 / pi-2 Pāli (list lines «Head – a, b», «Katame dhammā X?», «Tattha katamo X?»,
     Mātikā lines «(Ka) X dhammā.», headings, whole lines); a term found only by its recorded witness segment is
     checked there. Prints n / n identical.
Exit 1 on any mismatch.
"""
import pathlib
import re
import sys
import unicodedata

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import my3_formulas as F  # noqa: E402

ROOT = HERE.parents[3]
PALI = ROOT / "AI_translation/pali/pi-3_split_chapters"
OUT = ROOT / "AI_translation/burmese/pi-3-burmese-plain-zeroshot_split_chapters"
NAMES = ["preamble.md", "1-uddeso.md", "2-pathamanayo.md"]
bad = []


def lines(p):
    return [l for l in unicodedata.normalize("NFC", p.read_text(encoding="utf-8-sig")).splitlines() if l.strip()]


def body(l):
    return F.ID_RE.sub("", l).strip()


# ===================================================================================== A. regeneration
for name in NAMES:
    raw = (PALI / name).read_text(encoding="utf-8-sig").splitlines()
    bid_of, cur = {}, []
    for i, l in enumerate(raw):
        if l.strip():
            cur.append(i)
            m = F.ID_RE.search(l)
            if m:
                for j in cur:
                    bid_of[j] = m.group(1)
                cur = []
    regen = "\n".join(F.translate_line(l, bid_of.get(i)) for i, l in enumerate(raw)).rstrip("\n") + "\n"
    if unicodedata.normalize("NFC", regen) != (OUT / name).read_text(encoding="utf-8"):
        bad.append(f"A {name}: file differs from the regenerated text")
print(f"A. regeneration: {len(NAMES) - sum(1 for b in bad if b.startswith('A '))} / {len(NAMES)} files identical")

# ===================================================================================== B. per line
PN = {"ek": 1, "dv": 2, "t": 3, "cat": 4, "pañc": 5, "ch": 6, "satt": 7, "aṭṭh": 8, "nav": 9, "das": 10,
      "ekādas": 11, "dvādas": 12, "teras": 13, "cuddas": 14, "pannaras": 15, "soḷas": 16, "sattaras": 17,
      "aṭṭhāras": 18}
# instrumental stems as they stand before «-hi» / «-ena» / «-āya» (dvīhi, tīhi, catūhi: long vowel)
STEM = {"eken": "ek", "ekāy": "ek", "dvīh": "dv", "tīh": "t", "catūh": "cat"}
for k in ("pañc", "ch", "satt", "aṭṭh", "nav", "das", "ekādas", "dvādas", "teras", "cuddas", "pannaras", "soḷas",
          "sattaras", "aṭṭhāras"):
    STEM[k + "ah"] = k
_ST = "|".join(sorted(STEM, key=len, reverse=True))
P_TOK = re.compile(
    rf"(?<![\w])(?:(?P<k>{_ST})(?:a|i) khandhe(?:na|hi)"
    rf"|(?P<a>{_ST}|dvādas)āyatane(?:na|hi)"
    rf"|(?P<d>ekāy)a dhātuyā|(?P<d2>{_ST})i dhātūhi"
    rf"|na (?:kehici|kāhici) (?P<z>khandhehi|āyatanehi|dhātūhi))(?![\w])", re.IGNORECASE)
P_VERB = re.compile(r"(?<![\w])(?P<neg>a?)saṅgahit(?P<e>o|aṃ|ā|āni)(?![\w])", re.IGNORECASE)
P_Q1 = "katihi khandhehi katihāyatanehi katihi dhātūhi"
P_PL = re.compile(r"dhammā|(?<![\w])ca(?![\w])|ñca(?![\w])|saṅkhārā|khandhā|dhātuyo|āyatanāni|saccāni|indriyāni")
P_FSG = re.compile(r"(?:dhātu|avijjā|vedanā|taṇhā|jāti|jarā|appamaññā)$", re.IGNORECASE)

MY_NUM = {v: k for k, v in F.NUM_MY.items()}
KMY = {"အစုအဝေး": "k", "အာရုံခံ နယ်ပယ်": "a", "ဓာတ်": "d"}
_KN = "အစုအဝေး|အာရုံခံ နယ်ပယ်|ဓာတ်"
B_TOK = re.compile(rf"(?P<kind>{_KN}) (?P<n>[က-႟]+?)ပါး(?=၊|တို့တွင်|တွင်|…)")
B_ZERO = re.compile(rf"အကျုံး(?P<neg>မ)?ဝင်ရာ (?P<ks>(?:(?:{_KN})(?:၊ )?)+) မရှိ")
B_VERB = re.compile(r"အကျုံး(?P<neg>မ)?ဝင်(?!ရာ|သော)(?P<pl>ကြ)?")      # «…ဝင်သော» = inside a term (pariyāpanna)


def pali_counts(p):
    verbs = [(m.start(), m["neg"] == "") for m in P_VERB.finditer(p)]
    out = []
    for m in P_TOK.finditer(p):
        if m["z"]:
            kind, n = {"khandhehi": "k", "āyatanehi": "a", "dhātūhi": "d"}[m["z"]], 0
        else:
            kind = "k" if m["k"] else "a" if m["a"] else "d"
            st = m["k"] or m["a"] or m["d"] or m["d2"]
            n = 12 if st.lower() == "dvādas" else PN[STEM[st.lower()]]
        pol = next((pv for pos, pv in verbs if pos > m.start()), None)
        out.append((kind, n, pol))
    return out


def burmese_counts(b):
    verbs = [(m.start(), m["neg"] is None) for m in B_VERB.finditer(b)]
    out = []
    for m in B_TOK.finditer(b):
        pol = next((pv for pos, pv in verbs if pos > m.start()), None)
        out.append((m.start(), KMY[m["kind"]], MY_NUM.get(m["n"], -1), pol))
    for m in B_ZERO.finditer(b):
        for i, k in enumerate(m["ks"].split("၊ ")):
            out.append((m.start() + i, KMY[k], 0, m["neg"] is None))
    return [x[1:] for x in sorted(out)]


def pali_numbers(p):
    """Expected Burmese plurality of each verb: by its ending, «-ā» by the nearest subject text before it."""
    res = []
    for m in P_VERB.finditer(p):
        e = m["e"]
        if e in ("o", "aṃ"):
            res.append(False)
        elif e == "āni":
            res.append(True)
        else:
            before = p[:m.start()]
            chunk = re.split(r"…pe…|…|\?|\.", before)
            subj = ""
            for c in reversed(chunk):          # the nearest chunk that holds a subject (not only counts / question)
                c2 = re.sub(P_TOK, "", c)
                c2 = c2.replace(P_Q1, "").replace("asaṅkhataṃ khandhato ṭhapetvā", "")
                c2 = P_VERB.sub("", re.sub(r"(?i)katihi", "", c2)).strip(" ,")
                if c2:
                    subj = c2
                    break
            subj = re.sub(r" ?\[[^\]]*\]", "", subj)
            res.append(bool(P_PL.search(subj)) or not P_FSG.search(subj))
    return res


nlines = ncounts = nverbs = 0
pa, bu = lines(PALI / "2-pathamanayo.md"), lines(OUT / "2-pathamanayo.md")
for i, (p, b) in enumerate(zip(pa, bu)):
    pb, bb = body(p), body(b)
    if pb.startswith("#"):
        if not bb.startswith(pb.split()[0] + " "):
            bad.append(f"B line {i + 1}: heading level")
        continue
    m = re.fullmatch(r"\((?P<t>[^()]+)\.\)", pb)
    if m:
        if bb != f"({F.COLO[m['t']]}။)":
            bad.append(f"B line {i + 1}: colophon")
        continue
    if pb.endswith("padaniddeso paṭhamo."):
        continue
    nlines += 1
    # sentences: Pāli at «? » / «. » before a capital (brackets protected), Burmese at «။ »
    prot = re.sub(r"\[[^\]]*\]", lambda m: "⟦" + "x" * len(m[0]) + "⟧", pb)
    cuts = [m.end() for m in re.finditer(r"(?<=[?.]) (?=[A-ZĀĪŪṬḌṆÑ])", prot)]
    psent = [pb[a:b].strip() for a, b in zip([0] + cuts, cuts + [len(pb)])]
    bsent = [x for x in re.split(r"(?<=။) ", bb)]
    pnum = pali_numbers(pb)
    if len(psent) != len(bsent):
        bad.append(f"B line {i + 1}: {len(psent)} Pāli sentences vs {len(bsent)} Burmese")
    else:
        vi = 0
        for ps, bs in zip(psent, bsent):
            pv = [m["neg"] == "" for m in P_VERB.finditer(ps)]
            if len(pv) != 1:
                bad.append(f"B line {i + 1}: {len(pv)} Pāli verbs in «{ps[:50]}»")
                continue
            forms = [(m["neg"] is None, bool(m["pl"]), bs[m.end():m.end() + 2] == "ရာ")
                     for m in re.finditer(r"အကျုံး(?P<neg>မ)?ဝင်(?!သော)(?P<pl>ကြ)?", bs)]
            if not forms or any(f[0] != pv[0] for f in forms):
                bad.append(f"B line {i + 1}: polarity «{ps[:40]}» {pv[0]} vs {[f[0] for f in forms]}")
            main = [f for f in forms if not f[2]]
            if main and main[-1][1] != pnum[vi]:
                bad.append(f"B line {i + 1}: number «{ps[:40]}» plural={pnum[vi]}")
            if not main and not bs.endswith(f"{F.ZERO_TAIL}။"):
                bad.append(f"B line {i + 1}: no verb in «{bs[:40]}»")
            vi += 1
            nverbs += 1
    pc, bc = pali_counts(pb), burmese_counts(bb)
    if pc != bc:
        bad.append(f"B line {i + 1}: counts\n   pi {pc}\n   my {bc}")
    ncounts += len(pc)
    if pb.count(P_Q1) != bb.count(F.Q1_MY):
        bad.append(f"B line {i + 1}: question 1")
    if len(re.findall(r"Katihi asaṅgahit", pb)) != bb.count("မည်မျှတို့တွင် အကျုံးမဝင်"):
        bad.append(f"B line {i + 1}: question 2")
    if pb.count("asaṅkhataṃ khandhato ṭhapetvā") != bb.count(F.THAPETVA):
        bad.append(f"B line {i + 1}: ṭhapetvā")
    if "?" in bb or "।" in bb:
        bad.append(f"B line {i + 1}: «?» / «।»")

# uddeso: item numbers and items
pu, uu = lines(PALI / "1-uddeso.md"), lines(OUT / "1-uddeso.md")
for p, b in zip(pu, uu):
    pn, bn = re.findall(r"\((\d+)\)", p), re.findall(r"\((\d+)\)", b)
    if pn != bn:
        bad.append(f"B uddeso: item numbers {pn} vs {bn}")
    if pn and "^3-1" in p and not p.endswith("^3-1-1-0"):
        its = [x.strip().rstrip(".") for x in re.split(r"\(\d+\)", body(p))[1:]]
        mys = [x.strip().rstrip("။") for x in re.split(r"\(\d+\)", body(b))[1:]]
        for x, y in zip(its, mys):
            exp = F.naya_item_my(x) if p.endswith("^3-1") else (
                "၊ ".join(F.SUBJ[w.lower()][0] for w in x.split()) if x.lower().startswith("phasso") else
                F.SUBJ[x[0].lower() + x[1:]][0])
            if y != exp:
                bad.append(f"B uddeso: item «{x}» = «{y}», table «{exp}»")
print(f"B. per line: {nlines} content lines, {nverbs} verbs, {ncounts} counts; "
      f"{sum(1 for x in bad if x.startswith('B'))} mismatches")

# ===================================================================================== C. reuse test (pi-1 / pi-2)
FIN = F.FINAL
nov = lambda s: re.sub(r" ?\[[^\]]*\]", "", s)
norm = lambda s: s.replace("ṇṇ", "nn")
low = lambda s: s[0].lower() + s[1:] if s else s

# independent indexes of the pi-1 / pi-2 Pāli: list items, questions, Mātikā lines, headings, whole lines
occ = {}         # Pāli term -> set of final Burmese at its occurrences


def add(k, v, where):
    occ.setdefault(norm(low(k.strip())), {}).setdefault(v.strip(), where)


heads, whole = {}, {}
for book in ("1", "2"):
    for bid, f, p, b in FIN.lines(book):
        pp, bb = nov(F.ID_RE.sub("", p)).strip(), nov(F.ID_RE.sub("", b)).strip()
        whole.setdefault(pp, {}).setdefault(bb, bid)
        h = re.fullmatch(r"#+ (.+)", pp)
        if h:
            heads.setdefault(h[1], {}).setdefault(re.sub(r"^#+ ", "", bb), bid)
            continue
        c = re.fullmatch(r"([A-ZĀĪŪ][^ .]+)\.", pp)
        if c:
            heads.setdefault(c[1], {}).setdefault(bb.rstrip("။"), bid)
        if " – " in pp and " – " in bb and pp.count(" – ") == 1 and bb.count(" – ") == 1:
            ph, pl = pp.split(" – ")
            bh, bl = bb.split(" – ")
            pi = [x.strip() for x in pl.rstrip(".").split(",")]
            my = [x.strip() for x in bl.rstrip("။").split("၊")]
            if len(pi) == len(my) and "?" not in ph:
                for x, y in zip(pi, my):
                    add(x, y, bid)
                hh = ph.split(", ")[-1] if "?" not in ph else None
                if hh and "၊" not in bh:
                    add(hh, bh, bid)
        for m in re.finditer(r"Katame dhammā ([^?]+)\?", pp):
            mb = re.match(r"(.+?) ဟူသည် အဘယ်တို့နည်း။", bb)
            if m.start() == 0 and mb:
                add(m[1] + " dhammā", mb[1], bid)
        m = re.match(r"Tattha katam(?:o|ā|aṃ|e|āni) ([^?]+)\?", pp)
        mb = re.match(r"ထိုတို့အနက် (.+?) ဟူသည် အဘယ်(?:တို့)?နည်း။", bb)
        if m and mb:
            add(m[1], mb[1], bid)
        m = re.fullmatch(r"\((?:Ka|Kha|Ga)\) (.+ dhammā)\.", pp)
        if m and f == "1-matika.md":
            add(m[1], re.sub(r"^\(\S+\) ", "", bb).rstrip("။"), bid)

terms = sorted(F.USED)
n_found = n_same = 0
rep = []
for k in terms:
    v = F.SUBJ[k][0]
    kk = norm(F.TERM_ALIAS.get(k.removesuffix(" dhammā"), k.removesuffix(" dhammā")) +
              ("" if k in F.NO_DHAMMA else " dhammā")) if k.endswith(" dhammā") or k in F.NO_DHAMMA else norm(k)
    if k in F.NO_DHAMMA:
        kk = norm(k) + " dhammā"
    got = occ.get(kk) or occ.get(norm(k))
    if got:
        n_found += 1
        if v in got:
            n_same += 1
            others = [x for x in got if x != v]
            if others:
                rep.append(f"   info {k}: also «{others[0]}» at {got[others[0]]} (other sense)")
        else:
            bad.append(f"C term {k}: «{v}» but pi-1 / pi-2 have {dict(list(got.items())[:2])}")
        continue
    w = F.WITNESS.get(k)
    if w:
        n_found += 1
        f, p, b = FIN.seg(*w)
        if v in " ".join(b):
            n_same += 1
        else:
            bad.append(f"C term {k}: «{v}» not in its witness {w}")
    else:
        rep.append(f"   new {k} = {v}")
print(f"C. reuse test, topic names / mātikā terms: {n_same} / {n_found} identical with pi-1 / pi-2 final "
      f"({len(terms)} used, {len(terms) - n_found} not in pi-1 / pi-2)")

# headings, colophons and whole lines of the sample that pi-1 / pi-2 also have
n_h = s_h = 0
for name in NAMES:
    for p, b in zip(lines(PALI / name), lines(OUT / name)):
        pp, bb = body(p), body(b)
        h = re.fullmatch(r"#+ (.+)", pp)
        c = re.fullmatch(r"\(([^()]+)\.\)", pp)
        key = h[1] if h else c[1] if c else None
        mine = re.sub(r"^#+ ", "", bb) if h else bb[1:-2] if c else None
        if key and key in heads:
            n_h += 1
            if mine in heads[key]:
                s_h += 1
            else:
                bad.append(f"C heading {key}: «{mine}» vs {heads[key]}")
        elif nov(pp) in whole:
            n_h += 1
            if nov(bb) in whole[nov(pp)]:
                s_h += 1
            else:
                bad.append(f"C line {pp[:40]}: «{bb[:40]}» vs {list(whole[nov(pp)])[:1]}")
print(f"C. reuse test, headings / colophons / whole lines: {s_h} / {n_h} identical")
print("\n".join(rep[:60]))
if bad:
    print(f"\n{len(bad)} MISMATCHES")
    print("\n".join(bad[:40]))
    sys.exit(1)
print(f"\nOK: 0 mismatches; reuse {n_same + s_h} / {n_found + n_h} identical")
