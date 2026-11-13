"""pi-7 Pāli->Hindi keyword maps for 3-07-nivaranagocchaka, 3-08-paramasagocchaka, 3-10-upadanagocchaka,
4-03-dukatika-sahetukaduka, 4-04-dukatika-sappaccayaduka, 4-05-dukatika-asavaduka, 4-06-dukatika-sannojanaduka.

Uses map_sample_hi.py (read-only import) and hi-map-conventions-pi7.md.
usage: python -I -B -X utf8 map_3-07_4-06_hi.py probe [file …]   (unmapped keywords + fallback values, writes nothing)
       python -I -B -X utf8 map_3-07_4-06_hi.py build [file …]   (write <f>.mapped.md + verify)
       python -I -B -X utf8 map_3-07_4-06_hi.py audit [file …]   (fallback-source values)
"""
import sys, pathlib, collections
sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import *  # noqa: F401,F403
from map_sample_hi import read_keywords, make_resolver, build_part, verify, audit, PI7, NDE

FILES = ("3-07-nivaranagocchaka", "3-08-paramasagocchaka", "3-10-upadanagocchaka",
         "4-03-dukatika-sahetukaduka", "4-04-dukatika-sappaccayaduka", "4-05-dukatika-asavaduka",
         "4-06-dukatika-sannojanaduka")

# shared additions (lower-case first letter keys)
T = {}
# negative ablative: «<name> के बिना» in the text frames; in compound headings «Nahetu-naadhipatipaccayā»
# (plural noun, text «… का अभाव और … का अभाव») the noun value «<name> का अभाव».
for _st, _name, _loc, _neg, _plain in CONDITIONS:
    T[_neg + _st + "paccayā"] = (f"{_name} के बिना", f"{_name} का अभाव")
T.update({
    "majjhe": "बीच", "labbhati": "लागू होना",                                   # pi-2 बीच, pi-3 लागू होना
    "cūḷantaraduke": "बीच के छोटे दो-दो के वर्गीकरण",                           # = heading Cūḷantaradukaṃ
    "lokiyadukasadisaṃ": "लौकिक परिघटनाओं वाले दो के वर्गीकरण के समान",
    "vicikicchāsahagate": "संशय के साथ होने वाला", "vicikicchāsahagato": "संशय के साथ होने वाला",
    "uddhaccasahagate": "बेचैनी के साथ होने वाला", "uddhaccasahagato": "बेचैनी के साथ होने वाला",  # pi-1
    "moho": "मोह", "mohaṃ": "मोह", "mohassa": "मोह",
    "appaṭighaṃ": "टकराव से रहित", "appaṭigho": "टकराव से रहित",                 # pi-1
    "arūpiṃ": "अभौतिक", "arūpī": "अभौतिक", "arūpissa": "अभौतिक", "rūpiṃ": "भौतिक", "rūpī": "भौतिक",
    "lokuttaraṃ": "लोकोत्तर", "lokuttaro": "लोकोत्तर", "lokuttarassa": "लोकोत्तर",
    "sappaccayo": "कारणों पर निर्भर रहने वाला", "appaccayo": "कारणों पर निर्भर न रहने वाला",
    "appaccayaṃ": "कारणों पर निर्भर न रहने वाला",
    "naviññeyyo": "न जाना जा सकने वाला", "naviññeyyaṃ": "न जाना जा सकने वाला",
    # condition stems as members of compound headings («Pacchājāta-āsevanapaccayā» = the names;
    # «Sahajāta-paccaya-nissaya-saṃsaṭṭha-sampayuttavāro» = the vāra labels)
    "sahajāta": ("सह-उत्पत्ति-कारण", "सह-उत्पत्ति"), "pacchājāta": ("पश्चात्-उत्पत्ति-कारण", "पश्चात्-उत्पत्ति"),
    "anantara": ("निकटता-कारण", "निकटता"), "kamma": ("कर्म-कारण", "कर्म"),
    "adhipati": ("प्रधानता-कारण", "प्रधानता"), "nissaya": ("आश्रय-कारण", "आश्रय"),
    "saṃsaṭṭha": "घुले-मिले होने",                                    # VARAS «घुले-मिले होने का खंड»
    # the nīvaraṇa names (pi-1/pi-2/pi-7 2-09)
    "kāmacchandanīvaraṇaṃ": "इंद्रिय-सुखों की चाह की बाधा", "byāpādanīvaraṇaṃ": "दुर्भावना की बाधा",
    "thinamiddhanīvaraṇaṃ": "आलस्य और तंद्रा की बाधा", "uddhaccanīvaraṇaṃ": "बेचैनी की बाधा",
    "kukkuccanīvaraṇaṃ": "पछतावे की बाधा", "vicikicchānīvaraṇaṃ": "संशय की बाधा",
    "avijjānīvaraṇaṃ": "अज्ञान की बाधा",
    "kāmacchandanīvaraṇassa": "इंद्रिय-सुखों की चाह की बाधा", "thinamiddhanīvaraṇassa": "आलस्य और तंद्रा की बाधा",
    "uddhaccanīvaraṇassa": "बेचैनी की बाधा", "avijjānīvaraṇassa": "अज्ञान की बाधा",
    "vicikicchānīvaraṇassa": "संशय की बाधा", "byāpādanīvaraṇassa": "दुर्भावना की बाधा",
    "kāmacchandena": "इंद्रिय-सुखों की चाह", "paṭighena": "चिढ़",
    "dvikkhattuṃ": "दो बार", "catukkhattuṃ": "चार बार", "ubhopete": "ये दोनों",
    "nīvaraṇadukassa": "बाधा वाला दो का वर्गीकरण",
    # Pañhāvāra / frame words
    "cakkaṃ": "चक्र", "cakkā": "चक्र",
    "sampayuttake": "जुड़ा हुआ",                                      # «जुड़े हुए समूहों»
    "yāva": "तक", "asaññasattā": "पहचान-रहित प्राणी",                  # «(पहचान-रहित प्राणियों तक)»
    "avasesā": "बाकी", "kātabbaṃ": ("करना चाहिए", "बनाना चाहिए"), "kātabbā": "करना चाहिए",
    "kātabbo": "करना चाहिए", "kātabbāni": "करना चाहिए",
    "vibhajitabbaṃ": "विश्लेषण करना चाहिए", "vibhajitabbā": "विश्लेषण करना चाहिए",
    "nibbānaṃ": "निर्वाण", "āvajjanā": "मन को विषय की ओर मोड़ना",
    "vuṭṭhānassa": "बाहर आना",                                       # «बाहर आने के लिए»
    "cetopariyañāṇena": "दूसरों के मन को जानने का ज्ञान",
    "rāgassa": "राग", "āhāraṃ": "आहार", "upanissayā": "प्रबल आश्रय",   # «(तीन प्रबल आश्रय)»
    "anulomamātikā": "सकारात्मक क्रम की मूल सूची",
    "ninnānākaraṇaṃ": "बिना किसी अंतर के",
    "katvā": ("देकर", "पालन करके"),                                  # «उपवास-व्रत का पालन करके»
    "rūpaṃ": ("भौतिक रूप", "दृश्य रूप"),                               # «दिव्य आँख से दृश्य रूप देखता है»
    "jappeti": ("पालना", "करना"), "gaṇhāti": ("ग्रहण करना", "पकड़ना"),   # «अहंकार करता है, दृष्टि को पकड़ता है»
    "pāṇaṃ": ("जीव", "प्राणी"),                                       # «प्राणी की हत्या करता है»
    "doso": "द्वेष", "dosaṃ": "द्वेष", "dosassa": "द्वेष", "dukkhassa": "दुःख", "diṭṭhiyā": "दृष्टि",
    "gotrabhuṃ": "गोत्र-परिवर्तन", "gaṇanā": "गणना", "anulomagaṇanā": "सकारात्मक क्रम की गणना",
    "parivattetabbā": "उलट-पलट करना चाहिए", "ninnānākaraṇā": "बिना किसी अंतर के",
    "paccavekkhitvā": "जाँचकर",                                      # «इसी तरह जाँचकर करना चाहिए»
    "natthi": "नहीं",                                              # «… नहीं है» (pi-1 «नहीं»)
    "anulomaṃ": ("सकारात्मक क्रम", "अनुरूपता"),                       # «अनुलोमं गोत्रभुस्स» = अनुरूपता
    "vipāko": ("कर्म-फल रूपी", "कर्म के फल रूपी", "कर्म-फल"),          # «vipāko natthi» = «कर्म-फल नहीं है»
    "lokiyadukaṃ": ("लौकिक परिघटनाओं वाला दो का वर्गीकरण", "लौकिक वाला दो का वर्गीकरण"),
    "purimo": "पहले-पहले का",                                        # «पहले-पहले की ग़लत धारणा»
    "pacchājātā": ("बाद में उत्पन्न", "पश्चात्-उत्पत्ति"),             # «(पश्चात्-उत्पत्ति करनी चाहिए)»
    "parāmāsadukasadisaṃ": "ग़लत धारणा वाले दो के वर्गीकरण के समान",
    "labbhati": ("लागू होना", "मिलना"),                                # «जहाँ लोकोत्तर नहीं मिलता»
    "itare": "अन्य",
    "cakkā": ("बारी-बारी से", "चक्र"),                                 # «(sabbe cakkā kātabbā)» = «सभी को बारी-बारी से करना चाहिए»
    # the upādāna names (pi-1/pi-2; attavāda as the pi-7 text has it)
    "kāmupādānaṃ": "इंद्रिय-सुखों के प्रति आसक्ति", "kāmupādānassa": "इंद्रिय-सुखों के प्रति आसक्ति",
    "kāmupādāna": "इंद्रिय-सुखों के प्रति आसक्ति", "kāmupādānañca": "इंद्रिय-सुखों के प्रति आसक्ति",
    "diṭṭhupādānaṃ": "दृष्टियों के प्रति आसक्ति", "diṭṭhupādānañca": "दृष्टियों के प्रति आसक्ति",
    "diṭṭhupādānassa": "दृष्टियों के प्रति आसक्ति",
    "sīlabbatupādānaṃ": "सदाचार और व्रतों के प्रति आसक्ति", "attavādupādānaṃ": "आत्मवाद के प्रति आसक्ति",
    "lobho": "लोभ", "lobhaṃ": "लोभ", "lobhassa": "लोभ", "lobhañca": "लोभ",
    "diṭṭhigatavippayutto": "ग़लत दृष्टि से अलग", "diṭṭhigatavippayuttaṃ": "ग़लत दृष्टि से अलग",
    "ekoyeva": "केवल एक",
    # the unwholesome deeds of the Pañhāvāra (pi-4/pi-5)
    "adinnaṃ": "बिना दी गई वस्तु", "ādiyati": "ले लेना", "musā": "झूठ", "pisuṇaṃ": "चुगली",
    "samphaṃ": "व्यर्थ", "sandhiṃ": "सेंध", "nillopaṃ": "डाका", "ekāgārikaṃ": "एक ही घर में चोरी",
    "paripanthe": "राह में घात", "paradāraṃ": "पराई स्त्री", "gāmaghātaṃ": "गाँव पर हमला",
    "nigamaghātaṃ": "कस्बे पर हमला",
    "vibhajitabbaṃ": ("विश्लेषण करना चाहिए", "अलग-अलग दिखाना चाहिए"),
    "vibhajantena": "अलग-अलग दिखाते हुए",
    "arūpaṃyeva": "केवल अभौतिक", "pacchimassa": "बाद-बाद का",
    "kammapaccaye": "कर्म-कारण", "dassetabbo": "दिखाना चाहिए",
    "ninnānā": "बिना किसी अंतर के", "upādānadukasadisā": "आसक्ति वाले दो के वर्गीकरण के समान",
    "upādānadukasadisaṃ": "आसक्ति वाले दो के वर्गीकरण के समान",
    "sekkhā": ("सीखने के चरण का", "सीखने के चरण वाला"),                 # «सीखने के चरण वाले गोत्र-परिवर्तन को»
    "ghaṭane": "संयोजन", "ghaṭanādhipatipi": "संयोजन में प्रधानता",      # «संयोजन में तीनों», «संयोजन में प्रधानता भी»
    "anulomamātikā": ("सकारात्मक क्रम की मूल सूची", "सकारात्मक क्रम की सूची"),
    "itare": ("अन्य", "बाकी"),
    "āmasanaṃ": "उल्लेख", "nānākaraṇaṃ": "अंतर",                       # «केवल उल्लेख में अंतर है»
    "parihīne": "छूट जाना", "vippaṭisārissa": "ग्लानि से भरा व्यक्ति", "paripuṇṇaṃ": "पूर्ण",
    "diṭṭhigatavippayuttalobhasahagatādhipati": "ग़लत दृष्टि से अलग और लोभ के साथ होने वाली प्रधानता",
    "karoti": ("पालन करना", "करना"),                                  # «… कस्बे पर हमला करता है»
    "viññāṇā": "चेतना",                                              # «पाँच प्रकार की चेतनाएँ»
})
for _e in ("aṃ", "e", "ā", "ānaṃ", "o", "assa"):
    T["diṭṭhigatavippayuttalobhasahagat" + _e] = "ग़लत दृष्टि से अलग और लोभ के साथ होने वाला"
T["kātabbā"] = ("करना चाहिए", "बनाना चाहिए")                          # «मूल सूची बनानी चाहिए»

# per-file additions and overrides
TF = {f: {} for f in FILES}
OVR = {f: {} for f in FILES}
ALLOWED = {f: {} for f in FILES}
OVR["3-08-paramasagocchaka"]["7-U377"] = {"kātabbā": "तैयार करना चाहिए"}   # «… तैयार करने चाहिए»
OVR["3-10-upadanagocchaka"]["7-33-13"] = {"kātabbaṃ": "बनाना चाहिए"}     # «(cakkaṃ kātabbaṃ)» = «(चक्र बनाना चाहिए)»
ALLOWED["4-04-dukatika-sappaccayaduka"][("7-38-22", "labbhati")] = (
    "«na labbhati» = «लागू नहीं होती»: the negation «नहीं» (na, not a keyword) splits «लागू होना»")


def table(f):
    return {**PI7, **T, **TF[f]}


def probe(f):
    res = make_resolver(f, table(f), OVR[f])
    miss = collections.Counter()
    for bid, kws in read_keywords(f):
        for kw in kws:
            try:
                res(bid, kw, kws)
            except KeyError:
                miss[kw] += 1
    print("=" * 10, f, "unmapped:", len(miss))
    for kw, n in sorted(miss.items()):
        print("  ", kw, n)


def show(f, start=0, end=10 ** 9):
    """Per segment: Pāli, Hindi and the pairs; values not present in the Hindi are marked !!, values not
    from the table / heading / override get their source in braces."""
    from map_sample_hi import read_hindi, read_pali, present
    import os
    full = os.environ.get("FULL") == "1"
    width = int(os.environ.get("WIDTH", "500"))
    res = make_resolver(f, table(f), OVR[f])
    hi, pa = read_hindi(f), read_pali(f)
    for i, (bid, kws) in enumerate(read_keywords(f)):
        if not (start <= i < end):
            continue
        log = {}
        res = make_resolver(f, table(f), OVR[f], log)
        out, flag = [], False
        seen = set()
        for kw in kws:
            try:
                v = res(bid, kw, kws)
            except KeyError:
                out.append(f"{kw}=???")
                flag = True
                continue
            src = set(log.get((kw, v), {}))
            mark = "" if present(v, hi.get(bid)) else " !!"
            tag = "" if src <= {"table", "heading", "override"} else " {" + ",".join(sorted(src)) + "}"
            if mark or (tag and os.environ.get("FLAGSRC") == "1"):
                flag = True
            if (kw, v) in seen:
                continue
            seen.add((kw, v))
            out.append(f"{kw}={v}{mark}{tag}")
        if not full and not flag:
            continue
        if os.environ.get("ONLYKW") == "1":
            print(f"{i} [{bid}]", ", ".join(x for x in out if x.endswith(("???", "!!")) or "{" in x))
            continue
        print(f"{i} [{bid}] PA:", pa.get(bid, "")[:width])
        print("     HI:", hi.get(bid, "")[:width])
        print("     KW:", ", ".join(out))


def pairs(f):
    """Every distinct kw=value with its count and sources (lower-cased keyword)."""
    log = {}
    res = make_resolver(f, table(f), OVR[f], log)
    for bid, kws in read_keywords(f):
        for kw in kws:
            try:
                res(bid, kw, kws)
            except KeyError:
                log.setdefault((kw, "???"), collections.Counter())["miss"] += 1
    by = collections.defaultdict(list)
    for (kw, v), c in log.items():
        by[kw.lower()].append((v, sum(c.values()), ",".join(sorted(c))))
    for k in sorted(by):
        print(k, "->", " | ".join(f"{v} x{n} {s}" for v, n, s in by[k]))


def amb(f):
    """Segments where a tuple value has more than one alternative present (the first wins): read these."""
    from map_sample_hi import read_hindi, present, lc
    tab, hi = table(f), read_hindi(f)
    for bid, kws in read_keywords(f):
        for kw in dict.fromkeys(kws):
            if kw in OVR[f].get(bid, {}):
                continue
            v = tab.get(lc(kw))
            if isinstance(v, tuple):
                alts = [a for a in v if a != NDE and present(a, hi.get(bid))]
                alts = [a for i, a in enumerate(alts) if not any(a in b for b in alts[:i])]
                if len(alts) > 1:
                    print(f, bid, kw, alts, "count", kws.count(kw))


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "amb":
        for f in sys.argv[2:] or FILES:
            amb(f)
        sys.exit()
    if len(sys.argv) > 2 and sys.argv[1] == "pairs":
        pairs(sys.argv[2])
        sys.exit()
    if len(sys.argv) > 2 and sys.argv[1] == "show":
        a = int(sys.argv[3]) if len(sys.argv) > 3 else 0
        b = int(sys.argv[4]) if len(sys.argv) > 4 else 10 ** 9
        show(sys.argv[2], a, b)
        sys.exit()
    mode = sys.argv[1] if len(sys.argv) > 1 else "build"
    files = sys.argv[2:] or FILES
    for f in files:
        if mode == "probe":
            probe(f)
        elif mode == "audit":
            print("=" * 10, f)
            audit(f, table(f), OVR[f], only_fallback=True)
        else:
            build_part(f, make_resolver(f, table(f), OVR[f]))
            verify(f, allowed=ALLOWED[f])
