"""Check the Burmese zero-shot of pi-6 group ch10c (Indriyayamaka 10-10 … 10-13) line by line.

usage: python3 -I -X utf8 check_ch10c.py [--mutate]
Adapted from check_sample.py / check_ch6-8.py:
  A. rebuild: make_ch10c.py regenerates the four files byte for byte (nothing written here);
  B. per line: B1 structure (equal non-empty lines, dashes, «…», «[», item numbers, labels, block IDs, heading levels,
     no «?» «।» «:-», final «။», NFC, no U+1050-U+109F, one blank line between segments, no double blank);
     B2 POLARITY: every Pāli negation (na, no, nuppajj-, nappajah-, Natthi) is one Burmese negative (မဟုတ် / မရှိ /
     မဖြစ်ပေါ် / ပိုင်းခြား မသိ / မပယ် / မပွားများ / မျက်မှောက် မပြု / မရရှိ), privative names masked (arūpa,
     a-X-ka); B3 VERBS: the sequence of finite verbs (uppajj-, parijān-, pajah-, bhāv-, sacchikar-, paṭilabh-,
     parinibbāy-) with root, tense, polarity and the «no ca … na V» double negative equals the Burmese sequence;
     Āmantā / No / Natthi in order; B4 (Ka) / (Kha) labels, every «vā pana» = «တစ်ဖန်»; B5 digits and number
     words (dve … aṭṭha «Nယောက်», pañca- / catuvokāra «ငါးပါး / လေးပါး», dutiya); B6 every recurring Pāli sentence
     has one and the same Burmese; B7 headings / colophons come out as their table value;
  C. reuse test: C1 the 22 faculty names (pi-2 ^2-219, read here independently of the generator) in every line, as
     often as the Pāli has them; C2 the terms read from pi-1 … pi-5 (and the sample) as often as the Pāli has them;
     C3 every person group of these files that the finished pi-6 groups (sample, ch2-02-4-5, ch3, ch6-8) have for
     identical Pāli comes out as theirs (their majority rendering; documented conflicts between them apart);
     C4 (not counted in the reuse total): every lead shared with the sibling ch. 9 / 10 groups comes out as theirs.
  --mutate: also run a mutation test (in memory); each mutation must be caught.
Prints the mismatches (0 expected) and the counts; exit 1 on any mismatch.
"""
import collections
import importlib
import pathlib
import re
import sys
import unicodedata

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
MK = importlib.import_module("make_ch10c")
F = MK.F
ROOT = HERE.parents[3]
NAMES = MK.NAMES_OUT
ID_RE = re.compile(r" (\^[0-9A-Za-z-]+)\s*$")
SPLIT = re.compile(r"(?<=[?.]) (?=[A-ZĀĪŪṬḌṆÑṄ(])")


def nonempty(text):
    return [l for l in text.splitlines() if l.strip()]


def body(l):
    return ID_RE.sub("", l).strip()


def nobr(s):
    return re.sub(r" ?\[[^\]]*\]", "", s)


def nolab(s):
    return re.sub(r"^\(\S+?\) ", "", s)


# ===================================================================================== FINAL pi-2 list, read here
def blocks(text):
    res, cur = {}, []
    for line in text.splitlines():
        if not line.strip():
            continue
        cur.append(line)
        m = ID_RE.search(line)
        if m:
            res[m.group(1)] = cur
            cur = []
    return res


def final_faculties():
    pf = ROOT / "AI_translation/pali/pi-2_split_chapters"
    bf = ROOT / "AI_translation/burmese/pi-2-burmese-plain-rails_split_chapters"
    for f in sorted(pf.glob("*.md")):
        pb = blocks(f.read_text(encoding="utf-8-sig"))
        if "^2-219" in pb:
            mb = blocks(unicodedata.normalize("NFC", (bf / f.name).read_text(encoding="utf-8-sig")))
            p, m = nobr(body(pb["^2-219"][0])), nobr(body(mb["^2-219"][0]))
            pi = [x.strip() for x in p.split(" – ", 1)[1].rstrip(".").split(",")]
            my = [x.strip() for x in m.split(" – ", 1)[1].rstrip("။").split("၊")]
            assert len(pi) == len(my) == 22
            return dict(zip(pi, my))
    raise SystemExit("pi-2 ^2-219 not found")


FAC = final_faculties()
FAC_STEM = {k[:-1]: v for k, v in FAC.items()}          # cakkhundriya -> «မျက်စိ၏ စွမ်းရည်»

# ===================================================================================== B2 / B3 helpers
MASK = [F.PLACES["arūpa"]] + [f"{v} မ{F.HAVE}ဘဲ" for v in MK.SA.values()]
M_NEG = ["မဟုတ်", "မရှိ", "မဖြစ်ပေါ်", "ပိုင်းခြား မသိ", "မပယ်", "မပွားများ", "မျက်မှောက် မပြု", "မရရှိ"]


def p_neg(p):
    s = nobr(body(p))
    return (len(re.findall(r"(?<![\w])(?:na|no|No|Na)(?![\w])", s)) + len(re.findall(r"\bnuppajj", s))
            + len(re.findall(r"\bnappa(?:j)?jah", s)) + len(re.findall(r"\b[Nn]atthi\b", s)))


def m_neg(m):
    s = nobr(body(m))
    for t in sorted(MASK, key=len, reverse=True):
        s = s.replace(t, "")
    return sum(s.count(x) for x in M_NEG)


P_END = {
    "uppajj": {"issanti": "fut", "issati": "fut", "issatīti": "fut", "ittha": "past", "itthāti": "past",
               "anti": "pres", "ati": "pres", "atīti": "pres"},
    "parijān": {"issanti": "fut", "issati": "fut", "issatīti": "fut", "ittha": "past", "itthāti": "past",
                "anti": "pres", "āti": "pres", "ātīti": "pres"},
    "pajah": {"issanti": "fut", "issati": "fut", "issatīti": "fut", "ittha": "past", "itthāti": "past",
              "anti": "pres", "ati": "pres", "atīti": "pres"},
    "bhāv": {"essanti": "fut", "essati": "fut", "essatīti": "fut", "ittha": "past", "itthāti": "past",
             "enti": "pres", "eti": "pres", "etīti": "pres"},
    "sacchikar": {"issanti": "fut", "issati": "fut", "issatīti": "fut", "ittha": "past", "itthāti": "past",
                  "onti": "pres", "oti": "pres", "otīti": "pres"},
    "paṭilabh": {"issanti": "fut"},
    "parinibbāy": {"issanti": "fut"},
}
P_SLIP = {"bhavissanti": ("bhāv", "fut"), "sacchākāsi": ("sacchikar", "past"), "nappajjahittha": ("pajah", "past")}
P_TOK = re.compile(r"(?P<noca>\bno ca\b)|(?P<w>\b(?:na )?\w+)")


def p_verbs(s):
    """Pāli finite verbs of a line in order: (root, tense, Burmese polarity, double negative): after «no ca» a
    positive verb is negated in Burmese, a negative one becomes «… ကား မဟုတ်»."""
    s = nobr(body(s))
    out, noca = [], False
    for m in P_TOK.finditer(s):
        if m["noca"]:
            noca = True
            continue
        w = m["w"]
        w = w[0].lower() + w[1:]
        neg = w.startswith("na ")
        w0 = w[3:] if neg else w
        if w0 in P_SLIP:
            r, t = P_SLIP[w0]
            neg = neg or w0.startswith("napp")
            out.append((r, t, neg or noca, noca and neg))
            noca = False
            continue
        if w0.startswith("nuppajj"):
            neg, w0 = True, w0[1:]
        if w0.startswith("nappajah"):
            neg, w0 = True, w0[3:]
        for r, ends in P_END.items():
            if w0.startswith(r) and w0[len(r):] in ends:
                out.append((r, ends[w0[len(r):]], neg or noca, noca and neg))
                noca = False
                break
    return out


M_STEM = [("uppajj", "မဖြစ်ပေါ်", True), ("uppajj", "ဖြစ်ပေါ်", False),
          ("parijān", "ပိုင်းခြား မသိ", True), ("parijān", "ပိုင်းခြား သိ", False),
          ("pajah", "မပယ်", True), ("pajah", "ပယ်", False),
          ("bhāv", "မပွားများ", True), ("bhāv", "ပွားများ", False),
          ("sacchikar", "မျက်မှောက် မပြု", True), ("sacchikar", "မျက်မှောက်ပြု", False),
          ("paṭilabh", "မရရှိ", True), ("paṭilabh", "ရရှိ", False),
          ("parinibbāy", "ပရိနိဗ္ဗာန် ပြုမည့်", False)]
M_VERB = re.compile("(?P<s>" + "|".join(re.escape(x) for _, x, _ in M_STEM) + ")"
                    r"(?P<t>(?:ကြ)?(?:ခဲ့)?(?:ကြ)?(?:လိမ့်မည်|မည့်)?)")
M_ROOT = {x: (r, n) for r, x, n in M_STEM}


def m_verbs(s):
    s = nobr(body(s))
    out = []
    for m in M_VERB.finditer(s):
        st = m["s"]
        pre = s[max(0, m.start() - 8):m.start()]
        after = s[m.end():m.end() + 12]
        if st in ("ဖြစ်ပေါ်", "မဖြစ်ပေါ်"):
            if pre.endswith("ပြန်လည် ") or after.startswith(("ဆဲ", "ပြီး", "ခြင်း")):
                continue
        if st == "ပိုင်းခြား သိ" and after.startswith("ခြင်း"):
            continue
        r, n = M_ROOT[st]
        t = m["t"]
        tense = "fut" if (t.endswith("လိမ့်မည်") or t.endswith("မည့်") or st.endswith("မည့်")) else (
            "past" if "ခဲ့" in t else "pres")
        notso = bool(re.match(r"(?:သည်)?ကား မဟုတ်", after))
        out.append((r, tense, n, notso))
    return out


ANS_P = re.compile(r"(?<![\w])(Āmantā|No|Natthi)\.")
ANS_M = {"Āmantā": F.YES, "No": F.NO, "Natthi": F.NATTHI}


def answers_p(p):
    return [a for a in ANS_P.findall(nobr(body(p)))]


def answers_m(m):
    s = nobr(body(m))
    out = []
    for mm in re.finditer(r"(?<![^\s။…])(ဟုတ်ပါသည်။|မဟုတ်ပါ။|မရှိပါ။)", s):
        out.append({F.YES: "Āmantā", F.NO: "No", F.NATTHI: "Natthi"}[mm[1]])
    return out


NUMW = [(r"\b[Dd]ve\b", "နှစ်" + MK.YOKE), (r"\b[Tt]ayo\b", "သုံး" + MK.YOKE), (r"\b[Cc]attāro\b", "လေး" + MK.YOKE),
        (r"\b[Pp]añca\b", "ငါး" + MK.YOKE), (r"\b[Cc]ha\b", "ခြောက်" + MK.YOKE), (r"\b[Ss]atta\b", "ခုနစ်" + MK.YOKE),
        (r"\b[Aa]ṭṭha\b", "ရှစ်" + MK.YOKE), (r"[Pp]añcavokār", "ငါးပါး"), (r"[Cc]atuvokār", "လေးပါး"),
        (r"\bdutiye\b", "ဒုတိယ"), (r"[Aa]ṭṭhamak", "အဋ္ဌမ")]

# ===================================================================================== C2 terms (Pāli regex -> Burmese)
REUSE = [
    (r"\bArahā\b|arahant", MK.ARAHA), (r"[Aa]ṭṭhamak|puggal", F.PUGGALA), (r"\bAnāgāmī\b", MK.ANAGAMI),
    (r"[Aa]nāgāmimagg", MK.ANAGAMIMAGGA), (r"[Aa]ggamagg", f"{MK.AGGA} {MK.MAGGA}"), (r"aggaphal", f"{MK.AGGA} {MK.PHALA}"),
    (r"samaṅg", MK.SAMANGI), (r"puthujjan", MK.PUTHUJJANA), (r"paṭilabh", MK.PATILABH),
    (r"[Kk]āmāvacar", MK.PLANE["kāmāvacara"]), (r"(?<![Aa])[Rr]ūpāvacar", MK.PLANE["rūpāvacara"]),
    (r"[Aa]rūp", F.PLACES["arūpa"]), (r"[Pp]añcavokār", F.PLACES["pañcavokāra"]),
    (r"[Cc]atuvokār", F.PLACES["catuvokāra"]), (r"[Aa]saññasatt", F.SATTA_ASANNA), (r"[Ss]uddhāvās", F.PLACES["suddhāvāsa"]),
    (r"[Pp]acchimabhavik", F.PACCHIMA), (r"[Pp]acchimacitt", f"{MK.PACCHIMA} {MK.CITTA}"),
    (r"upapajjant|\buppajjantānaṃ", F.PART["upapajjantānaṃ"][0]), (r"cavant", F.PART["cavantānaṃ"][0]),   # harmonise A3
    (r"parinibbant", F.PART["parinibbantānaṃ"][0]), (r"upapajjitvā", "ပြန်လည် ဖြစ်ပေါ်ပြီး"),
    (r"uppādakkhaṇe", MK.UPPADAK), (r"bhaṅgakkhaṇe", MK.BHANGAK), (r"nirodhasamāpann", MK.NIRODHA_SAM),
    (r"vippayutt", MK.VIPP), (r"sampayutt", MK.SAMP), (r"(?<!\w)somanass", MK.SOMANASSA), (r"(?<!\w)upekkh", MK.UPEKKHA),
    (r"(?<!\w)itth", MK.ITTHI), (r"(?<!\w)puris", MK.PURISA), (r"cakkhu", "မျက်စိ"), (r"ghān", "နှာခေါင်း"),
    (r"(?<!\w)saddh", MK.SADDHA), (r"ñāṇa", MK.NANA), (r"eteneva bhāvena", MK.ETENEVA), (r"\b[Ss]abbesaṃ\b", "အားလုံးတို့"),
    (r"\b[Ii]taresaṃ\b", F.OTHERS), (r"ṭhapetvā", F.THAPETVA), (r"avasesā", F.AVASESA), (r"\bpavatte\b", MK.PAVATTE),
    (r"citte vattamāne", MK.VATTAMANE), (r"anantarā", "ချက်ချင်း နောက်၌"), (r"\btattha\b", F.FT["tattha"]),
    (r"\b[Yy]attha\b", F.CL["yattha"][0]), (r"\bĀmantā\b", F.YES), (r"\bNatthi\b", F.NATTHI), (r"\bNo\.", F.NO),
    (r"mūlakaṃ\)", F.BASED),
    (r"\bno ca tāsaṃ\b|(?:kkhaṇe|vattamāne) tāsaṃ\b", "ထိုမိန်းမတို့"),     # harmonise B3: the pronoun tāsaṃ «ထိုမိန်းမတို့»
]
NOT_HEAD = {MK.ITTHI: "ထိုမိန်းမတို့"}        # harmonise B3: the pronoun is not counted as the head noun itthī
W_SRC = {k: v for k, v in F.WITNESS.items()}            # values read / checked in pi-1 … pi-5 at import


# ===================================================================================== C3 pi-6 finished groups
FINISHED = ["1-mulayamaka.md", "2-01-khandhayamaka.md", "2-02-khandhayamaka.md", "3-01-ayatanayamaka.md",
            "3-02-ayatanayamaka.md", "3-03-ayatanayamaka.md", "3-04-ayatanayamaka.md", "3-05-ayatanayamaka.md",
            "3-06-ayatanayamaka.md", "4-dhatuyamaka.md", "5-01-saccayamaka.md", "5-02-saccayamaka.md",
            "5-03-saccayamaka.md", "6-01-sankharayamaka.md", "6-02-sankharayamaka.md", "8-cittayamaka.md"]
G_RE = re.compile(r"^(?P<who>.+?) (?P<pro>tesaṃ tattha|tāsaṃ tattha|tesaṃ|tāsaṃ) (?P<x>\S+?)(?:ñca| ca)? "
                  r"(?:na )?(?:n)?(?:uppajj|nirujjh)")
CONFLICTS = {   # identical Pāli rendered differently by the finished groups: mine follows the majority (listed)
}


def groups_of(pali_sentence):
    s = nolab(pali_sentence)
    if s.lower().startswith(("yassa", "yattha")):
        return None
    m = G_RE.match(s)
    if not m or m["who"].startswith(("(", "[")):
        return None
    return m["who"], m["pro"]


def my_prefix(m_sentence, pro):
    i = m_sentence.find("အား ")
    if i < 0:
        return None
    end = i + len("အား")
    if "tattha" in pro:
        if not m_sentence[end:].startswith(" " + F.FT["tattha"]):
            return None
        end += len(" " + F.FT["tattha"])
    return m_sentence[:end]


SIBLINGS = ["9-01-dhammayamaka.md", "9-02-dhammayamaka.md", "9-03-dhammayamaka.md"] + \
           [f"10-0{i}-indriyayamaka.md" for i in range(1, 10)]     # ch9-10a / ch10b (done 2026-11-21, read only)


def harvest(files=None):
    """identical person groups of the finished pi-6 files: (who, pro) -> Counter(Burmese prefix)."""
    P = ROOT / "AI_translation/pali/pi-6_split_chapters"
    B = MK.OUT
    out = collections.defaultdict(collections.Counter)
    for n in (files or FINISHED):
        if not (B / n).exists():
            continue
        for p, m in zip(nonempty((P / n).read_text(encoding="utf-8-sig")), nonempty((B / n).read_text())):
            ps, ms = SPLIT.split(nolab(body(p))), re.split(r"(?<=။) ", nolab(body(m)))
            if len(ps) != len(ms):
                continue
            for x, y in zip(ps, ms):
                g = groups_of(x)
                if not g:
                    continue
                pre = my_prefix(y, g[1].replace("tāsaṃ", "tesaṃ"))
                if pre:
                    out[(g[0], g[1].replace("tāsaṃ", "tesaṃ"))][pre] += 1
    return out


# ===================================================================================== the checks
def check(PAIRS, rebuild=True):
    bad, cnt = [], collections.Counter()

    def err(n, i, what, p="", m=""):
        bad.append(f"{n}:{i} {what}\n  P: {p[:300]}\n  M: {m[:300]}")

    if rebuild:
        for n in NAMES:
            text = F.translate_text((MK.PALI / n).read_text(encoding="utf-8-sig"))
            if text != (MK.OUT / n).read_text(encoding="utf-8"):
                err(n, 0, "A: regenerated text differs")
            cnt["A"] += 1
    sent = collections.defaultdict(set)
    reuse = collections.Counter()
    for n, (P, M) in PAIRS.items():
        raw = (MK.OUT / n).read_text(encoding="utf-8") if rebuild else ""
        if rebuild and ("\n\n\n" in raw or raw.startswith("\n")):
            err(n, 0, "B1: double blank line")
        if len(P) != len(M):
            err(n, 0, f"B1: {len(P)} vs {len(M)} lines")
        for i, (p, m) in enumerate(zip(P, M), 1):
            cnt["B1"] += 1
            for e in MK.line_check(p, m):
                err(n, i, "B1: " + e, p, m)
            if unicodedata.normalize("NFC", m) != m or re.search("[ၐ-႟]", m):
                err(n, i, "B1: NFC / code points", p, m)
            if p.startswith("#"):
                h = re.match(r"^(#+) (.*)$", body(p))
                exp = f"{h[1]} {F.heading(h[2])}"
                if body(m) != exp:
                    err(n, i, "B7: heading", p, m)
                cnt["B7"] += 1
                continue
            # B2
            a, b = p_neg(p), m_neg(m)
            cnt["B2"] += a
            if a != b:
                err(n, i, f"B2: negations {a} vs {b}", p, m)
            # B3
            pv, mv = p_verbs(p), m_verbs(m)
            cnt["B3"] += len(pv)
            if pv != mv:
                err(n, i, f"B3: verbs\n    {pv}\n    {mv}", p, m)
            pa, ma = answers_p(p), answers_m(m)
            cnt["B3a"] += len(pa)
            if pa != ma:
                err(n, i, f"B3: answers {pa} vs {ma}", p, m)
            # B4
            lp = F.LABEL_RE.match(p)
            if lp:
                cnt["B4"] += 1
            vp, vm = nobr(p).count("vā pana"), nobr(m).count(F.VA_PANA)
            if vp != vm:
                err(n, i, f"B4: vā pana {vp} vs {vm}", p, m)
            # B5
            for rx, my in NUMW:
                a, b = len(re.findall(rx, nobr(body(p)))), nobr(body(m)).count(my)
                cnt["B5"] += a
                if a != b:
                    err(n, i, f"B5: {rx} {a} vs {b}", p, m)
            # B6 sentences
            ps, ms = SPLIT.split(nolab(body(p))), re.split(r"(?<=။) ", nolab(body(m)))
            if len(ps) == len(ms):
                for x, y in zip(ps, ms):
                    sent[x].add(y)
            else:
                cnt["B6 lines not split"] += 1
            # B7 colophons / table lines
            bp = nolab(body(p))
            if bp in F.COLO:
                cnt["B7"] += 1
                if nolab(body(m)) != F.COLO[bp]:
                    err(n, i, "B7: colophon", p, m)
            # C1 faculty names
            sp, sm = nobr(body(p)), nobr(body(m))
            for st, my in FAC_STEM.items():
                a = len(re.findall(r"(?<!\w)" + st, sp, re.I))
                if a:
                    b = sm.count(my)
                    reuse["C1"] += a
                    if a != b:
                        err(n, i, f"C1: {st} {a} vs «{my}» {b}", p, m)
                    else:
                        reuse["C1 ok"] += a
            # C2 terms
            for rx, my in REUSE:
                a = len(re.findall(rx, sp, re.I))
                if a:
                    b = (sm.replace(NOT_HEAD[my], "") if my in NOT_HEAD else sm).count(my)
                    reuse["C2"] += a
                    if a != b:
                        err(n, i, f"C2: {rx} {a} vs «{my}» {b}", p, m)
                    else:
                        reuse["C2 ok"] += a
    for x, ys in sent.items():
        cnt["B6"] += 1
        if len(ys) != 1:
            bad.append(f"B6: «{x[:200]}» has {len(ys)} renderings: {sorted(ys)}")
    # C3 pi-6 groups
    H = harvest()
    mine = {}
    for n, (P, M) in PAIRS.items():
        for p, m in zip(P, M):
            ps, ms = SPLIT.split(nolab(body(p))), re.split(r"(?<=။) ", nolab(body(m)))
            if len(ps) != len(ms):
                continue
            for x, y in zip(ps, ms):
                g = groups_of(x)
                if g:
                    key = (g[0], g[1].replace("tāsaṃ", "tesaṃ"))
                    pre = my_prefix(y, key[1])
                    mine.setdefault(key, set()).add(pre)
    c3_exc = []
    for key, pres in mine.items():
        if key not in H:
            continue
        reuse["C3"] += 1
        major = H[key].most_common(1)[0][0]
        if pres == {major}:
            reuse["C3 ok"] += 1
        elif len(pres) == 1 and next(iter(pres)) in H[key] and key in CONFLICTS:
            c3_exc.append((key, next(iter(pres)), dict(H[key])))
        else:
            bad.append(f"C3: {key} mine {pres} vs finished {dict(H[key])}")
    # C4 the sibling ch. 10 groups (same Pāli leads in 9-01 … 10-09): every shared lead as theirs
    S = harvest(SIBLINGS)
    for key, pres in mine.items():
        if key in S:
            reuse["C4"] += 1
            if len(pres) == 1 and next(iter(pres)) in S[key]:
                reuse["C4 ok"] += 1
            else:
                bad.append(f"C4: {key} mine {pres} vs sibling groups {dict(S[key])}")
    return bad, cnt, reuse, c3_exc


def report(bad, cnt, reuse, c3_exc):
    for b in bad[:60]:
        print(b)
    print(f"A {cnt['A']}/{len(NAMES)} regenerated identical; B1 {cnt['B1']} lines; B2 {cnt['B2']} negations; "
          f"B3 {cnt['B3']} verbs, {cnt['B3a']} answers; B4 {cnt['B4']} labelled lines; B5 {cnt['B5']} numbers; "
          f"B6 {cnt['B6']} distinct Pāli sentences ({cnt['B6 lines not split']} lines not sentence-aligned); "
          f"B7 {cnt['B7']} headings / colophons")
    tot = reuse["C1"] + reuse["C2"] + reuse["C3"]
    ok = reuse["C1 ok"] + reuse["C2 ok"] + reuse["C3 ok"]
    print(f"reuse {ok} / {tot} (C1 faculty names {reuse['C1 ok']}/{reuse['C1']}, C2 terms {reuse['C2 ok']}/"
          f"{reuse['C2']}, C3 pi-6 person groups {reuse['C3 ok']}/{reuse['C3']}); {len(c3_exc)} documented exceptions")
    print(f"C4 sibling ch. 9 / 10 groups (ch9-10a, ch10b): {reuse['C4 ok']}/{reuse['C4']} distinct shared leads agree")
    for e in c3_exc:
        print("  exception:", e)
    print(f"{len(bad)} mismatches")
    return len(bad)


def mutate(PAIRS):
    muts = [("drop «မ»", "မဖြစ်ပေါ်", "ဖြစ်ပေါ်"), ("drop «ခဲ့»", "ဖြစ်ပေါ်ခဲ့", "ဖြစ်ပေါ်"),
            ("future -> present", "ဖြစ်ပေါ်လိမ့်မည်", "ဖြစ်ပေါ်"), ("drop «ကား မဟုတ်»", "သည်ကား မဟုတ်", ""),
            ("Āmantā -> No", F.YES, F.NO), ("drop «တစ်ဖန်»", F.VA_PANA + " ", ""),
            ("faculty changed", "နား၏ စွမ်းရည်", "နှာခေါင်း၏ စွမ်းရည်"), ("pariññā polarity", "ပိုင်းခြား မသိ", "ပိုင်းခြား သိ"),
            ("bhāveti polarity", "မပွားများ", "ပွားများ"), ("number", "နှစ်ယောက်", "သုံးယောက်"),
            ("person", "ရဟန္တာ", "အနာဂါမ်"), ("place", "ကာမဘုံ", "သိမ်မွေ့သော ရုပ်ဘုံ")]
    caught = 0
    for name, a, b in muts:
        P2 = {}
        done = False
        for n, (P, M) in PAIRS.items():
            M2 = list(M)
            if not done:
                for i, m in enumerate(M2):
                    if a in m and not m.startswith("#"):
                        M2[i] = m.replace(a, b, 1)
                        done = True
                        break
            P2[n] = (P, M2)
        bad = check(P2, rebuild=False)[0]
        ok = bool(bad) and done
        caught += ok
        print(f"mutation «{name}»: {'caught' if ok else 'NOT CAUGHT'} ({len(bad)} mismatches)")
    print(f"mutation test: {caught}/{len(muts)} caught")
    return caught == len(muts)


if __name__ == "__main__":
    PAIRS = {n: (nonempty((MK.PALI / n).read_text(encoding="utf-8-sig")),
                 nonempty((MK.OUT / n).read_text(encoding="utf-8"))) for n in NAMES if (MK.OUT / n).exists()}
    for n in PAIRS:                              # per chapter (no rebuild: A is book-wide above)
        bad1, cnt1, re1, _ = check({n: PAIRS[n]}, rebuild=False)
        ok1 = re1["C1 ok"] + re1["C2 ok"] + re1["C3 ok"]
        tot1 = re1["C1"] + re1["C2"] + re1["C3"]
        segs = sum(1 for l in PAIRS[n][0] if ID_RE.search(l))
        print(f"{n}: {segs} segments, {len(PAIRS[n][1])} lines, {len(bad1)} mismatches, reuse {ok1} / {tot1}")
    nb = report(*check(PAIRS))
    if "--mutate" in sys.argv:
        if not mutate(PAIRS):
            nb += 1
    sys.exit(1 if nb else 0)
