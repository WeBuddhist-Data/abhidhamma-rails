"""pi-7 Pāli->Hindi keyword maps for 3-02-culantaraduka, 3-03-asavagocchaka, 3-04-sannojanagocchaka,
3-05-ganthagocchaka, 3-06-oghayogagocchaka (conventions: hi-map-conventions-pi7.md; map_sample_hi.py imported
read-only).
usage: python -I -B -X utf8 map_3-02_3-06_hi.py [--audit]
"""
import collections, re, sys, pathlib; sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import *  # noqa
from map_sample_hi import read_hindi, read_pali, read_keywords, NDE, GAP, lc  # noqa

FILES = ["3-02-culantaraduka", "3-03-asavagocchaka", "3-04-sannojanagocchaka",
         "3-05-ganthagocchaka", "3-06-oghayogagocchaka"]

T = {}
_E = ("o", "ā", "aṃ", "assa", "ānaṃ", "e", "a", "añca", "ānañca")


def _forms(stem, value, endings=_E):
    for e in endings:
        T[stem + e] = value


# --- the minor dyads (cūḷantaraduka): sappaccaya, saṅkhata, sanidassana, sappaṭigha, rūpī, lokiya,
# kenaci viññeyya (pi-1/pi-2 matrix wording as the pi-7 Hindi has it)
_forms("sappaccay", "कारणों पर निर्भर रहने वाला")
_forms("appaccay", "कारणों पर निर्भर न रहने वाला")
_forms("saṅkhat", "निर्मित")
_forms("asaṅkhat", "अनिर्मित")
_forms("sanidassan", "दिखाई देने वाला")
_forms("anidassan", "दिखाई न देने वाला")
_forms("sappaṭigh", "टकराव वाला")
_forms("appaṭigh", "टकराव से रहित")
_forms("lokiy", "लौकिक")
_forms("lokuttar", "लोकोत्तर")
T["lokuttarasa"] = "लोकोत्तर"                                   # Pāli misprint (7-25-156)
for _k in ("rūpī", "rūpiṃ", "rūpissa", "rūpīnaṃ", "rūpino", "rūpiñca"):
    T[_k] = "भौतिक"
    T["a" + _k] = "अभौतिक"
T.update({
    "naviññeyyo": "न जाना जा सकने वाला", "naviññeyyaṃ": "न जाना जा सकने वाला", "naviññeyyā": "न जाना जा सकने वाला",
    "viññeyyo": "जाना जा सकने वाला", "viññeyyā": "जाना जा सकने वाला",
    "cūḷantaraduke": "बीच के छोटे दो-दो के वर्गीकरण", "cūḷantaradukaṃ": "बीच के छोटे दो-दो के वर्गीकरण",
    "lokiyadukaṃ": ("लौकिक परिघटनाओं वाला दो का वर्गीकरण", "लौकिक वाला दो का वर्गीकरण"),
    "lokiyadukasadisaṃ": "लौकिक वाले दो के वर्गीकरण के समान",
    "ganthadukasadisaṃ": "गाँठ वाले दो के वर्गीकरण के समान",
    "paṭhamadukasadisaṃ": "पहले दो के वर्गीकरण के समान",
    "saññojanagocchake": "बंधनों का वर्ग",
    "āsavadukepi": "मन के मैल वाला दो का वर्गीकरण",
    # sub-kinds of predominance in the Pañhāvāra («X प्रधानता»)
    "adhipati": "प्रधानता",
    "lokiyādhipati": "लौकिक प्रधानता", "lokuttarādhipati": "लोकोत्तर प्रधानता",
    "anidassanādhipati": "दिखाई न देने वाली प्रधानता",
    "noganthādhipati": "गाँठ रूपी न होने वाली प्रधानता",
    "domanassasahagatādhipati": "उदासी के साथ होने वाली प्रधानता",
    "diṭṭhigatavippayuttalobhasahagatādhipati": "ग़लत दृष्टि से अलग और लोभ के साथ होने वाली प्रधानता",
    # «X-cittasamaṅgissa» = «X मन से युक्त व्यक्ति»
    "anidassanacittasamaṅgissa": "दिखाई न देने वाले मन से युक्त व्यक्ति",
    "appaṭighacittasamaṅgissa": "टकराव से रहित मन से युक्त व्यक्ति",
    "arūpicittasamaṅgissa": "अभौतिक मन से युक्त व्यक्ति",
    "āsavavippayuttacittasamaṅgissa": "मन के मैलों से अलग मन से युक्त व्यक्ति",
    "cetopariyañāṇena": "दूसरों के मन को जानने का ज्ञान",
})

# --- mental factors and the "accompanied by" adjectives (hi-zeroshot-terms / build_3-03_3-08_hi.py)
_SAH = ("e", "o", "ā", "aṃ", "ānaṃ", "assa", "a", "añca")
for _p, _h in (("vicikicchā", "संशय"), ("uddhacca", "बेचैनी"), ("domanassa", "उदासी"),
               ("diṭṭhigatavippayuttalobha", "ग़लत दृष्टि से अलग और लोभ"), ("lobha", "लोभ"),
               ("cakkhuviññāṇa", "आँख की चेतना"), ("kāyaviññāṇa", "शरीर की चेतना"),
               ("sotaviññāṇa", "कान की चेतना"), ("ghānaviññāṇa", "नाक की चेतना"),
               ("jivhāviññāṇa", "जीभ की चेतना")):
    for _e in _SAH:
        T[f"{_p}sahagat{_e}"] = f"{_h} के साथ होने वाला"
T.update({
    "diṭṭhigatavippayutto": "ग़लत दृष्टि से अलग", "diṭṭhigatavippayuttaṃ": "ग़लत दृष्टि से अलग",
    "moho": "मोह", "mohaṃ": "मोह", "mohassa": "मोह", "mohañca": "मोह",
    "lobho": "लोभ", "lobhaṃ": "लोभ", "lobhassa": "लोभ", "lobhañca": "लोभ",
    "paṭighaṃ": "चिढ़", "paṭighañca": "चिढ़", "paṭighassa": "चिढ़", "paṭigho": "चिढ़",
    "doso": "द्वेष", "dosaṃ": "द्वेष", "dosassa": "द्वेष",
    "rāgassa": "राग", "diṭṭhiyā": "दृष्टि", "mānassa": "अहंकार",
    "jappeti": "करना",                               # «अहंकार करता है» in these files (pi-2 पालना not in the text)
    "gaṇhāti": ("पकड़ना", "ग्रहण करना"),            # «दृष्टि को पकड़ता है» / 3-02 «दृष्टि ग्रहण करता है»
    "pāṇaṃ": ("प्राणी", "जीव"),                      # «प्राणी की हत्या करता है»
    "vaṇṇasampadaṃ": ("रंग-रूप की संपन्नता", "रूप-सौंदर्य"), "vaṇṇasampadā": ("रंग-रूप की संपन्नता", "रूप-सौंदर्य"),
})

# --- the āsava / saññojana / gantha members (hi-zeroshot-terms; pi-1/pi-2 «दृष्टि का मैल» …)
for _p, _h in (("kāmāsav", "इंद्रिय-सुखों का मैल"), ("bhavāsav", "अस्तित्व का मैल"),
               ("diṭṭhāsav", "दृष्टि का मैल"), ("avijjāsav", "अज्ञान का मैल")):
    _forms(_p, _h)
for _p, _h in (("kāmarāga", "इंद्रिय-सुखों के राग का बंधन"), ("paṭigha", "चिढ़ का बंधन"), ("māna", "अहंकार का बंधन"),
               ("diṭṭhi", "दृष्टि का बंधन"), ("vicikicchā", "संशय का बंधन"),
               ("sīlabbataparāmāsa", "सदाचार और व्रतों के बारे में ग़लत धारणा का बंधन"),
               ("bhavarāga", "अस्तित्व के राग का बंधन"), ("issā", "ईर्ष्या का बंधन"),
               ("macchariya", "कंजूसी का बंधन"), ("avijjā", "अज्ञान का बंधन")):
    _forms(_p + "saññojan", _h)
    _forms(_p + "saṃyojan", _h)
_forms("abhijjhākāyaganth", "लालच रूपी काया की गाँठ")
_forms("byāpādakāyaganth", "दुर्भावना रूपी काया की गाँठ")
_forms("kāyaganth", "काया की गाँठ")
_forms("sīlabbataparāmās", "सदाचार और व्रतों के बारे में ग़लत धारणा")
_forms("sīlabbataparāmāsakāyaganth", "सदाचार और व्रतों के बारे में ग़लत धारणा रूपी काया की गाँठ")
_forms("idaṃsaccābhinives", "“केवल यही सत्य है” का आग्रह")
_forms("idaṃsaccābhinivesakāyaganth", "“केवल यही सत्य है” के आग्रह रूपी काया की गाँठ")
for _st, _niy, _term, _obl, _pron in CLUSTERS:
    for _e in ("akā", "akānaṃ", "akānañca", "ake"):
        T[f"{_st}sampayutt{_e}"] = f"{_obl} से जुड़ा"

# --- conditions in the locative «X-paccaye» (= the name, as the count locatives)
for _st, _name, _loc, _neg, _plain in CONDITIONS:
    T[_st + "paccaye"] = _name
T.update({"sahajāta": "सह-उत्पत्ति", "upanissayā": "प्रबल आश्रय", "upanissayaṃ": "प्रबल आश्रय",
          "anantaraṃ": "निकटता-कारण", "paccayaṃ": "कारण"})

# --- matter, objects, Pañhāvāra vocabulary
T.update({
    "āpodhātuṃ": "जल तत्व", "āpodhātuñca": "जल तत्व", "āpodhātu": "जल तत्व",
    "kabaḷīkāraṃ": "कौर-कौर खाया जाने वाला", "kabaḷīkārassa": "कौर-कौर खाया जाने वाला",
    "āhāraṃ": ("भोजन", "आहार"), "āhārassa": ("भोजन", "आहार"),
    "kaṭattārūpā": "किए गए कर्म से उत्पन्न भौतिक रूप",
    "cakkhāyatanassa": "आँख का इंद्रिय-क्षेत्र", "phoṭṭhabbāyatanassa": "स्पर्श का इंद्रिय-क्षेत्र",
    "pañcāyatanāni": "पाँच इंद्रिय-क्षेत्र",
    "nibbānaṃ": "निर्वाण", "gotrabhuṃ": "गोत्र-परिवर्तन", "phalā": "फल", "phalasamāpatti": "फल की ध्यान-अवस्था",
    "vuṭṭhānassa": "बाहर आना", "vuṭṭhānaṃ": "बाहर आना", "āvajjanā": "मन को विषय की ओर मोड़ना",
    "assādanā": "रस लेना",
    "vipākassa": "कर्म-फल", "vipākanti": "कर्म-फल",
    "vipāko": ("कर्म-फल रूपी", "कर्म के फल रूपी", "कर्म-फल"),
    "sekkhā": ("सीखने के चरण का", "सीखने के चरण वाला"),
    "anulomaṃ": ("सकारात्मक क्रम", "अनुरूपता"),                  # «anulomaṃ gotrabhussa» = अनुरूपता
    "garukārammaṇā": "महत्व दिए गए विषय",                          # plural concept, text «महत्व दिए गए विषय»
    "yāva": "तक", "asaññasattā": "पहचान-रहित प्राणी",
    "ahetukā": "मूल से रहित", "ahetuke": "मूल से रहित",
    "pavattipaṭisandhi": "जीवन-काल और पुनर्जन्म",
    "purimo": "पहले-पहले का", "pacchimassa": "बाद-बाद का",
    "paṭhamo": "पहला", "dutiyassa": "दूसरा", "tatiyo": "तीसरा", "catutthassa": "चौथा", "paṭhamassa": "पहला",
    "parikammaṃ": "प्रारंभिक तैयारी", "saṅkhāre": "मानसिक रचना",
    "ṭhānāṭhānakosallassa": "उचित और अनुचित की कुशलता",
    "uppādenti": "उत्पन्न करना", "samāpajjanti": "प्रवेश करना",
    "uppannaṃ": "उत्पन्न हो चुका",                                # «उत्पन्न हो चुकी (ध्यान-अवस्था)»
    "dukkhassa": "दुःख", "sukhassa": "सुख",
    "arūpaṃ": "अभौतिक", "sampayuttake": "जुड़ा हुआ",
})

# --- instructions and abbreviations
_KAT = ("करना चाहिए", "बनाना चाहिए", "तैयार करना चाहिए")
T.update({k: _KAT for k in ("kātabbā", "kātabbaṃ", "kātabbo", "kātabbāni")})
T.update({
    "vibhajitabbaṃ": ("विश्लेषण करना चाहिए", "अलग-अलग दिखाना चाहिए"),
    "vibhajitabbā": ("विश्लेषण करना चाहिए", "अलग-अलग दिखाना चाहिए"),
    "vibhajantena": "विश्लेषण करते हुए",
    "bandhitabbaṃ": "बाँधना चाहिए", "cakkaṃ": "चक्र", "ekekampi": "एक-एक",
    "uddharitabbā": "निकालना चाहिए", "ninnetabbaṃ": "जोड़ना चाहिए", "labbhati": "मिलना",
    "niyāmetabbaṃ": "निश्चित करना चाहिए", "vajjetabbā": "छोड़ देना चाहिए", "jānitvā": "जानकर",
    "dassetabbāni": "दिखाना चाहिए", "dassetabbaṃ": "दिखाना चाहिए",
    "gaṇanā": "गणना", "gaṇanāpi": "गणना",
    "paripuṇṇā": ("पूर्ण", "पूरा"), "paripuṇṇaṃ": ("पूरा", "पूर्ण"),
    "anulomamātikā": ("सकारात्मक क्रम की मूल सूची", "सकारात्मक क्रम की सूची"),
    "ekāyeva": "एक ही", "cattāripi": "चारों", "tiṇṇampi": "तीनों", "dvinnampi": "दोनों",
    "tīsuyeva": "तीनों" + GAP + "ही",
    "agge": "सबसे पहले", "suddhake": "अकेला कारण", "majjhe": "बीच", "pacchā": "बाद",
    "ninnānākaraṇaṃ": "बिना किसी अंतर के", "ninnānākaraṇā": "बिना किसी अंतर के",
    "natthi": ("नहीं होना", "नहीं है", "नहीं"),
    "avasesā": ("बाकी", "शेष"),
})

# --- context-dependent keywords: value per Pāli occurrence (in Pāli order)
# katvā: «garuṃ katvā» = देकर (sample); «uposathakammaṃ katvā» = पालन करके (text «उपवास-व्रत का पालन करके»)
# rūpaṃ: «(dibbena cakkhunā) rūpaṃ passati» = दृश्य रूप; otherwise भौतिक रूप
# a rule is a regex over «<40 chars before>@@<40 chars after>», @@ = the keyword's position
# (value None = the ordinary table lookup for that occurrence)
# kātabba-: «mūlaṃ / mūlā / cakkaṃ / anulomamātikā kātabba-» = «… बनाना चाहिए» (text «मूल वाक्य बनाना चाहिए»,
# «चक्र बनाना चाहिए», «सूची बनानी चाहिए»); āhāraṃ: «kabaḷīkāraṃ āhāraṃ» = भोजन, the label in a list of
# condition subtypes («… pacchājātaṃ, āhāraṃ, indriyaṃ» = «…, आहार, क्षमता») = आहार.
_KB = [(r"(mūlaṃ|mūlā|cakkaṃ|anulomamātikā)\s*(\(|…pe…)?\s*@@", "बनाना चाहिए"), (r"@@", None)]
CTX = {
    "katvā": [(r"uposathakammaṃ\s*@@", "पालन करके"), (r"@@", "देकर")],
    "rūpaṃ": [(r"@@\s*passati", "दृश्य रूप"), (r"@@", "भौतिक रूप")],
    "kātabbaṃ": _KB, "kātabbā": _KB, "kātabbo": _KB, "kātabbāni": _KB,
    "āhāraṃ": [(r"kabaḷīkāraṃ\s*@@", "भोजन"), (r"jātaṃ,\s*@@", "आहार"), (r"@@", None)],
    "āhārassa": [(r"kabaḷīkārassa\s*@@", "भोजन"), (r"@@", None)],
    # ceva: «X ceva Y ca» = भी (text «X रूपी भी और … भी»); «X ceva no ca Y» = «…, पर स्वयं …» (no direct equivalent)
    "ceva": [(r"@@\s*no\s+ca", NDE), (r"@@", "भी")],
}
CTX_LOG = []


def ctx_values(kw, pali):
    rules = CTX[kw]
    out = []
    for m in re.finditer(r"(?<![^\W\d_])" + re.escape(kw) + r"(?![^\W\d_])", pali):
        win = pali[max(0, m.start() - 40): m.start()] + "@@" + pali[m.end(): m.end() + 40]
        for rx, v in rules:
            if re.search(rx, win):
                out.append(v)
                break
    return out


OVR = {f: {} for f in FILES}
OVR["3-03-asavagocchaka"].update({
    "7-26-54": {"paccayā": "कारण"},              # «sabbe paccayā vitthāretabbā» = «सभी कारणों का विस्तार» (noun)
})
OVR["3-04-sannojanagocchaka"].update({
    "7-U357": {"kātabbo": "तैयार करना चाहिए"},   # «… sampayuttavāropi kātabbo» = «… भी तैयार करना चाहिए»
})
OVR["3-05-ganthagocchaka"].update({
    "7-28-116": {"Ārammaṇañca": "विषय-कारण"},     # «Ārammaṇañca sahajātañca upanissayañca» = «विषय-कारण, सह-उत्पत्ति-कारण …»
})
ALLOWED = {f: {} for f in FILES}


def resolver_for(f):
    base = make_resolver(f, {**PI7, **T}, OVR[f])
    pa = read_pali(f)
    seen = collections.Counter()

    def res(bid, kw, kws):
        if kw in OVR[f].get(bid, {}) or kw not in CTX:
            return base(bid, kw, kws)
        seen[(bid, kw)] += 1
        vals = ctx_values(kw, pa.get(bid, ""))
        n = kws.count(kw)
        if len(set(vals)) <= 1:
            v = vals[0] if vals else None
        else:
            i = seen[(bid, kw)] - 1
            if len(vals) != n:
                CTX_LOG.append((f, bid, kw, n, vals))
            if n < len(vals):                   # fewer keywords than occurrences: the commonest real sense
                real = [x for x in vals if x not in (None, NDE)] or vals
                v = collections.Counter(real).most_common(1)[0][0]
            else:
                v = vals[i] if i < len(vals) else vals[0]
        return base(bid, kw, kws) if v is None else v
    return res


def ambiguity(f):
    """Tuple-valued keywords where more than one alternative is present in the segment's Hindi."""
    hi = read_hindi(f)
    tab = {**PI7, **T}
    out = collections.Counter()
    for bid, kws in read_keywords(f):
        for kw in set(kws):
            if kw in OVR[f].get(bid, {}):
                continue
            k = lc(kw)
            v = tab.get(k)
            if isinstance(v, tuple):
                pres = [a for a in v if a != NDE and present(a, hi.get(bid, ""))]
                pres = [a for a in pres if not any(a != b and a in b for b in pres)]
                if len(pres) > 1:
                    out[(kw, tuple(pres))] += 1
                    print("   AMB", f[:4], bid, kw, pres)
    return out


if __name__ == "__main__":
    for f in FILES:
        build_part(f, resolver_for(f))
        verify(f, allowed=ALLOWED[f])
    for c in CTX_LOG:
        print("   CTX count mismatch", *c)
    if "--amb" in sys.argv:
        for f in FILES:
            ambiguity(f)
    if "--audit" in sys.argv:
        for f in FILES:
            print("=" * 20, f)
            audit(f, {**PI7, **T}, OVR[f], only_fallback=True)
