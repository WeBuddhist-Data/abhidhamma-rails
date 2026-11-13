"""Hindi plain zero-shot builder for pi-7 1-01-kusalattika.md (the whole wholesome triad).

Every Hindi line is composed from the approved frames in build_sample_hi.py (imported as S, never edited)
plus the fixed tables below, so identical Pāli always gives identical Hindi.

    python -I -B -X utf8 build_1-01_hi.py            # write the output file and check it
    python -I -B -X utf8 build_1-01_hi.py --check    # check only (no write)
    python -I -B -X utf8 build_1-01_hi.py --enginetest   # run the dependent-section engine on the sample lines

Sample lines (non-empty 1-128, 129-190, 1235-1262) are taken from S.build_s2/s3/s4 unchanged.
"""
import re
import sys
import unicodedata

HERE = r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi"
sys.path.insert(0, HERE)
import build_sample_hi as S  # noqa: E402

FNAME = "1-01-kusalattika.md"
PALI_TEXT = (S.PALI_DIR / FNAME).read_text(encoding="utf-8")
P = S.nonempty(PALI_TEXT)
OUT_PATH = S.HI_DIR / FNAME
K = S.COND_KEYS
NAME, ABL, NABL, INS, LOC, NLOC, NNAME, NNAME_OBL = (S.NAME, S.ABL, S.NABL, S.INS, S.LOC, S.NLOC,
                                                      S.NNAME, S.NNAME_OBL)


def body(n):
    """Pāli non-empty line n without its block ID."""
    return S.ID_RX.sub("", P[n - 1])


class Untranslated(ValueError):
    pass


LATIN = re.compile(r"[A-Za-zĀāĪīŪūṄṅÑñṬṭḌḍṆṇḶḷṂṃ]{2,}")
VAR_RX = re.compile(r"\[(?:पाठभेद|वर्तनी-भेद) \([^)]*\): [^\]]*\]")


def check_latin(h, where=""):
    rest = VAR_RX.sub("", h)
    m = LATIN.search(rest)
    if m:
        raise Untranslated(f"{where}: Latin left: {m.group(0)!r} in: {h[:300]}")
    return h


# =====================================================================================
# 1. Condition stems and helpers
# =====================================================================================
STEM_RX = "|".join(sorted(K, key=len, reverse=True))
NUM_EXTRA = {16: "सोलह", 17: "सत्रह", 18: "अठारह"}


def numword(n):
    return S.NUM_WORD.get(n) or NUM_EXTRA[n]


def cname(k, neg=False):
    return NNAME(k) if neg else NAME(k)


def cname_obl(k, neg=False):
    return NNAME_OBL(k) if neg else NAME(k)


def andjoin(xs):
    return xs[0] if len(xs) == 1 else ", ".join(xs[:-1]) + " और " + xs[-1]


def key_of(stem):
    """Pāli stem (any case, may carry na/no) -> (key, neg)."""
    s0 = stem[0].lower() + stem[1:]
    for s in (s0, s0 + "a"):
        for pre in ("na", "no"):
            if s.startswith(pre) and s[len(pre):] in K:
                return s[len(pre):], True
        if s in K:
            return s, False
    raise Untranslated(f"unknown condition stem {stem!r}")


# =====================================================================================
# 2. Headings
# =====================================================================================
GROUPW = {"dukaṃ": 2, "tikaṃ": 3, "catukkaṃ": 4, "pañcakaṃ": 5, "chakkaṃ": 6, "sattakaṃ": 7,
          "aṭṭhakaṃ": 8, "navakaṃ": 9, "dasakaṃ": 10, "ekādasakaṃ": 11, "dvādasakaṃ": 12,
          "terasakaṃ": 13, "cuddasakaṃ": 14, "pannarasakaṃ": 15, "soḷasakaṃ": 16, "sattarasakaṃ": 17,
          "aṭṭhārasakaṃ": 18, "vīsakaṃ": 20, "ekavīsakaṃ": 21, "bāvīsakaṃ": 22, "tevīsakaṃ": 23,
          "catuvīsakaṃ": 24}
SA_NOTE = {"sāsevanaṃ": S.SASEVANA, "savipākaṃ": S.SAVIPAKA,
           "sāhāraṃ": f"({NAME('āhāra')} सहित)", "saindriyaṃ": f"({NAME('indriya')} सहित)",
           "sakammaṃ": f"({NAME('kamma')} सहित)", "saupanissayaṃ": f"({NAME('upanissaya')} सहित)"}
HEAD_FIXED = {
    "Vibhaṅgavāro": S.VARA["vibhaṅga"], "Saṅkhyāvāro": S.VARA["saṅkhyā"], "Suddhaṃ": S.SUDDHA,
    "Paccayānulomaṃ": S.PACCAYANULOMA, "Paccayapaccanīyaṃ": S.PACCAYAPACCANIYA,
    "Paccayānulomapaccanīyaṃ": S.PACCAYANULOMAPACCANIYA,
    "Paccayapaccanīyānulomaṃ": S.PACCAYAPACCANIYANULOMA, "Anulomaṃ": S.ANULOMA,
    "Sahajātavāro": S.VARA["sahajāta"], "Paccayavāro": S.VARA["paccaya"], "Nissayavāro": S.VARA["nissaya"],
    "Saṃsaṭṭhavāro": S.VARA["saṃsaṭṭha"], "Sampayuttavāro": S.VARA["sampayutta"],
    "Pañhāvāro": S.VARA["pañhā"],
    "(2) Paccanīyuddhāro": "(2) नकारात्मक क्रम के लिए कारणों की छँटाई",
    "Tikādi": S.GROUP_HI(3) + " आदि", "Chakkādi": S.GROUP_HI(6) + " आदि",
    "Naadhipatyādi": NNAME("adhipati") + " आदि",
    "Atthiādidukādi": f"{NAME('atthi')} आदि के साथ दो कारणों के मेल आदि",
    "Namaggatikaṃ": f"{NNAME_OBL('magga')} के साथ तीन कारणों का मेल",   # source has -tikaṃ (slip?), kept
    # named ghaṭanā types
    "Sahajātachandādhipatighaṭanā": "सह-उत्पन्न प्रधान बनी हुई चाह के संयोजन",
    "Sahajāta-chandādhipatighaṭanā": "सह-उत्पन्न प्रधान बनी हुई चाह के संयोजन",
    "Cittādhipatighaṭanā": "प्रधान बने हुए मन के संयोजन",
    "Vīriyādhipatighaṭanā": "प्रधान बने हुए उत्साह के संयोजन",
    "Vīmaṃsādhipatighaṭanā": "प्रधान बनी हुई जाँच-परख के संयोजन",
    "Sāmaññaghaṭanā": "सामान्य संयोजन", "Pakiṇṇakaghaṭanā": "फुटकर संयोजन",
}

# combination-word parser (ghaṭanā names and the "...nti" lists). Sandhi forms first.
COMBO_PARTS = [("hetādhipati", ["hetu", "adhipati"]), ("ārammaṇādhipati", ["ārammaṇa", "adhipati"]),
               ("āhārādhipati", ["āhāra", "adhipati"]), ("ārammaṇūpanissaya", ["ārammaṇa", "upanissaya"]),
               ("adhipatyā", ["adhipati"])] + [(k, [k]) for k in K]
COMBO_PARTS += [(k[:-1] + "ādhipati", [k, "adhipati"]) for k in K if k.endswith("a")]
COMBO_PARTS.sort(key=lambda x: len(x[0]), reverse=True)


def parse_combo(word):
    """'Hetu-sahajātaaññamañña-nissaya-atthi-avigata' -> list of condition keys (hyphens optional)."""
    s = word.replace("ṃ-", "-").replace(" ", "").replace("-", "")   # 'vippayuttaṃ-avigata' (slip)
    s = s[0].lower() + s[1:]
    keys = []
    while s:
        for p, ks in COMBO_PARTS:
            if s.startswith(p):
                keys += ks
                s = s[len(p):]
                break
        else:
            raise Untranslated(f"cannot parse combination {word!r} at {s!r}")
    return keys


def combo_hi(keys):
    return andjoin([NAME(k) for k in keys]) + " के संयोजन"


def head_hi(t):
    if t in HEAD_FIXED:
        return HEAD_FIXED[t]
    m = re.fullmatch(r"(.*?)ghaṭanā(?: (\(\d+\)))?", t)
    if m:
        pre, num = m.group(1), m.group(2)
        tail = f" {num}" if num else ""
        if pre + "ghaṭanā" in HEAD_FIXED:
            return HEAD_FIXED[pre + "ghaṭanā"] + tail
        for suf, word in (("sāmañña", "सामान्य"), ("missaka", "मिश्रित"), ("pakiṇṇaka", "फुटकर")):
            if pre.endswith(suf):
                x = pre[: -len(suf)].rstrip("-")
                return f"{NAME(key_of(x)[0])} के {word} संयोजन{tail}"
        if pre.startswith(("Sa", "Sā")) and not pre.startswith(("Sahajāta", "Samanantara", "Sampayutta")):
            if pre.startswith("Sa"):
                keys = parse_combo(pre[2:])
            else:
                try:
                    keys = parse_combo("a" + pre[2:])
                except Untranslated:
                    keys = parse_combo("ā" + pre[2:])
            return f"{andjoin([NAME(k) for k in keys])} सहित संयोजन{tail}"
        return f"{NAME(key_of(pre)[0])} के संयोजन{tail}"
    m = re.fullmatch(r"(.*?)sabhāgaṃ", t)
    if m:
        return f"{NAME(key_of(m.group(1))[0])} के साथी कारण"
    m = re.fullmatch(r"(\w+)(?: \((\w+)\))?", t)
    if m and m.group(1).lower() in GROUPW:
        h = S.GROUP_HI(GROUPW[m.group(1).lower()]) if GROUPW[m.group(1).lower()] in S.NUM_WORD \
            else f"{numword(GROUPW[m.group(1).lower()])} कारणों का मेल"
        return h + (" " + SA_NOTE[m.group(2)] if m.group(2) else "")
    # condition names: Hetupaccayo / Nahetupaccayo
    m = re.fullmatch(r"(\w+)paccayo", t)
    if m:
        k, neg = key_of(m.group(1))
        return cname(k, neg)
    # X-Ypaccayā / X-Ydukāni
    m = re.fullmatch(r"(\w+)-(\w+?)(paccayā|dukāni)", t)
    if m:
        (k1, n1), (k2, n2) = key_of(m.group(1)), key_of(m.group(2))
        if m.group(3) == "paccayā":
            return f"{cname(k1, n1)} और {cname(k2, n2)}"
        return f"{cname_obl(k1, n1)} और {cname_obl(k2, n2)} के साथ दो कारणों के मेल"
    # Xādipaccayā / Xpaccayādi / Xādidukāni
    m = re.fullmatch(r"(\w+?)(?:ādipaccayā|paccayādi)", t)
    if m:
        k, neg = key_of(m.group(1))
        return cname(k, neg) + " आदि"
    m = re.fullmatch(r"(\w+?)ādidukāni", t)
    if m:
        k, neg = key_of(m.group(1))
        return f"{cname_obl(k, neg)} आदि के साथ दो कारणों के मेल"
    m = re.fullmatch(r"(\w+?)dukaṃ", t)
    if m:
        k, neg = key_of(m.group(1))
        return S.DUKANI(k, neg)
    raise Untranslated(f"heading {t!r}")


def heading_line(line):
    t = S.ID_RX.sub("", line)
    hashes = t[: len(t) - len(t.lstrip("#"))]
    inner = t.lstrip("#").strip()
    star = inner.startswith("*") and inner.endswith("*")
    core = inner.strip("*")
    h = head_hi(core)
    return f"{hashes} *{h}*" if star else f"{hashes} {h}"


# =====================================================================================
# 3. Notes in parentheses, closing lines
# =====================================================================================
def YATHA(x, verb="vit"):
    v = {"vit": "विस्तार करना चाहिए", "gan": "गिनना चाहिए"}[verb]
    return f"जैसे {x} में, वैसे ही {v}"


M_HETU, M_AR = S.MULAKA("hetu"), S.MULAKA("ārammaṇa")
M_NHETU = S.MULAKA("hetu", neg=True)
PATICCAVARE = "निर्भरता के खंड"
PACCAYAVARE = "कारण के खंड"
NOTES = {
    "Yathā hetumūlakaṃ, evaṃ vitthāretabbaṃ.": YATHA(M_HETU) + "।",
    "Yathā hetumūlakaṃ, evaṃ gaṇetabbaṃ.": YATHA(M_HETU, "gan") + "।",
    "Yathā ārammaṇamūlakaṃ, evaṃ vitthāretabbaṃ.": YATHA(M_AR) + "।",
    "ārammaṇamūlakaṃ yathā hetumūlakaṃ, evaṃ vitthāretabbaṃ.":
        f"{M_AR} का, जैसे {M_HETU} में, वैसे ही विस्तार करना चाहिए।",
    "Yathā nahetumūlakaṃ, evaṃ vitthāretabbaṃ.": YATHA(M_NHETU) + "।",
    "Yathā nahetumūlakaṃ, evaṃ vitthāretabbaṃ": YATHA(M_NHETU),
    "yathā nahetumūlakaṃ, evaṃ vitthāretabbaṃ": YATHA(M_NHETU),
    "Yathā nahetumūlakaṃ evaṃ vitthāretabbaṃ.": YATHA(M_NHETU) + "।",
    "Yathā nahetumūlakaṃ, evaṃ najhānamūlakaṃ vitthāretabbaṃ.":
        f"जैसे {M_NHETU} में, वैसे ही {S.MULAKA('jhāna', neg=True)} का विस्तार करना चाहिए।",
    "Yathā naaññamaññamūlakaṃ evaṃ vitthāretabbaṃ.": YATHA(S.MULAKA("aññamañña", neg=True)) + "।",
    "Yathā noatthimūlakaṃ, evaṃ vitthāretabbaṃ.": YATHA(S.MULAKA("atthi", neg=True)) + "।",
    "yathā nahetupaccayā, evaṃ vitthāretabbaṃ": YATHA(NNAME_OBL("hetu")),
    "Yathā hetupaccayaṃ, evaṃ vitthāretabbaṃ.": YATHA(NAME("hetu")) + "।",
    "Yathā ārammaṇapaccayaṃ, evaṃ vitthāretabbaṃ.": YATHA(NAME("ārammaṇa")) + "।",
    "Yathā sahajātapaccayaṃ, evaṃ vitthāretabbaṃ.": YATHA(NAME("sahajāta")) + "।",
    "Yathā anantarapaccayaṃ, evaṃ vitthāretabbaṃ.": YATHA(NAME("anantara")) + "।",
    "Yathā atthipaccayaṃ, evaṃ vitthāretabbaṃ.": YATHA(NAME("atthi")) + "।",
    "Yathā atthipaccayo vitthārito evaṃ avigatapaccayo vitthāretabbo.":
        f"जैसे {NAME('atthi')} का विस्तार किया गया है, वैसे ही {NAME('avigata')} का विस्तार करना चाहिए।",
    "Yathā anulome sahajātapaccayaṃ, evaṃ gaṇetabbaṃ.":
        f"जैसे {S.ANULOMA} के {NAME('sahajāta')} में, वैसे ही गिनना चाहिए।",
    "Yathā anulome sahajātapaccayaṃ, evaṃ vitthāretabbaṃ.":
        f"जैसे {S.ANULOMA} के {NAME('sahajāta')} में, वैसे ही विस्तार करना चाहिए।",
    "Yathā paṭiccavāre, evaṃ vitthāretabbaṃ.": YATHA(PATICCAVARE) + "।",
    "Yathā paṭiccavāre evaṃ vitthāretabbaṃ.": YATHA(PATICCAVARE) + "।",
    "Yathā paccayavāre, evaṃ vitthāretabbaṃ.": YATHA(PACCAYAVARE) + "।",
    "Yathā paṭiccavāre naārammaṇapaccayā, evaṃ vitthāretabbaṃ.":
        f"जैसे {PATICCAVARE} में {NLOC('ārammaṇa')}, वैसे ही विस्तार करना चाहिए।",
    "Yathā paṭiccavāragaṇanā, evaṃ gaṇetabbaṃ.": f"जैसे {PATICCAVARE} की गणना, वैसे ही गिनना चाहिए।",
    "Avasesaṃ yathā paṭiccavāre paccanīyaṃ, evaṃ vitthāretabbaṃ.":
        f"बाकी का, जैसे {PATICCAVARE} में {S.PACCANIYA}, वैसे ही विस्तार करना चाहिए।",
    "Anantarapaccayā samanantarapaccayā yathā ārammaṇapaccayā, evaṃ vitthāretabbā.":
        f"{NAME('anantara')} और {NAME('samanantara')} का, जैसे {NAME('ārammaṇa')} में, वैसे ही विस्तार करना चाहिए।",
    "Nissayapaccayā yathā sahajātamūlakaṃ. Upanissayapaccayā yathā ārammaṇamūlakaṃ.":
        f"{NAME('nissaya')} {S.MULAKA('sahajāta')} की तरह है। {NAME('upanissaya')} {M_AR} की तरह है।",
    "Nissayapaccayā yathā sahajātapaccayā.": f"{NAME('nissaya')} {NAME('sahajāta')} की तरह है।",
    "Indriyapaccayā yathā kammapaccayā, evaṃ vitthāretabbaṃ.":
        f"{NAME('indriya')} का, जैसे {NAME('kamma')} में, वैसे ही विस्तार करना चाहिए।",
    "Jhānapaccayāpi maggapaccayāpi yathā hetupaccayā, evaṃ vitthāretabbaṃ.":
        f"{NAME('jhāna')} का भी और {NAME('magga')} का भी, जैसे {NAME('hetu')} में, वैसे ही विस्तार करना चाहिए।",
    "Hetumūlakaṃ vitthāretabbaṃ.": f"{M_HETU} का विस्तार करना चाहिए।",
    "Vipākaṃ ṭhapetvā sabbattha vitthāretabbaṃ.": f"{NAME('vipāka')} को छोड़कर हर जगह विस्तार करना चाहिए।",
    "Avasesāni padāni etenupāyena vitthāretabbāni. Saṃkhittaṃ.":
        "बाकी पदों का इसी तरीके से विस्तार करना चाहिए। संक्षिप्त।",
    "Sabbāni padāni hetumūlakasadisāni": f"सभी पद {M_HETU} के समान हैं",
    "Imāni padāni hetupaccayasadisāni.": f"ये पद {S.SADISA('hetu')} हैं।",
    "imāni tīṇi mūlāni ekasadisāni": "ये तीन शृंखलाएँ एक जैसी हैं",
    "Saṃkhittaṃ.": "संक्षिप्त।", "Saṃkhittaṃ": "संक्षिप्त", "saṃkhittaṃ": "संक्षिप्त",
    "saṃkhittaṃ.": "संक्षिप्त।", "saṃkhittaṃ. Paripuṇṇaṃ.": "संक्षिप्त। पूर्ण।",
    "Paripuṇṇaṃ.": "पूर्ण।", "kātabbaṃ": "करना चाहिए",
    "abyākataṃ paripuṇṇaṃ kātabbaṃ": "नैतिक रूप से अनिर्धारित को पूर्ण करना चाहिए",
    "mūlakaṃ saṃkhittaṃ": "शृंखला संक्षिप्त",
    "Cakkaṃ bandhitabbaṃ.": "चक्र बाँधना चाहिए।", "Cakkaṃ kātabbaṃ.": "चक्र बनाना चाहिए।",
    "sabbattha ekaṃ": "हर जगह एक", "sabbattha dve": "हर जगह दो", "sabbattha satta": "हर जगह सात",
    "Paṭiccattaṃ nāma sahajātattaṃ, sahajātattaṃ nāma paṭiccattaṃ.":
        "निर्भरता का अर्थ है सह-उत्पत्ति, सह-उत्पत्ति का अर्थ है निर्भरता।",
    "Paccayattaṃ nāma nissayattaṃ, nissayattaṃ nāma paccayattaṃ.":
        "कारण होने का अर्थ है आश्रय होना, आश्रय होने का अर्थ है कारण होना।",
    "Saṃsaṭṭhattaṃ nāma sampayuttattaṃ, sampayuttattaṃ nāma saṃsaṭṭhattaṃ.":
        "घुले-मिले होने का अर्थ है जुड़ा होना, जुड़े होने का अर्थ है घुले-मिले होना।",
    "Saṃsaṭṭhavāre paccanīyavibhaṅge nakamme ca navipāke ca paṭisandhi natthi; avasesesu sabbattha atthi.":
        (f"{S.VARA['saṃsaṭṭha'].replace(' का खंड', ' के खंड')} के नकारात्मक विश्लेषण में {NLOC('kamma')} भी और "
         f"{NLOC('vipāka')} भी "
         "पुनर्जन्म नहीं है; बाकी सब जगह है।"),
    "adhipati paṭisandhikkhaṇe natthi.": "पुनर्जन्म के क्षण में प्रधानता नहीं है।",
    "Navippayutte paṭisandhi natthi.": f"{NLOC('vippayutta')} पुनर्जन्म नहीं है।",
    "Na jhāne idaṃ nānākaraṇaṃ.": f"{NLOC('jhāna')} यह अंतर है।",
    "Namagge idaṃ nānākaraṇaṃ.": f"{NLOC('magga')} यह अंतर है।",
    "Navipākamūlake idaṃ nānākaraṇaṃ, avasesāni yathā nahetumūlakaṃ.":
        f"{S.MULAKA('vipāka', neg=True)} में यह अंतर है, बाकी {M_NHETU} की तरह हैं।",
    "Naindriyapaccayā kamme satta pañhā.": f"{NABL('indriya')}, {LOC('kamma')} सात प्रश्न हैं।",
    "Naadhipatimūlakaṃ nahetumhi ṭhitena nahetumūlakasadisaṃ kātabbaṃ.":
        (f"{S.MULAKA('adhipati', neg=True)} को, {NNAME_OBL('hetu')} पर टिके रहने पर, {M_NHETU} के समान "
         "करना चाहिए।"),
    "Yāvāsevanā sabbaṃ sadisaṃ, nakamme gaṇite pañca pañhā honti.":
        f"{NAME('āsevana')} तक सब समान है, {NNAME('kamma')} को गिनने पर पाँच प्रश्न होते हैं।",
    "Natthipaccayampi vigatapaccayampi anantarapaccayasadisaṃ.":
        f"{NAME('natthi')} भी और {NAME('vigata')} भी {S.SADISA('anantara')} हैं।",
    "Navipākaṃ namaggaṃ navippayuttaṃ nakammapaccayasadisaṃ.":
        (f"{NNAME('vipāka')}, {NNAME('magga')} और {NNAME('vippayutta')} "
         f"{S.SADISA('kamma', neg=True)} हैं।"),
    "Upanissayapaccayā ārammaṇapaccayasadisaṃ.": f"{NAME('upanissaya')} {S.SADISA('ārammaṇa')} है।",
    "atthipaccayā sahajātapaccayasadisaṃ kātabbaṃ. Natthipaccayā vigatapaccayā ārammaṇapaccayasadisaṃ, "
    "avigatapaccayā sahajātapaccayasadisaṃ.":
        (f"{NAME('atthi')} को {S.SADISA('sahajāta')} करना चाहिए। {NAME('natthi')} और {NAME('vigata')} "
         f"{S.SADISA('ārammaṇa')} हैं, {NAME('avigata')} {S.SADISA('sahajāta')} है।"),
    "napacchājātapaccayampi naāsevanapaccayampi paripuṇṇaṃ, sattarasa.":
        f"{NNAME('pacchājāta')} भी और {NNAME('āsevana')} भी पूर्ण है, सत्रह।",
    "naāsevanapaccayamūlakampi nahetumūlakasadisaṃ.":
        f"{S.MULAKA('āsevana', neg=True)} भी {M_NHETU} के समान है।",
    "Sabbāni padāni vitthāretabbāni, imāni alikhitesu padesu tīṇi pañhā. Napurejātamūlake nahetuyā ṭhitena "
    "āsevane ca magge ca eko pañho kātabbo, avasesāni nahetupaccayasadisāni. Napacchājātapaccayā paripuṇṇaṃ "
    "naadhipatipaccayasadisaṃ.":
        (f"सभी पदों का विस्तार करना चाहिए, इन न लिखे गए पदों में तीन प्रश्न हैं। "
         f"{S.MULAKA('purejāta', neg=True)} में, {NNAME_OBL('hetu')} पर टिके रहने पर, {LOC('āsevana')} भी और "
         f"{LOC('magga')} भी एक प्रश्न करना चाहिए, बाकी {S.SADISA('hetu', neg=True)} हैं। "
         f"{NNAME('pacchājāta')} पूर्ण है, {S.SADISA('adhipati', neg=True)} है।"),
    "Avipākaṃ – 1": "कर्म-फल-कारण रहित – 1",
}
for _n in range(1, 6):
    NOTES[f"Avipākaṃ – {_n}"] = f"कर्म-फल-कारण रहित – {_n}"
    NOTES[f"Savipākaṃ – {_n}"] = f"{S.SAVIPAKA[1:-1]} – {_n}"
for _k in K:
    for _neg in (False, True):
        _p = ("no" if _k in ("atthi", "natthi", "vigata", "avigata") else "na") if _neg else ""
        _pali = f"{_p}{_k}paccayasadisaṃ"
        _hi = f"{S.SADISA(_k, neg=_neg)} है"
        NOTES[_pali] = _hi
        NOTES[_pali[0].upper() + _pali[1:] + "."] = _hi + "।"

VARIANTS = {"{āruppe (sabbattha)}": "[पाठभेद (सब जगह): āruppe]",
            "{pahīnakilese (syā.)}": "[वर्तनी-भेद (Syā.): pahīnakilese]",
            "{vikkhambhitakilese (syā.)}": "[वर्तनी-भेद (Syā.): vikkhambhitakilese]",
            "{nānākhaṇikā (ka.)}": "[वर्तनी-भेद (Ka.): nānākhaṇikā]",
            "{nahetumūlake (syā.)}": "[पाठभेद (Syā.): nahetumūlake]"}


NOTES.update({   # notes as rendered in the approved sample (build_sample_hi.py)
    "Ime tevīsatipaccayā sajjhāyantena vitthāretabbā.": "इन तेईस कारणों का पाठ करते हुए विस्तार करना चाहिए।",
    "Ārammaṇe ṭhitena sabbattha tīṇeva pañhā.": "विषय-कारण पर टिके रहने पर हर जगह तीन ही प्रश्न हैं।",
    "Āsevanamūlake vipākaṃ natthi.": f"{S.MULAKA('āsevana')} में {NAME('vipāka')} नहीं है।",
    "Vipākamūlake āsevanaṃ natthi.": f"{S.MULAKA('vipāka')} में {NAME('āsevana')} नहीं है।",
    "Ekekaṃ paccayaṃ mūlakaṃ kātūna sajjhāyantena gaṇetabbāti.":
        "एक-एक कारण को शुरुआत बनाकर पाठ करते हुए गिनना चाहिए।",
    "Saṅkhitaṃ.": "संक्षिप्त।",
})
_SUBJ = r"([A-Za-zāīūṃṅñṭḍṇḷĀ]+?)(?:paccaya)?"


def _pat_note(inner):
    m = re.fullmatch(_SUBJ + r"ṃ (\w+?)paccayasadisaṃ(\.?)", inner)
    if m:
        k, neg = key_of(m.group(1))
        k2, neg2 = key_of(m.group(2))
        return f"{cname(k, neg)} {S.SADISA(k2, neg2)} है" + ("।" if m.group(3) else "")
    m = re.fullmatch(_SUBJ + r"mpi " + _SUBJ + r"mpi (\w+?)paccayasadisaṃ(\.?)", inner)
    if m:
        (k, n), (k2, n2), (k3, n3) = key_of(m.group(1)), key_of(m.group(2)), key_of(m.group(3))
        return f"{cname(k, n)} भी और {cname(k2, n2)} भी {S.SADISA(k3, n3)} हैं" + ("।" if m.group(4) else "")
    return None


def note_hi(inner):
    if inner in NOTES:
        return NOTES[inner]
    h = _pat_note(inner)
    if h:
        return h
    parts = re.split(r"(?<=\.) ", inner)
    if len(parts) > 1:
        out = []
        for p in parts:
            out.append(NOTES.get(p) or _pat_note(p) or "")
            if not out[-1]:
                raise Untranslated(f"note ({inner}) part {p!r}")
        return " ".join(out)
    raise Untranslated(f"note ({inner})")


PANHA_OBL = S.VARA["pañhā"].replace(" का खंड", " के खंड")   # प्रश्नों के खंड
CLOSE = {
    "Paccanīyaṃ": S.PACCANIYA, "Paccanīyaṃ.": S.PACCANIYA + "।", "Anulomaṃ.": S.ANULOMA + "।",
    "Anulomapaccanīyaṃ.": S.ANULOMAPACCANIYA + "।", "Paccanīyānulomaṃ.": S.PACCANIYANULOMA + "।",
    "Anulomapaccanīyagaṇanā.": f"{S.ANULOMAPACCANIYA} की गणना।",
    "Paṭiccavāro.": S.VARA["paṭicca"] + "।", "Sahajātavāro.": S.VARA["sahajāta"] + "।",
    "Paccayavāro.": S.VARA["paccaya"] + "।", "Nissayavāro.": S.VARA["nissaya"] + "।",
    "Saṃsaṭṭhavāro.": S.VARA["saṃsaṭṭha"] + "।", "Sampayuttavāro.": S.VARA["sampayutta"] + "।",
    "Pañhāvārassa vibhaṅgo.": f"{PANHA_OBL} का विश्लेषण।",
    "Pañhāvārassa anulomagaṇanā.": f"{PANHA_OBL} में {S.ANULOMA} की गणना।",
    "Pañhāvārassa paccanīyuddhāro.": f"{PANHA_OBL} में नकारात्मक क्रम के लिए कारणों की छँटाई।",
    "Pañhāvārassa paccanīyagaṇanā.": f"{PANHA_OBL} में {S.PACCANIYA} की गणना।",
    "Pañhāvārassa anulomapaccanīyaṃ.": f"{PANHA_OBL} में {S.ANULOMAPACCANIYA}।",
    "Pañhāvārassa paccanīyānulomaṃ.": f"{PANHA_OBL} में {S.PACCANIYANULOMA}।",
    "Kusalattikaṃ niṭṭhitaṃ.": f"{S.TIKA('हितकर')} समाप्त।",
}
for _v, _vk in (("Paccayavāre", "paccaya"), ("Nissayavāre", "nissaya"), ("Saṃsaṭṭhavāre", "saṃsaṭṭha"),
                ("Sampayuttavāre", "sampayutta"), ("Sahajātavāre", "sahajāta"), ("Paṭiccavāre", "paṭicca")):
    _loc = S.VARA[_vk].replace(" का खंड", " के खंड") + " में"
    for _w, _h in (("anulomaṃ", S.ANULOMA), ("paccanīyaṃ", S.PACCANIYA),
                   ("anulomapaccanīyaṃ", S.ANULOMAPACCANIYA), ("paccanīyānulomaṃ", S.PACCANIYANULOMA)):
        CLOSE[f"{_v} {_w}."] = f"{_loc} {_h}।"
for _k in K:
    for _neg in (False, True):
        _p = ("no" if _k in ("atthi", "natthi", "vigata", "avigata") else "na") if _neg else ""
        _w = f"{_p}{_k}mūlakaṃ"
        CLOSE[_w[0].upper() + _w[1:] + "."] = S.MULAKA(_k, _neg) + "।"
        CLOSE[_w[0].upper() + _w[1:]] = S.MULAKA(_k, _neg)


# =====================================================================================
# 4. Counting lines (extends S.count_hi: notes, combinations, mūlaka words, several sentences)
# =====================================================================================
_ABL_RX = re.compile(r"^(?:(na|no)[\s-]?)?(" + STEM_RX + r")paccayā$")
_LOC2KEY = {v: k for k, v in S.COND_LOC_PALI.items()}
_LOC_RX = re.compile(r"^(?:(na|no)[\s-]?)?(" + "|".join(sorted(_LOC2KEY, key=len, reverse=True)) + r")$")
NUMX = dict(S.NUM)
NUMX.update({"soḷasa": "सोलह", "sattarasa": "सत्रह", "aṭṭhārasa": "अठारह", "sattaṃ": "सात"})
SLIP_TOKENS = {"sattaṃ": "satta (spelling)", "na-ārammaṇe": "naārammaṇe (hyphen)",
               "-paccayā": "X-paccayā (hyphen)", "naṃindriye": "naindriye (spelling)",
               "no avigate": "noavigate (space)", "Avigata āhāra-": "Avigata-āhāra (space for hyphen)", "ṃ-": "stray ṃ before a hyphen in a combination",
               "nadhipatipaccayā": "naadhipatipaccayā (elision)"}
SEEN_SLIPS = []


def _classify(tok):
    low = tok[0].lower() + tok[1:]
    if low in ("nadhipatipaccayā",):
        return "neg_abl", "adhipati"
    m = _ABL_RX.match(low)
    if m:
        return ("neg_abl" if m.group(1) else "abl"), m.group(2)
    m = _LOC_RX.match(low)
    if m:
        return ("neg_loc" if m.group(1) else "loc"), _LOC2KEY[m.group(2)]
    if low in NUMX:
        return "num", low
    if "-" in low and low.endswith("ti"):
        base = low[:-3] + "i" if low.endswith("īti") else (low[:-3] if low.endswith("nti") else low[:-2])
        return "combo", parse_combo(base)
    w = tok
    if w in CLOSE:
        return "word", CLOSE[w]
    raise Untranslated(f"count word {tok!r}")


def count_line(pali):
    """Translate a counting line. Raises Untranslated if something is unknown."""
    s = pali.strip()
    for slip in SLIP_TOKENS:
        if slip in s:
            SEEN_SLIPS.append(slip)
    s = re.sub(r"(?<=\w) +-(?=\w)", "-", s)
    s = re.sub(r"(?<=\w)- +(?=\w)", "-", s)
    s = s.replace("na-ārammaṇe", "naārammaṇe").replace("-paccayā", "paccayā").replace("naṃindriye", "naindriye")
    s = s.replace(" no avigate", " noavigate").replace("Avigata āhāra-", "Avigata-āhāra-")
    notes = []

    def _note(m):
        inner = m.group(1)
        if re.fullmatch(r"\d+", inner):
            notes.append(f"({inner})")
        else:
            notes.append(f"({note_hi(inner)})")
        return f" ⟦{len(notes) - 1}⟧ "

    s = re.sub(r"\(([^()]*)\)", _note, s)
    toks = re.findall(r"⟦\d+⟧|…pe…|…|[,;.]|na [^\s,;.…⟦]+|[^\s,;.…⟦]+", s)
    items = []
    for t in toks:
        if t in ("…pe…", "…"):
            items.append(("ell", "…"))
        elif t.startswith("⟦"):
            items.append(("paren", notes[int(t[1:-1])]))
        elif t in ",;.":
            items.append(("punct", t))
        else:
            items.append(_classify(t.replace("na ", "na")))
    words = ("abl", "neg_abl", "loc", "neg_loc", "num", "paren", "combo", "word")
    out = ""
    for i, (kind, v) in enumerate(items):
        nxt = items[i + 1][0] if i + 1 < len(items) else None
        if kind in words:
            if kind == "abl":
                text = ABL(v)
            elif kind == "neg_abl":
                text = NABL(v)
            elif kind == "loc":
                text = LOC(v)
            elif kind == "neg_loc":
                text = NLOC(v)
            elif kind == "num":
                text = NUMX[v]
            elif kind == "combo":
                text = combo_hi(v) + (" में" if nxt == "num" else " से")
            else:
                text = v
            if (kind in ("abl", "neg_abl", "num") or (kind == "combo" and nxt != "num")) and \
                    nxt in ("abl", "neg_abl", "loc", "neg_loc", "num", "combo"):
                text += ","
            if out and not out.endswith(" "):
                out += " "
            out += text
        else:
            if kind == "ell":
                out = out.rstrip(" ").rstrip(",") + "…"
            elif v == ".":
                out = out.rstrip(" ").rstrip(",") + "।"
            else:
                out = out.rstrip(" ") + v
    return out.strip()


# =====================================================================================
# 5. The engine for the dependent sections (sahajāta / paccaya / nissaya / saṃsaṭṭha / sampayutta)
# =====================================================================================
ITEM_STEM = {"k": "kusal", "a": "akusal", "ab": "abyākat"}
ITEM_LISTS = [["k"], ["a"], ["ab"], ["k", "ab"], ["a", "ab"], ["k", "a"], ["k", "a", "ab"]]
CSR, KTR, UPR = S.CSR, S.KTR, S.UPR
VK_SG, VK_PL, VAB, KAB = S.VK_SG, S.VK_PL, S.VIPAKA_ABY, S.KIRIYA_ABY

# (pāli phrase, direct form, oblique form or None = same)
NP = [
    ("kusalaṃ ekaṃ khandhaṃ", "एक हितकर समूह"), ("akusalaṃ ekaṃ khandhaṃ", "एक हानिकर समूह"),
    ("vipākābyākataṃ kiriyābyākataṃ ekaṃ khandhaṃ", f"{VK_SG} एक समूह"),
    ("ahetukaṃ vipākābyākataṃ kiriyābyākataṃ ekaṃ khandhaṃ", f"{S.AHETUKA}, {VK_SG} एक समूह"),
    ("vipākābyākataṃ ekaṃ khandhaṃ", f"{VAB} एक समूह"), ("kiriyābyākataṃ ekaṃ khandhaṃ", f"{KAB} एक समूह"),
    ("vipākābyākataṃ", VAB),
    ("pañcaviññāṇasahagataṃ ekaṃ khandhaṃ", S.KH_FIRST["pancavinnana"]),
    ("ekaṃ khandhaṃ", "एक समूह"),
    ("kusalaṃ ekaṃ khandhañca vatthuñca", "एक हितकर समूह और आधार", "एक हितकर समूह और आधार"),
    ("akusalaṃ ekaṃ khandhañca vatthuñca", "एक हानिकर समूह और आधार"),
    ("vipākābyākataṃ ekaṃ khandhañca vatthuñca", f"{VAB} एक समूह और आधार"),
    ("tayo khandhe ca vatthuñca", "तीन समूह और आधार", "तीन समूहों और आधार"),
    ("dve khandhe ca vatthuñca", "दो समूह और आधार", "दो समूहों और आधार"),
    ("tayo khandhā", "तीन समूह"), ("tayo khandhe", "तीन समूह", "तीन समूहों"), ("eko khandho", "एक समूह"),
    ("dve khandha", "दो समूह", "दो समूहों"),   # source slip (line 945) for dve khandhe
    ("dve khandhe", "दो समूह", "दो समूहों"), ("dve khandhā", "दो समूह"),
    ("kusale khandhe ca mahābhūte ca", "हितकर समूह और महाभूत", "हितकर समूहों और महाभूतों"),
    ("akusale khandhe ca mahābhūte ca", "हानिकर समूह और महाभूत", "हानिकर समूहों और महाभूतों"),
    ("kusale khandhe ca vatthuñca", "हितकर समूह और आधार", "हितकर समूहों और आधार"),
    ("akusale khandhe ca vatthuñca", "हानिकर समूह और आधार", "हानिकर समूहों और आधार"),
    ("vicikicchāsahagate uddhaccasahagate khandhe ca vatthuñca", "",
     f"{S.KHANDHE_VU} और आधार"),
    ("kusale khandhe", "हितकर समूह", "हितकर समूहों"), ("akusale khandhe", "हानिकर समूह", "हानिकर समूहों"),
    ("vipākābyākate kiriyābyākate khandhe", f"{VK_PL} समूह", f"{VK_PL} समूहों"),
    ("vipākābyākate khandhe", f"{VAB} समूह", f"{VAB} समूहों"),
    ("kiriyābyākate khandhe", f"{KAB} समूह", f"{KAB} समूहों"),
    ("vicikicchāsahagate uddhaccasahagate khandhe", "", S.KHANDHE_VU),
    ("vicikicchāsahagato uddhaccasahagato moho", S.MOHA_VU),
    ("khandhe", "समूह", "समूहों"), ("khandhā", "समूह"),
    ("kusalā khandhā", "हितकर समूह"), ("akusalā khandhā", "हानिकर समूह"),
    ("vipākābyākatā kiriyābyākatā khandhā", f"{VK_PL} समूह"),
    ("ahetukā vipākābyākatā kiriyābyākatā khandhā", f"{S.AHETUKA}, {VK_PL} समूह"),
    ("ahetukavipākābyākatā kiriyābyākatā khandhā", f"{S.AHETUKA}, {VK_PL} समूह"),
    ("vipākābyākatā khandhā", f"{VAB} समूह"), ("kiriyābyākatā khandhā", f"{KAB} समूह"),
    ("kusalā cetanā", f"हितकर {S.CETANA}"), ("akusalā cetanā", f"हानिकर {S.CETANA}"),
    ("kiriyābyākatā cetanā", f"{KAB} {S.CETANA}"),
    ("cittasamuṭṭhānañca rūpaṃ", S.AND_CSR), ("kaṭattā ca rūpaṃ", S.AND_KTR), ("vatthu ca", "और आधार"),
    ("cittasamuṭṭhānaṃ rūpaṃ kaṭattārūpaṃ upādārūpaṃ", f"{CSR}, {KTR}, {UPR}"),
    ("cittasamuṭṭhānaṃ rūpaṃ upādārūpaṃ", f"{CSR}, {UPR}"),
    ("kaṭattārūpaṃ upādārūpaṃ", f"{KTR}, {UPR}"),
    ("cittasamuṭṭhānaṃ rūpaṃ", CSR), ("kaṭattārūpaṃ", KTR), ("upādārūpaṃ", UPR),
    ("rūpajīvitindriyaṃ", S.RUPAJIVITINDRIYA),
    ("vatthu", "आधार"), ("vatthuṃ", "आधार"),
    ("bāhiraṃ ekaṃ mahābhūtaṃ", f"एक {S.BAHIRA} महाभूत"),
    ("ekaṃ mahābhūtaṃ", "एक महाभूत"), ("tayo mahābhūtā", "तीन महाभूत"),
    ("tayo mahābhūte", "तीन महाभूत", "तीन महाभूतों"), ("dve mahābhūte", "दो महाभूत", "दो महाभूतों"),
    ("dve mahābhūtā", "दो महाभूत"), ("mahābhūte", "महाभूत", "महाभूतों"), ("mahābhūtā", "महाभूत"),
    ("bāhire mahābhūte", f"{S.BAHIRA} महाभूत", f"{S.BAHIRA} महाभूतों"),
    ("āhārasamuṭṭhāne mahābhūte", f"{S.AHARASAM} महाभूत", f"{S.AHARASAM} महाभूतों"),
    ("utusamuṭṭhāne mahābhūte", f"{S.UTUSAM} महाभूत", f"{S.UTUSAM} महाभूतों"),
    ("bāhiraṃ", S.BAHIRA), ("āhārasamuṭṭhānaṃ", S.AHARASAM), ("utusamuṭṭhānaṃ", S.UTUSAM),
    ("asaññasattānaṃ", S.ASANNASATTA), ("arūpe", S.ARUPE),
    ("paṭisandhikkhaṇe", S.PATISANDHI), ("ahetukapaṭisandhikkhaṇe", S.AHETUKA_PATISANDHI),
]
for _s in S.SENSES:
    _pa = {"cakkhu": "cakkh", "sota": "sot", "ghāna": "ghān", "jivhā": "jivh", "kāya": "kāy"}[_s]
    NP.append((f"{_pa}āyatanaṃ", S.AYA_SENSE(_s), S.AYA_SENSE(_s).replace(" का ", " के ")))
    NP.append((f"{_s}viññāṇaṃ", S.VINNANA(_s)))
for _il in ITEM_LISTS:
    _st = [ITEM_STEM[i] for i in _il]
    if len(_il) == 1:
        NP.append((f"{_st[0]}aṃ dhammaṃ", S.OBJ(_il)))
        NP.append((f"{_st[0]}o dhammo", S.RES(_il)))
    else:
        NP.append((" ".join(f"{x}añca" for x in _st) + " dhammaṃ", S.OBJ(_il)))
        NP.append((" ".join(f"{x}o ca" for x in _st) + " dhammā", S.RES(_il)))
NP.sort(key=lambda e: len(e[0]), reverse=True)


def _cap_rx(p):
    return "[" + p[0].upper() + p[0].lower() + "]" + re.escape(p[1:])


B0, B1 = r"(?<![\w])", r"(?![\w])"
DEPWORD_RX = re.compile(B0 + r"(?:paṭicca|paccayā|nissāya|sahajāt(?:o|ā|aṃ)|saṃsaṭṭh(?:o|ā|aṃ)|"
                             r"sampayutt(?:o|ā|aṃ))" + B1)
NP_RULES = []
for _e in NP:
    _p, _d = _e[0], _e[1]
    _o = _e[2] if len(_e) > 2 else _d
    NP_RULES.append((re.compile(B0 + _cap_rx(_p) + r"(?=\s*⟨D⟩)"), _o))
    NP_RULES.append((re.compile(B0 + _cap_rx(_p) + r"(?=\s+(?:na|no)?(?:" + STEM_RX + r")paccayā" + B1 + ")"),
                     _o + " पर"))
    if _d:
        NP_RULES.append((re.compile(B0 + _cap_rx(_p) + B1), _d))

COND1 = r"(?:(?:na |no|na)?(?:" + STEM_RX + r")paccayā)"
CHAIN_RX = re.compile(r"[Uu]ppajja(ti|nti)\s+(" + COND1 + r"(?:(?:\s*…(?:pe…)?\s*|\s+)" + COND1 + r")*)")
COND_RX = re.compile(B0 + r"([Nn]a |[Nn]o|[Nn]a)?(" + STEM_RX + r"|" + "|".join(k.capitalize() for k in K) +
                     r")paccayā" + B1)


def _cond_hi(m):
    neg = bool(m.group(1))
    k = m.group(2).lower() if m.group(2).lower() in K else m.group(2)
    k = k[0].lower() + k[1:]
    return "⟪" + (NABL(k) if neg else ABL(k)) + "⟫"


def _chain(m):
    verb = "उत्पन्न होती हैं" if m.group(1) == "nti" else "उत्पन्न होती है"
    return COND_RX.sub(_cond_hi, m.group(2)) + " " + verb


WORDS = [(r"tīṇi", "तीन"), (r"ekaṃ", "एक"), (r"dve", "दो")]


def protect_variants(s, store):
    for v, h in VARIANTS.items():
        if v in s:
            store.append(h)
            s = s.replace(v, f"⟦{len(store) - 1}⟧")
    if "{" in s:
        raise Untranslated(f"unknown variant in {s[:80]}")
    return s


def protect_parens(s, store):
    def _r(m):
        inner = m.group(1)
        if re.fullmatch(r"\d+", inner):
            return m.group(0)
        store.append("(" + note_hi(inner) + ")")
        return f"⟦{len(store) - 1}⟧"
    return re.sub(r"\(([^()]*)\)", _r, s)


def finish(s, store):
    s = s.replace("…pe…", "…")
    s = re.sub(r"\s+…", "…", s)
    s = re.sub(r"\.(?=\s|$|\))", "।", s)
    s = re.sub(r"⟫(\s+)⟪", r", ", s)          # adjacent ablatives -> comma chain
    s = s.replace("⟪", "").replace("⟫", "")
    for i, t in enumerate(store):
        s = s.replace(f"⟦{i}⟧", t)
    return s


def tr_dep(pali, dep):
    """Translate a line of a dependent section with dependence word dep (key of S.DEP)."""
    store = []
    s = protect_variants(pali, store)
    s = protect_parens(s, store)
    s = re.sub(r"[Ss]iyā\s", "क्या ", s)
    s = CHAIN_RX.sub(_chain, s)
    s = DEPWORD_RX.sub("⟨D⟩", s)
    for rx, rep in NP_RULES:
        s = rx.sub(rep, s)
    s = COND_RX.sub(_cond_hi, s)
    for w, h in WORDS:
        s = re.sub(B0 + w + B1, h, s)
    s = s.replace("⟨D⟩", S.DEP[dep])
    s = finish(s, store)
    return s


# =====================================================================================
# 5b. The engine for the question section (pañhāvāra): "X dhammo Y dhammassa Zpaccayena paccayo"
#     Nominative phrases carry an agreement tag ⟨ms⟩/⟨fs⟩/⟨mp⟩/⟨fp⟩; every "…paccayena paccayo"
#     takes the verb form of the nearest tagged subject before it.
# =====================================================================================
VERB_OF = {"ms": "होता है", "fs": "होती है", "mp": "होते हैं", "fp": "होती हैं"}
_as = S._assada
REV_S, REV_P = S.REVIEW_SG, S.REVIEW_PL
CHAIN9 = "otaṃ… ghānaṃ… jivhaṃ… kāyaṃ… rūpe… sadde… gandhe… rase… phoṭṭhabbe… vatthuṃ"


def _schain(post):
    """'कान को… नाक को… … आधार को' (Sotaṃ… … vatthuṃ), without a final ellipsis."""
    return " ".join(f"{w} {post}…" for w in S.SENSE_ACC_PL[:-1]) + f" {S.SENSE_ACC_PL[-1]} {post}"


GIVE = [("dānaṃ deti", "दान देता है"), ("sīlaṃ samādiyati", "सदाचार ग्रहण करता है"),
        ("uposathakammaṃ karoti", "उपवास-व्रत का पालन करता है"), ("jhānaṃ uppādeti", "ध्यान उत्पन्न करता है"),
        ("vipassanaṃ uppādeti", "अंतर्दृष्टि उत्पन्न करता है"), ("maggaṃ uppādeti", "मार्ग उत्पन्न करता है"),
        ("abhiññaṃ uppādeti", "उच्च ज्ञान उत्पन्न करता है"),
        ("samāpattiṃ uppādeti", "ध्यान-अवस्था उत्पन्न करता है")]
CRIMES = [  # (present, gerund-phrase pāli, present hindi, gerund hindi)
    ("pāṇaṃ hanati", "pāṇaṃ hantvā", "जीव की हत्या करता है", "जीव की हत्या करके"),
    ("adinnaṃ ādiyati", "adinnaṃ ādiyitvā", "बिना दिया हुआ लेता है", "बिना दिया हुआ लेकर"),
    ("musā bhaṇati", "musā bhaṇitvā", "झूठ बोलता है", "झूठ बोलकर"),
    ("pisuṇaṃ bhaṇati", "pisuṇaṃ bhaṇitvā", "चुगली करता है", "चुगली करके"),
    ("pharusaṃ bhaṇati", "pharusaṃ bhaṇitvā", "कठोर वचन बोलता है", "कठोर वचन बोलकर"),
    ("samphaṃ palapati", "samphaṃ palapitvā", "व्यर्थ की बकवास करता है", "व्यर्थ की बकवास करके"),
    ("sandhiṃ chindati", "sandhiṃ chinditvā", "सेंध लगाता है", "सेंध लगाकर"),
    ("nillopaṃ harati", "nillopaṃ haritvā", "डाका डालता है", "डाका डालकर"),
    ("ekāgārikaṃ karoti", "ekāgārikaṃ karitvā", "किसी एक घर को लूटता है", "किसी एक घर को लूटकर"),
    ("paripanthe tiṭṭhati", "paripanthe ṭhatvā", "राह में घात लगाता है", "राह में घात लगाकर"),
    ("paradāraṃ gacchati", "paradāraṃ gantvā", "पराई स्त्री के पास जाता है", "पराई स्त्री के पास जाकर"),
    ("gāmaghātaṃ karoti", "gāmaghātaṃ karitvā", "गाँव लूटता है", "गाँव लूटकर"),
    ("nigamaghātaṃ karoti", "nigamaghātaṃ karitvā", "कस्बा लूटता है", "कस्बा लूटकर"),
    ("mātaraṃ jīvitā voropeti", "mātaraṃ jīvitā voropetvā", "माता की जान लेता है", "माता की जान लेकर"),
    ("pitaraṃ jīvitā voropeti", "pitaraṃ jīvitā voropetvā", "पिता की जान लेता है", "पिता की जान लेकर"),
    ("arahantaṃ jīvitā voropeti", "arahantaṃ jīvitā voropetvā", "अर्हत् की जान लेता है", "अर्हत् की जान लेकर"),
    ("duṭṭhena cittena tathāgatassa lohitaṃ uppādeti", "duṭṭhena cittena tathāgatassa lohitaṃ uppādetvā",
     "दुष्ट मन से तथागत का रक्त बहाता है", "दुष्ट मन से तथागत का रक्त बहाकर"),
    ("saṅghaṃ bhindati", "saṅghaṃ bhinditvā", "संघ में फूट डालता है", "संघ में फूट डालकर"),
]
DEEDS = [  # (nominative pāli, dative pāli, hindi nominative with tag, hindi dative)
    ("pāṇātipāto", "pāṇātipātassa", "जीव-हत्या⟨fs⟩", "जीव-हत्या के लिए"),
    ("adinnādānaṃ", "adinnādānassa", "बिना दिया हुआ लेना⟨ms⟩", "बिना दिया हुआ लेने के लिए"),
    ("kāmesumicchācāro", "kāmesumicchācārassa", "इंद्रिय-सुखों में दुराचार⟨ms⟩", "इंद्रिय-सुखों में दुराचार के लिए"),
    ("musāvādo", "musāvādassa", "झूठ बोलना⟨ms⟩", "झूठ बोलने के लिए"),
    ("pisuṇavācā", "pisuṇāya vācāya", "चुगली⟨fs⟩", "चुगली के लिए"),
    ("pharusavācā", "pharusāya vācāya", "कठोर वचन⟨ms⟩", "कठोर वचन के लिए"),
    ("samphappalāpo", "samphappalāpassa", "व्यर्थ की बकवास⟨fs⟩", "व्यर्थ की बकवास के लिए"),
    ("abhijjhā", "abhijjhāya", "लालच⟨ms⟩", "लालच के लिए"),
    ("byāpādo", "byāpādassa", "दुर्भावना⟨fs⟩", "दुर्भावना के लिए"),
    ("micchādiṭṭhi", "micchādiṭṭhiyā", "ग़लत दृष्टि⟨fs⟩", "ग़लत दृष्टि के लिए"),
    ("niyatamicchādiṭṭhi", "niyatamicchādiṭṭhiyā", "नियत ग़लत दृष्टि⟨fs⟩", "नियत ग़लत दृष्टि के लिए"),
    ("mātughātikammaṃ", "mātughātikammassa", "माता की हत्या का कर्म⟨ms⟩", "माता की हत्या के कर्म के लिए"),
    ("pitughātikammaṃ", "pitughātikammassa", "पिता की हत्या का कर्म⟨ms⟩", "पिता की हत्या के कर्म के लिए"),
    ("arahantaghātikammaṃ", "arahantaghātikammassa", "अर्हत् की हत्या का कर्म⟨ms⟩",
     "अर्हत् की हत्या के कर्म के लिए"),
    ("ruhiruppādakammaṃ", "ruhiruppādakammassa", "रक्त बहाने का कर्म⟨ms⟩", "रक्त बहाने के कर्म के लिए"),
    ("saṅghabhedakammaṃ", "saṅghabhedakammassa", "संघ में फूट डालने का कर्म⟨ms⟩",
     "संघ में फूट डालने के कर्म के लिए"),
]
KNOW = [  # (pāli stem, nominative hindi, oblique hindi)
    ("iddhividhañāṇ", "अलौकिक शक्तियों का ज्ञान", S.IDDHIVIDHA_OBL),
    ("cetopariyañāṇ", S.CETOPARIYA, S.CETOPARIYA_OBL),
    ("pubbenivāsānussatiñāṇ", "पूर्व जन्मों के अनुस्मरण का ज्ञान", S.PUBBENIVASA_OBL),
    ("yathākammūpagañāṇ", "प्राणियों के अपने कर्मों के अनुसार जाने का ज्ञान", S.YATHAKAMMUPAGA_OBL),
    ("anāgataṃsañāṇ", "भविष्य को जानने का ज्ञान", S.ANAGATAMSA_OBL),
]
ORD = {"paṭham": ("पहला", "पहले"), "dutiy": ("दूसरा", "दूसरे"), "tatiy": ("तीसरा", "तीसरे"),
       "catutth": ("चौथा", "चौथे")}
PARIKAMMA = "की प्रारंभिक तैयारी⟨fs⟩"
PATI = (", अर्थ के विश्लेषणात्मक ज्ञान के लिए, शिक्षा के विश्लेषणात्मक ज्ञान के लिए, "
        "भाषा के विश्लेषणात्मक ज्ञान के लिए, प्रत्युत्पन्न बुद्धि के विश्लेषणात्मक ज्ञान के लिए, "
        "संभव और असंभव को जानने की कुशलता के लिए")
PATI_P = ("atthappaṭisambhidāya, dhammappaṭisambhidāya, niruttippaṭisambhidāya, paṭibhānappaṭisambhidāya, "
          "ṭhānāṭhānakosallassa")
FRUIT = "फल की ध्यान-अवस्था"
OUT_OF_NIRODHA = "समाप्ति की ध्यान-अवस्था से बाहर आने वाले व्यक्ति में"

PN = [
    # --- labels of the kinds of a condition
    ("ārammaṇūpanissayo", S.ARAMMANUPANISSAYA), ("anantarūpanissayo", S.ANANTARUPANISSAYA),
    ("pakatūpanissayo", S.PAKATUPANISSAYA), ("ārammaṇapurejātaṃ", S.ARAMMANAPUREJATA),
    ("vatthupurejātaṃ", S.VATTHUPUREJATA),
    ("re:[Ss]ahajāt(?:ā|o|aṃ)(?= –)", "सह-उत्पत्ति"), ("re:[Pp]acchājātā(?= –)", "पश्चात्-उत्पत्ति"),
    ("re:[Pp]urejātaṃ(?= –)", "पूर्व-उत्पत्ति"), ("re:[Nn]ānākkhaṇikā(?= –)", "भिन्न क्षण"),
    ("sahajātā, nānākkhaṇikā", "सह-उत्पत्ति, भिन्न क्षण"),
    ("re:[Pp]urejātaṃ(?= [^– ])", "पूर्व-उत्पत्ति:"),
    ("re:[Ss]ahajātaṃ(?=[,.])", "सह-उत्पत्ति"), ("re:[Pp]urejātaṃ(?=[,.])", "पूर्व-उत्पत्ति"),
    ("re:[Pp]acchājātaṃ(?=[,.])", "पश्चात्-उत्पत्ति"), ("re:āhāraṃ(?=[,.])", "आहार"),
    ("re:indriyaṃ(?=[,.])", "क्षमता"),
    ("re:[Pp]acchājātā(?! –)", "बाद में उत्पन्न"),
    # --- khandha / vatthu / mahābhūta subjects and datives
    ("kusalo eko khandho ca vatthu ca", "एक हितकर समूह और आधार⟨mp⟩"),
    ("akusalo eko khandho ca vatthu ca", "एक हानिकर समूह और आधार⟨mp⟩"),
    ("tayo khandhā ca vatthu ca", "तीन समूह और आधार⟨mp⟩"), ("dve khandhā ca vatthu ca", "दो समूह और आधार⟨mp⟩"),
    ("kusalo eko khandho", "एक हितकर समूह⟨ms⟩"), ("akusalo eko khandho", "एक हानिकर समूह⟨ms⟩"),
    ("vipākābyākato kiriyābyākato eko khandho", f"{VK_SG} एक समूह⟨ms⟩"),
    ("vipākābyākato eko khandho", f"{VAB} एक समूह⟨ms⟩"),
    ("tayo khandhā", "तीन समूह⟨mp⟩"), ("dve khandhā", "दो समूह⟨mp⟩"), ("khandhā", "समूह⟨mp⟩"),
    ("kusalā khandhā ca mahābhūtā ca", "हितकर समूह और महाभूत⟨mp⟩"),
    ("akusalā khandhā ca mahābhūtā ca", "हानिकर समूह और महाभूत⟨mp⟩"),
    ("kusalā khandhā ca kabaḷīkāro āhāro ca", "हितकर समूह और कौर-कौर खाया जाने वाला भोजन⟨mp⟩"),
    ("akusalā khandhā ca kabaḷīkāro āhāro ca", "हानिकर समूह और कौर-कौर खाया जाने वाला भोजन⟨mp⟩"),
    ("kusalā khandhā ca rūpajīvitindriyañca", f"हितकर समूह और {S.RUPAJIVITINDRIYA}⟨mp⟩"),
    ("akusalā khandhā ca rūpajīvitindriyañca", f"हानिकर समूह और {S.RUPAJIVITINDRIYA}⟨mp⟩"),
    ("kusalā khandhā", "हितकर समूह⟨mp⟩"), ("akusalā khandhā", "हानिकर समूह⟨mp⟩"),
    ("vipākābyākatā kiriyābyākatā khandhā", f"{VK_PL} समूह⟨mp⟩"),
    ("vipākābyākatā, kiriyābyākatā khandhā", f"{VK_PL} समूह⟨mp⟩"),
    ("vipākābyākatā khandhā", f"{VAB} समूह⟨mp⟩"), ("kiriyābyākatā khandhā", f"{KAB} समूह⟨mp⟩"),
    ("purimā purimā", "पहले-पहले के"), ("pacchimānaṃ pacchimānaṃ", "बाद-बाद के"),
    ("kusalānaṃ khandhānaṃ", "हितकर समूहों के लिए"), ("akusalānaṃ khandhānaṃ", "हानिकर समूहों के लिए"),
    ("vipākābyākatānaṃ kiriyābyākatānaṃ khandhānaṃ", f"{VK_PL} समूहों के लिए"),
    ("kiriyābyākatānaṃ khandhānaṃ", f"{KAB} समूहों के लिए"),
    ("vipākānaṃ khandhānaṃ", "कर्म के फल रूपी समूहों के लिए"),
    ("sampayuttakānaṃ khandhānaṃ", f"{S.SAMPAYUTTAKA_KH_OBL} के लिए"),
    ("tiṇṇannaṃ khandhānaṃ", "तीन समूहों के लिए"), ("ekassa khandhassa", "एक समूह के लिए"),
    ("dvinnaṃ khandhānaṃ", "दो समूहों के लिए"), ("khandhānaṃ", "समूहों के लिए"),
    ("vatthussa ca", "और आधार के लिए"), ("vatthussa", "आधार के लिए"), ("vatthu", "आधार⟨ms⟩"),
    ("bāhiraṃ ekaṃ mahābhūtaṃ", f"एक {S.BAHIRA} महाभूत⟨ms⟩"), ("ekaṃ mahābhūtaṃ", "एक महाभूत⟨ms⟩"),
    ("tayo mahābhūtā", "तीन महाभूत⟨mp⟩"), ("dve mahābhūtā", "दो महाभूत⟨mp⟩"), ("mahābhūtā", "महाभूत⟨mp⟩"),
    ("tiṇṇannaṃ mahābhūtānaṃ", "तीन महाभूतों के लिए"), ("ekassa mahābhūtassa", "एक महाभूत के लिए"),
    ("dvinnaṃ mahābhūtānaṃ", "दो महाभूतों के लिए"),
    ("bāhiraṃ", S.BAHIRA), ("āhārasamuṭṭhānaṃ", S.AHARASAM), ("utusamuṭṭhānaṃ", S.UTUSAM),
    ("asaññasattānaṃ", S.ASANNASATTA), ("paṭisandhikkhaṇe", S.PATISANDHI),
    ("cittasamuṭṭhānānaṃ rūpānaṃ, kaṭattārūpānaṃ, upādārūpānaṃ", f"{S.CSR_OBL}, {S.KTR_OBL} और {S.UPR_OBL} के लिए"),
    ("cittasamuṭṭhānānaṃ rūpānaṃ kaṭattārūpānaṃ upādārūpānaṃ", f"{S.CSR_OBL}, {S.KTR_OBL} और {S.UPR_OBL} के लिए"),
    ("kaṭattārūpānaṃ, upādārūpānaṃ", f"{S.KTR_OBL} और {S.UPR_OBL} के लिए"),
    ("kaṭattārūpānaṃ upādārūpānaṃ", f"{S.KTR_OBL} और {S.UPR_OBL} के लिए"),
    ("cittasamuṭṭhānānañca rūpānaṃ", f"और {S.CSR_OBL} के लिए"),
    ("cittasamuṭṭhānānaṃ rūpānaṃ", f"{S.CSR_OBL} के लिए"), ("kaṭattā ca rūpānaṃ", f"और {S.KTR_OBL} के लिए"),
    ("kaṭattārūpānaṃ", f"{S.KTR_OBL} के लिए"), ("upādārūpānaṃ", f"{S.UPR_OBL} के लिए"),
    ("purejātassa imassa kāyassa", "पहले उत्पन्न इस शरीर के लिए"), ("imassa kāyassa", "इस शरीर के लिए"),
    # --- kamma / āhāra / indriya / jhāna / magga subjects
    ("kusalā cetanā", f"हितकर {S.CETANA}⟨ms⟩"), ("akusalā cetanā", f"हानिकर {S.CETANA}⟨ms⟩"),
    ("vipākābyākatā kiriyābyākatā cetanā", f"{VK_SG} {S.CETANA}⟨ms⟩"),
    ("vipākābyākatā cetanā", f"{VAB} {S.CETANA}⟨ms⟩"), ("cetanā", f"{S.CETANA}⟨ms⟩"),
    ("kusalā āhārā", "हितकर आहार⟨mp⟩"), ("akusalā āhārā", "हानिकर आहार⟨mp⟩"),
    ("vipākābyākatā kiriyābyākatā āhārā", f"{VK_PL} आहार⟨mp⟩"), ("vipākābyākatā āhārā", f"{VAB} आहार⟨mp⟩"),
    ("kabaḷīkāro āhāro", "कौर-कौर खाया जाने वाला भोजन⟨ms⟩"),
    ("kusalā indriyā", "हितकर क्षमताएँ⟨fp⟩"), ("akusalā indriyā", "हानिकर क्षमताएँ⟨fp⟩"),
    ("vipākābyākatā kiriyābyākatā indriyā", f"{VK_PL} क्षमताएँ⟨fp⟩"),
    ("vipākābyākatā indriyā", f"{VAB} क्षमताएँ⟨fp⟩"), ("rūpajīvitindriyaṃ", f"{S.RUPAJIVITINDRIYA}⟨fs⟩"),
    ("āvajjanā", "मन को विषय की ओर मोड़ना⟨ms⟩"),
    # --- anantara / samanantara
    ("kusalaṃ vuṭṭhānassa", "हितकर मन⟨ms⟩ बाहर आने के लिए"),
    ("akusalaṃ vuṭṭhānassa", "हानिकर मन⟨ms⟩ बाहर आने के लिए"),
    ("kiriyaṃ vuṭṭhānassa", f"{KAB.replace(' नैतिक रूप से अनिर्धारित', '')} मन⟨ms⟩ बाहर आने के लिए"),
    ("maggo phalassa", "मार्ग⟨ms⟩ फल के लिए"),
    ("anulomaṃ sekkhāya phalasamāpattiyā", f"अनुरूपता⟨fs⟩ सीखने के चरण वाले की {FRUIT} के लिए"),
    ("arahato anulomaṃ phalasamāpattiyā", f"अर्हत् की अनुरूपता⟨fs⟩ {FRUIT} के लिए"),
    ("nirodhā vuṭṭhahantassa nevasaññānāsaññāyatanakusalaṃ phalasamāpattiyā",
     f"{OUT_OF_NIRODHA} {S.ARUPA_OBL('nevasaññānāsañña')} का हितकर मन⟨ms⟩ {FRUIT} के लिए"),
    ("nirodhā vuṭṭhahantassa nevasaññānāsaññāyatanakiriyaṃ phalasamāpattiyā",
     f"{OUT_OF_NIRODHA} {S.ARUPA_OBL('nevasaññānāsañña')} का केवल क्रिया रूपी मन⟨ms⟩ {FRUIT} के लिए"),
    ("anulomaṃ gotrabhussa", f"अनुरूपता⟨fs⟩ {S.GOTRABHU} के लिए"),
    ("anulomaṃ vodānassa", f"अनुरूपता⟨fs⟩ {S.VODANA} के लिए"),
    ("gotrabhu maggassa", f"{S.GOTRABHU}⟨ms⟩ मार्ग के लिए"), ("vodānaṃ maggassa", f"{S.VODANA}⟨fs⟩ मार्ग के लिए"),
    ("bhavaṅgaṃ āvajjanāya", f"जीवन-धारा⟨fs⟩ {S.AVAJJANA_FOR}"),
    # --- ārammaṇa / garu prose (as in the approved sample)
    ("dānaṃ datvā sīlaṃ samādiyitvā uposathakammaṃ katvā", S.DANA3),
    ("taṃ garuṃ katvā paccavekkhati", f"उसे महत्व देकर उस पर {REV_S}"),
    ("pubbe suciṇṇāni garuṃ katvā paccavekkhati", f"{S.SUCINNA} को महत्व देकर उन पर {REV_S}"),
    ("jhānā vuṭṭhahitvā jhānaṃ garuṃ katvā paccavekkhati", f"ध्यान से उठकर ध्यान को महत्व देकर उस पर {REV_S}"),
    ("sekkhā gotrabhuṃ garuṃ katvā paccavekkhanti", f"{S.SEKKHA} {S.GOTRABHU} को महत्व देकर उस पर {REV_P}"),
    ("vodānaṃ garuṃ katvā paccavekkhanti", f"{S.VODANA} को महत्व देकर उस पर {REV_P}"),
    ("sekkhā maggā vuṭṭhahitvā maggaṃ garuṃ katvā paccavekkhanti",
     f"{S.SEKKHA} मार्ग से उठकर मार्ग को महत्व देकर उस पर {REV_P}"),
    ("arahā maggā vuṭṭhahitvā maggaṃ garuṃ katvā paccavekkhati",
     f"{S.ARAHA} मार्ग से उठकर मार्ग को महत्व देकर उस पर {REV_S}"),
    ("taṃ garuṃ katvā assādeti abhinandati", f"उसे महत्व देकर {_as('उस')}"),
    ("taṃ garuṃ katvā rāgo uppajjati, diṭṭhi uppajjati", f"उसे महत्व देकर {S.AROSE2}"),
    ("pubbe suciṇṇāni garuṃ katvā assādeti abhinandati", f"{S.SUCINNA} को महत्व देकर {_as('उन', 'उन')}"),
    ("jhānā vuṭṭhahitvā jhānaṃ garuṃ katvā assādeti abhinandati",
     f"ध्यान से उठकर ध्यान को महत्व देकर {_as('उस')}"),
    ("rāgaṃ garuṃ katvā assādeti abhinandati", f"राग को महत्व देकर {_as('उस')}"),
    ("diṭṭhiṃ garuṃ katvā assādeti abhinandati", f"दृष्टि को महत्व देकर {_as('उस')}"),
    ("cakkhuṃ garuṃ katvā assādeti abhinandati", f"आँख को महत्व देकर {_as('उस')}"),
    ("re:[Ss]" + CHAIN9 + "… vipākābyākate kiriyābyākate khandhe garuṃ katvā assādeti abhinandati",
     f"{S.SENSE_CHAIN('को')} {VK_PL} समूहों को महत्व देकर {_as('उन', 'उन')}"),
    ("arahā phalaṃ garuṃ katvā paccavekkhati", f"{S.ARAHA} फल को महत्व देकर उस पर {REV_S}"),
    ("nibbānaṃ garuṃ katvā paccavekkhati", f"निर्वाण को महत्व देकर उस पर {REV_S}"),
    ("sekkhā phalaṃ garuṃ katvā paccavekkhanti", f"{S.SEKKHA} फल को महत्व देकर उस पर {REV_P}"),
    ("nibbānaṃ garuṃ katvā paccavekkhanti", f"निर्वाण को महत्व देकर उस पर {REV_P}"),
    ("nibbānaṃ phalassa", "निर्वाण⟨ms⟩ फल के लिए"),
    ("nibbānaṃ gotrabhussa", f"निर्वाण⟨ms⟩ {S.GOTRABHU} के लिए"),
    ("vodānassa", f"{S.VODANA} के लिए"), ("maggassa", "मार्ग के लिए"),
    ("cakkhuṃ assādeti abhinandati", _as("आँख")), ("cakkhuṃ assādeti, abhinandati", _as("आँख")),
    ("re:[Ss]" + CHAIN9 + " assādeti,? abhinandati", f"{_schain('का')} {S.ASSADA}, उसमें आनंद लेता है"),
    ("taṃ ārabbha", "उसे विषय बनाकर"),
    ("rāgo uppajjati", "राग उत्पन्न होता है"), ("diṭṭhi uppajjati", "दृष्टि उत्पन्न होती है"),
    ("vicikicchā uppajjati", "संशय उत्पन्न होता है"), ("uddhaccaṃ uppajjati", "बेचैनी उत्पन्न होती है"),
    ("domanassaṃ uppajjati", "उदासी उत्पन्न होती है"),
    # --- vipassati (purejāta, atthi)
    ("arahā cakkhuṃ aniccato dukkhato anattato vipassati", f"{S.ARAHA} आँख को {S.ANICCA3} {S.VIPASSATI}"),
    ("sekkhā vā puthujjanā vā cakkhuṃ aniccato dukkhato anattato vipassanti",
     f"{S.SEKKHA_VA_PUTHUJJANA} आँख को {S.ANICCA3} {S.VIPASSANTI}"),
    ("re:[Ss]" + CHAIN9 + " aniccato dukkhato anattato vipassati", f"{_schain('को')} {S.ANICCA3} {S.VIPASSATI}"),
    ("re:[Ss]" + CHAIN9 + " aniccato dukkhato anattato vipassanti", f"{_schain('को')} {S.ANICCA3} {S.VIPASSANTI}"),
    ("dibbena cakkhunā rūpaṃ passati", "दिव्य आँख से दृश्य रूप देखता है"),
    ("dibbena cakkhunā rūpaṃ passanti", "दिव्य आँख से दृश्य रूप देखते हैं"),
    ("dibbāya sotadhātuyā saddaṃ suṇāti", "दिव्य कान के तत्व से ध्वनि सुनता है"),
    ("dibbāya sotadhātuyā saddaṃ suṇanti", "दिव्य कान के तत्व से ध्वनि सुनते हैं"),
    # --- pakatūpanissaya prose
    ("saddhaṃ upanissāya", "श्रद्धा के प्रबल आश्रय से"),
    ("re:[Ss]īlaṃ… sutaṃ… cāgaṃ… paññaṃ upaniss[aā]ya", "सदाचार… सुने-सीखे ज्ञान… त्याग… प्रज्ञा के प्रबल आश्रय से"),
    ("saddhā… sīlaṃ… sutaṃ… cāgo… paññā", "श्रद्धा… सदाचार… सुना-सीखा ज्ञान… त्याग… प्रज्ञा⟨fs⟩"),
    ("saddhāya… sīlassa… sutassa… cāgassa… paññāya",
     "श्रद्धा के लिए… सदाचार के लिए… सुने-सीखे ज्ञान के लिए… त्याग के लिए… प्रज्ञा के लिए"),
    ("rāgaṃ upanissāya", "राग के प्रबल आश्रय से"), ("dosaṃ upanissāya", "द्वेष के प्रबल आश्रय से"),
    ("mohaṃ upanissāya", "मोह के प्रबल आश्रय से"), ("mānaṃ upanissāya", "अहंकार के प्रबल आश्रय से"),
    ("diṭṭhiṃ upanissāya", "दृष्टि के प्रबल आश्रय से"), ("patthanaṃ upanissāya", "कामना के प्रबल आश्रय से"),
    ("dosaṃ… mohaṃ… mānaṃ… diṭṭhiṃ… patthanaṃ upanissāya",
     "द्वेष… मोह… अहंकार… दृष्टि… कामना के प्रबल आश्रय से"),
    ("rāgo… doso… moho… māno… diṭṭhi… patthanā", "राग… द्वेष… मोह… अहंकार… दृष्टि… कामना⟨fs⟩"),
    ("rāgassa… dosassa… mohassa… mānassa… diṭṭhiyā… patthanāya",
     "राग के लिए… द्वेष के लिए… मोह के लिए… अहंकार के लिए… दृष्टि के लिए… कामना के लिए"),
    ("kāyikaṃ sukhaṃ upanissāya", "शारीरिक सुख के प्रबल आश्रय से"),
    ("kāyikaṃ dukkhaṃ… utuṃ… bhojanaṃ… senāsanaṃ upanissāya",
     "शारीरिक दुःख… तापमान… भोजन… निवास-स्थान के प्रबल आश्रय से"),
    ("kāyikaṃ sukhaṃ… kāyikaṃ dukkhaṃ… utu… bhojanaṃ… senāsanaṃ",
     "शारीरिक सुख… शारीरिक दुःख… तापमान… भोजन… निवास-स्थान⟨ms⟩"),
    ("kāyikassa sukhassa… kāyikassa dukkhassa… phalasamāpattiyā",
     f"शारीरिक सुख के लिए… शारीरिक दुःख के लिए… {FRUIT} के लिए"),
    ("kāyikassa sukhassa, kāyikassa dukkhassa, phalasamāpattiyā",
     f"शारीरिक सुख के लिए, शारीरिक दुःख के लिए, {FRUIT} के लिए"),
    ("kāyikassa sukhassa", "शारीरिक सुख के लिए"),
    ("kāyikaṃ sukhaṃ", "शारीरिक सुख⟨ms⟩"), ("kāyikaṃ dukkhaṃ", "शारीरिक दुःख⟨ms⟩"), ("utu", "तापमान⟨ms⟩"),
    ("bhojanaṃ", "भोजन⟨ms⟩"), ("senāsanaṃ", "निवास-स्थान⟨ms⟩"),
    ("phalasamāpattiyā", f"{FRUIT} के लिए"), ("phalasamāpatti", f"{FRUIT}⟨fs⟩"),
    ("attānaṃ ātāpeti paritāpeti, pariyiṭṭhimūlakaṃ dukkhaṃ paccanubhoti",
     "स्वयं को तपाता है, संतप्त करता है, खोज से उत्पन्न दुःख भोगता है"),
    ("mānaṃ jappeti, diṭṭhiṃ gaṇhāti", "अहंकार करता है, दृष्टि पकड़ता है"),
    ("kusalaṃ kammaṃ vipākassa", "हितकर कर्म⟨ms⟩ कर्म-फल के लिए"),
    ("akusalaṃ kammaṃ vipākassa", "हानिकर कर्म⟨ms⟩ कर्म-फल के लिए"),
    ("arahā kāyikaṃ sukhaṃ upanissāya", f"{S.ARAHA} शारीरिक सुख के प्रबल आश्रय से"),
    ("arahā maggaṃ upanissāya", f"{S.ARAHA} मार्ग के प्रबल आश्रय से"),
    ("sekkhā maggaṃ upanissāya", f"{S.SEKKHA} मार्ग के प्रबल आश्रय से"),
    ("anuppannaṃ kiriyasamāpattiṃ uppādeti, uppannaṃ samāpajjati",
     "अब तक उत्पन्न न हुई केवल क्रिया रूपी ध्यान-अवस्था उत्पन्न करता है, उत्पन्न हो चुकी ध्यान-अवस्था में "
     "प्रवेश करता है"),
    ("anuppannaṃ samāpattiṃ uppādenti, uppannaṃ samāpajjanti",
     "अब तक उत्पन्न न हुई ध्यान-अवस्था उत्पन्न करते हैं, उत्पन्न हो चुकी ध्यान-अवस्था में प्रवेश करते हैं"),
    ("saṅkhāre aniccato dukkhato anattato vipassati", f"निर्मित परिघटनाओं को {S.ANICCA3} {S.VIPASSATI}"),
    ("saṅkhāre aniccato dukkhato anattato vipassanti", f"निर्मित परिघटनाओं को {S.ANICCA3} {S.VIPASSANTI}"),
    ("maggo sekkhānaṃ " + PATI_P, "मार्ग⟨ms⟩ सीखने के चरण वालों के" + PATI[1:].replace("अर्थ के", "अर्थ के", 1)),
    ("maggo arahato " + PATI_P, "मार्ग⟨ms⟩ अर्हत् के" + PATI[1:]),
    ("maggo phalasamāpattiyā", f"मार्ग⟨ms⟩ {FRUIT} के लिए"),
    ("tassa paṭighātatthāya", "उसके प्रतिकार के लिए"),
    ("re:upanissaya(?=…)", "प्रबल आश्रय"),
    ("dibbassa cakkhussa parikammaṃ", f"दिव्य आँख {PARIKAMMA}"), ("dibbassa cakkhussa", "दिव्य आँख के लिए"),
    ("dibbāya sotadhātuyā parikammaṃ", f"दिव्य कान के तत्व {PARIKAMMA}"),
    ("dibbāya sotadhātuyā", "दिव्य कान के तत्व के लिए"),
    ("dibbacakkhu", "दिव्य आँख⟨fs⟩"), ("dibbasotadhātu", "दिव्य कान का तत्व⟨ms⟩"),
]
PN += GIVE
for _p, _g, _h, _gh in CRIMES:
    PN += [(_p, _h), (_g, _gh)]
for _n, _d, _hn, _hd in DEEDS:
    PN += [(_n, _hn), (_d, _hd)]
for _st, _hn, _ho in KNOW:
    PN += [(_st + "assa parikammaṃ", f"{_ho} {PARIKAMMA}"), (_st + "assa", f"{_ho} के लिए"), (_st + "aṃ", _hn + "⟨ms⟩")]
for _o, (_hd, _ho) in ORD.items():
    PN += [(f"{_o}assa jhānassa parikammaṃ", f"{_ho} ध्यान {PARIKAMMA}"), (f"{_o}assa jhānassa", f"{_ho} ध्यान के लिए"),
           (f"{_o}aṃ jhānaṃ", f"{_hd} ध्यान⟨ms⟩"), (f"{_o}assa maggassa parikammaṃ", f"{_ho} मार्ग {PARIKAMMA}"),
           (f"{_o}assa maggassa", f"{_ho} मार्ग के लिए"), (f"{_o}o maggo", f"{_hd} मार्ग⟨ms⟩")]
for _a in S.ARUPA_AYATANA:
    PN += [(f"{_a[:-1]}āyatanassa parikammaṃ", f"{S.ARUPA_OBL(_a)} {PARIKAMMA}"),
           (f"{_a[:-1]}āyatanassa", f"{S.ARUPA_OBL(_a)} के लिए"),
           (f"{_a[:-1]}āyatanaṃ", S.ARUPA_AYATANA[_a] + "⟨ms⟩")]
for _s in S.SENSES:
    _pa = {"cakkhu": "cakkh", "sota": "sot", "ghāna": "ghān", "jivhā": "jivh", "kāya": "kāy"}[_s]
    _ip = {"cakkhu": "cakkhundriyaṃ", "sota": "sotindriyaṃ", "ghāna": "ghānindriyaṃ", "jivhā": "jivhindriyaṃ",
           "kāya": "kāyindriyaṃ"}[_s]
    PN += [(f"{_pa}āyatanaṃ", S.AYA_SENSE(_s) + "⟨ms⟩"), (f"{_s}viññāṇassa", f"{S.VINNANA(_s)} के लिए"),
           (_ip, S.INDRIYA_SENSE(_s) + "⟨fs⟩")]
for _o in S.OBJECTS:
    PN.append((f"{_o[:-1]}āyatanaṃ", S.AYA_OBJ(_o) + "⟨ms⟩"))
for _x in ("jhān", "magg"):
    _h = {"jhān": "ध्यान के अंग", "magg": "मार्ग के अंग"}[_x]
    PN += [(f"kusalāni {_x}aṅgāni", f"हितकर {_h}⟨mp⟩"), (f"akusalāni {_x}aṅgāni", f"हानिकर {_h}⟨mp⟩"),
           (f"vipākābyākatāni kiriyābyākatāni {_x}aṅgāni", f"{VK_PL} {_h}⟨mp⟩"),
           (f"vipākābyākatāni {_x}aṅgāni", f"{VAB} {_h}⟨mp⟩")]
# head items: "Kusalo dhammo" (subject, with a comma as in S.PANHA) and "kusalassa dhammassa" (dative)
PN_HEAD = []
for _il in ITEM_LISTS:
    _st = [ITEM_STEM[i] for i in _il]
    if len(_il) == 1:
        _nom, _dat = f"{_st[0]}o dhammo", f"{_st[0]}assa dhammassa"
        _tag = "⟨fs⟩"
    else:
        _nom = " ".join(f"{x}o ca" for x in _st) + " dhammā"
        _dat = " ".join(f"{x}assa ca" for x in _st) + " dhammassa"
        _tag = "⟨fp⟩"
    PN_HEAD.append((re.compile("^" + _cap_rx(_nom) + " "), S.RES(_il) + _tag + ", "))
    PN.append((_dat, S.DAT(_il)))

PN_RULES = []
PN = [(unicodedata.normalize("NFC", p), h) for p, h in PN]
for _p, _h in sorted(PN, key=lambda e: len(e[0]), reverse=True):
    if _p.startswith("re:"):
        PN_RULES.append((re.compile(B0 + _p[3:]), _h))
    else:
        PN_RULES.append((re.compile(B0 + _cap_rx(_p) + B1), _h))
INS_RX = re.compile(B0 + r"(" + STEM_RX + r")paccayena paccayo" + B1)


def _resolve_verbs(s):
    out, last = [], None
    for tok in re.split(r"(⟨(?:ms|fs|mp|fp)⟩|⟨V⟩)", s):
        if tok in ("⟨ms⟩", "⟨fs⟩", "⟨mp⟩", "⟨fp⟩"):
            last = tok[1:-1]
        elif tok == "⟨V⟩":
            if last is None:
                raise Untranslated("verb without subject")
            out.append(VERB_OF[last])
        else:
            out.append(tok)
    return "".join(out)


def tr_panha(pali):
    store = []
    s = protect_variants(unicodedata.normalize("NFC", pali), store)
    s = protect_parens(s, store)
    s = s.replace("…pe…", "…")
    s = re.sub(r"\s+…", "…", s)
    for rx, rep in PN_HEAD:
        s = rx.sub(rep, s)
    s = INS_RX.sub(lambda m: f"{INS(m.group(1))} ⟨V⟩", s)
    for rx, rep in PN_RULES:
        s = rx.sub(rep, s)
    s = _resolve_verbs(s)
    return finish(s, store)


# =====================================================================================
# 6. Line routing
# =====================================================================================
SAMPLE_RANGES = [(1, 128, "build_s2"), (129, 190, "build_s3"), (1235, 1262, "build_s4")]
DEP_RANGES = [(485, 519, "sahajāta"), (520, 920, "paccaya"), (921, 963, "nissaya"), (964, 1202, "saṃsaṭṭha"),
              (1203, 1234, "sampayutta")]
MAN = {}   # manual lines: non-empty line number -> Hindi (no block ID)
MAN[1865] = (f"{NABL('natthi')}, {NLOC('hetu')} पंद्रह (संक्षिप्त)। {NLOC('natthi')} भी, {NLOC('vigata')} भी "
             f"({S.SADISA('hetu', neg=True)} हैं)।")
MAN[2485] = (count_line("Naindriyapaccayā nahetupaccayā naārammaṇapaccayā (mūlakaṃ saṃkhittaṃ) navipākapaccayā "
                        "najhānapaccayā namaggapaccayā nasampayuttapaccayā navippayuttapaccayā nonatthipaccayā "
                        "novigatapaccayā āhāre ekaṃ, atthiyā ekaṃ, avigate ekaṃ")
             + f" (जैसे {M_NHETU} में [पाठभेद (Syā.): nahetumūlake]। संक्षिप्त)।")


def dep_of(n):
    for a, b, d in DEP_RANGES:
        if a <= n <= b:
            return d
    return None


def translate(n):
    if n in MAN:
        return MAN[n]
    line = P[n - 1]
    if line.startswith("#"):
        return heading_line(line)
    b = body(n).strip()
    if b in CLOSE:
        return CLOSE[b]
    try:
        return count_line(b)
    except Untranslated:
        pass
    d = dep_of(n)
    if d:
        return tr_dep(b, d)
    if 1263 <= n <= 1437 or 1681 <= n <= 1695:
        return tr_panha(b)
    raise Untranslated(f"line {n}: no route")


def build(strict=True):
    H = [None] * len(P)
    for a, b, fn in SAMPLE_RANGES:
        lines = getattr(S, fn)()
        assert len(lines) == b - a + 1, (fn, len(lines))
        for i, h in enumerate(lines):
            H[a - 1 + i] = h
    errs = []
    for n in range(1, len(P) + 1):
        if H[n - 1] is not None:
            continue
        try:
            H[n - 1] = check_latin(translate(n), f"line {n}")
        except Untranslated as e:
            errs.append(f"line {n}: {e}" if not str(e).startswith("line") else str(e))
            H[n - 1] = "??" + str(n)
    return H, errs


def enginetest():
    """Run tr_dep(..., 'paṭicca') on the sample's dependent lines and diff against the approved Hindi."""
    bad = 0
    for a, b, fn in SAMPLE_RANGES[:2]:
        lines = getattr(S, fn)()
        for i, h in enumerate(lines):
            n = a + i
            if P[n - 1].startswith("#"):
                continue
            pb = body(n).strip()
            if pb in CLOSE or pb.startswith("Gaṇanā"):
                continue
            try:
                c = count_line(pb)
                if c != h:
                    bad += 1
                    print(n, "COUNT\n  S:", h, "\n  M:", c)
                continue
            except Untranslated:
                pass
            try:
                mine = tr_dep(pb, "paṭicca")
            except Untranslated as e:
                mine = "ERR " + str(e)
            if mine != h:
                bad += 1
                print(n, "\n  S:", h, "\n  M:", mine)
    print("engine diffs:", bad)


def main():
    if "--enginetest" in sys.argv:
        enginetest()
        return
    H, errs = build()
    hist = {}
    for e in errs:
        m = re.match(r"line (\d+)", e)
        b = (int(m.group(1)) // 100) * 100 if m else -1
        hist[b] = hist.get(b, 0) + 1
        if "--quiet" not in sys.argv:
            print(e[:300])
    print("errors:", len(errs), "by hundred:", sorted(hist.items()))
    if errs:
        sys.exit(1)
    text = S.assemble(PALI_TEXT, H)
    if "--check" not in sys.argv:
        with open(OUT_PATH, "w", encoding="utf-8", newline="\n") as f:
            f.write(text)
        print("wrote", OUT_PATH)
    print("slips seen:", sorted(set(SEEN_SLIPS)))


if __name__ == "__main__":
    main()
