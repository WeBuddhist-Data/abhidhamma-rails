"""Burmese zero-shot of pi-7 part 5, chapters 5-05 paccanīya-dukatika, 5-06 paccanīya-tikaduka, 5-07 paccanīya-tikatika,
5-08 paccanīya-dukaduka, 5-09 anulomapaccanīya-tika, 5-10 anulomapaccanīya-duka, 5-11 anulomapaccanīya-dukatika,
5-12 anulomapaccanīya-tikaduka («အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ»), from the Pāli only.

usage: python3 -I -X utf8 make_ch5-05-12.py [chapter ...] [--dev] [--slips] [--new] [--out DIR] [--dump]
  (no flag)  translate the chapters and write them; stops on the first unmatched sentence (nothing is guessed).
  --dev      do not stop: list every unmatched skeleton with its count in chk-ch5-05-12/dev.txt (nothing written).
  --dump     print the combined-term table (Pāli chain = Burmese) and stop.

Method (read-only imports; no main block of another script runs; no file of the sample or of another group is edited
or written):
  * the finished part-5 group make_ch5-01-04.py is IMPORTED as M: its atoms (every triad / dyad term of the finished
    groups), its na-X rule, its chain rewriting («A၊ B N» stacking; the pi-1 dyad pairs; coordination), its note
    renderer, its numbers and its two engines (world A = make_ch3-09, world B = make_ch4-01) are used as they are,
    extended in memory only;
  * the dukatika / tikaduka stacking «<dyad term>၊ <triad term>» (and «<triad term>၊ <dyad term>») is the stacking of
    make_ch4-02-09 / make_ch4-10-14 (the same atom values, the same separator); the reuse test of
    check_ch5-05-12.py compares the shared sentences with 4-02 … 4-14 and 5-01 … 5-04.
A chapter is cut at its part headings («##### 1-1. Hetuduka-kusalattikaṃ», 5-09 «##### Kusalattikaṃ», 5-10
«##### Hetudukaṃ» …); every part runs with the atoms of the dyads / triads its heading names (a group word: the whole
group), their «na-» forms and the double negatives. Every new string is logged in notes-ch5-05-12.md.
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
NAMES = ["5-05-paccaniya-dukatika.md", "5-06-paccaniya-tikaduka.md", "5-07-paccaniya-tikatika.md",
         "5-08-paccaniya-dukaduka.md", "5-09-anulomapaccaniya-tika.md", "5-10-anulomapaccaniya-duka.md",
         "5-11-anulomapaccaniya-dukatika.md", "5-12-anulomapaccaniya-tikaduka.md"]
CHK = HERE / "chk-ch5-05-12"


def _load(name, fn):
    spec = importlib.util.spec_from_file_location(name, HERE / fn)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


M = _load("m5_ch50104", "make_ch5-01-04.py")          # the model (its setup() runs on import; its main() does not)
F, WA, WB = M.F, M.WA, M.WB
C, END, PE = M.C, M.END, M.PE
K = WA.K

NEW = collections.OrderedDict()     # every new string of this script: Pāli -> Burmese
SLIPS = []


def new(pali, my):
    if pali in NEW:
        assert NEW[pali] == my, (pali, NEW[pali], my)
    NEW.setdefault(pali, my)
    return my


def hl(pali, my, log=True):
    M.hl(pali, my, log=False)
    if log:
        new(pali, my)


# ===================================================================================== heading words
TITLE, TIKA, DUKA, PADA, ADI = M.TITLE, M.TIKA, M.DUKA, M.PADA, M.ADI
HEAD_ANUL, HEAD_PACC = M.HEAD_ANUL, M.HEAD_PACC
ORDER_N = K.ORDER_N
HEAD_AP = new("Dhammānulomapaccanīye", HEAD_ANUL.replace(K.ORDER_L["anulome"], ORDER_N["anulomapaccanīyaṃ"] + "၌"))
_TT = f"{TIKA}နှင့် {TIKA}တို့၏ {TITLE}"
_DD = f"{DUKA}နှင့် {DUKA}တို့၏ {TITLE}"
_DT = f"{DUKA}နှင့် {TIKA}တို့၏ {TITLE}"            # (4-02 «Dhammānulome dukatikapaṭṭhānaṃ»)
_TD = f"{TIKA}နှင့် {DUKA}တို့၏ {TITLE}"
_T = F.HEAD["Tikapaṭṭhānaṃ"]
_D = M._DUKAP
for _hd, _hm in (("Dhammapaccanīye", HEAD_PACC), ("Dhammānulomapaccanīye", HEAD_AP)):
    for _k, _v in (("tikatika", _TT), ("dukaduka", _DD), ("dukatika", _DT), ("tikaduka", _TD), ("tika", _T),
                   ("duka", _D)):
        hl(f"{_hd} {_k}paṭṭhānaṃ", f"{_hm} {_v}")
        hl(f"{_hd} {_k}paṭṭhānaṃ niṭṭhitaṃ.", f"{_hm} “{_v}” {F.DONE}{END}")
hl("Paccanīyapaṭṭhānaṃ niṭṭhitaṃ.", f"{K.ORDER_L['paccanīye']} “{TITLE}” {F.DONE}{END}")   # (as «Anulomapaṭṭhānaṃ …»)
hl("Tatiyapadaṃ", f"တတိယ {PADA}")
hl("Kusalattikapiṭṭhidukaṃ niṭṭhitaṃ.", F.finished(f"{M.TIKA_NAME['Kusalattikaṃ']}နှင့် {M.GNAME['Piṭṭhidukaṃ']}"))
for _p, (_th, _s) in {"Kusalapadaṃ": ("Kusalattikaṃ", "kusal"), "Akusalapadaṃ": ("Kusalattikaṃ", "akusal"),
                      "Abyākatapadaṃ": ("Kusalattikaṃ", "abyākat")}.items():
    hl(_p, f"{M.TRIADS[_th][_s]} {PADA}", log=False)          # (4-02 «Kusalapadaṃ» «ကုသိုလ် ပုဒ်»)

# ===================================================================================== the families of a part heading
TRIADS_ALL = list(M.TRIADS)
DYADS_ALL = list(M.DYAD_TERMS)
_IDX = {h: i for i, h in enumerate(DYADS_ALL)}


def _dy_from(first, last=None):
    i = _IDX[first]
    j = _IDX[last] if last else len(DYADS_ALL) - 1
    return DYADS_ALL[i:j + 1]


_PITTHI_FIRST = "Dassanenapahātabbadukaṃ"
DGROUP = {   # group word (lower case, as written in the part headings) -> dyad headings
    "cūḷantara": M._CULA, "mahantara": M._MAHA, "piṭṭhi": M._PITTHI,
    "āsava": M._CLUSTER_HEADS["asava"], "upādāna": M._CLUSTER_HEADS["upa"], "kilesa": M._KIL,
    "cha": _dy_from("Saññojanadukaṃ", "Parāmāsavippayuttaparāmaṭṭhadukaṃ"),
    "dvi": M._CLUSTER_HEADS["upa"] + M._KIL,
}
# the names of the group words in the part headings
GNAME = M.GNAME


def _noun(name, kind):
    tail = " " + (DUKA if kind == "d" else TIKA)
    assert name.endswith(tail), name
    return name[:-len(tail)]


def side(word):
    """a heading word -> (kind 'd' / 't', [headings], Burmese name)"""
    w = word
    lw = w[0].lower() + w[1:]
    # triads
    m = re.fullmatch(r"(.+?)ādittikāni", lw)
    if m:
        th = M.triad_of(_TRI_ADI.get(m[1], m[1]) + "ttikaṃ")
        i = TRIADS_ALL.index(th)
        name = f"{_noun(M.TIKA_NAME[th], 't')} {ADI}တို့၏ {TIKA}များ"
        return "t", TRIADS_ALL[i:], name
    if re.fullmatch(r".+ttik(?:aṃ|a)", lw):
        th = M.triad_of(w)
        return "t", [th], M.TIKA_NAME[th]
    # dyads: groups
    m = re.fullmatch(r"(cha|dvi)gocchak(?:āni|a)(dukāni)?", lw)
    if m:
        num = F.COUNT["cha"] if m[1] == "cha" else new("dvi (gocchakāni)", "နှစ်ခု")
        name = f"{M.GOCCHAKA_N} {num}" + (f"၏ {DUKA}များ" if m[2] else "")
        return "d", DGROUP[m[1]], name
    m = re.fullmatch(r"(.+?)(ādi)?gocchak(?:aṃ|a|āni)", lw)
    if m:
        base = m[1] + ("a" if m[2] else "")
        heads = _gocchaka_heads(base, lw)
        if "ādigocchak" in lw:
            noun = GNAME[base[0].upper() + base[1:] + "gocchakaṃ"][:-len(M._GOC_TAIL)]
            return "d", heads, f"{noun} {ADI}တို့၏ {M.GOCCHAKA_N}များ"
        return "d", heads, GNAME[base[0].upper() + base[1:] + "gocchakaṃ"]
    m = re.fullmatch(r"(cūḷantara|mahantara)duk(?:aṃ|a|āni)", lw)
    if m:
        return "d", DGROUP[m[1]], GNAME[m[1][0].upper() + m[1][1:] + "dukaṃ"]
    if lw in ("piṭṭhidukaṃ", "piṭṭhiduka"):
        return "d", DGROUP["piṭṭhi"], GNAME["Piṭṭhidukaṃ"]
    m = re.fullmatch(r"(.+?)ādidukāni", lw)
    if m:
        h = _dyad_head(m[1])
        heads = _adi_heads(h)
        return "d", heads, f"{_noun(M.DUKA_NAME[h], 'd')} {ADI}တို့၏ {DUKA}များ"
    m = re.fullmatch(r"(.+?)dukādi", lw)
    if m:
        h = _dyad_head(m[1])
        return "d", _adi_heads(h), f"{M.DUKA_NAME[h]} {ADI}"
    m = re.fullmatch(r"(.+?)dukāni", lw)
    if m:
        h = _dyad_head(m[1])
        return "d", CLUSTER_OF[h], f"{M.DUKA_NAME[h]}များ"
    m = re.fullmatch(r"(.+?)duk(?:aṃ|a)", lw)
    if m:
        h = _dyad_head(m[1])
        return "d", [h], M.DUKA_NAME[h]
    raise KeyError("heading word " + word)


_TRI_ADI = {"vipāk": "vipāka", "ācayagām": "ācayagāmi", "dassan": "dassana", "hīn": "hīna", "vedan": "vedanā",
            "vitakk": "vitakka"}
_DY_ALIAS = {"hetv": "hetu", "ajjhatta": "ajjhattika", "cittānuparivatt": "cittānuparivatti", "dassan": "dassanenapahātabba"}


def _dyad_head(base):
    base = _DY_ALIAS.get(base, base)
    if base.endswith("a") and base + "dukaṃ" not in [h[0].lower() + h[1:] for h in DYADS_ALL]:
        pass
    for cand in (base, base + "a"):
        h = cand[0].upper() + cand[1:] + "dukaṃ"
        if h in M.DYAD_TERMS:
            return h
    raise KeyError("dyad " + base)


_STARTS = ["Hetudukaṃ", "Sappaccayadukaṃ", "Āsavadukaṃ", "Saññojanadukaṃ", "Ganthadukaṃ", "Oghadukaṃ", "Yogadukaṃ",
           "Nīvaraṇadukaṃ", "Parāmāsadukaṃ", "Upādānadukaṃ", "Kilesadukaṃ", "Sārammaṇadukaṃ", "Dassanenapahātabbadukaṃ"]
CLUSTERS = []                       # the dyad clusters in the order of M.DYAD_TERMS
for _h in DYADS_ALL:
    if _h in _STARTS:
        CLUSTERS.append([])
    CLUSTERS[-1].append(_h)
CLUSTER_OF = {h: c for c in CLUSTERS for h in c}
assert [len(c) for c in CLUSTERS] == [6, 7, 6, 6, 6, 6, 6, 6, 5, 6, 8, 14, 18], [len(c) for c in CLUSTERS]
DGROUP["āsava"] = CLUSTER_OF["Āsavadukaṃ"]
DGROUP["cha"] = sum((CLUSTER_OF[h] for h in _STARTS[3:9]), [])
DGROUP["dvi"] = CLUSTER_OF["Upādānadukaṃ"] + CLUSTER_OF["Kilesadukaṃ"]
DGROUP["mahantara"] = M._MAHA + DGROUP["dvi"]       # (5-08 «1-54-81. Hetuduka-mahantaradukaṃ» runs to the kilesa dyads)


def _adi_heads(h):
    """«X-ādi»: X and the dyads after it in its cluster («Saññojana-ādi»: the six clusters, «Upādāna-ādi»: upādāna
    and kilesa, as the part numbers 20-54 / 69-82 say)"""
    if h == "Saññojanadukaṃ":
        return DGROUP["cha"]
    if h == "Upādānadukaṃ":
        return DGROUP["dvi"]
    c = CLUSTER_OF[h]
    return c[c.index(h):]


def _gocchaka_heads(base, lw):
    h = base[0].upper() + base[1:] + "dukaṃ"
    if "ādi" in lw:
        if h == "Āsavadukaṃ":
            return sum((CLUSTER_OF[x] for x in _STARTS[2:9]), [])
        return _adi_heads(h)
    return CLUSTER_OF[h]


# ===================================================================================== parts
PH_X = re.compile(r"^##### (\d[\d-]*\.?) (\S+?)-(\S+?) \^", re.M)       # «1-1. Hetuduka-kusalattikaṃ»
PH_T = re.compile(r"^##### (\S+ttikaṃ) \^", re.M)                      # 5-09
PH_D = re.compile(r"^##### (?:([\d-]+\.) )?(\S+?(?:dukaṃ|dukādi|dukāni|gocchakaṃ)) \^", re.M)   # 5-10


EXTRA_POS = {"Kusalattikaṃ": ["kusalākusal"]}      # (see the extensions)


def part_atoms(dheads, theads):
    pos = sum((M.DYAD_TERMS[h] for h in dheads), []) + sum((M.TRI_ATOMS[t] + EXTRA_POS.get(t, []) for t in theads), [])
    negs = sum((M.NEG_DY[h] + M.NEG2_DY[h] for h in dheads), []) + sum((M.NEG_TRI[t] for t in theads), [])
    pos = list(dict.fromkeys(pos))
    negs = list(dict.fromkeys(negs))
    return pos, negs


def world_of(dheads):
    return WB if dheads and all(h in M.WORLD_B_DYADS for h in dheads) else WA


def parts_of(name, src):
    if name[:4] in ("5-09",):
        rx = PH_T
    elif name[:4] in ("5-10",):
        rx = PH_D
    else:
        rx = PH_X
    ms = list(rx.finditer(src))
    if not ms:
        raise SystemExit("no part heading in " + name)
    out = []
    for i, m in enumerate(ms):
        s = 0 if i == 0 else m.start()
        e = ms[i + 1].start() if i + 1 < len(ms) else len(src)
        text = src[s:e]
        if rx is PH_X:
            k1, h1, n1 = side(m[2])
            k2, h2, n2 = side(m[3])
            hl(f"{m[1]} {m[2]}-{m[3]}", f"{m[1]} {n1}နှင့် {n2}")
            dh = (h1 if k1 == "d" else []) + (h2 if k2 == "d" else [])
            th = (h1 if k1 == "t" else []) + (h2 if k2 == "t" else [])
        elif rx is PH_T:
            th, dh = [M.triad_of(m[1])], []
        else:
            k, dh, nm = side(m[2])
            th = []
            hl(f"{m[1]} {m[2]}" if m[1] else m[2], f"{m[1]} {nm}" if m[1] else nm, log=bool(m[1]) or m[2] not in M.HL)
            dh = sorted({c for h in dh for c in CLUSTER_OF[h]}, key=DYADS_ALL.index)
        dh = sorted({c for h in dh for c in CLUSTER_OF[h]}, key=DYADS_ALL.index)
        pos, negs = part_atoms(dh, th)
        out.append((world_of(dh), M.Part(pos + negs, singles=pos + negs), text))
    return out


# ===================================================================================== extensions (logged)
# numbers of these chapters (5-07, 5-09)
for _w, _n, _my in (("ekūnapaññāsa", 49, "လေးဆယ့်ကိုး"), ("aṭṭhacattālīsa", 48, "လေးဆယ့်ရှစ်"),
                    ("ekūnavīsa", 19, "ဆယ့်ကိုး"), ("pañcavīsa", 25, "နှစ်ဆယ့်ငါး"), ("chabbīsa", 26, "နှစ်ဆယ့်ခြောက်"),
                    ("aṭṭhavīsa", 28, "နှစ်ဆယ့်ရှစ်"), ("ekūnavīsati", 19, "ဆယ့်ကိုး")):
    M.NUM_ADD[_w] = (_n, new(_w, _my))
for _w in (WA, WB):
    for _mod in (_w.F, _w.FG):
        M.setup_numbers(_mod)
# «X-vārepi … vitthāro» (the predicate without «sabbattha»): «… ၌လည်း အကျယ် ချဲ့ခြင်း»
M._PRED.append((r"vitthāro", "n", lambda: M.VITTHARO))
# source spellings of a term (the atom of the usual spelling; logged)
ALIAS = {"nanevāsekkhanāsekkh": ("nanevasekkhanāsekkh", "Sekkhattikaṃ", "a"),
         "nanevaācayagāmiṃ nāpacayagām": ("nanevācayagāmināpacayagām", "Ācayagāmittikaṃ", "i"),
         "naanupann": ("naanuppann", "Uppannattikaṃ", "a"),
         "naapaccay": ("naappaccay", "Sappaccayadukaṃ", "a")}
for _a, (_b, _h, _cls) in ALIAS.items():
    M.atom(_a, _cls, M.ATOM[_b][1])
    (M.NEG_TRI if _h in M.NEG_TRI else M.NEG_DY)[_h].append(_a)
    SLIPS.append(f"«{_a}» (spelling) = the term «{_b}»")
# «nocittasampayutta» (5-08 ^7-62-11; the dyad has no «no-» term): «no» = «na», the na-X rule on «cittasampayutta»
M.atom("nocittasampayutt", "a", M.neg(M.ATOM["cittasampayutt"][1]))
M.NEG_DY["Cittasampayuttadukaṃ"].append("nocittasampayutt")
new("nocittasampayutta", M.ATOM["nocittasampayutt"][1])
# «kusalākusala» (one compound: kusala or akusala) before a term and its noun: the engine's «kusalākusalaṃ»
M.atom("kusalākusal", "a", F.LEX["kusalākusalaṃ"][0])
# source slips (read as the parallel lines write them; logged by M.prep_text)
M.SLIP_FIX.update({
    "nakusalaṃ dhammaṃ paṭicca nanahetuṃ nakusalo dhammo": "nakusalaṃ dhammaṃ paṭicca nanahetu nakusalo dhammo",
    "naupādādhammaṃ": "naupādā dhammaṃ",
    "ceva nanahetu dhammo ca uppajjati": "ceva nanahetu ca dhammo uppajjati",
    "āsavavippayutto nanoanāsavo dhammo": "āsavavippayutto naanāsavo dhammo",
    "naahetukassa ceva nana hetussa": "naahetukassa ceva nana ca hetussa",
})
# a lone term before «…» (its noun elided: «nooghaṃ…pe… noyogaṃ…») is a term, as before its noun
_NOUNISH0 = M._NOUNISH


_MARK = "\u2060"                     # marks a list-final elided accusative term «…pe… nonīvaraṇaṃ.» (removed at once)


class _Nounish:
    def match(self, s):
        return _NOUNISH0.match(s) or s.startswith(("…", PE, _MARK))


M._NOUNISH = _Nounish()
_rewrite0 = M.rewrite


def _rewrite(text, part):
    text = re.sub(r"(?<=…pe… )([\wāīūṃṅñṭḍṇḷ]+aṃ)(?=\.)", r"\1" + _MARK, text)
    return _rewrite0(text, part).replace(_MARK, "")


M.rewrite = _rewrite


def _chains(text, terms, part):
    """M._chains, with one change: a «ceva … ca» term stacks with a following SINGLE term (the dukatika «hetu ceva
    sahetuko ca kusalo», as 5-02 with closer_links), never with a following «ceva» term (coordination, as 5-04)"""
    chains, cur = [], [terms[0]] if terms else []
    for a, b in zip(terms, terms[1:]):
        gap_ok = text[M._span_end(text, a):b.start] == " "
        link = False
        if gap_ok and part.stack:
            if not a.ceva and a.coord is None:
                link = True
            elif a.ceva and (a.closer is None or part.closer_links or not b.ceva):
                link = True
        if link:
            ca = M._CASE[M.ATOM[a.atoms[-1][0]][0]][a.atoms[-1][1]]
            cb = M._CASE[M.ATOM[b.atoms[0][0]][0]][b.atoms[0][1]]
            if ca is not None and cb is not None and ca != cb:
                link = False
        if link:
            cur.append(b)
        else:
            chains.append(cur)
            cur = [b]
    if cur:
        chains.append(cur)
    return chains


M._chains = _chains
# editorial notes in braces (no siglum)
_KT = M.TRIADS["Kusalattikaṃ"]
for _mod in (WA.F, WA.FG, WB.F, WB.FG):
    _mod.EDNOTES["ito paṭṭhāya yāva ajjhattārammaṇattikā sabbapotthakesu akusalābyākatapadāni na dissanti, "
                 "vedanāttika sanidassanattikesu viya nanu tehipi bhavitabbaṃ"] = new(
        "{ito paṭṭhāya yāva ajjhattārammaṇattikā … nanu tehipi bhavitabbaṃ}",
        f"ဤနေရာမှ စ၍ {M.TIKA_NAME['Ajjhattārammaṇattikaṃ']} တိုင်အောင် စာမူ အားလုံးတို့၌ {_KT['akusal']} ပုဒ်နှင့် "
        f"{_KT['abyākat']} ပုဒ်တို့ကို မတွေ့ရ{C} {M.TIKA_NAME['Vedanāttikaṃ']}နှင့် "
        f"{M.TIKA_NAME['Sanidassanasappaṭighattikaṃ']}တို့၌ကဲ့သို့ ထိုပုဒ်တို့လည်း ရှိသင့်သည် မဟုတ်လော")
for _mod in (WA.F, WA.FG, WB.F, WB.FG):
    # harmonise H23: an uncertain variant reading kept as the Pāli, as 2-07 «{ပါဌ်ကွဲ ((မသေချာ)): …}» and 5-15
    _mod.EDNOTES["hetuyā aṭṭha?"] = new("{hetuyā aṭṭha?}", f"ပါဌ်ကွဲ ({F.SIGLA['?']}): hetuyā aṭṭha")
    _mod.EDNOTES["ayaṃ saṅkhyā vicāretabbā, nalokiyanalokuttaradhammo nāma natthi"] = new(
        "{ayaṃ saṅkhyā vicāretabbā, nalokiyanalokuttaradhammo nāma natthi}",
        f"ဤ ရေတွက်ချက်ကို စိစစ်ရမည်{C} {M.ATOM['nalokiy'][1][:-len('သော')]}{C} {M.ATOM['nalokuttar'][1]} "
        f"{F.DHAMMA} ဟူ၍ {M.NATTHI}")
# a line written with a stray full stop, translated as written: «Hetuyā. Nava (sabbattha nava.)» (5-07 ^7-61-65):
# the engine renders «Hetuyā nava (…)», the stop is put back after the condition
LINE_FIX = {"^7-64-14": ("(Lokuttaraṃ dhammaṃ paṭicca nalokiyo ca nalokuttaro ca dhammā uppajjanti hetupaccayā.)",
                         "Lokuttaraṃ dhammaṃ paṭicca nalokiyo ca nalokuttaro ca dhammā uppajjanti hetupaccayā.",
                         lambda l: re.sub(r"(?<=။ )([^။()]*။)(?= \{)", r"(\1)", l, count=1)),
            "^7-61-65": ("Hetuyā. Nava (sabbattha nava.)", "Hetuyā nava (sabbattha nava.)",
                         lambda l: re.sub(r"^(\S+ဟူသော အကြောင်း၌) ", r"\1" + END + " ", l, count=1))}


# ===================================================================================== notes (hand-written, Pāli as written)
NOTE_HAND = collections.OrderedDict()
_orig_note_my = M.note_my


def note_my(note):
    if note in NOTE_HAND:
        return NOTE_HAND[note]
    return _orig_note_my(note)


M.note_my = note_my


def note(pali, my):
    """a note «(…)» of these chapters (Pāli as written, with its brackets) -> Burmese (with its brackets)"""
    NOTE_HAND[pali] = new(pali, my)


# hand-written units (a sentence or clause the engine has no frame for): Pāli as written (with its final stop when
# it has one) -> Burmese; each is replaced by a placeholder before the engine runs and put back afterwards
HAND = collections.OrderedDict()


def hand(pali, my):
    HAND[pali] = new(pali, my)


def _hand_in(src):
    for i, k in enumerate(HAND):
        ph = f"(⁑h{i})"
        for w in (WA, WB):
            w.K.NOTE_FIXED[ph[1:-1]] = f"⁌{i}⁌"
            for mod in (w.F, w.FG):
                mod.NOTES[ph] = f"(⁌{i}⁌)"
    for i, k in sorted(enumerate(HAND), key=lambda kv: -len(kv[1])):
        src = src.replace(k, f"(⁑h{i})")
    return src


def _hand_out(txt):
    vals = list(HAND.values())
    txt = re.sub(r"\(⁌(\d+)⁌\)", lambda m: vals[int(m[1])], txt)
    assert "⁌" not in txt and "⁑" not in txt, "hand placeholder left"
    return txt


# ===================================================================================== the note words of these chapters
_A = lambda surf: M.ATOM[surf][1]                     # an atom's Burmese
DH = F.DHAMMA
CNT = F.COUNT
PANHA = K.PANHA                                       # «ပြဿနာ»
KATABBA = new("kātabbā / kātabbaṃ (N …)", "ပြုရမည်")   # (finished groups «N kātabbā» «Nကို ပြုရမည်»)
YEVA = new("-yeva (only, after a count)", "သာ")        # (4-01 «tīṇiyeva» «သုံးခုသာ»)
EKAMYEVA = new("ekaṃyeva", "တစ်ခုတည်း")               # (3-01 … 3-02 «ekāyeva» «တစ်ခုတည်း»)
MULAM = new("X-mūlaṃ (nominative)", "ကို အခြေခံခြင်း")  # (finished groups «X-mūlake» «Xကို အခြေခံခြင်း၌»)
PVASENA = new("paccayavasena", "အကြောင်းအလိုက်")
UPAYENA = new("etena upāyena", "ဤနည်းလမ်းဖြင့်")       # (finished groups «iminā kāraṇena» «ဤနည်းလမ်းဖြင့်»)
ETTHA = new("ettha", "ဤနေရာ၌")                         # (finished groups «idha» «ဤနေရာ၌»)
NA_LABBHATI = new("na labbhati", "မတွေ့ရ")             # (3-02 «na labbhati» «မတွေ့ရ»)
NA_SADISA = new("(X-e) na sadisaṃ", "မတူ")
VATTATI = new("vattati / vaṭṭati (applies here)", "သက်ဆိုင်သည်")
SAMKHITTA_PL = new("ete saṃkhittā", "ဤတို့ကို အကျဉ်းချုပ်ထားသည်")
YAVA = new("yāva X-epi (up to X too)", "တိုင်အောင်လည်း")
CITTASAMU_R = F.FIXED["cittasamuṭṭhānaṃ rūpaṃ"][0] if "cittasamuṭṭhānaṃ rūpaṃ" in F.FIXED else WA.FG.FIXED["cittasamuṭṭhānaṃ rūpaṃ"][0]
MAHABHUTA = F.NOUN["mahābhūtā"][0] if "mahābhūtā" in F.NOUN else "မူလဓာတ်ကြီး"
AB = M.TRIADS["Kusalattikaṃ"]["abyākat"]
AB_MULA = f"{AB} {DH}{MULAM}"


def _counts(seq):
    """«hetuyā chabbīsa, ārammaṇe aṭṭhārasa…pe… avigate chabbīsa» -> the engine's counts"""
    toks = re.split(r"(, |…pe… ?|… ?)", seq)
    out = []
    for i, t in enumerate(toks):
        if i % 2:
            out.append(C + " " if t == ", " else t.replace("…pe…", PE))
            continue
        m = re.fullmatch(r"(na|no)?(\w+) (\w+)", t)
        if not m or m[3] not in CNT:
            return None
        loc = m[2].lower()
        if loc not in F.LOC2STEM:
            return None
        out.append(F.count_my(F.LOC2STEM[loc], bool(m[1]), m[3]))
    return "".join(out)


_CL_FIX = {
    "pañhāvāraṃ vitthāretabbaṃ": f"{M.PANHAVARA}ကို {M.VITTH}",
    "pañhāvāraṃ evaṃ vitthāretabbaṃ": f"{M.PANHAVARA}ကို {M.EVAM_T} {M.VITTH}",
    "vitthāretabbaṃ": M.VITTH,
    "piṭṭhidukaṃ vitthāretabbaṃ": f"{M.GNAME['Piṭṭhidukaṃ']}ကို {M.VITTH}",
    "paccanīyaṃ vitthāretabbaṃ": f"{ORDER_N['paccanīyaṃ']}ကို {M.VITTH}",
    "abyākatamūlaṃ tīṇiyeva": f"{AB_MULA}သည် {CNT['tīṇi']}{YEVA}",
    "abyākatamūlaṃ tīṇiyeva paccayavasena": f"{AB_MULA}သည် {PVASENA} {CNT['tīṇi']}{YEVA}",
    "abyākatamūlaṃ dve": f"{AB_MULA}သည် {CNT['dve']}",
    "abyākatamūlaṃ ekaṃyeva": f"{AB_MULA}သည် {EKAMYEVA}",
    "abyākatamūle dve": f"{AB_MULA}၌ {CNT['dve']}",
    "abyākatavāre sabbattha paccayavasena gaṇetabbaṃ": f"{AB} {DH}အလိုက် ဖော်ပြချက်၌ {M.SABB} {PVASENA} {M.GANETABBA}",
    "nanocittapadaṃ na labbhati": f"{_A('nanocitt')} {PADA}ကို {NA_LABBHATI}",
    "yāva pañhāvārepi ekaṃ": f"{M.PANHAVARA} {YAVA} {CNT['ekaṃ']}",
    "cittasamuṭṭhānarūpameva ettha vattati": f"{ETTHA} {CITTASAMU_R}{YEVA} {VATTATI}",
    "cittasamuṭṭhānameva": f"{CITTASAMU_R}{YEVA}",
    "ārammaṇaṃ natthi": f"{F.cname('ārammaṇa')} {M.NATTHI}",
    "mahābhūtā natthi": f"{MAHABHUTA}တို့ {M.NATTHI}",
    "ekapañhameva": f"{PANHA} {CNT['ekaṃ']}{YEVA}",
    "etena upāyena kusalākusaladukaṃ kusalattikameva ettha vaṭṭati":
        f"{UPAYENA} {ETTHA} {F.LEX['kusalākusalaṃ'][0]} {DUKA}{C} {M.TIKA_NAME['Kusalattikaṃ']}{YEVA} {VATTATI}",
    "etena upāyena nava pañhā kātabbā": f"{UPAYENA} {PANHA} {CNT['nava']} {KATABBA}",
    "etena upāyena kenaci naviññeyye ekūnavīsati pañhā kātabbā":
        f"{UPAYENA} {_A('kenaci naviññeyy')} {DH}၌ {PANHA} {CNT['ekūnavīsa']} {KATABBA}",
    "ete saṃkhittā": SAMKHITTA_PL,
    "dukattayaṃ cittadukasadisaṃ": f"{DUKA} {CNT['tīṇi']}သည် {M.DUKA_NAME['Cittadukaṃ']}{M.SADISA}",
    "pañhāvāre na sadisaṃ": f"{M.PANHAVARA}၌ {NA_SADISA}",
    "āsavagocchakasadisaṃ": f"{M.GNAME['Āsavagocchakaṃ']}{M.SADISA}",
    "saṃkiliṭṭhasaṃkilesikattikasadisaṃ": f"{M.TIKA_NAME['Saṃkiliṭṭhattikaṃ']}{M.SADISA}",
    "akusalaṃ tīṇi kātabbaṃ": f"{_A('akusal')} {DH}ကို {CNT['tīṇi']} {KATABBA}",
    "abyākataṃ tīṇi kātabbaṃ": f"{AB} {DH}ကို {CNT['tīṇi']} {KATABBA}",
}
# «X Y-sadisaṃ / -sadiso» (a term like a term: the term as a noun, term + «သဘောတရား», as the finished notes)
for _x, _y, _p in (("saṅkhat", "sappaccay", "saṅkhataṃ sappaccayasadisaṃ"),
                   ("asaṅkhat", "appaccay", "asaṅkhataṃ appaccayasadisaṃ"),
                   ("akusal", "kusal", "akusalaṃ kusalasadisaṃ"), ("anāgat", "atīt", "anāgato atītasadiso")):
    _CL_FIX[_p] = f"{_A(_x)} {DH}သည် {_A(_y)} {DH}{M.SADISA}"
_CL_FIX["saṃkhittaṃ sappaccayasadisaṃ"] = f"{M.SAMKH}{C} {_A('sappaccay')} {DH}{M.SADISA}"
for _k, _v in _CL_FIX.items():
    new(f"({_k})", _v)
_orig_clause = M._clause


def _clause(c):
    if c in _CL_FIX:
        return _CL_FIX[c]
    m = re.fullmatch(r"(sahajātavārampi(?:\s*…\s*)sampayuttavārampi) vitthāretabbaṃ", c)
    if m:        # harmonise H20: the object list «Xကိုလည်း» before «vitthāretabbaṃ» (= 4-10 … 4-21 now, 5-01 … 5-04)
        return f"{M._vara_list(*M._members(m[1]), 'a')} {M.VITTH}"
    m = re.fullmatch(r"(\w+)dukaṃ (\w+)dukasadisaṃ", c)            # «hetusampayuttadukaṃ sahetukadukasadisaṃ»
    if m:
        a, b = (x[0].upper() + x[1:] + "dukaṃ" for x in m.groups())
        return f"{M.DUKA_NAME[a]}သည် {M.DUKA_NAME[b]}{M.SADISA}"
    m = re.fullmatch(r"(\w+) pañhā(?: (kātabbā))?", c)              # «nava pañhā (kātabbā)»
    if m and m[1] in CNT:
        return f"{PANHA} {CNT[m[1]]}" + (f" {KATABBA}" if m[2] else "")
    r = _counts(c)                                                   # «ārammaṇe aṭṭhārasa…pe… avigate chabbīsa»
    if r is not None:
        return r
    m = re.fullmatch(r"(\w+)vārepi (.+)", c)                        # «paccayavārepi hetuyā chabbīsa, …»
    if m and m[1] in M.VARA_W:
        r = _counts(m[2])
        if r is not None:
            return f"{K.vara(m[1])}၌လည်း {r}"
    return _orig_clause(c)


M._clause = _clause
_orig_sentence = M._sentence


def _sentence(snt):
    m = re.fullmatch(r"yathā kusalattike pañhāvārassa ((?:\w+ampi )+)gaṇitaṃ, evaṃ gaṇetabbaṃ", snt)
    if m:
        ords = [K.ORDER_N[M.ORDERS_A[w]] + "ကိုလည်း" for w in m[1].split()]
        return f"{M.KT_L} {M.PANHAVARA}၏ {(C + ' ').join(ords)} {M.GANITA} {M.EVAM} {M.GANETABBA}"   # (as 4-02)
    return _orig_sentence(snt)


M._sentence = _sentence

# hand-written units (5-12: the counts after a term written as a short sentence)
_KU, _AKU = _A("kusal"), _A("akusal")
for _w, _my in (("Kusalaṃ", _KU), ("Akusalaṃ", _AKU), ("Abyākataṃ", AB)):
    hand(f"{_w} appaṭighena tīṇi.", f"{_my}၊ {_A('appaṭigh')} {DH}ဖြင့် {CNT['tīṇi']}{END}")
for _w, _my in (("Kusalaṃ", _KU), ("Akusalaṃ", _AKU)):
    hand(f"{_w} appaṭighañca abyākataṃ appaṭighañca tīṇi.",
         f"{_my}၊ {_A('appaṭigh')} {DH}နှင့် {AB}၊ {_A('appaṭigh')} {DH}၌ {CNT['tīṇi']}{END}")
hand("Akusalena tīṇiyeva.", f"{_AKU} {DH}ဖြင့် {CNT['tīṇi']}{YEVA}{END}")
hand("Abyākatena tīṇiyeva.", f"{AB} {DH}ဖြင့် {CNT['tīṇi']}{YEVA}{END}")
hand("Abyākatāni tīṇi.", f"{AB} {DH}များ၌ {CNT['tīṇi']}{END}")
hand("Acetasikāni nava.", f"{_A('acetasik')} {DH}များ၌ {CNT['nava']}{END}")
hand("Cittavippayutte tīṇi.", f"{_A('cittavippayutt')} {DH}၌ {CNT['tīṇi']}{END}")
# fragments and units the engine has no frame for (5-09, 5-12)
SATTA_PANHA = new("satta pañhā (after «…»)", f"{PANHA} {CNT['satta']}")
SUKHAVEDANA = new("sukhavedanā", "သာယာသော ခံစားမှု")      # (the vedanā triad «sukhāya vedanāya» «သာယာသော ခံစားမှု…»)
_ALLMODS = [(_w, _mod) for _w in (WA, WB) for _mod in (_w.F, _w.FG)]
_QV = {k: next(m.QUAL[k] for _, m in _ALLMODS if k in m.QUAL) for k in ("vipākābyākataṃ", "kiriyābyākataṃ")}
for _w in (WA, WB):
    for _mod in (_w.F, _w.FG):
        _mod.SKF.setdefault("satta pañhā", SATTA_PANHA)
        _mod.SKF.setdefault("vipākābyākataṃ kiriyābyākataṃ", f"{_QV['vipākābyākataṃ']}{C} {_QV['kiriyābyākataṃ']}")
        _mod.SK["§T§e khandhe paṭicca sukhavedanā cittasamuṭṭhānañca rūpaṃ"] = (
            f"{{T1}} {F.KHANDHA}တို့ကို မှီ၍ {SUKHAVEDANA}{F.LAKAUNG}{C} {CITTASAMU_R}{F.LAKAUNG}")


# ===================================================================================== the run
def translate_part(w, part, text):
    """M.translate_part with only the part's own synthetic terms active (the same key -> Burmese table, fewer
    alternatives in the engine's term pattern; the output is the same)"""
    t = M.prep_text(text, part)
    inv = {k: m for m, k in M.KEYS.items()}
    used = {k.lower() for k in re.findall(r"[Zz]qw[bcdfghjklmnpqrstvwxz]+", t)}
    M.set_terms(w, {k: inv[k] for k in used})
    t = w.D.prep(t, None)
    w.D.chapter_notes(t, None)
    w.FG.translate("")
    out = w.F.translate(t)
    out = re.sub(r"\(?⁂(\w+)⁂\)?", lambda m: w.F.COUNT[m[1]], out)
    assert "⁂" not in out and not re.search(r"zqw", out, re.I)
    return out



def translate(name):
    src = (PALI / name).read_text(encoding="utf-8-sig")
    lines = src.split("\n")
    fixed = {}
    for i, ln in enumerate(lines):
        for bid, (a, b, fix) in LINE_FIX.items():
            if a in ln:
                lines[i] = ln.replace(a, b)
                fixed[i] = fix
                SLIPS.append(f"{name} (segment {bid}): «{a}» rendered via «{b}», then restored")
    src = "\n".join(lines)
    src = _hand_in(src)
    parts = parts_of(name, src)
    for w in (WA, WB):
        for k, v in M.HL.items():
            w.F.HLINES.setdefault(k, v)
            assert w.F.HLINES[k] == v, (k, w.F.HLINES[k], v)
    out = "\n".join(translate_part(w, p, t) for w, p, t in parts).split("\n")
    assert len(out) == len(lines), (len(out), len(lines))
    for i, fix in fixed.items():
        new_ = fix(out[i])
        assert new_ != out[i], ("line fix did not apply", out[i][:80])
        out[i] = new_
    return _hand_out("\n".join(out))


class Counting(dict):
    cnt = collections.Counter()

    def setdefault(self, k, v):
        self.cnt[k] += 1
        return super().setdefault(k, v)


def main():
    global OUT
    if "--out" in sys.argv:
        OUT = pathlib.Path(sys.argv[sys.argv.index("--out") + 1]).resolve()
        del sys.argv[sys.argv.index("--out"):sys.argv.index("--out") + 2]
    names = [a for a in sys.argv[1:] if not a.startswith("--")] or NAMES
    names = [next(n for n in NAMES if n.startswith(a)) for a in names]
    dev = "--dev" in sys.argv
    for w in (WA, WB):
        w.F.DEV = dev
        if dev:
            w.F.UNSEEN = Counting()
    for n in names:
        txt = translate(n)
        if "--dump" in sys.argv:
            continue
        if not dev:
            (OUT / n).write_text(txt, encoding="utf-8")
            print(f"wrote {n}: {sum(1 for l in txt.splitlines() if l)} lines")
        else:
            CHK.mkdir(exist_ok=True)
            (CHK / ("dev-" + n)).write_text(txt, encoding="utf-8")
    if "--dump" in sys.argv:
        for my, k in M.KEYS.items():
            print(k, " | ".join(sorted(M.KEY_PALI[k])), "=", my, sep="\t")
        return
    if dev:
        CHK.mkdir(exist_ok=True)
        with open(CHK / ("dev-" + "_".join(n[:4] for n in names) + ".txt"), "w", encoding="utf-8") as fh:
            tot = 0
            for w in (WA, WB):
                rows = sorted(w.F.UNSEEN.items(), key=lambda kv: -w.F.UNSEEN.cnt[kv[0]])
                tot += len(rows)
                for k, v in rows:
                    fh.write(f"[{w.tag} {w.F.UNSEEN.cnt[k]}] SK: {k}\n    {v}\n")
        print(tot, "unmatched skeletons")
    if "--new" in sys.argv:
        for k, v in NEW.items():
            print(f"- {k} = {v}")
        for k, v in M.NEW.items():
            if k not in NEW:
                print(f"- (M) {k} = {v}")
    if "--slips" in sys.argv:
        print("slips:", *sorted(set(SLIPS) | set(M.SLIPS) | WA.F.SLIPS | WB.F.SLIPS), sep="\n  ")


if __name__ == "__main__":
    main()
