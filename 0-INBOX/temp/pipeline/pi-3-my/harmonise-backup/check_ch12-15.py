"""Check of the pi-3 Burmese zero-shot, chapters 12-15 (methods 11-14), against the Pāli (adapted from check_sample.py).

usage: python3 -I -X utf8 check_ch12-15.py
  A. regeneration: make_ch12-15.py (its frames on my3_formulas) on every Pāli line gives exactly the written file.
  B. per line, the Pāli parsed here with its own patterns (not those of the generator):
     * chain sentences «X-ena ye dhammā… Y-ena ye dhammā REL, te dhammā …»: number of items, the relation of the
       relative clause (saṅgahitā / asaṅgahitā by the three saṅgahas, sampayuttā, vippayuttā) and its polarity;
     * every verb of the questions and answers in order: kind (saṅgaha / sampayoga), polarity, question or statement,
       «kehici» (partly); every Burmese verb plural («ကြ», the subject is always ye / te dhammā);
     * every count of every answer (kind and number, in order, with the kind / polarity of its verb and its
       «kehici»; «na kehici / na kāhici» = 0);
     * «Natthi», «asaṅkhataṃ khandhato ṭhapetvā», the two question frames;
     * headings (#-level), colophons, verse lines (the numbers in each line).
  C. reuse test: every topic name / mātikā term used, every heading, colophon and whole line that also occurs in
     pi-1 or pi-2 has exactly their FINAL (rails) Burmese (searched independently, as check_sample.py). Prints n / n.
Exit 1 on any mismatch.
"""
import importlib.util
import pathlib
import re
import sys
import unicodedata

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
_spec = importlib.util.spec_from_file_location("make_ch12_15", HERE / "make_ch12-15.py")
M = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(M)
F = M.F

ROOT = HERE.parents[3]
PALI = ROOT / "AI_translation/pali/pi-3_split_chapters"
OUT = ROOT / "AI_translation/burmese/pi-3-burmese-plain-zeroshot_split_chapters"
NAMES = M.NAMES_OUT
bad = []


def lines(p):
    return [l for l in unicodedata.normalize("NFC", p.read_text(encoding="utf-8-sig")).splitlines() if l.strip()]


def body(l):
    return F.ID_RE.sub("", l).strip()


# ===================================================================================== A. regeneration
for name in NAMES:
    regen = "\n".join(M.render(name)).rstrip("\n") + "\n"
    if unicodedata.normalize("NFC", regen) != (OUT / name).read_text(encoding="utf-8"):
        bad.append(f"A {name}: file differs from the regenerated text")
print(f"A. regeneration: {len(NAMES) - sum(1 for b in bad if b.startswith('A '))} / {len(NAMES)} files identical")

# ===================================================================================== B. per line
PN = {"ek": 1, "dv": 2, "t": 3, "cat": 4, "pañc": 5, "ch": 6, "satt": 7, "aṭṭh": 8, "nav": 9, "das": 10,
      "ekādas": 11, "dvādas": 12, "teras": 13, "cuddas": 14, "pannaras": 15, "soḷas": 16, "sattaras": 17,
      "aṭṭhāras": 18}
STEM = {"eken": "ek", "ekāy": "ek", "dvīh": "dv", "tīh": "t", "catūh": "cat"}
for k in ("pañc", "ch", "satt", "aṭṭh", "nav", "das", "ekādas", "dvādas", "teras", "cuddas", "pannaras", "soḷas",
          "sattaras", "aṭṭhāras"):
    STEM[k + "ah"] = k
_ST = "|".join(sorted(STEM, key=len, reverse=True))
P_TOK = re.compile(
    rf"(?<![\w])(?:(?P<k>{_ST})(?:a|i) khandhe(?:na|hi)"
    rf"|(?P<a>{_ST})āyatane(?:na|hi)"
    rf"|(?P<d>ekāy)a dhātuyā|(?P<d2>{_ST})i dhātūhi"
    rf"|na (?:kehici|kāhici) (?P<z>khandhehi|āyatanehi|dhātūhi))(?![\w])", re.IGNORECASE)
# a verb of a question / answer: (kehici)? verb (ti)? and its end mark
P_VERB = re.compile(r"(?<![\w])(?P<keh>kehici )?(?P<v>asaṅgahitā|saṅgahitā|sampayuttā|vippayuttā)(?:ti)?(?P<e>[?.;])")
P_VK = {"saṅgahitā": ("inc", True), "asaṅgahitā": ("inc", False), "sampayuttā": ("ass", True),
        "vippayuttā": ("ass", False)}
P_Q1 = "katihi khandhehi katihāyatanehi katihi dhātūhi"
P_REL = re.compile(r" ye(?: dhammā)? (?:khandhasaṅgahena (a?)saṅgahitā āyatanasaṅgahena (a?)saṅgahitā "
                   r"dhātusaṅg(?:ah)?ena (a?)saṅgahitā|(sampayuttā|vippayuttā))(?:…pe…|…)?,? te dhammā ")

MY_NUM = {v: k for k, v in M.NUM_MY.items()}
KMY = {"အစုအဝေး": "k", "အာရုံခံ နယ်ပယ်": "a", "ဓာတ်": "d"}
_KN = "အစုအဝေး|အာရုံခံ နယ်ပယ်|ဓာတ်"
B_TOK = re.compile(rf"(?P<kind>{_KN}) (?P<n>[က-႟]+?)ပါး(?=၊|တို့|တွင်|နှင့်|၏)")
B_ZERO = re.compile(rf"အကျုံး(?P<neg>မ)?ဝင်ရာ (?P<ks>(?:(?:{_KN})(?:၊ )?)+) မရှိ")
B_VERB = re.compile(r"(?P<keh>အချို့နှင့် )?(?:(?P<ass>ယှဉ်တွဲ|ကင်းကွာ)(?P<pl1>ကြ)?(?P<q1>သနည်း|သည်)"
                    r"|အကျုံး(?P<neg>မ)?ဝင်(?!ရာ|သော|ခြင်း)(?P<pl2>ကြ)?(?P<q2>သနည်း|သည်)?)")
B_REL = re.compile(r"နှင့် (?:အစုအဝေး အကျုံးဝင်ခြင်းဖြင့် အကျုံး(မ?)ဝင်၊ အာရုံခံ နယ်ပယ် အကျုံးဝင်ခြင်းဖြင့် "
                   r"အကျုံး(မ?)ဝင်၊ ဓာတ် အကျုံးဝင်ခြင်းဖြင့် အကျုံး(မ?)ဝင်|(ယှဉ်တွဲ|ကင်းကွာ))သော သဘောတရားများ"
                   r"(?:…၊ |… |၊ )ထိုသဘောတရားများသည် ")


def pali_verbs(p):
    """[(kind, positive, question, kehici)] of the questions / answers, and the counts [(k, n, kind, pos, keh)]."""
    vs = [(m.start(), P_VK[m["v"]] + (m["e"] == "?", bool(m["keh"]))) for m in P_VERB.finditer(p)]
    cs = []
    for m in P_TOK.finditer(p):
        if m["z"]:
            kind, n = {"khandhehi": "k", "āyatanehi": "a", "dhātūhi": "d"}[m["z"]], 0
        else:
            kind = "k" if m["k"] else "a" if m["a"] else "d"
            st = m["k"] or m["a"] or m["d"] or m["d2"]
            n = PN[STEM[st.lower()]]
        v = next((x for pos, x in vs if pos > m.start()), None)
        cs.append((kind, n) + ((v[0], v[1], v[3]) if v else (None,) * 3))
    return [v for _, v in vs], cs


def burmese_verbs(b):
    vs = []
    for m in B_VERB.finditer(b):
        if m["ass"]:
            v = ("ass", m["ass"] == "ယှဉ်တွဲ", m["q1"] == "သနည်း", bool(m["keh"]), bool(m["pl1"]))
        else:
            v = ("inc", m["neg"] is None, m["q2"] == "သနည်း", bool(m["keh"]), bool(m["pl2"]))
        vs.append((m.start(), v))
    for m in B_ZERO.finditer(b):        # an all-zero answer «အကျုံး(မ)ဝင်ရာ … မရှိ။» is its own (plural) verb
        if b[m.end():] == "။":
            vs.append((m.start(), ("inc", m["neg"] is None, False, False, True)))
    vs.sort()
    cs = []
    for m in B_TOK.finditer(b):
        v = next((x for pos, x in vs if pos > m.start()), None)
        cs.append((m.start(), KMY[m["kind"]], MY_NUM.get(m["n"], -1)) + ((v[0], v[1], v[3]) if v else (None,) * 3))
    for m in B_ZERO.finditer(b):
        for i, k in enumerate(m["ks"].split("၊ ")):
            cs.append((m.start() + i, KMY[k], 0, "inc", m["neg"] is None, False))
    return [v for _, v in vs], [x[1:] for x in sorted(cs)]


VERSE_NUM = {"dve": 2, "pannarasindriyā": 15, "ekādasa": 11, "tiṃsavidhāti": 30, "cattāro": 4, "satta": 7,
             "cuddasindriyā": 14, "dvādasa": 12, "soḷasa": 16, "aṭṭha": 8, "tecattālīsameva": 43, "cha": 6,
             "dasa": 10, "cuddasa": 14, "sattacattālīsa": 47, "navamassa": 9,
             "saḷāyatanaṃ": 6}       # saḷ- = six (the Burmese names the six bases)
nlines = nverbs = ncounts = nchains = nverse = 0
for name in NAMES:
    pa, bu = lines(PALI / name), lines(OUT / name)
    if len(pa) != len(bu):
        bad.append(f"B {name}: line count")
        continue
    for i, (p, b) in enumerate(zip(pa, bu)):
        pb, bb = body(p), body(b)
        where = f"B {name} line {i + 1}"
        if pb.startswith("#"):
            if not bb.startswith(pb.split()[0] + " "):
                bad.append(f"{where}: heading level")
            continue
        m = re.fullmatch(r"(\S+padaniddeso) (\S+)\.", pb)
        if m:
            exp = f"{F.ORD[F.ORD_COLO[m[2]]]} {F.NIDDESO[m[1]]}။"
            if bb != exp:
                bad.append(f"{where}: colophon")
            continue
        if pb == "Dhātukathāpakaraṇaṃ niṭṭhitaṃ.":
            if bb != f"“{F.TITLE}” ကျမ်း ပြီးဆုံးပြီ။":
                bad.append(f"{where}: book colophon")
            continue
        if pb in M.VERSES:
            nverse += 1
            pn = [VERSE_NUM[w.strip(",;.").lower()] for w in pb.split() if w.strip(",;.").lower() in VERSE_NUM]
            bn = [MY_NUM.get(x, -1) for x in re.findall(r"(?:^| )([က-႟]+?)(?:ပါး|မျိုး(?!တွဲ))", bb)]
            bn += [9] * bb.count("နဝမ ")
            if sorted(pn) != sorted(bn):
                bad.append(f"{where}: verse numbers {pn} vs {bn}")
            if any(c in bb for c in "?;"):
                bad.append(f"{where}: verse marks")
            continue
        nlines += 1
        # sentences: Pāli at «? » / «. » before a capital, Burmese at «။ »
        cuts = [mm.end() for mm in re.finditer(r"(?<=[?.]) (?=[A-ZĀĪŪṬḌṆÑ])", pb)]
        psent = [pb[x:y].strip() for x, y in zip([0] + cuts, cuts + [len(pb)])]
        bsent = re.split(r"(?<=။) ", bb)
        if len(psent) != len(bsent):
            bad.append(f"{where}: {len(psent)} Pāli sentences vs {len(bsent)} Burmese")
            continue
        for ps, bs in zip(psent, bsent):
            pr = P_REL.search(ps)
            if " ye " in ps:
                nchains += 1
                br = B_REL.search(bs)
                if not pr or not br:
                    bad.append(f"{where}: chain frame «{ps[:50]}»")
                    continue
                prel = ("inc", [x == "" for x in pr.groups()[:3]]) if pr[4] is None else ("ass", [pr[4] == "sampayuttā"])
                brel = ("inc", [x == "" for x in br.groups()[:3]]) if br[4] is None else ("ass", [br[4] == "ယှဉ်တွဲ"])
                if prel != brel:
                    bad.append(f"{where}: relative clause {prel} vs {brel}")
                n_pi = len(re.findall(r"(?<![\w])ye(?![\w])", ps))
                n_my = bs[:br.start()].count("နှင့်… ") + 1
                if n_pi != n_my:
                    bad.append(f"{where}: {n_pi} items vs {n_my}")
                ps, bs = ps[pr.end():], bs[br.end():]
            if ps == "Natthi." or ps == "Natthi?":
                if bs != "မရှိ။":
                    bad.append(f"{where}: natthi")
                continue
            pv, pc = pali_verbs(ps)
            bv, bc = burmese_verbs(bs)
            if [x[:4] for x in bv] != pv:
                bad.append(f"{where}: verbs\n   pi {pv}\n   my {[x[:4] for x in bv]}")
            if not all(x[4] for x in bv):
                bad.append(f"{where}: singular verb in «{bs[:40]}»")
            if pc != bc:
                bad.append(f"{where}: counts\n   pi {pc}\n   my {bc}")
            nverbs += len(pv)
            ncounts += len(pc)
            if ps.count(P_Q1) != bs.count(F.Q1_MY) + bs.count(M.Q_ASSOC):
                bad.append(f"{where}: question frame")
            if ps.count("asaṅkhataṃ khandhato ṭhapetvā") != bs.count(F.THAPETVA):
                bad.append(f"{where}: ṭhapetvā")
            if re.fullmatch(r"Katihi \S+\?", ps) and not re.fullmatch(r"မည်မျှတို့(?:တွင်|နှင့်) \S+။", bs):
                bad.append(f"{where}: katihi")
        if "?" in bb or "।" in bb or ";" in bb:
            bad.append(f"{where}: «?» / «।» / «;»")
print(f"B. per line: {nlines} content lines, {nchains} chains, {nverbs} verbs, {ncounts} counts, {nverse} verse lines; "
      f"{sum(1 for x in bad if x.startswith('B'))} mismatches")

# ===================================================================================== C. reuse test (pi-1 / pi-2)
FIN = F.FINAL
nov = lambda s: re.sub(r" ?\[[^\]]*\]", "", s)
norm = lambda s: s.replace("ṇṇ", "nn")
low = lambda s: s[0].lower() + s[1:] if s else s
occ = {}


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
# verse lines and the book colophon: the pi-1 / pi-2 names they reuse (heads read through F.heads in the generator)
for key, mine in (("Mahantaradukaṃ", M.MAHANTARA), ("Piṭṭhidukaṃ", M.PITTHI)):
    n_h += 1
    s_h += mine in heads.get(key, {})
print(f"C. reuse test, headings / colophons / whole lines / verse names: {s_h} / {n_h} identical")
print("\n".join(rep[:60]))
if bad:
    print(f"\n{len(bad)} MISMATCHES")
    print("\n".join(bad[:40]))
    sys.exit(1)
print(f"\nOK: 0 mismatches; reuse {n_same + s_h} / {n_found + n_h} identical")
