"""Hindi plain zero-shot of pi-7 (Paṭṭhāna) files 2-09 .. 2-17 (triads hīna .. sanidassanasappaṭigha).

Rule-based composer: every line is built from fixed frames and item tables (imported from
build_sample_hi.py where they exist), so identical Pāli gives identical Hindi.

    python -I -B -X utf8 build_2-09_2-17_hi.py            # write all nine files + self-check
    python -I -B -X utf8 build_2-09_2-17_hi.py --dry 2-12 # print residues for one file, write nothing
"""
import pathlib
import re
import sys

PIPE = r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi"
sys.path.insert(0, PIPE)
import build_sample_hi as S  # noqa: E402

PALI_DIR = S.PALI_DIR
HI_DIR = S.HI_DIR

FILES = {
    "2-09": "2-09-hinattika.md",
    "2-10": "2-10-micchattaniyatattika.md",
    "2-11": "2-11-maggarammanattika.md",
    "2-12": "2-12-uppannattika.md",
    "2-13": "2-13-atitattika.md",
    "2-14": "2-14-atitarammanattika.md",
    "2-15": "2-15-ajjhattattika.md",
    "2-16": "2-16-ajjhattarammanattika.md",
    "2-17": "2-17-sanidassanasappatighattika.md",
}

# numbers missing from the sample table (Pāli short forms used in these files)
S.NUM.update({"ekavīsa": "इक्कीस", "pañcavīsa": "पच्चीस", "tevīsa": "तेईस", "bāvīsa": "बाईस",
              "dvāvīsa": "बाईस", "ekūnavīsa": "उन्नीस", "vīsa": "बीस", "catuvīsa": "चौबीस"})

# =====================================================================================
# 1. Items (the triad members), Hindi forms: f = with परिघटना (fem.), ms = masc. sg. direct,
#    mo = masc. oblique / plural.  Taken from pi-1 1-matika.md.
# =====================================================================================
A_SUF = r"(?:ānañca|ānaṃ|assa|añca|aṃ|āya|ā|o|e)"
I_SUF = r"(?:īnañca|īnaṃ|issa|iñca|iṃ|ī|i)"
IN_SUF = r"(?:īnaṃ|issa|iñca|iṃ|ī|ino)"


def vala(base):
    """'X वाली' -> (f, ms, mo)."""
    return (base + "ी", base + "ा", base + "े")


def IT(stem, cls, f, ms=None, mo=None):
    suf = {"a": A_SUF, "i": I_SUF, "in": IN_SUF, "ind": ""}[cls]
    return {"rx": stem + suf, "f": f, "ms": ms or f, "mo": mo or f, "one": " " not in f}


MAGGA_AR = ("मार्ग को विषय बनाने वाली", "मार्ग को विषय बनाने वाला", "मार्ग को विषय बनाने वाले")
MAGGA_HE = ("मार्ग को मूल बनाने वाली", "मार्ग को मूल बनाने वाला", "मार्ग को मूल बनाने वाले")
MAGGA_AD = ("मार्ग की प्रधानता वाली", "मार्ग की प्रधानता वाला", "मार्ग की प्रधानता वाले")
ATITA = ("अतीत की", "अतीत का", "अतीत के")
ANAGATA = ("भविष्य की", "भविष्य का", "भविष्य के")
PACCUPPANNA = ("वर्तमान की", "वर्तमान का", "वर्तमान के")
ATITA_AR = ("अतीत के विषय वाली", "अतीत के विषय वाला", "अतीत के विषय वाले")
ANAGATA_AR = ("भविष्य के विषय वाली", "भविष्य के विषय वाला", "भविष्य के विषय वाले")
PACC_AR = ("वर्तमान के विषय वाली", "वर्तमान के विषय वाला", "वर्तमान के विषय वाले")
AJJH = "स्वयं से संबंधित"
BAH = "दूसरों से संबंधित"
AJBA = "स्वयं और दूसरों दोनों से संबंधित"
AJJH_AR = ("स्वयं से संबंधित विषय वाली", "स्वयं से संबंधित विषय वाला", "स्वयं से संबंधित विषय वाले")
BAH_AR = ("दूसरों से संबंधित विषय वाली", "दूसरों से संबंधित विषय वाला", "दूसरों से संबंधित विषय वाले")
AJBA_AR = ("स्वयं और दूसरों दोनों से संबंधित विषय वाली", "स्वयं और दूसरों दोनों से संबंधित विषय वाला",
           "स्वयं और दूसरों दोनों से संबंधित विषय वाले")
SAN = ("दिखाई देने वाली और टकराव वाली", "दिखाई देने वाला और टकराव वाला", "दिखाई देने वाले और टकराव वाले")
ANI_S = ("दिखाई न देने वाली, पर टकराव वाली", "दिखाई न देने वाला, पर टकराव वाला",
         "दिखाई न देने वाले, पर टकराव वाले")
ANI_A = ("दिखाई न देने वाली और टकराव से रहित", "दिखाई न देने वाला और टकराव से रहित",
         "दिखाई न देने वाले और टकराव से रहित")

TRIADS = {  # file key: (heading Hindi keyword, [items...], [extra adjectives...])
    "2-09": ("हीन", [IT("hīn", "a", "हीन"), IT("majjhim", "a", "मध्यम"), IT("paṇīt", "a", "उत्तम")], []),
    "2-10": ("ग़लत दिशा में निश्चित", [IT("micchattaniyat", "a", "ग़लत दिशा में निश्चित"),
                                     IT("sammattaniyat", "a", "सही दिशा में निश्चित"),
                                     IT("aniyat", "a", "अनिश्चित")], []),
    "2-11": ("मार्ग को विषय बनाने वाला", [IT("maggārammaṇ", "a", *MAGGA_AR), IT("maggahetuk", "a", *MAGGA_HE),
                                        IT("maggādhipat", "i", *MAGGA_AD)],
             [(1, IT("maggāhetuk", "a", *MAGGA_HE))]),   # spelling slip in the source
    "2-12": ("उत्पन्न", [IT("uppann", "a", "उत्पन्न हो चुकी", "उत्पन्न हो चुका", "उत्पन्न हो चुके"),
                        IT("anuppann", "a", "उत्पन्न न हुई", "उत्पन्न न हुआ", "उत्पन्न न हुए"),
                        IT("uppād", "in", "उत्पन्न होने वाली", "उत्पन्न होने वाला", "उत्पन्न होने वाले")], []),
    "2-13": ("अतीत", [IT("atīt", "a", *ATITA), IT("anāgat", "a", *ANAGATA), IT("paccuppann", "a", *PACCUPPANNA)],
             [(2, IT("paccuppan", "a", *PACCUPPANNA))]),  # spelling slip "paccuppano"
    "2-14": ("अतीत के विषय", [IT("atītārammaṇ", "a", *ATITA_AR), IT("anāgatārammaṇ", "a", *ANAGATA_AR),
                             IT("paccuppannārammaṇ", "a", *PACC_AR)],
             [(3, IT("atīt", "a", *ATITA)), (4, IT("anāgat", "a", *ANAGATA)), (5, IT("paccuppann", "a", *PACCUPPANNA))]),
    "2-15": ("स्वयं से संबंधित", [IT("ajjhatt", "a", AJJH), IT("bahiddhā", "ind", BAH),
                                IT("ajjhattabahiddhā", "ind", AJBA)], []),
    "2-16": ("स्वयं से संबंधित विषय", [IT("ajjhattārammaṇ", "a", *AJJH_AR), IT("bahiddhārammaṇ", "a", *BAH_AR),
                                     IT("ajjhattabahiddhārammaṇ", "a", *AJBA_AR)],
             [(3, IT("ajjhatt", "a", AJJH)), (4, IT("bahiddhā", "ind", BAH))]),
    "2-17": ("दिखाई देने वाला और टकराव वाला", [IT("sanidassanasappaṭigh", "a", *SAN),
                                              IT("anidassanasappaṭigh", "a", *ANI_S),
                                              IT("anidassanaappaṭigh", "a", *ANI_A)],
             [(2, IT("anidassanāppaṭigh", "a", *ANI_A))]),
}


class Ctx:
    def __init__(self, key):
        self.key = key
        kw, items, extra = TRIADS[key]
        self.kw = kw
        self.items = list(items)
        self.idx = []      # (compiled full-match regex, item index)
        for i, it in enumerate(items):
            self.idx.append((re.compile(it["rx"] + r"$"), i))
        for i, it in extra:
            if i >= len(self.items):
                self.items.extend([None] * (i + 1 - len(self.items)))
                self.items[i] = it
            self.idx.append((re.compile(it["rx"] + r"$"), i))
        alts = sorted({it["rx"] for it in items} | {it["rx"] for _, it in extra}, key=len, reverse=True)
        self.IT = r"(?:" + "|".join(alts) + r")"
        self.ITS = rf"{self.IT}(?: ca)?(?: {self.IT}(?: ca)?)*"
        self.joiner = " तथा " if key == "2-17" else " और "

    def which(self, word):
        for rx, i in self.idx:
            if rx.match(word):
                return i
        raise ValueError("not an item: " + word)

    def which_stem(self, st):
        for suf in ("aṃ", "iṃ", "i", "ī", ""):
            try:
                return self.which(st + suf)
            except ValueError:
                pass
        raise ValueError("not an item stem: " + st)

    def parse(self, its):
        ws = its.split()
        # coordinated ("X ca Y ca", "Xañca Yañca") or stacked adjectives ("atītārammaṇaṃ atītaṃ")
        self.coord = any(w == "ca" or w.endswith("ñca") for w in ws) or len(ws) == 1
        return [self.which(w) for w in ws if w != "ca"]

    def adj(self, idxs, form):
        w = [self.items[i][form] for i in idxs]
        if len(w) == 1:
            return w[0]
        if not getattr(self, "coord", True):
            return ", ".join(w)
        return ", ".join(w[:-1]) + self.joiner + w[-1]

    def one(self, idxs):
        return len(idxs) == 1 and self.items[idxs[0]]["one"]


# =====================================================================================
# 2. Markers (agreement) and placeholders
# =====================================================================================
def MK(code):          # agreement marker emitted by a nominative subject: ms / mp / fs / fp
    return f"\ue001{code}\ue002"


VP = "\ue003"          # "होता है / होती है / होते हैं / होती हैं" chosen from the nearest subject marker
PPH = "\ue004"         # postposition placeholder of an object, chosen from the next verb


def PPM(pp):           # postposition marker emitted by a verb phrase
    return f"\ue005{pp}\ue006"


BE = {"ms": "होता है", "mp": "होते हैं", "fs": "होती है", "fp": "होती हैं"}
ASLOT = ""       # before "रस लेता है": "का" after an object, otherwise "उसका "

# =====================================================================================
# 3. Headings and fixed lines
# =====================================================================================
N = S.NAME
NN = S.NNAME


def cond_heading(p):
    """Hetupaccayo / Naārammaṇapaccayo / Ārammaṇapaccayādi / Natthivigatāvigatapaccayā ..."""
    p = p[0].lower() + p[1:]
    m = re.fullmatch(r"(na|no)?(\w+?)paccay(?:o|ādi)", p)
    if m:
        neg, stem = m.group(1), m.group(2)
        k = _stem_key(stem)
        if k:
            base = NN(k) if neg else N(k)
            return base + (" आदि" if p.endswith("ādi") else "")
    return None


def _stem_key(stem):
    stem = stem[0].lower() + stem[1:]
    for k in S.COND_KEYS:
        if stem == k:
            return k
    return None


HEAD = {
    "Paṭiccavāro": S.VARA["paṭicca"], "Sahajātavāro": S.VARA["sahajāta"], "Paccayavāro": S.VARA["paccaya"],
    "Nissayavāro": S.VARA["nissaya"], "Saṃsaṭṭhavāro": S.VARA["saṃsaṭṭha"],
    "Sampayuttavāro": S.VARA["sampayutta"], "Pañhāvāro": S.VARA["pañhā"],
    "Vibhaṅgavāro": S.VARA["vibhaṅga"], "Saṅkhyāvāro": S.VARA["saṅkhyā"],
    "Paccayānulomaṃ": S.PACCAYANULOMA, "Paccayapaccanīyaṃ": S.PACCAYAPACCANIYA,
    "Paccayānulomapaccanīyaṃ": S.PACCAYANULOMAPACCANIYA,
    "Paccayapaccanīyānulomaṃ": S.PACCAYAPACCANIYANULOMA,
    "Paccanīyānulomaṃ": S.PACCANIYANULOMA,   # short form used as a heading, translated as written
    "Hetudukaṃ": S.DUKANI("hetu"),
    "Nahetudukaṃ": S.DUKANI("hetu", neg=True),
    "Suddhaṃ": S.SUDDHA,
    "Paccanīyuddhāro": "नकारात्मक क्रम के लिए कारणों का संकलन",
    "2-6. Sahajāta-paccaya-nissaya-saṃsaṭṭha-sampayuttavāro":
        "2-6. सह-उत्पत्ति, कारण, आश्रय, घुले-मिले होने और जुड़ाव का खंड",
    "Anantara-samanantarapaccayā": f"{N('anantara')} और {N('samanantara')}",
    "Natthivigatāvigatapaccayā": f"{N('natthi')}, {N('vigata')} और {N('avigata')}",
    "Jhānapaccayādi": f"{N('jhāna')} आदि",
    "4-6. Nissaya-saṃsaṭṭha-sampayuttavāro": "4-6. आश्रय, घुले-मिले होने और जुड़ाव का खंड",
    "Hetusabhāgaṃ": f"{N('hetu')} के सहभागी कारण",
    "Hetusāmaññaghaṭanā (9)": f"{N('hetu')} वाले साझा मेल (9)",
    "Hetusāmaññaghaṭanā": f"{N('hetu')} वाले साझा मेल",
    "Nahetutikaṃ": f"{S.NNAME_OBL('hetu')} के साथ तीन कारणों का मेल",
}


def heading(text, ctx):
    star = text.startswith("*") and text.endswith("*")
    core = text[1:-1] if star else text
    if core in HEAD:
        h = HEAD[core]
    elif core.endswith("ttikaṃ") and core == ctx_title(ctx):
        h = tika_title(ctx)
    else:
        h = cond_heading(core)
        if h is None:
            raise ValueError("unknown heading: " + core)
    return f"*{h}*" if star else h


TITLES = {"2-09": "Hīnattikaṃ", "2-10": "Micchattaniyatattikaṃ", "2-11": "Maggārammaṇattikaṃ",
          "2-12": "Uppannattikaṃ", "2-13": "Atītattikaṃ", "2-14": "Atītārammaṇattikaṃ",
          "2-15": "Ajjhattattikaṃ", "2-16": "Ajjhattārammaṇattikaṃ", "2-17": "Sanidassanasappaṭighattikaṃ"}


def tika_title(ctx):
    return ctx.kw + " तीन का वर्गीकरण" if ctx.kw.endswith("वाला") else S.TIKA(ctx.kw)


def ctx_title(ctx):
    return TITLES[ctx.key]


def fixed_line(p, ctx):
    t = {
        "Anulomaṃ.": S.ANULOMA + "।", "Paccanīyaṃ.": S.PACCANIYA + "।",
        "Anulomapaccanīyaṃ.": S.ANULOMAPACCANIYA + "।", "Paccanīyānulomaṃ.": S.PACCANIYANULOMA + "।",
        "Paccayānulomaṃ.": S.PACCAYANULOMA + "।",     # source slip (for Paccanīyānulomaṃ), kept as written
        "Paṭiccavāro.": S.VARA["paṭicca"] + "।", "Paccayavāro.": S.VARA["paccaya"] + "।",
        "Saṃsaṭṭhavāro.": S.VARA["saṃsaṭṭha"] + "।", "Pañhāvāro.": S.VARA["pañhā"] + "।",
        "Pañhāvāro niṭṭhito.": S.VARA["pañhā"] + " समाप्त।",
        "Dhammānulome tikapaṭṭhānaṃ niṭṭhitaṃ.": f"{S.DHAMMANULOMA}: {S.TIKAPATTHANA} समाप्त।",
        "Dutiyo bhāgo niṭṭhito.": S.BHAGA[2].strip("()") + " समाप्त।",
        ctx_title(ctx) + " niṭṭhitaṃ.": tika_title(ctx) + " समाप्त।",
    }
    return t.get(p)


# =====================================================================================
# 4. Parentheticals and other fixed sentences (exact Pāli -> Hindi)
# =====================================================================================
EVAM = "(इस प्रकार गिनना चाहिए)"
PAREN = {
    "(evaṃ gaṇetabbaṃ)": EVAM,
    "(saṃkhittaṃ)": "(संक्षिप्त)",
    "(paripuṇṇaṃ)": "(परिपूर्ण)",
    "(sabbattha tīṇi)": "(हर जगह तीन)",
    "(saṃkhittaṃ, sabbattha nava)": "(संक्षिप्त, हर जगह नौ)",
    "(sabbattha tīṇi, saṃkhittaṃ)": "(हर जगह तीन, संक्षिप्त)",
    "(imesu padesu ekaṃyeva)": "(इन पदों में एक ही)",
    "(naārammaṇe gahite pakatārammaṇampi upanissayārammaṇampi dvepi chijjanti)":
        "(विषय-कारण का अभाव लेने पर स्वाभाविक विषय भी और प्रबल आश्रय रूपी विषय भी, दोनों ही कट जाते हैं)",
    "(anantarasadisaṃ)": f"({S.SADISA('anantara')})",
    "(anantarasadisā)": f"({S.SADISA('anantara')})",
    "(paṭiccavārasadisaṃ, nava pañhā)": "(निर्भरता के खंड के समान, नौ प्रश्न)",
    "(paṭiccavārasadisaṃ, tisso pañhā)": "(निर्भरता के खंड के समान, तीन प्रश्न)",
    "(kusalattikasadisā, terasa pañhā)": "(हितकर वाले तीन के वर्गीकरण के समान, तेरह प्रश्न)",
    "(kusalattikasadisaṃ, pañca kātabbā)": "(हितकर वाले तीन के वर्गीकरण के समान, पाँच करने चाहिए)",
    "(cakkaṃ kātabbaṃ)": "(चक्र बनाना चाहिए)",
    "(paripuṇṇā dvepi)": "(दोनों ही परिपूर्ण)",
    # --- 2-17
    "(saṃkhittaṃ, sabbe pañhā vibhajitabbā)": "(संक्षिप्त, सभी प्रश्नों का विभाजन करना चाहिए)",
    "(saṃkhittaṃ, sattapi pañhā vibhajitabbā)": "(संक्षिप्त, सातों प्रश्नों का विभाजन करना चाहिए)",
    "(Evaṃ sattapi pañhā vibhajitabbā.)": "(इस प्रकार सातों प्रश्नों का विभाजन करना चाहिए।)",
    "(Evaṃ sattapi pañhā vibhajitabbā)": "(इस प्रकार सातों प्रश्नों का विभाजन करना चाहिए)",
    "(nahetusadisaṃ kātabbaṃ. Paripuṇṇaṃ. Moho natthi)":
        f"({S.SADISA('hetu', neg=True)} करना चाहिए। परिपूर्ण। मोह नहीं है)",
    "(saṃkhittaṃ, sabbattha ekavīsa)": "(संक्षिप्त, हर जगह इक्कीस)",
    "(Sahajātavāropi paccayavāropi nissayavāropi paṭiccavārasadisā, saṃsaṭṭhavāropi sampayuttavāropi arūpeyeva kātabbā.)":
        "(सह-उत्पत्ति का खंड भी, कारण का खंड भी और आश्रय का खंड भी निर्भरता के खंड के समान हैं, "
        "घुले-मिले होने का खंड भी और जुड़ाव का खंड भी केवल अभौतिक में ही करने चाहिए।)",
    "(Anidassanaappaṭighamūlakeyeva iminā kāraṇena satta pañhā vibhajitabbā.)":
        f"({'{AMUL}'} में ही इसी तरीके से सात प्रश्नों का विभाजन करना चाहिए।)",
    "(Anidassanasappaṭighamūlake iminā kāraṇena satta pañhā vibhajitabbā, pariyosānapadā natthi.)":
        "({SMUL} में इसी तरीके से सात प्रश्नों का विभाजन करना चाहिए, अंतिम पद नहीं हैं।)",
    "(Iminā kāraṇena anidassanaappaṭighamūlake satta pañhā vibhajitabbā, niṭṭhānapadā natthi.)":
        "(इसी तरीके से {AMUL} में सात प्रश्नों का विभाजन करना चाहिए, समापन पद नहीं हैं।)",
    "(Iminā kāraṇena sattapi pañhā vibhajitabbā.)": "(इसी तरीके से सातों प्रश्नों का विभाजन करना चाहिए।)",
    "(Anidassanasappaṭighamūlakā satta pañhā iminā kāraṇena vibhajitabbā.)":
        "({SMUL} वाले सात प्रश्नों का इसी तरीके से विभाजन करना चाहिए।)",
    "(Anidassanaappaṭighamūlake satta pañhā iminā kāraṇena kātabbā.)":
        "({AMUL} में सात प्रश्न इसी तरीके से बनाने चाहिए।)",
    "(Iminā kāraṇena satta pañhā vibhajitabbā.)": "(इसी तरीके से सात प्रश्नों का विभाजन करना चाहिए।)",
    "(Anidassanasappaṭighamūlake iminā kāraṇena sattapi pañhā vibhajitabbā.)":
        "({SMUL} में इसी तरीके से सातों प्रश्नों का विभाजन करना चाहिए।)",
    "(Anidassanaappaṭighamūlakā iminā kāraṇena satta pañhā vibhajitabbā.)":
        "({AMUL} वाले सात प्रश्नों का इसी तरीके से विभाजन करना चाहिए।)",
    "(Iminā kāraṇena satta pañhā vitthāretabbā asammohantena.)":
        "(इसी तरीके से बिना भ्रमित हुए सात प्रश्नों का विस्तार करना चाहिए।)",
    "(Anidassanasappaṭighamūlakā iminā kāraṇena sattapi pañhā vitthāretabbā.)":
        "({SMUL} वाले सातों प्रश्नों का इसी तरीके से विस्तार करना चाहिए।)",
    "(Anidassanaappaṭighamūlake iminā kāraṇena sattapi pañhā vitthāretabbā.)":
        "({AMUL} में इसी तरीके से सातों प्रश्नों का विस्तार करना चाहिए।)",
    "(Ghaṭane iminā kāraṇena sattapi pañhā vibhajitabbā.)": "(मेल में इसी तरीके से सातों प्रश्नों का विभाजन करना चाहिए।)",
    "(Iminā kāraṇena ekavīsa pañhā vibhajitabbā.)": "(इसी तरीके से इक्कीस प्रश्नों का विभाजन करना चाहिए।)",
    "(kammaṃ vibhajitvā nakammeneva ekavīsa pañhā kātabbā)":
        f"(कर्म का विभाजन करके {S.NNAME_OBL('kamma')} से ही इक्कीस प्रश्न बनाने चाहिए)",
    "(paṭisandhipi kaṭattāpi natthi, pañcavokāreyeva kātabbā)":
        "(न पुनर्जन्म है, न किए गए कर्म से उत्पन्न भौतिक रूप, केवल पाँच समूहों वाले अस्तित्व में ही करना चाहिए)",
    "(iminā kāraṇena vibhajitabbā ekavīsāpi)": "(इसी तरीके से इक्कीसों का भी विभाजन करना चाहिए)",
    "(ārammaṇasadisaṃ)": f"({S.SADISA('ārammaṇa')})",
    "(Anidassanaappaṭighamūlake sattapi pañhā vibhajitabbā, adhipati tividharūpasaṅgahena.)":
        "({AMUL} में सातों प्रश्नों का विभाजन करना चाहिए, प्रधानता को भौतिक रूप के तीन प्रकार के संग्रह के साथ।)",
    "(paṭiccavārasadisaṃ sādhukaṃ kātabbaṃ. Aññamaññapaccaye paṭiccavāre aññamaññasadisaṃ, nissayapaccaye paṭiccavārasadisaṃ)":
        f"(निर्भरता के खंड के समान भली-भाँति करना चाहिए। {N('aññamañña')} में निर्भरता के खंड के "
        f"{S.SADISA('aññamañña')}, {N('nissaya')} में निर्भरता के खंड के समान)",
    "(Evaṃ satta pañhā vibhajitabbā, tividharūpasaṅgaho.)":
        "(इस प्रकार सात प्रश्नों का विभाजन करना चाहिए, भौतिक रूप का तीन प्रकार का संग्रह।)",
    "(Evaṃ satta pañhā sahajātā nānākkhaṇikā iminā kāraṇena vibhajitabbā, tividharūpasaṅgaho.)":
        "(इस प्रकार सह-उत्पत्ति और भिन्न क्षण वाले सात प्रश्नों का इसी तरीके से विभाजन करना चाहिए, "
        "भौतिक रूप का तीन प्रकार का संग्रह।)",
    "(Evaṃ satta pañhā vitthāretabbā, pavattipaṭisandhi.)":
        "(इस प्रकार सात प्रश्नों का विस्तार करना चाहिए, प्रक्रिया और पुनर्जन्म।)",
    "(Evaṃ satta pañhā pavattipaṭisandhi vibhajitabbā, sattasupi kabaḷīkāro āhāro kātabbo.)":
        "(इस प्रकार प्रक्रिया और पुनर्जन्म में सात प्रश्नों का विभाजन करना चाहिए, सातों में ही कौर-कौर खाया "
        "जाने वाला भोजन लेना चाहिए।)",
    "(Evaṃ pavattipaṭisandhi satta pañhā vibhajitabbā, rūpajīvitindriyañca ante ante.)":
        f"(इस प्रकार प्रक्रिया और पुनर्जन्म में सात प्रश्नों का विभाजन करना चाहिए, और {S.RUPAJIVITINDRIYA} "
        "हर एक के अंत में।)",
    "(Avasesā pañca pañhā evaṃ vitthāretabbā. Sahajātā, pacchājātā.)":
        "(शेष पाँच प्रश्नों का इस प्रकार विस्तार करना चाहिए। सह-उत्पत्ति, पश्चात्-उत्पत्ति।)",
    "(Paṭiccavāre nissayapaccayasadisaṃ.)": f"(निर्भरता के खंड में {S.SADISA('nissaya')}।)",
    "(yāva asaññasattā vitthāretabbā)": "(पहचान-रहित प्राणियों तक विस्तार करना चाहिए)",
    "(Avasesā cattāro pañhā vitthāretabbā. Paṭiccavāre sahajātapaccayasadisā, ninnānākaraṇā.)":
        f"(शेष चार प्रश्नों का विस्तार करना चाहिए। निर्भरता के खंड में {S.SADISA('sahajāta')}, कोई अंतर नहीं।)",
    "(evaṃ avasesā cha pañhā vibhajitabbā. Sahajātaṃ, pacchājātaṃ, āhāraṃ, indriyampi kātabbā)":
        "(इस प्रकार शेष छह प्रश्नों का विभाजन करना चाहिए। सह-उत्पत्ति, पश्चात्-उत्पत्ति, आहार और क्षमता भी "
        "लेने चाहिए)",
    "(saṃkhittaṃ, asaññasattānañca kātabbā)": "(संक्षिप्त, पहचान-रहित प्राणियों के भी करने चाहिए)",
    "(yāva asaññasattā kātabbā)": "(पहचान-रहित प्राणियों तक करने चाहिए)",
    "(Avasesā catasso pañhā vibhajitabbā.)": "(शेष चार प्रश्नों का विभाजन करना चाहिए।)",
    "(Natthivigatapaccayaṃ anantarasadisaṃ. Avigatapaccayaṃ atthisadisaṃ.)":
        f"({N('natthi')} और {N('vigata')} {S.SADISA('anantara')} हैं। {N('avigata')} {S.SADISA('atthi')} है।)",
    "(Evaṃ sabbo gaṇanavāro gaṇetabbo.)": "(इस प्रकार पूरे गणना के खंड की गिनती करनी चाहिए।)",
    "(paṭhamagamanasadisaṃ)": "(पहले क्रम के समान)",
    "(idhāpi saṃkhittaṃ)": "(यहाँ भी संक्षिप्त)",
    "(sabbattha ekaṃ)": S.SABBATTHA_EKAM,
    "(avipākaṃ-4)": f"({N('vipāka')} रहित 4)",
    "(savipākaṃ-5)": f"({N('vipāka')} सहित 5)",
    "(nahetusadiso. Moho natthi)": f"({S.SADISA('hetu', neg=True)}। मोह नहीं है)",
    "(sabbattha dve )": "(हर जगह दो)", "(sabbattha dve. Evaṃ gaṇetabbaṃ)": "(हर जगह दो। इस प्रकार गिनना चाहिए)",
    "(saṃkhittaṃ, sabbattha cattāri)": "(संक्षिप्त, हर जगह चार)",
    "(anulomasahajātasadisaṃ, ninnānākaraṇaṃ)": f"(सकारात्मक क्रम के {S.SADISA('sahajāta')}, कोई अंतर नहीं)",
    "(nahetusadisaṃ. Moho natthi)": f"({S.SADISA('hetu', neg=True)}। मोह नहीं है)",
    "(paṭisandhi natthi)": "(पुनर्जन्म नहीं है)",
    "(paṭiccavārasadisaṃ)": "(निर्भरता के खंड के समान)",
    "(vatthuṃ atirekaṃ, paṭiccavārasadisaṃ)": "(आधार अतिरिक्त है, निर्भरता के खंड के समान)",
    "(sahajātavāre paripuṇṇā)": "(सह-उत्पत्ति के खंड में परिपूर्ण)",
    "(mahābhūtānaṃ khandhānañca pacchā pañcāyatanāni ca vatthu ca kātabbā)":
        "(महाभूतों और समूहों के बाद पाँच इंद्रिय-क्षेत्र और आधार भी लेने चाहिए)",
    "(pavattipaṭisandhipi mahābhūtāpi kātabbā)": "(प्रक्रिया और पुनर्जन्म भी, महाभूत भी लेने चाहिए)",
    "(sahajātasadisaṃ)": f"({S.SADISA('sahajāta')})",
    "(paṭiccavārapaccanīye vippayuttasadisaṃ)":
        f"(निर्भरता के खंड के नकारात्मक क्रम में {S.SADISA('vippayutta')})",
    "(Nissayavāro paccayavārasadiso. Saṃsaṭṭhavāropi sampayuttavāropi vitthāretabbo.)":
        f"({S.VARA['nissaya']} {S.VARA['paccaya']} के समान है। {S.VARA['saṃsaṭṭha']} भी और "
        f"{S.VARA['sampayutta']} भी, इनका विस्तार करना चाहिए।)",
    "(rūpajīvitindriyampi vitthāretabbaṃ)": f"({S.RUPAJIVITINDRIYA} का भी विस्तार करना चाहिए)",
    "(mātikāpadāni anumajjantena vitthāretabbāni)":
        "(मूल सूची के पदों को ध्यान से देखते हुए उनका विस्तार करना चाहिए)",
    "(bahiddhā ninnānākaraṇaṃ, mātikāpadāni vitthāretabbāni)":
        "(दूसरों से संबंधित में कोई अंतर नहीं, मूल सूची के पदों का विस्तार करना चाहिए)",
    "(purejātasadisaṃ)": f"({S.SADISA('purejāta')})",
    "(pavattipaṭisandhi)": "(प्रक्रिया और पुनर्जन्म)",
    "(purimā purimā bahiddhāti nānākaraṇaṃ, taṃyeva gamanaṃ)":
        "(“पहले-पहले के दूसरों से संबंधित”, यही अंतर है, वही क्रम है)",
    "(ajjhattasadisaṃyeva)": "(स्वयं से संबंधित के समान ही)",
    "(paripuṇṇaṃ, paṭiccavārasadisaṃ)": "(परिपूर्ण, निर्भरता के खंड के समान)",
    "(saṃkhittaṃ, sabbattha cha kātabbā)": "(संक्षिप्त, हर जगह छह करने चाहिए)",
    "(anulomapadāni gaṇetabbāni)": "(सकारात्मक क्रम के पद गिनने चाहिए)",
    "(saṃkhittaṃ, sabbattha dve)": "(संक्षिप्त, हर जगह दो)",
    "(pañca pañhā)": "(पाँच प्रश्न)",
    "(paṭhamaghaṭane tīṇi)": "(पहले मेल में तीन)",
    "(dutiyaghaṭane tīṇi pañhā)": "(दूसरे मेल में तीन प्रश्न)",
    "(paripuṇṇaṃ, arūpanti niyāmetabbaṃ)": "(परिपूर्ण, “अभौतिक लोक में” ऐसा निर्धारित करना चाहिए)",
    "(Sahajātavāropi paccayavāropi nissayavāropi saṃsaṭṭhavāropi sampayuttavāropi paṭiccavārasadiso.)":
        "(सह-उत्पत्ति का खंड भी, कारण का खंड भी, आश्रय का खंड भी, घुले-मिले होने का खंड भी और जुड़ाव का खंड भी "
        "निर्भरता के खंड के समान है।)",
    "(Sahajātavāropi paccayavāropi nissayavāropi saṃsaṭṭhavāropi sampayuttavāropi paṭiccavārasadisā.)":
        "(सह-उत्पत्ति का खंड भी, कारण का खंड भी, आश्रय का खंड भी, घुले-मिले होने का खंड भी और जुड़ाव का खंड भी "
        "निर्भरता के खंड के समान हैं।)",
    "(iminā kāraṇena sattarasa pañhā kātabbā)": "(इसी तरीके से सत्रह प्रश्न बनाने चाहिए)",
    "(tīsupi sattarasa pañhā kātabbā)": "(तीनों में ही सत्रह प्रश्न बनाने चाहिए)",
    "(anantarasadisaṃ. Nava pañhā kātabbā, āvajjanā na kātabbā)":
        f"({S.SADISA('anantara')}। नौ प्रश्न बनाने चाहिए, मन को विषय की ओर मोड़ना नहीं लेना चाहिए)",
    "(nānākkhaṇikā natthi, sattarasa pañhā kātabbā)": "(भिन्न क्षण वाला नहीं है, सत्रह प्रश्न बनाने चाहिए)",
    "(ime satta paccayā sattarasa pañhā hetusadisā)": f"(ये सात कारण, सत्रह प्रश्न, {S.SADISA('hetu')})",
    "(sattarasa pañhā)": "(सत्रह प्रश्न)",
    "(adhipatiyā paṭisandhi natthi)": f"({S.LOC('adhipati')} पुनर्जन्म नहीं है)",
    "(purejātepi āsevanepi paṭisandhi natthi)":
        f"({S.LOC('purejāta')} भी और {S.LOC('āsevana')} भी पुनर्जन्म नहीं है)",
    "(vipākaṃ atītārammaṇaṃ ekaṃ khandhaṃ, tissopi pañhā paripuṇṇā. Pavattipaṭisandhi kātabbā)":
        "(कर्म के फल रूपी, अतीत के विषय वाला एक समूह, तीनों ही प्रश्न परिपूर्ण हैं। "
        "प्रक्रिया और पुनर्जन्म दोनों लेने चाहिए)",
    "(anulomasahajātasadisaṃ)": f"(सकारात्मक क्रम के {S.SADISA('sahajāta')})",
    "(naadhipatisadisā)": f"({S.SADISA('adhipati', neg=True)})",
    "(navipāke paṭisandhi natthi)": f"({S.NLOC('vipāka')} पुनर्जन्म नहीं है)",
    "(nahetusadisā tisso pañhā, moho natthi )": f"({S.SADISA('hetu', neg=True)} तीन प्रश्न, मोह नहीं है)",
    "(tayopi paccayā paṭiccavārasadisā)": "(तीनों ही कारण निर्भरता के खंड के समान)",
    "(uppannattike atthisadisaṃ)": f"(उत्पन्न वाले तीन के वर्गीकरण में {S.SADISA('atthi')})",
    "(tisso pañhā)": "(तीन प्रश्न)",
    "(dve pañhā micchattaniyatasadisā)": "(दो प्रश्न, ग़लत दिशा में निश्चित परिघटना के समान)",
    "(tīṇi pañhā, micchattasadisaṃ)": "(तीन प्रश्न, ग़लती वाले के समान)",
    "(sabbe paccayā iminā kāraṇena vitthāretabbā. Saṃkhittaṃ)":
        "(सभी कारणों का इसी तरीके से विस्तार करना चाहिए। संक्षिप्त)",
    "(saṃkhittaṃ, sabbāni paccayāni vitthāretabbāni)": "(संक्षिप्त, सभी कारणों का विस्तार करना चाहिए)",
    "(saṃkhittaṃ, kusalattike paccayavārasadisaṃ vibhajitabbaṃ)":
        "(संक्षिप्त, हितकर वाले तीन के वर्गीकरण में कारण के खंड के समान विभाजन करना चाहिए)",
    "(Sahajātavāro paṭiccavārasadiso.)": f"({S.VARA['sahajāta']} {S.VARA['paṭicca']} के समान है।)",
    "(Nissayavāro paccayavārasadiso)": f"({S.VARA['nissaya']} {S.VARA['paccaya']} के समान है)",
    "(Sampayuttavāro saṃsaṭṭhavārasadiso)": f"({S.VARA['sampayutta']} {S.VARA['saṃsaṭṭha']} के समान है)",
    "(Hīnattikaṃ saṃkiliṭṭhattikasadisaṃ vitthāretabbaṃ paripuṇṇaṃ.)":
        f"(हीन वाले तीन के वर्गीकरण का, क्लेशों से मलिन वाले तीन के वर्गीकरण के समान, पूरा विस्तार करना चाहिए।)",
}

SMUL = "दिखाई न देने वाली, पर टकराव वाली परिघटना से शुरू होने वाली शृंखला"     # anidassanasappaṭighamūlaka
AMUL = "दिखाई न देने वाली और टकराव से रहित परिघटना से शुरू होने वाली शृंखला"   # anidassanaappaṭighamūlaka
for _k in PAREN:
    PAREN[_k] = PAREN[_k].replace("{SMUL}", SMUL).replace("{AMUL}", AMUL)

# =====================================================================================
# 5. Count lines
# =====================================================================================
COUNT_START = re.compile(r"^(?:na|no)?\w+?(?:paccayā|yā|e)\s")


def count_line(p):
    pieces = re.split(r"(\([^()]*\))", p)
    out = []
    for piece in pieces:
        if not piece:
            continue
        if piece.startswith("("):
            if piece not in PAREN:
                raise ValueError("paren: " + piece)
            out.append(" " + PAREN[piece])
        else:
            s = piece.strip()
            if not s:
                continue
            h = S.count_hi(s)
            if out and not h.startswith((",", "।", "…")):
                h = " " + h
            out.append(h)
    return "".join(out).strip()


GH_RX = re.compile(r"((?:[A-Za-zāīūñṃ]+ ?- ?)+[A-Za-zāīūñṃ]+)nti ")


def _gh_names(comp):
    out = []
    for part in re.split(r"\s*-\s*", comp.lower()):
        if part in S.COND_KEYS:
            out.append(N(part))
            continue
        for k in S.COND_KEYS:          # two names run together: aññamaññanissaya, atthiavigata
            if part.startswith(k) and part[len(k):] in S.COND_KEYS:
                out += [N(k), N(part[len(k):])]
                break
        else:
            raise ValueError("ghaṭanā part: " + part)
    return ", ".join(out[:-1]) + " और " + out[-1]


def ghatana(p):
    """Hetu-sahajāta-nissaya-atthi-avigatanti satta. … -> “मूल-कारण, … और अविलीनता-कारण” के मेल में सात।"""
    parts = GH_RX.split(p)
    out = []
    for i in range(1, len(parts), 2):
        comp, rest = parts[i], parts[i + 1].strip()
        first = re.match(r"[^\s,.…(]+", rest).group(0)
        join = "के मेल में" if first in S.NUM else "के मेल से,"
        out.append(f"“{_gh_names(comp)}” {join} {count_line(rest)}")
    return " ".join(out)


def try_count(p):
    if not COUNT_START.match(p[0].lower() + p[1:]):
        return None
    try:
        return count_line(p)
    except ValueError:
        return None


# =====================================================================================
# 6. Vocabulary
# =====================================================================================
CSR, KTR, UPR = S.CSR, S.KTR, S.UPR
AHETUKA, ARUPE = S.AHETUKA, S.ARUPE
REV_SG, REV_PL = S.REVIEW_SG, S.REVIEW_PL
ANICCA3 = S.ANICCA3
KILESA_PL = "मन के क्लेशों"

# condition stems
STEMS = "|".join(sorted(S.COND_KEYS, key=len, reverse=True))
COND = rf"(?:na|no)?(?:{STEMS})paccayā"


def cond_hi(w):
    m = re.fullmatch(rf"(na|no)?({STEMS})paccayā", w)
    return S.NABL(m.group(2)) if m.group(1) else S.ABL(m.group(2))


DEP_HI = {"paṭicca": "पर निर्भर होकर", "paccayā": "के कारण", "nissāya": "के आश्रय से",
          "saṃsaṭṭho": "से घुल-मिलकर", "saṃsaṭṭhā": "से घुल-मिलकर",
          "sampayutto": "से जुड़कर", "sampayuttā": "से जुड़कर",
          "sahajāto": "के साथ जन्म लेकर", "sahajātā": "के साथ जन्म लेकर"}
DEPW = "|".join(DEP_HI)

# nouns usable after item adjectives: pāli -> (hindi, gender, number, kind, numeral, marker)
#   kind: nom (direct, emits marker) / acc (oblique + postposition placeholder) / dat (oblique + के लिए)
NOUNS = {
    "ekaṃ khandhaṃ": ("समूह", "m", "sg", "acc", "एक"),
    "eko khandho": ("समूह", "m", "sg", "nom", "एक"),
    "tayo khandhā": ("समूह", "m", "pl", "nom", "तीन"),
    "khandhānaṃ": ("समूहों", "m", "pl", "dat", None),
    "khandhā": ("समूह", "m", "pl", "nom", None),
    "khandhe": ("समूहों", "m", "pl", "acc", None),
    "khandho": ("समूह", "m", "sg", "nom", None),
    "hetū": ("मूल", "m", "pl", "nom", None),
    "cetanā": ("इरादा", "m", "sg", "nom", None),
    "adhipati": ("प्रधानता", "f", "sg", "nom", None),
    "rāgo": ("राग", "m", "sg", "nom", None),
    "domanassaṃ": ("उदासी", "f", "sg", "nom", None),
    "domanassassa": ("उदासी", "f", "sg", "dat", None),
    "cittasamuṭṭhānaṃ rūpaṃ": (CSR, "m", "sg", "nom", None),
    "kaṭattārūpaṃ": (KTR, "m", "sg", "nom", None),
    "upādārūpaṃ": (UPR, "m", "sg", "nom", None),
    "mahābhūtā": ("महाभूत", "m", "pl", "nom", None),
    "mahābhūte": ("महाभूतों", "m", "pl", "acc", None),
    "ekaṃ mahābhūtaṃ": ("महाभूत", "m", "sg", "acc", "एक"),
    "saddhaṃ": ("श्रद्धा", "f", "sg", "acc", None),
    "saddhā": ("श्रद्धा", "f", "sg", "nom", None),
    "saddhāya": ("श्रद्धा", "f", "sg", "dat", None),
    "sīlaṃ": ("सदाचार", "m", "sg", "acc", None),
    "rāgaṃ": ("राग", "m", "sg", "acc", None),
    "dosaṃ": ("द्वेष", "m", "sg", "acc", None),
    "utuṃ": ("तापमान", "m", "sg", "acc", None),
    "bhojanaṃ": ("भोजन", "m", "sg", "acc", None),
    "cakkhuṃ": ("आँख", "f", "sg", "acc", None),
    "sotaṃ": ("कान", "m", "sg", "acc", None),
    "rūpe": ("दृश्य रूपों", "m", "pl", "acc", None),
    "iddhividhañāṇaṃ": ("अलौकिक शक्तियों के ज्ञान", "m", "sg", "acc", None),
    "viññāṇañcāyatanaṃ": ("अनंत चेतना के क्षेत्र", "m", "sg", "acc", None),
    "cuticittaṃ": ("मृत्यु का मन", "m", "sg", "nom", None),
    "paṭisandhicittaṃ": ("पुनर्जन्म का मन", "m", "sg", "nom", None),
    "paṭisandhicittassa": ("पुनर्जन्म के मन", "m", "sg", "dat", None),
    "bhavaṅgaṃ": ("जीवन-धारा का मन", "m", "sg", "nom", None),
    "bhavaṅgassa": ("जीवन-धारा के मन", "m", "sg", "dat", None),
    "āvajjanāya": ("मन को विषय की ओर मोड़ने", "m", "sg", "dat", None),
    "vuṭṭhānassa": ("बाहर आने", "m", "sg", "dat", None),
    "aniccānupassanā, dukkhānupassanā, anattānupassanā":
        ("अनित्यता का अवलोकन, दुःख का अवलोकन और आत्मा से रहित होने का अवलोकन", "m", "pl", "nom", None),
    "aniccānupassanāya, dukkhānupassanāya, anattānupassanāya":
        ("अनित्यता के अवलोकन, दुःख के अवलोकन और आत्मा से रहित होने के अवलोकन", "m", "pl", "dat", None),
    "khandhe ca mahābhūte ca": ("समूहों और महाभूतों", "m", "pl", "acc", None),
    "khandhe ca vatthuñca": ("समूहों और आधार", "m", "pl", "acc", None),
    "ekaṃ khandhañca vatthuñca": ("समूह और आधार", "m", "sg", "acc", "एक"),
    "āhārā": ("आहार", "m", "pl", "nom", None),
    "indriyā": ("क्षमताएँ", "f", "pl", "nom", None),
    "utu… bhojanaṃ… senāsanaṃ": ("तापमान… भोजन… निवास-स्थान", "m", "sg", "nom", None),
    "utu": ("तापमान", "m", "sg", "nom", None),
    "ghānaṃ": ("नाक", "f", "sg", "acc", None),
    "jivhaṃ": ("जीभ", "f", "sg", "acc", None),
    "kāyaṃ": ("शरीर", "m", "sg", "acc", None),
    "sadde": ("ध्वनियों", "f", "pl", "acc", None),
    "gandhe": ("गंधों", "f", "pl", "acc", None),
    "rase": ("स्वादों", "m", "pl", "acc", None),
    "phoṭṭhabbe": ("स्पर्शों", "m", "pl", "acc", None),
    "vatthuṃ": ("आधार", "m", "sg", "acc", None),
    "rūpāyatanaṃ": (S.AYA_OBJ("rūpa"), "m", "sg", "nom", None),
    "phoṭṭhabbāyatanaṃ": (S.AYA_OBJ("phoṭṭhabba"), "m", "sg", "nom", None),
    "cakkhāyatanaṃ": (S.AYA_SENSE("cakkhu"), "m", "sg", "nom", None),
    "kāyāyatanaṃ": (S.AYA_SENSE("kāya"), "m", "sg", "nom", None),
    "cakkhuviññāṇassa": ("आँख की चेतना", "f", "sg", "dat", None),
    "kāyaviññāṇassa": ("शरीर की चेतना", "f", "sg", "dat", None),
    "kāyassa": ("शरीर", "m", "sg", "dat", None),
    "kabaḷīkāro āhāro": ("कौर-कौर खाया जाने वाला भोजन", "m", "sg", "nom", None),
    "anulomaṃ": ("अनुरूपता", "f", "sg", "nom", None),
    "cittasamuṭṭhānañca rūpaṃ": (CSR, "m", "sg", "nom", None),
    "cittasamuṭṭhānaṃ rūpaṃ kaṭattārūpaṃ upādārūpaṃ": (f"{CSR}, {KTR}, {UPR}", "m", "sg", "nom", None),
    "cittasamuṭṭhānaṃ rūpaṃ kaṭatārūpaṃ upādārūpaṃ": (f"{CSR}, {KTR}, {UPR}", "m", "sg", "nom", None),
    "cittasamuṭṭhānaṃ rūpaṃ upādārūpaṃ": (f"{CSR}, {UPR}", "m", "sg", "nom", None),
    "kaṭattārūpaṃ upādārūpaṃ": (f"{KTR}, {UPR}", "m", "sg", "nom", None),
    "mahābhūte ca āpodhātuñca": ("महाभूतों और जल तत्व", "m", "pl", "acc", None),
    "ekaṃ mahābhūtañca āpodhātuñca": ("महाभूत और जल तत्व", "m", "sg", "acc", "एक"),
    "kaṭattā ca rūpaṃ": (KTR, "m", "sg", "nom", None),
    "kaṭatārūpaṃ": (KTR, "m", "sg", "nom", None),            # spelling slip in the source
    "cittasamuṭṭhānānañca rūpānaṃ": (S.CSR_OBL, "m", "pl", "dat", None),
    "cittasamuṭṭhānānaṃ rūpānaṃ": (S.CSR_OBL, "m", "pl", "dat", None),
    "cittasamuṭṭhānānaṃ rūpānaṃ kaṭattārūpānaṃ upādārūpānaṃ":
        (f"{S.CSR_OBL} के लिए, {S.KTR_OBL} के लिए, {S.UPR_OBL}", "m", "pl", "dat", None),
    "kaṭattārūpānaṃ upādārūpānaṃ": (f"{S.KTR_OBL} के लिए, {S.UPR_OBL}", "m", "pl", "dat", None),
    "kaṭattārūpānaṃ": (S.KTR_OBL, "m", "pl", "dat", None),
    "upādārūpānaṃ": (S.UPR_OBL, "m", "pl", "dat", None),
    "ekaṃ mahābhūtaṃ dvinnaṃ mahābhūtānaṃ": ("महाभूत", "m", "sg", "nom", "एक", " दो महाभूतों के लिए"),
    "upapatticittassa": ("उत्पत्ति के मन", "m", "sg", "dat", None),
    "dibbaṃ cakkhuṃ": ("दिव्य आँख", "f", "sg", "acc", None),
    "dibbaṃ sotadhātuṃ": ("दिव्य कान के तत्व", "m", "sg", "acc", None),
    "rāgo uppajjati": ("राग", "m", "sg", "nom", None, " उत्पन्न होता है"),
    "khandhā uppajjanti": ("समूह", "m", "pl", "nom", None, " उत्पन्न होते हैं"),
    "eko khandho ca vatthu ca": ("समूह और आधार", "m", "pl", "nom", "एक"),
    "khandhā ca mahābhūtā ca": ("समूह और महाभूत", "m", "pl", "nom", None),
    "khandhā ca kabaḷīkāro āhāro ca": ("समूह और कौर-कौर खाया जाने वाला भोजन", "m", "pl", "nom", None),
    "khandhā ca rūpajīvitindriyañca": (f"समूह और {S.RUPAJIVITINDRIYA}", "m", "pl", "nom", None),
    "vipākānaṃ khandhānaṃ": ("कर्म के फल रूपी समूहों", "m", "pl", "dat", None),
    "domanassaṃ": ("उदासी", "f", "sg", "nom", None),
}
AND_NOUNS = {"cittasamuṭṭhānañca rūpaṃ", "kaṭattā ca rūpaṃ", "cittasamuṭṭhānānañca rūpānaṃ"}
SAMPADA = {"vaṇṇa": "रंग-रूप", "sadda": "ध्वनि", "gandha": "गंध", "rasa": "स्वाद", "phoṭṭhabba": "स्पर्श",
           "cakkhu": "आँख", "sota": "कान", "ghāna": "नाक", "jivhā": "जीभ", "kāya": "शरीर"}
for _k, _v in SAMPADA.items():
    NOUNS[_k + "sampadaṃ"] = (f"{_v} की संपन्नता", "f", "sg", "acc", None)
    NOUNS[_k + "sampadā"] = (f"{_v} की संपन्नता", "f", "sg", "nom", None)
# plain (no item) object nouns of the sense chains
SENSE_ACC = {"cakkhuṃ": "आँख", "sotaṃ": "कान", "ghānaṃ": "नाक", "jivhaṃ": "जीभ", "kāyaṃ": "शरीर",
             "rūpe": "दृश्य रूपों", "sadde": "ध्वनियों", "gandhe": "गंधों", "rase": "स्वादों",
             "phoṭṭhabbe": "स्पर्शों"}
NANA = {"iddhividhañāṇassa": S.IDDHIVIDHA_OBL, "cetopariyañāṇassa": S.CETOPARIYA_OBL,
        "pubbenivāsānussatiñāṇassa": S.PUBBENIVASA_OBL, "yathākammūpagañāṇassa": S.YATHAKAMMUPAGA_OBL,
        "anāgataṃsañāṇassa": S.ANAGATAMSA_OBL}
NANA_RX = "|".join(NANA)
NANA_NOM = {"iddhividhañāṇaṃ": "अलौकिक शक्तियों का ज्ञान", "cetopariyañāṇaṃ": "दूसरों के मन को जानने का ज्ञान",
            "pubbenivāsānussatiñāṇaṃ": "पूर्व जन्मों के अनुस्मरण का ज्ञान",
            "yathākammūpagañāṇaṃ": "प्राणियों के अपने कर्मों के अनुसार जाने का ज्ञान",
            "anāgataṃsañāṇaṃ": "भविष्य को जानने का ज्ञान"}
for _k, _v in NANA.items():   # accusative objects: "… के ज्ञान को / पर"
    NOUNS[_k[:-4] + "aṃ"] = (_v, "m", "sg", "acc", None)


def nana_run(m):
    """iddhividhañāṇassa, cetopariyañāṇassa, …, āvajjanāya -> 'A, B और C के लिए तथा मन को … के लिए'."""
    words = re.findall(NANA_RX, m.group(1))
    names = [NANA[w] for w in words]
    h = names[0] if len(names) == 1 else ", ".join(names[:-1]) + " और " + names[-1]
    h += " के लिए"
    if m.group(2):
        h += " तथा " + S.AVAJJANA_FOR
    return h
NOUN_RX = "|".join(re.escape(k) for k in sorted(NOUNS, key=len, reverse=True))


def np_hi(ctx, idxs, noun, prefix=""):
    hi, g, num, kind, numeral, *rest = NOUNS[noun]
    suffix = rest[0] if rest else ""
    if g == "f":
        form = "f"
    elif kind == "nom" and num == "sg":
        form = "ms"
    else:
        form = "mo"
    adj = ctx.adj(idxs, form)
    if numeral:
        core = f"{numeral} {adj} {hi}" if ctx.one(idxs) else f"{adj} {numeral} {hi}"
    else:
        core = f"{adj} {hi}"
    core = prefix + core
    if kind == "nom":
        code = ("f" if g == "f" else "m") + ("s" if num == "sg" else "p")
        return core + MK(code) + suffix
    if kind == "acc":
        return core + PPH + suffix
    return core + " के लिए" + suffix


# plain nominative subjects (emit an agreement marker)
def NOM(hi, code):
    return hi + MK(code)


PLAIN = {
    # --- frames inside explanations
    "ekaṃ khandhaṃ": "एक समूह" + PPH, "eko khandho": NOM("एक समूह", "ms"),
    "tayo khandhā": NOM("तीन समूह", "mp"), "tayo khandhe": "तीन समूहों" + PPH,
    "dve khandhe": "दो समूहों" + PPH, "dve khandhā": NOM("दो समूह", "mp"),
    "khandhe": "समूहों" + PPH, "khandhā": NOM("समूह", "mp"), "khandho": NOM("समूह", "ms"),
    "khandhānaṃ": "समूहों के लिए",
    "tiṇṇannaṃ khandhānaṃ": "तीन समूहों के लिए", "dvinnaṃ khandhānaṃ": "दो समूहों के लिए",
    "ekaṃ mahābhūtaṃ": "एक महाभूत" + PPH, "tayo mahābhūtā": NOM("तीन महाभूत", "mp"),
    "dve mahābhūtā": NOM("दो महाभूत", "mp"), "tayo mahābhūte": "तीन महाभूतों" + PPH,
    "dve mahābhūte": "दो महाभूतों" + PPH, "mahābhūte": "महाभूतों" + PPH,
    "mahābhūtā": NOM("महाभूत", "mp"), "tiṇṇannaṃ mahābhūtānaṃ": "तीन महाभूतों के लिए",
    "vatthuṃ": "आधार" + PPH, "vatthu": NOM("आधार", "ms"), "vatthussa": "आधार के लिए",
    "vatthussa ca": "और आधार के लिए",
    "cittasamuṭṭhānaṃ rūpaṃ kaṭattārūpaṃ upādārūpaṃ": NOM(f"{CSR}, {KTR}, {UPR}", "ms"),
    "cittasamuṭṭhānaṃ rūpaṃ upādārūpaṃ": NOM(f"{CSR}, {UPR}", "ms"),
    "kaṭattārūpaṃ upādārūpaṃ": NOM(f"{KTR}, {UPR}", "ms"),
    "cittasamuṭṭhānaṃ rūpaṃ": NOM(CSR, "ms"), "cittasamuṭṭhānañca rūpaṃ": S.AND_CSR,
    "kaṭattā ca rūpaṃ": S.AND_KTR, "kaṭattārūpaṃ": NOM(KTR, "ms"), "upādārūpaṃ": NOM(UPR, "ms"),
    "cittasamuṭṭhānānaṃ rūpānaṃ kaṭattārūpānaṃ upādārūpānaṃ":
        f"{S.CSR_OBL} के लिए, {S.KTR_OBL} के लिए, {S.UPR_OBL} के लिए",
    "kaṭattārūpānaṃ upādārūpānaṃ": f"{S.KTR_OBL} के लिए, {S.UPR_OBL} के लिए",
    "cittasamuṭṭhānānaṃ rūpānaṃ": f"{S.CSR_OBL} के लिए",
    "cittasamuṭṭhānānañca rūpānaṃ": f"और {S.CSR_OBL} के लिए",
    "kaṭattā ca rūpānaṃ": f"और {S.KTR_OBL} के लिए",
    "kaṭattārūpānaṃ": f"{S.KTR_OBL} के लिए",
    "sampayuttakānaṃ khandhānaṃ": f"{S.SAMPAYUTTAKA_KH_OBL} के लिए",
    "paṭisandhikkhaṇe": S.PATISANDHI, "ahetukapaṭisandhikkhaṇe": S.AHETUKA_PATISANDHI,
    "arūpe": ARUPE, "ahetukaṃ": AHETUKA + ",",
    "bāhiraṃ": S.BAHIRA, "āhārasamuṭṭhānaṃ": S.AHARASAM, "utusamuṭṭhānaṃ": S.UTUSAM,
    "asaññasattānaṃ": S.ASANNASATTA,
    "vicikicchāsahagate uddhaccasahagate khandhe paṭicca vicikicchāsahagato uddhaccasahagato moho":
        f"{S.KHE_VU_TEXT} {S.MOHA_VU}",
    "vicikicchāsahagate uddhaccasahagate khandhe ca vatthuñca paccayā vicikicchāsahagato uddhaccasahagato moho":
        f"{S.KHANDHE_VU} और आधार के कारण {S.MOHA_VU}",
    "pañcaviññāṇasahagataṃ ekaṃ khandhaṃ": f"{S.PANCAVINNANA_SAHAGATA} एक समूह" + PPH,
    "pañcaviññāṇaṃ": "पाँच प्रकार की चेतना",
    "cakkhāyatanaṃ paccayā cakkhuviññāṇaṃ": "आँख के इंद्रिय-क्षेत्र के कारण आँख की चेतना",
    "kāyāyatanaṃ paccayā kāyaviññāṇaṃ": "शरीर के इंद्रिय-क्षेत्र के कारण शरीर की चेतना",
    # --- pañhāvāra
    "sahajātaṃ, purejātaṃ, pacchājātaṃ, āhāraṃ, indriyaṃ": "सह-उत्पत्ति, पूर्व-उत्पत्ति, पश्चात्-उत्पत्ति, आहार, क्षमता",
    "sahajātaṃ, purejātaṃ, pacchājātaṃ": "सह-उत्पत्ति, पूर्व-उत्पत्ति, पश्चात्-उत्पत्ति",
    "sahajātaṃ, pacchājātaṃ, āhāraṃ, indriyaṃ": "सह-उत्पत्ति, पश्चात्-उत्पत्ति, आहार, क्षमता",
    "sahajātaṃ, pacchājātaṃ": "सह-उत्पत्ति, पश्चात्-उत्पत्ति",
    "sahajātaṃ, purejātaṃ": "सह-उत्पत्ति, पूर्व-उत्पत्ति",
    "sahajātā, nānākkhaṇikā": "सह-उत्पत्ति, भिन्न क्षण",
    "sahajātā –": "सह-उत्पत्ति –", "nānākkhaṇikā –": "भिन्न क्षण –",
    "sahajāto –": "सह-उत्पत्ति –", "purejātaṃ –": "पूर्व-उत्पत्ति –", "pacchājātā –": "पश्चात्-उत्पत्ति –",
    "sahajātaṃ –": "सह-उत्पत्ति –",
    # --- micchattaniyata prose
    "mātughātikammassa": "माता की हत्या के कर्म के लिए", "pitughātikammassa": "पिता की हत्या के कर्म के लिए",
    "arahantaghātikammassa": "अर्हत् की हत्या के कर्म के लिए",
    "ruhiruppādakammassa": "बुद्ध का खून बहाने के कर्म के लिए",
    "saṅghabhedakammassa": "संघ में फूट डालने के कर्म के लिए",
    "mātughātikammaṃ": NOM("माता की हत्या का कर्म", "ms"), "pitughātikammaṃ": NOM("पिता की हत्या का कर्म", "ms"),
    "arahantaghātikammaṃ": NOM("अर्हत् की हत्या का कर्म", "ms"),
    "ruhiruppādakammaṃ": NOM("बुद्ध का खून बहाने का कर्म", "ms"),
    "saṅghabhedakammaṃ": NOM("संघ में फूट डालने का कर्म", "ms"),
    "niyatamicchādiṭṭhiyā": "निश्चित ग़लत दृष्टि के लिए",
    "niyatamicchādiṭṭhi": NOM("निश्चित ग़लत दृष्टि", "fs"),
    "aniyatamicchādiṭṭhi": NOM("अनिश्चित ग़लत दृष्टि", "fs"),
    "paṭhamo maggo": NOM("पहला मार्ग", "ms"), "tatiyo maggo": NOM("तीसरा मार्ग", "ms"),
    "dutiyassa maggassa": "दूसरे मार्ग के लिए", "catutthassa maggassa": "चौथे मार्ग के लिए",
    "paṭhamassa maggassa parikammaṃ paṭhamassa maggassa":
        NOM("पहले मार्ग की प्रारंभिक तैयारी", "fs") + " पहले मार्ग के लिए",
    "catutthassa maggassa parikammaṃ catutthassa maggassa":
        NOM("चौथे मार्ग की प्रारंभिक तैयारी", "fs") + " चौथे मार्ग के लिए",
    "paṭhamassa jhānassa parikammaṃ tasseva": NOM("पहले ध्यान की प्रारंभिक तैयारी", "fs") + " उसी के लिए",
    "nevasaññānāsaññāyatanassa parikammaṃ tasseva":
        NOM("न पहचान न अ-पहचान के क्षेत्र की प्रारंभिक तैयारी", "fs") + " उसी के लिए",
    "paṭhamaṃ jhānaṃ dutiyassa jhānassa": NOM("पहला ध्यान", "ms") + " दूसरे ध्यान के लिए",
    "pāṇātipāto pāṇātipātassa": NOM("जीव-हत्या", "fs") + " जीव-हत्या के लिए",
    "mātaraṃ jīvitā voropetvā": "माता की जान लेकर", "pitaraṃ jīvitā voropetvā": "पिता की जान लेकर",
    "arahantaṃ jīvitā voropetvā": "अर्हत् की जान लेकर",
    "duṭṭhena cittena tathāgatassa lohitaṃ uppādetvā": "द्वेष से भरे मन से तथागत का खून बहाकर",
    "saṅghaṃ bhinditvā": "संघ में फूट डालकर", "tassa paṭighātatthāya": "उसके निवारण के लिए",
    "mātaraṃ jīvitā voropeti": "माता की जान लेता है", "nigamaghātaṃ karoti": "कस्बे पर डाका डालता है",
    "saṅkhāre": "निर्मित परिघटनाओं" + PPH, "ariyānaṃ": "आर्यों के",
    "atthappaṭisambhidāya": "अर्थ के विश्लेषणात्मक ज्ञान के लिए",
    "ṭhānāṭhānakosallassa": "संभव और असंभव को जानने की कुशलता के लिए",
    "vuṭṭhānassa": "बाहर आने के लिए",
    "dve khandhā ca": NOM("दो समूह और", "mp"),
    "sahajātā…pe…": "सह-उत्पत्ति…",
    # --- sanidassana prose
    "āpodhātuṃ": "जल तत्व" + PPH, "āpodhātu ca": NOM("और जल तत्व", "ms"), "āpodhātu": NOM("जल तत्व", "ms"),
    "mahābhūte ca āpodhātuñca": "महाभूतों और जल तत्व" + PPH,
    "ekaṃ mahābhūtañca āpodhātuñca": "एक महाभूत और जल तत्व" + PPH,
    "dve mahābhūte ca āpodhātuñca": "दो महाभूतों और जल तत्व" + PPH,
    "phoṭṭhabbāyatanañca āpodhātuñca": "स्पर्श के इंद्रिय-क्षेत्र और जल तत्व" + PPH,
    "phoṭṭhabbāyatanaṃ paṭicca": "स्पर्श के इंद्रिय-क्षेत्र पर निर्भर होकर",
    "itthindriyaṃ": NOM("स्त्रीत्व की क्षमता", "fs") + PPH, "purisindriyaṃ": NOM("पुरुषत्व की क्षमता", "fs") + PPH,
    "jīvitindriyaṃ": NOM("जीवन-क्षमता", "fs") + PPH, "indriyaṃ": NOM("क्षमता", "fs"),
    "kabaḷīkāraṃ āhāraṃ": "कौर-कौर खाए जाने वाले भोजन" + PPH,
    "dānaṃ datvā sīlaṃ samādiyitvā uposathakammaṃ katvā taṃ garuṃ katvā": f"{S.DANA3}, उसे महत्व देकर",
    "nibbānaṃ garuṃ katvā": "निर्वाण को महत्व देकर",
    "cakkhuviññāṇassa": "आँख की चेतना के लिए", "purejātaṃ": "पूर्व-उत्पत्ति", "vatthu ca": NOM("और आधार", "ms"),
    "ekaṃ mahābhūtaṃ dvinnaṃ mahābhūtānaṃ": NOM("एक महाभूत", "ms") + " दो महाभूतों के लिए",
    "rasāyatanaṃ": NOM(S.AYA_OBJ("rasa"), "ms"),
    "saddāyatanaṃ sotaviññāṇassa": NOM(S.AYA_OBJ("sadda"), "ms") + " कान की चेतना के लिए",
    "cakkhāyatanassa": "आँख के इंद्रिय-क्षेत्र के लिए", "rasāyatanassa": "स्वाद के इंद्रिय-क्षेत्र के लिए",
    "itthindriyassa": "स्त्रीत्व की क्षमता के लिए",
    "kabaḷīkārāhārassa ca": "और कौर-कौर खाए जाने वाले भोजन के लिए",
    "dvinnaṃ mahābhūtānaṃ": "दो महाभूतों के लिए",
    "dve mahābhūtā ekassa mahābhūtassa": NOM("दो महाभूत", "mp") + " एक महाभूत के लिए",
    "utusamuṭṭhānā mahābhūtā": NOM("तापमान से उत्पन्न महाभूत", "mp"),
    "vicikicchā uppajjati": "संशय उत्पन्न होता है", "uddhaccaṃ uppajjati": "बेचैनी उत्पन्न होती है",
    "phalā vuṭṭhahitvā": "फल से उठकर", "phalaṃ": "फल" + PPH, "rūpaṃ": "दृश्य रूप" + PPH,
    "kaṭatārūpaṃ": NOM(KTR, "ms"),
    "paro": "दूसरा व्यक्ति", "bahiddhādhipati": NOM("दूसरों से संबंधित प्रधानता", "fs"),
    "nirodhā vuṭṭhahantassa": "समाप्ति की ध्यान-अवस्था से बाहर आ रहे व्यक्ति का",
    "nevasaññānāsaññāyatanaṃ phalasamāpattiyā": NOM("न पहचान न अ-पहचान का क्षेत्र", "ms") + " फल की ध्यान-अवस्था के लिए",
    "pañcaviññāṇasahagataṃ": S.PANCAVINNANA_SAHAGATA, "ajjhattikā indriyā": NOM("स्वयं से संबंधित क्षमताएँ", "fp"),
    "āhāraṃ –": "आहार –", "purejātaṃ, āhāraṃ": "पूर्व-उत्पत्ति, आहार",
    "rūpāyatanaṃ": NOM(S.AYA_OBJ("rūpa"), "ms"), "phoṭṭhabbāyatanaṃ": NOM(S.AYA_OBJ("phoṭṭhabba"), "ms"),
    "cakkhāyatanaṃ": NOM(S.AYA_SENSE("cakkhu"), "ms"), "kāyāyatanaṃ": NOM(S.AYA_SENSE("kāya"), "ms"),
    "assādeti, abhinandati": ASLOT + f"रस लेता है, उस{S.ABHINANDA}",
    "dānaṃ datvā sīlaṃ samādiyitvā uposathakammaṃ katvā, taṃ garuṃ katvā paccavekkhati":
        f"{S.DANA3}, उसे महत्व देकर उस पर {REV_SG}",
    "pubbe suciṇṇāni": S.SUCINNA + PPH, "jhānā vuṭṭhahitvā": "ध्यान से उठकर", "jhānaṃ": "ध्यान" + PPH,
    "maggā vuṭṭhahitvā": "मार्ग से उठकर", "pubbe samudāciṇṇe": f"पहले बार-बार उठे",
    "nevasaññānāsaññāyatanaṃ": "न पहचान न अ-पहचान के क्षेत्र" + PPH,
    **{k[:-4] + "aṃ": v + PPH for k, v in NANA.items()},
    "dibbaṃ cakkhuṃ": "दिव्य आँख" + PPH, "dibbaṃ sotadhātuṃ": "दिव्य कान के तत्व" + PPH,
    "ārammaṇapurejātaṃ, vatthupurejātaṃ": f"{S.ARAMMANAPUREJATA}, {S.VATTHUPUREJATA}",
    "ārammaṇapurejātaṃ –": f"{S.ARAMMANAPUREJATA} –", "vatthupurejātaṃ –": f"{S.VATTHUPUREJATA} –",
    "ārammaṇādhipati, sahajātādhipati": f"{S.ARAMMANADHIPATI}, {S.SAHAJATADHIPATI}",
    "ārammaṇādhipati sahajātādhipati": f"{S.ARAMMANADHIPATI}, {S.SAHAJATADHIPATI}",
    "ārammaṇādhipati –": f"{S.ARAMMANADHIPATI} –", "sahajātādhipati –": f"{S.SAHAJATADHIPATI} –",
    "ārammaṇūpanissayo, anantarūpanissayo, pakatūpanissayo":
        f"{S.ARAMMANUPANISSAYA}, {S.ANANTARUPANISSAYA}, {S.PAKATUPANISSAYA}",
    "ārammaṇūpanissayo, pakatūpanissayo": f"{S.ARAMMANUPANISSAYA}, {S.PAKATUPANISSAYA}",
    "anantarūpanissayo, pakatūpanissayo": f"{S.ANANTARUPANISSAYA}, {S.PAKATUPANISSAYA}",
    "pakatūpanissayo –": f"{S.PAKATUPANISSAYA} –", "ārammaṇūpanissayo –": f"{S.ARAMMANUPANISSAYA} –",
    "purimā purimā": "पहले-पहले के", "pacchimānaṃ pacchimānaṃ": "बाद-बाद के",
    "purejātassa imassa kāyassa": "पहले उत्पन्न इस शरीर के लिए",
    "imassa kāyassa": "इस शरीर के लिए",
    "kabaḷīkāro āhāro": NOM("कौर-कौर खाया जाने वाला भोजन", "ms"),
    "rūpajīvitindriyaṃ": NOM(S.RUPAJIVITINDRIYA, "fs"),
    "rūpajīvitindriyañca": NOM("और " + S.RUPAJIVITINDRIYA, "fs"),
    "pacchājātā": "बाद में उत्पन्न",
    "vipāko": "कर्म के फल रूपी",
    "vipākānaṃ khandhānaṃ": "कर्म के फल रूपी समूहों के लिए",
    "vipākānaṃ": "कर्म के फल रूपी",
    "nibbānaṃ maggassa": NOM("निर्वाण", "ms") + " मार्ग के लिए",
    "nibbānaṃ": NOM("निर्वाण", "ms"),
    "maggo phalassa": NOM("मार्ग", "ms") + " फल के लिए",
    "phalaṃ phalassa": NOM("फल", "ms") + " फल के लिए",
    "anulomaṃ gotrabhussa": NOM("अनुरूपता", "fs") + " गोत्र-परिवर्तन के लिए",
    "anulomaṃ vodānassa": NOM("अनुरूपता", "fs") + " शुद्धि के लिए",
    "anulomaṃ phalasamāpattiyā": NOM("अनुरूपता", "fs") + " फल की ध्यान-अवस्था के लिए",
    "gotrabhu maggassa": NOM("गोत्र-परिवर्तन", "ms") + " मार्ग के लिए",
    "vodānaṃ maggassa": NOM("शुद्धि", "fs") + " मार्ग के लिए",
    "nirodhā vuṭṭhahantassa nevasaññānāsaññāyatanaṃ phalasamāpattiyā":
        "समाप्ति की ध्यान-अवस्था से बाहर आ रहे व्यक्ति का " + NOM("न पहचान न अ-पहचान का क्षेत्र", "ms")
        + " फल की ध्यान-अवस्था के लिए",
    "gotrabhussa": "गोत्र-परिवर्तन के लिए", "vodānassa": "शुद्धि के लिए", "phalassa": "फल के लिए",
    "maggassa": "मार्ग के लिए", "phalasamāpattiyā": "फल की ध्यान-अवस्था के लिए",
    "maggo": NOM("मार्ग", "ms"),
    "āvajjanā": NOM("मन को विषय की ओर मोड़ना", "ms"),
    "paccavekkhaṇā paccavekkhaṇāya": NOM("पुनः विचार", "ms") + " पुनः विचार के लिए",
    "ākāsānañcāyatanaṃ viññāṇañcāyatanassa": NOM("अनंत आकाश का क्षेत्र", "ms") + " अनंत चेतना के क्षेत्र के लिए",
    "ākiñcaññāyatanaṃ nevasaññānāsaññāyatanassa":
        NOM("कुछ भी न होने का क्षेत्र", "ms") + " न पहचान न अ-पहचान के क्षेत्र के लिए",
    "rūpāyatanaṃ cakkhuviññāṇassa": NOM(S.AYA_OBJ("rūpa"), "ms") + " आँख की चेतना के लिए",
    "phoṭṭhabbāyatanaṃ kāyaviññāṇassa": NOM(S.AYA_OBJ("phoṭṭhabba"), "ms") + " शरीर की चेतना के लिए",
    "cakkhāyatanaṃ cakkhuviññāṇassa": NOM(S.AYA_SENSE("cakkhu"), "ms") + " आँख की चेतना के लिए",
    "kāyāyatanaṃ kāyaviññāṇassa": NOM(S.AYA_SENSE("kāya"), "ms") + " शरीर की चेतना के लिए",
    "cakkhundriyaṃ cakkhuviññāṇassa": NOM(S.INDRIYA_SENSE("cakkhu"), "fs") + " आँख की चेतना के लिए",
    "kāyindriyaṃ kāyaviññāṇassa": NOM(S.INDRIYA_SENSE("kāya"), "fs") + " शरीर की चेतना के लिए",
    "rūpāyatanaṃ cakkhuviññāṇassa …pe…": NOM(S.AYA_OBJ("rūpa"), "ms") + " आँख की चेतना के लिए…",
    "cakkhāyatanaṃ cakkhuviññāṇassa …pe…": NOM(S.AYA_SENSE("cakkhu"), "ms") + " आँख की चेतना के लिए…",
    # --- ārammaṇa / adhipati prose
    "dānaṃ datvā sīlaṃ samādiyitvā uposathakammaṃ katvā taṃ paccavekkhati":
        f"{S.DANA3} उस पर {REV_SG}",
    "dānaṃ datvā sīlaṃ samādiyitvā uposathakammaṃ katvā taṃ garuṃ katvā paccavekkhati":
        f"{S.DANA3}, उसे महत्व देकर उस पर {REV_SG}",
    "dānaṃ datvā sīlaṃ samādiyitvā uposathakammaṃ…pe… paccavekkhati":
        f"दान देकर, सदाचार ग्रहण करके, उपवास-व्रत… {REV_SG}",
    "dānaṃ datvā sīlaṃ samādiyitvā…pe…": "दान देकर, सदाचार ग्रहण करके…",
    "pubbe suciṇṇāni paccavekkhati": f"{S.SUCINNA} पर {REV_SG}",
    "pubbe suciṇṇāni garuṃ katvā paccavekkhati": f"{S.SUCINNA} को महत्व देकर उन पर {REV_SG}",
    "jhānā vuṭṭhahitvā jhānaṃ paccavekkhati": f"ध्यान से उठकर ध्यान पर {REV_SG}",
    "jhānā vuṭṭhahitvā jhānaṃ garuṃ katvā paccavekkhati": f"ध्यान से उठकर ध्यान को महत्व देकर उस पर {REV_SG}",
    "jhānā…pe…": "ध्यान से…",
    "ariyā maggā vuṭṭhahitvā maggaṃ paccavekkhanti": f"आर्य मार्ग से उठकर मार्ग पर {REV_PL}",
    "ariyā maggā vuṭṭhahitvā maggaṃ garuṃ katvā paccavekkhanti":
        f"आर्य मार्ग से उठकर मार्ग को महत्व देकर उस पर {REV_PL}",
    "ariyā phalaṃ paccavekkhanti": f"आर्य फल पर {REV_PL}",
    "ariyā phalaṃ garuṃ katvā paccavekkhanti": f"आर्य फल को महत्व देकर उस पर {REV_PL}",
    "phalaṃ paccavekkhanti": f"फल पर {REV_PL}",
    "phalaṃ garuṃ katvā paccavekkhanti": f"फल को महत्व देकर उस पर {REV_PL}",
    "nibbānaṃ paccavekkhanti": f"निर्वाण पर {REV_PL}",
    "nibbānaṃ garuṃ katvā paccavekkhanti": f"निर्वाण को महत्व देकर उस पर {REV_PL}",
    "pahīne kilese paccavekkhanti": f"छोड़े जा चुके {KILESA_PL} पर {REV_PL}",
    "vikkhambhite kilese paccavekkhanti": f"दबाए जा चुके {KILESA_PL} पर {REV_PL}",
    "pubbe samudāciṇṇe kilese jānanti": f"पहले बार-बार उठे {KILESA_PL} को जानते हैं",
    "ariyā": "आर्य",
    "dibbena cakkhunā rūpaṃ passati": "दिव्य आँख से दृश्य रूप देखता है",
    "dibbāya sotadhātuyā saddaṃ suṇāti": "दिव्य कान के तत्व से ध्वनि सुनता है",
    "dibbāya sotudhātuyā saddaṃ suṇāti": "दिव्य कान के तत्व से ध्वनि सुनता है",   # spelling slip in 2-12
    "aniccato dukkhato anattato vipassati": PPM("को") + f"{ANICCA3} {S.VIPASSATI}",
    "aniccato dukkhato anattato vipassanti": PPM("को") + f"{ANICCA3} {S.VIPASSANTI}",
    "aniccato dukkhato anattato": PPM("को") + ANICCA3,
    "aniccato": PPM("को") + "अनित्य",
    "vipassati": PPM("को") + S.VIPASSATI, "vipassanti": PPM("को") + S.VIPASSANTI,
    "vipassati assādeti abhinandati": PPM("को") + f"{S.VIPASSATI}, " + ASLOT + f"रस लेता है, उस{S.ABHINANDA}",
    "assādeti abhinandati": ASLOT + f"रस लेता है, उस{S.ABHINANDA}",
    "assādenti abhinandanti": ASLOT + "रस लेते हैं, उसमें आनंद लेते हैं",
    "ekaṃ mahābhūtaṃ tiṇṇannaṃ mahābhūtānaṃ": NOM("एक महाभूत", "ms") + " तीन महाभूतों के लिए",
    "utu… bhojanaṃ… senāsanaṃ": NOM("तापमान… भोजन… निवास-स्थान", "ms"),
    **{k: v + PPH for k, v in SENSE_ACC.items()},
    **{k + "sampadaṃ": f"{v} की संपन्नता" + PPH for k, v in SAMPADA.items()},
    **{k + "sampadā": NOM(f"{v} की संपन्नता", "fs") for k, v in SAMPADA.items()},
    "garuṃ katvā paccavekkhati": PPM("को") + f"महत्व देकर उस पर {REV_SG}",
    "garuṃ katvā paccavekkhanti": PPM("को") + f"महत्व देकर उस पर {REV_PL}",
    "garuṃ katvā": PPM("को") + "महत्व देकर",
    "paccavekkhati": PPM("पर") + REV_SG, "paccavekkhanti": PPM("पर") + REV_PL,
    "taṃ ārabbha": "उसे विषय बनाकर", "taṃ garuṃ katvā": "उसे महत्व देकर",
    "rāgo uppajjati": "राग उत्पन्न होता है", "diṭṭhi uppajjati": "दृष्टि उत्पन्न होती है",
    "domanassaṃ uppajjati": "उदासी उत्पन्न होती है",
    "rāgo": "राग", "diṭṭhi": "दृष्टि", "vicikicchā": "संशय", "uddhaccaṃ": "बेचैनी",
    "cetopariyañāṇena": S.CETOPARIYENA,
    # --- upanissaya prose
    "upanissāya": PPM("के") + "प्रबल आश्रय से",
    "patthayamāno": PPM("की") + "कामना करते हुए",
    "dānaṃ deti": "दान देता है", "sīlaṃ samādiyati": "सदाचार ग्रहण करता है",
    "uposathakammaṃ karoti": "उपवास-व्रत का पालन करता है", "uposathakammaṃ": "उपवास-व्रत",
    "jhānaṃ uppādeti": "ध्यान उत्पन्न करता है", "samāpattiṃ uppādeti": "ध्यान-अवस्था उत्पन्न करता है",
    "vipassanaṃ": "अंतर्दृष्टि", "maggaṃ": "मार्ग" + PPH, "abhiññaṃ": "उच्च ज्ञान", "samāpattiṃ": "ध्यान-अवस्था",
    "mānaṃ jappeti": "अहंकार पालता है", "diṭṭhiṃ gaṇhāti": "दृष्टि ग्रहण करता है",
    "pāṇaṃ hanati": "जीव-हत्या करता है", "saṅghaṃ bhindati": "संघ में फूट डालता है",
    "kāyikassa sukhassa": "शारीरिक सुख के लिए", "kāyikassa dukkhassa": "शारीरिक दुःख के लिए",
    "kāyikaṃ sukhaṃ": "शारीरिक सुख" + PPH, "kāyikaṃ dukkhaṃ": "शारीरिक दुःख" + PPH,
    "paññāya": "प्रज्ञा के लिए", "paññaṃ": "प्रज्ञा" + PPH, "paññā": "प्रज्ञा",
    "patthanaṃ": "कामना" + PPH, "patthanāya": "कामना के लिए", "patthanā": "कामना",
    "rāgassa": "राग के लिए", "senāsanaṃ": "निवास-स्थान" + PPH,
    "bhojanaṃ": "भोजन" + PPH, "utu": "तापमान",
    "kāyikassa": "शारीरिक",
    "rāgaṃ": "राग" + PPH, "dosaṃ": "द्वेष" + PPH, "sīlaṃ": "सदाचार" + PPH, "saddhaṃ": "श्रद्धा" + PPH,
    "sutaṃ": "सुना-सीखा ज्ञान" + PPH, "cāgaṃ": "त्याग" + PPH, "utuṃ": "तापमान" + PPH,
    "saddhā": NOM("श्रद्धा", "fs"), "saddhāya": "श्रद्धा के लिए",
    "āvajjanāya": S.AVAJJANA_FOR,
}
PLAIN_KEYS = sorted(PLAIN, key=len, reverse=True)

# phrases applied before the item rules (they contain words that are items in other files)
PRE = {
    "rūpāyatanañca cakkhāyatanañca cakkhuviññāṇañca cakkhuviññāṇasahagatānaṃ khandhānaṃ":
        NOM(f"{S.AYA_OBJ('rūpa')}, {S.AYA_SENSE('cakkhu')} और आँख की चेतना", "mp")
        + " आँख की चेतना के साथ होने वाले समूहों के लिए",
    "cakkhundriyañca cakkhuviññāṇañca cakkhuviññāṇasahagatānaṃ khandhānaṃ":
        NOM("आँख की क्षमता और आँख की चेतना", "fp") + " आँख की चेतना के साथ होने वाले समूहों के लिए",
    "kāyindriyañca kāyaviññāṇañca kāyaviññāṇasahagatānaṃ khandhānaṃ":
        NOM("शरीर की क्षमता और शरीर की चेतना", "fp") + " शरीर की चेतना के साथ होने वाले समूहों के लिए",
    "anuppannaṃ samāpattiṃ uppādenti, uppannaṃ samāpajjanti":
        "उत्पन्न न हुई ध्यान-अवस्था उत्पन्न करते हैं, उत्पन्न हो चुकी ध्यान-अवस्था में प्रवेश करते हैं",
}


# =====================================================================================
# 7. Regex rules with items (compiled per file)
# =====================================================================================
def item_rules(ctx):
    IT_, ITS = ctx.IT, ctx.ITS
    R = []

    def add(rx, fn):
        R.append((re.compile(rx), fn))

    # (1) dependent frame:  X dhammaṃ paṭicca Y dhammo uppajjati <conditions>
    chain = rf"{COND}(?:(?:\s?…pe…\s?|\s?…\s?|,\s|\s)(?:\([^()]*\)(?:\s?…pe…\s?|\s?…\s?|,\s|\s))?{COND})*"

    def frame(m):
        o = ctx.parse(m.group("obj"))
        r = ctx.parse(m.group("res"))
        objhi = " और ".join(f"{ctx.items[i]['f']} {S.DHAMMA}" for i in o) if len(o) < 3 else \
            ", ".join(f"{ctx.items[i]['f']} {S.DHAMMA}" for i in o[:-1]) + f" और {ctx.items[o[-1]]['f']} {S.DHAMMA}"
        if len(r) == 1:
            reshi = f"{ctx.items[r[0]]['f']} {S.DHAMMA}"
        else:
            reshi = ctx.adj(r, "f") + " " + S.DHAMMA_PL
        verb = "उत्पन्न होती हैं" if m.group("verb") == "uppajjanti" else "उत्पन्न होती है"
        ch = re.sub(COND, lambda c: cond_hi(c.group(0)), m.group("chain"))
        return f"{objhi} {DEP_HI[m.group('dep')]} {reshi} {ch} {verb}"

    add(rf"^(?P<obj>{ITS}) dhammaṃ (?P<dep>{DEPW}) (?P<res>{ITS}) dhamm(?:o|ā) "
        rf"(?P<verb>uppajjati|uppajjanti) (?P<chain>{chain})", frame)

    # (2) pañhā frame:  X dhammo Y dhammassa ...
    def panha(m):
        s_ = ctx.parse(m.group("src"))
        d = ctx.parse(m.group("dst"))
        if len(s_) == 1:
            src = NOM(f"{ctx.items[s_[0]]['f']} {S.DHAMMA}", "fs")
        else:
            src = NOM(ctx.adj(s_, "f") + " " + S.DHAMMA_PL, "fp")
        dst = " और ".join(f"{ctx.items[i]['f']} {S.DHAMMA}" for i in d) + " के लिए"
        return f"{src}, {dst} "

    add(rf"(?:^|(?<=\(\d\) ))(?P<src>{ITS}) dhamm(?:o|ā) (?P<dst>{ITS})(?: dhammassa)? ", panha)

    # (3) item + ādhipati compound:  micchattaniyatādhipati / maggārammaṇādhipati
    def adhip(m):
        i = ctx.which_stem(m.group(1))
        return NOM(f"{ctx.items[i]['f']} प्रधानता", "fs")

    add(rf"\b({'|'.join(_stems(ctx))})ādhipati\b", adhip)

    # (4) cittasamaṅgissa compounds: micchattaniyatacittasamaṅgissa cittaṃ jānāti/jānanti
    def samangi(m):
        parts = [p for p in re.findall("|".join(_stems(ctx)), m.group(1))]
        idxs = [ctx.which_stem(p) for p in parts]
        ctx.coord = ctx.key == "2-11"
        verb = "जानते हैं" if m.group(2) == "jānanti" else "जानता है"
        return f"{ctx.adj(idxs, 'mo')} मन से युक्त व्यक्ति के मन को {verb}"

    add(rf"\b((?:(?:{'|'.join(_stems(ctx))})[aiī]?)+)cittasamaṅgissa cittaṃ (jānāti|jānanti)\b", samangi)

    # (2b) pañhā frame with two subjects: X dhammo ca Y dhammo ca Z dhammassa
    def panha2(m):
        a, b = ctx.which(m.group(1)), ctx.which(m.group(2))
        d = ctx.parse(m.group("dst"))
        dst = " और ".join(f"{ctx.items[i]['f']} {S.DHAMMA}" for i in d) + " के लिए"
        src = f"{ctx.items[a]['f']} {S.DHAMMA} और {ctx.items[b]['f']} {S.DHAMMA}"
        return f"{NOM(src, 'fp')}, {dst} "

    add(rf"(?:^|(?<=\(\d\) ))({IT_}) dhammo ca ({IT_}) dhammo ca (?P<dst>{ITS})(?: dhammassa)? ", panha2)

    # (2c) pairs: "bahiddhā rūpāyatanañca ajjhattaṃ cakkhāyatanañca", "X kabaḷīkāro āhāro ca Y kabaḷīkāro āhāro ca"
    AYA = {"rūpāyatanañca": S.AYA_OBJ("rūpa"), "phoṭṭhabbāyatanañca": S.AYA_OBJ("phoṭṭhabba"),
           "cakkhāyatanañca": S.AYA_SENSE("cakkhu"), "kāyāyatanañca": S.AYA_SENSE("kāya"),
           "vatthu ca": "आधार", "cakkhu ca": "आँख", "kabaḷīkāro āhāro ca": "कौर-कौर खाया जाने वाला भोजन"}
    AYA_G = {"cakkhu ca": "f"}

    def pair(m):
        out = []
        for its, n in ((m.group(1), m.group(2)), (m.group(3), m.group(4))):
            hi = AYA[n]
            if its:
                idxs = ctx.parse(its)
                hi = f"{ctx.adj(idxs, 'f' if AYA_G.get(n) == 'f' else 'ms')} {hi}"
            out.append(hi)
        return NOM(" और ".join(out), "mp")

    ayx = "|".join(re.escape(k) for k in sorted(AYA, key=len, reverse=True))
    add(rf"\b(?:({ITS}) )?({ayx}) (?:({ITS}) )?({ayx})(?![\wṃ])", pair)

    # (4b) "bahiddhā cittasamaṅgissa (cittaṃ jānāti)"
    def samangi2(m):
        idxs = ctx.parse(m.group(1))
        tail = ""
        if m.group(2):
            tail = " मन को " + ("जानते हैं" if m.group(2) == "jānanti" else "जानता है")
        return f"{ctx.adj(idxs, 'mo')} मन से युक्त व्यक्ति के" + tail

    add(rf"\b({ITS}) cittasamaṅgissa(?: cittaṃ (jānāti|jānanti))?(?![\wṃ])", samangi2)

    # (6b) (purejātassa) imassa X kāyassa
    def kaya(m):
        idxs = ctx.parse(m.group(2))
        pre = "पहले उत्पन्न " if m.group(1) else ""
        return f"{pre}इस {ctx.adj(idxs, 'mo')} शरीर के लिए"

    add(rf"\b(purejātassa )?imassa ({ITS}) kāyassa\b", kaya)

    # (7) yaṃ vatthuṃ parāmasantassa X khandhā uppajjanti, taṃ vatthu
    def yam(m):
        idxs = ctx.parse(m.group(1))
        return (f"जिस आधार को ग़लत ढंग से पकड़े रहने वाले व्यक्ति में {ctx.adj(idxs, 'mo')} समूह उत्पन्न होते हैं, "
                f"वह आधार" + MK("ms"))

    add(rf"\byaṃ vatthuṃ parāmasantassa ({ITS}) khandhā uppajjanti, taṃ vatthu\b", yam)

    # (7b) a knowledge as subject before "X vuṭṭhānassa": anāgatārammaṇaṃ iddhividhañāṇaṃ atītārammaṇassa vuṭṭhānassa
    def nana_nom(m):
        hi = NANA_NOM[m.group(2)]
        if m.group(1):
            idxs = ctx.parse(m.group(1))
            hi = f"{ctx.adj(idxs, 'ms')} {hi}"
        return NOM(hi, "ms") + " "

    add(rf"\b(?:({ITS}) )?({'|'.join(NANA_NOM)}) (?=(?:{ITS}) vuṭṭhānassa)", nana_nom)

    # (5) item adjectives + noun
    def npm(m):
        pre = m.group("pre") or ""
        idxs = ctx.parse(m.group("its"))
        noun = m.group("noun")
        prefix = ""
        kind = NOUNS[noun][3]
        before = m.string[:m.start()]
        if noun in AND_NOUNS:
            prefix = "और "
        elif "ñca" in m.group("its").split()[-1] and kind == "dat":
            prefix = "और "
        elif "ñca" in m.group("its").split()[-1] and kind == "nom":
            if re.search(r"(?:khandhā|khandho|\ue002),? $", before):
                prefix = "और "
        hi = np_hi(ctx, idxs, noun, prefix)
        p = []
        for w in pre.split():
            p.append({"arūpe": ARUPE, "ahetukaṃ": AHETUKA + ",", "ahetuke": AHETUKA + ",",
                      "ahetukā": AHETUKA + ",", "vipāko": "कर्म के फल रूपी", "vipākaṃ": "कर्म के फल रूपी",
                      "pacchājātā": "बाद में उत्पन्न", "purimā": "पहले-पहले के", "pacchimānaṃ": "बाद-बाद के",
                      "sampayuttakānaṃ": "जुड़े हुए,", "vipākānaṃ": "कर्म के फल रूपी,",
                      "pañcaviññāṇasahagataṃ": S.PANCAVINNANA_SAHAGATA + ",", "vipākā": "कर्म के फल रूपी"}[w])
        out = " ".join(dict.fromkeys(p)) if False else " ".join(_dedup_pairs(p))
        if out:
            if ctx.one(idxs) and out.endswith(","):
                out = out[:-1]
            return out + " " + hi
        return hi

    add(rf"\b(?P<pre>(?:(?:arūpe|ahetukaṃ|ahetuke|ahetukā|vipāko|vipākaṃ|pacchājātā|purimā purimā|"
        rf"pacchimānaṃ pacchimānaṃ|sampayuttakānaṃ|vipākānaṃ|pañcaviññāṇasahagataṃ|vipākā) )*)(?P<its>{ITS}) (?P<noun>{NOUN_RX})(?![\wṃ])", npm)

    # (6) item + pahīne/vikkhambhite kilese
    def kil(m):
        idxs = ctx.parse(m.group(1))
        sep = " " if ctx.one(idxs) else ", "
        return f"{ctx.adj(idxs, 'mo')}{sep}" + {"pahīne": "छोड़े जा चुके", "vikkhambhite": "दबाए जा चुके"}[m.group(2)] + \
            f" {KILESA_PL}" + PPH

    add(rf"\b({ITS}) (pahīne|vikkhambhite) kilese\b", kil)

    # (8) a lone item word (noun left out by the abbreviation)
    add(rf"(?<![\wṃ])({IT_})(?![\wṃ])", lambda m: ctx.items[ctx.which(m.group(1))]["mo"])
    return R


def _stems(ctx):
    out = []
    for it in ctx.items:
        if it is None:
            continue
        st = re.match(r"[^(]+", it["rx"]).group(0)
        out.append(st)
    return sorted(set(out), key=len, reverse=True)


def _dedup_pairs(words):
    out = []
    for w in words:
        if out and out[-1] == w and w in ("पहले-पहले के", "बाद-बाद के"):
            continue
        out.append(w)
    return out


# =====================================================================================
# 8. Line translation
# =====================================================================================
CAP = re.compile(r"(?<![\w])([A-ZĀĪŪṄÑṬḌṆḶṂ])")


def plain_pass(s):
    for k in PLAIN_KEYS:
        if k in s:
            s = re.sub(rf"(?<![\wṃ]){re.escape(k)}(?![\wṃ])", lambda m, v=PLAIN[k]: v, s)
    return s


NUM_RX = "|".join(sorted(S.NUM, key=len, reverse=True))


def generic_pass(s):
    s = re.sub(rf"\b((?:na|no)?(?:{STEMS}))paccayena paccayo\b",
               lambda m: _ins(m.group(1)), s)
    s = re.sub(rf"(?<![\wṃ])({NUM_RX})(?![\wṃ])", lambda m: S.NUM[m.group(1)], s)
    s = re.sub(rf"(?<![\wṃ]){COND}(?![\wṃ])", lambda m: cond_hi(m.group(0)), s)
    for w, h in DEP_HI.items():
        if w.startswith("sahajāt"):
            continue
        s = re.sub(rf"(?<![\wṃ]){w}(?![\wṃ])", PPM("") + h, s)
    return s


def _ins(stem):
    return f"{S.INS(stem)} {VP}"


def punct(s):
    s = s.replace("…pe…", "…")
    s = re.sub(r"\.(?=\s|$|\))", "।", s)
    s = s.replace("……", "…")
    return s


def resolve(s):
    # "assādeti": "X का रस लेता है" after an object, "उसका रस लेता है" otherwise
    while ASLOT in s:
        j = s.index(ASLOT)
        if s[:j].rstrip(" ").endswith(PPH):
            s = s[:j] + PPM("का") + s[j + 1:]
        else:
            s = s[:j] + "उसका " + s[j + 1:]
    # postpositions: next PP marker within the clause
    out = []
    i = 0
    while True:
        j = s.find(PPH, i)
        if j < 0:
            out.append(s[i:])
            break
        out.append(s[i:j])
        rest = s[j + 1:]
        stop = re.search(r"[,;।–]", rest)
        seg = rest[:stop.start()] if stop else rest
        m = re.search("(.*?)", seg)
        pp = m.group(1) if m else ""
        out.append((" " + pp) if pp else "")
        i = j + 1
    s = "".join(out)
    s = re.sub(".*?", "", s)
    # verbs: nearest preceding subject marker within the clause
    while VP in s:
        j = s.index(VP)
        before = s[:j]
        cut = max(before.rfind("–"), before.rfind("।"), before.rfind(";"))
        seg = before[cut + 1:]
        ms = re.findall("(..)", seg)
        if not ms:
            raise ValueError("no subject for predicate: " + strip_marks(before[-80:]))
        s = s[:j] + BE[ms[-1]] + s[j + 1:]
    return strip_marks(s)


def strip_marks(s):
    return re.sub("..", "", s)


def tidy(s):
    s = re.sub(r" {2,}", " ", s)
    s = s.replace(" ,", ",").replace(" ।", "।").replace(" …", "…").replace("( ", "(")
    s = s.replace(",,", ",")
    return s.strip()


def translate_body(p, ctx, rules):
    if p.startswith("#"):
        lvl = len(p) - len(p.lstrip("#"))
        return "#" * lvl + " " + heading(p[lvl:].strip(), ctx)
    f = fixed_line(p, ctx)
    if f is not None:
        return f
    if GH_RX.match(p):
        return ghatana(p)
    c = try_count(p)
    if c is not None:
        return c
    s = p
    for k in sorted(PAREN, key=len, reverse=True):
        if k in s:
            s = s.replace(k, PAREN[k])
    s = CAP.sub(lambda m: m.group(1).lower(), s)
    for k in sorted(PRE, key=len, reverse=True):
        if k in s:
            s = s.replace(k, PRE[k])
    for rx, fn in rules:
        s = rx.sub(fn, s)
    s = re.sub(rf"((?:(?:{NANA_RX}),? )*(?:{NANA_RX}))(,? āvajjanāya)?(?![\wṃ])", nana_run, s)
    s = plain_pass(s)
    s = generic_pass(s)
    s = punct(s)
    s = resolve(s)
    return tidy(s)


LATIN = re.compile(r"[A-Za-zĀāĪīŪūṄṅÑñṬṭḌḍṆṇḶḷṂṃ]{2,}")


def build(key, report=None):
    ctx = Ctx(key)
    rules = item_rules(ctx)
    src = (PALI_DIR / FILES[key]).read_text(encoding="utf-8")
    out = []
    for n, line in enumerate(src.splitlines(), 1):
        if not line.strip():
            out.append("")
            continue
        m = S.ID_RX.search(line)
        body = S.ID_RX.sub("", line).strip()
        try:
            h = translate_body(body, ctx, rules)
        except ValueError as e:
            h = f"!!ERR {e}!! {body}"
        if report is not None and (LATIN.search(h) or "!!" in h):
            report.append((n, h))
        if m:
            h = f"{h} ^{m.group(1)}"
        out.append(h)
    return "\n".join(out).rstrip("\n") + "\n"


def main():
    args = sys.argv[1:]
    if "--dry" in args:
        keys = [a for a in args if a in FILES] or list(FILES)
        for k in keys:
            rep = []
            build(k, rep)
            print(f"=== {k}: {len(rep)} lines with residue")
            for n, h in rep:
                print(f"[{n}] {h}")
        return
    for k in FILES:
        text = build(k)
        path = HI_DIR / FILES[k]
        with open(path, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)
        print("wrote", path.name)


if __name__ == "__main__":
    main()
