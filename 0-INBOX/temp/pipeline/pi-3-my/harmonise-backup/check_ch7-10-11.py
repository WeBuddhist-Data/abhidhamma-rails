"""Check of the pi-3 Burmese zero-shot chapters 7-chatthanayo, 10-navamanayo, 11-dasamanayo against the Pāli.

usage: python3 -I -X utf8 check_ch7-10-11.py
  A. regeneration: make_ch7-10-11.render() on every chapter gives exactly the written file.
  B. per line, the Pāli parsed here with its own patterns (not those of the generator):
     * every count (kind, number, in order) with the polarity of its verb (sampayutta / vippayutta) and its
       «kehici» flag; «na kehici / na kāhici» = 0;
     * the main verbs in order: polarity, question / statement, number (-o / -aṃ singular, -āni plural, -ā by the
       subject: «te dhammā» plural, a feminine singular subject singular, else plural);
     * the relative clauses «ye dhammā V» (count and polarity), «tehi dhammehi», «te dhammā», the questions
       «katihi khandhehi …», «Katihi V?», «Natthi.» and the sentence count;
     * no «?» / «।», no Zawgyi-only code points; headings keep their level; colophons and verse lines as the tables;
       the number words of the verse lines; identical verse lines identical in Burmese (ch7 / ch11).
     Topic names inside the Burmese are masked before verbs and counts are read; a frame relative is
     «V-သော သဘောတရားများ» followed by «…» / «၊» (a mātikā term in a frame is followed by «နှင့်» / «သည်»).
  C. reuse test (as check_sample.py): every topic name / mātikā term used, every heading and colophon and every whole
     line that also occurs in pi-1 / pi-2 has exactly their FINAL (rails) Burmese; prints n / n.
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
_spec = importlib.util.spec_from_file_location("make_ch7_10_11", HERE / "make_ch7-10-11.py")
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
    if unicodedata.normalize("NFC", M.render(name)) != (OUT / name).read_text(encoding="utf-8"):
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
P_VERB = re.compile(r"(?<![\w])(?<!ye dhammā )(?P<v>sampayutt|vippayutt)(?P<e>oti|anti|āti|āni|o|aṃ|ā)(?![\w])"
                    r"(?! dhammā)", re.IGNORECASE)
P_REL = re.compile(r"(?<![\w])ye dhammā(?: (sampayuttā|vippayuttā))?")
P_SOME = re.compile(r"(?<![\w])(?<!na )kehici (?=sampayutt|vippayutt)")      # «kehici V» (not «na kehici …»)
P_Q1 = "katihi khandhehi katihāyatanehi katihi dhātūhi"
P_PL = re.compile(r"dhammā|(?<![\w])ca(?![\w])|ñca(?![\w])|saṅkhārā|khandhā|dhātuyo|āyatanāni|saccāni|indriyāni|"
                  r"balāni|bojjhaṅgā")
P_FSG = re.compile(r"(?:dhātu|avijjā|vedanā|taṇhā|jāti|jarā|appamaññā|saññā|cetanā)$", re.IGNORECASE)

MY_NUM = {v: k for k, v in F.NUM_MY.items()}
KMY = {"အစုအဝေး": "k", "အာရုံခံ နယ်ပယ်": "a", "ဓာတ်": "d"}
_KN = "အစုအဝေး|အာရုံခံ နယ်ပယ်|ဓာတ်"
B_TOKS = rf"(?:(?:{_KN}) [က-႟]+?ပါး)"
B_RUN = re.compile(rf"(?P<run>{B_TOKS}(?:၊ {B_TOKS})*)(?P<post>တို့၏ အချို့နှင့်|၏ အချို့နှင့်|တို့နှင့်|နှင့်) "
                   r"(?P<v>ယှဉ်တွဲ|ကင်းကွာ)(?P<pl>ကြ)?သည်(?=[၊။])")
B_TOK = re.compile(rf"(?P<kind>{_KN}) (?P<n>[က-႟]+?)ပါး")
B_ZERO = re.compile(rf"(?P<v>ယှဉ်တွဲ|ကင်းကွာ)ရာ (?P<ks>(?:(?:{_KN})(?:၊ )?)+) မရှိ")
B_VERB = re.compile(r"(?P<v>ယှဉ်တွဲ|ကင်းကွာ)(?P<pl>ကြ)?(?P<q>သနည်း|သည်)(?=[၊။])")
B_REL = re.compile(r"(?P<v>ယှဉ်တွဲ|ကင်းကွာ)သော သဘောတရားများ(?=…|၊|\.\.)")   # a frame relative (a term is followed by နှင့် / သည်)
POL = {"ယှဉ်တွဲ": True, "ကင်းကွာ": False, "sampayutt": True, "vippayutt": False}
Q1_B = "အစုအဝေး မည်မျှ၊ အာရုံခံ နယ်ပယ် မည်မျှ၊ ဓာတ် မည်မျှတို့နှင့်"
ZAWGYI = re.compile(r"[ၠ-႗]")      # code points Zawgyi misuses (not used by these Burmese texts)
NAMES_MASK = sorted({v for v, _ in F.SUBJ.values() if re.search("ယှဉ်တွဲ|ကင်းကွာ", v)}, key=len, reverse=True)


def mask(b):
    for n in NAMES_MASK:
        b = b.replace(n, "⟨T⟩")
    return b


def pali_counts(p):
    verbs = [(m.start(), POL[m["v"].lower()]) for m in P_VERB.finditer(p)]
    out = []
    for m in P_TOK.finditer(p):
        if m["z"]:
            kind, n = {"khandhehi": "k", "āyatanehi": "a", "dhātūhi": "d"}[m["z"]], 0
        else:
            kind = "k" if m["k"] else "a" if m["a"] else "d"
            st = m["k"] or m["a"] or m["d"] or m["d2"]
            n = PN[STEM[st.lower()]]
        vpos, pol = next(((pos, pv) for pos, pv in verbs if pos > m.start()), (None, None))
        some = vpos is not None and bool(P_SOME.search(p[m.end():vpos + 12])) and ";" not in p[m.end():vpos]
        out.append((kind, n, pol, some))
    return out


def burmese_counts(b):
    out = []
    for m in B_RUN.finditer(b):
        some = "အချို့" in m["post"]
        toks = list(B_TOK.finditer(m["run"]))
        one = len(toks) == 1 and toks[0]["n"] == "တစ်"
        if one != (not m["post"].startswith("တို့")):
            bad.append(f"B grammar «{m['run']}{m['post']}»")
        for i, t in enumerate(toks):
            out.append((m.start() + i, KMY[t["kind"]], MY_NUM.get(t["n"], -1), POL[m["v"]], some))
    for m in B_ZERO.finditer(b):
        for i, k in enumerate(m["ks"].split("၊ ")):
            out.append((m.start() + i, KMY[k], 0, POL[m["v"]], False))
    return [x[1:] for x in sorted(out)]


def pali_verbs(p):
    """[(polarity, question?, plural?)] of the main verbs of a line."""
    res = []
    for m in P_VERB.finditer(p):
        e = M.END_NORM.get(m["e"], m["e"])
        q = p[m.end():m.end() + 3].lstrip("ti").startswith("?") or p[m.end():].startswith("?")
        if e in ("o", "aṃ"):
            pl = False
        elif e == "āni":
            pl = True
        else:
            before = p[:m.start()]
            subj = ""
            for c in reversed(re.split(r"…pe…|…|\?|\.|;|, te dhammā ", before)):
                c2 = re.sub(P_TOK, "", c).replace(P_Q1, "")
                c2 = re.sub(r"(?i)katihi|natthi|kehici", "", P_VERB.sub("", c2)).strip(" ,")
                if c2:
                    subj = c2
                    break
            if ", te dhammā " in before[-len(subj) - 14:] or re.search(r"(?i)(?:^| )te dhammā$", subj):
                subj = "te dhammā"
            subj = re.sub(r" ?\[[^\]]*\]", "", subj)
            pl = bool(P_PL.search(subj)) or not P_FSG.search(subj)
        res.append((POL[m["v"].lower()], q, pl))
    return res


def burmese_verbs(b):
    return [(POL[m["v"]], m["q"] == "သနည်း", bool(m["pl"])) for m in B_VERB.finditer(b)]


VERSE_NUM = {"ekūnavīsati": "ဆယ့်ကိုး", "paññāsa": "ငါးဆယ်", "aṭṭha ": "ရှစ်", "pannarasa": "ဆယ့်ငါး",
             "aṭṭhārasa": "ဆယ့်ရှစ်", "tevīsa": "တစ်ရာ့နှစ်ဆယ့်သုံး", "cattāro": "လေး", "satta": "ခုနစ်",
             "dve ": "နှစ်", "cuddas": "ဆယ့်လေး", "dvādasa": "ဆယ့်နှစ်", "soḷasa": "ဆယ့်ခြောက်",
             "tecattālīsa": "လေးဆယ့်သုံး", " cha;": "ခြောက်"}
nlines = ncounts = nverbs = nrel = 0
verse_my = {}
for name in NAMES:
    pa, bu = lines(PALI / name), lines(OUT / name)
    if len(pa) != len(bu):
        bad.append(f"B {name}: {len(pa)} vs {len(bu)} lines")
        continue
    for i, (p, b) in enumerate(zip(pa, bu)):
        pb, bb = body(p), body(b)
        where = f"B {name} line {i + 1}"
        if "?" in bb or "।" in bb or ZAWGYI.search(bb):
            bad.append(f"{where}: «?» / «।» / Zawgyi")
        if pb.startswith("#"):
            if not bb.startswith(pb.split()[0] + " ") or bb[len(pb.split()[0]) + 1:] != F.HEAD[pb.split(" ", 1)[1]]:
                bad.append(f"{where}: heading")
            continue
        m = F.NIDDESA_COLO_RE.fullmatch(pb)
        if m:
            if bb != f"{F.ORD[F.ORD_COLO[m['o']]]} {F.NIDDESO[m['n']]}။":
                bad.append(f"{where}: colophon")
            continue
        if pb in F.FIXED:                       # verse lines
            if bb != F.FIXED[pb]:
                bad.append(f"{where}: verse line differs from the table")
            if verse_my.setdefault(pb, bb) != bb:
                bad.append(f"{where}: identical verse line, different Burmese")
            for pw, mw in VERSE_NUM.items():
                if pw in pb + " " and mw not in bb:
                    bad.append(f"{where}: number «{pw.strip()}» = «{mw}» missing")
            continue
        nlines += 1
        mb = mask(bb)
        # sentences
        prot = re.sub(r"\[[^\]]*\]", lambda x: "⟦" + "x" * len(x[0]) + "⟧", pb)
        nps = len(re.findall(r"(?<=[?.]) (?=[A-ZĀĪŪṬḌṆÑ])", prot)) + 1
        nbs = len(re.findall(r"(?<=။) ", bb)) + 1
        if nps != nbs:
            bad.append(f"{where}: {nps} Pāli sentences vs {nbs} Burmese")
        pv, bv = pali_verbs(pb), burmese_verbs(mb)
        if pv != bv:
            bad.append(f"{where}: verbs\n   pi {pv}\n   my {bv}")
        nverbs += len(pv)
        pc, bc = pali_counts(pb), burmese_counts(mb)
        if pc != bc:
            bad.append(f"{where}: counts\n   pi {pc}\n   my {bc}")
        ncounts += len(pc)
        # relatives: polarity of each «ye dhammā» = the next «ye dhammā V»
        rels = list(P_REL.finditer(pb))
        prl = []
        for j, r in enumerate(rels):
            v = next((x[1] for x in rels[j:] if x[1]), None)
            prl.append(POL[v[:-1]] if v else None)
        brl = [POL[x["v"]] for x in B_REL.finditer(bb)]
        if prl != brl:
            bad.append(f"{where}: relatives pi {prl} my {brl}")
        nrel += len(prl)
        checks = [("question 1", pb.count(P_Q1), mb.count(Q1_B)),
                  ("Katihi V?", len(re.findall(r"Katihi (?:sampayutt|vippayutt)\w*\?", pb)),
                   len(re.findall(r"(?<!ဓာတ် )မည်မျှတို့နှင့် (?:ယှဉ်တွဲ|ကင်းကွာ)(?:ကြ)?သနည်း", mb))),
                  ("Natthi", pb.count("Natthi."), sum(1 for s in re.split(r"(?<=။) ", bb) if s == "မရှိ။")),
                  ("tehi dhammehi", len(re.findall(r"(?<![\w])tehi dhammehi", pb)), mb.count("ထိုသဘောတရားတို့နှင့်")),
                  ("te dhammā", len(re.findall(r"(?<![\w])(?<!ye )[Tt]e dhammā", pb)), mb.count("ထိုသဘောတရားများသည်")),
                  ("kehici", len(P_SOME.findall(pb)), mb.count("အချို့နှင့်")),
                  ("ellipsis", len(re.findall(r"…pe…|…Pe…|…", pb)), bb.count("…")),
                  ("variants", pb.count("["), bb.count("["))]
        for what, x, y in checks:
            if x != y:
                bad.append(f"{where}: {what} {x} vs {y}")
print(f"B. per line: {nlines} content lines, {nverbs} verbs, {ncounts} counts, {nrel} relatives; "
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
    base = k.removesuffix(" dhammā")
    if k.endswith(" dhammā") or k in F.NO_DHAMMA:
        kk = norm(F.TERM_ALIAS.get(base, base) + ("" if k in F.NO_DHAMMA else " dhammā"))
        if k in F.NO_DHAMMA:
            kk = norm(k) + " dhammā"
    else:
        kk = norm(k)
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

# frame phrases read from pi-1 (witnessed segments)
n_w = s_w = 0
for pali, my, wid in (("Tehi dhammehi ye dhammā sampayuttā", "ထိုသဘောတရားတို့နှင့် ယှဉ်တွဲသော သဘောတရားများ", "^1-1115"),
                      ("te dhammā", "ထိုသဘောတရားများသည်", "^1-1091"), ("natthi", "မရှိ", "^1-1433")):
    n_w += 1
    f, p, b = FIN.seg("1", wid)
    used = any(my in (OUT / n).read_text(encoding="utf-8") for n in NAMES)
    if pali.lower() in " ".join(p).lower() and my in " ".join(b) and used:
        s_w += 1
    else:
        bad.append(f"C frame {pali}: «{my}» not at {wid} or unused")
print(f"C. reuse test, frame phrases: {s_w} / {n_w} identical with pi-1 final")

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
print(f"\nOK: 0 mismatches; reuse {n_same + s_w + s_h} / {n_found + n_w + n_h} identical")
