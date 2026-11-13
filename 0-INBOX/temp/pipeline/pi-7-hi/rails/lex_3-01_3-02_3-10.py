"""Lexicon for build_rails_3-01_3-02_3-10.py (pi-7 Hindi plain RAILS, files 3-01, 3-02, 3-10).
All Pāli keys are lowercase at word starts (the builder lowercases initials)."""
import sys
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi\rails")
import build_rails_sample as S  # noqa: E402  (read-only)

# ------------------------------------------------------------------ dyad items
# (key, acc sg, nom sg, dat sg, Hindi attribute (feminine, before परिघटना), complex?)
ITEMS = [
    ("hetu", "hetuṃ", "hetu", "hetussa", "मूल रूपी", False),
    ("nahetu", "nahetuṃ", "nahetu", "nahetussa", "मूल रूपी न होने वाली", False),
    ("sahetuka", "sahetukaṃ", "sahetuko", "sahetukassa", "मूल वाली", False),
    ("ahetuka", "ahetukaṃ", "ahetuko", "ahetukassa", "मूल से रहित", False),
    ("hetusampayutta", "hetusampayuttaṃ", "hetusampayutto", "hetusampayuttassa", "मूलों से जुड़ी", False),
    ("hetuvippayutta", "hetuvippayuttaṃ", "hetuvippayutto", "hetuvippayuttassa", "मूलों से अलग", False),
    ("hetusahetuka", "hetuñceva sahetukañca", "hetu ceva sahetuko ca", "hetussa ceva sahetukassa ca", "मूल रूपी भी और मूल वाली भी", True),
    ("sahetukanahetu", "sahetukañceva na ca hetuṃ", "sahetuko ceva na ca hetu", "sahetukassa ceva na ca hetussa", "मूल वाली, पर स्वयं मूल रूपी न होने वाली", True),
    ("hetuhetusampayutta", "hetuñceva hetusampayuttañca", "hetu ceva hetusampayutto ca", "hetussa ceva hetusampayuttassa ca", "मूल रूपी भी और मूलों से जुड़ी भी", True),
    ("hetusampayuttanahetu", "hetusampayuttañceva na ca hetuṃ", "hetusampayutto ceva na ca hetu", "hetusampayuttassa ceva na ca hetussa", "मूलों से जुड़ी, पर स्वयं मूल रूपी न होने वाली", True),
    ("nahetusahetuka", "nahetuṃ sahetukaṃ", "nahetu sahetuko", "nahetusahetukassa", "मूल रूपी न होने वाली, पर मूल वाली", True),
    ("nahetuahetuka", "nahetuṃ ahetukaṃ", "nahetu ahetuko", "nahetuahetukassa", "मूल रूपी न होने वाली और मूल से रहित", True),
    ("sappaccaya", "sappaccayaṃ", "sappaccayo", "sappaccayassa", "कारणों पर निर्भर रहने वाली", False),
    ("appaccaya", "appaccayaṃ", "appaccayo", "appaccayassa", "कारणों पर निर्भर न रहने वाली", False),
    ("saṅkhata", "saṅkhataṃ", "saṅkhato", "saṅkhatassa", "निर्मित", False),
    ("asaṅkhata", "asaṅkhataṃ", "asaṅkhato", "asaṅkhatassa", "अनिर्मित", False),
    ("sanidassana", "sanidassanaṃ", "sanidassano", "sanidassanassa", "दिखाई देने वाली", False),
    ("anidassana", "anidassanaṃ", "anidassano", "anidassanassa", "दिखाई न देने वाली", False),
    ("sappaṭigha", "sappaṭighaṃ", "sappaṭigho", "sappaṭighassa", "टकराव वाली", False),
    ("appaṭigha", "appaṭighaṃ", "appaṭigho", "appaṭighassa", "टकराव से रहित", False),
    ("rūpī", "rūpiṃ", "rūpī", "rūpissa", "भौतिक", False),
    ("arūpī", "arūpiṃ", "arūpī", "arūpissa", "अभौतिक", False),
    ("lokiya", "lokiyaṃ", "lokiyo", "lokiyassa", "लौकिक", False),
    ("lokuttara", "lokuttaraṃ", "lokuttaro", "lokuttarassa", "लोकोत्तर", False),
    ("viññeyya", "kenaci viññeyyaṃ", "kenaci viññeyyo", "kenaci viññeyyassa", "किसी एक प्रकार की चेतना से जानी जा सकने वाली", False),
    ("naviññeyya", "kenaci naviññeyyaṃ", "kenaci naviññeyyo", "kenaci naviññeyyassa", "किसी एक प्रकार की चेतना से न जानी जा सकने वाली", False),
    ("upādāna", "upādānaṃ", "upādāno", "upādānassa", "आसक्ति रूपी", False),
    ("noupādāna", "noupādānaṃ", "noupādāno", "noupādānassa", "आसक्ति रूपी न होने वाली", False),
    ("upādāniya", "upādāniyaṃ", "upādāniyo", "upādāniyassa", "आसक्ति का विषय बनने वाली", False),
    ("anupādāniya", "anupādāniyaṃ", "anupādāniyo", "anupādāniyassa", "आसक्ति का विषय न बनने वाली", False),
    ("upādānasampayutta", "upādānasampayuttaṃ", "upādānasampayutto", "upādānasampayuttassa", "आसक्ति से जुड़ी", False),
    ("upādānavippayutta", "upādānavippayuttaṃ", "upādānavippayutto", "upādānavippayuttassa", "आसक्ति से अलग", False),
    ("upādānaupādāniya", "upādānañceva upādāniyañca", "upādāno ceva upādāniyo ca", "upādānassa ceva upādāniyassa ca", "आसक्ति रूपी भी और आसक्ति का विषय बनने वाली भी", True),
    ("upādāniyanoupādāna", "upādāniyañceva no ca upādānaṃ", "upādāniyo ceva no ca upādāno", "upādāniyassa ceva no ca upādānassa", "आसक्ति का विषय बनने वाली, पर स्वयं आसक्ति रूपी न होने वाली", True),
    ("upādānaupādānasampayutta", "upādānañceva upādānasampayuttañca", "upādāno ceva upādānasampayutto ca", "upādānassa ceva upādānasampayuttassa ca", "आसक्ति रूपी भी और आसक्ति से जुड़ी भी", True),
    ("upādānasampayuttanoupādāna", "upādānasampayuttañceva no ca upādānaṃ", "upādānasampayutto ceva no ca upādāno", "upādānasampayuttassa ceva no ca upādānassa", "आसक्ति से जुड़ी, पर स्वयं आसक्ति रूपी न होने वाली", True),
    ("upādānavippayuttaupādāniya", "upādānavippayuttaṃ upādāniyaṃ", "upādānavippayutto upādāniyo", "upādānavippayuttaupādāniyassa", "आसक्ति से अलग, पर उसका विषय बनने वाली", True),
    ("upādānavippayuttaanupādāniya", "upādānavippayuttaṃ anupādāniyaṃ", "upādānavippayutto anupādāniyo", "upādānavippayuttaanupādāniyassa", "आसक्ति से अलग और उसका विषय न बनने वाली", True),
]
IT = {k: (a, n, d, h, c) for k, a, n, d, h, c in ITEMS}
PAIRS = [("hetu", "nahetu"), ("sahetuka", "ahetuka"), ("hetusampayutta", "hetuvippayutta"),
         ("hetusahetuka", "sahetukanahetu"), ("hetuhetusampayutta", "hetusampayuttanahetu"),
         ("nahetusahetuka", "nahetuahetuka"), ("sappaccaya", "appaccaya"), ("saṅkhata", "asaṅkhata"),
         ("sanidassana", "anidassana"), ("sappaṭigha", "appaṭigha"), ("rūpī", "arūpī"), ("lokiya", "lokuttara"),
         ("viññeyya", "naviññeyya"), ("upādāna", "noupādāna"), ("upādāniya", "anupādāniya"),
         ("upādānasampayutta", "upādānavippayutta"), ("upādānaupādāniya", "upādāniyanoupādāna"),
         ("upādānaupādānasampayutta", "upādānasampayuttanoupādāna"),
         ("upādānavippayuttaupādāniya", "upādānavippayuttaanupādāniya")]

ACC_I, NOM_I, PNOM_I, DAT_I = {}, {}, {}, {}
for k, (a, n, d, h, c) in IT.items():
    ACC_I[a] = f"{h} परिघटना"
    NOM_I[n + " dhammo"] = (f"{h} परिघटना", "s")
    PNOM_I[n + " dhammo"] = (f"{h} परिघटना", "fs")
    DAT_I[d] = f"{h} परिघटना के लिए"


def _ca_acc(a):
    """last word -ṃ -> -ñca"""
    ws = a.split(" ")
    w = ws[-1]
    if w.endswith("ñca"):
        return a + "ñca" if False else a  # already has ñca
    ws[-1] = w[:-1] + "ñca" if w.endswith("ṃ") else w + "ñca"
    return " ".join(ws)


for k1, k2 in PAIRS:
    a1, n1, d1, h1, c1 = IT[k1]
    a2, n2, d2, h2, c2 = IT[k2]
    cx = c1 or c2
    accs = {f"{_ca_acc(a1)} {_ca_acc(a2)}", f"{a1}ñca {a2}ñca"}
    if cx:
        accs |= {f"{a1} {a2}ñca", f"{a1}ñca {a2}ñca", f"{a1} {_ca_acc(a2)}", f"{_ca_acc(a1)} {_ca_acc(a2)}"}
    for acc in accs:
        ACC_I[acc] = f"{h1} परिघटना और {h2} परिघटना"
    nom_h = f"{h1} परिघटना और {h2} परिघटना" if cx else f"{h1} और {h2} परिघटनाएँ"
    for nom in {f"{n1} ca {n2} ca dhammā", f"{n1} {n2} ca dhammā" if n1.endswith(" ca") else f"{n1} ca {n2} ca dhammā"}:
        NOM_I[nom] = (nom_h, "p")
        PNOM_I[nom] = (nom_h, "fp")
    DAT_I[f"{d1} ca {d2} ca"] = f"{h1} परिघटना और {h2} परिघटना के लिए"
    if d1.endswith(" ca"):
        DAT_I[f"{d1} {d2} ca"] = f"{h1} परिघटना और {h2} परिघटना के लिए"

# spellings attested in the source
ACC_I["upādānañca noupādānaṃ ca"] = ACC_I["upādānañca noupādānañca"]
NOM_I["hetū ca nahetū ca dhammā"] = NOM_I["hetu ca nahetu ca dhammā"]
PNOM_I["hetū ca nahetū ca dhammā"] = PNOM_I["hetu ca nahetu ca dhammā"]
DAT_I["nahetusahetukassa ca nahetuahetukassa ca"] = DAT_I["nahetusahetukassa ca nahetuahetukassa ca"]
DAT_I["lokuttarasa"] = DAT_I["lokuttarassa"]   # spelling slip in the source, rendered as meant
DAT_I["sahetukassa ceva na ca hetussa ca"] = DAT_I["sahetukassa ceva na ca hetussa"]
DAT_I["upādāniyassa ceva no ca upādānassa ca"] = DAT_I["upādāniyassa ceva no ca upādānassa"]

FRAME = {"paṭicca": "पर निर्भर होकर", "paccayā": "के कारण", "nissāya": "के आश्रय से",
         "saṃsaṭṭho": "से घुल-मिलकर", "saṃsaṭṭhā": "से घुल-मिलकर", "sampayutto": "से जुड़कर",
         "sampayuttā": "से जुड़कर", "sahajāto": "के साथ जन्म लेकर", "sahajātā": "के साथ जन्म लेकर"}
FRAME_ROOT = {"paṭicca": "paṭicca", "paccayā": "paccayā", "nissāya": "nissāya", "saṃsaṭṭho": "saṃsaṭṭha",
              "saṃsaṭṭhā": "saṃsaṭṭha", "sampayutto": "sampayutta", "sampayuttā": "sampayutta",
              "sahajāto": "sahajāta", "sahajātā": "sahajāta"}

# ------------------------------------------------------------------ body units: Pāli form -> (Hindi, case, gn)
# case: N nominative (direct form), A accusative (oblique), D dative/genitive (oblique, «के लिए» added by the builder)
UNITS = {}


def U(keys, hi, case, gn="mp"):
    for k in keys.split("|"):
        UNITS[k] = (hi, case, gn)


def masc(h, form):
    """feminine attribute -> masculine (form: 'd' direct sg, 'o' oblique / plural)"""
    rep = {"वाली": "वाला" if form == "d" else "वाले", "जुड़ी": "जुड़ा" if form == "d" else "जुड़े",
           "जानी": "जाना" if form == "d" else "जाने"}
    for a, b in rep.items():
        h = h.replace(a, b)
    return h


# adjective stems for the body phrases: key -> (nom pl, acc pl, dat pl, acc sg, nom sg m, nom sg f, neuter pl)
ADJ = {
    "sahetuka": ("sahetukā", "sahetuke", "sahetukānaṃ", "sahetukaṃ", "sahetuko", "sahetukā", "sahetukāni"),
    "ahetuka": ("ahetukā", "ahetuke", "ahetukānaṃ", "ahetukaṃ", "ahetuko", "ahetukā", "ahetukāni"),
    "nahetu": ("nahetū", "nahetū", "nahetūnaṃ", "nahetuṃ", "nahetu", "nahetu", "nahetūni"),
    "hetusampayutta": ("hetusampayuttā", "hetusampayutte", "hetusampayuttānaṃ", "hetusampayuttaṃ", "hetusampayutto", "hetusampayuttā", "-"),
    "hetuvippayutta": ("hetuvippayuttā", "hetuvippayutte", "hetuvippayuttānaṃ", "hetuvippayuttaṃ", "hetuvippayutto", "hetuvippayuttā", "-"),
    "nahetusahetuka": ("nahetusahetukā", "nahetusahetuke", "nahetusahetukānaṃ", "nahetusahetukaṃ", "nahetusahetuko", "nahetusahetukā", "-"),
    "nahetuahetuka": ("nahetuahetukā", "nahetuahetuke", "nahetuahetukānaṃ", "nahetuahetukaṃ", "nahetuahetuko", "nahetuahetukā", "-"),
    "sappaccaya": ("sappaccayā", "sappaccaye", "sappaccayānaṃ", "sappaccayaṃ", "sappaccayo", "sappaccayā", "-"),
    "saṅkhata": ("saṅkhatā", "saṅkhate", "saṅkhatānaṃ", "saṅkhataṃ", "saṅkhato", "saṅkhatā", "-"),
    "sanidassana": ("sanidassanā", "sanidassane", "sanidassanānaṃ", "sanidassanaṃ", "sanidassano", "sanidassanā", "-"),
    "anidassana": ("anidassanā", "anidassane", "anidassanānaṃ", "anidassanaṃ", "anidassano", "anidassanā", "-"),
    "sappaṭigha": ("sappaṭighā", "sappaṭighe", "sappaṭighānaṃ", "sappaṭighaṃ", "sappaṭigho", "sappaṭighā", "-"),
    "appaṭigha": ("appaṭighā", "appaṭighe", "appaṭighānaṃ", "appaṭighaṃ", "appaṭigho", "appaṭighā", "-"),
    "lokiya": ("lokiyā", "lokiye", "lokiyānaṃ", "lokiyaṃ", "lokiyo", "lokiyā", "-"),
    "lokuttara": ("lokuttarā", "lokuttare", "lokuttarānaṃ", "lokuttaraṃ", "lokuttaro", "lokuttarā", "-"),
    "upādāna": ("upādānā", "upādāne", "upādānānaṃ", "upādānaṃ", "upādāno", "upādānā", "-"),
    "noupādāna": ("noupādānā", "noupādāne", "noupādānānaṃ", "noupādānaṃ", "noupādāno", "noupādānā", "-"),
    "upādāniya": ("upādāniyā", "upādāniye", "upādāniyānaṃ", "upādāniyaṃ", "upādāniyo", "upādāniyā", "-"),
    "anupādāniya": ("anupādāniyā", "anupādāniye", "anupādāniyānaṃ", "anupādāniyaṃ", "anupādāniyo", "anupādāniyā", "-"),
    "upādānasampayutta": ("upādānasampayuttā", "upādānasampayutte", "upādānasampayuttānaṃ", "upādānasampayuttaṃ", "upādānasampayutto", "upādānasampayuttā", "-"),
    "upādānavippayutta": ("upādānavippayuttā", "upādānavippayutte", "upādānavippayuttānaṃ", "upādānavippayuttaṃ", "upādānavippayutto", "upādānavippayuttā", "-"),
}
ADJ_X = {  # multi-word adjective items: name -> (IT key, forms as in ADJ)
    "nahetu sahetuka": ("nahetusahetuka", ("nahetū sahetukā", "nahetū sahetuke", "nahetusahetukānaṃ", "nahetuṃ sahetukaṃ", "nahetu sahetuko", "nahetu sahetukā", "-")),
    "nahetu ahetuka": ("nahetuahetuka", ("nahetū ahetukā", "nahetū ahetuke", "nahetuahetukānaṃ", "nahetuṃ ahetukaṃ", "nahetu ahetuko", "nahetu ahetukā", "nahetu ahetukāni")),
    "sahetuka ceva na ca hetu": ("sahetukanahetu", ("sahetukā ceva na ca hetū", "sahetuke ceva na ca hetū", "sahetukānañceva na ca hetūnaṃ", "sahetukañceva na ca hetuṃ", "sahetuko ceva na ca hetu", "sahetukā ceva na ca hetū", "-")),
    "hetusampayutta ceva na ca hetu": ("hetusampayuttanahetu", ("hetusampayuttā ceva na ca hetū", "hetusampayutte ceva na ca hetū", "hetusampayuttānañceva na ca hetūnaṃ", "hetusampayuttañceva na ca hetuṃ", "hetusampayutto ceva na ca hetu", "hetusampayuttā ceva na ca hetū", "-")),
    "upādāniya ceva no ca upādāna": ("upādāniyanoupādāna", ("upādāniyā ceva no ca upādānā", "upādāniye ceva no ca upādāne", "upādāniyānañceva no ca upādānānaṃ", "upādāniyañceva no ca upādānaṃ", "upādāniyo ceva no ca upādāno", "upādāniyā ceva no ca upādānā", "-")),
    "upādānasampayutta ceva no ca upādāna": ("upādānasampayuttanoupādāna", ("upādānasampayuttā ceva no ca upādānā", "upādānasampayutte ceva no ca upādāne", "upādānasampayuttānañceva no ca upādānānaṃ", "upādānasampayuttañceva no ca upādānaṃ", "upādānasampayutto ceva no ca upādāno", "upādānasampayuttā ceva no ca upādānā", "-")),
    "upādānavippayutta upādāniya": ("upādānavippayuttaupādāniya", ("upādānavippayuttā upādāniyā", "upādānavippayutte upādāniye", "upādānavippayuttaupādāniyānaṃ", "upādānavippayuttaṃ upādāniyaṃ", "upādānavippayutto upādāniyo", "upādānavippayuttā upādāniyā", "-")),
    "upādānavippayutta anupādāniya": ("upādānavippayuttaanupādāniya", ("upādānavippayuttā anupādāniyā", "upādānavippayutte anupādāniye", "upādānavippayuttaanupādāniyānaṃ", "upādānavippayuttaṃ anupādāniyaṃ", "upādānavippayutto anupādāniyo", "upādānavippayuttā anupādāniyā", "-")),
}
for _n, (_k, _f) in ADJ_X.items():
    ADJ[_n] = _f
ADJ_KEY = {n: k for n, (k, f) in ADJ_X.items()}
for k, (npl, apl, dpl, asg, nsg, fsg, neu) in ADJ.items():
    hf = IT[ADJ_KEY.get(k, k)][3]
    hm, hmd = masc(hf, "o"), masc(hf, "d")
    U(f"{npl} khandhā|{npl} khandhā ca", f"{hm} समूह", "N", "mp")
    U(f"{apl} khandhe|{apl} ca khandhe", f"{hm} समूहों", "A")
    U(f"{dpl} khandhānaṃ|{dpl[:-1]}ñca khandhānaṃ", f"{hm} समूहों", "D")
    U(f"{asg} ekaṃ khandhaṃ|{asg} ekaṃ khandhañca", f"एक {hm} समूह" if " " not in hf else f"{hm} एक समूह", "A")
    U(f"{nsg} eko khandho", f"एक {hmd} समूह" if " " not in hf else f"{hmd} एक समूह", "N", "ms")
    U(f"{fsg} cetanā", f"{hmd} इरादा", "N", "ms")
    U(f"{npl} āhārā", f"{hm} आहार", "N", "mp")
    U(f"{npl} indriyā", f"{hf} क्षमताएँ", "N", "fp")
    U(f"{npl} hetū", f"{hm} मूल", "N", "mp")
    U(f"{dpl} hetūnaṃ", f"{hm} मूलों", "D")
    if neu != "-":
        U(f"{neu} jhānaṅgāni", f"{hm} ध्यान के अंग", "N", "mp")
    U(f"{k[:-1] if k.endswith('a') else k}ādhipati|{nsg} adhipati", f"{hf} प्रधानता", "N", "fs")
    U(f"{nsg} vipāko", f"{hmd} कर्म-फल", "N", "ms")
    U(f"{asg} cittaṃ", f"{hm} मन", "A")
    U(f"{asg} bhavaṅgaṃ", f"{hf} जीवन-धारा", "N", "fs")
    U(f"{asg} cuticittaṃ", f"{hmd} मृत्यु का मन", "N", "ms")
    U(f"{nsg[:-1] if nsg.endswith('o') else nsg}assa upapatticittassa|{dpl[:-4]}assa upapatticittassa", f"{hm} जन्म के मन", "D")
    U(f"{dpl[:-4]}assa bhavaṅgassa", f"{hf} जीवन-धारा", "D")
    U(f"{dpl[:-4]}assa vuṭṭhānassa", f"{hm} बाहर आने", "D")

U("nahetu sahetukādhipati|nahetusahetukādhipati", "मूल रूपी न होने वाली, पर मूल वाली प्रधानता", "N", "fs")
U("hetu ceva sahetukādhipati", "मूल रूपी भी और मूल वाली भी प्रधानता", "N", "fs")
U("sahetuko ceva na ca hetu adhipati", "मूल वाली, पर स्वयं मूल रूपी न होने वाली प्रधानता", "N", "fs")
U("hetusampayutto ceva na ca hetu adhipati", "मूलों से जुड़ी, पर स्वयं मूल रूपी न होने वाली प्रधानता", "N", "fs")
U("hetu ceva hetusampayuttādhipati", "मूल रूपी भी और मूलों से जुड़ी भी प्रधानता", "N", "fs")
U("taṃ", "उस", "A"); U("cakkhuṃ", "आँख", "A")
U("purejātassa", "पहले उत्पन्न इस शरीर", "D")
# 3-02 matter vocabulary
U("itthindriyaṃ|itthindriyañca", "स्त्रीत्व की क्षमता", "AN", "fs"); U("purisindriyaṃ|purisindriyañca", "पुरुषत्व की क्षमता", "AN", "fs")
U("jīvitindriyaṃ|jīvitindriyañca", "जीवन-क्षमता", "AN", "fs"); U("itthindriyassa", "स्त्रीत्व की क्षमता", "D")
U("āpodhātuṃ|āpodhātuñca", "जल तत्व", "A"); U("āpodhātu|āpodhātu ca", "जल तत्व", "N", "ms"); U("āpodhātuyā", "जल तत्व", "D")
U("phoṭṭhabbe", "स्पर्शों", "A"); U("rūpe", "दृश्य रूपों", "A"); U("sadde", "ध्वनियों", "A")
U("rūpaṃ", "भौतिक रूप", "AN", "ms"); U("kāyassa", "शरीर", "D")
U("imassa", "इस", "D")  # only before an adjective + kāyassa
U("cakkhuviññāṇasahagataṃ ekaṃ khandhaṃ|cakkhuviññāṇasahagataṃ ekaṃ khandhañca", "आँख की चेतना के साथ होने वाले एक समूह", "A")
U("kāyaviññāṇasahagataṃ ekaṃ khandhaṃ|kāyaviññāṇasahagataṃ ekaṃ khandhañca", "शरीर की चेतना के साथ होने वाले एक समूह", "A")
U("cakkhuviññāṇasahagatānaṃ khandhānaṃ", "आँख की चेतना के साथ होने वाले समूहों", "D")
U("kāyaviññāṇasahagatānaṃ khandhānaṃ", "शरीर की चेतना के साथ होने वाले समूहों", "D")
U("cakkhuviññāṇasahagato eko khandho", "आँख की चेतना के साथ होने वाला एक समूह", "N", "ms")
U("kāyaviññāṇasahagato eko khandho", "शरीर की चेतना के साथ होने वाला एक समूह", "N", "ms")
U("cakkhuviññāṇañca|cakkhuviññāṇaṃ", "आँख की चेतना", "AN", "fs"); U("kāyaviññāṇañca", "शरीर की चेतना", "AN", "fs")
U("cakkhundriyañca", "आँख की क्षमता", "AN", "fs"); U("kāyindriyañca", "शरीर की क्षमता", "AN", "fs")
U("kaṭattārūpā", "किए गए कर्म से उत्पन्न भौतिक रूप", "N")
# 3-10 clinging vocabulary
U("upādānā|upādānā ca", "आसक्तियाँ", "N", "fp"); U("upādāne|upādāne ca", "आसक्तियों", "A")
U("upādānānaṃ|upādānānañca", "आसक्तियों", "D")
for p, h in [("kām", "इंद्रिय-सुखों के प्रति आसक्ति"), ("diṭṭh", "दृष्टियों के प्रति आसक्ति"),
             ("sīlabbat", "सदाचार और व्रतों के प्रति आसक्ति"), ("attavād", "आत्मवाद के प्रति आसक्ति")]:
    U(f"{p}upādānaṃ|{p}upādānañca", h, "AN", "fs"); U(f"{p}upādānassa", h, "D")
DGV = "ग़लत दृष्टि से अलग और लोभ के साथ होने वाले"
U("diṭṭhigatavippayuttaṃ lobhaṃ|diṭṭhigatavippayuttaṃ lobhañca", "ग़लत दृष्टि से अलग लोभ", "A")
U("diṭṭhigatavippayutto lobho|diṭṭhigatavippayutto lobho ca", "ग़लत दृष्टि से अलग लोभ", "N", "ms")
U("diṭṭhigatavippayuttassa lobhassa|diṭṭhigatavippayuttalobhassa", "ग़लत दृष्टि से अलग लोभ", "D")
U("diṭṭhigatavippayutto rāgo", "ग़लत दृष्टि से अलग राग", "N", "ms")
U("diṭṭhigatavippayuttalobhasahagate khandhe|diṭṭhigatavippayuttalobhasahagate khandhe ca", DGV + " समूहों", "A")
U("diṭṭhigatavippayuttalobhasahagatā khandhā|diṭṭhigatavippayuttalobhasahagatā khandhā ca", DGV + " समूह", "N")
U("diṭṭhigatavippayuttalobhasahagatānaṃ khandhānaṃ", DGV + " समूहों", "D")
U("diṭṭhigatavippayuttalobhasahagataṃ ekaṃ khandhaṃ|diṭṭhigatavippayuttalobhasahagataṃ ekaṃ khandhañca", DGV + " एक समूह", "A")
U("diṭṭhigatavippayuttalobhasahagato eko khandho", "ग़लत दृष्टि से अलग और लोभ के साथ होने वाला एक समूह", "N", "ms")
U("diṭṭhigatavippayuttalobhasahagatā cetanā", "ग़लत दृष्टि से अलग और लोभ के साथ होने वाला इरादा", "N", "ms")
U("diṭṭhigatavippayuttalobhasahagatādhipati", "ग़लत दृष्टि से अलग और लोभ के साथ होने वाली प्रधानता", "N", "fs")
U("rāgaṃ", "राग", "A")
_EARLY = ({
    "assādeti abhinandati": "रस लेता है, उसमें आनंद लेता है",
    "anantarūpanissayo pakatūpanissayo": "निकटता रूपी प्रबल आश्रय, स्वाभाविक प्रबल आश्रय",
    "ariyā maggā vuṭṭhahitvā": "आर्य मार्ग से उठकर",
    "ariyā maggaṃ upanissāya anuppannaṃ samāpattiṃ uppādenti": "आर्य मार्ग के प्रबल आश्रय से अनुत्पन्न ध्यान-अवस्था उत्पन्न करते हैं",
})
U("nahetu ahetukā āhārā", "मूल रूपी न होने वाले और मूल से रहित आहार", "N", "mp")
U("nahetu ahetukā indriyā", "मूल रूपी न होने वाली और मूल से रहित क्षमताएँ", "N", "fp")
U("nahetu sahetukā āhārā", "मूल रूपी न होने वाले, पर मूल वाले आहार", "N", "mp")
U("nahetu sahetukā indriyā", "मूल रूपी न होने वाली, पर मूल वाली क्षमताएँ", "N", "fp")
U("nahetu sahetukaṃ bhavaṅgaṃ", "मूल रूपी न होने वाली, पर मूल वाली जीवन-धारा", "N", "fs")
U("nahetu ahetukaṃ bhavaṅgaṃ", "मूल रूपी न होने वाली और मूल से रहित जीवन-धारा", "N", "fs")
U("nahetu sahetukaṃ cuticittaṃ", "मूल रूपी न होने वाला, पर मूल वाला मृत्यु का मन", "N", "ms")
U("nahetu ahetukaṃ cuticittaṃ", "मूल रूपी न होने वाला और मूल से रहित मृत्यु का मन", "N", "ms")

# hetu as a noun (the roots) and the six roots
U("hetū|hetu|hetū ca", "मूल", "N", "mp")
U("hetuṃ|hetuñca", "मूल", "A")
U("hetūnaṃ|hetūnañca", "मूलों", "D")
U("hetu adhipati", "मूल रूपी प्रधानता", "N", "fs")
U("nahetu adhipati", "मूल रूपी न होने वाली प्रधानता", "N", "fs")
for p, h in [("alobh", "लोभ का अभाव"), ("ados", "द्वेष का अभाव"), ("amoh", "मोह का अभाव"),
             ("lobh", "लोभ"), ("dos", "द्वेष"), ("moh", "मोह")]:
    obl = h.replace(" का ", " के ")
    U(f"{p}o|{p}o ca", h, "N", "ms")
    U(f"{p}aṃ|{p}añca", obl, "A")
    U(f"{p}assa", obl, "D")

# aggregates, matter, base
U("tayo khandhā", "तीन समूह", "N"); U("dve khandhā|dve khandhā ca", "दो समूह", "N"); U("eko khandho", "एक समूह", "N", "ms")
U("khandhā|khandhā ca", "समूह", "N"); U("sabbe khandhā", "सभी समूह", "N")
U("tayo khandhe", "तीन समूहों", "A"); U("dve khandhe|dve khandhe ca", "दो समूहों", "A"); U("khandhe|khandhe ca", "समूहों", "A")
U("ekaṃ khandhaṃ|ekaṃ khandhañca", "एक समूह", "A")
U("tiṇṇannaṃ khandhānaṃ", "तीन समूहों", "D"); U("dvinnaṃ khandhānaṃ", "दो समूहों", "D"); U("khandhānaṃ", "समूहों", "D")
U("sampayuttakā khandhā|sampayuttakā ca khandhā", "जुड़े हुए समूह", "N")
U("sampayuttake khandhe|sampayuttake ca khandhe", "जुड़े हुए समूहों", "A")
U("sampayuttakānaṃ khandhānaṃ|sampayuttakānañca khandhānaṃ", "जुड़े हुए समूहों", "D")
U("sampayuttakānaṃ hetūnaṃ", "जुड़े हुए मूलों", "D")
U("sampayuttakā cetanā", "जुड़ा हुआ इरादा", "N", "ms")
U("cittasamuṭṭhānaṃ rūpaṃ|cittasamuṭṭhānañca rūpaṃ", "मन से उत्पन्न भौतिक रूप", "AN", "ms")
U("kaṭattārūpaṃ|kaṭattā ca rūpaṃ", "किए गए कर्म से उत्पन्न भौतिक रूप", "AN", "ms")
U("upādārūpaṃ", "व्युत्पन्न भौतिक रूप", "AN", "ms")
U("cittasamuṭṭhānānaṃ rūpānaṃ|cittasamuṭṭhānānañca rūpānaṃ", "मन से उत्पन्न भौतिक रूपों", "D")
U("kaṭattārūpānaṃ|kaṭattā ca rūpānaṃ", "किए गए कर्म से उत्पन्न भौतिक रूपों", "D")
U("upādārūpānaṃ", "व्युत्पन्न भौतिक रूपों", "D")
U("vatthu|vatthu ca", "आधार", "N", "ms"); U("vatthuṃ|vatthuñca", "आधार", "A"); U("vatthussa", "आधार", "D")
U("ekaṃ mahābhūtaṃ|ekaṃ mahābhūtañca", "एक महाभूत", "AN", "ms"); U("tayo mahābhūtā", "तीन महाभूत", "N")
U("dve mahābhūtā", "दो महाभूत", "N"); U("tayo mahābhūte", "तीन महाभूतों", "A"); U("dve mahābhūte", "दो महाभूतों", "A")
U("mahābhūte|mahābhūte ca", "महाभूतों", "A"); U("mahābhūtā|mahābhūtā ca", "महाभूत", "N"); U("mahābhūtānaṃ", "महाभूतों", "D")
U("sabbe mahābhūtā", "सभी महाभूत", "N")
U("rūpajīvitindriyaṃ|rūpajīvitindriyañca", "भौतिक जीवन-क्षमता", "AN", "fs")
U("kabaḷīkāro āhāro|kabaḷīkāro āhāro ca", "कौर-कौर खाया जाने वाला भोजन", "N", "ms")
U("imassa kāyassa", "इस शरीर", "D"); U("purejātassa imassa kāyassa", "पहले उत्पन्न इस शरीर", "D")
U("cetanā", "इरादा", "N", "ms")
U("āvajjanā", "मन को विषय की ओर मोड़ना", "N", "ms"); U("āvajjanāya", "मन को विषय की ओर मोड़ने", "D")
U("pañcannaṃ viññāṇānaṃ", "पाँच प्रकार की चेतना", "D")
U("cakkhuviññāṇassa", "आँख की चेतना", "D"); U("sotaviññāṇassa", "कान की चेतना", "D")
U("ghānaviññāṇassa", "नाक की चेतना", "D"); U("jivhāviññāṇassa", "जीभ की चेतना", "D"); U("kāyaviññāṇassa", "शरीर की चेतना", "D")
U("cakkhuviññāṇaṃ", "आँख की चेतना", "N", "fs"); U("kāyaviññāṇaṃ", "शरीर की चेतना", "N", "fs")
for p, h in [("rūp", "दृश्य रूप"), ("sadd", "ध्वनि"), ("gandh", "गंध"), ("ras", "स्वाद"), ("phoṭṭhabb", "स्पर्श"),
             ("cakkh", "आँख"), ("sot", "कान"), ("ghān", "नाक"), ("jivh", "जीभ"), ("kāy", "शरीर")]:
    U(f"{p}āyatanaṃ|{p}āyatanañca", f"{h} का इंद्रिय-क्षेत्र", "AN", "ms")
    U(f"{p}āyatanassa", f"{h} के इंद्रिय-क्षेत्र", "D")
U("cakkhundriyaṃ|cakkhundriyañca", "आँख की क्षमता", "N", "fs"); U("kāyindriyaṃ|kāyindriyañca", "शरीर की क्षमता", "N", "fs")
U("phalasamāpattiyā", "फल की ध्यान-अवस्था", "D")
U("nevasaññānāsaññāyatanaṃ", "न पहचान न अ-पहचान का क्षेत्र", "N", "ms")
U("gotrabhu", "गोत्र-परिवर्तन", "N", "ms"); U("vodānaṃ", "शुद्धि", "N", "fs"); U("maggo", "मार्ग", "N", "ms")
U("phalaṃ", "फल", "N", "ms"); U("anulomaṃ", "अनुरूपता", "N", "fs")
U("gotrabhussa", "गोत्र-परिवर्तन", "D"); U("vodānassa", "शुद्धि", "D"); U("maggassa", "मार्ग", "D"); U("phalassa", "फल", "D")
U("nibbānaṃ", "निर्वाण", "AN", "ms")
U("kāyikaṃ sukhaṃ", "शारीरिक सुख", "AN", "ms"); U("kāyikaṃ dukkhaṃ", "शारीरिक दुःख", "AN", "ms")
U("kāyikassa sukhassa", "शारीरिक सुख", "D"); U("kāyikassa dukkhassa", "शारीरिक दुःख", "D")
U("utu", "तापमान", "N", "ms"); U("bhojanaṃ", "भोजन", "AN", "ms"); U("senāsanaṃ", "निवास-स्थान", "AN", "ms")
U("vipākānaṃ khandhānaṃ", "कर्म-फल रूपी समूहों", "D")
U("vicikicchāsahagato uddhaccasahagato moho|vicikicchāsahagato uddhaccasahagato moho ca", "संशय के साथ होने वाला या बेचैनी के साथ होने वाला मोह", "N", "ms")
U("vicikicchāsahagataṃ uddhaccasahagataṃ mohaṃ", "संशय के साथ होने वाले या बेचैनी के साथ होने वाले मोह", "A")
U("vicikicchāsahagatassa uddhaccasahagatassa mohassa", "संशय के साथ होने वाले या बेचैनी के साथ होने वाले मोह", "D")
U("vicikicchāsahagate uddhaccasahagate khandhe|vicikicchāsahagate uddhaccasahagate khandhe ca", "संशय के साथ होने वाले और बेचैनी के साथ होने वाले समूहों", "A")
U("vicikicchāsahagatā uddhaccasahagatā khandhā|vicikicchāsahagatā uddhaccasahagatā khandhā ca", "संशय के साथ होने वाले और बेचैनी के साथ होने वाले समूह", "N")
U("vicikicchāsahagatānaṃ uddhaccasahagatānaṃ khandhānaṃ", "संशय के साथ होने वाले और बेचैनी के साथ होने वाले समूहों", "D")
U("vicikicchāsahagataṃ uddhaccasahagataṃ ekaṃ khandhaṃ|vicikicchāsahagataṃ uddhaccasahagataṃ ekaṃ khandhañca", "संशय के साथ होने वाले या बेचैनी के साथ होने वाले एक समूह", "A")
U("vicikicchāsahagato uddhaccasahagato eko khandho", "संशय के साथ होने वाला या बेचैनी के साथ होने वाला एक समूह", "N", "ms")


# modifiers that precede a unit: Pāli -> {gn-key: Hindi}
MOD = {
    "purimā purimā": {"m": "पहले-पहले के", "f": "पहले-पहले की"},
    "purimo purimo": {"m": "पहले-पहले का", "f": "पहले-पहले की"},
    "pacchimānaṃ pacchimānaṃ": {"m": "बाद-बाद के", "f": "बाद-बाद की"},
    "pacchimassa pacchimassa": {"m": "बाद-बाद के", "f": "बाद-बाद की"},
    "pacchājātā": {"m": "बाद में उत्पन्न", "f": "बाद में उत्पन्न"},
    "purejātaṃ": {"m": "पहले उत्पन्न", "f": "पहले उत्पन्न"},
    "vipāko": {"m": "कर्म-फल रूपी", "f": "कर्म-फल रूपी"},
    "vipākā": {"m": "कर्म-फल रूपी", "f": "कर्म-फल रूपी"},
    "vipākaṃ": {"m": "कर्म-फल रूपी", "f": "कर्म-फल रूपी"},
    "vipākānaṃ": {"m": "कर्म-फल रूपी", "f": "कर्म-फल रूपी"},
}

# adjectives used as modifiers of any unit: Pāli word -> {"f": fem, "d": masc direct sg, "o": masc oblique/pl}
ADJF = {}
for k, (npl, apl, dpl, asg, nsg, fsg, neu) in ADJ.items():
    if " " in k:
        continue
    hf = IT[k][3]
    forms = {"f": hf, "d": masc(hf, "d"), "o": masc(hf, "o"), "m": masc(hf, "o")}
    for w in (npl, apl, dpl, asg, nsg, fsg, asg[:-1] + "ñca", dpl[:-1] + "ñca", dpl[:-4] + "assa", npl + "ñca"):
        ADJF.setdefault(w, forms)
for w, hf in [("rūpi", "भौतिक"), ("arūpi", "अभौतिक")]:
    forms = {"f": hf, "d": hf, "o": hf, "m": hf}
    for suf in ("ṃ", "ñca", "no", "nañca", "ssa", "naṃ", "nānaṃ", "nānañca", "nā"):
        ADJF[w + suf] = forms
ADJF["sanidassanaṃ"]  # sanity

NUM_EXTRA = {"cattāripi": "चारों", "navapi": "नौ"}

PREFIX = {"arūpe": "अभौतिक लोक में", "paṭisandhikkhaṇe": "पुनर्जन्म के क्षण में",
          "sahajātādhipati": "सह-उत्पत्ति रूपी प्रधानता", "ārammaṇādhipati": "विषय रूपी प्रधानता",
          "ahetukapaṭisandhikkhaṇe": "मूल से रहित पुनर्जन्म के क्षण में", "pavatte": "जीवन के दौरान"}

# ------------------------------------------------------------------ clauses (exact pieces)
CLAUSE_SKIP_S = set()
CLAUSE = {
    "paṭisandhikkhaṇe": "पुनर्जन्म के क्षण में", "ahetukapaṭisandhikkhaṇe": "मूल से रहित पुनर्जन्म के क्षण में",
    "arūpe": "अभौतिक लोक में",
    "bāhiraṃ": "बाह्य", "āhārasamuṭṭhānaṃ": "आहार से उत्पन्न", "utusamuṭṭhānaṃ": "तापमान से उत्पन्न",
    "asaññasattānaṃ": "पहचान-रहित प्राणियों में",
    "asaññasattānaṃ ekaṃ mahābhūtaṃ": "पहचान-रहित प्राणियों में एक महाभूत पर निर्भर होकर",
    "asaññasattānaṃ ekaṃ": "पहचान-रहित प्राणियों में एक",
    "asaññasattānaṃ mahābhūte paṭicca rūpajīvitindriyaṃ": "पहचान-रहित प्राणियों में महाभूतों पर निर्भर होकर भौतिक जीवन-क्षमता",
    "pañcaviññāṇaṃ": "पाँच प्रकार की चेतना",
    # labels
    "sahajātaṃ": "सह-उत्पत्ति", "sahajātā": "सह-उत्पत्ति", "sahajāto": "सह-उत्पत्ति", "purejātaṃ": "पूर्व-उत्पत्ति",
    "pacchājātaṃ": "पश्चात्-उत्पत्ति", "pacchājātā": "पश्चात्-उत्पत्ति", "āhāraṃ": "आहार", "indriyaṃ": "क्षमता",
    "nānākkhaṇikā": "भिन्न क्षण", "ārammaṇūpanissayo": "विषय रूपी प्रबल आश्रय",
    "anantarūpanissayo": "निकटता रूपी प्रबल आश्रय", "pakatūpanissayo": "स्वाभाविक प्रबल आश्रय",
    "ārammaṇapurejātaṃ": "विषय रूपी पूर्व-उत्पत्ति", "vatthupurejātaṃ": "आधार रूपी पूर्व-उत्पत्ति",
    "ārammaṇādhipati": "विषय रूपी प्रधानता", "sahajātādhipati": "सह-उत्पत्ति रूपी प्रधानता",
    "tīṇi": "तीन", "nava": "नौ", "anulomaṃ": "सकारात्मक क्रम", "paccanīyaṃ": "नकारात्मक क्रम",
    "anulomapaccanīyaṃ": "सकारात्मक-नकारात्मक क्रम", "paccanīyānulomaṃ": "नकारात्मक-सकारात्मक क्रम",
    # pañhāvāra narrative
    "dānaṃ datvā": "दान देकर", "dānaṃ datvā sīlaṃ": "दान देकर, सदाचार",
    "uposathakammaṃ katvā taṃ paccavekkhati": "उपवास-व्रत का पालन करके उस पर पुनः विचार करता है",
    "uposathakammaṃ katvā taṃ garuṃ katvā paccavekkhati": "उपवास-व्रत का पालन करके उसे महत्व देकर पुनः विचार करता है",
    "uposathakammaṃ katvā taṃ assādeti abhinandati": "उपवास-व्रत का पालन करके उसका रस लेता है, उसमें आनंद लेता है",
    "jhānā vuṭṭhahitvā": "ध्यान से उठकर", "jhānā": "ध्यान से",
    "ariyā maggā vuṭṭhahitvā maggaṃ paccavekkhanti": "आर्य मार्ग से उठकर मार्ग पर पुनः विचार करते हैं",
    "ariyā maggā vuṭṭhahitvā maggaṃ garuṃ katvā": "आर्य मार्ग से उठकर मार्ग को महत्व देकर",
    "phalaṃ paccavekkhanti": "फल पर पुनः विचार करते हैं", "phalaṃ": "फल", "nibbānaṃ": "निर्वाण",
    "pahīne kilese": "छोड़े जा चुके मन के क्लेशों पर", "vikkhambhite kilese": "दबाए जा चुके मन के क्लेशों पर",
    "pubbe": "पहले", "cakkhuṃ": "आँख", "vatthuṃ": "आधार", "sotaṃ": "कान",
    "ariyā nahetū pahīne kilese paccavekkhanti": "आर्य मूल रूपी न होने वाले छोड़े जा चुके मन के क्लेशों पर पुनः विचार करते हैं",
    "ariyā ahetuke pahīne kilese paccavekkhanti": "आर्य मूल से रहित छोड़े जा चुके मन के क्लेशों पर पुनः विचार करते हैं",
    "vikkhambhite kilese paccavekkhanti": "दबाए जा चुके मन के क्लेशों पर पुनः विचार करते हैं",
    "pubbe samudāciṇṇe kilese jānanti": "पहले बार-बार उठे मन के क्लेशों को जानते हैं",
    "domanassaṃ uppajjati": "उदासी उत्पन्न होती है",
    "kusalākusale niruddhe sahetuko vipāko tadārammaṇatā uppajjati": "हितकर और हानिकर के समाप्त होने पर मूल वाला कर्म-फल उसी विषय को लेकर उत्पन्न होता है",
    "kusalākusale niruddhe ahetuko vipāko tadārammaṇatā uppajjati": "हितकर और हानिकर के समाप्त होने पर मूल से रहित कर्म-फल उसी विषय को लेकर उत्पन्न होता है",
    "ariyā nibbānaṃ paccavekkhanti": "आर्य निर्वाण पर पुनः विचार करते हैं",
    "ariyā nibbānaṃ garuṃ katvā paccavekkhanti": "आर्य निर्वाण को महत्व देकर पुनः विचार करते हैं",
    "taṃ garuṃ katvā paccavekkhati": "उसे महत्व देकर पुनः विचार करता है",
    "garuṃ katvā": "महत्व देकर",
    "dibbena cakkhunā rūpaṃ passati": "दिव्य आँख से दृश्य रूप को देखता है",
    "dibbāya sotadhātuyā saddaṃ suṇāti": "दिव्य कान के तत्व से ध्वनि को सुनता है",
    "taṃ garuṃ katvā rāgo uppajjati": "उसे महत्व देकर राग उत्पन्न होता है", "diṭṭhi uppajjati": "दृष्टि उत्पन्न होती है",
    "saddhaṃ upanissāya dānaṃ deti": "श्रद्धा के प्रबल आश्रय से दान देता है",
    "samāpattiṃ uppādeti": "ध्यान-अवस्था उत्पन्न करता है", "diṭṭhiṃ gaṇhāti": "दृष्टि ग्रहण करता है",
    "sīlaṃ": "सदाचार", "saddhaṃ": "श्रद्धा", "saddhā": "श्रद्धा", "saṅghaṃ bhindati": "संघ में फूट डालता है",
    "senāsanaṃ upanissāya dānaṃ deti": "निवास-स्थान के प्रबल आश्रय से दान देता है",
    "senāsanaṃ saddhāya": "निवास-स्थान श्रद्धा के लिए",
    "phalasamāpattiyā upanissayapaccayena paccayo": "फल की ध्यान-अवस्था के लिए प्रबल आश्रय-कारण के रूप में कारण होता है",
    "patthanāya maggassa phalasamāpattiyā upanissayapaccayena paccayo": "कामना, मार्ग और फल की ध्यान-अवस्था के लिए प्रबल आश्रय-कारण के रूप में कारण होता है",
    "kāyikaṃ sukhaṃ upanissāya dānaṃ deti": "शारीरिक सुख के प्रबल आश्रय से दान देता है",
    "kāyikaṃ dukkhaṃ": "शारीरिक दुःख", "kāyikaṃ sukhaṃ": "शारीरिक सुख", "utu": "तापमान", "utuṃ": "तापमान",
    "bhojanaṃ": "भोजन", "senāsanaṃ": "निवास-स्थान",
    "mohaṃ upanissāya dānaṃ deti": "मोह के प्रबल आश्रय से दान देता है",
    "moho ca saddhāya": "और मोह श्रद्धा के लिए", "paññāya rāgassa": "प्रज्ञा के लिए, राग के लिए",
    "nibbānaṃ āvajjanāya ārammaṇapaccayena paccayo": "निर्वाण मन को विषय की ओर मोड़ने के लिए विषय-कारण के रूप में कारण होता है",
    "nirodhā vuṭṭhahantassa nevasaññānāsaññāyatanaṃ phalasamāpattiyā anantarapaccayena paccayo":
        "समाप्ति की ध्यान-अवस्था से बाहर आने वाले व्यक्ति में न पहचान न अ-पहचान का क्षेत्र फल की ध्यान-अवस्था के लिए निकटता-कारण के रूप में कारण होता है",
    "anulomaṃ gotrabhussa": "अनुरूपता गोत्र-परिवर्तन के लिए", "anulomaṃ vodānassa": "अनुरूपता शुद्धि के लिए",
    "gotrabhu maggassa": "गोत्र-परिवर्तन मार्ग के लिए", "vodānaṃ maggassa": "शुद्धि मार्ग के लिए",
    "maggo phalassa": "मार्ग फल के लिए", "phalaṃ phalassa": "फल फल के लिए",
    "anulomaṃ phalasamāpattiyā": "अनुरूपता फल की ध्यान-अवस्था के लिए",
    "sahetuke khandhe garuṃ katvā assādeti abhinandati": "मूल वाले समूहों को महत्व देकर उनका रस लेता है, उनमें आनंद लेता है",
    "ahetuke khandhe garuṃ katvā assādeti abhinandati": "मूल से रहित समूहों को महत्व देकर उनका रस लेता है, उनमें आनंद लेता है",
}

# whole Pāli phrases replaced before splitting (lowercase)
PHRASE = {}
PHRASE_ORDER = []


def _ph(p, h):
    PHRASE[p] = h


def _nana_list(pali):
    return S.dat_list(pali)


PAT = "निर्भरता के खंड के समान"
NOTE = {
    "adhipatiyā nava pañhā pavatteyeva": "प्रधानता-कारण में नौ प्रश्न, केवल जीवन के दौरान",
    "anantarasadisaṃ": "निकटता-कारण के समान", "anantarasadisaṃ.": "निकटता-कारण के समान।",
    "anantarasadisaṃ. āvajjanampi bhavaṅgampi natthi, āsevanapaccaye vajjetabbā navapi ":
        "निकटता-कारण के समान। मन को विषय की ओर मोड़ना भी नहीं है, जीवन-धारा भी नहीं है; पुनरावृत्ति-कारण में नौ के नौ छोड़ देने चाहिए ",
    "anulomamātikā": "सकारात्मक क्रम की मूल सूची", "anulomamātikā gaṇetabbā": "सकारात्मक क्रम की मूल सूची गिननी चाहिए",
    "anulomamātikā kātabbā": "सकारात्मक क्रम की मूल सूची बनानी चाहिए",
    "anulomasahajātasadisā": "सकारात्मक क्रम के सह-उत्पत्ति-कारण के समान",
    "appaṭighamūlakaṃ itarepi dve pañhā kātabbā. ghaṭanepi tīṇi pañhā kātabbā. ajjhattikā bāhirā mahābhūtā sabbe jānitvā kātabbā.":
        "टकराव से रहित परिघटना से शुरू होने वाली शृंखला के बाकी दो प्रश्न भी बनाने चाहिए। संयोजन में भी तीन प्रश्न बनाने चाहिए। आंतरिक और बाह्य सभी महाभूतों को जानकर बनाना चाहिए।",
    "avasesā dvepi pañhā kātabbā, paṭisandhi kabaḷīkāro āhāro dvīsupi kātabbo agge":
        "शेष दोनों प्रश्न भी बनाने चाहिए, पुनर्जन्म और कौर-कौर खाया जाने वाला भोजन दोनों में सबसे पहले रखना चाहिए",
    "avasesā dvepi ārammaṇādhipati sahajātādhipatipi upādānadukasadisā":
        "शेष दोनों, विषय रूपी प्रधानता और सह-उत्पत्ति रूपी प्रधानता भी, आसक्ति वाले दो के वर्गीकरण के समान हैं",
    "avasesā pañca pañhā paṭiccavārasadisā.": "शेष पाँच प्रश्न निर्भरता के खंड के समान हैं।",
    "cakkaṃ": "चक्र", "cakkaṃ kātabbaṃ": "चक्र बनाना चाहिए",
    "cakkaṃ. evaṃ navapi pañhā kātabbā": "चक्र। इसी तरह नौ के नौ प्रश्न बनाने चाहिए",
    "cattāripi kātabbāni": "चारों बनाने चाहिए", "cha pañhā": "छह प्रश्न",
    "dutiyaupanissayasadisaṃ": "दूसरे प्रबल आश्रय-कारण के समान",
    "dve mūlāni pucchitabbāni": "दोनों मूल वाक्य पूछने चाहिए",
    "dve pañhā upanissayamūlaṃ": "प्रबल आश्रय-कारण से शुरू होने वाली शृंखला में दो प्रश्न",
    "dvinnampi mūlā kātabbā": "दोनों के मूल वाक्य बनाने चाहिए",
    "dvīsupi paṭisandhi natthi": "दोनों में पुनर्जन्म नहीं है",
    "ekoyeva kabaḷīkāro āhāro": "केवल एक, कौर-कौर खाया जाने वाला भोजन",
    "evaṃ anumajjantena gaṇetabbaṃ": "इसी तरह क्रम से अनुसरण करते हुए गिनना चाहिए",
    "evaṃ avasesā pañhā, pavattipaṭisandhi vibhajitabbā": "इसी तरह शेष प्रश्नों में जीवन-काल और पुनर्जन्म का विश्लेषण करना चाहिए",
    "evaṃ avasesāpi dve gaṇanā gaṇetabbā.": "इसी तरह शेष दो गणनाएँ भी गिननी चाहिए।",
    "evaṃ cattāripi gaṇanā paripuṇṇā": "इसी तरह चारों गणनाएँ परिपूर्ण हैं",
    "evaṃ gaṇetabbaṃ": "इसी तरह गिनना चाहिए",
    "evaṃ indriyapaccayā vitthāretabbā. nava": "इसी तरह क्षमता-कारण का विस्तार करना चाहिए। नौ",
    "evaṃ itare dve gaṇanāpi nissayavāropi kātabbo.": "इसी तरह बाकी दो गणनाएँ भी और आश्रय का खंड भी बनाना चाहिए।",
    "evaṃ itare dve gaṇanāpi sampayuttavāropi kātabbo.": "इसी तरह बाकी दो गणनाएँ भी और जुड़ाव का खंड भी बनाना चाहिए।",
    "evaṃ navapi kātabbā, ekekassa mūle tīṇi tīṇi pañhā": "इसी तरह नौ के नौ बनाने चाहिए, हर एक मूल वाक्य में तीन-तीन प्रश्न",
    "evaṃ navapi pañhā kātabbā, āvajjanāpi vuṭṭhānampi natthi":
        "इसी तरह नौ के नौ प्रश्न बनाने चाहिए, मन को विषय की ओर मोड़ना भी नहीं है, बाहर आना भी नहीं है",
    "evaṃ paccanīyagaṇanāpi kātabbā": "इसी तरह नकारात्मक क्रम की गणना भी करनी चाहिए",
    "evaṃ paccanīyādīni gaṇanāpi sampayuttavārepi sabbe kātabbā. ekoyeva pañho":
        "इसी तरह नकारात्मक क्रम आदि की गणनाएँ भी और जुड़ाव के खंड में भी सब बनाने चाहिए। केवल एक ही प्रश्न",
    "evaṃ paccayavāropi nissayavāropi saṃsaṭṭhavāropi sampayuttavāropi vitthāretabbo, sabbattha ekāyeva pañhā.":
        "इसी तरह कारण के खंड का, आश्रय के खंड का, घुले-मिले होने के खंड का और जुड़ाव के खंड का भी विस्तार करना चाहिए, हर जगह केवल एक ही प्रश्न।",
    "evaṃ sabbaṃ sappaccayagaṇanāhi saddhiṃ kātabbaṃ": "इसी तरह सब कुछ कारणों पर निर्भर रहने वाली परिघटनाओं की गणनाओं के साथ करना चाहिए",
    "evaṃ sabbe kātabbā.": "इसी तरह सब बनाने चाहिए।",
    "ghaṭanā adhipati tīṇi, upādānadukasadisā. sabbe paccayā upādānadukasadisā. upādāniye lokuttaraṃ natthi, paccanīyampi itare dve gaṇanāpi upādānadukasadisaṃ.":
        "संयोजन में प्रधानता-कारण में तीन, आसक्ति वाले दो के वर्गीकरण के समान। सभी कारण आसक्ति वाले दो के वर्गीकरण के समान हैं। आसक्ति का विषय बनने वाली परिघटना में लोकोत्तर नहीं है; नकारात्मक क्रम भी और बाकी दो गणनाएँ भी आसक्ति वाले दो के वर्गीकरण के समान हैं।",
    "ghaṭanā tīṇi, pavattipaṭisandhi paripuṇṇaṃ. saṃkhittaṃ": "संयोजन में तीन, जीवन-काल और पुनर्जन्म परिपूर्ण। संक्षिप्त",
    "hetumūlake tīṇi": "मूल-कारण से शुरू होने वाली शृंखला में तीन",
    "heṭṭhā adhipati tīṇi, upādānadukasadisā": "नीचे प्रधानता-कारण में तीन, आसक्ति वाले दो के वर्गीकरण के समान",
    "iha ghaṭanā natthi, satta pañhā": "यहाँ संयोजन नहीं है, सात प्रश्न",
    "imaṃ dukaṃ cūḷantaraduke lokiyadukasadisaṃ, ninnānākaraṇaṃ.":
        "यह दो का वर्गीकरण बीच के छोटे दो-दो के वर्गीकरणों में लौकिक परिघटनाओं वाले दो के वर्गीकरण के समान है, बिना किसी अंतर के।",
    "imaṃ dukaṃ yathā sappaccayadukaṃ, evaṃ gaṇetabbaṃ, ninnānākaraṇaṃ.":
        "इस दो के वर्गीकरण को कारणों पर निर्भर रहने वाली परिघटनाओं वाले दो के वर्गीकरण की तरह गिनना चाहिए, बिना किसी अंतर के।",
    "imaṃ nānaṃ": "यह अंतर है",
    "ime ajjhattikabāhirā mahābhūtā kātabbā": "ये आंतरिक और बाह्य महाभूत बनाने चाहिए",
    "ime dvepi paṭiccasadisā. nissayapaccayo paccayavāre nissayapaccayasadiso.":
        "ये दोनों निर्भरता के खंड के समान हैं। आश्रय-कारण कारण के खंड के आश्रय-कारण के समान है।",
    "ime pañca pañhā hetusadisā, ninnānaṃ": "ये पाँच प्रश्न मूल-कारण के समान हैं, बिना किसी अंतर के",
    "imesaṃ dvinnampi pañhānaṃ mūlāni pucchitabbāni": "इन दोनों प्रश्नों के मूल वाक्य पूछने चाहिए",
    "imesu catūsupi yathā kammapaccaye diṭṭhigatavippayutto lobho dassito evaṃ dassetabbo. cattāri cattāri pañhā":
        "इन चारों में भी, जैसे कर्म-कारण में ग़लत दृष्टि से अलग लोभ दिखाया गया है, वैसे ही दिखाना चाहिए। चार-चार प्रश्न",
    "imesu dvīsu nava.": "इन दोनों में नौ।",
    "imesu sahajātaṃ sahajātasadisaṃ, purejātaṃ purejātasadisaṃ":
        "इनमें सह-उत्पत्ति सह-उत्पत्ति-कारण के समान है, पूर्व-उत्पत्ति पूर्व-उत्पत्ति-कारण के समान है",
    "iminā kāraṇena nava pañhā kātabbā": "इसी तरीके से नौ प्रश्न बनाने चाहिए",
    "iminā kāraṇena vitthāretabbaṃ yathā sahetukadukaṃ ninnānākaraṇaṃ.":
        "इसी तरीके से विस्तार करना चाहिए, जैसे मूल वाली परिघटनाओं वाला दो का वर्गीकरण, बिना किसी अंतर के।",
    "indriyanti niyāmetabbaṃ, navapi paripuṇṇaṃ": "“क्षमता” निश्चित करना चाहिए, नौ के नौ परिपूर्ण",
    "itare dve gaṇanāpi kātabbā. sahajātavāro paṭiccavārasadiso.":
        "बाकी दो गणनाएँ भी करनी चाहिए। सह-उत्पत्ति का खंड निर्भरता के खंड के समान है।",
    "itarepi dve kātabbā. saṃkhittaṃ": "बाकी दो भी बनाने चाहिए। संक्षिप्त",
    "itarepi dve pañhā kātabbā": "बाकी दो प्रश्न भी बनाने चाहिए",
    "jhānampi maggampi sahajātapaccayasadisā, bāhirā mahābhūtā natthi ":
        "ध्यान-कारण भी और मार्ग-कारण भी सह-उत्पत्ति-कारण के समान हैं, बाह्य महाभूत नहीं हैं ",
    "lokuttare arūpe vipākanti niyāmetabbaṃ": "लोकोत्तर में और अभौतिक लोक में “कर्म-फल” निश्चित करना चाहिए",
    "mūlaṃ kātabbaṃ": "मूल वाक्य बनाना चाहिए", "mūlaṃ pucchitabbaṃ": "मूल वाक्य पूछना चाहिए",
    "naanantarapadādī paccanīyasadisā": "निकटता-कारण के अभाव वाले पद आदि नकारात्मक क्रम के समान हैं",
    "nasamanantarapadādī paccanīyasadisā": "पूर्ण निकटता-कारण के अभाव वाले पद आदि नकारात्मक क्रम के समान हैं",
    "nahetumūlakaṃ tīṇipi ekasadisaṃ": "मूल रूपी न होने वाली परिघटना से शुरू होने वाली शृंखला के तीनों एक समान हैं",
    "nahetupaccayā nava pañhā, ahetukanti niyāmetabbaṃ": "मूल-कारण के बिना नौ प्रश्न, “मूल से रहित” निश्चित करना चाहिए",
    "napurejātasadisaṃ, arūpapañhāyeva": "पूर्व-उत्पत्ति-कारण के अभाव के समान, केवल अभौतिक लोक के प्रश्न",
    "navapi pañhā kātabbā, rūpaṃ chaḍḍetabbaṃ": "नौ के नौ प्रश्न बनाने चाहिए, भौतिक रूप छोड़ देना चाहिए",
    "naāsevanamūlake lokuttare suddhake vipākoti niyāmetabbaṃ, avasesā pakatikāyeva":
        "पुनरावृत्ति-कारण के अभाव से शुरू होने वाली शृंखला में, लोकोत्तर के शुद्ध पद में “कर्म-फल” निश्चित करना चाहिए, शेष स्वाभाविक रूप में ही",
    "nissayavāro paccayavārasadiso": "आश्रय का खंड कारण के खंड के समान है",
    "nissayavāro paccayavārasadiso.": "आश्रय का खंड कारण के खंड के समान है।",
    "nissayavāropi evaṃ kātabbo.": "आश्रय का खंड भी इसी तरह बनाना चाहिए।",
    "nissayavāropi paccayavārasadiso": "आश्रय का खंड भी कारण के खंड के समान है",
    "nissayavāropi paccayavārasadiso.": "आश्रय का खंड भी कारण के खंड के समान है।",
    "paccayasadisaṃ": "कारण के खंड के समान", "paccayavārasadisaṃ": "कारण के खंड के समान",
    "paripuṇṇaṃ": "परिपूर्ण", "paripuṇṇaṃ nava": "परिपूर्ण, नौ",
    "pavattipaṭisandhi kātabbā": "जीवन-काल और पुनर्जन्म बनाने चाहिए",
    "pavattipaṭisandhi satta pañhā, iha ghaṭanā natthi": "जीवन-काल और पुनर्जन्म में सात प्रश्न, यहाँ संयोजन नहीं है",
    "pañca pañhā, ghaṭanā natthi": "पाँच प्रश्न, संयोजन नहीं है",
    "paṭhamagamanaṃyeva": "केवल पहला प्रसंग",
    "paṭhamagamanaṃyeva, āvajjanā natthi. rūpāyatanaṃ cakkhuviññāṇassa…pe… phoṭṭhabbāyatanaṃ kāyaviññāṇassāti idaṃ natthi":
        "केवल पहला प्रसंग, मन को विषय की ओर मोड़ना नहीं है। “दृश्य रूप का इंद्रिय-क्षेत्र आँख की चेतना के लिए… स्पर्श का इंद्रिय-क्षेत्र शरीर की चेतना के लिए”, यह नहीं है",
    "paṭiccasadisaṃ": PAT, "paṭiccasadisaṃ yāva asaññasattā": PAT + ", पहचान-रहित प्राणियों तक",
    "paṭiccasadisaṃ, arūpaṃyeva kātabbaṃ": PAT + ", केवल अभौतिक बनाना चाहिए",
    "paṭiccasadisā": PAT, "paṭiccasadisā paṭhamapañhā": "पहला प्रश्न " + PAT,
    "paṭiccavārasadisaṃ": PAT, "paṭiccavārasadisaṃ. vipākavibhaṅge nava pañhā": PAT + "। कर्म-फल-कारण के विश्लेषण में नौ प्रश्न",
    "paṭiccavārasadisaṃyeva": "निर्भरता के खंड के समान ही", "paṭiccavārasadisā": PAT,
    "paṭiccavāre nissayapaccayasadisaṃ, iha ghaṭanā natthi": "निर्भरता के खंड के आश्रय-कारण के समान, यहाँ संयोजन नहीं है",
    "paṭiccavāre sahajātasadisaṃ, iha ghaṭanā natthi": "निर्भरता के खंड के सह-उत्पत्ति-कारण के समान, यहाँ संयोजन नहीं है",
    "paṭiccavāre sampayuttasadisā cha pañhā": "निर्भरता के खंड के जुड़ाव-कारण के समान छह प्रश्न",
    "paṭisandhi kātabbā": "पुनर्जन्म बनाना चाहिए", "paṭisandhi natthi": "पुनर्जन्म नहीं है",
    "paṭisandhi natthi, paripuṇṇaṃ": "पुनर्जन्म नहीं है, परिपूर्ण",
    "paṭisandhi vajjetabbā, kaṭattārūpā ca": "पुनर्जन्म छोड़ देना चाहिए, और किए गए कर्म से उत्पन्न भौतिक रूप भी",
    "purejātasadisaṃ": "पूर्व-उत्पत्ति-कारण के समान",
    "rūpajīvitindriyaṃ ekaṃyeva": "केवल एक, भौतिक जीवन-क्षमता",
    "rūpaṃ chaḍḍetvā arūpeyeva nava pañhā": "भौतिक रूप को छोड़कर केवल अभौतिक में नौ प्रश्न",
    "sabbaṃ cakkaṃ kātabbaṃ": "पूरा चक्र बनाना चाहिए", "sabbaṃ paripuṇṇaṃ": "सब परिपूर्ण",
    "sabbaṃ saṃkhittaṃ": "सब संक्षिप्त",
    "sabbaṃ yāva asaññasattā tāva kātabbaṃ.": "पहचान-रहित प्राणियों तक सब करना चाहिए।",
    "sabbe cakkā kātabbā": "सभी चक्र बनाने चाहिए", "sabbe kātabbā": "सब बनाने चाहिए",
    "sabbe mahābhūtā kātabbā": "सभी महाभूत बनाने चाहिए",
    "sabbe mahābhūtā yāva asaññasattā": "सभी महाभूत, पहचान-रहित प्राणियों तक",
    "sahajātapaccaye satta, iha ghaṭanā natthi. aññamaññapaccaye cha, nissayapaccaye satta pañhā, iha ghaṭanā natthi":
        "सह-उत्पत्ति-कारण में सात, यहाँ संयोजन नहीं है। परस्पर-कारण में छह, आश्रय-कारण में सात प्रश्न, यहाँ संयोजन नहीं है",
    "sahajātasadisaṃ": "सह-उत्पत्ति-कारण के समान",
    "sahajātavārepi evaṃ gaṇetabbaṃ.": "सह-उत्पत्ति के खंड में भी इसी तरह गिनना चाहिए।",
    "sahajātavāro paṭiccavārasadiso": "सह-उत्पत्ति का खंड निर्भरता के खंड के समान है",
    "sahajātavāro paṭiccavārasadiso.": "सह-उत्पत्ति का खंड निर्भरता के खंड के समान है।",
    "sahajātavāro paṭiccavārasadiso vibhajantena diṭṭhupādānaṃ \"sahajātaṃ kāmupādāna\"nti kātabbaṃ.":
        "सह-उत्पत्ति का खंड निर्भरता के खंड के समान है; विश्लेषण करते हुए दृष्टियों के प्रति आसक्ति को “सह-उत्पत्ति, इंद्रिय-सुखों के प्रति आसक्ति” इस रूप में करना चाहिए।",
    "sahajātavāropi paccayavāropi nissayavāropi paṭiccavārasadisāyeva pañhā. mahābhūtesu niṭṭhitesu \"vatthuṃ paccayā\"ti kātabbā. pañcāyatanāni anulomepi paccanīyepi yathā labbhanti tathā kātabbā. saṃsaṭṭhavāropi sampayuttavāropi paripuṇṇo. rūpaṃ natthi, arūpameva.":
        "सह-उत्पत्ति का खंड भी, कारण का खंड भी और आश्रय का खंड भी, इनके प्रश्न निर्भरता के खंड के समान ही हैं। महाभूतों के पूरे हो जाने पर “आधार के कारण” इस रूप में करना चाहिए। पाँच इंद्रिय-क्षेत्र सकारात्मक क्रम में भी और नकारात्मक क्रम में भी जैसे लागू होते हैं, वैसे ही करने चाहिए। घुले-मिले होने का खंड भी और जुड़ाव का खंड भी परिपूर्ण है। भौतिक रूप नहीं है, केवल अभौतिक।",
    "sahajātavāropi paccayavāropi nissayavāropi saṃsaṭṭhavāropi sampayuttavāropi evaṃ vitthāretabbā. paccayavāre vatthu ca pañcāyatanāni ca dassetabbāni. yathā yathā labbhati taṃ taṃ kātabbaṃ":
        "सह-उत्पत्ति के खंड का, कारण के खंड का, आश्रय के खंड का, घुले-मिले होने के खंड का और जुड़ाव के खंड का भी इसी तरह विस्तार करना चाहिए। कारण के खंड में आधार और पाँच इंद्रिय-क्षेत्र दिखाने चाहिए। जैसे-जैसे लागू हो, वैसे-वैसे करना चाहिए",
    "sahajātavāropi paccayavāropi nissayavāropi saṃsaṭṭhavāropi sampayuttavāropi paṭiccavārasadisā.":
        "सह-उत्पत्ति का खंड, कारण का खंड, आश्रय का खंड, घुले-मिले होने का खंड और जुड़ाव का खंड भी निर्भरता के खंड के समान हैं।",
    "sahajātavāropi paṭiccavārasadiso": "सह-उत्पत्ति का खंड भी निर्भरता के खंड के समान है",
    "sahajātavāropi paṭiccavārasadiso.": "सह-उत्पत्ति का खंड भी निर्भरता के खंड के समान है।",
    "sahetukamūlakaṃ paṭiccavārasadisaṃ": "मूल वाली परिघटना से शुरू होने वाली शृंखला निर्भरता के खंड के समान है",
    "sahetuko ceva na ca hetumūlakaṃ tīṇipi ekasadisā.":
        "मूल वाली, पर स्वयं मूल रूपी न होने वाली परिघटना से शुरू होने वाली शृंखला के तीनों एक समान हैं।",
    "sahetuko ceva na ca hetumūlake iminākārena vitthāretabbā avasesā dve pañhā.":
        "मूल वाली, पर स्वयं मूल रूपी न होने वाली परिघटना से शुरू होने वाली शृंखला में शेष दो प्रश्नों का इसी तरीके से विस्तार करना चाहिए।",
    "sampayuttavāro saṃsaṭṭhavārasadiso": "जुड़ाव का खंड घुले-मिले होने के खंड के समान है",
    "sampayuttavāro saṃsaṭṭhavārasadiso.": "जुड़ाव का खंड घुले-मिले होने के खंड के समान है।",
    "sampayuttavāropi saṃsaṭṭhavārasadiso": "जुड़ाव का खंड भी घुले-मिले होने के खंड के समान है",
    "saṃkhittaṃ": "संक्षिप्त", "saṃkhittaṃ.": "संक्षिप्त।",
    "saṃkhittaṃ, itare dve upādānadukasadisā": "संक्षिप्त, बाकी दो आसक्ति वाले दो के वर्गीकरण के समान हैं",
    "saṃkhittaṃ, navapi pañhā arūpe dve upādānā": "संक्षिप्त, नौ के नौ प्रश्न, अभौतिक लोक में दो आसक्तियाँ",
    "saṃkhittaṃ, paṭiccasadisaṃ": "संक्षिप्त, " + PAT,
    "saṃkhittaṃ, sabbe kātabbā": "संक्षिप्त, सब बनाने चाहिए", "saṃkhittaṃ, sabbe kātabbā.": "संक्षिप्त, सब बनाने चाहिए।",
    "saṃkhittaṃ, sahajātasadisaṃ sahajātaṃ vibhajitabbaṃ, purejātasadisaṃ purejātaṃ":
        "संक्षिप्त, सह-उत्पत्ति का सह-उत्पत्ति-कारण के समान विश्लेषण करना चाहिए, पूर्व-उत्पत्ति का पूर्व-उत्पत्ति-कारण के समान",
    "saṃkhittaṃ, vitthāretabbaṃ": "संक्षिप्त, विस्तार करना चाहिए",
    "saṃkhittaṃ, yāva asaññasattā": "संक्षिप्त, पहचान-रहित प्राणियों तक",
    "saṃkhittaṃ. evaṃ vibhajitabbaṃ": "संक्षिप्त। इसी तरह विश्लेषण करना चाहिए",
    "saṃkhittaṃ. evaṃ vitthāretabbaṃ.": "संक्षिप्त। इसी तरह विस्तार करना चाहिए।",
    "saṃkhittaṃ. sabbattha nava": "संक्षिप्त। हर जगह नौ",
    "saṃkhittaṃ. sabbattha nava, evaṃ gaṇetabbaṃ": "संक्षिप्त। हर जगह नौ, इसी तरह गिनना चाहिए",
    "saṃkhittaṃ. sabbattha satta": "संक्षिप्त। हर जगह सात", "saṃkhittaṃ. sabbattha tīṇi": "संक्षिप्त। हर जगह तीन",
    "saṃkhittaṃ. yāva asaññasattā": "संक्षिप्त। पहचान-रहित प्राणियों तक",
    "saṃkhittaṃ. yāva vatthu nahetū ca khandhā tāva kātabbaṃ":
        "संक्षिप्त। आधार और मूल रूपी न होने वाले समूहों तक करना चाहिए",
    "saṃkhittaṃ. āmasanaṃ nānākaraṇaṃ upādānadukasadisaṃ nava pañhā. rūpaṃ natthi. evaṃ sabbepi vārā vitthāretabbā. arūpaṃyeva.":
        "संक्षिप्त। उल्लेख में अंतर है, आसक्ति वाले दो के वर्गीकरण के समान नौ प्रश्न। भौतिक रूप नहीं है। इसी तरह सभी खंडों का विस्तार करना चाहिए। केवल अभौतिक।",
    "saṃkhittaṃ. ārammaṇapaccayamhi pañca viññāṇā kātabbā.": "संक्षिप्त। विषय-कारण में पाँच प्रकार की चेतना बनानी चाहिए।",
    "saṃsaṭṭhavārepi sabbattha ekaṃ, saṃkhittaṃ. avigatapaccayā, ekāyeva pañhā. dvepi vārā kātabbā.":
        "घुले-मिले होने के खंड में भी हर जगह एक, संक्षिप्त। अविलीनता-कारण से, केवल एक ही प्रश्न। दोनों खंड बनाने चाहिए।",
    "saṃsaṭṭhavāro evaṃ vitthāretabbo, saha gaṇanāhi dve pañhā":
        "घुले-मिले होने के खंड का इसी तरह विस्तार करना चाहिए, गणनाओं के साथ दो प्रश्न",
    "tattha tattha ṭhitena imaṃ kātabbaṃ dutiyagamanasadisaṃ":
        "जहाँ-जहाँ टिके हों, वहाँ-वहाँ इसे दूसरे प्रसंग के समान करना चाहिए",
    "tīsupi jīvitindriyaṃ agge kātabbaṃ": "तीनों में जीवन-क्षमता सबसे पहले रखनी चाहिए",
    "tīsupi kabaḷīkāro āhāro kātabbo": "तीनों में कौर-कौर खाया जाने वाला भोजन बनाना चाहिए",
    "tīsupi rūpajīvitindriyaṃ": "तीनों में भौतिक जीवन-क्षमता",
    "tīṇi ghaṭanupanissayepi tīṇi": "तीन, संयोजन वाले प्रबल आश्रय-कारण में भी तीन",
    "tīṇi upanissayā": "तीनों प्रबल आश्रय",
    "tīṇipi kātabbā, ghaṭane tīṇipi kātabbā": "तीनों बनाने चाहिए, संयोजन में भी तीनों बनाने चाहिए",
    "tīṇipi paccayā paṭiccavāre hetusadisā": "तीनों कारण निर्भरता के खंड के मूल-कारण के समान हैं",
    "tīṇipi, tīsupi dvepi adhipati kātabbā, ghaṭanādhipatipi tīṇi":
        "तीनों, तीनों में दोनों प्रधानताएँ बनानी चाहिए, संयोजन वाली प्रधानता में भी तीन",
    "upādānadukasadisā ninnānā, nava pañhā": "आसक्ति वाले दो के वर्गीकरण के समान, बिना किसी अंतर के, नौ प्रश्न",
    "vitthāretabbaṃ": "विस्तार करना चाहिए",
    "vitthāretabbaṃ yāva. nahetū khandhā": "विस्तार करना चाहिए, तक। मूल रूपी न होने वाले समूह",
    "yathā hetupaccayā evaṃ vitthāretabbaṃ, navapi vipākanti niyāmetabbaṃ":
        "जैसे मूल-कारण से, वैसे ही विस्तार करना चाहिए, नौ के नौ में “कर्म-फल” निश्चित करना चाहिए",
    "yathā hetusahetukadukaṃ evaṃ vitthāretabbaṃ, ninnānākaraṇaṃ":
        "जैसे मूल रूपी भी और मूल वाली भी परिघटनाओं वाला दो का वर्गीकरण, वैसे ही विस्तार करना चाहिए, बिना किसी अंतर के",
    "yathā lokiyadukaṃ, evaṃ kātabbaṃ. ninnānākaraṇaṃ": "जैसे लौकिक परिघटनाओं वाला दो का वर्गीकरण, वैसे ही करना चाहिए। बिना किसी अंतर के",
    "yathā paṭhamagamanaṃ evaṃ ninnānaṃ": "जैसे पहला प्रसंग, वैसे ही, बिना किसी अंतर के",
    "yathā paṭiccavārasadisaṃ": "जैसे निर्भरता के खंड में",
    "yathā upādānadukaṃ evaṃ paṭiccavāropi sahajātavāropi paccayavāropi nissayavāropi saṃsaṭṭhavāropi sampayuttavāropi kātabbā, ninnānākaraṇā, āmasanaṃ nānākaraṇaṃ.":
        "जैसे आसक्ति वाला दो का वर्गीकरण, वैसे ही निर्भरता का खंड, सह-उत्पत्ति का खंड, कारण का खंड, आश्रय का खंड, घुले-मिले होने का खंड और जुड़ाव का खंड भी बनाने चाहिए, बिना किसी अंतर के; केवल उल्लेख में अंतर है।",
    "yāva ajjhattikā mahābhūtā": "आंतरिक महाभूतों तक",
    "yāva asaññasattā": "पहचान-रहित प्राणियों तक", "yāva asaññasattā ": "पहचान-रहित प्राणियों तक ",
    "yāva asaññasattā kātabbaṃ": "पहचान-रहित प्राणियों तक करना चाहिए",
    "yāva asaññasattā moho natthi": "पहचान-रहित प्राणियों तक, मोह नहीं है",
    "yāva asaññasattā tāva vitthāro": "पहचान-रहित प्राणियों तक विस्तार",
    "yāva kāyaviññāṇaṃ": "शरीर की चेतना तक",
    "yāva vatthu nahetū khandhā, ca tāva kātabbaṃ": "आधार और मूल रूपी न होने वाले समूहों तक करना चाहिए",
    "ārabbha kātabbā": "विषय बनाकर करना चाहिए",
    "ārabbha kātabbā, ārammaṇādhipatiyeva": "विषय बनाकर करना चाहिए, केवल विषय रूपी प्रधानता",
    "ārammaṇe noupādānamūlake pañcāyatanañca vatthuñca kātabbā":
        "विषय-कारण में, आसक्ति रूपी न होने वाली परिघटना से शुरू होने वाली शृंखला में पाँच इंद्रिय-क्षेत्र और आधार बनाने चाहिए",
    "ārammaṇādhipatiyeva": "केवल विषय रूपी प्रधानता",
}
for _w, _h in [("cattāri", "चार"), ("cha", "छह"), ("dve", "दो"), ("ekaṃ", "एक"), ("nava", "नौ"), ("pañca", "पाँच"),
               ("satta", "सात"), ("tīṇi", "तीन")]:
    NOTE[f"sabbattha {_w}"] = f"हर जगह {_h}"
NOTE["sabbattha ekāyeva pañhā"] = "हर जगह केवल एक ही प्रश्न"
LINE = {}
SLIPS = {}
VARIANTS = {
    "{ākāsānañcāyatanakiriyaṃ (syā.) evamuparipi tīsu ṭhānesu}":
        ("[पाठभेद (Syā.): ākāsānañcāyatanakiriyaṃ evamuparipi tīsu ṭhānesu]", "अनंत आकाश का क्षेत्र"),
}

# knowledges and other datives that come in comma lists
for w, h in S.NANA.items():
    U(w, h, "D")
DLIST = list(S.NANA) + ["dukkhassa", "kāyikassa", "mohassa"]
DLIST_ALT = "|".join(sorted(DLIST, key=len, reverse=True))
U("ākāsānañcāyatanaṃ", "अनंत आकाश का क्षेत्र", "N", "ms"); U("ākiñcaññāyatanaṃ", "कुछ भी न होने का क्षेत्र", "N", "ms")
U("viññāṇañcāyatanassa", "अनंत चेतना के क्षेत्र", "D"); U("nevasaññānāsaññāyatanassa", "न पहचान न अ-पहचान के क्षेत्र", "D")
U("hetuṃ dhammaṃ", "मूल रूपी परिघटना", "A")
U("ahetukaṃ nahetuṃ ekaṃ khandhaṃ", "मूल से रहित, मूल रूपी न होने वाले एक समूह", "A")
U("hetuñca nahetuñca khandhe", "मूल और मूल रूपी न होने वाले समूहों", "A")
U("nahetuṃ ekaṃ khandhañca hetuñca", "मूल रूपी न होने वाले एक समूह और मूल", "A")

# strong-support narrative (pakatūpanissaya)
for p, h, g in [("saddh", "श्रद्धा", "f"), ("paññ", "प्रज्ञा", "f"), ("patthan", "कामना", "f")]:
    U(f"{p}aṃ", h, "A"); U(f"{p}ā|{p}ā ca", h, "N", g + "s"); U(f"{p}āya", h, "D")
for p, h in [("rāg", "राग"), ("mān", "अहंकार")]:
    U(f"{p}aṃ", h, "A"); U(f"{p}o|{p}o ca", h, "N", "ms"); U(f"{p}assa", h, "D")
U("sīlaṃ", "सदाचार", "A"); U("sīlassa", "सदाचार", "D"); U("diṭṭhiṃ", "दृष्टि", "A"); U("diṭṭhi", "दृष्टि", "N", "fs")
U("diṭṭhiyā", "दृष्टि", "D"); U("utuṃ", "तापमान", "A"); U("mohaṃ", "मोह", "A")
U("kabaḷīkāraṃ āhāraṃ", "कौर-कौर खाए जाने वाले भोजन", "A")
U("jhānaṃ", "ध्यान", "A"); U("maggaṃ", "मार्ग", "A"); U("gotrabhuṃ", "गोत्र-परिवर्तन", "A"); U("phalaṃ", "फल", "AN", "ms")
U("dānaṃ", "दान", "AN", "ms")
CLAUSE.update({
    "dānaṃ": "दान", "jhānaṃ": "ध्यान", "uposathakammaṃ": "उपवास-व्रत", "pubbe suciṇṇāni": "पहले भली-भाँति किए गए कार्य",
    "pubbe samudāciṇṇe": "पहले बार-बार उठे", "ekaṃ": "एक", "cha": "छह", "dve": "दो", "pañca": "पाँच", "satta": "सात",
    "cattāri": "चार", "vicikicchā": "संशय", "uddhaccaṃ": "बेचैनी",
    "dānaṃ deti": "दान देता है", "mānaṃ jappeti": "अहंकार पालता है", "diṭṭhiṃ gaṇhāti": "दृष्टि ग्रहण करता है",
    "pāṇaṃ hanati": "जीव की हत्या करता है", "adinnaṃ ādiyati": "बिना दिया हुआ लेता है", "adinnaṃ": "बिना दिया हुआ",
    "musā": "झूठ", "pisuṇaṃ": "चुगली", "samphaṃ": "व्यर्थ", "sandhiṃ": "सेंध", "nillopaṃ": "डाका",
    "ekāgārikaṃ": "एक ही घर में डाका", "paripanthe": "राह में घात", "paradāraṃ": "पराई स्त्री",
    "gāmaghātaṃ": "गाँव पर हमला", "nigamaghātaṃ karoti": "कस्बे पर हमला करता है",
    "patthanā": "कामना", "patthanāya": "कामना के लिए", "paññaṃ": "प्रज्ञा", "mānaṃ": "अहंकार", "mānassa": "अहंकार के लिए",
    "sīlaṃ samādiyati": "सदाचार ग्रहण करता है", "uposathakammaṃ karoti": "उपवास-व्रत का पालन करता है",
    "jhānaṃ uppādeti": "ध्यान उत्पन्न करता है", "vipassanaṃ uppādeti": "अंतर्दृष्टि उत्पन्न करता है",
    "maggaṃ uppādeti": "मार्ग उत्पन्न करता है", "abhiññaṃ uppādeti": "उच्च ज्ञान उत्पन्न करता है",
    "saṅghaṃ bhindati": "संघ में फूट डालता है",
    "ariyā gotrabhuṃ paccavekkhanti": "आर्य गोत्र-परिवर्तन पर पुनः विचार करते हैं",
    "ariyā pahīne kilese paccavekkhanti": "आर्य छोड़े जा चुके मन के क्लेशों पर पुनः विचार करते हैं",
    "kusalākusale niruddhe nahetu ahetuko vipāko tadārammaṇatā uppajjati":
        "हितकर और हानिकर के समाप्त होने पर मूल रूपी न होने वाला और मूल से रहित कर्म-फल उसी विषय को लेकर उत्पन्न होता है",
    "kusalākusale niruddhe nahetu sahetuko vipāko tadārammaṇatā uppajjati":
        "हितकर और हानिकर के समाप्त होने पर मूल रूपी न होने वाला, पर मूल वाला कर्म-फल उसी विषय को लेकर उत्पन्न होता है",
    "bāhiraṃ": "बाह्य", "bāhire": "बाह्य", "bāhirā": "बाह्य", "āhārasamuṭṭhāne": "आहार से उत्पन्न",
    "āhārasamuṭṭhānā": "आहार से उत्पन्न", "utusamuṭṭhāne": "तापमान से उत्पन्न", "utusamuṭṭhānā": "तापमान से उत्पन्न",
    "kāyaviññāṇasahagataṃ": "शरीर की चेतना के साथ होने वाले",
    "nirodhā vuṭṭhahantassa": "समाप्ति की ध्यान-अवस्था से बाहर आने वाले व्यक्ति में",
    "paṭisandhikkhaṇe sahetuko": "पुनर्जन्म के क्षण में मूल वाला",
    "dānaṃ datvā sīlaṃ samādiyitvā uposathakammaṃ katvā taṃ garuṃ katvā paccavekkhati":
        S.GIFT + " उसे महत्व देकर पुनः विचार करता है",
    "ariyā maggā vuṭṭhahitvā maggaṃ garuṃ katvā paccavekkhanti": "आर्य मार्ग से उठकर मार्ग को महत्व देकर पुनः विचार करते हैं",
    "ariyā phalaṃ garuṃ katvā paccavekkhanti": "आर्य फल को महत्व देकर पुनः विचार करते हैं",
    "phalaṃ garuṃ katvā paccavekkhanti": "फल को महत्व देकर पुनः विचार करते हैं",
})
CLAUSE.update(_EARLY)
PREFIX["ariyā"] = "आर्य"
PREFIX["asaññasattānaṃ"] = "पहचान-रहित प्राणियों में"
CLAUSE.update({
    "ariyā maggaṃ upanissāya anuppannaṃ samāpattiṃ uppādenti": "आर्य मार्ग के प्रबल आश्रय से उत्पन्न न हुई ध्यान-अवस्था उत्पन्न करते हैं",
    "uppannaṃ samāpajjanti": "उत्पन्न हो चुकी ध्यान-अवस्था में प्रवेश करते हैं",
    "lokuttaro dhammo": "लोकोत्तर परिघटना", "ariyānaṃ maggo": "आर्यों का मार्ग",
    "dibbena cakkhunā": "दिव्य आँख से", "gāmaghātaṃ karoti": "गाँव पर हमला करता है",
    "jhānā vuṭṭhahitvā jhānaṃ": "ध्यान से उठकर ध्यान", "kāyaviññāṇasahagato": "शरीर की चेतना के साथ होने वाला",
    "lokiye ekaṃ": "लौकिक में एक", "lokuttare tīṇi": "लोकोत्तर में तीन",
    "phalaṃ garuṃ katvā": "फल को महत्व देकर",
    "sekkhā gotrabhuṃ garuṃ katvā": "सीखने के चरण वाले व्यक्ति गोत्र-परिवर्तन को महत्व देकर",
    "pubbe samudāciṇṇe kilese": "पहले बार-बार उठे मन के क्लेशों को",
    "saṅkhāre aniccato dukkhato anattato vipassanti": "निर्मित परिघटनाओं को " + S.ANICCA + " अंतर्दृष्टि से देखते हैं",
    "sīlaṃ samādiyitvā": "सदाचार ग्रहण करके", "uposathakammaṃ katvā": "उपवास-व्रत का पालन करके",
    "uposathakammaṃ katvā taṃ garuṃ katvā assādeti abhinandati": "उपवास-व्रत का पालन करके उसे महत्व देकर उसका रस लेता है, उसमें आनंद लेता है",
    "uposathakammaṃ katvā taṃ paccavekkhati assādeti abhinandati": "उपवास-व्रत का पालन करके उस पर पुनः विचार करता है, उसका रस लेता है, उसमें आनंद लेता है",
    "tatiyo bhāgo niṭṭhito": "तीसरा भाग समाप्त",
    "vatthuṃ aniccato dukkhato anattato": "आधार को " + S.ANICCA,
    "vaṇṇasampadaṃ patthayamāno dānaṃ": "रंग-रूप की संपन्नता की कामना करते हुए दान",
    "vaṇṇasampadā saddhāya": "रंग-रूप की संपन्नता श्रद्धा के लिए",
    "vicikicchā uddhaccaṃ domanassaṃ uppajjati": "संशय, बेचैनी और उदासी उत्पन्न होते हैं",
    "vipassati": "अंतर्दृष्टि से देखता है",
    "vipāko appaṭigho": "कर्म-फल रूपी, टकराव से रहित", "vipāko upādānavippayutto eko": "कर्म-फल रूपी, आसक्ति से अलग एक",
    "senāsanaṃ lokiyāya saddhāya": "निवास-स्थान लौकिक श्रद्धा के लिए",
})
U("paṭhamassa maggassa parikammaṃ", "पहले मार्ग की प्रारंभिक तैयारी", "N", "fs")
U("catutthassa maggassa parikammaṃ", "चौथे मार्ग की प्रारंभिक तैयारी", "N", "fs")
for o, d, h, hd in [("paṭhamo", "paṭhamassa", "पहला", "पहले"), ("dutiyo", "dutiyassa", "दूसरा", "दूसरे"),
                    ("tatiyo", "tatiyassa", "तीसरा", "तीसरे"), ("catuttho", "catutthassa", "चौथा", "चौथे")]:
    U(f"{o} maggo", f"{h} मार्ग", "N", "ms"); U(f"{d} maggassa", f"{hd} मार्ग", "D")
U("kabaḷīkārassa āhārassa", "कौर-कौर खाए जाने वाले भोजन", "D")
U("kusalākusalaṃ kammaṃ", "हितकर और हानिकर कर्म,", "N", "ms"); U("vipākassa", "कर्म-फल", "D")
U("upādānaṃ|upādānañca", "आसक्ति", "AN", "fs"); U("vuṭṭhānassa", "बाहर आने", "D")
U("sampayuttakānaṃ upādānānaṃ", "जुड़ी हुई आसक्तियों", "D")
U("upādānasampayuttakānaṃ khandhānaṃ", "आसक्ति से जुड़े समूहों", "D")
U("upādānavippayuttakānaṃ khandhānaṃ", "आसक्ति से अलग समूहों", "D")
U("upādānasampayuttakā khandhā", "आसक्ति से जुड़े समूह", "N")
U("upādānasampayuttakānañceva no ca upādānānaṃ khandhānaṃ", "आसक्ति से जुड़े, पर स्वयं आसक्ति रूपी न होने वाले समूहों", "D")
U("upādānā ca noupādānā ca hetū", "आसक्ति रूपी और आसक्ति रूपी न होने वाले मूल", "N")
U("upādāniyā ceva no ca upādānādhipati", "आसक्ति का विषय बनने वाली, पर स्वयं आसक्ति रूपी न होने वाली प्रधानता", "N", "fs")
U("upādānāni maggaṅgāni", "आसक्ति रूपी मार्ग के अंग", "N")
U("phalasamāpatti", "फल की ध्यान-अवस्था", "N", "fs")
U("diṭṭhigatavippayuttalobhasahagato moho|diṭṭhigatavippayuttalobhasahagato moho ca", "ग़लत दृष्टि से अलग और लोभ के साथ होने वाला मोह", "N", "ms")
U("diṭṭhigatavippayuttalobhasahagatā hetū", DGV + " मूल", "N")
U("cittasamuṭṭhānānañca rūpaṃ", "मन से उत्पन्न भौतिक रूप", "N", "ms")   # agreement slip in the source, rendered grammatically
U("dvinnaṃ mahābhūtānaṃ", "दो महाभूतों", "D")
U("ṭhānāṭhānakosallassa", "संभव और असंभव को जानने की कुशलता", "D")
U("arūpī adhipati", "अभौतिक प्रधानता", "N", "fs"); U("rūpī adhipati", "भौतिक प्रधानता", "N", "fs")
CLAUSE["appaṭigho eko khandho tiṇṇannaṃ khandhānaṃ sappaṭighānañca appaṭighānañca"] = \
    "टकराव से रहित एक समूह तीन समूहों के लिए और टकराव वाले और टकराव से रहित"
U("kenaci viññeyyā hetū","किसी एक प्रकार की चेतना से जाने जा सकने वाले मूल", "N")
for w, hf in [("rūpī", "भौतिक"), ("arūpī", "अभौतिक"), ("rūpīnaṃ", "भौतिक"), ("arūpīnaṃ", "अभौतिक")]:
    ADJF[w] = {"f": hf, "d": hf, "o": hf, "m": hf}
ADJF["lokiyāya"] = {"f": "लौकिक", "d": "लौकिक", "o": "लौकिक", "m": "लौकिक"}
# multi-word adjectives (complex items) as modifiers
_MW = {
    "kenaci viññeyya": ("viññeyya", ["kenaci viññeyyā", "kenaci viññeyyaṃ", "kenaci viññeyyañca", "kenaci viññeyyo", "kenaci viññeyye", "kenaci viññeyyānaṃ"]),
    "kenaci naviññeyya": ("naviññeyya", ["kenaci naviññeyyā", "kenaci naviññeyyaṃ", "kenaci naviññeyyañca", "kenaci naviññeyyo", "kenaci naviññeyye", "kenaci naviññeyyānaṃ"]),
    "upādānaupādānasampayutta": ("upādānaupādānasampayutta", ["upādānā ceva upādānasampayuttā ca", "upādāno ceva upādānasampayutto ca", "upādāne ceva upādānasampayutte ca"]),
    "upādānaupādāniya": ("upādānaupādāniya", ["upādānā ceva upādāniyā ca", "upādāno ceva upādāniyo ca", "upādāne ceva upādāniye ca"]),
    "hetusahetuka": ("hetusahetuka", ["hetū ceva sahetukā ca", "hetu ceva sahetuko ca", "hetū ceva sahetuke ca"]),
    "hetuhetusampayutta": ("hetuhetusampayutta", ["hetū ceva hetusampayuttā ca", "hetu ceva hetusampayutto ca", "hetū ceva hetusampayutte ca"]),
}
for _n, (_k, _ws) in _MW.items():
    hf = IT[_k][3]
    for w in _ws:
        ADJF[w] = {"f": hf, "d": masc(hf, "d"), "o": masc(hf, "o"), "m": masc(hf, "o")}
for _n, (_k, _f) in ADJ_X.items():
    hf = IT[_k][3]
    for w in _f[:6]:
        ADJF.setdefault(w, {"f": hf, "d": masc(hf, "d"), "o": masc(hf, "o"), "m": masc(hf, "o")})
SLIPS["ādhipatiyā"] = "adhipatiyā"   # spelling slip, rendered as meant
# closing lines «X niṭṭhitaṃ» = «X समाप्त»
_CLOSE = {"hetudukaṃ": "Hetudukaṃ", "hetugocchakaṃ": "Hetugocchakaṃ"}

# «cetopariyañāṇena Xcittasamaṅgissa cittaṃ jānāti / jānanti»
_CS = {"rūpī": "rūpi", "arūpī": "arūpi", "sahetukanahetu": "sahetukā ceva na ca hetu",
       "hetusampayuttanahetu": "hetusampayuttā ceva na ca hetu", "hetusahetuka": "hetū ceva sahetukā ca ",
       "upādāniyanoupādāna": "upādāniyā ceva no ca upādāna", "upādānasampayuttanoupādāna": "upādānasampayuttā ceva no ca upādāna"}
for k, (a, n, d, h, c) in IT.items():
    if k in ("viññeyya", "naviññeyya"):
        continue
    stem = _CS.get(k, k)
    hm = masc(h, "o")
    for v, vh in (("jānāti", "जानता है"), ("jānanti", "जानते हैं")):
        CLAUSE[f"cetopariyañāṇena {stem}cittasamaṅgissa cittaṃ {v}"] = \
            f"दूसरों के मन को जानने के ज्ञान से {hm} मन से युक्त व्यक्ति के मन को {vh}"

# headings
HEAD = {
    "(Tatiyo bhāgo)": "(तीसरा भाग)",
    "Dhammānulome dukapaṭṭhānaṃ": "परिघटनाओं का सकारात्मक क्रम: दो-दो के वर्गीकरणों के कारण-संबंध",
    "Hetugocchakaṃ": "मूलों का वर्ग", "Cūḷantaradukaṃ": "बीच के छोटे दो-दो के वर्गीकरण",
    "Upādānagocchakaṃ": "आसक्ति का वर्ग",
    "Hetudukaṃ": "मूल वाला दो का वर्गीकरण", "*Hetudukaṃ": S.DUKA["hetu"],
    "Sahetukadukaṃ": "मूल वाली परिघटनाओं वाला दो का वर्गीकरण",
    "Hetusampayuttadukaṃ": "मूलों से जुड़ी परिघटनाओं वाला दो का वर्गीकरण",
    "Hetusahetukadukaṃ": "मूल रूपी भी और मूल वाली भी परिघटनाओं वाला दो का वर्गीकरण",
    "Hetuhetusampayuttadukaṃ": "मूल रूपी भी और मूलों से जुड़ी भी परिघटनाओं वाला दो का वर्गीकरण",
    "Nahetusahetukadukaṃ": "मूल रूपी न होने वाली, पर मूल वाली परिघटनाओं वाला दो का वर्गीकरण",
    "Sappaccayadukaṃ": "कारणों पर निर्भर रहने वाली परिघटनाओं वाला दो का वर्गीकरण",
    "Saṅkhatadukaṃ": "निर्मित परिघटनाओं वाला दो का वर्गीकरण",
    "Sanidassanadukaṃ": "दिखाई देने वाली परिघटनाओं वाला दो का वर्गीकरण",
    "Sappaṭighadukaṃ": "टकराव वाली परिघटनाओं वाला दो का वर्गीकरण",
    "Rūpīdukaṃ": "भौतिक परिघटनाओं वाला दो का वर्गीकरण",
    "Lokiyadukaṃ": "लौकिक परिघटनाओं वाला दो का वर्गीकरण",
    "Kenaciviññeyyadukaṃ": "किसी एक प्रकार की चेतना से जानी जा सकने वाली परिघटनाओं वाला दो का वर्गीकरण",
    "Upādānadukaṃ": "आसक्ति वाला दो का वर्गीकरण",
    "Upādāniyadukaṃ": "आसक्ति का विषय बनने वाली परिघटनाओं वाला दो का वर्गीकरण",
    "Upādānasampayuttadukaṃ": "आसक्ति से जुड़ी परिघटनाओं वाला दो का वर्गीकरण",
    "Upādānaupādāniyadukaṃ": "आसक्ति रूपी भी और आसक्ति का विषय बनने वाली भी परिघटनाओं वाला दो का वर्गीकरण",
    "Upādānaupādānasampayuttadukaṃ": "आसक्ति रूपी भी और आसक्ति से जुड़ी भी परिघटनाओं वाला दो का वर्गीकरण",
    "Upādānavippayuttaupādāniyadukaṃ": "आसक्ति से अलग, पर उसका विषय बनने वाली परिघटनाओं वाला दो का वर्गीकरण",
    "Paccanīyuddhāro": "नकारात्मक क्रम के लिए कारणों की छँटाई",
    "Sahajātavāro": "सह-उत्पत्ति का खंड", "Paccayavāro": "कारण का खंड", "Nissayavāro": "आश्रय का खंड",
    "Saṃsaṭṭhavāro": "घुले-मिले होने का खंड", "Sampayuttavāro": "जुड़ाव का खंड",
    "2-6 Sahajāta-paccaya-nissaya-saṃsaṭṭha-sampayuttavāro": "2-6 सह-उत्पत्ति, कारण, आश्रय, घुले-मिले होने और जुड़ाव का खंड",
    "2-6. Sahajāta-paccaya-nissaya-saṃsaṭṭha-sampayuttavāro": "2-6. सह-उत्पत्ति, कारण, आश्रय, घुले-मिले होने और जुड़ाव का खंड",
    "4-6. Nissaya-saṃsaṭṭha-sampayuttavāro": "4-6. आश्रय, घुले-मिले होने और जुड़ाव का खंड",
    "1-7. Paṭiccavārādi": "1-7. निर्भरता का खंड आदि",
    "1-4. Paccayānulomādi": "1-4. कारणों का सकारात्मक क्रम आदि",
    "Paccayānulomādi": "कारणों का सकारात्मक क्रम आदि",
    "Anulomapaccanīyaṃ": "सकारात्मक-नकारात्मक क्रम",
    "Pacchājātāsevanapaccayā": "पश्चात्-उत्पत्ति-कारण और पुनरावृत्ति-कारण",
    "Vipākāhārapaccayā": "कर्म-फल-कारण और आहार-कारण",
    "Kamma-vipākapaccayā": "कर्म-कारण और कर्म-फल-कारण",
    "Saṅkhyāvāro": "गणना का खंड", "Vibhaṅgavāro": "विश्लेषण का खंड",
}
for _h, _v in list(HEAD.items()):
    if _h[0].isupper() and _h.endswith("aṃ") and " " not in _h:
        CLAUSE[_h[0].lower() + _h[1:] + " niṭṭhitaṃ"] = _v + " समाप्त"
        CLAUSE[_h[0].lower() + _h[1:] + " niṭṭhito"] = _v + " समाप्त"
for _k in S.KEYS:
    _cap = _k[0].upper() + _k[1:]
    _n = ("no" if _k in ("atthi", "natthi", "vigata", "avigata") else "na") + _k
    _ncap = _n[0].upper() + _n[1:]
    HEAD[f"{_cap}paccayādi"] = S.NAME[_k] + " आदि"
    HEAD[f"{_ncap}paccayādi"] = S.NNAME[_k] + " आदि"
    HEAD[f"*{_cap}dukaṃ"] = S.DUKA[_k]
    HEAD[f"*{_ncap}dukaṃ"] = S.NDUKA[_k]
