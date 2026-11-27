"""Burmese zero-shot of pi-7 4-10 … 4-14, the remaining DUKATIKA chapters of the Paṭṭhāna («အကြောင်းနှင့် အကျိုး
ဆက်စပ်ပုံ»): a dyad of the mahantara / upādāna / kilesa / piṭṭhi groups combined with a triad on one noun, from the
Pāli only.

usage: python3 -I -X utf8 make_ch4-10-14.py [chapter ...] [--dev] [--slips] [--new] [--out DIR] [--dump]
  (no flag)  translate the chapters and write them; stops on the first unmatched sentence (nothing is guessed).
  --dev      do not stop: list every unmatched skeleton with its count in chk-ch4-10-14/dev.txt (nothing written).
  --dump     print the combined-term table (dyad term + triad term = Burmese) and stop.
  --new      translate without writing and print every new string («Pāli = Burmese») and the readings.

Method (read-only imports; no main block of another script runs; no file of the sample or of another group is edited
or written):
  * the model make_ch4-02-09.py is IMPORTED as X: its combined-term machinery (combine, dd_split, note renderer,
    heading lines, the triad tables and names, worlds A and B) is used as it is, extended in memory;
  * world C = make_ch3-09.py (→ make_ch3-03-06 → make_ch3-01-02 …), loaded on its OWN copies of my7_formulas /
    make_sample, for 4-10 (the mahantara dyads, its DYADS / DUKA_NAME);
  * world B = X's make_ch3-07-08-10.py for 4-11 (the upādāna dyads, as 4-08 … 4-09 use it for nīvaraṇa / parāmāsa);
  * world E = make_ch4-01.py (→ make_ch3-07-08-10 → make_ch3-01-02 …), loaded on its own copies, for 4-12 … 4-14
    (the kilesa and piṭṭhi dyads, its DYADS_ADD / DUKA_NAME).
Every new string is logged in notes-ch4-10-14.md.
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
NAMES = ["4-10-dukatika-sarammanaduka.md", "4-11-dukatika-upadanaduka.md", "4-12-dukatika-kilesaduka.md",
         "4-13-dukatika-dassanenapahatabbaduka.md", "4-14-dukatika-saranaduka.md"]
CHK = HERE / "chk-ch4-10-14"
WCH = r"[\wāīūṃṅñṭḍṇḷ]"
_NB = r"(?!" + WCH + ")"
_PB = r"(?<!" + WCH + ")"


def _load(name, fn):
    spec = importlib.util.spec_from_file_location(name, HERE / fn)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


X = _load("x_ch40209", "make_ch4-02-09.py")            # the model (its setup() runs on import; its main() does not)
C3 = X._isolated("w_c_ch309", "make_ch3-09.py")       # world C (own shared modules)
E4 = X._isolated("w_e_ch401", "make_ch4-01.py")       # world E (own shared modules)
WC = X.World("C", C3, C3.M3)
WE = X.World("E", E4, E4.D)
WB = X.WB
for _w in (WC, WE):
    assert (_w.F.C, _w.F.END, _w.F.PE) == (X.C, X.END, X.PE)
assert WC.F is not WE.F and WC.F is not X.WA.F and WE.F is not WB.F
C, END, PE = X.C, X.END, X.PE
WORLD_OF = {"4-10": WC, "4-11": WB, "4-12": WE, "4-13": WE, "4-14": WE}

NEW = collections.OrderedDict()     # every new string of this script: Pāli -> Burmese
SLIPS = set()
READ_LOG = set()


def new(pali, my):
    if pali in NEW:
        assert NEW[pali] == my, (pali, NEW[pali], my)
    NEW.setdefault(pali, my)
    return my


# ===================================================================================== the dyads (finished groups)
_EA, _EU, _EI = X._EA, r"(?:uṃ|uno|ussa|ūnaṃ|uñca|u|ū)", X._EI
_ci = X._ci
HEAD_WORLD = {}      # dyad heading -> world
DS = X.DYAD_SURF


def _add(head, world, items):
    DS[head] = items
    HEAD_WORLD[head] = world


# 3-09 (world C): the fourteen mahantara dyads (C3.DYADS / C3.DYAD_OF); the surface is the dyad word as the Pāli
# writes it before the triad word (cittasahabhū / -uṃ, cittānuparivattī / -iṃ, the indeclinable upādā)
_C9 = {"sarammana": [("sārammaṇ", _ci("sārammaṇ") + _EA), ("anārammaṇ", _ci("anārammaṇ") + _EA)],
       "citta": [("cittdk", _ci("citt") + _EA), ("nocittdk", _ci("nocitt") + _EA)],
       "cetasika": [("cetasik", _ci("cetasik") + _EA), ("acetasik", _ci("acetasik") + _EA)],
       "cittasamp": [("cittasampayutt", _ci("cittasampayutt") + _EA), ("cittavippayutt", _ci("cittavippayutt") + _EA)],
       "cittasams": [("cittasaṃsaṭṭh", _ci("cittasaṃsaṭṭh") + _EA),
                     ("cittavisaṃsaṭṭh", _ci("cittavisaṃsaṭṭh") + _EA)],
       "cittasamu": [("cittasamuṭṭhān", _ci("cittasamuṭṭhān") + _EA),
                     ("nocittasamuṭṭhān", _ci("nocittasamuṭṭhān") + _EA)],
       "cittasaha": [("cittasahabhudk", _ci("cittasahabh") + _EU), ("nocittasahabhudk", _ci("nocittasahabh") + _EU)],
       "cittanu": [("cittānuparivattdk", _ci("cittānuparivatt") + _EI),
                   ("nocittānuparivattdk", _ci("nocittānuparivatt") + _EI)],
       "css": [("cittasaṃsaṭṭhasamuṭṭhān", _ci("cittasaṃsaṭṭhasamuṭṭhān") + _EA),
               ("nocittasaṃsaṭṭhasamuṭṭhān", _ci("nocittasaṃsaṭṭhasamuṭṭhān") + _EA)],
       "csssaha": [("cittasaṃsaṭṭhasamuṭṭhānasahabhudk", _ci("cittasaṃsaṭṭhasamuṭṭhānasahabh") + _EU),
                   ("nocittasaṃsaṭṭhasamuṭṭhānasahabhudk", _ci("nocittasaṃsaṭṭhasamuṭṭhānasahabh") + _EU)],
       "cssanu": [("cittasaṃsaṭṭhasamuṭṭhānānuparivattdk", _ci("cittasaṃsaṭṭhasamuṭṭhānānuparivatt") + _EI),
                  ("nocittasaṃsaṭṭhasamuṭṭhānānuparivattdk", _ci("nocittasaṃsaṭṭhasamuṭṭhānānuparivatt") + _EI)],
       "ajjhattika": [("ajjhattik", _ci("ajjhattik") + _EA), ("bāhir", _ci("bāhir") + _EA)],
       "upada": [("upādādk", _ci("upād") + "ā"), ("noupādādk", _ci("noupād") + "ā")],
       "upadinna": [("upādinn", _ci("upādinn") + _EA), ("anupādinn", _ci("anupādinn") + _EA)]}
for _h, _d in C3.DYAD_OF.items():
    _add(_h, WC, [(_d, k, s) for k, s in _C9[_d]])
    assert all(k in WC.DYADS[_d] for k, _ in _C9[_d]), _d
# 3-10 (world B): the upādāna cluster, keyed as the model keys nīvaraṇa / parāmāsa (make_ch3-07-08-10 DYADS_ADD)
_x, _s, _as = "upādān", "upādāniy", "anupādāniy"
X._cluster("Upādāna", "Upādāniya", "upa", _x, _s, _as, _x + "asampayutt", _x + "avippayutt",
           {"x": ("upa1", f"{_x}dk", f"no{_x}"), "s": ("upa2", _s, _as),
            "samp": ("upa3", f"{_x}asampayutt", f"{_x}avippayutt"),
            "xs": ("upa4", f"{_x}a{_s}dk", f"{_s}ano{_x}dk"),
            "xxs": ("upa5", f"{_x}a{_x}asampdk", f"{_x}asampno{_x}dk"),
            "vs": ("upa6", f"{_x}avipp{_s}", f"{_x}avipp{_as}")})
for _h in ("Upādānadukaṃ", "Upādāniyadukaṃ", "Upādānasampayuttadukaṃ", "Upādānaupādāniyadukaṃ",
           "Upādānaupādānasampayuttadukaṃ", "Upādānavippayuttaupādāniyadukaṃ"):
    HEAD_WORLD[_h] = WB
    for _dk, _k, _ in DS[_h]:
        assert _k in WB.DYADS[_dk], (_h, _k)
# 4-01 (world E): the kilesa dyads (glued terms as 4-01 / 3-07 … 3-10) and the piṭṭhi dyads
_CEVA, _CA2, _EV, _EC = X._CEVA, X._CA2, X._EV, X._EC
_K = {
    "Kilesadukaṃ": [("kil1", "kilesdk", _ci("kiles") + _EA), ("kil1", "nokiles", _ci("nokiles") + _EA)],
    "Saṃkilesikadukaṃ": [("kil2", "saṃkilesik", _ci("saṃkilesik") + _EA),
                         ("kil2", "asaṃkilesik", _ci("asaṃkilesik") + _EA)],
    "Saṃkiliṭṭhadukaṃ": [("kilS", "saṃkiliṭṭh", _ci("saṃkiliṭṭh") + _EA),
                         ("kilS", "asaṃkiliṭṭh", _ci("asaṃkiliṭṭh") + _EA)],
    "Kilesasampayuttadukaṃ": [("kilP", "kilesasampayutt", _ci("kilesasampayutt") + _EA),
                              ("kilP", "kilesavippayutt", _ci("kilesavippayutt") + _EA)],
    "Kilesasaṃkilesikadukaṃ": [
        ("kil4", "kilesasaṃkilesikdk", _ci("kiles") + _EV + _CEVA + " saṃkilesik" + _EC + _CA2),
        ("kil4", "saṃkilesikanokilesdk", _ci("saṃkilesik") + _EV + _CEVA + " no ca kiles" + _EA)],
    "Kilesasaṃkiliṭṭhadukaṃ": [
        ("kilB", "kilesasaṃkiliṭṭhdk", _ci("kiles") + _EV + _CEVA + " saṃkiliṭṭh" + _EC + _CA2),
        ("kilB", "saṃkiliṭṭhanokilesdk", _ci("saṃkiliṭṭh") + _EV + _CEVA + " no ca kiles" + _EA)],
    "Kilesakilesasampayuttadukaṃ": [
        ("kil5", "kilesakilesasampdk", _ci("kiles") + _EV + _CEVA + " kilesasampayutt" + _EC + _CA2),
        ("kil5", "kilesasampnokilesdk", _ci("kilesasampayutt") + _EV + _CEVA + " no ca kiles" + _EA)],
    "Kilesavippayuttasaṃkilesikadukaṃ": [
        ("kil6", "kilesavippsaṃkilesik", _ci("kilesavippayutt") + _EA + " saṃkilesik" + _EA),
        ("kil6", "kilesavippasaṃkilesik", _ci("kilesavippayutt") + _EA + " asaṃkilesik" + _EA)],
}
# the piṭṭhi dyads: the two terms of E4.DYADS_ADD as the Pāli writes them (one word, or «dassanena pahātabb-»)
_P = {"Dassanenapahātabbadukaṃ": "dass", "Bhāvanāyapahātabbadukaṃ": "bhav", "Dassanenapahātabbahetukadukaṃ": "dassh",
      "Bhāvanāyapahātabbahetukadukaṃ": "bhavh", "Savitakkadukaṃ": "vitakka", "Savicāradukaṃ": "vicara",
      "Sappītikadukaṃ": "sappitika", "Pītisahagatadukaṃ": "piti", "Sukhasahagatadukaṃ": "sukha",
      "Upekkhāsahagatadukaṃ": "upekkha", "Kāmāvacaradukaṃ": "kama", "Rūpāvacaradukaṃ": "rupa",
      "Arūpāvacaradukaṃ": "arupa", "Pariyāpannadukaṃ": "pariyapanna", "Niyyānikadukaṃ": "niyyanika",
      "Niyatadukaṃ": "niyata", "Sauttaradukaṃ": "sauttara", "Saraṇadukaṃ": "sarana"}
for _h, _d in _P.items():
    _K[_h] = [(_d, k, _ci(k) + _EA) for k in E4.DYADS_ADD[_d] if not k.endswith("_both")]
for _h, _v in _K.items():
    _add(_h, WE, _v)
    for _dk, _k, _ in _v:
        assert _k in WE.DYADS[_dk], (_h, _k)
# a part heading naming two dyads at once («90-91-1. Pītisahagatādiduka-kusalattikaṃ»): both term pairs active
_add("Pītisahagatādidukaṃ", WE, DS["Pītisahagatadukaṃ"] + DS["Sukhasahagatadukaṃ"])
# a part heading with another name of a dyad («Saṃkilesasaṃkilesikaduka-» = the dyad «Kilesasaṃkilesikadukaṃ», ^1-M2-79)
_add("Saṃkilesasaṃkilesikadukaṃ", WE, DS["Kilesasaṃkilesikadukaṃ"])


def dyad_world_of(head):
    if head in HEAD_WORLD:
        return HEAD_WORLD[head]
    return X.WB if head.startswith(("Nīvaraṇ", "Parām")) else X.WA


X.dyad_world_of = dyad_world_of

# dyad names: the finished groups' DUKA_NAME (3-09, 3-10, 4-01)
for _dn in (C3.DUKA_NAME, X.B.DUKA_NAME, E4.DUKA_NAME):
    for _k, _v in _dn.items():
        assert X.DUKA_NAME.get(_k, _v) == _v, _k
        X.DUKA_NAME[_k] = _v
X.DUKA_NAME["Pītisahagatādidukaṃ"] = new(
    "Pītisahagatādidukaṃ", f"{E4.DUKA_NAME['Pītisahagatadukaṃ']} {WE.F.ADI}")
X.DUKA_NAME["Saṃkilesasaṃkilesikadukaṃ"] = E4.DUKA_NAME["Kilesasaṃkilesikadukaṃ"]
READ_LOG.add("heading «Saṃkilesasaṃkilesikaduka-kusalattikaṃ» (4-12) = the dyad Kilesasaṃkilesikadukaṃ (^1-M2-79): "
             "its name")
assert all(h in X.DUKA_NAME for h in DS), [h for h in DS if h not in X.DUKA_NAME]

# triad headings in a short form (4-14): «Micchattattikaṃ» = Micchattaniyatattikaṃ, «Sanidassanattikaṃ» =
# Sanidassanasappaṭighattikaṃ (the same triads; their terms and names)
for _a, _b in (("Micchattattikaṃ", "Micchattaniyatattikaṃ"), ("Sanidassanattikaṃ", "Sanidassanasappaṭighattikaṃ")):
    X.TRIADS[_a] = X.TRIADS[_b]
    X.TIKA_NAME[_a] = X.TIKA_NAME[_b]
    READ_LOG.add(f"triad heading «{_a}» = {_b} (its terms and name)")

# a part number of two dyads («90-91-1.»)
X.PART_HEAD = re.compile(r"^(#{5,6}) (\d+(?:-\d+)+\.?) (\S+?)duka-(\S+?)ttikaṃ \^", re.M)

# ===================================================================================== the worlds C and E
X.NOTEP.setdefault("C", {})
X.NOTEP.setdefault("E", {})


def setup_worlds():
    for w in (WC, WE):
        w.K.CUR["fix"] = True
        X._install_chain(w.F)
        X._install_chain(w.FG)
        s = X.S(w)
        for pali in ("Cūḷantaraduke lokiyadukasadisaṃ.",):
            key = w.D._key(pali, None)
            my = X.piece(s, pali[0].lower() + pali[1:-1]) + END
            for mod in (w.F, w.FG):
                mod.SK[key] = my


setup_worlds()

# ===================================================================================== notes (this group)
_PIECE0 = X.piece
DV = X.dyad_value


def _stem_key(h):
    return h[:-len("dukaṃ")].lower()


# «X-duka» inside a note -> the dyad heading (the Pāli writes «dassanena pahātabba-» apart)
DSTEM = {_stem_key(h): h for h in X.DUKA_NAME}
_TRI_T = {"kusala": "kusal", "akusala": "akusal", "abyākata": "abyākat"}
_NB2 = r"(?![\wāīūṃṅñṭḍṇḷ])"


class N_:
    """this group's note strings of one world (all built from the finished groups' words; NEW ones logged)"""

    def __init__(self, s):
        w = s.w
        F, K, D = w.F, w.K, w.D
        self.s, self.F, self.K, self.D = s, F, K, D
        self.PANHA, self.IHA, self.EV = D.PANHA, D.IHA, D.EVAM_T
        self.KABALI, self.RJIVIT = D.KABALI, D.RJIVIT
        self.KAYYA, self.ADI, self.MULAKA, self.GH = K.KAYYA, F.ADI, F.MULAKA, F.GHATANA
        self.NAYA = new("naya (method, in a note)", "နည်း")                      # (3-03-06 nayena «နည်းအတိုင်း»)
        self.ADIMHI = new("ādimhi", "အစ၌")
        self.PATHAME = new("paṭhame (in the first)", "ပထမ၌")                     # (2-11 paṭhamaghaṭane «ပထမ …၌»)
        self.DUTIYE = new("dutiye (in the second)", "ဒုတိယ၌")
        self.HETTHA = new("heṭṭhā (in the text above)", "အထက်")                   # = 3-10 «heṭṭhā» «အထက်၌»
        self.ETTAKA = new("ettakāyeva pañhā", f"ဤမျှသော {D.PANHA}များသာ")
        self.TATTAKA = new("tattakā eva pañhā", f"{D.PANHA}များသည် ထိုမျှသာ")
        self.PARIV = new("heṭṭhuparikaṃ parivattanti", "အောက်နှင့် အထက် လှည့်ပြောင်းကြသည်")  # (3-03-06 «လှည့်ပြောင်းရမည်»)
        self.GAMANAKALE = new("X-o Y-assa gamanakāle", "အား သွားသည့် အခါ၌")
        self.MAJJHANU = new("majjhimānulomikāyeva pañhā",
                            f"အလယ် {s.ORD['anulomaṃ']}နှင့် ဆိုင်သော {D.PANHA}များသာ")
        self.NANUPEKKHA = new("upekkhāti nānāupekkhā", "ဥပေက္ခာဟူသည် အမျိုးမျိုးသော ဥပေက္ခာ")
        self.KUSAK = new("kusalākusale (in a note)", f"{TRI('kusal')}နှင့် {TRI('akusal')}၌")   # (1-2. Kusalākusalapadaṃ)
        self.PANA = new("pana (but, in a note)", "ကား")
        self.IMANANAM = D.NOTE_ADD["imaṃ nānaṃ"]                                  # idaṃ nānaṃ = imaṃ nānaṃ (3-01-02)

    def tn(self, tt):
        return f"{TRI(tt)} {self.s.DH}"

    def dname(self, stem):
        """the dyad named by «X» in «X-duka…» (None: not a dyad of the table)"""
        st = stem.replace(" ", "").lower()
        if st == "lokiyalokuttara":
            return self.s.LLD
        h = DSTEM.get(st)
        return X.DUKA_NAME[h] if h else None

    def term(self, word):
        """a dyad term used as a noun inside a note («nadassane», «kāmāvacare», «upādinnamūlake» …): (Burmese, rest)"""
        for h, items in DS.items():
            for _, tk, _ in items:
                base = tk.replace("dk", "") if tk.endswith("dk") else tk
                if word.startswith(base) and dyad_world_of(h) is self.s.w:
                    return DV(h, tk), word[len(base):]
        return None, None


def TRI(tt):
    return X.TRIADS["Kusalattikaṃ"][tt]


_NS = {}


def NS(s):
    if s.w.tag not in _NS:
        _NS[s.w.tag] = N_(s)
    return _NS[s.w.tag]


# a dyad term in the locative / «-mūlake» inside a count note: Pāli word -> (heading, term key) (abbreviations logged)
LOC_TERMS = {
    "dassane": ("Dassanenapahātabbadukaṃ", "dassanena pahātabb"),
    "nadassane": ("Dassanenapahātabbadukaṃ", "nadassanena pahātabb"),
    "kāmāvacare": ("Kāmāvacaradukaṃ", "kāmāvacar"), "nakāmāvacare": ("Kāmāvacaradukaṃ", "nakāmāvacar"),
    "rūpāvacare": ("Rūpāvacaradukaṃ", "rūpāvacar"), "narūpāvacare": ("Rūpāvacaradukaṃ", "narūpāvacar"),
    "naarūpāvacare": ("Arūpāvacaradukaṃ", "naarūpāvacar"), "naarūpe": ("Arūpāvacaradukaṃ", "naarūpāvacar"),
    "niyate": ("Niyatadukaṃ", "niyat"), "avitakke": ("Savitakkadukaṃ", "avitakk"),
    "upādānavippayutte": ("Upādānasampayuttadukaṃ", "upādānavippayutt"),
}
MULA_TERMS = {
    "upādinnamūlake": ("Upādinnadukaṃ", "upādinn"), "anupādinnamūlake": ("Upādinnadukaṃ", "anupādinn"),
    "noupādānamūlake": ("Upādānadukaṃ", "noupādān"),
    "upādānasampayuttamūlake": ("Upādānasampayuttadukaṃ", "upādānasampayutt"),
    "arūpāvacaramūle": ("Arūpāvacaradukaṃ", "arūpāvacar"),
    "dassanena pahātabbamūlakaṃ": ("Dassanenapahātabbadukaṃ", "dassanena pahātabb"),
    "dassanamūlakaṃ": ("Dassanenapahātabbadukaṃ", "dassanena pahātabb"),
    "cittasamuṭṭhānamūlaṃ": ("Cittasamuṭṭhānadukaṃ", "cittasamuṭṭhān"),
}
ABBREV = {"dassane": "dassanena pahātabbe", "nadassane": "nadassanena pahātabbe", "naarūpe": "naarūpāvacare",
          "dassanamūlakaṃ": "dassanena pahātabbamūlakaṃ"}
ABBREV_LOG = set()

_SADIS = re.compile(r"(?:yathā )?(?P<stem>[\wāīūṃṅñṭḍṇḷ ]+?)duka(?P<t>kusala|akusala|abyākata)?sadis(?P<e>aṃ|ā)"
                    r"(?P<v> vitthāretabbaṃ)?")


def sadisa(s, p):
    """«X-duka[-T]-sadisaṃ / -ā [vitthāretabbaṃ]» (yathā: «… တူသည့်အတိုင်း») -> Burmese, or None"""
    n = NS(s)
    m = _SADIS.fullmatch(p)
    if not m:
        return None
    nm = n.dname(m["stem"])
    if nm is None:
        return None
    head = nm + (f"၏ {n.tn(_TRI_T[m['t']])}" if m["t"] else "")
    if m["v"]:
        return f"{head}{s.TAUNG} {s.VITTH}"
    if p.startswith("yathā "):
        return f"{head}{s.LIKE_AS}"
    return head + (s.SADISA if m["e"] == "aṃ" else s.SADISANI)


def count_frag(s, frag):
    """a counting fragment inside a note («nahetuyā nava, najhāne cha», «indriye jhāne cha») through the engine's own
    counting frame (the sentence translated alone, its «။» cut)"""
    my = s.w.F.translate(frag[0].upper() + frag[1:] + ".").strip()
    assert my.endswith(END) and "\n" not in my, my
    return my[:-len(END)]


def loc_piece(s, p):
    """«<term-loc> N» / «<term>-mūlake N» / «<term-loc> sahajātādhipati[yeva]» (positions in a count): Burmese, or None"""
    n = NS(s)
    m = re.fullmatch(r"(.+?)(?: (" + "|".join(s.CNT) + r"))?(?: (sahajātādhipatiyeva|sahajātādhipati))?", p)
    if not m:
        return None
    word, cnt, adh = m[1], m[2], m[3]
    if word in ABBREV:
        ABBREV_LOG.add(f"«{word}» read as «{ABBREV[word]}» (the dyad term abbreviated in a count note)")
    if word in LOC_TERMS:
        h, tk = LOC_TERMS[word]
        out = f"{DV(h, tk)} {s.DH}၌"
    elif word in MULA_TERMS:
        h, tk = MULA_TERMS[word]
        out = f"{DV(h, tk)} {s.DH}{n.MULAKA}၌"
    else:
        return None
    if cnt:
        out += f" {s.CNT[cnt]}"
    if adh:
        out += f" {s.SAA}" + ("သာ" if adh.endswith("yeva") else "")
    return out


def fixed_pieces(s):
    n = NS(s)
    CNT, SAA, AA, DH = s.CNT, s.SAA, s.AA, s.DH
    E = END
    sapp_k = s.comb_n("Sappaccayadukaṃ", "sappaccay", "Kusalattikaṃ", "kusal")
    sapp_a = s.comb_n("Sappaccayadukaṃ", "sappaccay", "Kusalattikaṃ", "akusal")
    nadh = s.w.F.cond("hetu", "loc", True)
    ajj = f"{DV('Ajjhattikadukaṃ', 'ajjhattik')} {DH}" if "Ajjhattikadukaṃ" in DS else ""
    bah = f"{DV('Ajjhattikadukaṃ', 'bāhir')} {DH}" if "Ajjhattikadukaṃ" in DS else ""
    csamu = f"{DV('Cittasamuṭṭhānadukaṃ', 'cittasamuṭṭhān')} {DH}"
    nocsamu = f"{DV('Cittasamuṭṭhānadukaṃ', 'nocittasamuṭṭhān')} {DH}"
    cet = X.DUKA_NAME["Cetasikadukaṃ"]
    aps = s.w.F.LEX["ārammaṇapurejātaṃ"][0]
    vps = s.w.F.LEX["vatthupurejātaṃ"][0]
    return {
        "yathā kusalattike pañhāvāraṃ, evaṃ vitthāretabbaṃ": f"{s.KT}၌ {s.vara('pañhā')}{n.KAYYA} {s.EVAM} {s.VITTH}",
        "yathā kusalattike pañhāvāraṃ evaṃ vitthāretabbaṃ": f"{s.KT}၌ {s.vara('pañhā')}{n.KAYYA} {s.EVAM} {s.VITTH}",
        "yathā sappaccayaṃ kusalaṃ, evaṃ vitthāretabbaṃ": f"{sapp_k}{n.KAYYA} {s.EVAM} {s.VITTH}",
        "yathā sappaccayaṃ akusalaṃ, evaṃ kātabbaṃ": f"{sapp_a}{n.KAYYA} {s.EVAM} {s.KAT}",
        "yathā kusalanayaṃ evaṃ nahetupaccayampi kātabbaṃ":
            f"{n.tn('kusal')}၏ {n.NAYA}{n.KAYYA} {s.EVAM} {s.w.F.cond('hetu', 'pi', True)} {s.KAT}",
        "nahetuyāpi kātabbaṃ": f"{nadh}လည်း {s.KAT}",
        "kusalasadisaṃ": f"{n.tn('kusal')}{s.SADISA}",
        "kusalattikasadisaṃ": f"{s.KT}{s.SADISA}",
        "sabbe kātabbā": f"{s.SAB}ကို {s.KAT}",
        "sabbattha vitthāretabbaṃ": f"{s.SABB} {s.VITTH}",
        "sahajātavārādi vitthāretabbo": f"{s.vara('sahajāta')} {n.ADI} {s.VITTH}",
        "ettha chasu sahajātādhipati": f"{n.IHA} {CNT['cha']}၌ {SAA}",
        "cattāri sahajātādhipati": f"{CNT['cattāri']}သည် {SAA}",
        "majjhe tīṇi sahajātādhipati": f"{s.MAJJHIME} {CNT['tīṇi']}သည် {SAA}",
        "ādimhi tīṇi, sahajātādhipati, majjhimesu tīsu majjhimānulomikāyeva pañhā, sahajātādhipati,":
            f"{n.ADIMHI} {CNT['tīṇi']}{C} {SAA}{C} {s.MAJJHE3} {n.MAJJHANU}{C} {SAA}{C}",
        "ajjhattiko bāhirassa gamanakāle sahajātādhipati, majjhe tīsupi sahajātādhipati":
            f"{ajj}သည် {bah}{n.GAMANAKALE} {SAA}{C} အလယ် {CNT['tīṇi']}လုံး၌ {SAA}",
        "ārammaṇapurejātampi vatthupurejātampi": f"{aps}လည်း{C} {vps}လည်း",
        "ārammaṇapurejātaṃyeva, ghaṭanā dve, ārammaṇapurejātampi vatthupurejātampi":
            f"{aps}သာ{C} {n.GH} {CNT['dve']}{C} {aps}လည်း{C} {vps}လည်း",
        "tiṇṇannaṃ kabaḷīkāro āhāro": f"{CNT['tīṇi']}တို့၌ {n.KABALI}",
        "tiṇṇannaṃ rūpajīvitindriyaṃ": f"{CNT['tīṇi']}တို့၌ {n.RJIVIT}",
        "rūpajīvitindriyaṃ ekaṃ": f"{n.RJIVIT} {CNT['ekaṃ']}",
        "paṭhame dvepi adhipatī, dvīsu sahajātādhipati":
            f"{n.PATHAME} {s.w.F.N['adhipati']} {CNT['dve']}လုံး{C} {CNT['dve']}၌ {SAA}",
        "cittasamuṭṭhānamūlaṃ nocittasamuṭṭhānassa kabaḷīkāro āhāro kātabbo":
            f"{csamu}{n.MULAKA}၌ {nocsamu}အား {n.KABALI}ကို {s.KAT}",
        "nocittasamuṭṭhāno cittasamuṭṭhānassa kabaḷīkāro āhāro ghaṭane majjhe kabaḷīkāro āhāro":
            f"{nocsamu}သည် {csamu}အား {n.KABALI}{C} {n.GH}၌ {s.MAJJHIME} {n.KABALI}",
        "yathā cetasikadukamūlā tīṇi gamanā, evaṃ imepi tīṇi gamanā kātabbā":
            (f"{cet}ကို အခြေခံသော {s.GAMANA} {CNT['tīṇi']}{n.KAYYA} {s.EVAM} ဤ {s.GAMANA} {CNT['tīṇi']}ကိုလည်း "
             f"{s.KAT}"),
        "yathā mahantaraduke cetasikadukakusalasadisaṃ, tattakā eva pañhā":
            f"{C3.MAHANTARA}၌ {cet}၏ {n.tn('kusal')}{s.LIKE_AS}{C} {n.TATTAKA}",
        "yathā cittasampayuttadukaṃ abyākatasadisaṃ":
            f"{X.DUKA_NAME['Cittasampayuttadukaṃ']}၏ {n.tn('abyākat')}{s.LIKE_AS}",
        "yathā kāmāvacaradukaabyākatasadisaṃ, ettakāyeva pañhā heṭṭhuparikaṃ parivattanti":
            f"{X.DUKA_NAME['Kāmāvacaradukaṃ']}၏ {n.tn('abyākat')}{s.LIKE_AS}{C} {n.ETTAKA} {n.PARIV}",
        "kusalampi akusalampi abyākatampi sappītikadukasadisaṃ":
            (f"{n.tn('kusal')}လည်း{C} {n.tn('akusal')}လည်း{C} {n.tn('abyākat')}လည်း "
             f"{X.DUKA_NAME['Sappītikadukaṃ']}{s.SADISA}"),
        "akusalaṃ dhammaṃ paṭicca… paccanīye nahetuyā ekaṃ":
            f"{n.tn('akusal')}ကို မှီ၍{PE} {n.K.ORDER_L['paccanīye']} {count_frag(s, 'nahetuyā ekaṃ')}",
        "abyākataṃ dhammaṃ paṭicca… paccanīye nahetuyā nava… najhāne cha, kātabbā":
            (f"{n.tn('abyākat')}ကို မှီ၍{PE} {n.K.ORDER_L['paccanīye']} {count_frag(s, 'nahetuyā nava')}{PE} "
             f"{count_frag(s, 'najhāne cha')}{C} {s.KAT}"),
        "paccanīye pañhāvāre kusalākusale indriye jhāne cha, pañhāvāre abyākate nava":
            (f"{n.K.ORDER_L['paccanīye']} {s.vara('pañhā')}၌ {n.KUSAK} {count_frag(s, 'indriye jhāne cha')}{C} "
             f"{s.vara('pañhā')}၌ {n.tn('abyākat')}၌ {CNT['nava']}"),
        "pañhāvāre kusalākusale indriye jhāne cha, abyākate nava":
            (f"{s.vara('pañhā')}၌ {n.KUSAK} {count_frag(s, 'indriye jhāne cha')}{C} "
             f"{n.tn('abyākat')}၌ {CNT['nava']}"),
        "upekkhāti nānāupekkhā abyākate": f"{n.tn('abyākat')}၌ {n.NANUPEKKHA}",      # (the place first)
        "paccanīye nahetuyā nava, najhāne cha":
            f"{n.K.ORDER_L['paccanīye']} {count_frag(s, 'nahetuyā nava, najhāne cha')}",
        "evaṃ sabbattha akusalaṃ vitthāretabbaṃ": f"{n.EV} {s.SABB} {n.tn('akusal')}ကို {s.VITTH}",
        "imaṃ gamanaṃ upādānadukaakusalasadisaṃ":
            f"ဤ {s.GAMANA}သည် {X.DUKA_NAME['Upādānadukaṃ']}၏ {n.tn('akusal')}{s.SADISA}",
        "idha pana hetupaccayā idaṃ nānaṃ": f"{n.IHA}{n.PANA} {s.cname('hetu')}၌ {n.IMANANAM}",
        "dassanena pahātabbamūlakaṃ ekaṃ, nadassane dve, ārammaṇādhipati, sahajātādhipati, ekārammaṇādhipati":
            (f"{loc_piece(s, 'dassanena pahātabbamūlakaṃ ekaṃ')}{C} {loc_piece(s, 'nadassane dve')}{C} {AA}{C} "
             f"{SAA}{C} {AA} {CNT['ekaṃ']}"),
        "heṭṭhā tīsu sahajātādhipati, avitakke ekaṃ, sahajātādhipati":
            f"{n.HETTHA} {CNT['tīṇi']}၌ {SAA}{C} {loc_piece(s, 'avitakke ekaṃ')}{C} {SAA}",
        "niyate sahajātādhipati, dutiye ārammaṇādhipati sahajātādhipati":
            f"{loc_piece(s, 'niyate sahajātādhipati')}{C} {n.DUTIYE} {AA}{C} {SAA}",
        "sahajātādhipati": SAA,
        "sahajātādhipatiyeva": f"{SAA}သာ",
        "ghaṭane ekaṃ": f"{n.GH}၌ {CNT['ekaṃ']}",
    }


_FIXED_CACHE = {}
_VL = X._VL


def piece(s, p):
    r = _PIECE0(s, p)
    if r is not None:
        return r
    if s.w.tag not in _FIXED_CACHE:
        _FIXED_CACHE[s.w.tag] = fixed_pieces(s)
    fx = _FIXED_CACHE[s.w.tag]
    if p in fx:
        return new(p, fx[p])
    r = sadisa(s, p)
    if r is not None:
        return new(p, r)
    r = loc_piece(s, p)
    if r is not None:
        return new(p, r)
    # vāra lists (the model's frame) with this group's predicates
    m = re.fullmatch("(?:(kusalattikasadisaṃ) )?(" + _VL + r")(.+)", p)
    if m:
        pre, lst, pred = m[1], m[2], m[3]
        loc = "vārepi" in lst
        if all(("epi" in x[1]) == loc for x in X.VARA_RE.findall(lst)):
            L_ = X.vara_list(s, lst)
            sapp_k = s.comb_n("Sappaccayadukaṃ", "sappaccay", "Kusalattikaṃ", "kusal")
            nom = {"kātabbaṃ": s.KAT, "sabbattha vitthāretabbaṃ": f"{s.SABB} {s.VITTH}"}
            locp = {"vitthāretabbaṃ": s.VITTH, "vitthāretabbo": s.VITTH,
                    "sabbattha vitthāretabbo": f"{s.SABB} {s.VITTH}",
                    "ekaṃ sappaccayakusalasadisaṃ": f"{s.CNT['ekaṃ']} {sapp_k}{s.SADISA}"}
            mm = re.fullmatch(r"sabbattha vitthāretabbaṃ (.+sadisaṃ)", pred)
            if mm and not loc and sadisa(s, mm[1]):
                r = f"{L_} {s.SABB} {sadisa(s, mm[1] + ' vitthāretabbaṃ')}"
            elif pre and not loc and pred == "vitthāretabbaṃ":
                r = f"{s.KT}{s.TAUNG} {L_} {s.VITTH}"
            elif not pre:
                r = (locp if loc else nom).get(pred)
                r = r and f"{L_} {r}"
            if r:
                return new(p, r)
    return None


X.piece = piece

# ===================================================================================== special terms, headings
# 4-10 ^7-44-41 (2 lines): «nocittasaṃsaṭṭha» (written for the Mātikā's «cittavisaṃsaṭṭha»): translated as written, the
# pattern of «no cittasamuṭṭhāna» «စိတ်မှ ဖြစ်ပေါ်လာသည် မဟုတ်သော» (NEW; logged)
WC.DYADS["cittasams"]["nocittasaṃsaṭṭh"] = new("nocittasaṃsaṭṭho (dyad term, as written)",
                                               "စိတ်နှင့် ရောနှောသည် မဟုတ်သော")
DS["Cittasaṃsaṭṭhadukaṃ"].append(("cittasams", "nocittasaṃsaṭṭh", _ci("nocittasaṃsaṭṭh") + _EA))
SLIPS.add("4-10 ^7-44-41 (2 lines): «nocittasaṃsaṭṭha» for «cittavisaṃsaṭṭha» (translated as written)")

# 4-13 ^7-47-59: «Upekkhāsahagatañca naupekkhāsahagatañca dhammaṃ» (no triad word, as written): the two dyad terms
# alone on the noun (two extra keys of that part's table; nothing supplied)
_UP_TAB = X.combo("Upekkhāsahagatadukaṃ", "Kusalattikaṃ")
BARE = {}
for _tk in ("upekkhāsahagat", "naupekkhāsahagat"):
    _key = X._skey(X._N[0])
    X._N[0] += 1
    _UP_TAB[_key] = DV("Upekkhāsahagatadukaṃ", _tk)
    X.COMBO_PALI[_key] = ("Upekkhāsahagatadukaṃ", _tk, None, None)
    BARE[_tk] = _key
_BARE_PALI = "Upekkhāsahagatañca naupekkhāsahagatañca dhammaṃ"
READ = {_BARE_PALI: f"{BARE['upekkhāsahagat'][0].upper()}{BARE['upekkhāsahagat'][1:]}añca "
                    f"{BARE['naupekkhāsahagat']}añca dhammaṃ",
        # 4-12 ^7-46-4: «… uddhaccasahagato moho (1).» (the digit before the full stop): read with the stop first,
        # the Burmese then put back in the Pāli order (POSTFIX)
        "uddhaccasahagato moho (1).": "uddhaccasahagato moho. (1)"}
POSTFIX = [("uddhaccasahagato moho (1).", "မောဟ။ (1)", "မောဟ (1)။")]
SLIP_FIX = {"kusalaṃ dhamma paṭicca": "kusalaṃ dhammaṃ paṭicca",          # 4-13 ^7-47-11 «dhamma» for dhammaṃ
            "*Hetuārammaṇapaccayādi*": "*Hetu-ārammaṇapaccayādi*",          # 4-10 heading without hyphen
            "nahetuyāpi kattabbaṃ": "nahetuyāpi kātabbaṃ"}                   # 4-10 ^7-44-14 «kattabbaṃ»
for _a, _b in SLIP_FIX.items():
    assert _a not in X.SLIP_FIX
X.SLIP_FIX.update(SLIP_FIX)
X.READ.update(READ)
READ_LOG.add(f"4-13 ^7-47-59 «{_BARE_PALI}» (no triad word): the dyad terms alone, as written")


def setup_lex():
    # 4-10 ^7-44-100 «upādinne khandhe ca mahābhūte ca paṭicca …»: «upādinne» the dyad term on the noun (pi-1 ^1-M2-68)
    for mod in (WC.F, WC.FG):
        mod.add_qual(C3.UPADINNA_T, "upādinne")
        mod.LEX.setdefault("upādinne", (C3.UPADINNA_T, "adj"))
    # 4-13 ^7-47-61 «… uppajjati hetupaccayā nava pañhā (…)»: the count of questions after the verb (as 3-09's
    # «… uppajjati §C§ā pañca»)
    for mod in (WE.F, WE.FG):
        mod.SKF["§T§aṃ dhammaṃ paṭicca §T§o dhammo uppajjati §C§ā nava pañhā"] = new(
            "… uppajjati Xpaccayā nava pañhā",
            f"{{T1}} {mod.DHAMMA}ကို မှီ၍ {{T2}} {mod.DHAMMA}သည် {{C1.ab}} {mod.UP} {WE.D.PANHA} {mod.COUNT['nava']}")


def setup_heads():
    """headings and colophons this group adds (the finished groups' names)"""
    X.GOC_NAME["Kilesagocchaka"] = E4.GOCCHAKA["Kilesagocchakaṃ"]
    X.GOC_NAME["Mahantaraduka"] = C3.MAHANTARA
    X.GOC_NAME["Piṭṭhiduka"] = E4.GOCCHAKA["Piṭṭhidukaṃ"]
    for w in (WC, WB, WE):
        F = w.F
        hl = {"Paccayacatukkaṃ": new("Paccayacatukkaṃ (heading)", f"{F.PACCAYA} {F.GROUP['catukka']}"),
              "*Hetu-ārammaṇa-adhipatipaccayā*": new(
                  "*Hetu-ārammaṇa-adhipatipaccayā*",
                  "*" + F._join_and([F.cond(c, "n") for c in ("hetu", "ārammaṇa", "adhipati")]) + "*")}
        F.HLINES.update(hl)


setup_lex()
setup_heads()

# ===================================================================================== the run


def translate(name):
    w = WORLD_OF[name[:4]]
    src = (PALI / name).read_text(encoding="utf-8-sig")
    parts = X.parts_of(src)
    for dh, _, _, _ in parts:
        assert dyad_world_of(dh) is w, (name, dh)
    hl = X.heading_lines(w, parts)
    hl["Dhammānulome dukatikapaṭṭhānaṃ niṭṭhitaṃ."] = w.F.finished(hl["Dhammānulome dukatikapaṭṭhānaṃ"])
    w.F.HLINES.update(hl)
    if w is WC:
        C3.MY_RUN[0] = True
        C3.gate(True)
    try:
        txt = "\n".join(X.translate_part(w, dh, th, t) for dh, th, _, t in parts)
    finally:
        if w is WC:
            C3.MY_RUN[0] = False
            C3.gate(False)
    return postfix(src, txt)


def postfix(src, txt):
    """the Burmese of a line read in another order put back in the Pāli order (POSTFIX; logged)"""
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
            for dh, th, _, _ in X.parts_of((PALI / n).read_text(encoding="utf-8-sig")):
                for k, v in X.combo(dh, th).items():
                    print(n, k, X.COMBO_PALI[k], v, sep="\t")
        return
    dev = "--dev" in sys.argv or "--new" in sys.argv
    worlds = (WC, WB, WE)
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
        for k, v in list(X.NEW.items()) + list(NEW.items()):
            print(f"{k} = {v}")
        print("readings:", *sorted(READ_LOG | X.READ_LOG | ABBREV_LOG), sep="\n  ")
    if "--slips" in sys.argv:
        print("slips:", *sorted(SLIPS | X.SLIPS | WC.F.SLIPS | WB.F.SLIPS | WE.F.SLIPS), sep="\n  ")


if __name__ == "__main__":
    main()
