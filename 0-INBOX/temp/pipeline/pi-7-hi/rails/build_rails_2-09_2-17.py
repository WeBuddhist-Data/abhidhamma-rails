"""pi-7 Paṭṭhāna, Hindi plain RAILS: builder for 2-09 … 2-17 (Hīnattika … Sanidassanasappaṭighattika).

Imports the approved sample builder read-only (formula constants), then builds every file from
lines_2-09_2-17_<nn>.py (one list L of Hindi content lines per Pāli file, in order; headings and
block IDs come from the Pāli automatically).
  python -I -B -X utf8 build_rails_2-09_2-17.py [2-09 2-10 …]
"""
import os
import re
import sys

RAILS = r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi\rails"
sys.path.insert(0, RAILS)
import build_rails_sample as R  # noqa: E402  (read-only)

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
SRC = ROOT + r"\AI_translation\pali\pi-7_split_chapters"
DST = ROOT + r"\AI_translation\hindi\pi-7-hindi-plain-rails_split_chapters"
FILES = {
    "2-09": "2-09-hinattika", "2-10": "2-10-micchattaniyatattika", "2-11": "2-11-maggarammanattika",
    "2-12": "2-12-uppannattika", "2-13": "2-13-atitattika", "2-14": "2-14-atitarammanattika",
    "2-15": "2-15-ajjhattattika", "2-16": "2-16-ajjhattarammanattika",
    "2-17": "2-17-sanidassanasappatighattika",
}

# ---------------------------------------------------------------- condition forms (from the sample)
N, A, NA, NN, LOC, NLOC = R.NAME, R.ABL, R.NABL, R.NNAME, R.LOC, R.NLOC


def I(k, g="fs"):
    """Xpaccayena paccayo."""
    return R.INS(k, g)


def SAD(k):
    return R.SADISA[k]


# ---------------------------------------------------------------- triad items (pi-1 matrix + pi-7 termbase)
ADJ = {
    "hi": "हीन", "ma": "मध्यम", "pa": "उत्तम",
    "mi": "ग़लत दिशा में निश्चित", "sa": "सही दिशा में निश्चित", "an": "अनिश्चित",
    "mr": "मार्ग को विषय बनाने वाल{a}", "mh": "मार्ग को मूल बनाने वाल{a}", "md": "मार्ग की प्रधानता वाल{a}",
    "up": "उत्पन्न हो चुक{a}", "au": "उत्पन्न न हु{A}", "ud": "उत्पन्न होने वाल{a}",
    "at": "अतीत क{a}", "ag": "भविष्य क{a}", "pc": "वर्तमान क{a}",
    "ar": "अतीत के विषय वाल{a}", "gr": "भविष्य के विषय वाल{a}", "pr": "वर्तमान के विषय वाल{a}",
    "aj": "स्वयं से संबंधित", "ba": "दूसरों से संबंधित",
    "jr": "स्वयं से संबंधित विषय वाल{a}", "br": "दूसरों से संबंधित विषय वाल{a}",
    "ss": "दिखाई देने वाल{a} और टकराव वाल{a}", "as": "दिखाई न देने वाल{a} पर टकराव वाल{a}",
    "aa": "दिखाई न देने वाल{a} और टकराव से रहित",
}
SHORT = {"hi", "ma", "pa", "an"}  # one-word adjectives go after «एक»
_M = {"m": "ा", "o": "े", "f": "ी"}
_V = {"m": "आ", "o": "ए", "f": "ई"}


def J(c, g="f"):
    """Adjective of item c: g = m (masc. direct sg), o (masc. oblique / plural), f (feminine)."""
    return ADJ[c].replace("{a}", _M[g]).replace("{A}", _V[g])


def joinA(xs):
    """'A और B' / 'A, B और C'; «तथा» before the last member when a member already contains «और»."""
    conj = " तथा " if any(" और " in x for x in xs) else " और "
    return ", ".join(xs[:-1]) + conj + xs[-1] if len(xs) > 1 else xs[0]


def D(c):
    """X dhammaṃ / X dhammo."""
    return f"{J(c)} परिघटना"


def D2(*cs):
    """Xañca Yañca dhammaṃ / Xo dhammo ca Yo dhammo ca."""
    xs = [D(c) for c in cs]
    return ", ".join(xs[:-1]) + " और " + xs[-1]


def DP(*cs):
    """X ca Y ca dhammā."""
    return joinA([J(c) for c in cs]) + " परिघटनाएँ"


def DT(*cs):
    """Xassa (ca Yassa ca) dhammassa."""
    return D2(*cs) + " के लिए" if len(cs) > 1 else D(cs[0]) + " के लिए"


def ONE(c, g="o"):
    """X ekaṃ khandhaṃ (g=o, before a postposition) / X eko khandho (g=m)."""
    return f"एक {J(c, g)} समूह" if c in SHORT else f"{J(c, g)} एक समूह"


def KH(c):
    """X khandhe (oblique pl.)."""
    return f"{J(c, 'o')} समूहों"


def KN(c):
    """X khandhā (nom. pl.)."""
    return f"{J(c, 'o')} समूह"


PREP = {"p": "पर निर्भर होकर", "c": "के कारण", "s": "से घुल-मिलकर"}


def C(k):
    """condition word: 'hetu' -> ablative, 'na:hetu' -> negative ablative, other text passes."""
    if k.startswith("na:"):
        return NA[k[3:]]
    return A[k] if k in A else k


def PT(x, y, k, v="p"):
    """X dhammaṃ paṭicca / paccayā / saṃsaṭṭho Y dhammo uppajjati Kpaccayā."""
    verb = "उत्पन्न होती हैं" if y.endswith("परिघटनाएँ") else "उत्पन्न होती है"
    return f"{x} {PREP[v]} {y} {C(k)} {verb}"


def PN(x, y, k, g="fs"):
    """X dhammo Y dhammassa Kpaccayena paccayo."""
    return f"{x}, {y} {I(k, g)}"


# ---------------------------------------------------------------- common clause strings
B1 = "पर निर्भर होकर"
RC, RK, RU = R.RUPA_CITTA, R.RUPA_KATATTA, R.RUPA_UPADA
RCKU = f"{RC}, {RK} और {RU}"
RCU = f"{RC} और {RU}"
RKU = f"{RK} और {RU}"
DCR = "मन से उत्पन्न भौतिक रूपों के लिए"
DKR = "किए गए कर्म से उत्पन्न भौतिक रूपों के लिए"
DCKU = "मन से उत्पन्न भौतिक रूपों, किए गए कर्म से उत्पन्न भौतिक रूपों और व्युत्पन्न भौतिक रूपों के लिए"
DKU = "किए गए कर्म से उत्पन्न भौतिक रूपों और व्युत्पन्न भौतिक रूपों के लिए"
SK = "जुड़े हुए समूहों के लिए"
SKC = "जुड़े हुए समूहों के लिए और मन से उत्पन्न भौतिक रूपों के लिए"
SKK = "जुड़े हुए समूहों के लिए और किए गए कर्म से उत्पन्न भौतिक रूपों के लिए"
VKK = "कर्म-फल रूपी समूहों के लिए और किए गए कर्म से उत्पन्न भौतिक रूपों के लिए"
PK = "पुनर्जन्म के क्षण में"
APK = "मूल से रहित पुनर्जन्म के क्षण में"
ARU = "अभौतिक लोक में"
KV = "समूहों पर निर्भर होकर आधार, आधार पर निर्भर होकर समूह"
KVc = "समूहों के कारण आधार, आधार के कारण समूह"
MOHA = "संशय के साथ होने वाले और बेचैनी के साथ होने वाले समूहों पर निर्भर होकर संशय के साथ होने वाला या बेचैनी के साथ होने वाला मोह"
ANI = R.ANICCA  # अनित्य, दुःख और आत्मा से रहित के रूप में
GIFT = R.GIFT
DEEDS = R.DEEDS
CETO = R.CETOPARIYA
KIL_P, KIL_V, KIL_S = R.KILESA["pahīne"], R.KILESA["vikkhambhite"], R.KILESA["pubbe samudāciṇṇe"]
LAB = {"ādh_ā": "विषय रूपी प्रधानता", "ādh_s": "सह-उत्पत्ति रूपी प्रधानता", "up_ā": "विषय रूपी प्रबल आश्रय",
       "up_a": "निकटता रूपी प्रबल आश्रय", "up_p": "स्वाभाविक प्रबल आश्रय", "pj_ā": "विषय रूपी पूर्व-उत्पत्ति",
       "pj_v": "आधार रूपी पूर्व-उत्पत्ति"}
NANA = dict(R.NANA)  # genitive stems of the knowledges
NANA.update({"phalassa": "फल", "nibbānassa": "निर्वाण"})


def NL(*ws):
    """list of knowledges etc. (genitive stems) sharing one «के लिए»: 'A, B और C के लिए'."""
    hs = [NANA[w] for w in ws]
    return (", ".join(hs[:-1]) + " और " + hs[-1] if len(hs) > 1 else hs[0]) + " के लिए"


DIBBA = "दिव्य आँख से दृश्य रूप को देखता है, दिव्य कान के तत्व से ध्वनि को सुनता है"
RUPA5 = "दृश्य रूप का इंद्रिय-क्षेत्र आँख की चेतना के लिए… स्पर्श का इंद्रिय-क्षेत्र शरीर की चेतना के लिए"
VATTHU5 = "आँख का इंद्रिय-क्षेत्र आँख की चेतना के लिए… शरीर का इंद्रिय-क्षेत्र शरीर की चेतना के लिए"
ANULOMA4 = "अनुरूपता गोत्र-परिवर्तन के लिए… अनुरूपता शुद्धि के लिए… गोत्र-परिवर्तन मार्ग के लिए… शुद्धि मार्ग के लिए"
NIRODHA = "समाप्ति की ध्यान-अवस्था से बाहर आने वाले व्यक्ति में"
NEVA = "न पहचान न अ-पहचान का क्षेत्र"
FS = "फल की ध्यान-अवस्था के लिए"
KAYA = "पहले उत्पन्न इस शरीर के लिए"
KABA = "कौर-कौर खाया जाने वाला भोजन"
RJI = "भौतिक जीवन-क्षमता"
RAGO = "उसे विषय बनाकर राग उत्पन्न होता है"
SAV = "उसका रस लेता है, उसमें आनंद लेता है"
SAVp = "उनका रस लेता है, उनमें आनंद लेता है"
GARU_RAGA = "उसे महत्व देकर राग उत्पन्न होता है, दृष्टि उत्पन्न होती है"
OBJ10 = "कान… नाक… जीभ… शरीर… दृश्य रूपों… ध्वनियों… गंधों… स्वादों… स्पर्शों… आधार…"

# ---------------------------------------------------------------- headings
HD = dict(R.HEAD)
for _k in R.KEYS:
    _cap = _k[0].upper() + _k[1:]
    _n = ("no" if _k in ("atthi", "natthi", "vigata", "avigata") else "na") + _k
    _ncap = _n[0].upper() + _n[1:]
    HD[_cap + "paccayādi"] = N[_k] + " आदि"
    HD[_ncap + "paccayādi"] = NN[_k] + " आदि"
HD.update({
    "Hīnattikaṃ": "हीन वाला तीन का वर्गीकरण",
    "Micchattaniyatattikaṃ": "ग़लत दिशा में निश्चित परिघटनाओं वाला तीन का वर्गीकरण",
    "Maggārammaṇattikaṃ": "मार्ग को विषय बनाने वाला तीन का वर्गीकरण",
    "Uppannattikaṃ": "उत्पन्न वाला तीन का वर्गीकरण",
    "Atītattikaṃ": "अतीत वाला तीन का वर्गीकरण",
    "Atītārammaṇattikaṃ": "अतीत के विषय वाला तीन का वर्गीकरण",
    "Ajjhattattikaṃ": "स्वयं से संबंधित परिघटनाओं वाला तीन का वर्गीकरण",
    "Ajjhattārammaṇattikaṃ": "स्वयं से संबंधित विषय वाला तीन का वर्गीकरण",
    "Sanidassanasappaṭighattikaṃ": "दिखाई देने वाला और टकराव वाला तीन का वर्गीकरण",
    "Sahajātavāro": "सह-उत्पत्ति का खंड", "Paccayavāro": "कारण का खंड", "Nissayavāro": "आश्रय का खंड",
    "Saṃsaṭṭhavāro": "घुले-मिले होने का खंड", "Sampayuttavāro": "जुड़ाव का खंड",
    "Paccanīyuddhāro": "नकारात्मक क्रम के लिए कारणों की छँटाई",
    "Paccanīyānulomaṃ": "नकारात्मक-सकारात्मक क्रम",
    "Nahetudukaṃ": R.NDUKA["hetu"],
    "Nahetutikaṃ": N["hetu"] + " के अभाव के साथ तीन कारणों का मेल",
    "Hetusabhāgaṃ": N["hetu"] + " के साथी कारण",
    "Hetusāmaññaghaṭanā (9)": N["hetu"] + " के सामान्य संयोजन (9)",
    "Hetusāmaññaghaṭanā": N["hetu"] + " के सामान्य संयोजन",
    "Natthivigatāvigatapaccayā": f"{N['natthi']}, {N['vigata']} और {N['avigata']}",
    "2-6. Sahajāta-paccaya-nissaya-saṃsaṭṭha-sampayuttavāro":
        "2-6. सह-उत्पत्ति, कारण, आश्रय, घुले-मिले होने और जुड़ाव का खंड",
    "4-6. Nissaya-saṃsaṭṭha-sampayuttavāro": "4-6. आश्रय, घुले-मिले होने और जुड़ाव का खंड",
})


def heading(body):
    m = re.fullmatch(r"(#+) (\*?)(.*?)(\*?)", body)
    hashes, st, inner, en = m.groups()
    return f"{hashes} {st}{HD[inner]}{en}"


# ---------------------------------------------------------------- counting lines
NUMX = dict(R.NUM)
NUMX.update({"dasa": "दस", "ekādasa": "ग्यारह", "dvādasa": "बारह", "terasa": "तेरह", "sattarasa": "सत्रह",
             "ekavīsa": "इक्कीस", "dvāvīsa": "बाईस", "bāvīsa": "बाईस", "tevīsa": "तेईस", "catuvīsa": "चौबीस",
             "pañcavīsa": "पच्चीस"})
CNOTE = {  # notes inside counting lines
    "evaṃ gaṇetabbaṃ": "इस तरह गिनना चाहिए",
    "saṃkhittaṃ": "संक्षिप्त",
    "saṃkhittaṃ, sabbattha nava": "संक्षिप्त, हर जगह नौ",
    "saṃkhittaṃ, sabbattha dve": "संक्षिप्त, हर जगह दो",
    "saṃkhittaṃ, sabbattha cattāri": "संक्षिप्त, हर जगह चार",
    "saṃkhittaṃ, sabbattha cha kātabbā": "संक्षिप्त, हर जगह छह करने चाहिए",
    "saṃkhittaṃ, sabbattha ekavīsa": "संक्षिप्त, हर जगह इक्कीस",
    "sabbattha tīṇi": "हर जगह तीन",
    "sabbattha tīṇi, saṃkhittaṃ": "हर जगह तीन, संक्षिप्त",
    "sabbattha dve ": "हर जगह दो",
    "sabbattha dve. Evaṃ gaṇetabbaṃ": "हर जगह दो। इस तरह गिनना चाहिए",
    "sabbattha ekaṃ": "हर जगह एक",
    "imesu padesu ekaṃyeva": "इन पदों में एक ही",
    "anulomapadāni gaṇetabbāni": "सकारात्मक क्रम के पदों को गिनना चाहिए",
    "paṭhamagamanasadisaṃ": "पहले प्रसंग के समान",
    "idhāpi saṃkhittaṃ": "यहाँ भी संक्षिप्त",
    "naārammaṇe gahite pakatārammaṇampi upanissayārammaṇampi dvepi chijjanti":
        "विषय-कारण का अभाव लेने पर स्वाभाविक विषय भी और प्रबल आश्रय रूपी विषय भी, दोनों कट जाते हैं",
    "avipākaṃ-4": f"{N['vipāka']} रहित-4",
    "savipākaṃ-5": f"{N['vipāka']} सहित-5",
}
_W = {}
for _d in (R.P_ABL, R.P_NABL, R.P_LOC, R.P_NLOC, NUMX):
    _W.update(_d)


def GH(s):
    """ghaṭanā 'Hetu-sahajāta-…-avigatanti' -> 'मूल-कारण, …और अविलीनता-कारण के संयोजन में'."""
    parts = [p.strip() for p in re.split(r"-| -|- ", s[:-3]) if p.strip()]
    fix = {"aññamaññanissaya": ["aññamañña", "nissaya"], "nissayavipāka": ["nissaya", "vipāka"],
           "atthiavigata": ["atthi", "avigata"]}
    ks = []
    for p in parts:
        p = p[0].lower() + p[1:]
        ks.extend(fix.get(p, [p]))
    return ", ".join(N[k] for k in ks[:-1]) + " और " + N[ks[-1]] + " के संयोजन में"


def CNT(line):
    """A counting line (any mix of ablatives, locatives, numbers, notes, ghaṭanā heads)."""
    notes = []

    def keep(m):
        notes.append("(" + CNOTE[m.group(1)] + ")")
        return f"\x00{len(notes) - 1}\x00"
    t = re.sub(r"\(([^()]*)\)", keep, line)
    gh = []

    def keepg(m):
        gh.append(GH(m.group(0)))
        return f"\x01{len(gh) - 1}\x01"
    t = re.sub(r"[A-Za-zāīūṃñṭḍṇḷ]+(?:\s?-\s?[A-Za-zāīūṃñṭḍṇḷ]+)+nti", keepg, t)
    t = R.lower_initials(t)
    toks = [x for x in re.split(r"(…pe…|…|, |; | |\.$|\. )", t) if x]
    out = []
    for i, x in enumerate(toks):
        if x == " ":
            prev = toks[i - 1]
            nxt = toks[i + 1] if i + 1 < len(toks) else ""
            if prev in R.P_ABL or prev in R.P_NABL:
                out.append(", ")
            elif prev.startswith("\x01"):
                out.append(" " if nxt.rstrip(".") in NUMX else ", ")
            else:
                out.append(" ")
        elif x == "…pe…":
            out.append("…")
        elif x == ".":
            out.append("।")
        elif x == ". ":
            out.append("। ")
        elif x in ("…", ", ", "; "):
            out.append(x)
        elif x.startswith("\x00"):
            out.append(notes[int(x.strip("\x00").rstrip("।"))])
        elif x.startswith("\x01"):
            out.append(gh[int(x.strip("\x01"))])
        elif x.endswith(".") and x[:-1] in _W:  # '…ekaṃ.' inside a line
            out.append(_W[x[:-1]] + "।")
        else:
            out.append(_W[x])
    return "".join(out)


# ---------------------------------------------------------------- closing lines
CLOSE = {
    "Anulomaṃ.": "सकारात्मक क्रम।", "Paccanīyaṃ.": "नकारात्मक क्रम।",
    "Anulomapaccanīyaṃ.": "सकारात्मक-नकारात्मक क्रम।", "Paccanīyānulomaṃ.": "नकारात्मक-सकारात्मक क्रम।",
    "Paccayānulomaṃ.": "कारणों का सकारात्मक क्रम।",
    "Paṭiccavāro.": "निर्भरता का खंड।", "Paccayavāro.": "कारण का खंड।", "Saṃsaṭṭhavāro.": "घुले-मिले होने का खंड।",
    "Pañhāvāro.": "प्रश्नों का खंड।", "Pañhāvāro niṭṭhito.": "प्रश्नों का खंड समाप्त।",
    "Dhammānulome tikapaṭṭhānaṃ niṭṭhitaṃ.": "परिघटनाओं का सकारात्मक क्रम: तीन-तीन के वर्गीकरणों के कारण-संबंध समाप्त।",
    "Dutiyo bhāgo niṭṭhito.": "दूसरा भाग समाप्त।",
}
for _p, _h in list(HD.items()):
    if _p.endswith("ttikaṃ"):
        CLOSE[_p + " niṭṭhitaṃ."] = _h + " समाप्त।"

ID_RE = re.compile(r" \^([0-9A-Za-z-]+)\s*$")


def is_count(s):
    t = re.sub(r"\([^()]*\)", "", s)
    t = re.sub(r"[A-Za-zāīūṃñṭḍṇḷ]+(?:\s?-\s?[A-Za-zāīūṃñṭḍṇḷ]+)+nti", "", t)
    toks = [x for x in re.split(r"…pe…|…|, |; | |\.", R.lower_initials(t)) if x]
    return bool(toks) and all(x in _W for x in toks) and any(x in NUMX for x in toks)


def build(key):
    name = FILES[key]
    pali = [l for l in open(os.path.join(SRC, name + ".md"), encoding="utf-8").read().splitlines() if l.strip()]
    g = dict(globals())
    exec(open(os.path.join(RAILS, f"lines_2-09_2-17_{key}.py"), encoding="utf-8").read(), g)
    L = list(g["L"])
    out, it = [], iter(L)
    for line in pali:
        m = ID_RE.search(line)
        body = line[: m.start()] if m else line
        if body.startswith("#"):
            h = heading(body)
        elif body in CLOSE:
            h = CLOSE[body]
        elif is_count(body):
            h = CNT(body)
        else:
            try:
                h = next(it)
            except StopIteration:
                raise SystemExit(f"{key}: too few hand lines at: {body[:80]}")
        out.append((h, m.group(1) if m else None))
    rest = list(it)
    if rest:
        raise SystemExit(f"{key}: {len(rest)} hand lines left over, first: {rest[0][:80]}")
    text = ""
    for h, bid in out:
        text += h + (f" ^{bid}" if bid else "") + "\n" + ("\n" if bid else "")
    text = text.rstrip("\n") + "\n"
    with open(os.path.join(DST, name + ".md"), "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(key, "lines", len(out), "hand", len(L))


if __name__ == "__main__":
    for k in (sys.argv[1:] or list(FILES)):
        build(k)
