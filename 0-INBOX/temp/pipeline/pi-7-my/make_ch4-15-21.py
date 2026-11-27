"""Burmese zero-shot of pi-7 4-15 … 4-21, the TIKADUKA chapters of the Paṭṭhāna («အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ»):
a triad term combined with a dyad term on one noun («kusalaṃ hetuṃ dhammaṃ paṭicca …»), the mirror of the dukatika
chapters, from the Pāli only.

usage: python3 -I -X utf8 make_ch4-15-21.py [chapter ...] [--dev] [--slips] [--new] [--out DIR] [--dump]
  (no flag)  translate the chapters and write them; stops on the first unmatched sentence (nothing is guessed).
  --dev      do not stop: list every unmatched skeleton with its count in chk-ch4-15-21/dev.txt (nothing written).
  --dump     print the combined-term table (triad term + dyad term = Burmese) and stop.
  --new      translate without writing and print every new string («Pāli = Burmese») and the readings.

Method (read-only imports; no main block of another script runs; no file of the sample or of another group is edited
or written):
  * the finished dukatika group make_ch4-10-14.py is IMPORTED as Y (it imports the model make_ch4-02-09.py as X):
    all the dyads of worlds A (3-01 … 3-06), B (3-07, 3-08, 3-10), C (3-09) and E (4-01), the triads, the names,
    the note pieces and the dyad chapters' engines are used as they are, extended in memory;
  * the combined term is built in the Pāli order of the tikaduka: «<triad term> <dyad term>» is rewritten into ONE
    synthetic a-stem term (the case of the triad word; a closing «-ñca» of a one-word dyad term = the conjunct)
    whose Burmese is the two qualifiers stacked «<triad term>၊ <dyad term>» (the dukatika pattern «A၊ B N», here
    with the terms in the Pāli order); then the dyad chapters' engine translates the part with that table only;
  * the part names follow the Pāli order: «<triad name>နှင့် <dyad name>»; pada headings «<dyad term> ပုဒ်».
Every new string is logged in notes-ch4-15-21.md.
"""
import collections
import importlib.util
import pathlib
import re
import sys

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
ROOT = HERE.parents[3]
PALI = ROOT / "AI_translation/pali/pi-7_split_chapters"
OUT = ROOT / "AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters"
NAMES = ["4-15-tikaduka-hetuduka.md", "4-16-tikaduka-sappaccayaduka.md", "4-17-tikaduka-asavaduka.md",
         "4-18-tikaduka-sarammanaduka.md", "4-19-tikaduka-kilesaduka.md",
         "4-20-tikaduka-dassanenapahatabbaduka.md", "4-21-tikaduka-sauttaraduka.md"]
CHK = HERE / "chk-ch4-15-21"
WCH = r"[\wāīūṃṅñṭḍṇḷ]"
_NB = r"(?!" + WCH + ")"
_PB = r"(?<!" + WCH + ")"


def _load(name, fn):
    spec = importlib.util.spec_from_file_location(name, HERE / fn)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


Y = _load("y_ch41014", "make_ch4-10-14.py")        # the finished dukatika group (its main() does not run)
X = Y.X                                             # the model make_ch4-02-09 (as Y extended it)
WA, WB, WC, WE = X.WA, X.WB, Y.WC, Y.WE
C, END, PE = X.C, X.END, X.PE
WORLD_OF = {"4-15": WA, "4-16": WA, "4-17": WA, "4-18": WC, "4-19": WE, "4-20": WE, "4-21": WE}
DS = X.DYAD_SURF
DV = X.dyad_value

NEW = collections.OrderedDict()     # every new string of this script: Pāli -> Burmese
SLIPS = set()
READ_LOG = set()


def new(pali, my):
    if pali in NEW:
        assert NEW[pali] == my, (pali, NEW[pali], my)
    NEW.setdefault(pali, my)
    return my


# ===================================================================================== triads: short headings
# «Dassanattikaṃ» = Dassanenapahātabbattikaṃ, «Dassanahetuttikaṃ» = Dassanenapahātabbahetukattikaṃ (4-21; the same
# triads, their terms and names; Y already reads «Sanidassanattikaṃ» / «Micchattattikaṃ»)
for _a, _b in (("Dassanattikaṃ", "Dassanenapahātabbattikaṃ"),
               ("Dassanahetuttikaṃ", "Dassanenapahātabbahetukattikaṃ")):
    X.TRIADS[_a] = X.TRIADS[_b]
    X.TIKA_NAME[_a] = X.TIKA_NAME[_b]
    READ_LOG.add(f"triad heading «{_a}» = {_b} (its terms and name)")

# ===================================================================================== extra dyad terms
# 4-16 ^7-50-48 «nakenaci viññeyyaṃ» (for the Mātikā's «kenaci naviññeyyaṃ»): translated as written, the «na-X» rule
# of 5-01 … 5-04 («…သော» -> «…သည် မဟုတ်သော»; 5-02 / 5-04 «nakenaci viññeyy-» = this Burmese)
_KV = DV("Kenaciviññeyyadukaṃ", "kenaci viññeyy")
assert _KV.endswith("သော")
NAKENACI = new("nakenaci viññeyyo (dyad term, as written; = 5-02 / 5-04)", _KV[:-len("သော")] + f"သည် {WA.F.NOT}သော")
assert NAKENACI == "တစ်စုံတစ်ခုသော စိတ်ဖြင့် သိနိုင်သည် မဟုတ်သော"      # notes-ch5-01-04 «nakenaci viññeyy-»
WA.DYADS["kenaci"]["nakenaci viññeyy"] = NAKENACI
DS["Kenaciviññeyyadukaṃ"].append(("kenaci", "nakenaci viññeyy", X._ci("nakenaci viññeyy") + X._EA))
SLIPS.add("4-16 ^7-50-48: «nakenaci viññeyya» for «kenaci naviññeyya» (translated as written)")


def TRI(tt):
    return X.TRIADS["Kusalattikaṃ"][tt]


# ===================================================================================== counts above twenty-four
# 4-15 (the vitakka / pīti triads with the hetu dyad): «ekavīsa … sattatiṃsa»; the words of make_ch2-01-02 (NUM_ADD,
# its Burmese «…ခု»), added to the counting tables of every world as that group adds them to its own
NUM_ADD = X.L.M.NUM_ADD


def setup_counts():
    for w in (WA, WB, WC, WE):
        for mod in (w.F, w.FG):
            for _w, (_n, _my) in NUM_ADD.items():
                v = _my + "ခု"
                assert mod.COUNT.get(_w, v) == v, _w
                mod.COUNT[_w] = v
                mod.COUNT_VAL[_w] = _n
                mod.SKF.setdefault(_w, v)
            mod._CNT_ALT = "|".join(sorted(mod.COUNT, key=len, reverse=True))
            mod.COUNT_RE = re.compile(r"(?<![\wāīūṃṅñṭḍṇḷ])(?P<neg>[Nn]a|[Nn]o)?(?P<loc>(?i:" + mod._LOC_ALT
                                      + r")) (?P<num>" + mod._CNT_ALT + r")(?![\wāīūṃṅñṭḍṇḷ])")
        g = w.G
        if hasattr(g, "SKF"):
            for _w, (_n, _my) in NUM_ADD.items():
                g.SKF.setdefault(_w, _my + "ခု")
        # the term endings of 1-03 … 1-05 exclude «-e <count>» («vipāke ekavīsa» is the condition, not the term
        # vipāka): the new counts join that exclusion, as make_ch2-01-02 does it
        nums2 = "|".join(sorted(set(g._NUMS.split("|")) | set(NUM_ADD), key=len, reverse=True))
        for mod in (w.F, w.FG):
            ch = False
            for tri, rx in list(mod.TRIAD_END.items()):
                if g._NUMS in rx:
                    mod.TRIAD_END[tri] = rx.replace(g._NUMS, nums2)
                    ch = True
            if ch:
                mod.rebuild()


setup_counts()

# ===================================================================================== note pieces (this group)
_PIECE0 = X.piece
_SADISA_RX = re.compile(r"(kusala|akusala|abyākata)(\w+?)sadisaṃ")
_TT = {"kusala": "kusal", "akusala": "akusal", "abyākata": "abyākat"}


def _vara_names(s, lst):
    """«Xvārampi… Yvārampi» -> «X… Y» (the names, the source's separators)"""
    return X.vara_list(s, lst).replace("လည်း", "")       # the model's list frame without the «-pi» particle


def piece(s, p):
    r = _PIECE0(s, p)
    if r is not None:
        return r
    n = Y.NS(s)
    F = s.w.F
    if p == "kenaciviññeyyasadisaṃ":           # like the term kenaci viññeyya (as X «sappaccayasadisaṃ …»)
        return new(p, f"{DV('Kenaciviññeyyadukaṃ', 'kenaci viññeyy')} {s.DH}{s.SADISA}")
    if p == "āsavagocchakasadisaṃ":
        return new(p, f"{s.GN['asava']}{s.SADISA}")
    if p == "upādānagocchakaṃ vitthāretabbaṃ":   # (5-01 … 5-04 «sabbattha gocchakaṃ vitthāretabbaṃ»)
        return new(p, f"{X.GOC_NAME['Upādānagocchaka']}ကို {s.VITTH}")
    if p == "aññamaññanissayapaccayā sahajātapaccayasadisā":
        return new(p, f"{F._join_and([s.cname('aññamañña'), s.cname('nissaya')])}တို့သည် "
                      f"{s.cname('sahajāta')}နှင့် {s.SADISA_PL}")
    m = re.fullmatch(r"yathā (\w+?)ttika(\w+?)dukaṃ, evaṃ vitthāretabbaṃ", p)
    if m:
        th, dh = m[1][0].upper() + m[1][1:] + "ttikaṃ", m[2][0].upper() + m[2][1:] + "dukaṃ"
        if th in X.TRIADS and dh in DS:
            return new(p, f"{part_name(th, dh)}{n.KAYYA} {s.EVAM} {s.VITTH}")
    m = _SADISA_RX.fullmatch(p)
    if m:                                       # «kusalasavitakkasadisaṃ»: like the combined term (as a noun)
        for h, items in DS.items():
            if Y.dyad_world_of(h) is not s.w:
                continue
            for _, tk, _ in items:
                if m[2] in (tk, tk + "a"):
                    return new(p, f"{TRI(_TT[m[1]])}{C} {DV(h, tk)} {s.DH}{s.SADISA}")
    # «Yathā sahajātavārampi… sampayuttavārampi evaṃ vitthāretabbaṃ» (4-15 ^7-49-79): the vāras as the model of the
    # comparison («…တို့ကဲ့သို့ ထိုနည်းတူ»; their «-pi» is the comparison's, not rendered apart; logged)
    m = re.fullmatch("yathā (" + X._VL + r")evaṃ vitthāretabbaṃ", p)
    if m and "vārepi" not in m[1]:
        READ_LOG.add("4-15 ^7-49-79 «Yathā sahajātavārampi… sampayuttavārampi evaṃ vitthāretabbaṃ»: the vāras as "
                     "the model («…တို့ကဲ့သို့ ထိုနည်းတူ အကျယ် ချဲ့ရမည်»)")
        return new(p, f"{_vara_names(s, m[1])}တို့{n.KAYYA} {s.EVAM} {s.VITTH}")
    # vāra lists with this group's predicates (the model's list frame)
    m = re.fullmatch("(" + X._VL + r")(.+)", p)
    if m:
        lst, pred = m[1], m[2]
        loc = "vārepi" in lst
        if all(("epi" in x[1]) == loc for x in X.VARA_RE.findall(lst)):
            L_ = X.vara_list(s, lst, obj=not loc and "vitthāret" in pred)      # harmonise H20
            vitthr = WA.D.NEW["vitthāro"]                                   # «အကျယ် ချဲ့ခြင်း» (3-01 … 3-02)
            nom = {"evaṃ vitthāretabbaṃ": f"ဤသို့ {s.VITTH}"}     # harmonise H14: bare «evaṃ» «ဤသို့» (= 5-01 … 5-04)
            locp = {"sabbattha vitthāro": f"{s.SABB} {vitthr}",                  # = 5-01 … 5-04
                    "tattakāva pañhā": n.TATTAKA}                               # tattakā + eva (= Y «tattakā eva»)
            r = (locp if loc else nom).get(pred)
            if r:
                return new(p, f"{L_} {r}")
    return None


X.piece = piece

# ===================================================================================== combined terms (tikaduka)
TK_COMBO = {}        # (triad head, dyad heads) -> {synthetic key: Burmese}
TK_RE = {}           # (triad head, dyad heads) -> (regex, {group: (triad term, dyad term, key, two-member dyad)})
_T_END = {"a": "(?P<e>o|aṃ|añca|assa|ā|ānaṃ|ānañca|e|ena)",
          "i": "(?P<e>issa|iṃ|iñca|ino|īnaṃ|ī|i)",
          "d": "(?P<e>ā)"}


def tk_combo(th, dhs):
    dhs = tuple(dhs)
    if (th, dhs) in TK_COMBO:
        return TK_COMBO[(th, dhs)]
    tab, groups, alts = {}, {}, []
    rows = []
    for dh in dhs:
        for dk, dterm, dsurf in DS[dh]:
            dval = DV(dh, dterm)
            for tterm, tval in X.TRIADS[th].items():
                rows.append((len(tterm), dh, dterm, dsurf, dval, tterm, tval))
    for _, dh, dterm, dsurf, dval, tterm, tval in sorted(rows, key=lambda r: -r[0]):
        key = X._skey(X._N[0])
        X._N[0] += 1
        g = f"g{len(groups)}"
        groups[g] = (tterm, dterm, key, "ceva" in dsurf)
        tab[key] = f"{tval}{C} {dval}"
        X.COMBO_PALI[key] = (dh, dterm, th, tterm)
        cls = X.STEM_CLASS.get(tterm, "a")
        tend = _T_END[cls].replace("(?P<e>", f"(?P<e{g}>")
        alts.append(f"(?P<{g}>{X._ci(tterm)}{tend} (?P<d{g}>{dsurf}))")
    rx = re.compile(_PB + "(?:" + "|".join(alts) + ")" + _NB)
    TK_COMBO[(th, dhs)] = tab
    TK_RE[(th, dhs)] = (rx, groups)
    return tab


def tk_combine(text, th, dhs):
    tk_combo(th, dhs)
    rx, groups = TK_RE[(th, tuple(dhs))]

    def rep(m):
        g = next(k for k in groups if m.group(k))
        tterm, dterm, key, two = groups[g]
        e = m.group("e" + g)
        dw = m.group("d" + g)
        conj = (not two) and dw.endswith("ñca")
        cls = X.STEM_CLASS.get(tterm, "a")
        if cls == "i":
            e = X._I2A[e]
        elif cls == "d":           # «bahiddhā»: the case of the dyad word
            dw0 = dw[:-len("ñca")] + "ṃ" if conj else dw
            e = next(a for s, a in X._DYCASE if dw0.endswith(s))
        if conj:
            assert e in ("aṃ", "ānaṃ"), (m[0], e)
            e = {"aṃ": "añca", "ānaṃ": "ānañca"}[e]
        cap = m.group(g)[0].isupper()
        return (key[0].upper() + key[1:] if cap else key) + e
    return rx.sub(rep, text)


# ===================================================================================== parts and headings
TK_HEAD = re.compile(r"^(#{5,6}) (\d+ ?-\d+\.?) (\S+?)ttika-(\S+?)dukaṃ \^", re.M)
# a group heading inside a chapter («1-58-65. Kusalattika-cittasampayuttādidukāni»): the dyads it names are active
# together in the part it opens (the world of those dyads)
SUB_HEAD = re.compile(r"^(#{6,7}) (\*?)(\d+-\d+-\d+\.) (\S+?)ttika-(\S+?)ādidukāni(\*?) \^", re.M)
SUBS = {   # first dyad word -> (the dyads whose terms the part uses, the dyad that names the group)
    "saññojan": (["Parāmāsadukaṃ"], "Saññojanadukaṃ"),
    "cittasampayutt": (["Cittasampayuttadukaṃ", "Cittasaṃsaṭṭhadukaṃ", "Cittasamuṭṭhānadukaṃ", "Cittasahabhūdukaṃ",
                         "Cittānuparivattidukaṃ", "Cittasaṃsaṭṭhasamuṭṭhānadukaṃ",
                         "Cittasaṃsaṭṭhasamuṭṭhānasahabhūdukaṃ", "Cittasaṃsaṭṭhasamuṭṭhānānuparivattidukaṃ"],
                        "Cittasampayuttadukaṃ"),
    "upādān": (["Upādānadukaṃ"], "Upādānadukaṃ"),
    "pītisahagat": (["Pītisahagatadukaṃ", "Sukhasahagatadukaṃ", "Upekkhāsahagatadukaṃ"], "Pītisahagatadukaṃ"),
}
# 4-17: under the heading 1-18 (āsava + āsavasampayutta) the Pāli also has the first term of the next dyad
# («āsavavippayuttaṃ sāsavaṃ», 1-19; its own heading follows with the other term): both dyads active in that part
EXTRA = {("4-17", "1-18."): ["Āsavavippayuttasāsavadukaṃ"]}


class Part:
    def __init__(self, th, dhs, num, text, world, name, sub=None):
        self.th, self.dhs, self.num, self.text, self.w, self.name, self.sub = th, dhs, num, text, world, name, sub


def parts_of(src, ch="4-15"):
    """[Part]: the chapter cut before each triad-dyad heading and each group heading"""
    ms = sorted(list(TK_HEAD.finditer(src)) + list(SUB_HEAD.finditer(src)), key=lambda m: m.start())
    if not ms:
        raise SystemExit("no triad-dyad heading")
    out = []
    for i, m in enumerate(ms):
        s = 0 if i == 0 else m.start()
        e = ms[i + 1].start() if i + 1 < len(ms) else len(src)
        if m.re is TK_HEAD:
            th = m[3] + "ttikaṃ"
            dh = m[4][0].upper() + m[4][1:] + "dukaṃ"
            if dh not in DS or th not in X.TRIADS:
                raise SystemExit(f"unknown part {th} / {dh}")
            dhs = [dh] + EXTRA.get((ch, m[2]), [])
            for x in dhs[1:]:
                READ_LOG.add(f"{ch} part {m[2]} {th[:-1]}-{dh}: the terms of {x} too (the Pāli has them there)")
            out.append(Part(th, dhs, m[2], src[s:e], Y.dyad_world_of(dh), dh))
        else:
            th = m[4] + "ttikaṃ"
            dhs, nh = SUBS[m[5]]
            out.append(Part(th, dhs, m[3], src[s:e], Y.dyad_world_of(dhs[0]), nh, sub=m))
        for x in out[-1].dhs:
            assert Y.dyad_world_of(x) is out[-1].w, (x, out[-1].dhs)
    return out


def part_name(th, dh):
    """«Xttika-Ydukaṃ» = «<triad name>နှင့် <dyad name>» (the Pāli order)"""
    return f"{X.TIKA_NAME[th]}နှင့် {X.DUKA_NAME[dh]}"


PADA_ALIAS = {"hetusampnahetudk": "Hetusampayuttanahetupadaṃ"}     # «hetusampayutto ceva na ca hetu»


def _dpada_key(dterm):
    """the pada heading of a dyad term («Hetupadaṃ», «Sahetukanahetupadaṃ», «Nahetuahetukapadaṃ»)"""
    if dterm in PADA_ALIAS:
        return PADA_ALIAS[dterm]
    s = dterm[:-2] if dterm.endswith("dk") else dterm
    s = s.replace(" ", "")
    s = s[0].upper() + s[1:]
    return s + ("padaṃ" if s.endswith(("u", "a")) else "apadaṃ")


# the gocchaka names of the colophons «<triad>Xgocchakaṃ niṭṭhitaṃ.» (the finished groups' names)
X.GOC_NAME.setdefault("Hetugocchaka", WA.D.GOCCHAKA["Hetugocchakaṃ"])
X.GOC_NAME.setdefault("Cūḷantaraduka", WA.D.GOCCHAKA["Cūḷantaradukaṃ"])
# «*Paccanīyaṃ –nahetupaccayo*» (no space after the dash, 4-15 / 4-16): the heading «Paccanīyaṃ – X» of the module
DASH_HEADS = ("*Paccanīyaṃ –nahetupaccayo*", "*Paccanīyaṃ –naadhipatipaccayo*")
# condition headings of the group without hyphens / with three conditions: the conditions joined (as Y
# «*Hetu-ārammaṇa-adhipatipaccayā*»); no hyphen = the hyphenated heading (logged)
COND_HEADS = {"*Hetu-ārammaṇa-adhipatipaccayā*": ("hetu", "ārammaṇa", "adhipati"),
              "*Hetu-ārammaṇa-anantarapaccayā*": ("hetu", "ārammaṇa", "anantara"),
              "*Ārammaṇa-adhipati-anantarapaccayā*": ("ārammaṇa", "adhipati", "anantara")}
NOHYPH = {"*Hetuārammaṇapaccayā*": "*Hetu-ārammaṇapaccayā*",
          "*Hetusahajātapaccayādi*": ("hetu", "sahajāta")}
E4 = Y.E4
CATUTTHO = E4.HL_ADD["(Catuttho bhāgo)"][1:-1]                     # «စတုတ္ထ အပိုင်း» (4-01)


def heading_lines(w, parts):
    F = w.F
    hl = X.heading_lines(w, [])          # the model's general headings (1-6. Paṭiccavārādi, *Hetu-ārammaṇapaccayādi* …)
    hl.pop("Dhammānulome dukatikapaṭṭhānaṃ", None)
    hl["Paccayacatukkaṃ"] = Y.new("Paccayacatukkaṃ (heading)", f"{F.PACCAYA} {F.GROUP['catukka']}")   # = 4-10 … 4-14
    for h in DASH_HEADS:
        hl[h] = F.heading(h.replace("–", "– "))
        READ_LOG.add(f"heading «{h}» (no space after the dash) = «{h.replace('–', '– ')}»")
    for h, conds in COND_HEADS.items():
        hl[h] = new(h, "*" + F._join_and([F.cond(c, "n") for c in conds]) + "*")
    for h, v in NOHYPH.items():
        if isinstance(v, str):
            hl[h] = F.heading(v)
        else:
            hl[h] = new(h, "*" + F._join_and([F.cond(c, "n") for c in v]) + f" {F.ADI}*")
        READ_LOG.add(f"heading «{h}» (no hyphen): the conditions as named")
    hl["Dhammānulome tikadukapaṭṭhānaṃ"] = new("Dhammānulome tikadukapaṭṭhānaṃ",
                                              f"{F.HEAD['Dhammānulome']} {F.TIKA}နှင့် {F.DUKA}တို့၏ {F.TITLE}")
    hl["Dhammānulome tikadukapaṭṭhānaṃ niṭṭhitaṃ."] = F.finished(hl["Dhammānulome tikadukapaṭṭhānaṃ"])
    hl["Catuttho bhāgo niṭṭhito."] = new("Catuttho bhāgo niṭṭhito.", f"{CATUTTHO} {F.DONE}{END}")   # = 3-10 «Tatiyo …»
    pv = f"{F.HEAD['Paṭiccavāro']} {F.ADI}"
    hl["1-6. Paṭiccavārādi"] = f"1-6. {pv}"
    hl["1-7. Paṭiccavārādi"] = f"1-7. {pv}"
    hl["*Paccayacatukkaṃ*"] = f"*{F.PACCAYA} {F.GROUP['catukka']}*"
    for g, gn in X.GOC_NAME.items():
        for th in {p.th for p in parts}:
            hl[f"{th[:-1]}{g[0].lower()}{g[1:]}ṃ niṭṭhitaṃ."] = F.finished(f"{X.TIKA_NAME[th]}နှင့် {gn}")
    for p in parts:
        th, num = p.th, p.num
        if p.sub is None:
            dh = p.dhs[0]
            name = part_name(th, dh)
            hl[f"{num} {th[:-1]}-{dh[0].lower()}{dh[1:]}"] = f"{num} {name}"
            new(f"{th[:-1]}-{dh[0].lower()}{dh[1:]}", name)
            hl[f"{th[:-1]}{dh[0].lower()}{dh[1:]} niṭṭhitaṃ."] = F.finished(name)
        else:
            m = p.sub
            name = new(f"{m[4]}ttika-{m[5]}ādidukāni", f"{X.TIKA_NAME[th]}နှင့် {X.DUKA_NAME[p.name]} {F.ADI}")
            hl[f"{m[2]}{num} {m[4]}ttika-{m[5]}ādidukāni{m[6]}"] = f"{m[2]}{num} {name}{m[6]}"
        for dh in p.dhs:
            for _, dterm, _ in DS[dh]:
                k = _dpada_key(dterm)
                v = f"{DV(dh, dterm)} {X.PADA}"
                hl.setdefault(k, v)
                hl.setdefault(f"*{k}*", f"*{v}*")
                hl.setdefault(f"{k}.", f"{v}{END}")                     # 4-15 ^7-49-84 «Nahetupadaṃ.» (a line)
                hl.setdefault(f"*{k[:-1]}paccayacatukkaṃ*", new(        # «*Nahetupadapaccayacatukkaṃ*»
                    f"*{k[:-1]}paccayacatukkaṃ*", f"*{v}၏ {F.PACCAYA} {F.GROUP['catukka']}*"))
    return hl


# ===================================================================================== hand lines, slips
SLIP_FIX = {
    "upekkhāsahagato nahetudhammo": "upekkhāsahagato nahetu dhammo",          # 4-15 ^7-49-? (glued)
    "Hetuyā ekaṃ, āmammaṇe ekaṃ": "Hetuyā ekaṃ, ārammaṇe ekaṃ",                # 4-17
    "paṭiccavārasadisaṃ vitthārebbaṃ": "paṭiccavārasadisaṃ vitthāretabbaṃ",    # 4-15 ^7-49-141
    "adhipatiyā pañca…pe. … avigate tīṇi": "adhipatiyā pañca…pe… avigate tīṇi",   # 4-15 (POSTFIX keeps 2 «…»)
}
# the Burmese of a line read in another form put back to the Pāli's marks (Pāli line part, Burmese a -> b)
POSTFIX = [("adhipatiyā pañca…pe. … avigate tīṇi", "ငါးခု… ", "ငါးခု… … ")]


def _hand_4_17_1(w):
    """4-17 ^7-51-34 line 1: «Akusalaṃ saññojanaṃ dhammaṃ paṭicca…pe… akusalaṃ ganthaṃ… oghaṃ… yogaṃ… nīvaraṇaṃ….»
    (the cluster terms, each the dyad's first term; «oghaṃ … nīvaraṇaṃ» without the triad word: as written)"""
    s = X.S(w)
    ak = TRI("akusal")
    sj, gt = DV("Saññojanadukaṃ", DS["Saññojanadukaṃ"][0][1]), DV("Ganthadukaṃ", DS["Ganthadukaṃ"][0][1])
    og, yg = WA.DYADS["ogha"]["oghdk"], WA.DYADS["yoga"]["yogdk"]
    nv = WB.DYADS["niv1"]["nīvaraṇdk"]
    return (f"{ak}{C} {sj} {s.DH}ကို မှီ၍{PE} {ak}{C} {gt}{PE} {og}{PE} {yg}{PE} {nv}{PE}{END}")


def _hand_4_17_2(w):
    """4-17 ^7-51-34 line 2: the engine's sentence (world B, the parāmāsa dyad) + the note + «Diṭṭhiṃ paṭicca diṭṭhi
    na uppajjati.» (diṭṭhi «အယူ» the module's word; na uppajjati «မဖြစ်ပေါ်» pi-6)"""
    s = X.S(w)
    first = translate_part(w, "Kusalattikaṃ", ["Parāmāsadukaṃ"],
                           "Kusalaṃ noparāmāsaṃ dhammaṃ paṭicca kusalo noparāmāso dhammo uppajjati hetupaccayā.")
    first = first.strip()
    assert "\n" not in first and first.endswith(END), first
    dt = w.F.LEX["diṭṭhi"][0] if "diṭṭhi" in w.F.LEX else None
    dt = dt or "အယူ"
    assert dt == "အယူ", dt
    note = f"({s.GN['asava']}{s.SADISA}{END})"
    last = new("Diṭṭhiṃ paṭicca diṭṭhi na uppajjati.", f"{dt}ကို မှီ၍ {dt}သည် {NUPP}{END}")
    return f"{first} {note} {last}"


NUPP = new("na uppajjati", "မဖြစ်ပေါ်")
GOCCHAKA_N = new("gocchakaṃ (the cluster)", "အစု")                    # = 5-01 … 5-04 (pi-1 «…တို့၏ အစု»)
HAND = {
    "Akusalaṃ saññojanaṃ dhammaṃ paṭicca…pe… akusalaṃ ganthaṃ… oghaṃ… yogaṃ… nīvaraṇaṃ….": _hand_4_17_1,
    "Kusalaṃ noparāmāsaṃ dhammaṃ paṭicca kusalo noparāmāso dhammo uppajjati hetupaccayā. (Āsavagocchakasadisaṃ.) "
    "Diṭṭhiṃ paṭicca diṭṭhi na uppajjati.": _hand_4_17_2,
    "Kusalattike cha gocchakaṃ niṭṭhitaṃ.": lambda w: w.F.finished(new(
        "Kusalattike cha gocchakaṃ", f"{X.TIKA_NAME['Kusalattikaṃ']}၌ {GOCCHAKA_N} "
                                      f"{w.F.COUNT['cha']}")),
}
HAND_MY = {}
_ID = re.compile(r"\s*\^[0-9A-Za-z-]+\s*$")


# ===================================================================================== the run
def tk_prep(w, text, th, dhs):
    lines = text.split("\n")
    for i, l in enumerate(lines):
        m = _ID.search(l)
        body = l[:m.start()] if m else l
        if body in HAND:
            if body not in HAND_MY:
                HAND_MY[body] = HAND[body](w)
                new(body, HAND_MY[body])
            mk = f"⁂h{list(HAND).index(body)}"
            w.F.HLINES[mk] = HAND_MY[body]
            lines[i] = mk + (l[m.start():] if m else "")
    text = "\n".join(lines)
    for a, b in SLIP_FIX.items():
        if a in text:
            SLIPS.add(f"«{a}» read as «{b}»")
            text = text.replace(a, b)
    for a, b in X.SLIP_FIX.items():
        if a in text and a != b:
            X.SLIPS.add(f"«{a}» read as «{b}»")
            text = text.replace(a, b)
    for a, b in X.READ.items():
        if a in text:
            X.READ_LOG.add(f"«{a}» read as «{b}»")
            text = text.replace(a, b)
    X.register_notes(w, text)
    for k in sorted(X.NOTEP[w.tag], key=len, reverse=True):
        text = text.replace(k, f"(⁑k{X._NOTE_IDS[k]})")
    return tk_combine(text, th, dhs)


def translate_part(w, th, dhs, text):
    tab = tk_combo(th, dhs)
    t = tk_prep(w, text, th, dhs)
    X.set_terms(w, tab)
    t = w.D.prep(t, None)
    w.D.chapter_notes(t, None)
    w.FG.translate("")
    if w is WC:
        Y.C3.MY_RUN[0] = True
        Y.C3.gate(True)
    try:
        return w.F.translate(t)
    finally:
        if w is WC:
            Y.C3.MY_RUN[0] = False
            Y.C3.gate(False)


def translate(name):
    src = (PALI / name).read_text(encoding="utf-8-sig")
    parts = parts_of(src, name[:4])
    assert all(p.w is WORLD_OF[name[:4]] or p.sub is not None for p in parts), name
    for w in {p.w for p in parts}:
        w.F.HLINES.update(heading_lines(w, [p for p in parts if p.w is w]))
    txt = "\n".join(translate_part(p.w, p.th, p.dhs, p.text) for p in parts)
    return postfix(src, txt)


def postfix(src, txt):
    """the Burmese of a line read in another form put back to the Pāli's marks (POSTFIX; logged)"""
    pl = [l for l in src.splitlines() if l.strip()]
    ml = txt.split("\n")
    j = 0
    for i, l in enumerate(ml):
        if not l.strip():
            continue
        for p_, a, b in POSTFIX:
            if p_ in pl[j]:
                assert ml[i].count(a) == 1, ml[i]
                ml[i] = ml[i].replace(a, b)
        j += 1
    return "\n".join(ml)


def main():
    global OUT
    if "--out" in sys.argv:
        OUT = pathlib.Path(sys.argv[sys.argv.index("--out") + 1]).resolve()
        del sys.argv[sys.argv.index("--out"):sys.argv.index("--out") + 2]
    names = [a for a in sys.argv[1:] if not a.startswith("--")] or NAMES
    names = [next(n for n in NAMES if n.startswith(a[:4])) for a in names]
    if "--dump" in sys.argv:
        for n in names:
            for p in parts_of((PALI / n).read_text(encoding="utf-8-sig"), n[:4]):
                for k, v in tk_combo(p.th, p.dhs).items():
                    print(n, k, X.COMBO_PALI[k], v, sep="\t")
        return
    dev = "--dev" in sys.argv or "--new" in sys.argv
    worlds = (WA, WB, WC, WE)
    for w in worlds:
        w.F.DEV = dev
        if dev:
            w.F.UNSEEN = X.Counting()
    for n in names:
        txt = translate(n)
        if not dev:
            (OUT / n).write_text(txt, encoding="utf-8")
            print(f"wrote {n}: {sum(1 for l in txt.splitlines() if l)} lines")
        else:
            CHK.mkdir(exist_ok=True)
            (CHK / ("dev-" + n)).write_text(txt, encoding="utf-8")
    if dev:
        CHK.mkdir(exist_ok=True)
        with open(CHK / "dev.txt", "w", encoding="utf-8") as fh:
            tot = 0
            for w in worlds:
                rows = sorted(w.F.UNSEEN.items(), key=lambda kv: -w.F.UNSEEN.cnt[kv[0]])
                tot += len(rows)
                for k, v in rows:
                    fh.write(f"[{w.tag} {w.F.UNSEEN.cnt[k]}] SK: {k}\n    {v}\n")
        print(tot, "unmatched skeletons")
    if "--new" in sys.argv:
        for k, v in list(NEW.items()):
            print(f"{k} = {v}")
        print("readings:", *sorted(READ_LOG | X.READ_LOG | Y.READ_LOG | Y.ABBREV_LOG), sep="\n  ")
    if "--slips" in sys.argv:
        print("slips:", *sorted(SLIPS | X.SLIPS | Y.SLIPS | WA.F.SLIPS | WB.F.SLIPS | WC.F.SLIPS | WE.F.SLIPS),
              sep="\n  ")


if __name__ == "__main__":
    main()
