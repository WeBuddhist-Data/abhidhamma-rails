"""Check of the pi-3 Burmese zero-shot, chapters 3, 4, 5, 6, 8, 9, against the Pāli (adapted from check_sample.py).

usage: python3 -I -X utf8 check_ch3-6-8-9.py
  A. regeneration: make_ch3-6-8-9.render() (my3_formulas + the in-memory extensions) gives exactly the written files.
  B. per sentence, the Pāli parsed here with its own patterns (not those of the generator):
     * the predicates in order: each «khandhasaṅgahena (a)saṅgahitā āyatana… dhātu…» triple (polarity of each of
       the three) and each «ye dhammā sampayuttā / vippayuttā», against the Burmese predicates
       «… အကျုံးဝင်ခြင်းဖြင့် အကျုံး(မ)ဝင်» ×3 / «ယှဉ်တွဲ / ကင်းကွာသော သဘောတရားများ»;
     * the question: kind (saṅgaha / sampayutta / vippayutta) and polarity, with «တွင်» / «နှင့်»;
     * every count of every answer (kind, number, in order) with the kind and polarity of its verb, «kehici»
       (partly) and «na kehici / na kāhici» = 0;
     * «asaṅkhataṃ khandhato ṭhapetvā», «te dhammā», «tehi dhammehi», «Natthi», the number of chain items and the
       bare items (without «ye dhammā»); the plural «ကြ» of every question / answer verb (subject «te dhammā»);
     * no «?» / «।»; headings keep their level; the colophons; the verses: the number words in order and the
       Roman text of every variant bracket.
  C. reuse test (as check_sample.py): every topic name / mātikā term used, every heading and colophon, and every
     whole Pāli line that also occurs in pi-1 or pi-2 has exactly their FINAL (rails) Burmese. Prints n / n.
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
_spec = importlib.util.spec_from_file_location("make_ch3_6_8_9", HERE / "make_ch3-6-8-9.py")
MK = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(MK)
F = MK.F

ROOT = HERE.parents[3]
PALI = ROOT / "AI_translation/pali/pi-3_split_chapters"
OUT = ROOT / "AI_translation/burmese/pi-3-burmese-plain-zeroshot_split_chapters"
NAMES = MK.NAMES_OUT
bad = []


def lines(p):
    return [l for l in unicodedata.normalize("NFC", p.read_text(encoding="utf-8-sig")).splitlines() if l.strip()]


def body(l):
    return F.ID_RE.sub("", l).strip()


# ===================================================================================== A. regeneration
for name in NAMES:
    if MK.render(name) != (OUT / name).read_text(encoding="utf-8"):
        bad.append(f"A {name}: file differs from the regenerated text")
print(f"A. regeneration: {len(NAMES) - sum(1 for b in bad if b.startswith('A '))} / {len(NAMES)} files identical")

# ===================================================================================== B. per sentence
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
    rf"|(?P<a>{_ST}|dvādas)āyatane(?:na|hi)"
    rf"|(?P<d>ekāy)a dhātuyā|(?P<d2>{_ST})i dhātūhi"
    rf"|na (?:kehici|kāhici) (?P<z>khandhehi|āyatanehi|dhātūhi))(?![\w])", re.IGNORECASE)
P_VERB = re.compile(r"(?<![\w])(?P<v>asaṅgahitā|saṅgahitā|sampayuttā|vippayuttā)(?:ti)?(?![\w])")
P_PRED = re.compile(r"khandhasaṅgahena (a?)saṅgahitā āyatanasaṅgahena (a?)saṅgahitā dhātusaṅgahena (a?)saṅgahitā"
                    r"|(?<=ye dhammā )(sampayuttā|vippayuttā)(?![\w])")
P_Q = re.compile(r"katihi khandhehi katihāyatanehi katihi dhātūhi (asaṅgahitā|saṅgahitā|sampayuttā|vippayuttā)(?:ti)?\?")
VK = {"saṅgahitā": "S+", "asaṅgahitā": "S-", "sampayuttā": "samp", "vippayuttā": "vipp"}

MY_NUM = {v: k for k, v in F.NUM_MY.items()}
KMY = {"အစုအဝေး": "k", "အာရုံခံ နယ်ပယ်": "a", "ဓာတ်": "d"}
_KN = "အစုအဝေး|အာရုံခံ နယ်ပယ်|ဓာတ်"
BV = {"အကျုံးဝင်": "S+", "အကျုံးမဝင်": "S-", "ယှဉ်တွဲ": "samp", "ကင်းကွာ": "vipp"}
_BV = "အကျုံးမဝင်|အကျုံးဝင်|ယှဉ်တွဲ|ကင်းကွာ"
B_TOK = re.compile(rf"(?P<kind>{_KN}) (?P<n>[က-႟]+?)ပါး(?=၊|တို့|တွင်|နှင့်|၏)")
B_ZERO = re.compile(rf"(?P<v>{_BV})ရာ (?P<ks>(?:(?:{_KN})(?:၊ )?)+) မရှိ")
B_AVERB = re.compile(rf"(?:တွင်|နှင့်) (?P<v>{_BV})(?P<pl>ကြ)?(?P<t>သည်|သနည်း|(?=[။၊]))")
B_PRED = re.compile(rf"အစုအဝေး အကျုံးဝင်ခြင်းဖြင့် ({_BV})၊ အာရုံခံ နယ်ပယ် အကျုံးဝင်ခြင်းဖြင့် ({_BV})၊ "
                    rf"ဓာတ် အကျုံးဝင်ခြင်းဖြင့် ({_BV})သော သဘောတရားများ(?=[၊ …]|$)"
                    rf"|(?<=နှင့် )({_BV})သော သဘောတရားများ(?=[၊ …]|$)")
B_Q = re.compile(rf"မည်မျှတို့(တွင်|နှင့်) ({_BV})ကြသနည်း")


def pali_counts(p):
    verbs = [(m.start(), VK[m["v"]]) for m in P_VERB.finditer(p)]
    out = []
    for m in P_TOK.finditer(p):
        if m["z"]:
            kind, n = {"khandhehi": "k", "āyatanehi": "a", "dhātūhi": "d"}[m["z"]], 0
        else:
            kind = "k" if m["k"] else "a" if m["a"] else "d"
            st = m["k"] or m["a"] or m["d"] or m["d2"]
            n = 12 if st.lower() == "dvādas" else PN[STEM[st.lower()]]
        vpos, vk = next(((pos, v) for pos, v in verbs if pos > m.start()), (None, None))
        gap = p[m.end():vpos] if vpos else ""
        part = bool(re.search(r"(?<!na )kehici $", gap))
        out.append((kind, n, vk, part))
    return out


def burmese_counts(b):
    verbs = [(m.start(), BV[m["v"]]) for m in re.finditer(rf"(?P<v>{_BV})(?!သော)", b)]
    out = []
    for m in B_TOK.finditer(b):
        vpos, vk = next(((pos, v) for pos, v in verbs if pos > m.start()), (None, None))
        gap = b[m.end():vpos] if vpos else ""
        out.append((m.start(), KMY[m["kind"]], MY_NUM.get(m["n"], -1), vk, gap.endswith("၏ အချို့နှင့် ")))
    for m in B_ZERO.finditer(b):
        for i, k in enumerate(m["ks"].split("၊ ")):
            out.append((m.start() + i, KMY[k], 0, BV[m["v"]], False))
    return [x[1:] for x in sorted(out)]


def p_sentences(pb):
    prot = re.sub(r"\[[^\]]*\]", lambda m: "⟦" + "x" * (len(m[0]) - 2) + "⟧", pb)
    cuts = [m.end() for m in re.finditer(r"(?<=[?.]) (?=[A-ZĀĪŪṬḌṆÑ])", prot)]
    return [pb[a:b].strip() for a, b in zip([0] + cuts, cuts + [len(pb)])]


ELL = re.compile(r"\s*(?:…pe…|…Pe…|…)\s*")
PNUM = {"ekaṃ": 1, "mekaṃ": 1, "dve": 2, "duve": 2, "dve": 2, "tayo": 3, "tīṇi": 3, "caturo": 4, "cha": 6,
        "satta": 7, "aṭṭha": 8, "dasa": 10, "ekādasa": 11, "cuddasa": 14, "soḷasa": 16, "sattarasa": 17,
        "tiṃsa": 30, "sattacattālīsa": 47}
PNUM_PFX = {"dasāyatanā": 10, "sattindriyā": 7, "pannarasindriyā": 15, "cuddasūpari": 14, "ekavokārabhavo": 1, "saḷāyatanaṃ": 6, "phassapañcamā": 5, "samatiṃsa": 30,
            "tiṃsavidhāti": 30, "dasasvatha": 10, "sattantarā": 7, "dvepi": 2}
nlines = nsent = ncounts = npred = nverse = 0
for name in NAMES:
    pa, bu = lines(PALI / name), lines(OUT / name)
    if len(pa) != len(bu):
        bad.append(f"B {name}: {len(pa)} vs {len(bu)} lines")
        continue
    for i, (p, b) in enumerate(zip(pa, bu)):
        pb, bb = body(p), body(b)
        where = f"B {name} line {i + 1}"
        if "?" in bb or "।" in bb:
            bad.append(f"{where}: «?» / «।»")
        if pb.startswith("#"):
            if not bb.startswith(pb.split()[0] + " "):
                bad.append(f"{where}: heading level")
            continue
        if re.fullmatch(r"\S+padaniddeso \S+\.", pb):
            if not bb.endswith(F.NIDDESA + "။"):
                bad.append(f"{where}: colophon")
            continue
        if pb in MK.VERSES:
            nverse += 1
            pw = [w.strip(",;.").lower() for w in re.sub(r"\[[^\]]*\]", "", pb).split()]
            pn = []
            for w in pw:
                if w in PNUM:
                    pn.append(PNUM[w])
                elif w in PNUM_PFX:
                    v = PNUM_PFX[w]
                    pn += [v[0], v[0]] if isinstance(v, tuple) else [v]
            bn = [MY_NUM[m[1]] for m in re.finditer(r"(?:^|[ ၊])([က-႟]+?)(?:ပါး| အပြည့်| မျိုး)", bb)
                  if m[1] in MY_NUM]
            if sorted(pn) != sorted(bn):         # a verse line may be reordered within the line
                bad.append(f"{where}: verse numbers {pn} vs {bn}")
            pv = [re.sub(r" \([^()]+\)", "", x) for x in re.findall(r"\[([^\]]+)\]", pb)]
            bv = [x.split("): ", 1)[1] for x in re.findall(r"\[([^\]]+)\]", bb)]
            if pv != bv:
                bad.append(f"{where}: verse variant {pv} vs {bv}")
            continue
        nlines += 1
        ps, bs = p_sentences(pb), re.split(r"(?<=။) ", bb)
        if len(ps) != len(bs):
            bad.append(f"{where}: {len(ps)} Pāli sentences vs {len(bs)} Burmese")
            continue
        for x, y in zip(ps, bs):
            nsent += 1
            # predicates
            pp = [(VK[("a" if m[1] else "") + "saṅgahitā"], VK[("a" if m[2] else "") + "saṅgahitā"],
                   VK[("a" if m[3] else "") + "saṅgahitā"]) if m[1] is not None else (VK[m[4]],)
                  for m in P_PRED.finditer(x)]
            bp = [(BV[m[1]], BV[m[2]], BV[m[3]]) if m[1] else (BV[m[4]],) for m in B_PRED.finditer(y)]
            npred += len(pp)
            if pp != bp:
                bad.append(f"{where}: predicates {pp} vs {bp}")
            # question
            pq = [VK[m[1]] for m in P_Q.finditer(x)]
            bq = [BV[m[2]] for m in B_Q.finditer(y)]
            bqp = [m[1] == ("တွင်" if BV[m[2]].startswith("S") else "နှင့်") for m in B_Q.finditer(y)]
            if pq != bq or not all(bqp):
                bad.append(f"{where}: question {pq} vs {bq}")
            # counts
            xa = x[[m.end() for m in re.finditer(r"(?<![\w])[Tt]e dhammā ", x)][-1]:] if re.search(r"(?<![\w])[Tt]e dhammā ", x) else ""
            ya = y[y.rfind(MK.TE + F.SUBJ_MARK):] if MK.TE + F.SUBJ_MARK in y else ""
            pc, bc = pali_counts(xa), burmese_counts(ya)     # counts stand only in the answers
            ncounts += len(pc)
            if pc != bc:
                bad.append(f"{where}: counts\n   pi {pc}\n   my {bc}")
            # plural verbs (subject «te dhammā»)
            for m in B_AVERB.finditer(y):
                if not m["pl"]:
                    bad.append(f"{where}: verb without «ကြ» «{y[m.start():m.end() + 5]}»")
            # fixed pieces
            for pk, bk in ((r"asaṅkhataṃ khandhato ṭhapetvā", F.THAPETVA), (r"(?<![\w])tehi dhammehi", MK.TEHI)):
                if len(re.findall(pk, x)) != y.count(bk):
                    bad.append(f"{where}: «{pk}» {x.count(pk)} vs {y.count(bk)}")
            if len(re.findall(r"(?<![\w])[Tt]e dhammā", x)) != y.count(MK.TE + F.SUBJ_MARK):
                bad.append(f"{where}: «te dhammā»")
            if (x == "Natthi.") != (y == MK.NATTHI + "။"):
                bad.append(f"{where}: «Natthi»")
            # chain items: number and bare items
            mp = P_PRED.search(x)
            pch = x[:mp.start()] if mp else (x[:-1] if x.endswith("….") else None)
            if pch is not None and " ye dhammā" in pch:
                mb = B_PRED.search(y)
                bch = y[:mb.start()] if mb else y[:-1]
                pit = [z for z in ELL.split(pch.strip()) if z]
                bit = [z for z in ELL.split(bch.strip()) if z]
                if len(pit) != len(bit):
                    bad.append(f"{where}: {len(pit)} chain items vs {len(bit)}")
                else:
                    for u, v in zip(pit, bit):
                        bare = not u.endswith(" ye dhammā")
                        if bare == bool(re.search(r"နှင့်(?: \[[^\]]+\])?$", v)):
                            bad.append(f"{where}: bare item «{u}» / «{v[-30:]}»")
print(f"B. per sentence: {nlines} content lines, {nsent} sentences, {npred} predicates, {ncounts} counts, "
      f"{nverse} verse lines; {sum(1 for x in bad if x.startswith('B'))} mismatches")

# ===================================================================================== C. reuse test (pi-1 / pi-2)
FIN = F.FINAL
nov = lambda s: re.sub(r" ?\[[^\]]*\]", "", s)              # noqa: E731
norm = lambda s: s.replace("ṇṇ", "nn")                      # noqa: E731
low = lambda s: s[0].lower() + s[1:] if s else s            # noqa: E731
occ = {}         # Pāli term -> {final Burmese at its occurrences: block id}


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
if MK.SLIPS_SEEN:
    print("source slips read:", sorted(set(MK.SLIPS_SEEN)))
if bad:
    print(f"\n{len(bad)} MISMATCHES")
    print("\n".join(bad[:40]))
    sys.exit(1)
print(f"\nOK: 0 mismatches; reuse {n_same + s_h} / {n_found + n_h} identical")
