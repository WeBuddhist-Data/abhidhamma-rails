"""Alignment pass for the pi-7 Hindi plain RAILS translation (Paṭṭhāna).

Applies fixed old -> new strings (kind "str"), regex patterns (kind "rx"), or functions (kind "fn": gets the Hindi
line, returns (line, n); "fnp": also gets the Pāli line) to the Hindi chapter files. A rule touches a Hindi line ONLY
when the aligned Pāli line (non-empty line i <-> non-empty line i) matches the rule's Pāli pattern, and only in the
files whose name starts with one of the rule's prefixes (None = all files).
Line counts, block IDs, heading levels, dashes and '[' counts are never touched (asserted per changed line).
Protected (user-approved, never changed): preamble.md, 1-00-paccaya.md, 1-01-kusalattika.md non-empty lines
1-190 and 1235-1262 (the sample).
Backup of the pre-pass files: backup-pre-align/ (made once, if missing). The pass always reads from the backup, so
rerunning it rebuilds the same output. Log: align-log.tsv (rule, file, replacements, lines).

usage: python -I -B -X utf8 align_rails_pi7.py [--dry]
"""
import os, re, sys, shutil, collections

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import ar7_common as C  # noqa: E402
from ar7_common import PARTS, PDIR, HDIR, BAK  # noqa: E402

PROTECTED = {"preamble": None, "1-00-paccaya": None, "1-01-kusalattika": [(1, 190), (1235, 1262)]}
DEV = "ऀ-ॣ०-ॿ"
E = r"(?![" + DEV + r"])"       # end of a Devanagari word
B = r"(?<![" + DEV + r"-])"      # start of a Devanagari word
VA = r"वा(ला|ली|ले)"

R = []  # (id, pali_regex, old, new, kind, prefixes)
REPORT = []  # lines a function rule had to skip


def rule(rid, pali, old, new, kind="str", files=None):
    R.append((rid, pali, old, new, kind, files))


# ============================================================================ 1. kātabba- = «करना चाहिए» (termbase)
KAT = r"[kK]ātabb|kattabb"
# Mūlaṃ kātabbaṃ (4-01 «मूल वाक्य से शुरू करना चाहिए») = «मूल वाक्य करना चाहिए» (3-xx «बनाना» with the termbase verb)
rule("K1-mulam-katabbam", r"[Mm]ūlaṃ kātabb", "मूल वाक्य से शुरू करना चाहिए", "मूल वाक्य करना चाहिए")
# Mūlaṃ pucchitabbaṃ = «मूल वाक्य पूछना चाहिए» (47 of 51; 4-01 «मूल वाक्य से पूछना चाहिए»)
rule("K1-mulam-pucchitabbam", r"[Mm]ūlaṃ pucchitabb", "मूल वाक्य से पूछना चाहिए", "मूल वाक्य पूछना चाहिए")
# anulomamātikā kātabbā: 3-xx «… मूल सूची बनानी चाहिए» (12) -> «करनी»; 4-01 «… मूल सूची के अनुसार करना चाहिए» (6)
rule("K2-anulomamatika", r"anulomamātikā kātabb", "मूल सूची के अनुसार करना चाहिए", "मूल सूची करनी चाहिए")
# kabaḷīkāro āhāro kātabbo: «भोजन करना» would read «to eat»; the object takes «को»
rule("K3-kabalikara", KAT, r"कौर-कौर खाया जाने वाला भोजन (?:बनाना|शामिल करना) चाहिए",
     "कौर-कौर खाए जाने वाले भोजन को करना चाहिए", "rx")
# (sabbe kātabbā): 3-02 «सब बनाने चाहिए» (4) -> «सब करने चाहिए»; 4-10 «सभी को शामिल करना चाहिए»
rule("K4-sabbe-katabba", r"\(sabbe kātabbā\)", "(सभी को शामिल करना चाहिए)", "(सब करने चाहिए)")
# the verb itself
rule("K5-katabba-verb", KAT, r"(?:तैयार|शामिल) (नहीं )?कर(ना|ने|नी) चाहिए", r"\1कर\2 चाहिए", "rx")
rule("K5-katabba-verb", KAT, B + r"(नहीं )?बना(ना|ने|नी) चाहिए", r"\1कर\2 चाहिए", "rx")
rule("K5-katabba-verb", r"agge kātabb", B + r"रख(ना|नी) चाहिए", r"कर\1 चाहिए", "rx")
rule("K5-katabba-verb", r"lokuttaraṃ na kātabb", "नहीं लेना चाहिए", "नहीं करना चाहिए")
# (ārabbha kātabbā), plural: «करने चाहिए» (3-05, 3-07, 3-09; 3-10 had «करना»)
rule("K6-arabbha-katabba", r"ārabbha kātabbā(?!\w)", "विषय बनाकर करना चाहिए", "विषय बनाकर करने चाहिए")
# navapi pañhā = «नौ के नौ प्रश्न» (3-10, 4-01; 3-09 «सभी नौ»)
rule("K7-navapi", r"navapi pañhā", "सभी नौ प्रश्न", "नौ के नौ प्रश्न")
# iminā kāraṇena = «इस तरीके से» (21 of 23)
rule("K8-imina-karanena", r"iminā kāraṇena", "इसी तरीके से", "इस तरीके से")

# ============================================================================ 2. editorial notes
# (evaṃ gaṇetabbaṃ) = «इसी तरह गिनना चाहिए» (122 of 181; evaṃ = «इसी तरह» elsewhere)
rule("N1-evam", r"evaṃ gaṇ", "इस तरह गिनना चाहिए", "इसी तरह गिनना चाहिए")
rule("N1-evam", r"evaṃ vitthār", "का इस तरह विस्तार", "का इसी तरह विस्तार")
# (Sabbattha vitthāro) = «हर जगह विस्तार» (4-21, 5-01 .. 5-04, 5-13; 129 of 168)
rule("N2-sabbattha-vitthara", r"[Ss]abbattha vitthāro", r"हर जगह विस्तार से(?=[।)]| ?\)|$)", "हर जगह विस्तार", "rx")
# Yathā kusalattike pañhāvārassa anulomampi … gaṇitaṃ = 4-02 .. 4-07 (72 of 83)
rule("N3-ganitam", r"paccanīyānulomampi [gn]aṇitaṃ",
     r"प्रश्नों के खंड का सकारात्मक क्रम(?: भी)?, नकारात्मक क्रम(?: भी)?, सकारात्मक-नकारात्मक क्रम(?: भी)? और "
     r"नकारात्मक-सकारात्मक क्रम भी गिना गया है",
     "प्रश्नों के खंड को सकारात्मक क्रम, नकारात्मक क्रम, सकारात्मक-नकारात्मक क्रम और नकारात्मक-सकारात्मक क्रम "
     "में भी गिना गया है", "rx")
# Sahajātavārepi…pe… (locative) = «सह-उत्पत्ति के खंड में भी…» (66 of 82)
rule("N4-varepi", r"[Ss]ahajātavārepi ?…", r"सह-उत्पत्ति के खंड(?= ?…)", "सह-उत्पत्ति के खंड में भी", "rx")
# Sahajātavārampi / -vāropi …pe… = «सह-उत्पत्ति का खंड भी…» (no verb) / «सह-उत्पत्ति के खंड का भी…» (vitthāretabba)
rule("N5-varampi", r"[Ss]ahajātavār(?:ampi|opi) ?…", r"सह-उत्पत्ति का खंड(?= ?…)", "सह-उत्पत्ति का खंड भी", "rx")
rule("N5-varampi", r"[Ss]ahajātavār(?:ampi|opi) ?…", r"सह-उत्पत्ति के खंड(?= ?…)", "सह-उत्पत्ति के खंड का भी", "rx")
# ārammaṇādhipatiyeva = «केवल विषय रूपी प्रधानता» (-yeva = «केवल X», 4-02 .. 4-07, 4-08 .. 4-15)
rule("N9-adhipatiyeva", r"ādhipatiyeva", r"([^\s(]+ रूपी प्रधानता) ही" + E, r"केवल \1", "rx")
rule("N10-purejatasadisa", r"purejātasadisaṃ", "पूर्व-उत्पत्ति के समान", "पूर्व-उत्पत्ति-कारण के समान")
rule("N11-tini-upanissaya", r"tīṇi upanissayā", "(तीनों प्रबल आश्रय)", "(तीन प्रबल आश्रय)")
rule("N12-sankhata-sadisa", r"[Ss]aṅkhataṃ sappaccayasadis|[Aa]saṅkhataṃ appaccayasadis",
     r"(अनिर्मित|निर्मित) परिघटना कारणों", r"\1 परिघटना, कारणों", "rx")
rule("N13-avipakam", r"\([Aa]vipākaṃ", "कर्म-फल-कारण के बिना –", "कर्म-फल-कारण रहित –")
rule("N14-paripunna", r"vibhajitabbāni paripuṇṇāni", "उनका पूरा-पूरा विश्लेषण", "उनका परिपूर्ण विश्लेषण")
rule("N15-varopi-vittharetabbo", r"^\(Sahajātavāropi paccayavāropi nissayavāropi saṃsaṭṭhavāropi sampayuttavāropi "
     r"vitthāretabbo\.\)",
     "(सह-उत्पत्ति का खंड, कारण का खंड, आश्रय का खंड, घुले-मिले होने का खंड और जुड़ाव का खंड भी विस्तार से देना चाहिए।)",
     "(सह-उत्पत्ति के खंड, कारण के खंड, आश्रय के खंड, घुले-मिले होने के खंड और जुड़ाव के खंड का भी विस्तार करना चाहिए।)")
# Evaṃ itare dve gaṇanāpi Xvāropi kātabbo = «इसी तरह बाकी दो गणनाएँ और X का खंड भी …» (3-09, 4-01: 30 of 37)
rule("N8-itare-dve", r"[Ii]tare dve gaṇanāpi", r"बाकी दो गणनाएँ भी(?= और )", "बाकी दो गणनाएँ", "rx")

PPAR = re.compile(r"\(([^()]*)\)")
NUM = re.compile(r"[\d.\s,=-]*")


def paren_pairs(p, h):
    """aligned (pāli inner, hindi match) note pairs; None if the counts differ"""
    ps = [m.group(1) for m in PPAR.finditer(p) if not NUM.fullmatch(m.group(1))]
    hs = [m for m in PPAR.finditer(h) if not NUM.fullmatch(m.group(1))]
    if len(ps) != len(hs):
        return None
    return list(zip(ps, hs))


VARS = re.compile(r"vār(?:ampi|opi|āpi)\b")


def sadisa_plural_fn(h, p, ctx):
    """«Xvārampi Yvārampi … paṭiccavārasadisaṃ/-ā» (no verb, several sections): «… के समान हैं» (formulas §10:
    «X-कारण और Y-कारण भी Z-कारण के समान हैं»)"""
    pp = paren_pairs(p, h)
    if pp is None:
        REPORT.append(("N6", ctx, "paren counts differ"))
        return h, 0
    out, n = h, 0
    for pi, m in reversed(pp):
        if len(VARS.findall(pi)) < 2 or "sadis" not in pi or re.search(r"vitthār|kātabb|vibhaj|gaṇet", pi):
            continue
        seg = m.group(0)
        seg2 = re.sub(r"के समान है(?=[।)])", "के समान हैं", seg)
        if seg2 != seg:
            out = out[:m.start()] + seg2 + out[m.end():]
            n += 1
    return out, n


rule("N6-sadisa-plural", r"vār(?:ampi|opi|āpi)\b.*vār(?:ampi|opi|āpi)\b.*sadis", None, sadisa_plural_fn, "fnp")


def fulllist_fn(h, p, ctx):
    """a full section list without …pe… («Sahajātavārampi paccayavārampi … sampayuttavārampi …»): «भी» / «का भी»
    once, after the last member, «और» before it (formulas §10; sample «…खंड और जुड़ाव का खंड भी …»)"""
    pp = paren_pairs(p, h)
    if pp is None:
        REPORT.append(("N7", ctx, "paren counts differ"))
        return h, 0
    out, n = h, 0
    for pi, m in reversed(pp):
        if len(VARS.findall(pi)) < 3 or "…" in pi:
            continue
        seg = m.group(0)
        # «भी» / «का भी» off every member that has a next member; the last member keeps it
        s = re.sub(r"(का खंड|गणनाएँ) भी(?=(?:, | और )[^,।()]*? का खंड)", r"\1", seg)
        s = re.sub(r"के खंड का भी(?=(?:, | और )[^,।()]*? के खंड)", "के खंड", s)
        if " और " not in s:
            ms = list(re.finditer(r", ((?:(?!, ).)*? (?:का खंड भी|के खंड का भी))", s))
            if ms:
                s = s[:ms[-1].start()] + " और " + ms[-1].group(1) + s[ms[-1].end():]
        if s != seg:
            out = out[:m.start()] + s + out[m.end():]
            n += 1
    return out, n


rule("N7-full-section-list", r"[Ss]ahajātavār(?:ampi|opi|āpi) paccayavār", None, fulllist_fn, "fnp")

# ============================================================================ 3. words without a termbase entry
rule("W1-pisunam", r"pisuṇaṃ bhaṇ", "चुगली की बात बोल", "चुगली की बातें बोल")
rule("W2-dhammapatisambhida", r"dhamma(?:p)?paṭisambhid", r"शिक्षा (का|के) विश्लेषणात्मक ज्ञान",
     r"परिघटनाओं \1 विश्लेषणात्मक ज्ञान", "rx")
rule("W3-sakabhande", r"[Ss]akabhaṇḍe|parabhaṇḍe", r"(अपनी|पराई) वस्तुओं के प्रति", r"\1 वस्तु के प्रति", "rx")
rule("W4-pariggahe", r"pariggahe", r"(?:अपने परिग्रह|अपने अधिकार की चीज़ों) के प्रति", "अपनी संपत्ति के प्रति", "rx")
rule("W4-pariggahe", r"pariggahe", r"(?:पराए परिग्रह|दूसरों के अधिकार की चीज़ों) के प्रति", "पराई संपत्ति के प्रति", "rx")
rule("W5-samapatti", r"anuppannaṃ samāpattiṃ uppādenti", "ध्यान-अवस्था को उत्पन्न करते हैं", "ध्यान-अवस्था उत्पन्न करते हैं")
# ^7-8-37: «khandhānaṃ» is not in the Pāli (user rule: as written): the adjectives as substantives
rule("W6-7-8-37", r"pacchimānaṃ pītisahagatānañca sukhasahagatānañca āsevana",
     "बाद-बाद के उल्लास के साथ होने वाले और सुख के साथ होने वाले समूहों के लिए",
     "बाद-बाद के उल्लास के साथ होने वालों के लिए और सुख के साथ होने वालों के लिए")

# ============================================================================ 4. items: termbase wording, no pi-1 comma
I = "(?i)"
rule("I1-avitakkavicaramatta", I + r"avitakka ?vicāramatt", "आरंभिक विचार से रहित, केवल सतत", "आरंभिक विचार से रहित केवल सतत")
rule("I2-nevadassanena", I + r"nevadassanena", "न सत्य-दर्शन से, न मानसिक अभ्यास से", "न सत्य-दर्शन से न मानसिक अभ्यास से")
rule("I3-nevavipaka", I + r"nevavipāka", "न कर्म-फल रूपी, न कर्म-फल उत्पन्न", "न कर्म-फल रूपी न कर्म-फल उत्पन्न")
rule("I4-anupadinnaanupadaniya", I + r"anupādinna", "न कर्म से उत्पन्न, न आसक्ति", "न कर्म से उत्पन्न न आसक्ति")
rule("I5-adukkhamasukha", I + r"adukkhamasukh", "न दुःखद, न सुखद", "न दुःखद न सुखद")
rule("I6-nevacayagami", I + r"neva ?ācaya|nevācaya", "न संचय की ओर, न संचय घटाने", "न संचय की ओर न संचय घटाने")
rule("I7-nevasekkha", I + r"nev[aā]sekkh", r"न सीखने के चरण (का|की|के), न सीखना पूरा", r"न सीखने के चरण \1 न सीखना पूरा",
     "rx")
rule("I8-anidassanasappatigha", I + r"anidassanasappaṭigh", r"दिखाई न देने " + VA + r", पर टकराव",
     r"दिखाई न देने वा\1 पर टकराव", "rx")
rule("I9-asamkilittha", I + r"asaṃkiliṭṭh|asaṅkiliṭṭh", r"क्लेशों से मलिन न होने " + VA + r", पर क्लेशों",
     r"क्लेशों से मलिन न होने वा\1 पर क्लेशों", "rx")
rule("I10-nahetusahetuka", I + r"nahetu ?sahetuk|nahetuṃ sahetuk", r"मूल रूपी न होने " + VA + r", पर मूल वा",
     r"मूल रूपी न होने वा\1 पर मूल वा", "rx")
rule("I11-vippayutta-niya", I + r"vippayutt", r"से अलग, पर (उनका|उसका|क्लेशों का) विषय", r"से अलग पर \1 विषय", "rx")
rule("I12-cittasamsattha3", I + r"cittasaṃsaṭṭhasamuṭṭhān(?:asahabh|ānuparivatt)",
     r"मन से (घुली-मिली|घुले-मिले|घुला-मिला), मन से उत्पन्न और", r"मन से \1 मन से उत्पन्न और", "rx")

# ============================================================================ 5. headings and names
rule("H1-2-6-heading", r"^#.*Sahajāta-paccaya-nissaya-saṃsaṭṭha-sampayuttavāro",
     "सह-उत्पत्ति का खंड, कारण का खंड, आश्रय का खंड, घुले-मिले होने का खंड और जुड़ाव का खंड",
     "सह-उत्पत्ति, कारण, आश्रय, घुले-मिले होने और जुड़ाव का खंड")
rule("H2-vedana-padam", r"^#.*[Vv]edanāyasampayuttapadaṃ", r"अनुभूति से जुड़ी परिघटना वाला पद", "अनुभूति से जुड़ा पद", "rx")
# «Xādidukāni / -ttikāni / -gocchakāni / -chagocchakāni» = termbase «<name> आदि» (saññojanādidukāni = «बंधन वाला
# दो का वर्गीकरण आदि», saññojanādigocchakāni = «बंधनों का वर्ग आदि», Saññojanādichagocchakāni = «बंधनों का वर्ग आदि
# छह वर्ग»)
ADI = r"ādiduk|ādittik|ādigocch|ādichagocch"
rule("H3-adi-names", ADI, r" आदि वाले दो-दो के वर्गीकरण" + E, " वाला दो का वर्गीकरण आदि", "rx")
rule("H3-adi-names", ADI, r" आदि वाले तीन-तीन के वर्गीकरण" + E, " वाला तीन का वर्गीकरण आदि", "rx")
rule("H3-adi-names", ADI, r" आदि के छह वर्ग" + E, " का वर्ग आदि छह वर्ग", "rx")
rule("H3-adi-names", ADI, r" आदि के वर्ग" + E, " का वर्ग आदि", "rx")
# «मन के मैलों का वर्ग के दो-दो के वर्गीकरण» (oblique)
rule("H4-gocchaka-oblique", r"gocchakāni", "का वर्ग के दो-दो के वर्गीकरण", "के वर्ग के दो-दो के वर्गीकरण")
# 5-10 opening «Hetudukaṃ» is the dyad title (5-04, 5-09/5-03 «Kusalattikaṃ»): termbase sense 1
rule("H5-hetudukam-title", r"^##### Hetudukaṃ", "मूल-कारण के साथ दो कारणों का मेल", "मूल वाला दो का वर्गीकरण", "str",
     ("5-10",))


# ============================================================================ 6. «X ceva na/no/nana/nano ca Y» = «X, पर स्वयं …»
CEVA_P = re.compile(r"(?:ceva|ñceva)\b( (?:na|no|nana|nano) ca\b)?")
CEVA_H = re.compile(r", पर स्वयं | भी और ")
AND2BUT = re.compile(r" भी और ((?:(?! भी" + E + r"| और ).)*? न होने वा(?:ली|ले|ला)(?: न होने वा(?:ली|ले|ला))?) भी" + E)


def ceva_fn(h, p, ctx):
    pe = [bool(m.group(1)) for m in CEVA_P.finditer(p)]
    he = list(CEVA_H.finditer(h))
    want = sum(pe)
    have = sum(1 for m in he if m.group(0).startswith(","))
    if want <= have:
        return h, 0
    if len(pe) != len(he):
        REPORT.append(("C1", ctx, f"ceva events pali {len(pe)} hindi {len(he)}"))
        return h, 0
    out, n = h, 0
    for is_but, m in reversed(list(zip(pe, he))):
        if is_but and not m.group(0).startswith(","):
            mm = AND2BUT.match(out, m.start())
            if not mm:
                REPORT.append(("C1", ctx, "no match at " + out[m.start():m.start() + 60]))
                continue
            out = out[:mm.start()] + ", पर स्वयं " + mm.group(1) + out[mm.end():]
            n += 1
    return out, n


rule("C1-ceva-na-ca", r"(?:ceva|ñceva) (?:na|no|nana|nano) ca\b", None, ceva_fn, "fnp")

# ============================================================================ 7. whole lines
# identical Pāli -> identical Hindi: (ref part, ref non-empty line, literal or None)
WL = [
]


# ============================================================================ runner
def nonempty_idx(lines):
    return [i for i, l in enumerate(lines) if l.strip()]


def dashes(t):
    return t.count("—") + t.count("–")


def protected(part, k):
    if part not in PROTECTED:
        return False
    rng = PROTECTED[part]
    return rng is None or any(a <= k + 1 <= b for a, b in rng)


def main(dry=False):
    if not os.path.isdir(BAK):
        os.makedirs(BAK)
        for part in PARTS:
            shutil.copy2(os.path.join(HDIR, part + ".md"), os.path.join(BAK, part + ".md"))
        print("backup made:", BAK)
    log = collections.defaultdict(lambda: [0, 0])  # (rid, part) -> [replacements, lines]
    changed_lines = collections.Counter()
    hit_idx = set()
    blocked = []
    comp = []
    for rid, p, old, new, kind, files in R:
        o = re.compile(old) if kind == "rx" else old
        comp.append((rid, re.compile(p), o, new, kind, files))
    data = {}
    for part in PARTS:
        pl = [l for l in open(os.path.join(PDIR, part + ".md"), encoding="utf-8-sig").read().splitlines() if l.strip()]
        raw = open(os.path.join(BAK, part + ".md"), encoding="utf-8").read()
        bom = raw.startswith("﻿")
        text = raw.lstrip("﻿")
        assert "\r" not in text, part
        el = text.split("\n")
        idx = nonempty_idx(el)
        assert len(idx) == len(pl), (part, len(idx), len(pl))
        orig = list(el)
        for k, li in enumerate(idx):
            p, e = pl[k], el[li]
            for ri, (rid, pr, old, new, kind, files) in enumerate(comp):
                if files and not part.startswith(files):
                    continue
                if not pr.search(p):
                    continue
                if kind == "fn":
                    e2, n = new(e, f"{part}:{k + 1}")
                elif kind == "fnp":
                    e2, n = new(e, p, f"{part}:{k + 1}")
                elif kind == "rx":
                    e2, n = old.subn(new, e)
                    if e2 == e:
                        n = 0
                else:
                    n = e.count(old)
                    e2 = e.replace(old, new)
                if n:
                    e = e2
                    hit_idx.add(ri)
                    log[(rid, part)][0] += n
                    log[(rid, part)][1] += 1
            el[li] = e
        data[part] = (pl, el, idx, orig, bom)

    def body(line):
        m = re.match(r"^(#*\s*\*?(?:[\d\-–]+\.\s*)?)(.*?)(\*?\s*(?:\(\d+\)\s*)?(?:\^[\w-]+)?\s*)$", line)
        return m.group(1), m.group(2), m.group(3)

    def pkey(p):
        return re.sub(r"\s+", " ", body(p)[1]).strip()

    wl_hit = set()
    for wi, (rpart, rline, lit) in enumerate(WL):
        rpl, rel, ridx, _, _ = data[rpart]
        key = pkey(rpl[rline - 1])
        canon = lit if lit else body(rel[ridx[rline - 1]])[1]
        for part in PARTS:
            pl, el, idx, _, _ = data[part]
            for k, li in enumerate(idx):
                if pkey(pl[k]) != key or "[" in el[li]:
                    continue
                a, b_, c = body(el[li])
                new = a + canon + c
                if new != el[li]:
                    el[li] = new
                    wl_hit.add(wi)
                    log[("W0-whole-line", part)][0] += 1
                    log[("W0-whole-line", part)][1] += 1
    for wi, w in enumerate(WL):
        if wi not in wl_hit:
            print("WL NO HIT:", w)
    for part in PARTS:
        pl, el, idx, orig, bom = data[part]
        for k, li in enumerate(idx):
            e, e0 = el[li], orig[li]
            if e != e0:
                if protected(part, k):
                    blocked.append((part, k + 1))
                    el[li] = e0
                    continue
                assert dashes(e) == dashes(e0), (part, k + 1, "dash count changed", e0, e)
                assert re.findall(r"\^[\w-]+\s*$", e) == re.findall(r"\^[\w-]+\s*$", e0), (part, k + 1, "block id")
                assert re.match(r"#*", e).group(0) == re.match(r"#*", e0).group(0), (part, k + 1, "heading")
                assert e.count("[") == e0.count("["), (part, k + 1, "brackets")
                changed_lines[part] += 1
        if not dry:
            out = ("﻿" if bom else "") + "\n".join(el)
            open(os.path.join(HDIR, part + ".md"), "w", encoding="utf-8", newline="\n").write(out)
    if not dry:
        with open(os.path.join(HERE, "align-log.tsv"), "w", encoding="utf-8") as f:
            f.write("rule\tfile\treplacements\tlines\n")
            for (rid, part), (n, l) in sorted(log.items(), key=lambda kv: (kv[0][0], PARTS.index(kv[0][1]))):
                f.write(f"{rid}\t{part}\t{n}\t{l}\n")
    tot = collections.defaultdict(lambda: [0, 0, set()])
    for (rid, part), (n, l) in log.items():
        tot[rid][0] += n
        tot[rid][1] += l
        tot[rid][2].add(part[:4])
    for rid in sorted(tot):
        print(f"{rid:28s} repl={tot[rid][0]:5d} lines={tot[rid][1]:5d} files={len(tot[rid][2])}")
    print("lines changed:", sum(changed_lines.values()), "in", len(changed_lines), "files")
    if blocked:
        print("BLOCKED (protected lines a rule would have changed):", blocked[:50], len(blocked))
    for ri, r in enumerate(R):
        if ri not in hit_idx:
            print("NO HIT:", r[0], "|", str(r[2])[:100])
    for x in REPORT:
        print("REPORT:", x)


if __name__ == "__main__":
    main(dry="--dry" in sys.argv)
