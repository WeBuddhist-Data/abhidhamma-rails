"""one-off: build check_ch4-15-21.py from check_ch4-10-14.py (read-only) with the tikaduka changes"""
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parents[1]
src = (HERE / "check_ch4-10-14.py").read_text(encoding="utf-8")
L = src.split("\n")


def find(prefix, start=0):
    for i in range(start, len(L)):
        if L[i].startswith(prefix):
            return i
    raise KeyError(prefix)


def block_end(i):
    """the end (exclusive) of a top-level def/assignment block starting at line i"""
    j = i + 1
    while j < len(L) and (L[j].startswith((" ", "\t", ")", "]", "}")) or L[j] == "" and j + 1 < len(L)
                          and L[j + 1].startswith((" ", ")"))):
        j += 1
    return j


out = list(L)
NEW_DOC = '''"""Per-line check of the Burmese pi-7 chapters 4-15 … 4-21 (the TIKADUKA chapters: a triad term combined with a
dyad term on one noun, «<triad term> <dyad term>») against the Pāli (adapted from check_ch4-10-14.py; independent of
the generator's frames: the condition, count and negation tables and the term regexes are typed here again; the dyad /
triad / name values are a frozen copy, compared with the generator's (T); the active triad-dyad pair of a line is read
from the Pāli headings).

usage: python3 -I -X utf8 check_ch4-15-21.py [chapter ...] [--out DIR] [--mutate] [--sample] [--regress] [--pe]
       [--groups]
Checks, line by line (Pāli line i <-> Burmese line i):
  S  structure: equal non-empty lines, heading #-level, block IDs, no «?» «।» «:-», no Latin left outside variants;
  P  polarity: «မဟုတ်» count and the «မ…» negatives expected from the Pāli tokens (NEG_*);
  C  conditions: the sequence of conditions (stem + polarity) named in the Pāli = the sequence in the Burmese;
  O  term order: the sequence of combined terms (triad term + dyad term) in the Pāli = the sequence in the Burmese
     (conditioning -> conditioned); the triad-dyad headings, the group headings, the pada headings and the colophons
     carry their names (the Pāli order «<triad name>နှင့် <dyad name>»);
  N  numbers: counts «… ခု», khandha numbers «… ပါး», group numbers «… မျိုးတွဲ», digits «(n)»;
  I  identity: identical Pāli sentences have identical Burmese sentences (these chapters and the approved sample);
     against the finished pi-7 groups the agreement is counted (G) and the differences listed with --groups;
  T  tables: the module's condition names and counts, and the generator's terms and names = this checker's copy;
  R  reuse: every value taken from pi-1 … pi-6 (WITNESS) is re-read from the FINAL rails and found in every line
     whose Pāli contains its Pāli; sentences that occur in pi-1 … pi-6 are identical.
--sample  regenerates the approved sample (1-00, 1-02) in memory with this generator's extensions (world A) and
          requires it to be identical to the files on disk.
--regress regenerates the dukatika chapters 4-02 … 4-09 (make_ch4-02-09) and 4-10 … 4-14 (make_ch4-10-14) in memory
          WITH this group's extensions loaded (make_ch4-15-21 imports and extends them) and requires them identical
          to the files on disk.
--mutate  plants errors in copies (pi-7-my/chk-mut-ch4-15-21/, deleted afterwards); each must be caught.
--pe      runs pi-3-mr/check_text.py on a «…Pe…»-folded copy of the Pāli in pi-7-my/chk-pe/ch4-15-21/ (deleted).
Exit 1 on any mismatch.
"""'''
# docstring
end_doc = next(i for i in range(1, len(L)) if L[i].startswith('"""'))
out[0:end_doc + 1] = [NEW_DOC]
L = out
out = list(L)
s = "\n".join(L)

s = s.replace('''MINE = ["4-10-dukatika-sarammanaduka.md", "4-11-dukatika-upadanaduka.md", "4-12-dukatika-kilesaduka.md",
        "4-13-dukatika-dassanenapahatabbaduka.md", "4-14-dukatika-saranaduka.md"]''',
              '''MINE = ["4-15-tikaduka-hetuduka.md", "4-16-tikaduka-sappaccayaduka.md", "4-17-tikaduka-asavaduka.md",
        "4-18-tikaduka-sarammanaduka.md", "4-19-tikaduka-kilesaduka.md",
        "4-20-tikaduka-dassanenapahatabbaduka.md", "4-21-tikaduka-sauttaraduka.md"]''')
assert "4-15-tikaduka-hetuduka.md" in s
s = re.sub(r'MODEL = \["4-02-dukatika-hetuduka.md".*?\]\n', lambda m: m[0].replace(
    '"4-09-dukatika-paramasaduka.md"]', '"4-09-dukatika-paramasaduka.md"]\nMODEL2 = ["4-10-dukatika-sarammanaduka.md", '
    '"4-11-dukatika-upadanaduka.md", "4-12-dukatika-kilesaduka.md",\n          "4-13-dukatika-dassanenapahatabbaduka.md", '
    '"4-14-dukatika-saranaduka.md"]'), s, flags=re.S)
assert "MODEL2" in s
s = s.replace('''# the finished groups (identity, informational): every pi-7 chapter on disk except these and 5-01 … 5-04 (in progress)''',
              '''# the finished groups (identity, informational): every pi-7 chapter on disk except these and 5-05 … 5-20 (in progress)''')
s = s.replace('''if p.name[:4] not in ("4-10", "4-11", "4-12", "4-13", "4-14", "5-01", "5-02", "5-03", "5-04")''',
              '''if p.name[:4] not in ("4-15", "4-16", "4-17", "4-18", "4-19", "4-20", "4-21")
                and not ("5-05" <= p.name[:4] <= "5-20")''')
assert '"5-05" <= p.name[:4]' in s

# frozen-table additions (after the short triad headings of 4-14)
s = s.replace('''TIKA_MY["Sanidassanattikaṃ"] = "မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိခြင်း သုံးမျိုးတွဲ"
''', '''TIKA_MY["Sanidassanattikaṃ"] = "မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိခြင်း သုံးမျိုးတွဲ"
# 4-15 … 4-21 (this group): the short triad headings of 4-21, the term «nakenaci viññeyya» (4-16, as written; = 5-02 /
# 5-04), the cluster names of the colophons
TRIAD_MY["Dassanattikaṃ"] = TRIAD_MY["Dassanenapahātabbattikaṃ"]
TRIAD_MY["Dassanahetuttikaṃ"] = TRIAD_MY["Dassanenapahātabbahetukattikaṃ"]
TIKA_MY["Dassanattikaṃ"] = TIKA_MY["Dassanenapahātabbattikaṃ"]
TIKA_MY["Dassanahetuttikaṃ"] = TIKA_MY["Dassanenapahātabbahetukattikaṃ"]
DYAD_MY["Kenaciviññeyyadukaṃ"] = DYAD_MY["Kenaciviññeyyadukaṃ"] + [
    ("nakenaci viññeyy", "တစ်စုံတစ်ခုသော စိတ်ဖြင့် သိနိုင်သည် မဟုတ်သော")]
GOC_MY.update({"Hetugocchaka": "အမြစ်တို့၏ အစု", "Cūḷantaraduka": "ကြားညှပ် နှစ်မျိုးတွဲ အစုငယ်",
               "Mahantaraduka": "ကြားညှပ် နှစ်မျိုးတွဲ အစုကြီး", "Piṭṭhiduka": "နောက်ဆုံး နှစ်မျိုးတွဲများ"})
PADA_MY = "ပုဒ်"
''')
assert "PADA_MY" in s

# term regexes: nakenaci
s = s.replace('''DYAD_PI["Pītisahagatādidukaṃ"] = DYAD_PI["Pītisahagatadukaṃ"] + DYAD_PI["Sukhasahagatadukaṃ"]
''', '''DYAD_PI["Pītisahagatādidukaṃ"] = DYAD_PI["Pītisahagatadukaṃ"] + DYAD_PI["Sukhasahagatadukaṃ"]
DYAD_PI["Kenaciviññeyyadukaṃ"] = DYAD_PI["Kenaciviññeyyadukaṃ"] + [_ci("nakenaci viññeyy") + _W]
''')

# parts / terms / names: replace the block from TERM_SPECIAL to the N: numbers section
i0 = s.index("# Pāli spots the term regexes cannot see")
i1 = s.index("# ----------------------------------------------------------------------------- N: numbers")
NEW_TERMS = r'''# Pāli spots the term regexes cannot see: (regex, [(dyad head, dyad term index, triad stem)]) (slips, logged)
TERM_SPECIAL = []
PART_RE = re.compile(r"^(#{5,6}) (\d+ ?-\d+\.?) (\S+?)ttika-(\S+?)dukaṃ \^")
SUB_RE = re.compile(r"^(#{6,7}) (\*?)(\d+-\d+-\d+\.) (\S+?)ttika-(\S+?)ādidukāni(\*?) \^")
# the group headings: the dyads whose terms the part uses (typed here again), the dyad that names the group
SUB_DY = {"saññojan": (("Parāmāsadukaṃ",), "Saññojanadukaṃ"),
          "cittasampayutt": (("Cittasampayuttadukaṃ", "Cittasaṃsaṭṭhadukaṃ", "Cittasamuṭṭhānadukaṃ",
                              "Cittasahabhūdukaṃ", "Cittānuparivattidukaṃ", "Cittasaṃsaṭṭhasamuṭṭhānadukaṃ",
                              "Cittasaṃsaṭṭhasamuṭṭhānasahabhūdukaṃ", "Cittasaṃsaṭṭhasamuṭṭhānānuparivattidukaṃ"),
                             "Cittasampayuttadukaṃ"),
          "upādān": (("Upādānadukaṃ",), "Upādānadukaṃ"),
          "pītisahagat": (("Pītisahagatadukaṃ", "Sukhasahagatadukaṃ", "Upekkhāsahagatadukaṃ"), "Pītisahagatadukaṃ")}
# 4-17: the 1-19 dyad's first term under the 1-18 heading (the Pāli's layout)
EXTRA_DY = {("4-17", "1-18."): ("Āsavavippayuttasāsavadukaṃ",)}
ADI_MY = "စသည်"


def parts_of(name):
    """the active (triad head, dyad heads) of each non-empty Pāli line"""
    cur, out = None, []
    for l in nonempty(PALI / name):
        m = PART_RE.match(l)
        if m:
            cur = (m[3] + "ttikaṃ", (m[4][0].upper() + m[4][1:] + "dukaṃ",) + EXTRA_DY.get((name[:4], m[2]), ()))
        m = SUB_RE.match(l)
        if m:
            cur = (m[4] + "ttikaṃ", SUB_DY[m[5]][0])
        out.append(cur)
    first = next(p for p in out if p)
    return [p or first for p in out]


def pali_terms(line, part):
    th, dhs = part
    s = strip_var(ID.sub("", line))
    found = []
    for rx, items in TERM_SPECIAL:
        for m in re.finditer(rx, s):
            for j, it in enumerate(items):
                found.append((m.start() + j / 10, m.end(), it))
    stems = sorted((st for st, _ in TRIAD_MY[th]), key=len, reverse=True)
    for dh in dhs:
        for di, drx in enumerate(DYAD_PI[dh]):
            for st in stems:
                for m in re.finditer(r"(?<![\wāīūṃṅñṭḍṇḷ])" + _ci(st) + _W + " (?:" + drx + r")(?![\wāīūṃṅñṭḍṇḷ])", s):
                    if not any(a <= m.start() < b for a, b, _ in found):
                        found.append((m.start(), m.end(), (dh, di, st)))
    found.sort()
    return [k for _, _, k in found]


def my_terms(line, part):
    th, dhs = part
    vals = {}
    for dh in dhs:
        for di, (_, dv) in enumerate(DYAD_MY[dh]):
            for st, tv in TRIAD_MY[th]:
                vals[f"{tv}၊ {dv}"] = (dh, di, st)
    rx = re.compile("(" + "|".join(re.escape(v) for v in sorted(vals, key=len, reverse=True)) + ")")
    return [vals[m.group(1)] for m in rx.finditer(strip_var(ID.sub("", line)))]


def _pada(dterm):
    if dterm == "hetusampnahetudk":
        return "Hetusampayuttanahetu"
    s = (dterm[:-2] if dterm.endswith("dk") else dterm).replace(" ", "")
    s = s[0].upper() + s[1:]
    return s if s.endswith(("u", "a")) else s + "a"


def names_ok(p, m, part):
    """the triad-dyad heading, the group headings, the pada headings and the colophons carry the right names (None:
    not such a line)"""
    th, dhs = part
    mb = m.split(" ^")[0]
    mh = PART_RE.match(p)
    if mh:
        want = (f"{mh[1]} {mh[2]} {TIKA_MY[mh[3] + 'ttikaṃ']}နှင့် "
                f"{DUKA_MY[mh[4][0].upper() + mh[4][1:] + 'dukaṃ']}")
        return mb == want
    ms = SUB_RE.match(p)
    if ms:
        want = (f"{ms[1]} {ms[2]}{ms[3]} {TIKA_MY[ms[4] + 'ttikaṃ']}နှင့် {DUKA_MY[SUB_DY[ms[5]][1]]} {ADI_MY}{ms[6]}")
        return mb == want
    mp = re.match(r"^(?:#+ )?(\*?)(\S+?)pada(ṃ|paccayacatukkaṃ)(\*?)(\.?)(?: \^|$)", p)
    if mp:
        for dh in dhs:
            for (dterm, dv) in DYAD_MY[dh]:
                if mp[2] == _pada(dterm):
                    body = mb.split(" ", 1)[1] if p.startswith("#") else mb
                    tail = "" if mp[3] == "ṃ" else "၏ အကြောင်း လေးမျိုးတွဲ"
                    return body == f"{mp[1]}{dv} {PADA_MY}{tail}{mp[4]}{'။' if mp[5] else ''}"
        return False
    mc = re.search(r"(\S+?)ttika(\S+?)(duka|gocchaka)ṃ niṭṭhitaṃ\.", p)
    if mc:
        x = mc[2][0].upper() + mc[2][1:]
        second = DUKA_MY.get(x + "dukaṃ") if mc[3] == "duka" else None
        second = second or GOC_MY.get(x + mc[3])
        return f"“{TIKA_MY[mc[1] + 'ttikaṃ']}နှင့် {second}” ပြီးဆုံးပြီ။" in m
    return None


'''
s = s[:i0] + NEW_TERMS + s[i1:]

# load_make
s = s.replace('''    spec = importlib.util.spec_from_file_location("make_ch4_10_14", HERE / "make_ch4-10-14.py")''',
              '''    spec = importlib.util.spec_from_file_location("make_ch4_15_21", HERE / "make_ch4-15-21.py")''')
assert "make_ch4_15_21" in s
s = s.replace("    for w in (mk.WC, mk.WB, mk.WE):\n        for st, my in CONDS_MY.items():",
              "    for w in (mk.WA, mk.WB, mk.WC, mk.WE):\n        for st, my in CONDS_MY.items():")
s = s.replace("    for w in (mk.WC, mk.WB, mk.WE):\n        wit.update(w.F.WITNESS)",
              "    for w in (mk.WA, mk.WB, mk.WC, mk.WE):\n        wit.update(w.F.WITNESS)")
assert s.count("(mk.WA, mk.WB, mk.WC, mk.WE)") == 2
i0 = s.index("    for k, tab in X.COMBO.items():")
i1 = s.index("    # R: reuse")
s = s[:i0] + '''    for k, tab in mk.TK_COMBO.items():
        for key, val in tab.items():
            stats["T"] += 1
            dh, dt, th, tt = X.COMBO_PALI[key]
            if val != f"{dict(TRIAD_MY[th])[tt]}၊ {dict(DYAD_MY[dh])[dt]}":
                bad.append(("T", "-", 0, f"combined term {key}"))
''' + s[i1:]

# regress: both dukatika groups
i0 = s.index("def regress(mk):")
i1 = s.index("MUT = [")
s = s[:i0] + '''def regress(mk):
    """the dukatika chapters 4-02 … 4-09 (make_ch4-02-09) and 4-10 … 4-14 (make_ch4-10-14), regenerated in memory with
    this group's extensions loaded, equal the files on disk (this group's additions change nothing there)"""
    bad = 0
    X, Y = mk.X, mk.Y
    for w in (mk.WA, mk.WB, mk.WC, mk.WE):
        w.F.DEV = False
    disk = ROOT / "AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters"
    for n in MODEL + MODEL2:
        txt = X.translate(n) if n in MODEL else Y.translate(n)
        same = txt == (disk / n).read_text(encoding="utf-8")
        print(f"regress {n}: {'identical' if same else 'DIFFERS'}")
        bad += not same
    return bad


''' + s[i1:]

# mutations
i0 = s.index("MUT = [")
i1 = s.index("def mutate():")
s = s[:i0] + '''MUT = [  # (file, old, new, what)
    ("4-15-tikaduka-hetuduka.md", "အမြစ်ဟူသော အကြောင်း၌ သုံးခု၊ အာရုံဟူသော အကြောင်း၌ ကိုးခု",
     "အမြစ်ဟူသော အကြောင်း၌ သုံးခု၊ အာရုံဟူသော အကြောင်း၌ ရှစ်ခု", "count"),
    ("4-15-tikaduka-hetuduka.md", "အကြီးအမှူးဟူသော အကြောင်း မဟုတ်ခြင်း၌ သုံးခု၊ ရှေးဦးစွာ",
     "အကြီးအမှူးဟူသော အကြောင်း၌ သုံးခု၊ ရှေးဦးစွာ", "polarity"),
    ("4-15-tikaduka-hetuduka.md", "ကုသိုလ်၊ အမြစ် ဖြစ်သော သဘောတရားကို မှီ၍ ကုသိုလ်၊ အမြစ် ဖြစ်သော",
     "ကုသိုလ်၊ အမြစ် မဟုတ်သော သဘောတရားကို မှီ၍ ကုသိုလ်၊ အမြစ် ဖြစ်သော", "dyad term"),
    ("4-15-tikaduka-hetuduka.md", "အကုသိုလ်၊ အမြစ် ဖြစ်သော သဘောတရားကို မှီ၍",
     "ကုသိုလ်၊ အမြစ် ဖြစ်သော သဘောတရားကို မှီ၍", "triad term"),
    ("4-15-tikaduka-hetuduka.md", "အမြစ် ဖြစ်သော၊ ကုသိုလ်", "အမြစ် ဖြစ်သော၊ ကုသိုလ်", "(no-op guard)"),
    ("4-16-tikaduka-sappaccayaduka.md", "ကုသိုလ်၊ အကြောင်း ရှိသော သဘောတရားကို မှီ၍ ကုသိုလ်၊ အကြောင်း ရှိသော "
     "သဘောတရားသည် အမြစ်ဟူသော", "ကုသိုလ်၊ အကြောင်း ရှိသော သဘောတရားကို မှီ၍ ကုသိုလ်၊ အကြောင်း ရှိသော "
     "သဘောတရားသည် အာရုံဟူသော", "condition"),
    ("4-17-tikaduka-asavaduka.md", "။ (3)\\n", "။ (2)\\n", "digits"),
    ("4-15-tikaduka-hetuduka.md", "1-1. ကုသိုလ် သုံးမျိုးတွဲနှင့် အမြစ် နှစ်မျိုးတွဲ",
     "1-1. အမြစ် နှစ်မျိုးတွဲနှင့် ကုသိုလ် သုံးမျိုးတွဲ", "part name order"),
    ("4-18-tikaduka-sarammanaduka.md", "ကုသိုလ်၊ အာရုံ ရှိသော", "ကုသိုလ်၊ အာရုံ မရှိသော", "C world term"),
    ("4-19-tikaduka-kilesaduka.md", "အကုသိုလ်၊ ကိလေသာ ဖြစ်သော", "အကုသိုလ်၊ ကိလေသာ မဟုတ်သော", "E world term"),
    ("4-21-tikaduka-sauttaraduka.md", "ပဋိပက္ခ မရှိသော သဘောတရား", "ပဋိပက္ခ ရှိသော သဘောတရား", "E world term 2"),
    ("4-16-tikaduka-sappaccayaduka.md", "စိတ်ဖြင့် သိနိုင်သည် မဟုတ်သော", "စိတ်ဖြင့် မသိနိုင်သော", "as-written term"),
    ("4-15-tikaduka-hetuduka.md", "###### အမြစ် မဟုတ်သော ပုဒ်", "###### အမြစ် ဖြစ်သော ပုဒ်", "pada heading"),
    ("4-21-tikaduka-sauttaraduka.md", "စတုတ္ထ အပိုင်း", "တတိယ အပိုင်း", "colophon"),
]
MUT = [m for m in MUT if m[1] != m[2]]


''' + s[i1:]
s = s.replace('tmp = HERE / "chk-mut-ch4-10-14"', 'tmp = HERE / "chk-mut-ch4-15-21"')
s = s.replace('str(HERE / "check_ch4-10-14.py")', 'str(HERE / "check_ch4-15-21.py")')
s = s.replace('tmp = HERE / "chk-pe" / "ch4-10-14"', 'tmp = HERE / "chk-pe" / "ch4-15-21"')
assert "check_ch4-10-14" not in s.split('"""', 2)[2], [l for l in s.split("\n") if "4-10-14" in l][:5]
(HERE / "check_ch4-15-21.py").write_text(s, encoding="utf-8")
print("written", len(s))
