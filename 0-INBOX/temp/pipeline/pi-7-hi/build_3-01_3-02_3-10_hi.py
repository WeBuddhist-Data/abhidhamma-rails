"""Hindi plain zero-shot of pi-7 (Paṭṭhāna) 3-01 hetugocchaka, 3-02 cūḷantaraduka, 3-10 upādānagocchaka.

Every line is composed mechanically: the Pāli line is cut into units at its punctuation
(" – ", ";", ",", ".", "…pe…", "…", brackets); every unit is translated by
  1. the fixed frames of the sample (build_sample_hi, imported as S): the "dependent" frames
     (paṭicca / paccayā / nissāya / saṃsaṭṭho / sampayutto), the pañhāvāra frame, the bare
     conditions, the counting lines (S.count_hi);
  2. the item tables (dyad items as in the pi-1 matrix Hindi);
  3. the phrase table PH (one Hindi string per Pāli unit, so a repeated unit is byte-identical).
The punctuation is carried over ("…pe…" -> "…", "." -> "।"). A verb of a frame is moved to the end of the
chain of conditions that follows it ("…pe… X-paccayā… Y-paccayā" -> "X-कारण से… Y-कारण से उत्पन्न होती है").

usage: python -I -B -X utf8 build_3-01_3-02_3-10_hi.py            # write + check
       python -I -B -X utf8 build_3-01_3-02_3-10_hi.py --unknown  # list untranslated units only
"""
import collections
import pathlib
import re
import sys

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi")
import build_sample_hi as S  # noqa: E402

HERE = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi")
FILES = ["3-01-hetugocchaka.md", "3-02-culantaraduka.md", "3-10-upadanagocchaka.md"]

sys.path.insert(0, str(HERE))
from phrases_3_01_3_02_3_10 import PH, HEAD, LINES, HN, NOUNF, HA, ADJF, NUMF, VPH, COMPOUND  # noqa: E402

# =====================================================================================
# 1. Dyad items (pi-1 matrix Hindi, singular, feminine with परिघटना)
# =====================================================================================
ITEMS = {  # key: (acc, nom, gen, Hindi)
    "hetu": ("hetuṃ", "hetu", "hetussa", "मूल रूपी"),
    "nahetu": ("nahetuṃ", "nahetu", "nahetussa", "मूल रूपी न होने वाली"),
    "sahetuka": ("sahetukaṃ", "sahetuko", "sahetukassa", "मूल वाली"),
    "ahetuka": ("ahetukaṃ", "ahetuko", "ahetukassa", "मूल से रहित"),
    "hetusampayutta": ("hetusampayuttaṃ", "hetusampayutto", "hetusampayuttassa", "मूलों से जुड़ी"),
    "hetuvippayutta": ("hetuvippayuttaṃ", "hetuvippayutto", "hetuvippayuttassa", "मूलों से अलग"),
    "hetu-sahetuka": ("hetuñceva sahetukañca", "hetu ceva sahetuko ca", "hetussa ceva sahetukassa ca",
                      "मूल रूपी भी और मूल वाली भी"),
    "sahetuka-nahetu": ("sahetukañceva na ca hetuṃ", "sahetuko ceva na ca hetu", "sahetukassa ceva na ca hetussa",
                        "मूल वाली, पर स्वयं मूल रूपी न होने वाली"),
    "hetu-hetusampayutta": ("hetuñceva hetusampayuttañca", "hetu ceva hetusampayutto ca",
                            "hetussa ceva hetusampayuttassa ca", "मूल रूपी भी और मूलों से जुड़ी भी"),
    "hetusampayutta-nahetu": ("hetusampayuttañceva na ca hetuṃ", "hetusampayutto ceva na ca hetu",
                              "hetusampayuttassa ceva na ca hetussa", "मूलों से जुड़ी, पर स्वयं मूल रूपी न होने वाली"),
    "nahetu-sahetuka": ("nahetuṃ sahetukaṃ", "nahetu sahetuko", "nahetusahetukassa", "मूल रूपी न होने वाली, पर मूल वाली"),
    "nahetu-ahetuka": ("nahetuṃ ahetukaṃ", "nahetu ahetuko", "nahetuahetukassa", "मूल रूपी न होने वाली और मूल से रहित"),
    "sappaccaya": ("sappaccayaṃ", "sappaccayo", "sappaccayassa", "कारणों पर निर्भर रहने वाली"),
    "appaccaya": ("appaccayaṃ", "appaccayo", "appaccayassa", "कारणों पर निर्भर न रहने वाली"),
    "saṅkhata": ("saṅkhataṃ", "saṅkhato", "saṅkhatassa", "निर्मित"),
    "asaṅkhata": ("asaṅkhataṃ", "asaṅkhato", "asaṅkhatassa", "अनिर्मित"),
    "sanidassana": ("sanidassanaṃ", "sanidassano", "sanidassanassa", "दिखाई देने वाली"),
    "anidassana": ("anidassanaṃ", "anidassano", "anidassanassa", "दिखाई न देने वाली"),
    "sappaṭigha": ("sappaṭighaṃ", "sappaṭigho", "sappaṭighassa", "टकराव वाली"),
    "appaṭigha": ("appaṭighaṃ", "appaṭigho", "appaṭighassa", "टकराव से रहित"),
    "rūpī": ("rūpiṃ", "rūpī", "rūpissa", "भौतिक"),
    "arūpī": ("arūpiṃ", "arūpī", "arūpissa", "अभौतिक"),
    "lokiya": ("lokiyaṃ", "lokiyo", "lokiyassa", "लौकिक"),
    "lokuttara": ("lokuttaraṃ", "lokuttaro", "lokuttarassa", "लोकोत्तर"),
    "kenaci-viññeyya": ("kenaci viññeyyaṃ", "kenaci viññeyyo", "kenaci viññeyyassa",
                        "किसी एक प्रकार की चेतना से जानी जा सकने वाली"),
    "kenaci-naviññeyya": ("kenaci naviññeyyaṃ", "kenaci naviññeyyo", "kenaci naviññeyyassa",
                          "किसी एक प्रकार की चेतना से न जानी जा सकने वाली"),
    "upādāna": ("upādānaṃ", "upādāno", "upādānassa", "आसक्ति रूपी"),
    "noupādāna": ("noupādānaṃ", "noupādāno", "noupādānassa", "आसक्ति रूपी न होने वाली"),
    "upādāniya": ("upādāniyaṃ", "upādāniyo", "upādāniyassa", "आसक्ति का विषय बनने वाली"),
    "anupādāniya": ("anupādāniyaṃ", "anupādāniyo", "anupādāniyassa", "आसक्ति का विषय न बनने वाली"),
    "upādānasampayutta": ("upādānasampayuttaṃ", "upādānasampayutto", "upādānasampayuttassa", "आसक्ति से जुड़ी"),
    "upādānavippayutta": ("upādānavippayuttaṃ", "upādānavippayutto", "upādānavippayuttassa", "आसक्ति से अलग"),
    "upādāna-upādāniya": ("upādānañceva upādāniyañca", "upādāno ceva upādāniyo ca", "upādānassa ceva upādāniyassa ca",
                          "आसक्ति रूपी भी और आसक्ति का विषय बनने वाली भी"),
    "upādāniya-noupādāna": ("upādāniyañceva no ca upādānaṃ", "upādāniyo ceva no ca upādāno",
                            "upādāniyassa ceva no ca upādānassa",
                            "आसक्ति का विषय बनने वाली, पर स्वयं आसक्ति रूपी न होने वाली"),
    "upādāna-upādānasampayutta": ("upādānañceva upādānasampayuttañca", "upādāno ceva upādānasampayutto ca",
                                  "upādānassa ceva upādānasampayuttassa ca", "आसक्ति रूपी भी और आसक्ति से जुड़ी भी"),
    "upādānasampayutta-noupādāna": ("upādānasampayuttañceva no ca upādānaṃ", "upādānasampayutto ceva no ca upādāno",
                                    "upādānasampayuttassa ceva no ca upādānassa",
                                    "आसक्ति से जुड़ी, पर स्वयं आसक्ति रूपी न होने वाली"),
    "upādānavippayutta-upādāniya": ("upādānavippayuttaṃ upādāniyaṃ", "upādānavippayutto upādāniyo",
                                    "upādānavippayuttupādāniyassa", "आसक्ति से अलग, पर उसका विषय बनने वाली"),
    "upādānavippayutta-anupādāniya": ("upādānavippayuttaṃ anupādāniyaṃ", "upādānavippayutto anupādāniyo",
                                      "upādānavippayuttaanupādāniyassa", "आसक्ति से अलग और उसका विषय न बनने वाली"),
}
PAIRS = [("hetu", "nahetu"), ("sahetuka", "ahetuka"), ("hetusampayutta", "hetuvippayutta"),
         ("hetu-sahetuka", "sahetuka-nahetu"), ("hetu-hetusampayutta", "hetusampayutta-nahetu"),
         ("nahetu-sahetuka", "nahetu-ahetuka"), ("sappaccaya", "appaccaya"), ("saṅkhata", "asaṅkhata"),
         ("sanidassana", "anidassana"), ("sappaṭigha", "appaṭigha"), ("rūpī", "arūpī"), ("lokiya", "lokuttara"),
         ("kenaci-viññeyya", "kenaci-naviññeyya"), ("upādāna", "noupādāna"), ("upādāniya", "anupādāniya"),
         ("upādānasampayutta", "upādānavippayutta"), ("upādāna-upādāniya", "upādāniya-noupādāna"),
         ("upādāna-upādānasampayutta", "upādānasampayutta-noupādāna"),
         ("upādānavippayutta-upādāniya", "upādānavippayutta-anupādāniya")]


def _ca_acc(a):
    return a if a.endswith("ca") else a[:-1] + "ñca"


def _ca(x):
    return x if x.endswith(" ca") else x + " ca"


ACC, NOM, GEN = {}, {}, {}
for k, (a, n, g, h) in ITEMS.items():
    ACC[a] = [k]
    NOM[n] = [k]
    GEN[g] = [k]
for k1, k2 in PAIRS:
    a1, n1, g1, _ = ITEMS[k1]
    a2, n2, g2, _ = ITEMS[k2]
    ACC[_ca_acc(a1) + " " + _ca_acc(a2)] = [k1, k2]
    NOM[_ca(n1) + " " + _ca(n2)] = [k1, k2]
    GEN[_ca(g1) + " " + _ca(g2)] = [k1, k2]
# attested spelling/form variants (listed in the notes)
ACC["upādānañca noupādānaṃ ca"] = ["upādāna", "noupādāna"]
NOM["hetū ca nahetū ca"] = ["hetu", "nahetu"]
GEN["lokuttarasa"] = ["lokuttara"]                      # spelling slip for lokuttarassa
GEN["sahetukassa ceva na ca hetussa ca"] = ["sahetuka-nahetu"]
GEN["upādāniyassa ceva no ca upādānassa ca"] = ["upādāniya-noupādāna"]
GEN["upādānasampayuttassa ceva no ca upādānassa ca"] = ["upādānasampayutta-noupādāna"]


def _compound(items):
    return any("," in ITEMS[i][3] or " और " in ITEMS[i][3] or " भी" in ITEMS[i][3] for i in items)


def OBJ(items):
    w = [f"{ITEMS[i][3]} {S.DHAMMA}" for i in items]
    if len(w) == 1:
        return w[0]
    return f"{w[0]} तथा {w[1]}" if _compound(items) else f"{w[0]} और {w[1]}"


def RES(items):
    if len(items) == 1:
        return f"{ITEMS[items[0]][3]} {S.DHAMMA}"
    if _compound(items):
        return f"{ITEMS[items[0]][3]} {S.DHAMMA} तथा {ITEMS[items[1]][3]} {S.DHAMMA}"
    return f"{ITEMS[items[0]][3]} और {ITEMS[items[1]][3]} {S.DHAMMA_PL}"


def DAT(items):
    return OBJ(items) + " के लिए"


# =====================================================================================
# 2. Frames
# =====================================================================================
DEPW = {"paṭicca": "paṭicca", "paccayā": "paccaya", "nissāya": "nissaya", "saṃsaṭṭho": "saṃsaṭṭha",
        "saṃsaṭṭhā": "saṃsaṭṭha", "sampayutto": "sampayutta", "sampayuttā": "sampayutta",
        "sahajāto": "sahajāta", "sahajātā": "sahajāta"}
_STEMS = "|".join(sorted(S.COND_KEYS, key=len, reverse=True))
RX_DEP = re.compile(r"^(?P<obj>.+?) dhammaṃ (?P<dep>" + "|".join(DEPW) + r") (?P<res>.+?) (?P<dh>dhammo|dhammā)"
                    r"(?: (?P<verb>uppajjati|uppajjanti))?(?: (?P<neg>na|no)?(?P<cond>" + _STEMS + r")paccayā)?$")
RX_PANHA = re.compile(r"^(?P<src>.+?) (?P<dh>dhammo|dhammā) (?P<dst>.+?) dhammassa"
                      r"(?: (?P<neg>na |no )?(?P<cond>" + _STEMS + r")paccayena paccayo)?$")
RX_ABL = re.compile(r"^(?P<neg>na|no)?(?P<cond>" + _STEMS + r")paccayā$")
RX_INS = re.compile(r"^(?P<neg>na |no )?(?P<cond>" + _STEMS + r")paccayena paccayo$")

# =====================================================================================
# 3. Small noun-phrase grammar for the sub-clauses (lexicon in the phrases module)
#    noun: HN[key] = (gender, dir_sg, dir_pl, obl_sg, obl_pl); NOUNF[pāli] = (key, num, is_gen)
#    adj:  HA[key] = (m_dir_sg, m_other, f, alt_group); ADJF[pāli] = (key, is_gen)
#    num:  NUMF[pāli] = (hindi, is_gen)
# =====================================================================================
_MAXW = 5


_COMP_RX = None


def _norm_words(np):
    """Words of a noun phrase; "ca"/"ceva"/"-ñca" become the marker "&" after the word."""
    global _COMP_RX
    if _COMP_RX is None:
        _COMP_RX = re.compile(r"(?<!\S)(" + "|".join(re.escape(k) for k in sorted(COMPOUND, key=len, reverse=True))
                              + r")(?!\S)")
    np = _COMP_RX.sub(lambda m: COMPOUND[m.group(1)], np)
    out = []
    for w in np.split():
        if w in ("ca", "ceva"):
            out.append("&")
            continue
        if w.endswith("ādhipati") and w != "ādhipati":
            out += [w[:-8] + "a", "adhipati"]
            continue
        if w.endswith("ñceva"):
            out += [w[:-5] + "ṃ", "&"]
        elif w.endswith("ñca"):
            out += [w[:-3] + "ṃ", "&"]
        else:
            out.append(w)
    return out


def parse_np(np):
    """-> list of conjuncts: dict(adjs=[keys], num=hindi|None, noun=key, n='sg'|'pl', gen=bool, coord=bool)."""
    ws = _norm_words(np)
    res, adjs, num, coord = [], [], None, False
    i = 0
    prev = None
    while i < len(ws):
        if ws[i] == "&":
            # "sanidassanassa ca anidassanassa ca kāyassa": two coordinated adjectives
            if prev == "adj" and i + 1 < len(ws) and any(" ".join(ws[i + 1:i + 1 + L]) in ADJF
                                                         for L in range(1, _MAXW + 1)):
                coord = True
            i += 1
            continue
        for L in range(min(_MAXW, len(ws) - i), 0, -1):
            if ws[i + L - 1] == "&":
                continue
            cand = " ".join(w for w in ws[i:i + L] if w != "&")
            if cand in NOUNF:
                key, n, g = NOUNF[cand]
                res.append(dict(adjs=adjs, num=num, noun=key, n=n, gen=g, coord=coord))
                adjs, num, coord = [], None, False
                i += L
                prev = "noun"
                break
            if cand in ADJF:
                adjs = adjs + [ADJF[cand][0]]
                i += L
                prev = "adj"
                break
            if cand in NUMF:
                num = NUMF[cand][0]
                i += L
                prev = "num"
                break
        else:
            return None
    if adjs or num:
        return None
    return res


def _adj_form(key, gender, n, role):
    m_sg, m_oth, f, _ = HA[key]
    if gender == "f":
        return f
    return m_sg if (role == "dir" and n == "sg") else m_oth


def conj_hi(c, role):
    g, dsg, dpl, osg, opl = HN[c["noun"]]
    noun = {("dir", "sg"): dsg, ("dir", "pl"): dpl, ("obl", "sg"): osg, ("obl", "pl"): opl}[(role, c["n"])]
    def jadj(keys):
        a = [_adj_form(k, g, c["n"], role) for k in keys]
        if len(a) == 2 and HA[keys[0]][3] and HA[keys[0]][3] == HA[keys[1]][3]:
            return a[0] + (" या " if c["n"] == "sg" else " और ") + a[1]
        if len(a) == 2 and c.get("coord"):
            return a[0] + (" तथा " if any("," in x or " भी" in x for x in a) else " और ") + a[1]
        out = ""
        for j, x in enumerate(a):
            if j:
                out += " " if keys[j - 1] in ("purima", "pacchima", "pacchājāta", "purejāta") else ", "
            out += x
        return out

    if "ima" in c["adjs"]:   # demonstrative: "purejātassa imassa sanidassanassa kāyassa"
        k = c["adjs"].index("ima")
        dem = _adj_form("ima", g, c["n"], role)
        parts = [jadj(c["adjs"][:k]), dem, jadj(c["adjs"][k + 1:]), noun]
        return " ".join(x for x in parts if x)
    a = c["adjs"]
    adj = jadj(a)
    if c["num"]:
        if not a:
            return f"{c['num']} {noun}"
        if len(a) == 1 and " " not in adj:
            return f"{c['num']} {adj} {noun}"
        return f"{adj} {c['num']} {noun}"
    return f"{adj} {noun}" if adj else noun


def join_hi(parts):
    return parts[0] if len(parts) == 1 else ", ".join(parts[:-1]) + " और " + parts[-1]


def np_dir(cs):
    return join_hi([conj_hi(c, "dir") for c in cs])


def np_obl(cs):
    return join_hi([conj_hi(c, "obl") for c in cs])


def np_dat(cs):
    return join_hi([conj_hi(c, "obl") + " के लिए" for c in cs])


def agree(cs, stem):
    """verb agreement: stem 'होता' -> होता है / होती है / होते हैं / होती हैं"""
    if not cs:
        return None
    fem = all(HN[c["noun"]][0] == "f" for c in cs)
    pl = len(cs) > 1 or cs[0]["n"] == "pl"
    if fem:
        return "होती हैं" if pl else "होती है"
    return "होते हैं" if pl else "होता है"


PRE_HI = {"paṭisandhikkhaṇe": S.PATISANDHI, "ahetukapaṭisandhikkhaṇe": S.AHETUKA_PATISANDHI, "arūpe": S.ARUPE,
          "pavatte": "जीवन के दौरान",
          "nirodhā vuṭṭhahantassa": "समाप्ति की ध्यान-अवस्था से उठने वाले व्यक्ति में"}
RX_SUBDEP = re.compile(r"^(?:(?P<pre>" + "|".join(PRE_HI) + r") )?(?P<acc>.+?) (?P<dep>paṭicca|paccayā|nissāya|"
                       r"saṃsaṭṭhā|saṃsaṭṭho|sampayuttā|sampayutto)(?: (?P<nom>.+))?$")
RX_SUBVERB = re.compile(r"^(?:(?P<pre>" + "|".join(PRE_HI) + r") )?(?P<acc>.+?) (?P<conn>ārabbha|garuṃ katvā) "
                        r"(?P<nom>.+?) (?P<verb>uppajjati|uppajjanti)$")
RX_SUBPANHA = re.compile(r"^(?:(?P<pre>" + "|".join(PRE_HI) + r") )?(?P<np>.+?)(?: (?:(?P<neg>na|no) )?(?P<cond>"
                         + _STEMS + r")paccayena paccayo)?$")
CONN_HI = {"ārabbha": "को विषय बनाकर", "garuṃ katvā": "को महत्व देकर"}


def _acc_obl(acc):
    if acc == "taṃ":
        return "उसे", True
    cs = parse_np(acc)
    if cs is None:
        return None, False
    return np_obl(cs), False


SUBJ_HI = {"ariyā": "आर्य", "sekkhā": S.SEKKHA, "puthujjanā": S.PUTHUJJANA, "arahā": S.ARAHA,
           "sekkhā vā puthujjanā vā": S.SEKKHA_VA_PUTHUJJANA}
FROM_HI = {"jhānā": "ध्यान से उठकर", "maggā": "मार्ग से उठकर"}
_SUBJ = "|".join(sorted(SUBJ_HI, key=len, reverse=True))
RX_REVIEW = re.compile(r"^(?:(?P<subj>" + _SUBJ + r") )?(?:(?P<from>jhānā|maggā) vuṭṭhahitvā )?(?P<acc>.+?)"
                       r"(?P<garu> garuṃ katvā)? (?P<v>paccavekkhati|paccavekkhanti)$")
RX_ANICCA = re.compile(r"^(?:(?P<subj>" + _SUBJ + r") )?(?P<acc>.+?) aniccato$")
RX_ASSADA = re.compile(r"^(?P<acc>.+?)(?P<garu> garuṃ katvā)? assādeti abhinandati$")
RX_UPAN = re.compile(r"^(?P<acc>.+?) upanissāya (?P<vp>.+)$")


def _plural(acc):
    if acc == "taṃ":
        return False
    cs = parse_np(acc)
    return bool(cs) and (len(cs) > 1 or cs[0]["n"] == "pl")


RX_CETO = re.compile(r"^(?:(?P<subj>" + _SUBJ + r") )?cetopariyañāṇena (?P<x>.+?)cittasamaṅgissa cittaṃ "
                     r"(?P<v>jānāti|jānanti)$")
RX_TADA = re.compile(r"^kusalākusale niruddhe (?P<x>.+?) vipāko tadārammaṇatā uppajjati$")


def _adj_m(x, oblique):
    """Pāli adjective (stem or form, possibly a compound) -> Hindi masculine form."""
    ws = _norm_words(x)
    keys = []
    for w in ws:
        if w in ADJF:
            keys.append(ADJF[w][0])
        elif w + "a" in ADJF:
            keys.append(ADJF[w + "a"][0])
        elif w in ("hetu",):
            keys.append("hetu-adj")
        else:
            return None
    return ", ".join(HA[k][1] if oblique else HA[k][0] for k in keys)


def tr_verbal(u):
    m = RX_CETO.match(u)
    if m:
        x = _adj_m(m.group("x"), True)
        if x:
            subj = (SUBJ_HI[m.group("subj")] + " ") if m.group("subj") else ""
            v = "जानते हैं" if m.group("v") == "jānanti" else "जानता है"
            return Tok("text", f"{subj}{S.CETOPARIYENA} {x} मन से युक्त व्यक्ति के मन को {v}")
    m = RX_TADA.match(u)
    if m:
        x = _adj_m(m.group("x"), False)
        if x:
            return Tok("text", f"हितकर और हानिकर के समाप्त होने पर {x} {S.TADARAMMANA}")
    m = RX_REVIEW.match(u)
    if m:
        acc = m.group("acc")
        a, pron = _acc_obl(acc)
        if a:
            on = "उन पर" if _plural(acc) else "उस पर"
            if pron:
                obj = "उसे महत्व देकर उस पर" if m.group("garu") else "उस पर"
            else:
                obj = f"{a} को महत्व देकर {on}" if m.group("garu") else f"{a} पर"
            subj = (SUBJ_HI[m.group("subj")] + " ") if m.group("subj") else ""
            frm = (FROM_HI[m.group("from")] + " ") if m.group("from") else ""
            v = S.REVIEW_PL if m.group("v") == "paccavekkhanti" else S.REVIEW_SG
            return Tok("text", f"{subj}{frm}{obj} {v}")
    m = RX_ANICCA.match(u)
    if m:
        a, pron = _acc_obl(m.group("acc"))
        if a and not pron:
            subj = (SUBJ_HI[m.group("subj")] + " ") if m.group("subj") else ""
            return Tok("text", f"{subj}{a} को अनित्य के रूप में")
    m = RX_ASSADA.match(u)
    if m:
        acc = m.group("acc")
        a, pron = _acc_obl(acc)
        if a:
            p = "उन" if _plural(acc) else "उस"
            if pron:
                return Tok("text", f"उस{S.ASSADA}, उस{S.ABHINANDA}")
            if m.group("garu"):
                return Tok("text", f"{a} को महत्व देकर {p}{S.ASSADA}, {p}{S.ABHINANDA}")
            return Tok("text", f"{a} {S.ASSADA}, {p}{S.ABHINANDA}")
    m = RX_UPAN.match(u)
    if m and m.group("vp") in VPH:
        a, pron = _acc_obl(m.group("acc"))
        if a and not pron:
            return Tok("text", f"{a} के प्रबल आश्रय से {VPH[m.group('vp')]}")
    return None


def tr_sub(u):
    """Sub-clauses of the vibhaṅga sections; returns a Tok or None."""
    t = tr_verbal(u)
    if t:
        return t
    pre_of = lambda m: (PRE_HI[m.group("pre")] + " ") if m.group("pre") else ""
    m = RX_SUBVERB.match(u)
    if m:
        a, pron = _acc_obl(m.group("acc"))
        nom = parse_np(m.group("nom"))
        if a and nom:
            conn = CONN_HI[m.group("conn")]
            head = f"{a} {conn.split(' ', 1)[1]}" if pron else f"{a} {conn}"
            v = agree(nom, "होता")
            return Tok("text", f"{pre_of(m)}{head} {np_dir(nom)} उत्पन्न {v}")
    m = RX_SUBDEP.match(u)
    if m:
        a, _ = _acc_obl(m.group("acc"))
        nom = parse_np(m.group("nom")) if m.group("nom") else []
        if a and nom is not None:
            d = S.DEP[DEPW[m.group("dep")] if m.group("dep") in DEPW else m.group("dep")]
            tail = f" {np_dir(nom)}" if nom else ""
            return Tok("text", f"{pre_of(m)}{a} {d}{tail}")
    m = RX_SUBPANHA.match(u)
    if m:
        cs = parse_np(m.group("np"))
        if cs is not None and cs:
            subj = [c for c in cs if not c["gen"]]
            dat = [c for c in cs if c["gen"]]
            if subj and dat and cs.index(dat[0]) < len(subj):
                return None   # dative before subject: not this pattern
            parts = []
            if subj:
                parts.append(np_dir(subj))
                CUR["verb"] = "कारण " + agree(subj, "होता")
            if dat:
                parts.append(np_dat(dat))
            head = pre_of(m) + " ".join(parts)
            if m.group("cond"):
                c = m.group("cond")
                v = CUR.get("verb") or "कारण होता है"
                if m.group("neg"):
                    v = v.replace("होते हैं", "नहीं होते").replace("होती हैं", "नहीं होतीं").replace(
                        "होता है", "नहीं होता").replace("होती है", "नहीं होती")
                return Tok("frame", f"{head} {S.NAME(c)} के रूप में", v)
            if subj and not dat:
                return bare_np(m.group("np"), cs, pre_of(m))
            return Tok("text", head)
    return None


def _is_acc(w):
    return w.endswith(("aṃ", "uṃ", "iṃ")) or (w.endswith("e") and not w.endswith("kkhaṇe"))


def bare_np(np, cs, pre):
    """An abbreviated noun phrase ("dve khandhe…pe…"): accusative = the object of the current
    dependence word (paṭicca -> "पर निर्भर होकर"), else "को"; nominative = plain."""
    last = [w for w in _norm_words(np) if w != "&"][-1]
    acc_nouns = {"khandha", "mahābhūta", "vatthu", "hetu", "moha", "lobha", "dosa", "alobha", "adosa", "amoha",
                 "cetanā", "diṭṭhi", "cakkhu", "phala", "nibbāna", "magga", "gotrabhu", "vodāna", "jhāna"}
    if not _is_acc(last) or (last.endswith("ṃ") and cs[-1]["noun"] not in acc_nouns):
        return Tok("text", pre + np_dir(cs))
    if CUR.get("dep"):
        return Tok("text", f"{pre}{np_obl(cs)} {S.DEP[CUR['dep']]}")
    post = {"vatthu": "को", "cakkhu": "को", "phala": "पर", "nibbāna": "पर", "magga": "पर", "gotrabhu": "पर",
            "vodāna": "पर", "jhāna": "पर"}.get(cs[-1]["noun"])
    if post is None:      # neuter nominatives in -aṃ ("ākāsānañcāyatanaṃ …")
        return Tok("text", pre + np_dir(cs))
    return Tok("text", f"{pre}{np_obl(cs)} {post}")


ELLIPSIS_DELIMS = ("…",)


class Tok:
    """kind: 'text' | 'frame' | 'abl' | 'ins' | 'delim'"""
    __slots__ = ("kind", "hi", "verb", "pl")

    def __init__(self, kind, hi, verb="", pl=False):
        self.kind, self.hi, self.verb, self.pl = kind, hi, verb, pl


def lc(s):
    return s[:1].lower() + s[1:]


def items_of(table, phrase):
    return table.get(lc(phrase))


UNKNOWN = collections.Counter()
UNKNOWN_WHERE = {}
CUR = {"pl": False, "where": ""}


def tr_unit(u):
    """Translate one unit; returns a Tok."""
    key = lc(u)
    if key in PH:
        return Tok("text", PH[key])
    m = RX_DEP.match(u)
    if m:
        o, r = items_of(ACC, m.group("obj")), items_of(NOM, m.group("res"))
        if o and r:
            d = S.DEP[DEPW[m.group("dep")]]
            head = f"{OBJ(o)} {d} {RES(r)}"
            verb = ""
            if m.group("verb"):
                verb = "उत्पन्न होती हैं" if m.group("verb") == "uppajjanti" else "उत्पन्न होती है"
            CUR["pl"] = m.group("verb") == "uppajjanti"
            CUR["dep"] = DEPW[m.group("dep")]
            if m.group("cond"):
                c = m.group("cond")
                return Tok("frame", f"{head} {S.NABL(c) if m.group('neg') else S.ABL(c)}", verb, CUR["pl"])
            return Tok("frame", head, verb, CUR["pl"])
    m = RX_PANHA.match(u)
    if m:
        s_, d_ = items_of(NOM, m.group("src")), items_of(GEN, m.group("dst"))
        if s_ and d_:
            pl = m.group("dh") == "dhammā"
            CUR["pl"] = pl
            CUR["verb"] = "कारण होती हैं" if pl else "कारण होती है"
            CUR["frame_verb"] = CUR["verb"]
            head = f"{RES(s_)}, {DAT(d_)}"
            if m.group("cond"):
                c = m.group("cond")
                neg = bool(m.group("neg"))
                return Tok("frame", f"{head} {S.NAME(c)} के रूप में",
                           ("कारण नहीं होतीं" if pl else "कारण नहीं होती") if neg else
                           ("कारण होती हैं" if pl else "कारण होती है"), pl)
            return Tok("text", head)
    m = RX_ABL.match(key)
    if m:
        c = m.group("cond")
        return Tok("abl", S.NABL(c) if m.group("neg") else S.ABL(c))
    m = RX_INS.match(key)
    if m:
        v = (CUR.get("frame_verb") if CUR.get("at_start") else CUR.get("verb")) or "कारण होती है"
        if m.group("neg"):
            v = v.replace("होते हैं", "नहीं होते").replace("होती हैं", "नहीं होतीं").replace(
                "होता है", "नहीं होता").replace("होती है", "नहीं होती")
        return Tok("ins", f"{S.NAME(m.group('cond'))} के रूप में", v, CUR["pl"])
    t = tr_sub(u) or (tr_sub(key) if key != u else None)
    if t:
        return t
    # source quirk: a pañhā frame run into its first label without " – " ("… dhammassa sahajātaṃ")
    if u.endswith(" sahajātaṃ"):
        t = tr_unit(u[: -len(" sahajātaṃ")])
        if not t.hi.startswith("«"):
            hi = (t.hi + " " + t.verb).strip() if t.verb else t.hi
            return Tok("text", hi + " " + PH["sahajātaṃ"])
    UNKNOWN[key] += 1
    UNKNOWN_WHERE.setdefault(key, CUR["where"])
    return Tok("text", "«" + u + "»")


DELIM_RX = re.compile(r"(\s*\{[^}]*\}\s*|\s*\(\d+\)\s*|\s*…pe…\s*|\s*…\s*|\s+–\s+|;\s*|,\s*|\.(?=\s|$|\)|\()\s*|"
                      r"\s*\(|\)\s*)")


def variant(d):
    inner = d.strip()[1:-1]
    if inner in PH:
        return d.replace(d.strip(), PH[inner])
    UNKNOWN["{" + inner + "}"] += 1
    UNKNOWN_WHERE.setdefault("{" + inner + "}", CUR["where"])
    return d


def hi_delim(d):
    if d.strip().startswith("{"):
        return variant(d)
    if d.strip() == ".":
        return d.replace(".", "।")
    return d.replace("…pe…", "…")


def tr_body(body):
    parts = DELIM_RX.split(body)
    toks = []
    for i, p in enumerate(parts):
        if i % 2:
            toks.append(Tok("delim", hi_delim(p)))
        elif p.strip():
            lead = p[: len(p) - len(p.lstrip())]
            trail = p[len(p.rstrip()):]
            if lead:
                toks.append(Tok("delim", lead))
            CUR["at_start"] = not any(t.kind != "delim" for t in toks)
            toks.append(tr_unit(p.strip()))
            if trail:
                toks.append(Tok("delim", trail))
    # move frame verbs to the end of the chain of conditions that follows
    out = []
    i = 0
    while i < len(toks):
        t = toks[i]
        if t.kind in ("frame", "ins") and t.verb:
            want = "ins" if t.verb.startswith("कारण") else "abl"
            last = i
            while (last + 2 < len(toks) and toks[last + 1].kind == "delim" and toks[last + 1].hi.strip() == "…"
                   and toks[last + 2].kind == want):
                last += 2
            seq = [s.hi for s in toks[i:last + 1]]
            seq[-1] = seq[-1] + " " + t.verb
            out += seq
            i = last + 1
            continue
        out.append(t.hi)
        i += 1
    return "".join(out)


# counting lines ---------------------------------------------------------------------
COUNT_SLIPS = {"ādhipatiyā": "adhipatiyā"}   # spelling slips, rendered as the word meant (see notes)


def is_count(body):
    w = re.findall(r"[^\s,;.…()]+", body)
    if not w:
        return False
    k0 = S._classify(w[0])[0]
    if k0 in ("loc", "neg_loc"):
        return True
    if k0 in ("abl", "neg_abl") and len(w) > 1 and S._classify(w[1])[0] in ("loc", "neg_loc"):
        return True
    return False


def tr_count(body):
    parts = re.split(r"(\s*\([^)]*\))", body)
    out = ""
    for i, p in enumerate(parts):
        if i % 2:
            inner = p.strip()[1:-1]
            if inner in PH:
                out += p.replace(p.strip(), "(" + PH[inner] + ")")
            else:
                UNKNOWN["(" + inner + ")"] += 1
                UNKNOWN_WHERE.setdefault("(" + inner + ")", CUR["where"])
                out += p
        elif p.strip():
            if re.fullmatch(r"[\s.,;]+", p):
                out += p.replace(".", "।")
            else:
                lead = p[: len(p) - len(p.lstrip())]
                q = p.strip()
                for a, b in COUNT_SLIPS.items():
                    q = q.replace(a, b)
                try:
                    out += lead + S.count_hi(q)
                except ValueError as e:
                    UNKNOWN["COUNT " + str(e)] += 1
                    UNKNOWN_WHERE.setdefault("COUNT " + str(e), CUR["where"])
                if p.endswith(" "):
                    out += " "
    return out


# headings ----------------------------------------------------------------------------
def tr_heading(text):
    if text in HEAD:
        return HEAD[text]
    star = text.startswith("*") and text.endswith("*")
    t = text.strip("*")
    m = re.match(r"^(\d+(?:-\d+)?\.? )(.*)$", t)
    num, t = (m.group(1), m.group(2)) if m else ("", t)
    if t in HEAD:
        h = num + HEAD[t]
    else:
        UNKNOWN["#" + t] += 1
        UNKNOWN_WHERE.setdefault("#" + t, CUR["where"])
        h = num + "«" + t + "»"
    return f"*{h}*" if star else h


def tr_line(line):
    m = S.ID_RX.search(line)
    bid = m.group(1) if m else ""
    body = S.ID_RX.sub("", line) if m else line
    CUR["where"] = bid or body[:40]
    CUR["pl"] = False
    CUR["verb"] = ""
    CUR["dep"] = ""
    hm = re.match(r"^(#+) (.*)$", body)
    if hm:
        return hm.group(1) + " " + tr_heading(hm.group(2))
    if body in LINES:
        return LINES[body]
    if is_count(body):
        return tr_count(body)
    return tr_body(body)


def build(fname):
    ptxt = (S.PALI_DIR / fname).read_text(encoding="utf-8")
    hi = [tr_line(l) for l in ptxt.splitlines() if l.strip()]
    return ptxt, hi


def main():
    outs = {}
    for f in FILES:
        ptxt, hi = build(f)
        outs[f] = S.assemble(ptxt, hi)
    if UNKNOWN or "--unknown" in sys.argv:
        with open(HERE / "unknown_3-01_3-02_3-10.txt", "w", encoding="utf-8", newline="\n") as fh:
            for k, v in sorted(UNKNOWN.items(), key=lambda kv: (UNKNOWN_WHERE[kv[0]], kv[0])):
                fh.write(f"{v}\t{UNKNOWN_WHERE[k]}\t{k}\n")
        print("unknown units:", len(UNKNOWN), "occurrences:", sum(UNKNOWN.values()))
        if UNKNOWN:
            sys.exit(1)
    for f, text in outs.items():
        with open(S.HI_DIR / f, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)
        print("wrote", S.HI_DIR / f)
    pairs = [(S.PALI_DIR / f, S.HI_DIR / f) for f in FILES]
    sys.exit(1 if S.check(pairs) else 0)


if __name__ == "__main__":
    main()
