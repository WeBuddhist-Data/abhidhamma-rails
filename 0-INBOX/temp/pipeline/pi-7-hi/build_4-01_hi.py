"""Hindi builder for pi-7 4-01-kilesagocchaka.md (the defilement cluster and the final dyads).

Run:
    python -I -B -X utf8 build_4-01_hi.py            # write the Hindi file and check it
    python -I -B -X utf8 build_4-01_hi.py --missing  # list Pāli segments that have no Hindi yet
    python -I -B -X utf8 build_4-01_hi.py --check    # check only

Every line is composed from fixed frames (imported from build_sample_hi.py) and the segment tables in
segs_4-01_hi.py; repeated Pāli therefore always yields byte-identical Hindi.
Item words of the current dyad are replaced by placeholders before lookup ({P:o}, {N:aṃ}, ...), so a
segment translated once serves every dyad; Hindi templates use {Pf} {Pm} {Pms} {Pn} {Pno} / {Nf} ...
"""
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import build_sample_hi as S  # noqa: E402

FNAME = "4-01-kilesagocchaka.md"
PALI = S.PALI_DIR / FNAME
OUT = S.HI_DIR / FNAME

# =====================================================================================
# 1. Dyad items
# =====================================================================================
GEN_RULES = [("वाली", "वाले", "वाला"), ("जुड़ी", "जुड़े", "जुड़ा"), ("छोड़ी", "छोड़े", "छोड़ा"),
             ("समाई", "समाए", "समाया"), ("हुई", "हुए", "हुआ")]


def gform(f, g):
    """Feminine adjective phrase -> masculine plural/oblique (g='m') or masculine singular (g='ms')."""
    if g == "f":
        return f
    idx = 1 if g == "m" else 2
    words = f.split(" ")
    out = []
    for w in words:
        core = w.rstrip(",")
        tail = w[len(core):]
        for r in GEN_RULES:
            if core == r[0]:
                core = r[idx]
                break
        out.append(core + tail)
    return " ".join(out)


class Item:
    def __init__(self, f, noun=None, noun_obl=None):
        self.f = f
        self.noun = noun or f"{f} {S.DHAMMA_PL}"
        self.noun_obl = noun_obl or f"{f} {S.DHAMMA_OBL_PL}"

    def forms(self, tag):
        return {f"{tag}f": self.f, f"{tag}m": gform(self.f, "m"), f"{tag}ms": gform(self.f, "ms"),
                f"{tag}n": self.noun, f"{tag}no": self.noun_obl}


KL = "मन के क्लेश रूपी"
KL_NOT = "मन के क्लेश रूपी न होने वाली"
SK = "क्लेशों का विषय बनने वाली"
SKT = "क्लेशों से मलिन"
KSP = "क्लेशों से जुड़ी"

# key: (heading Pāli, heading Hindi, kind, P regex stem, N regex stem, P item, N item)
# kind "s" = simple one-word items (stem + ending); "c" = compound (handled by COMPOUND below)
DYADS = [
    ("kilesa", "Kilesadukaṃ", "मन के क्लेश वाला दो का वर्गीकरण", "s", "kiles", "nokiles",
     Item(KL, "मन के क्लेश", "मन के क्लेशों"), Item(KL_NOT)),
    ("saṃkilesika", "Saṃkilesikadukaṃ", "क्लेशों का विषय बनने वाला दो का वर्गीकरण", "s",
     "saṃkilesik", "asaṃkilesik", Item(SK), Item("क्लेशों का विषय न बनने वाली")),
    ("saṃkiliṭṭha", "Saṃkiliṭṭhadukaṃ", "क्लेशों से मलिन वाला दो का वर्गीकरण", "s",
     "saṃkiliṭṭh", "asaṃkiliṭṭh", Item(SKT), Item("क्लेशों से मलिन न होने वाली")),
    ("kilesasampayutta", "Kilesasampayuttadukaṃ", "क्लेशों से जुड़ाव वाला दो का वर्गीकरण", "s",
     "kilesasampayutt", "kilesavippayutt", Item(KSP), Item("क्लेशों से अलग")),
    ("kilesasaṃkilesika", "Kilesasaṃkilesikadukaṃ",
     "मन के क्लेश और क्लेशों का विषय बनने वाला दो का वर्गीकरण", "c", ("kiles", "saṃkilesik"), None,
     Item(f"{KL} भी और {SK} भी"), Item(f"{SK}, पर स्वयं {KL_NOT}")),
    ("kilesasaṃkiliṭṭha", "Kilesasaṃkiliṭṭhadukaṃ", "मन के क्लेश और क्लेशों से मलिन वाला दो का वर्गीकरण", "c",
     ("kiles", "saṃkiliṭṭh"), None,
     Item(f"{KL} भी और {SKT} भी"), Item(f"{SKT}, पर स्वयं {KL_NOT}")),
    ("kilesakilesasampayutta", "Kilesakilesasampayuttadukaṃ",
     "मन के क्लेश और क्लेशों से जुड़ाव वाला दो का वर्गीकरण", "c", ("kiles", "kilesasampayutt"), None,
     Item(f"{KL} भी और {KSP} भी"), Item(f"{KSP}, पर स्वयं {KL_NOT}")),
    ("kilesavippayuttasaṃkilesika", "Kilesavippayuttasaṃkilesikadukaṃ",
     "क्लेशों से अलगाव और क्लेशों का विषय बनने वाला दो का वर्गीकरण", "v", None, None,
     Item(f"क्लेशों से अलग, पर {SK}"), Item("क्लेशों से अलग और क्लेशों का विषय न बनने वाली")),
    ("dassanena", "Dassanenapahātabbadukaṃ", "सत्य-दर्शन से छोड़े जाने वाला दो का वर्गीकरण", "s",
     "dassanena ?pahātabb(?!ahetuk)", "nadassanena ?pahātabb(?!ahetuk)",
     Item("सत्य-दर्शन से छोड़ी जाने वाली"), Item("सत्य-दर्शन से न छोड़ी जाने वाली")),
    ("bhāvanāya", "Bhāvanāyapahātabbadukaṃ", "मानसिक अभ्यास से छोड़े जाने वाला दो का वर्गीकरण", "s",
     "bhāvanāya ?pahātabb(?!ahetuk)", "nabhāvanāya ?pahātabb(?!ahetuk)",
     Item("मानसिक अभ्यास से छोड़ी जाने वाली"), Item("मानसिक अभ्यास से न छोड़ी जाने वाली")),
    ("dassanenahetuka", "Dassanenapahātabbahetukadukaṃ",
     "सत्य-दर्शन से छोड़े जाने वाले मूलों वाला दो का वर्गीकरण", "s",
     "dassanena ?pahātabbahetuk", "nadassanena ?pahātabbahetuk",
     Item("सत्य-दर्शन से छोड़े जाने वाले मूलों वाली"), Item("सत्य-दर्शन से छोड़े जाने वाले मूलों से रहित")),
    ("bhāvanāyahetuka", "Bhāvanāyapahātabbahetukadukaṃ",
     "मानसिक अभ्यास से छोड़े जाने वाले मूलों वाला दो का वर्गीकरण", "s",
     "bhāvanāya ?pahātabbahetuk", "nabhāvanāya ?pahātabbahetuk",
     Item("मानसिक अभ्यास से छोड़े जाने वाले मूलों वाली"),
     Item("मानसिक अभ्यास से छोड़े जाने वाले मूलों से रहित")),
    ("savitakka", "Savitakkadukaṃ", "आरंभिक विचार वाला दो का वर्गीकरण", "s", "savitakk", "avitakk",
     Item("आरंभिक विचार वाली"), Item("आरंभिक विचार से रहित")),
    ("savicāra", "Savicāradukaṃ", "सतत विचार वाला दो का वर्गीकरण", "s", "savicār", "avicār",
     Item("सतत विचार वाली"), Item("सतत विचार से रहित")),
    ("sappītika", "Sappītikadukaṃ", "उल्लास वाला दो का वर्गीकरण", "s", "sappītik", "appītik",
     Item("उल्लास वाली"), Item("उल्लास से रहित")),
    ("pītisahagata", "Pītisahagatadukaṃ", "उल्लास के साथ होने वाला दो का वर्गीकरण", "s",
     "pītisahagat", "napītisahagat", Item("उल्लास के साथ होने वाली"), Item("उल्लास के साथ न होने वाली")),
    ("sukhasahagata", "Sukhasahagatadukaṃ", "सुख के साथ होने वाला दो का वर्गीकरण", "s",
     "sukhasahagat", "nasukhasahagat", Item("सुख के साथ होने वाली"), Item("सुख के साथ न होने वाली")),
    ("upekkhāsahagata", "Upekkhāsahagatadukaṃ", "समभाव के साथ होने वाला दो का वर्गीकरण", "s",
     "upekkhāsahagat", "naupekkhāsahagat",
     Item("समभाव के साथ होने वाली"), Item("समभाव के साथ न होने वाली")),
    ("kāmāvacara", "Kāmāvacaradukaṃ", "इंद्रिय-सुखों के लोक वाला दो का वर्गीकरण", "s",
     "kāmāvacar", "nakāmāvacar", Item("इंद्रिय-सुखों के लोक से संबंधित"),
     Item("इंद्रिय-सुखों के लोक से संबंधित न होने वाली")),
    ("rūpāvacara", "Rūpāvacaradukaṃ", "सूक्ष्म भौतिक लोक वाला दो का वर्गीकरण", "s",
     "rūpāvacar", "narūpāvacar", Item("सूक्ष्म भौतिक लोक से संबंधित"),
     Item("सूक्ष्म भौतिक लोक से संबंधित न होने वाली")),
    ("arūpāvacara", "Arūpāvacaradukaṃ", "अभौतिक लोक वाला दो का वर्गीकरण", "s",
     "arūpāvacar", "naarūpāvacar", Item("अभौतिक लोक से संबंधित"),
     Item("अभौतिक लोक से संबंधित न होने वाली")),
    ("pariyāpanna", "Pariyāpannadukaṃ", "अस्तित्व के लोकों में समाए होने वाला दो का वर्गीकरण", "s",
     "pariyāpann", "apariyāpann", Item("अस्तित्व के लोकों में समाई हुई"),
     Item("अस्तित्व के लोकों में न समाई हुई")),
    ("niyyānika", "Niyyānikadukaṃ", "मुक्ति की ओर ले जाने वाला दो का वर्गीकरण", "s",
     "niyyānik", "aniyyānik", Item("मुक्ति की ओर ले जाने वाली"), Item("मुक्ति की ओर न ले जाने वाली")),
    ("niyata", "Niyatadukaṃ", "निश्चित वाला दो का वर्गीकरण", "s", "niyat", "aniyat",
     Item("निश्चित"), Item("अनिश्चित")),
    ("sauttara", "Sauttaradukaṃ", "सर्वोच्च न होने वाला दो का वर्गीकरण", "s", "sauttar", "anuttar",
     Item("सर्वोच्च न होने वाली"), Item("सर्वोच्च")),
    ("saraṇa", "Saraṇadukaṃ", "संघर्ष वाला दो का वर्गीकरण", "s", "saraṇ", "araṇ",
     Item("संघर्ष वाली"), Item("संघर्ष से रहित")),
]
DYAD = {d[0]: d for d in DYADS}
DYAD_BY_HEAD = {d[1]: d[0] for d in DYADS}
COMPOUND = {d[0] for d in DYADS if d[3] in ("c", "v")}


def item_fields(dkey):
    d = DYAD[dkey]
    m = {}
    m.update(d[6].forms("P"))
    m.update(d[7].forms("N"))
    return m


def _tag(end):
    """Pāli ending -> (case tag, trailing 'ca'?)"""
    ca = False
    if end.endswith("ñceva"):
        end = end[:-5] + "ṃ"
    elif end.endswith("ñca"):
        end, ca = end[:-3] + "ṃ", True
    return end, ca


def normalize(text, dkey):
    """Replace the current dyad's item words with {P:tag} / {N:tag}."""
    if dkey is None:
        return text
    d = DYAD[dkey]
    kind = d[3]

    def ph(side, end):
        tag, ca = _tag(end)
        return "{" + side + ":" + tag + "}" + (" ca" if ca else "")

    if kind == "s":
        pstem, nstem = d[4], d[5]
        text = re.sub(r"\b" + nstem + r"(\w*)", lambda m: ph("N", m.group(1)), text, flags=re.I)
        text = re.sub(r"\b" + pstem + r"(\w*)", lambda m: ph("P", m.group(1)), text, flags=re.I)
        if dkey in TSTEM:
            text = re.sub(r"\b" + TSTEM[dkey][0] + r"(\w*)", lambda m: tph(m.group(1)), text, flags=re.I)
        return text
    if kind == "c":
        a, b = d[4]   # kiles, saṃkilesik
        # N: "<b>X ceva no ca <a>Y" / "<b>Xñceva no ca <a>Y"
        rxn = re.compile(r"\b" + b + r"(\w*?)(ñceva| ceva) no ca " + a + r"(\w*)", re.I)

        def fn(m):
            end = m.group(1) + ("ṃ" if m.group(2) == "ñceva" else "")
            tail = m.group(3)
            if tail.endswith("dhipati"):
                end = "ādhipati"
            return "{N:" + end + "}" + (" ca" if tail.endswith("ñca") else "")
        text = rxn.sub(fn, text)
        rxp = re.compile(r"\b" + a + r"(\w*?)(ñceva| ceva) " + b + r"(\w*?)(ñca| ca)\b", re.I)

        def fp(m):
            end = m.group(1) + ("ṃ" if m.group(2) == "ñceva" else "")
            return "{P:" + end + "}"
        text = rxp.sub(fp, text)
        return K_RX.sub(lambda m: ph("K", m.group(1)), text)
    if kind == "v":
        text = re.sub(r"\bkilesavippayutt(\w*) asaṃkilesik(\w*)", lambda m: ph("N", m.group(2)), text, flags=re.I)
        text = re.sub(r"\bkilesavippayutt(\w*) saṃkilesik(\w*)", lambda m: ph("P", m.group(2)), text, flags=re.I)
        return K_RX.sub(lambda m: ph("K", m.group(1)), text)
    return text


# the "third term" of a dyad (vitakka in the savitakka dyad, pīti in the sappītika dyad, ...) -> {T:case}
TSTEM = {"savitakka": ("vitakk", "आरंभिक विचार"), "savicāra": ("vicār", "सतत विचार"),
         "sappītika": ("pīti", "उल्लास"), "pītisahagata": ("pīti", "उल्लास"),
         "sukhasahagata": ("sukh", "सुख"), "upekkhāsahagata": ("upekkh", "समभाव")}
# nominative and accusative render the same Hindi ("{T}"), and sukhaṃ is both: one tag "nom" for both
TCASE = {"o": "nom", "": "nom", "ā": "nom", "aṃ": "nom", "ṃ": "nom", "assa": "dat", "yā": "dat", "āya": "dat"}


def tph(end):
    ca = False
    if end.endswith("ñca"):
        end, ca = end[:-3] + "ṃ", True
    c = TCASE.get(end)
    if c is None:
        return None or ("{T:" + end + "}")
    return "{T:" + c + "}" + (" ca" if ca else "")


# bare defilement nouns (kilesā, kilese ...) outside the kilesa dyad itself -> {K:tag}
K_RX = re.compile(r"\bkiles(o|aṃ|assa|ā|ānaṃ|e|añca|ānañca|āya)\b", re.I)
K_FIELDS = Item(KL, "मन के क्लेश", "मन के क्लेशों").forms("K")
K_FIELDS.update({"Ks": "मन का क्लेश", "Kso": "मन के क्लेश"})   # singular kileso / kilesaṃ


# =====================================================================================
# 2. Frames
# =====================================================================================
ITEM_RX = r"\{[PN]:[^}]*\}"
ITEMS_RX = rf"{ITEM_RX}(?: ca)?(?: {ITEM_RX}(?: ca)?)*"
DEP_PALI = {"paṭicca": "paṭicca", "paccayā": "paccaya", "nissāya": "nissaya", "saṃsaṭṭho": "saṃsaṭṭha",
            "saṃsaṭṭhā": "saṃsaṭṭha", "sampayutto": "sampayutta", "sampayuttā": "sampayutta",
            "sahajāto": "sahajāta", "sahajātā": "sahajāta"}
FRAME_A = re.compile(rf"^(?P<o>{ITEMS_RX}) dhammaṃ (?P<dep>{'|'.join(DEP_PALI)}) (?P<r>{ITEMS_RX}) "
                     rf"(?:dhammo|dhammā) (?:uppajjati|uppajjanti) (?P<c>\w+paccayā)$")
FRAME_B = re.compile(rf"^(?P<s>{ITEMS_RX}) (?:dhammo|dhammā) (?P<d>{ITEMS_RX}) dhammassa "
                     rf"(?P<c>\w+)paccayena paccayo$")
FRAME_B0 = re.compile(r"^(?P<c>\w+)paccayena paccayo$")
FRAME_B2 = re.compile(rf"^(?P<s>{ITEMS_RX}) (?:dhammo|dhammā) (?P<d>{ITEMS_RX}) dhammassa (?P<rest>.+)$")
COND_ABL = re.compile(r"^(na|no)?(" + "|".join(sorted(S.COND_KEYS, key=len, reverse=True)) + r")paccayā$")
COND_STEM = re.compile(r"^(" + "|".join(sorted(S.COND_KEYS, key=len, reverse=True)) + r")$")


TYPEW_B2 = {"sahajātaṃ": "सह-उत्पत्ति के रूप में", "purejātaṃ": "पूर्व-उत्पत्ति के रूप में",
            "pacchājātaṃ": "पश्चात्-उत्पत्ति के रूप में", "āhāraṃ": "आहार के रूप में",
            "indriyaṃ": "क्षमता के रूप में"}


def sides(s):
    return re.findall(r"\{([PN]):[^}]*\}", s)


class Ctx:
    def __init__(self, dkey):
        self.dkey = dkey
        self.f = dict(K_FIELDS)
        if dkey:
            self.f.update(item_fields(dkey))
        if dkey in TSTEM:
            self.f["T"] = TSTEM[dkey][1]
        self.f["DEP"] = S.DEP["paṭicca"]
        self.f["VB"] = "होता है"
        self.compound = dkey in COMPOUND
        self.plural = False   # agreement of a subject-less "...paccayena paccayo" in the same line
        self.b2 = False       # "X dhammā Y dhammassa sahajātaṃ… purejātaṃ" line: bare type words = "… के रूप में"

    def it(self, side, g="f"):
        return self.f[side + g]

    def obj(self, ss):
        w = [f"{self.it(x)} {S.DHAMMA}" for x in ss]
        return w[0] if len(w) == 1 else ", ".join(w[:-1]) + " और " + w[-1]

    def res(self, ss):
        if len(ss) == 1:
            return f"{self.it(ss[0])} {S.DHAMMA}"
        if self.compound:
            return self.obj(ss)
        w = [self.it(x) for x in ss]
        return ", ".join(w[:-1]) + " और " + w[-1] + " " + S.DHAMMA_PL

    def dat(self, ss):
        return self.obj(ss) + " के लिए"


def cond_abl(c):
    m = COND_ABL.match(c)
    if not m:
        return None
    return S.NABL(m.group(2)) if m.group(1) else S.ABL(m.group(2))


def frame(seg, ctx):
    """Try the fixed frames on a normalized segment (first letter lower-case). Return Hindi or None."""
    m = FRAME_A.match(seg)
    if m:
        c = cond_abl(m.group("c"))
        if c is None:
            return None
        o, r = sides(m.group("o")), sides(m.group("r"))
        dep = S.DEP[DEP_PALI[m.group("dep")]]
        ctx.f["DEP"] = dep
        verb = "उत्पन्न होती हैं" if len(r) > 1 else "उत्पन्न होती है"
        return f"{ctx.obj(o)} {dep} {ctx.res(r)} {c} {verb}"
    m = FRAME_B.match(seg)
    if m and COND_STEM.match(m.group("c")):
        s, d = sides(m.group("s")), sides(m.group("d"))
        ctx.plural = len(s) > 1
        verb = "होती हैं" if ctx.plural else "होती है"
        return f"{ctx.res(s)}, {ctx.dat(d)} {S.INS(m.group('c'))} {verb}"
    m = FRAME_B2.match(seg)
    if m:
        toks = re.split(r"(…\s?|, )", m.group("rest"))
        if all((t in TYPEW_B2) for t in toks[0::2]):
            s, d = sides(m.group("s")), sides(m.group("d"))
            ctx.b2 = True
            rest = "".join(TYPEW_B2[t] if j % 2 == 0 else t for j, t in enumerate(toks))
            return f"{ctx.res(s)}, {ctx.dat(d)} {rest}"
    if ctx.b2 and seg in TYPEW_B2:
        return TYPEW_B2[seg]
    m = FRAME_B0.match(seg)
    if m and COND_STEM.match(m.group("c")):
        verb = "होती हैं" if ctx.plural else "होती है"
        return f"{S.INS(m.group('c'))} {verb}"
    c = cond_abl(seg)
    if c is not None:
        return c
    if seg in S.NUM:
        return S.NUM[seg]
    m = re.match(r"^(\S+) (\S+)$", seg)      # "hetuyā cha" inside a prose line
    if m and m.group(2) in S.NUM:
        kind, v = S._classify(m.group(1))
        if kind in ("loc", "neg_loc"):
            return f"{(S.LOC if kind == 'loc' else S.NLOC)(v)} {S.NUM[m.group(2)]}"
    return None


# =====================================================================================
# 3. Segment tables
# =====================================================================================
SEGS_FILE = HERE / "segs_4-01_hi.py"
_ns = {"S": S, "__name__": "segs_4_01_hi"}
exec(compile(SEGS_FILE.read_text(encoding="utf-8"), str(SEGS_FILE), "exec"), _ns)
G = {}
for k, v in _ns["G"].items():
    G[k[0].lower() + k[1:]] = v
DY = {dk: {k[0].lower() + k[1:]: v for k, v in tab.items()} for dk, tab in _ns.get("DY", {}).items()}
PAREN = {k: v for k, v in _ns["PAREN"].items()}
HEAD = dict(_ns["HEAD"])
for d in DYADS:
    HEAD.setdefault(d[1], d[2])
LINE = dict(_ns.get("LINE", {}))   # whole-line overrides keyed by block-less Pāli line
GEN = _ns.get("GEN")               # GEN(key, dkey) -> Hindi template or None (rule-generated segments)

MISSING = {}
SENT = {}


def miss(key, where):
    MISSING.setdefault(key, where)
    return "⟪" + key + "⟫"


def lookup(key, ctx):
    k = key[0].lower() + key[1:] if key else key
    tab = DY.get(ctx.dkey, {})
    alt = k.replace("{P:", "{K:") if ctx.dkey == "kilesa" else None
    if k in tab:
        v = tab[k]
    elif k in G:
        v = G[k]
    elif alt and alt in G:
        v = G[alt]
    else:
        v = GEN(k, ctx.dkey) if GEN else None
        if v is None and alt:
            v = GEN(alt, ctx.dkey) if GEN else None
        if v is None:
            return None
    try:
        return v.format_map(ctx.f) if "{" in v else v
    except KeyError as e:
        raise SystemExit(f"template field {e} missing for dyad {ctx.dkey}: {key!r}")


# =====================================================================================
# 4. Line translation
# =====================================================================================
VAR_RX = re.compile(r"\{([^{}]*?) \(([^()]*)\)\}")
PAREN_RX = re.compile(r"\([^()]*\)")
STRONG = re.compile(r"( – |\. |; |\.$)")
WEAK = re.compile(r"(…pe…|…|\s*⟦P\d+⟧\s*)")
COMMA = re.compile(r"(, )")
SEPMAP = {" – ": " – ", ". ": "। ", "; ": "; ", ".": "।", "…pe…": "…", "…": "…", ", ": ", "}


def sigla(s):
    return ", ".join(w.strip().capitalize() for w in s.split(" ") if w.strip()).replace("..", ".")


def variants(text):
    """{thīnaṃ (sī. syā.)} -> ⟦V0⟧ with its Hindi bracket."""
    toks = {}

    def f(m):
        n = f"⟦V{len(toks)}⟧"
        sig = sigla(m.group(2))
        toks[n] = f"[वर्तनी-भेद ({sig}): {m.group(1)}]"
        return n
    return VAR_RX.sub(f, text), toks


def tr_paren(p, ctx, where):
    inner = p[1:-1]
    if re.fullmatch(r"\d+", inner):
        return p
    key = normalize(inner, ctx.dkey)
    key = key[0].lower() + key[1:]
    tab = DY.get(ctx.dkey, {})
    v = tab.get("(" + key + ")", PAREN.get(key))
    if v is None:
        return miss("(" + key + ")", where)
    return "(" + (v.format_map(ctx.f) if "{" in v else v) + ")"


def tr_piece(seg, ctx, where):
    """Translate a piece without separators; tokens ⟦..⟧ at the edges are passed through."""
    lead = re.match(r"^(\s*(?:⟦[^⟧]*⟧\s*)*)", seg).group(1)
    rest = seg[len(lead):]
    trail = re.search(r"((?:\s*⟦[^⟧]*⟧)*\s*)$", rest).group(1)
    core = rest[:len(rest) - len(trail)] if trail else rest
    if not core.strip():
        return seg
    c = core.strip()
    lsp = core[:len(core) - len(core.lstrip())]
    tsp = core[len(core.rstrip()):]
    key = c[0].lower() + c[1:]
    if re.match(r"^\{[PNK]:ā\} (khandhā|hetū)", key):
        ctx.f["VB"] = "होते हैं"
    elif key.startswith("nibbānaṃ"):
        ctx.f["VB"] = "होता है"
    h = frame(key, ctx)
    if h is None:
        h = lookup(key, ctx)
    if h is None:
        cm = re.match(r"^(.*\S) niṭṭhitaṃ$", c)
        if cm and cm.group(1) in HEAD:
            h = HEAD[cm.group(1)] + " समाप्त"
    if h is None:
        return None
    return lead + lsp + h + tsp + trail


def tr_level(text, ctx, where, level):
    rx = [STRONG, WEAK, COMMA][level]
    parts = rx.split(text)
    out = []
    for i, p in enumerate(parts):
        if i % 2 == 1:
            out.append(SEPMAP.get(p, p))
            continue
        if p == "":
            out.append("")
            continue
        # case of a bare object before "…pe…": "आँख का…" before assādeti, else "आँख को…"
        ahead = "".join(parts[i + 1:])
        mv = re.search(r"assādeti|garuṃ katvā|aniccato|upanissāya|ārabbha|paccavekkhati|paccavekkhanti", ahead)
        ctx.f["KO"] = "का" if (mv and mv.group(0) == "assādeti") else "को"
        h = tr_piece(p, ctx, where)
        if h is None and level == 0:
            k0 = re.sub(r"⟦P\d+⟧", "", p).strip()
            SENT.setdefault(k0[0].lower() + k0[1:] if k0 else k0, where)
        if h is None:
            if level < 2:
                h = tr_level(p, ctx, where, level + 1)
            else:
                key = re.sub(r"⟦P\d+⟧", "", p).strip()
                key = key[0].lower() + key[1:] if key else key
                h = miss(key, where)
        out.append(h)
    return "".join(out)


def tr_body(text, ctx, where):
    text, vt = variants(text)
    ptoks = {}

    def pf(m):
        n = f"⟦P{len(ptoks)}⟧"
        ptoks[n] = m.group(0)
        return n
    text = PAREN_RX.sub(pf, text)
    text = normalize(text, ctx.dkey)
    h = tr_level(text, ctx, where, 0)
    for n, p in ptoks.items():
        h = h.replace(n, tr_paren(p, ctx, where))
    for n, v in vt.items():
        h = h.replace(n, v)
    return h


# ---- counting lines ------------------------------------------------------------------
CNT_TOK = re.compile(r"…pe…|…|\([^()]*\)|[,;.]|na [^\s,;.…()]+|[^\s,;.…()]+")


def count_line(pali, ctx, where):
    """S.count_hi extended: any parenthesis is a pass-through note (PAREN table)."""
    toks = CNT_TOK.findall(pali)
    items = []
    for t in toks:
        if t in ("…pe…", "…"):
            items.append(("ell", "…"))
        elif t.startswith("("):
            items.append(("paren", t))
        elif t in ",;.":
            items.append(("punct", t))
        else:
            kind, v = S._classify(t.replace(" ", ""))
            if kind == "other":
                return None
            items.append((kind, v))
    if not any(k in ("loc", "neg_loc") for k, _ in items):
        return None
    words = ("abl", "neg_abl", "loc", "neg_loc", "num", "paren")
    out = ""
    for i, (kind, v) in enumerate(items):
        nxt = items[i + 1][0] if i + 1 < len(items) else None
        if kind in words:
            if kind == "paren":
                text = tr_paren(v, ctx, where)
            elif kind == "num":
                text = S.NUM[v]
            else:
                text = {"abl": S.ABL, "neg_abl": S.NABL, "loc": S.LOC, "neg_loc": S.NLOC}[kind](v)
            if kind in ("abl", "neg_abl", "num") and nxt in ("abl", "neg_abl", "loc", "neg_loc", "num"):
                text += ","
            if out and not out.endswith(" "):
                out += " "
            out += text
        else:
            out = out.rstrip(" ").rstrip(",") + ("…" if kind == "ell" else ("।" if v == "." else v))
    return out.strip()


# ---- headings ------------------------------------------------------------------------
def tr_heading(line, ctx):
    hashes = line[:len(line) - len(line.lstrip("#"))]
    body = line[len(hashes):].strip()
    star = body.startswith("*") and body.endswith("*")
    core = body.strip("*")
    m = re.match(r"^(\d-\d\. )(.*)$", core)
    pre, name = (m.group(1), m.group(2)) if m else ("", core)
    dot = name.endswith(".")
    nm = name[:-1] if dot else name
    if nm not in HEAD:
        return None
    h = pre + HEAD[nm] + ("।" if dot else "")
    if star:
        h = f"*{h}*"
    return f"{hashes} {h}"


def build():
    lines = PALI.read_text(encoding="utf-8").splitlines()
    out = []
    dkey = None
    n = 0
    for line in lines:
        if not line.strip():
            continue
        n += 1
        body = S.ID_RX.sub("", line)
        where = n
        if body.startswith("#"):
            core = body.lstrip("#").strip().strip("*")
            if core in DYAD_BY_HEAD:
                dkey = DYAD_BY_HEAD[core]
            ctx = Ctx(dkey)
            h = tr_heading(body, ctx)
            if h is None:
                h = body.split(" ", 1)[0] + " " + miss("HEAD:" + core, where)
            out.append(h)
            continue
        ctx = Ctx(dkey)
        if body in LINE:
            out.append(LINE[body])
            continue
        cm = re.match(r"^(.+) niṭṭhitaṃ\.$", body)
        if cm and cm.group(1) in HEAD:
            out.append(HEAD[cm.group(1)] + " समाप्त।")
            continue
        h = count_line(body, ctx, where)
        if h is None:
            h = tr_body(body, ctx, where)
        out.append(h)
    return out


def main():
    hi = build()
    if "--show" in sys.argv:
        a, b = int(sys.argv[sys.argv.index("--show") + 1]), int(sys.argv[sys.argv.index("--show") + 2])
        for i in range(a, b + 1):
            print(i, hi[i - 1])
        return
    if "--sent" in sys.argv:
        a, b = int(sys.argv[sys.argv.index("--sent") + 1]), int(sys.argv[sys.argv.index("--sent") + 2])
        for k, w in SENT.items():
            if a <= w <= b:
                print(f"{w}\t{k}")
        pm = [(w, k) for k, w in MISSING.items() if a <= w <= b and k.startswith("(")]
        for w, k in pm:
            print(f"{w}\t{k}")
        return
    if "--missing" in sys.argv:
        print(len(MISSING), "missing")
        lim = int(sys.argv[sys.argv.index("--missing") + 1]) if len(sys.argv) > sys.argv.index("--missing") + 1 else 10 ** 6
        for k, w in list(MISSING.items())[:lim]:
            print(f"{w}\t{k}")
        return
    if MISSING:
        print(len(MISSING), "segments missing; run with --missing")
        sys.exit(1)
    text = S.assemble(PALI.read_text(encoding="utf-8"), hi)
    if "--check" not in sys.argv:
        with open(OUT, "w", encoding="utf-8", newline="\n") as f:
            f.write(text)
        print("wrote", OUT)
    sys.exit(1 if S.check([(PALI, OUT)]) else 0)


if __name__ == "__main__":
    main()
