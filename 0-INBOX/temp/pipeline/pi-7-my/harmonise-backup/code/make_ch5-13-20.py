"""Burmese zero-shot of pi-7 part 5, the mixed orders («အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ»), from the Pāli only:
5-13 anulomapaccanīya tikatika, 5-14 anulomapaccanīya dukaduka, 5-15 paccanīyānuloma tika, 5-16 paccanīyānuloma
duka, 5-17 paccanīyānuloma dukatika, 5-18 paccanīyānuloma tikaduka, 5-19 paccanīyānuloma tikatika, 5-20
paccanīyānuloma dukaduka (the last chapter of the book, with its colophons).

usage: python3 -I -X utf8 make_ch5-13-20.py [chapter ...] [--dev] [--slips] [--out DIR] [--dump]
  (no flag)  translate the chapters and write them; stops on the first unmatched sentence (nothing is guessed).
  --dev      do not stop: list every unmatched skeleton with its count in chk-ch5-13-20/dev.txt (nothing written).
  --dump     print the combined-term table (Pāli chain = Burmese) and stop.

Method: the finished part-5 group make_ch5-01-04.py is IMPORTED as Q (read-only; its setup() runs on import, its
main() never runs; it loads its own engines, world A = make_ch3-09.py and world B = make_ch4-01.py, on their own
copies of my7_formulas / make_sample). Its machinery is used as it is:
  * the atoms (every triad / dyad term of the finished groups) and the «na-X» atoms with the na-X rule
    («…သော» -> «…သည် မဟုတ်သော», «X ဖြစ်သော» -> «X မဟုတ်သော», double negatives twice);
  * the rewrite of every term chain into ONE synthetic term, stacked «A၊ B N» (the pattern of 5-01 … 5-04, which is
    also the dukatika pattern «<dyad term>၊ <triad term>» of 4-02 … 4-14);
  * its notes renderer, headings, names and numbers.
This script only adds (in memory, logged in notes-ch5-13-20.md): the part cutting of the mixed orders (a part runs
with the positive AND the negated atoms of its triads / dyads active), the order headings anulomapaccanīya /
paccanīyānuloma (the words of the finished groups' sections of those orders), the part names of the dukatika /
tikaduka / group headings, the notes of these chapters and the book's closing colophons.
No file of the sample or of another group is edited or written.
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
NAMES = ["5-13-anulomapaccaniya-tikatika.md", "5-14-anulomapaccaniya-dukaduka.md", "5-15-paccaniyanuloma-tika.md",
         "5-16-paccaniyanuloma-duka.md", "5-17-paccaniyanuloma-dukatika.md", "5-18-paccaniyanuloma-tikaduka.md",
         "5-19-paccaniyanuloma-tikatika.md", "5-20-paccaniyanuloma-dukaduka.md"]
CHK = HERE / "chk-ch5-13-20"


def _load(name, fn):
    spec = importlib.util.spec_from_file_location(name, HERE / fn)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


Q = _load("q5_ch50104", "make_ch5-01-04.py")           # the model (read-only; its main() does not run)
Q_NEW0 = dict(Q.NEW)
F, K, WA, WB = Q.F, Q.K, Q.WA, Q.WB
C, END, PE = Q.C, Q.END, Q.PE
TITLE, TIKA, DUKA, ADI, DONE = F.TITLE, F.TIKA, F.DUKA, F.ADI, F.DONE

NEW = collections.OrderedDict()     # every new string of this script: Pāli -> Burmese
SLIPS = []


def new(pali, my):
    if pali in NEW:
        assert NEW[pali] == my, (pali, NEW[pali], my)
    NEW.setdefault(pali, my)
    return my


def hl(pali, my, log=True):
    """a heading / whole line (shared with Q's table; the same Pāli keeps the same Burmese)"""
    if pali in Q.HL:
        assert Q.HL[pali] == my, (pali, Q.HL[pali], my)
        return
    Q.HL[pali] = my
    if log:
        new(pali, my)


# ===================================================================================== the order headings
ORDER_N = K.ORDER_N
HEAD_ANUL = Q.HEAD_ANUL                                   # «သဘောတရား အဟုတ်ပြ ပုံစံ၌» (Dhammānulome)
HEAD_AP = new("Dhammānulomapaccanīye", HEAD_ANUL.replace(Q.ORDER_L["anulome"], ORDER_N["anulomapaccanīyaṃ"] + "၌"))
HEAD_PA = new("Dhammapaccanīyānulome", HEAD_ANUL.replace(Q.ORDER_L["anulome"], ORDER_N["paccanīyānulomaṃ"] + "၌"))
_TT = f"{TIKA}နှင့် {TIKA}တို့၏ {TITLE}"                     # (5-01)
_DD = f"{DUKA}နှင့် {DUKA}တို့၏ {TITLE}"                     # (5-02)
_DT = f"{DUKA}နှင့် {TIKA}တို့၏ {TITLE}"                     # (4-02 «Dhammānulome dukatikapaṭṭhānaṃ»)
_TD = f"{TIKA}နှင့် {DUKA}တို့၏ {TITLE}"                     # (as _DT, the triad first)
_T = F.HEAD["Tikapaṭṭhānaṃ"]
_D = Q._DUKAP
for _hp, _hm in (("Dhammānulomapaccanīye", HEAD_AP), ("Dhammapaccanīyānulome", HEAD_PA)):
    for _w, _n in (("tikatika", _TT), ("dukaduka", _DD), ("dukatika", _DT), ("tikaduka", _TD), ("tika", _T),
                   ("duka", _D)):
        hl(f"{_hp} {_w}paṭṭhānaṃ", f"{_hm} {_n}")
        hl(f"{_hp} {_w}paṭṭhānaṃ niṭṭhitaṃ.", f"{_hm} “{_n}” {DONE}{END}")
hl("Anulomapaccanīyapaṭṭhānaṃ niṭṭhitaṃ.", f"{ORDER_N['anulomapaccanīyaṃ']}၌ “{TITLE}” {DONE}{END}")
hl("Paccanīyānulomapaṭṭhānaṃ niṭṭhitaṃ.", f"{ORDER_N['paccanīyānulomaṃ']}၌ “{TITLE}” {DONE}{END}")
# the book's colophons (pi-1 / pi-3 / pi-4 «“…” ကျမ်း ပြီးဆုံးပြီ။»; pi-1 bhāṇavāra «ရွတ်ဖတ်ရန် အပိုင်း»)
KYAM = "ကျမ်း"
hl("Paṭṭhānapakaraṇaṃ niṭṭhitaṃ.", f"“{TITLE}” {KYAM} {DONE}{END}")
BHANAVARA = new("bhāṇavāra", "ရွတ်ဖတ်ရန် အပိုင်း")
hl("Anulomadukatikapaṭṭhānato paṭṭhāya yāva pariyosānā tiṃsamattehi bhāṇavārehi paṭṭhānaṃ.",
   f"{Q.ORDER_L['anulome']} “{_DT}” မှ စ၍ အဆုံးတိုင်အောင် “{TITLE}” သည် {BHANAVARA} "
   f"{new('tiṃsamatta', 'သုံးဆယ်ခန့်')} ရှိသည်{END}")

# ===================================================================================== the terms of a part
TRI_ORDER = list(Q.TRIADS)                       # the 22 triads in Mātikā order
assert len(TRI_ORDER) == 22 and TRI_ORDER[0] == "Kusalattikaṃ" and TRI_ORDER[-1] == "Sanidassanasappaṭighattikaṃ"
# the 100 dyads in Mātikā order: hetu 1-6, cūḷantara 7-13, āsava … parāmāsa 14-54, mahantara 55-68, upādāna 69-74,
# kilesa 75-82, piṭṭhi 83-100
CLUSTER_HEADS = {}       # the six (parāmāsa: five) dyads of a cluster, in Mātikā order (from Q.CL)
for _cl, _c in Q.CL.items():
    _cap, _s = _c["cap"], _c["s"]
    _S = _s[0].upper() + _s[1:]
    CLUSTER_HEADS[_cl] = [h for h in (f"{_cap}adukaṃ", f"{_S}adukaṃ", f"{_cap}asampayuttadukaṃ", f"{_cap}a{_s}adukaṃ",
                                      f"{_cap}a{_c['x']}asampayuttadukaṃ", f"{_cap}avippayutta{_s}adukaṃ")
                          if h in Q.DYAD_TERMS]
_MAHA = Q._MAHA
DY_ORDER = (Q._HETU_CL + Q._CULA + sum((CLUSTER_HEADS[c] for c in ("asava", "sannojana", "gantha", "ogha", "yoga",
                                                                    "niv", "par")), [])
            + _MAHA + CLUSTER_HEADS["upa"] + Q._KIL + Q._PITTHI)
assert len(DY_ORDER) == 100 and len(set(DY_ORDER)) == 100 and set(DY_ORDER) == set(Q.DYAD_TERMS), len(DY_ORDER)
CLUSTER_OF = {}
for _grp in [Q._HETU_CL, Q._KIL] + list(CLUSTER_HEADS.values()):
    for _h in _grp:
        CLUSTER_OF[_h] = _grp
SUPER = [(1, 6), (7, 13), (14, 19), (20, 54), (55, 68), (69, 74), (75, 82), (83, 100)]
GROUP_START = {"hetu": 1, "cūḷantara": 7, "āsava": 14, "saññojana": 20, "mahantara": 55, "upādāna": 69, "kilesa": 75,
               "piṭṭhi": 83}


def _nums(num):
    return [int(x) for x in re.findall(r"\d+", num or "")]


def _span(nums, s, default_end):
    """the end of a range that starts at s (1-based): from a pair (a, b) of the heading's numbers with a = s or s-1"""
    for a, b in zip(nums, nums[1:]):
        if b > a and a in (s, s - 1):
            return s + (b - a)
    return default_end


def _super_end(s):
    return next(e for a, e in SUPER if a <= s <= e)


TRI_RX = re.compile(r"(\w+?)(ttikaṃ|ttika|ttikadvayaṃ|ttikadvaya|ttikādi|ādittikāni)")


def triads_of(word, nums):
    """a triad word of a heading -> [triad heads] or None"""
    m = TRI_RX.fullmatch(word)
    if not m:
        return None
    try:
        th = Q.triad_of(m[1] + ("attika" if m[2] == "ādittikāni" else "ttika"))
    except KeyError:
        return None
    i = TRI_ORDER.index(th)
    kind = m[2]
    if kind.startswith("ttikadvay"):
        return TRI_ORDER[i:i + 2]
    if kind in ("ttikādi", "ādittikāni"):
        e = _span(nums, i + 1, 22)
        return TRI_ORDER[i:e]
    return [th]


DY_RX = re.compile(r"(\w+?)(ādicha|ādi)?(dukaṃ|duka|dukāni|dukādi|gocchakaṃ|gocchaka|gocchakāni|gocchakādi)")


def _dysplit(word):
    """-> (base, adi, kind) or None; the stem vowel before «ādi» is restored («sahetukādi» -> «sahetuka»)"""
    m = DY_RX.fullmatch(word)
    if not m:
        return None
    base, adi, kind = m[1][0].lower() + m[1][1:], m[2], m[3]
    if adi:
        base += "a"
    return base, adi, kind


def dyads_of(word, nums):
    """a dyad / group word of a heading -> [dyad heads] or None"""
    sp = _dysplit(word)
    if not sp:
        return None
    base, adi, kind = sp
    head = base[0].upper() + base[1:] + "dukaṃ"
    if kind.startswith("gocchak"):
        if base not in GROUP_START:
            return None
        s = GROUP_START[base]
        e = CLUSTER_OF.get(DY_ORDER[s - 1])
        e = s + len(e) - 1 if e else _super_end(s)
        if adi or kind in ("gocchakāni", "gocchakādi"):
            e = _span(nums, s, _super_end(s) if adi else e)
        return DY_ORDER[s - 1:e]
    if base in ("cūḷantara", "mahantara", "piṭṭhi"):
        s = GROUP_START[base]
        e = _super_end(s)
        if kind in ("dukāni", "dukādi") or adi:
            e = _span(nums, s, e)
        return DY_ORDER[s - 1:e]
    if head not in DY_ORDER:
        return None
    s = DY_ORDER.index(head) + 1
    if adi or kind in ("dukāni", "dukādi"):
        e = _span(nums, s, _super_end(s))
        return DY_ORDER[s - 1:e]
    return [head]


def _expand(heads):
    """the whole cluster of each dyad (the paccanīya of a «ceva» dyad is written with the cluster's other terms)"""
    out = []
    for h in heads:
        for c in CLUSTER_OF.get(h, [h]):
            if c not in out:
                out.append(c)
    return sorted(out, key=DY_ORDER.index)


def atoms_tri(ths):
    pos = sum((Q.TRI_ATOMS[t] for t in ths), [])
    neg = sum((Q.NEG_TRI[t] for t in ths), [])
    return pos, neg


def atoms_dy(hs):
    hs = _expand(hs)
    pos = sum((Q.DYAD_TERMS[h] for h in hs), [])
    neg = sum((Q.NEG_DY[h] + Q.NEG2_DY[h] for h in hs), [])
    if "Kenaciviññeyyadukaṃ" in hs:
        pos.append("nakenaci viññeyy")
    return pos, neg


def world_of(hs):
    """world B when every dyad is one of world B (5-02 / 5-04 rule), else world A (the triads: world A)"""
    if hs and all(h in Q.WORLD_B_DYADS for h in _expand(hs) if h != "Hetudukaṃ") and \
            any(h in Q.WORLD_B_DYADS for h in hs):
        return WB
    return WA


# ===================================================================================== part names
def tri_noun(th):
    n = Q.TIKA_NAME[th]
    assert n.endswith(" " + TIKA), n
    return n[:-len(TIKA) - 1]


def duka_noun(h):
    n = Q.DUKA_NAME[h]
    assert n.endswith(" " + DUKA), n
    return n[:-len(DUKA) - 1]


PLURAL = "များ"
TWO = F.COUNT["dve"]                    # «နှစ်ခု»
SIX = F.COUNT["cha"]                    # «ခြောက်ခု»


def name_tri(word, ths):
    m = TRI_RX.fullmatch(word)
    th = ths[0]
    kind = m[2]
    if kind.startswith("ttikadvay"):
        return new(word, f"{Q.TIKA_NAME[th]} {TWO}")                       # the two X triads
    if kind == "ttikādi":
        return new(word, f"{Q.TIKA_NAME[th]} {ADI}")                       # as «Tikādi» «သုံးမျိုးတွဲ စသည်»
    if kind == "ādittikāni":
        return new(word, f"{tri_noun(th)} {ADI}တို့၏ {TIKA}{PLURAL}")       # as «Ārammaṇādidukāni» (1-01)
    return Q.TIKA_NAME[th]


def name_dy(word, hs):
    base, adi, kind = _dysplit(word)
    full = word[0].upper() + word[1:]
    cap = base[0].upper() + base[1:]
    # the finished groups' names first (identity with 5-02 / 5-04 / 4-02 … 4-14)
    if full in Q.DUKA_NAME:
        return Q.DUKA_NAME[full]
    if full + "ṃ" in Q.DUKA_NAME and kind == "duka":
        return Q.DUKA_NAME[full + "ṃ"]
    if full in Q.GNAME:
        return Q.GNAME[full]
    if full + "ṃ" in Q.GNAME and kind in ("duka", "gocchaka"):
        return Q.GNAME[full + "ṃ"]
    if not adi and base == "piṭṭhi" and kind in ("duka", "dukaṃ", "dukāni"):
        return Q.GNAME["Piṭṭhidukaṃ"]                                    # already plural «… နှစ်မျိုးတွဲများ»
    if adi and base[:-1] in Q.ADI_NOUN and kind in ("duka", "dukāni"):
        return Q.dd_name(word[:-len(kind)], kind, hs)                    # «saññojanādidukāni» (5-02)
    # a cluster noun («နှောင်ကြိုး» of «နှောင်ကြိုးတို့၏ အစု»)
    goc = Q.GNAME.get(cap + "gocchakaṃ")
    noun = goc[:-len(Q._GOC_TAIL)] if goc and goc.endswith(Q._GOC_TAIL) else None
    if kind.startswith("gocchak"):
        if adi:
            if adi == "ādicha":                                          # «saññojanādichagocchakāni»
                return new(word, f"{noun} {ADI}တို့၏ {Q.GOCCHAKA_N} {SIX}")
            return new(word, f"{noun} {ADI}တို့၏ {Q.GOCCHAKA_N}" + (PLURAL if kind == "gocchakāni" else ""))
        if kind == "gocchakāni":
            return new(word, f"{goc}{PLURAL}")
        if kind == "gocchakādi":
            return new(word, f"{goc} {ADI}")
        return goc
    gname = {"cūḷantara": "Cūḷantaradukaṃ", "mahantara": "Mahantaradukaṃ", "piṭṭhi": "Piṭṭhidukaṃ"}
    if base in gname:
        g = Q.GNAME[gname[base]]
        if kind == "dukāni":                     # the group's dyads = the group's name («… အစုငယ်», «… များ»)
            return g
        if kind == "dukādi":
            return new(word, f"{g} {ADI}")
        return g
    h = cap + "dukaṃ"
    if adi:                          # «Sahetukādidukāni» «… စသည်တို့၏ နှစ်မျိုးတွဲများ» (as «Ārammaṇādidukāni», 1-01)
        nn = noun if noun else duka_noun(h)
        return new(word, f"{nn} {ADI}တို့၏ {DUKA}" + (PLURAL if kind == "dukāni" else ""))
    if kind == "dukādi":                                                 # as «Tikādi» «သုံးမျိုးတွဲ စသည်»
        return new(word, f"{Q.DUKA_NAME[h]} {ADI}")
    raise KeyError("dyad name " + word)


def name_of(word, nums):
    ths = triads_of(word, nums)
    if ths:
        return "t", ths, name_tri(word, ths)
    hs = dyads_of(word, nums)
    if hs:
        return "d", hs, name_dy(word, hs)
    return None


# ===================================================================================== parts
PH2 = re.compile(r"^(#{5,6}) (?:([\d-]+\.?) )?(\S+?)-(\S+?) (\^\S+)$", re.M)
PH1 = re.compile(r"^(#{5,6}) (?:([\d-]+\.?) )?(\S+) (\^\S+)$", re.M)
PART_LOG = []        # (chapter, heading, [terms]) for the notes / checker


def parts_of(name, src):
    two = name[:4] in ("5-13", "5-14", "5-17", "5-18", "5-19", "5-20")
    ms = []
    for m in (PH2 if two else PH1).finditer(src):
        nums = _nums(m[2])
        if two:
            a, b = name_of(m[3], nums), name_of(m[4], nums)
            if not (a and b):
                continue
            num = m[2] + " " if m[2] else ""
            hl(f"{num}{m[3]}-{m[4]}", f"{num}{a[2]}နှင့် {b[2]}")
            ms.append((m, [a, b]))
        else:
            a = name_of(m[3], nums)
            if not a:
                continue
            num = m[2] + " " if m[2] else ""
            if num or a[2] != Q.HL.get(m[3]):
                hl(f"{num}{m[3]}", f"{num}{a[2]}")
            ms.append((m, [a]))
    if not ms:
        raise SystemExit("no part heading in " + name)
    out = []
    for i, (m, sets) in enumerate(ms):
        s = 0 if i == 0 else m.start()
        e = ms[i + 1][0].start() if i + 1 < len(ms) else len(src)
        text = src[s:e]
        pos, neg, hs = [], [], []
        for kind, heads, _ in sets:
            p, n = atoms_tri(heads) if kind == "t" else atoms_dy(heads)
            pos += [x for x in p if x not in pos]
            neg += [x for x in n if x not in neg]
            if kind == "d":
                hs += heads
        PART_LOG.append((name, m[0].split(" ^")[0], [h for _, hh, _ in sets for h in hh]))
        if two:
            part = Q.Part(pos + neg, closer_links=True)
        else:
            part = Q.Part(pos + neg, singles=pos + neg)
        out.append((world_of(hs), part, text))
    return out


# ===================================================================================== notes of these chapters
MY_NOTES = collections.OrderedDict()     # note as written -> Burmese (hand-written, composed from the model's words)
D_ = F.DHAMMA                            # «သဘောတရား»: supplied after a term used as a noun (2-01 «… ရှိသော သဘောတရားကို
#                                          အခြေခံသော ပြဿနာ»; logged)
SEP = Q.SEP
KAT = K.KATABBA                          # kātabbaṃ «ပြုရမည်»
PANHA = K.PANHA                          # pañhā «ပြဿနာ»
SAMKH, SABB, VITTH, EVAM, NATTHI, SADISA = Q.SAMKH, Q.SABB, Q.VITTH, Q.EVAM_T, Q.NATTHI, Q.SADISA
MULA = F.MULAKA                          # -mūla(ka) «… ကို အခြေခံခြင်း» (1-01)
LAKAUNG = F.LAKAUNG
NA_LAB = new("na labbhati / no labbhati", "မတွေ့ရ")                 # (the module's LEX «na labbhati»)
YEVA = new("-yeva / -meva / -eva (only)", "သာ")                       # (4-01 «tīṇiyeva» «သုံးခုသာ»)
EVA_EMPH = new("-eva (emphasis, after an instrumental)", "ပင်")
GANITAKENA = new("gaṇitakena", "ရေတွက်ချက်အားဖြင့်")
PURIMANAYENA = new("purimanayena", "ရှေ့နည်းအတိုင်း")
NAYAVASENA = new("nayavasena", "နည်းအလိုက်")
ETENA_UPAYENA = new("etena upāyena", "ဤ နည်းလမ်းဖြင့်")
MULANI = new("mūlāni (the roots, bases)", "အခြေခံ")                  # (1-01 «imāni tīṇi mūlāni» «ဤ အခြေခံ သုံးခု»)
ORD = {"paṭhamaṃ": new("paṭhamaṃ (gaṇitakena)", "ပထမတွင်"), "dutiyaṃ": new("dutiyaṃ (gaṇitakena)", "ဒုတိယတွင်"),
       "tatiyaṃ": new("tatiyaṃ (gaṇitakena)", "တတိယတွင်")}
OVATTA = new("ovattā", "ပြောင်းပြန် ဖြစ်ကြသည်")                       # (reversed; unsure word, logged)
VEDITAKA = new("veditakaṃ kātabbaṃ", f"သိမှတ်၍ {KAT}")                # (unsure word, logged)
ANTIMA = new("antimadukaṃ", f"အဆုံးသတ် {DUKA}")                        # (not «နောက်ဆုံး»: that is piṭṭhi)
EACH = "စီ"                                                            # «dve dve» «နှစ်ခုစီ» (4-01 «nava nava» «ကိုးခုစီ»)
NUM_NEW = {"aṭṭhavīsa": (28, "နှစ်ဆယ့်ရှစ်"), "chabbīsa": (26, "နှစ်ဆယ့်ခြောက်"), "chabbīsati": (26, "နှစ်ဆယ့်ခြောက်"),
           "ekūnapaññāsa": (49, "လေးဆယ့်ကိုး"), "dvāvīsa": (22, "နှစ်ဆယ့်နှစ်"), "tevīsa": (23, "နှစ်ဆယ့်သုံး"),
           "dvāvīsati": (22, "နှစ်ဆယ့်နှစ်"), "tevīsati": (23, "နှစ်ဆယ့်သုံး"), "ekavīsati": (21, "နှစ်ဆယ့်တစ်"),
           "chabbīsa": (26, "နှစ်ဆယ့်ခြောက်")}
CNT = dict(F.COUNT)
for _k, (_n, _my) in NUM_NEW.items():
    assert CNT.setdefault(_k, _my + "ခု") == _my + "ခု", _k
RUPA_CS = new("cittasamuṭṭhānarūpa", f"{F.QUAL['cittasamuṭṭhānānaṃ']} ရုပ်")


FOR = new("-ssa (for a root / term: «X-mūlassa», «X-ssa … pañhā»)", "အတွက်")
PURIMASADISA = new("purimasadisaṃ", "ရှေ့နှင့် တူသော")


def A(*atoms):
    """stacked atom values «A၊ B» (Q's composition)"""
    return SEP.join(Q.ATOM[a][1] for a in atoms)


def pn(num):
    """N pañhā «ပြဿနာ Nခု» (2-01)"""
    return f"{PANHA} {CNT[num]}"


def mula(*atoms):
    return f"{A(*atoms)} {D_}{MULA}"


T_ = Q.TIKA_NAME
DN = Q.DUKA_NAME
E = END


def note(pali, my):
    assert pali not in MY_NOTES, pali
    MY_NOTES[pali] = my


note("(Kusale pañca, akusale pañca, abyākate tīṇi.)",
     f"({A('kusal')} {D_}၌ {CNT['pañca']}{C} {A('akusal')} {D_}၌ {CNT['pañca']}{C} {A('abyākat')} {D_}၌ {CNT['tīṇi']}{E})")
note("(Dve mūlāni.)", f"({MULANI} {CNT['dve']}{E})")
note("(Uppādī anuppannasadisaṃ.)", f"({A('uppād')} {D_}သည် {A('anuppann')} {D_}{SADISA}{E})")
note("(Anāgataṃ atītasadisaṃ.)", f"({A('anāgat')} {D_}သည် {A('atīt')} {D_}{SADISA}{E})")
note("(Tīṇi veditakaṃ kātabbaṃ.)", f"({CNT['tīṇi']}ကို {VEDITAKA}{E})")
note("(Ekavīsati pañhā.)", f"({PANHA} {CNT['ekavīsati']}{E})")
note("(Dukkhāya vedanāya sampayuttaabyākatamūlaṃ adukkhamasukhāya vedanāya sampayuttaabyākatamūlampi kātabbaṃ.)",
     f"({mula('dukkhāya vedanāya sampayutt', 'abyākat')}ကို{C} "
     f"{mula('adukkhamasukhāya vedanāya sampayutt', 'abyākat')}ကိုလည်း {KAT}{E})")
note("(Vedanāttikasadisaṃ. Saṃkhittaṃ.)", f"({T_['Vedanāttikaṃ']}{SADISA}{E} {SAMKH}{E})")
note("(Pañhāvāraṃ vitthāretabbaṃ.)", f"({Q.PANHAVARA}ကို {VITTH}{E})")
note("(Sahetukasadisaṃ.)", f"({A('sahetuk')} {D_}{SADISA}{E})")
note("(Asaṅkhataṃ appaccayasadisaṃ.)", f"({A('asaṅkhat')} {D_}သည် {A('appaccay')} {D_}{SADISA}{E})")
note("(Lokiyasadisaṃ.)", f"({A('lokiy')} {D_}{SADISA}{E})")
note("(saṃkhittaṃ. Nayavasena vitthāretabbaṃ)", f"({SAMKH}{E} {NAYAVASENA} {VITTH})")
note("(Saṅkhataṃ sappaccayasadisaṃ)", f"({A('saṅkhat')} {D_}သည် {A('sappaccay')} {D_}{SADISA})")
note("(Saṅkhataṃ sappaccayasadisaṃ.)", f"({A('saṅkhat')} {D_}သည် {A('sappaccay')} {D_}{SADISA}{E})")
note("(Sabbattha pañhe saṃkhittaṃ.)", f"({SABB} {PANHA}များကို {SAMKH}{E})")        # as «(mūlakaṃ saṃkhittaṃ)»
note("(Etena upāyena sabbattha vitthāretabbaṃ.)", f"({ETENA_UPAYENA} {SABB} {VITTH}{E})")
note("(Sahajātavāro paṭiccavārasadiso)", f"({K.vara('sahajāta')}သည် {K.vara('paṭicca')}{SADISA})")
note("(Yathā kusalattike pañhāvārassa anulomampi paccanīyampi anulomapaccanīyampi paccanīyānulomampi gaṇitaṃ, "
     "evaṃ gaṇetabbaṃ.)",
     "(" + Q._sentence("yathā kusalattike pañhāvārassa anulomampi paccanīyampi anulomapaccanīyampi "
                       "paccanīyānulomampi gaṇitaṃ evaṃ gaṇetabbaṃ") + f"{E})")
note("(Sabbattha nava pañhā.)", f"({SABB} {pn('nava')}{E})")
note("(saṃkhittaṃ, nava pañhā)", f"({SAMKH}{C} {pn('nava')})")
note("(Nava pañhā.)", f"({pn('nava')}{E})")
note("(saṃkhittaṃ, nava pañhā kātabbā)", f"({SAMKH}{C} {pn('nava')} {KAT})")
note("(Nava pañhā kātabbā.)", f"({pn('nava')} {KAT}{E})")
note("(Nava pañhā kātabbā)", f"({pn('nava')} {KAT})")
note("(Cha pañhā kātabbā.)", f"({pn('cha')} {KAT}{E})")
note("(Dukamūlakaṃ ekaṃ.)", f"({DUKA}{MULA} {CNT['ekaṃ']}{E})")
note("(Āsavaāsavasampayuttadukaṃ natthi.)", f"({DN['Āsavaāsavasampayuttadukaṃ']} {NATTHI}{E})")
note("(Naakusale tīṇi. Naabyākate tīṇi. Saṃkhittaṃ.)",
     f"({A('naakusal')} {D_}၌ {CNT['tīṇi']}{E} {A('naabyākat')} {D_}၌ {CNT['tīṇi']}{E} {SAMKH}{E})")
note("(Nava pañhā saṃkhittaṃ.)", f"({pn('nava')}ကို {SAMKH}{E})")
note("(Dukamūlaṃ ekaṃ saṃkhittaṃ, sabbattha tīṇi.)",
     f"({DUKA}{MULA} {CNT['ekaṃ']}ကို {SAMKH}{C} {SABB} {CNT['tīṇi']}{E})")
note("(Ajjhattattiko na labbhati paṭiccavārādīsu.)",
     f"({K.vara('paṭicca')} {ADI}တို့၌ {T_['Ajjhattattikaṃ']}ကို {NA_LAB}{E})")
note("(Ajjhattabahiddhārammaṇaṃ natthi.)", f"({A('ajjhattabahiddhārammaṇ')} {D_} {NATTHI}{E})")
note("(Nahetunaanidassanasappaṭighamūlepi tīṇiyeva.)",
     f"({mula('nahet', 'naanidassanasappaṭigh')}၌လည်း {CNT['tīṇi']}{YEVA}{E})")
note("(Nasahetukanaanidassanasappaṭighamūlepi tīṇiyeva.)",
     f"({mula('nasahetuk', 'naanidassanasappaṭigh')}၌လည်း {CNT['tīṇi']}{YEVA}{E})")
note("(Nahetusampayuttaṃ nasanidassanasappaṭighaṃ sahetukadukasadisaṃ. Tīṇi pañhā. Hetusahetukaduke ca "
     "hetuhetusampayuttaduke ca pañhā no labbhati.)",
     f"({A('nahetusampayutt', 'nasanidassanasappaṭigh')} {D_}သည် {DN['Sahetukadukaṃ']}{SADISA}{E} {pn('tīṇi')}{E} "
     f"{DN['Hetusahetukadukaṃ']}၌{LAKAUNG}{C} {DN['Hetuhetusampayuttadukaṃ']}၌{LAKAUNG} {PANHA}ကို {NA_LAB}{E})")
note("(Naappaccayanaanidassanaappaṭighamūlepi ekameva.)",
     f"({mula('naappaccay', 'naanidassanaappaṭigh')}၌လည်း {CNT['ekaṃ']}{YEVA}{E})")
note("(Nasaṅkhataṃ nasappaccayasadisaṃ.)", f"({A('nasaṅkhat')} {D_}သည် {A('nasappaccay')} {D_}{SADISA}{E})")
note("(Gaṇitakena gaṇetabbā tīṇi pañhā.)", f"({GANITAKENA} {pn('tīṇi')}ကို {Q.GANETABBA}{E})")
note("(tīṇiyeva pañhā kātabbā)", f"({PANHA} {CNT['tīṇi']}{YEVA} {KAT})")
note("(purimanayena tīṇi pañhā)", f"({PURIMANAYENA} {pn('tīṇi')})")
note("(Nasāsavaṃ naanidassanasappaṭighamūlassa purimanayena tīṇi pañhā.)",
     f"({mula('nasāsav', 'naanidassanasappaṭigh')}{FOR} {PURIMANAYENA} {pn('tīṇi')}{E})")
note("(Naāsavasampayuttanaanidassanasappaṭighamūle tīṇiyeva.)",
     f"({mula('naāsavasampayutt', 'naanidassanasappaṭigh')}၌ {CNT['tīṇi']}{YEVA}{E})")
note("(Naāsavañceva naanāsavaṃ naanidassanasappaṭighamūlepi purimanayena tīṇiyeva.)",
     f"({mula('naāsav', 'naanāsav', 'naanidassanasappaṭigh')}၌လည်း {PURIMANAYENA} {CNT['tīṇi']}{YEVA}{E})")
note("(Āsavaāsavasampayuttaduke pañhā na labbhati.)",
     f"({DN['Āsavaāsavasampayuttadukaṃ']}၌ {PANHA}ကို {NA_LAB}{E})")
note("(Āsavavippayuttanasāsavanaanidassanasappaṭighamūlepi purimanayeneva tīṇi pañhā.)",
     f"({mula('āsavavippayutt', 'nasāsav', 'naanidassanasappaṭigh')}၌လည်း {PURIMANAYENA}{EVA_EMPH} {pn('tīṇi')}{E})")
note("(Tīṇi pañhā.)", f"({pn('tīṇi')}{E})")
note("(Anidassanasappaṭighe tīṇiyeva.)", f"({A('anidassanasappaṭigh')} {D_}၌ {CNT['tīṇi']}{YEVA}{E})")
note("(Cittasamuṭṭhānarūpeneva tīṇi, saṃkhittaṃ.)", f"({RUPA_CS}ဖြင့်{YEVA} {CNT['tīṇi']}{C} {SAMKH}{E})")
note("(Ahetukasadisaṃ, saṃkhittaṃ.)", f"({A('ahetuk')} {D_}{SADISA}{C} {SAMKH}{E})")
_G3 = (f"{ORD['paṭhamaṃ']} {GANITAKENA} {CNT['ekaṃ']}{C} {ORD['dutiyaṃ']} {GANITAKENA} {CNT['ekaṃ']}{C} "
       f"{ORD['tatiyaṃ']} {GANITAKENA} {CNT['ekaṃ']}")
note("(Naakusale dve, naabyākate dve. Paṭhamaṃ gaṇitakena ekaṃ, dutiyaṃ gaṇitakena ekaṃ, tatiyaṃ gaṇitakena ekaṃ, "
     "sabbattha nava pañhā.)",
     f"({A('naakusal')} {D_}၌ {CNT['dve']}{C} {A('naabyākat')} {D_}၌ {CNT['dve']}{E} {_G3}{C} {SABB} {pn('nava')}{E})")
note("(Gaṇitakena tīṇi pañhā.)", f"({GANITAKENA} {pn('tīṇi')}{E})")
note("(Akusalamūle dve, dukamūle dve.)", f"({mula('akusal')}၌ {CNT['dve']}{C} {DUKA}{MULA}၌ {CNT['dve']}{E})")
note("(apariyāpannasadisaṃ cha pañhā)", f"({A('apariyāpann')} {D_}{SADISA}{C} {pn('cha')})")
note("(dutiyaṃ gaṇitakena tīṇi)", f"({ORD['dutiyaṃ']} {GANITAKENA} {CNT['tīṇi']})")
note("(dve pañhāyeva)", f"({PANHA} {CNT['dve']}{YEVA})")
note("(dveyeva. Paṭhamaṃ gaṇitakena ekaṃ, dutiyaṃ gaṇitakena ekaṃ, tatiyaṃ gaṇitakena ekaṃ kātabbaṃ.)",
     f"({CNT['dve']}{YEVA}{E} {_G3} {KAT}{E})")
note("(Nahetu nanahetu ovattā, tīṇi mūlāni, ekavīsati pañhā kātabbā.)",
     f"({A('nahet')} {D_}နှင့် {A('nanahet')} {D_}တို့ {OVATTA}{C} {MULANI} {CNT['tīṇi']}{C} "
     f"{PANHA} {CNT['ekavīsati']} {KAT}{E})")
note("(Akusalāneva tīṇi.)", f"({A('akusal')} {D_}များ{YEVA} {CNT['tīṇi']}{E})")
note("(Cattāri gaṇitakena dve dve pañhā kātabbā.)",
     f"({CNT['cattāri']}{C} {GANITAKENA} {PANHA} {CNT['dve']}{EACH} {KAT}{E})")
note("(Naakusalaṃ naabyākataṃ natthi.)", f"({A('naakusal')} {D_}နှင့် {A('naabyākat')} {D_} {NATTHI}{E})")
note("(Atītattikaṃ uppannattikasadisaṃ.)", f"({T_['Atītattikaṃ']}သည် {T_['Uppannattikaṃ']}{SADISA}{E})")
note("(Naanidassanasappaṭighanaabyākatamūlāni sattameva, dukamūlāni sattameva, sabbaṃ ekavīsatimeva.)",
     f"({mula('naanidassanasappaṭigh', 'naabyākat')}များ {CNT['satta']}{YEVA}{C} {DUKA}{MULA}များ "
     f"{CNT['satta']}{YEVA}{C} {new('sabbaṃ', 'အားလုံး')} {CNT['ekavīsati']}{YEVA}{E})")
note("(gaṇitakena tīṇi.)", f"({GANITAKENA} {CNT['tīṇi']}{E})")
note("(Sabbattha saṃkhittaṃ.)", f"({SABB} {SAMKH}{E})")
note("(Antimadukaṃ na labbhati.)", f"({ANTIMA}ကို {NA_LAB}{E})")
note("(Hetuhetusampayuttadukaṃ saṃkhittaṃ.)", f"({DN['Hetuhetusampayuttadukaṃ']}ကို {SAMKH}{E})")

# whole sentences the engine has no frame for (a sentence -> one placeholder, as Q's bare counts; logged)
SENT = collections.OrderedDict()


def sent(pali, my):
    assert pali not in SENT, pali
    SENT[pali] = my


sent("Akusale tīṇi.", f"{A('akusal')} {D_}၌ {CNT['tīṇi']}")                    # = the notes «(Naakusale tīṇi. …)»
sent("Abyākataṃ anupādinnupādāniye tīṇiyeva…pe….",
     f"{A('abyākat')} {D_}ကို {A('anupādinnupādāniy')} {D_}၌ {CNT['tīṇi']}{YEVA}{PE}")
sent("Nahetu nadukkhāya vedanāya sampayuttamūlaṃ tīṇiyeva.",
     f"{mula('nahet', 'nadukkhāya vedanāya sampayutt')} {CNT['tīṇi']}{YEVA}")
sent("Nakenaci viññeyyaṃ naanidassanasappaṭighassa purimasadisaṃ navapañhaṃ kātabbaṃ.",
     f"{A('nakenaci viññeyy', 'naanidassanasappaṭigh')} {D_}{FOR} {PURIMASADISA} {pn('nava')} {KAT}")
sent("Nakenaci viññeyyaṃ naanidassanaappaṭighamūlassa navapañhameva.",
     f"{mula('nakenaci viññeyy', 'naanidassanaappaṭigh')}{FOR} {pn('nava')}{YEVA}")
sent("Hetuyā cha pañhā.", f"{F.cond('hetu', 'loc')} {pn('cha')}")
sent("Naasaṅkhataṃ…pe… (sappaccayadukasadisaṃ).",
     f"{A('naasaṅkhat')} {D_}{PE} ({DN['Sappaccayadukaṃ']}{SADISA})")

# loose (unbracketed) words and fragments: LEX items of the engines (logged)
LEX_X = {
    "gaṇitakena tīṇi": f"{GANITAKENA} {CNT['tīṇi']}",
    "gaṇitakena tīṇi pañhā": f"{GANITAKENA} {pn('tīṇi')}",
    "cha pañhā": pn("cha"),
    "saṃsaṭṭhavāre": f"{K.vara('saṃsaṭṭha')}၌",
}
# counts with «-yeva / -meva» («only N», 4-01 «tīṇiyeva» «သုံးခုသာ») and new numbers
ONLY = {"tīṇiyeva": "tīṇi", "tīṇimeva": "tīṇi", "ekameva": "ekaṃ", "sattameva": "satta"}
EDN = {"hetuyā aṭṭha?": f"ပါဌ်ကွဲ ({F.SIGLA['?']}): hetuyā aṭṭha"}     # as «{ပါဌ်ကွဲ ((မသေချာ)): …}» (1-01)


def setup_extra():
    for w, (n, my) in NUM_NEW.items():
        Q.NUM_ADD.setdefault(w, (n, my))
        if w not in F.COUNT:
            new(w, my)
    for w in (WA, WB):
        for mod in (w.F, w.FG):
            for k, (n, my) in NUM_NEW.items():
                if k in mod.COUNT:
                    assert mod.COUNT[k] == my + "ခု", (k, mod.COUNT[k])
                mod.COUNT.setdefault(k, my + "ခု")
                mod.COUNT_VAL.setdefault(k, n)
                mod.LEX.setdefault(k, (mod.COUNT[k], "x"))
            for k, base in ONLY.items():
                v = mod.COUNT[base] + YEVA
                if k in mod.COUNT:
                    assert mod.COUNT[k] == v, (k, mod.COUNT[k])
                mod.COUNT.setdefault(k, v)
                mod.COUNT_VAL.setdefault(k, mod.COUNT_VAL[base])
                mod.LEX.setdefault(k, (v, "x"))
            Q.setup_numbers(mod)
            for k, v in LEX_X.items():
                if k in mod.LEX:
                    assert mod.LEX[k][0] == v, (k, mod.LEX[k], v)
                mod.LEX.setdefault(k, (v, "x"))
            for k, v in EDN.items():
                mod.EDNOTES.setdefault(k, v)
    for k, v in LEX_X.items():
        new(k, v)
    for k, v in EDN.items():
        new("{" + k + "}", "{" + v + "}")


def setup_notes():
    for k, r in MY_NOTES.items():
        assert k not in Q.NOTE_MINE, k
        Q.NOTE_MINE[k] = r
        Q.NOTE_PH[k] = f"(⁑q{len(Q.NOTE_PH)})"
        for w in (WA, WB):
            w.K.NOTE_FIXED[Q.NOTE_PH[k][1:-1]] = r[1:-1]
            for mod in (w.F, w.FG):
                mod.NOTES[Q.NOTE_PH[k]] = r


# ===================================================================================== headings, slips, count-after
hl("Nahetunaārammaṇapaccayādi", f"{F.cond('hetu', 'n', True)}နှင့် {F.cond('ārammaṇa', 'n', True)} {ADI}")
hl("1-2. Paṭiccavārādi", f"1-2. {K.vara('paṭicca')} {ADI}")                    # as «1-7. Paṭiccavārādi»
hl("3-6. Paccayavārādi", f"3-6. {K.vara('paccaya')} {ADI}")
hl("Anuttarapadaṃ", f"{Q.ATOM['anuttar'][1]} {F.PADA}")                        # as «Sahetukapadaṃ» (5-02)
SLIP_ADD = {   # source slips: as written -> read as (logged)
    "dve khandhā nakusalaṃ dhammaṃ paṭicca abyākato": "dve khandhā. Nakusalaṃ dhammaṃ paṭicca abyākato",  # 5-15 ^7-69-1
}
for _a, _b in SLIP_ADD.items():
    assert _a not in Q.SLIP_FIX
    Q.SLIP_FIX[_a] = _b
# «… paccayā ekaṃ… hetuyā dve.» (5-14 ^7-68-49): the count after the condition, before «…» as before «.»
Q._COUNT_AFTER = re.compile(r"(?<=paccayā) (ekaṃ|dve|tīṇi)(?=\.|…)")
_PREP0 = Q.prep_text


def prep_text(text, part):
    """the sentences of SENT -> placeholders «(⁑zqsN)» (rendered as Q's bare counts, without brackets)"""
    for k in sorted(SENT, key=len, reverse=True):
        text = re.sub(r"(?<![\wāīūṃṅñṭḍṇḷ(])" + re.escape(k), lambda m: SENT_PH[k], text)
    return _PREP0(text, part)


SENT_PH = {}


def setup_sent():
    for i, (k, my) in enumerate(SENT.items()):
        key = f"zqs{chr(97 + i // 26)}{chr(97 + i % 26)}"
        SENT_PH[k] = f"(⁑{key})."
        for w in (WA, WB):
            w.K.NOTE_FIXED[f"⁑{key}"] = f"⁂{key}⁂"
            for mod in (w.F, w.FG):
                mod.NOTES[f"(⁑{key})"] = f"(⁂{key}⁂)"
                mod.COUNT[key] = my
    Q.prep_text = prep_text


# ===================================================================================== the run
Q.parts_of = parts_of


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
    setup_extra()
    setup_notes()
    setup_sent()
    for w in (WA, WB):
        w.F.DEV = dev
        if dev:
            w.F.UNSEEN = Counting()
    for n in names:
        txt = Q.translate(n)
        if "--dump" in sys.argv:
            continue
        if not dev:
            (OUT / n).write_text(txt, encoding="utf-8")
            print(f"wrote {n}: {sum(1 for l in txt.splitlines() if l)} lines")
        else:
            CHK.mkdir(exist_ok=True)
            (CHK / ("dev-" + n)).write_text(txt, encoding="utf-8")
    if "--dump" in sys.argv:
        for my, k in Q.KEYS.items():
            print(k, " | ".join(sorted(Q.KEY_PALI[k])), "=", my, sep="\t")
        return
    if dev:
        CHK.mkdir(exist_ok=True)
        tag = "" if names == NAMES else "-" + "_".join(n[:4] for n in names)
        with open(CHK / f"dev{tag}.txt", "w", encoding="utf-8") as fh:
            tot = 0
            for w in (WA, WB):
                rows = sorted(w.F.UNSEEN.items(), key=lambda kv: -w.F.UNSEEN.cnt[kv[0]])
                tot += len(rows)
                for k, v in rows:
                    fh.write(f"[{w.tag} {w.F.UNSEEN.cnt[k]}] SK: {k}\n    {v}\n")
        print(tot, "unmatched skeletons")
    if not dev and "--dump" not in sys.argv:              # the logs for the notes (scratch)
        CHK.mkdir(exist_ok=True)
        tag = "_".join(n[:4] for n in names)
        with open(CHK / f"new-{tag}.txt", "w", encoding="utf-8") as fh:
            for k, v in NEW.items():
                fh.write(f"N\t{k} = {v}\n")
            for k, v in Q.NEW.items():
                if k not in Q_NEW0:
                    fh.write(f"Q\t{k} = {v}\n")
            for k, v in Q.NEG_LOG.items():
                fh.write(f"NEG\t{k} = {v}\n")
            for my, k in Q.KEYS.items():
                fh.write("T\t" + " | ".join(sorted(Q.KEY_PALI[k])) + f" = {my}\n")
            for x in sorted(set(SLIPS) | set(Q.SLIPS) | WA.F.SLIPS | WB.F.SLIPS):
                fh.write(f"SLIP\t{x}\n")
    if "--slips" in sys.argv:
        print("slips:", *sorted(set(SLIPS) | set(Q.SLIPS) | WA.F.SLIPS | WB.F.SLIPS), sep="\n  ")


if __name__ == "__main__":
    main()
