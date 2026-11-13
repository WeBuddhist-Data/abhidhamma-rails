r"""pi-6 Yamaka, Hindi plain zero-shot: shared translator for 6-01/6-02 (Saṅkhārayamaka)
and 9-01/9-02/9-03 (Dhammayamaka). Imported by build_6_hi.py and build_9_hi.py.

Every line is composed from fixed frames (reused from build_sample_hi.py) and item tables;
an unknown line raises an error, so identical Pāli always gives identical Hindi.
"""
import pathlib
import re
import sys

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-hi")
import build_sample_hi as S  # noqa: E402  (import only)

ROOT = S.ROOT
PALI_DIR = S.PALI_DIR
HI_DIR = S.HI_DIR
ID_RE = S.ID_RE

# ---------------------------------------------------------------- headings (sample + new)
HEADINGS = dict(S.HEADINGS)
HEADINGS.update({
    "Suddhasaṅkhāravāro": "केवल रचनाओं का खंड",                          # terms file
    "Suddhadhammavāro": "केवल परिघटनाओं का खंड",                         # terms file
    "3 Suddhadhammavāro": "3 केवल परिघटनाओं का खंड",                     # stray number in the Pāli
    "Suddhadhammamūlacakkavāro": "केवल परिघटनाओं पर आधारित चक्र का खंड",  # terms file pattern
    "4 Suddhadhammamūlacakkavāro": "4 केवल परिघटनाओं पर आधारित चक्र का खंड",
    "Pavattivāro": "प्रक्रिया का खंड",
    "Uppādavāro": "उत्पन्न होने का खंड",                                  # terms file
    "Nirodhavāro": "समाप्त होने का खंड",
    "Uppādanirodhavāro": "उत्पन्न होने और समाप्त होने का खंड",
    "(Ṅa) paccanīkaokāsā": "(ङ) नकारात्मक: स्थान",
    "Pariññāvāro": "पूरी तरह समझने का खंड",                               # terms file
    "1-6. Paccuppannavārādi": "1-6. वर्तमान का खंड आदि",                  # model: 2-10. Hetuvārādi
    "Bhāvanāvāro": "अभ्यास का खंड",                                       # terms file
})

PLAIN = {   # non-heading lines that are fixed
    "(Kha) paccanīkaṃ": HEADINGS["(Kha) paccanīkaṃ"],
    "(Kha) niddeso": HEADINGS["(Kha) niddeso"],
    "(Ga) anulomapuggalokāsā": HEADINGS["(Ga) anulomapuggalokāsā"],
    "(Ca) paccanīkapuggalokāsā": HEADINGS["(Ca) paccanīkapuggalokāsā"],
    "4 (Ṅa) paccanīkaokāso": "4 (ङ) नकारात्मक: स्थान",
    "Paṇṇattiuddesavāro.": "शब्दावली की सूची का खंड।",                    # sample
    "Paṇṇattiniddesavāro.": "शब्दावली की व्याख्या का खंड।",               # sample
    "Paṇṇattivāro.": "शब्दावली का खंड।",
    "Uppādavāro.": "उत्पन्न होने का खंड।",
    "Nirodhavāro.": "समाप्त होने का खंड।",
    "Uppādanirodhavāro.": "उत्पन्न होने और समाप्त होने का खंड।",
    "Pariññāvāro.": "पूरी तरह समझने का खंड।",
    "Bhāvanāvāro.": "अभ्यास का खंड।",
    "Pavattivāro niṭṭhito.": "प्रक्रिया का खंड पूरा हुआ।",
    "Saṅkhārayamakaṃ niṭṭhitaṃ.": S.CHAPTER_END.format(title=S.CHAPTER_TITLES["Saṅkhārayamakaṃ"]),
    "Dhammayamakaṃ niṭṭhitaṃ.": S.CHAPTER_END.format(title=S.CHAPTER_TITLES["Dhammayamakaṃ"]),
    "Namo tassa bhagavato arahato sammāsambuddhassa": S.NAMO,
    "Abhidhammapiṭake": S.ABHIDHAMMAPITAKE,
    # editorial abbreviation notes
    "(Yassakampi yassayatthakampi sadisaṃ.)":
        "(व्यक्ति वाला भाग भी और व्यक्ति और स्थान वाला भाग भी समान है।)",
    "(Yassakampi yassayatthakampi sadisaṃ vitthāretabbaṃ, yassayatthake nirodhasamāpannānanti na labbhati.)":
        "(व्यक्ति वाले भाग को भी और व्यक्ति और स्थान वाले भाग को भी समान रूप से विस्तार देना चाहिए, व्यक्ति और स्थान वाले भाग में “समाप्ति की ध्यान-अवस्था में लीन लोगों में” नहीं आता।)",
    "(Yassakampi yassayatthakampi sadisaṃ vitthāretabbaṃ, yassayatthake nirodhasamāpannānanti na kātabbaṃ.)":
        "(व्यक्ति वाले भाग को भी और व्यक्ति और स्थान वाले भाग को भी समान रूप से विस्तार देना चाहिए, व्यक्ति और स्थान वाले भाग में “समाप्ति की ध्यान-अवस्था में लीन लोगों में” नहीं जोड़ना चाहिए।)",
    "(Yassakampi yassayatthakampi sadisaṃ, yassayatthake nirodhasamāpannānanti na labbhati).":
        "(व्यक्ति वाला भाग भी और व्यक्ति और स्थान वाला भाग भी समान है, व्यक्ति और स्थान वाले भाग में “समाप्ति की ध्यान-अवस्था में लीन लोगों में” नहीं आता)।",
    "(yassakampi yassayatthakampi sadisaṃ).":
        "(व्यक्ति वाला भाग भी और व्यक्ति और स्थान वाला भाग भी समान है)।",
    "(Yatthakampi sabbattha ekasadisaṃ).":
        "(स्थान वाला भाग भी हर जगह एक समान है)।",
    "(Yathā uppādavāre atītā pucchā yassakampi yassayatthakampi anulomampi paccanīkampi vibhattaṃ evaṃ nirodhavārepi vibhajitabbaṃ, natthi nānākaraṇaṃ.)":
        "(जैसे उत्पन्न होने के खंड में अतीत के प्रश्न व्यक्ति वाले भाग में भी और व्यक्ति और स्थान वाले भाग में भी, सकारात्मक भी और नकारात्मक भी, विभाजित किए गए हैं, वैसे ही समाप्त होने के खंड में भी विभाजित करने चाहिए, कोई अंतर नहीं है।)",
    "(Atītā pucchā uppādavārepi nirodhavārepi uppādanirodhavārepi sadisaṃ vitthāretabbā).":
        "(अतीत के प्रश्न को उत्पन्न होने के खंड में भी, समाप्त होने के खंड में भी और उत्पन्न होने और समाप्त होने के खंड में भी समान रूप से विस्तार देना चाहिए)।",
    "(Yathā uppādavāre paccuppannātītā pucchā anulomampi paccanīkampi vibhattā evaṃ uppādavāranirodhavārepi paccuppannātītā pucchā anulomampi paccanīkampi vibhajitabbā.)":
        "(जैसे उत्पन्न होने के खंड में वर्तमान और अतीत के प्रश्न सकारात्मक भी और नकारात्मक भी विभाजित किए गए हैं, वैसे ही उत्पन्न होने और समाप्त होने के खंड में भी वर्तमान और अतीत के प्रश्न सकारात्मक भी और नकारात्मक भी विभाजित करने चाहिए।)",
    "(Yathā nirodhavāre atītānāgatā pucchā anulomampi paccanīkampi evaṃ uppādanirodhavārepi atītānāgatā pucchā anulomampi paccanīkampi vibhajitabbaṃ asammohantena nirodhavārena sadisaṃ, natthi nānākaraṇaṃ.)":
        "(जैसे समाप्त होने के खंड में अतीत और भविष्य के प्रश्न सकारात्मक भी और नकारात्मक भी हैं, वैसे ही उत्पन्न होने और समाप्त होने के खंड में भी अतीत और भविष्य के प्रश्न सकारात्मक भी और नकारात्मक भी बिना भ्रमित हुए, समाप्त होने के खंड के समान विभाजित करने चाहिए, कोई अंतर नहीं है।)",
    "(Yathā khandhayamake pariññāvāraṃ vibhattaṃ evaṃ saṅkhārayamakepi pariññāvāraṃ vibhajitabbaṃ.)":
        "(जैसे “समूहों पर प्रश्नों के जोड़े” में पूरी तरह समझने का खंड विभाजित किया गया है, वैसे ही “रचनाओं पर प्रश्नों के जोड़े” में भी पूरी तरह समझने का खंड विभाजित करना चाहिए।)",
}

# ---------------------------------------------------------------- short answers
AMANTA = S.AMANTA          # Āmantā = हाँ।
NO = "नहीं।"               # No. (pi-2 No = नहीं)
NATTHI = "ऐसा कोई नहीं है।"  # Natthi. (new)

# feminine plural (परिघटनाएँ); Pāli uses uppajjittha / nirujjhittha with a plural subject too
VERBS_FPL = {
    "uppajjanti": ("उत्पन्न होती हैं", "उत्पन्न नहीं होतीं"),
    "uppajjittha": ("उत्पन्न हुई थीं", "उत्पन्न नहीं हुई थीं"),
    "uppajjissanti": ("उत्पन्न होंगी", "उत्पन्न नहीं होंगी"),
    "nirujjhanti": ("समाप्त होती हैं", "समाप्त नहीं होतीं"),
    "nirujjhittha": ("समाप्त हुई थीं", "समाप्त नहीं हुई थीं"),
    "nirujjhissanti": ("समाप्त होंगी", "समाप्त नहीं होंगी"),
}


def verb(tok, verbs):
    neg = False
    if tok.startswith("na "):
        neg, tok = True, tok[3:]
    elif tok.startswith("n") and tok[1:] in verbs:
        neg, tok = True, tok[1:]
    if tok not in verbs:
        raise KeyError(tok)
    return verbs[tok][1 if neg else 0]


def verb_flip(tok, verbs):
    neg = False
    if tok.startswith("na "):
        neg, tok = True, tok[3:]
    elif tok.startswith("n") and tok[1:] in verbs:
        neg, tok = True, tok[1:]
    if tok not in verbs:
        raise KeyError(tok)
    return verbs[tok][0 if neg else 1]


# ---------------------------------------------------------------- answer prefixes (who / where / when)
ORD = {"paṭhama": "पहली", "dutiya": "दूसरी", "tatiya": "तीसरी", "catuttha": "चौथी"}
SPHERE = {"kāmāvacar": "इंद्रिय-सुखों के लोक", "rūpāvacar": "सूक्ष्म भौतिक लोक", "arūpāvacar": "अभौतिक लोक"}
VOKARA = {"catuvokār": "चार समूहों वाले", "pañcavokār": "पाँच समूहों वाले"}
CITTA_GEN = {   # <X>ssa … kkhaṇe
    "kusalavippayuttaakusalavippayuttacitta": "हितकर से अलग और हानिकर से अलग मन",
    "akusalavippayuttakusalavippayuttacitta": "हानिकर से अलग और हितकर से अलग मन",
    "kusalavippayuttacitta": "हितकर से अलग मन",
    "akusalavippayuttacitta": "हानिकर से अलग मन",
    "savitakkasavicārapacchimacitta": "आरंभिक विचार और सतत विचार वाले अंतिम मन",
    "avitakkaavicārapacchimacitta": "आरंभिक विचार और सतत विचार से रहित अंतिम मन",
    "avitakkaavicāracitta": "आरंभिक विचार और सतत विचार से रहित मन",
    "pacchimacitta": "अंतिम मन",
    "aggamagga": "सर्वोच्च मार्ग",
    "citta": "मन",
}
PL_GEN = {     # <X>ānaṃ … kkhaṇe
    "kusalākusalānaṃ": "हितकर और हानिकर परिघटनाओं",
    "kusalānaṃ": "हितकर परिघटनाओं",
    "akusalānaṃ": "हानिकर परिघटनाओं",
    "assāsapassāsānaṃ": "साँस लेने और छोड़ने",
    "vitakkavicārānaṃ": "आरंभिक विचार और सतत विचार",
}
GEN_PRE = {"sabbesaṃ": "सभी के ", "tassa": "उस ", "kāmāvacarānaṃ": "इंद्रिय-सुखों के लोक के प्राणियों के "}
KHANA = {"uppāda": "के उत्पन्न होने के क्षण में", "bhaṅga": "के भंग होने के क्षण में"}

FIXED_CHUNKS = [   # (Pāli, kind, Hindi); longest first
    ("rūpāvacare arūpāvacare pacchimabhavikānaṃ ye ca rūpāvacaraṃ arūpāvacaraṃ upapajjitvā parinibbāyissanti tesaṃ cavantānaṃ", "np",
     "सूक्ष्म भौतिक लोक और अभौतिक लोक में अंतिम जन्म वालों में और जो सूक्ष्म भौतिक लोक या अभौतिक लोक में जन्म लेकर पूर्ण निर्वाण पाएँगे, उन मरने वालों में"),
    ("yassa cittassa anantarā aggamaggaṃ paṭilabhissanti tassa cittassa uppādakkhaṇe", "np",
     "जिस मन के ठीक बाद वे सर्वोच्च मार्ग प्राप्त करेंगे, उस मन के उत्पन्न होने के क्षण में"),
    ("yassa cittassa anantarā aggamaggaṃ paṭilabhissanti tassa cittassa bhaṅgakkhaṇe", "np",
     "जिस मन के ठीक बाद वे सर्वोच्च मार्ग प्राप्त करेंगे, उस मन के भंग होने के क्षण में"),
    ("yassa cittassa anantarā aggamaggaṃ paṭilabhissanti", "np",
     "जो इस मन के ठीक बाद सर्वोच्च मार्ग प्राप्त करेंगे, उनमें"),
    ("yassa cittassa anantarā kāmāvacarānaṃ pacchimacittaṃ uppajjissati", "np",
     "इंद्रिय-सुखों के लोक के जिन प्राणियों में इस मन के ठीक बाद अंतिम मन उत्पन्न होगा, उनमें"),
    ("yassa cittassa anantarā avitakkaavicāraṃ pacchimacittaṃ uppajjissati", "np",
     "जिनमें इस मन के ठीक बाद आरंभिक विचार और सतत विचार से रहित अंतिम मन उत्पन्न होगा, उनमें"),
    ("sabbesaṃ upapajjantānaṃ", "np", "सभी जन्म लेने वालों में"),
    ("sabbesaṃ cavantānaṃ", "np", S.WHO["Sabbesaṃ cavantānaṃ"]),
    ("suddhāvāsaṃ upapajjantānaṃ", "np", "शुद्ध निवास लोक में जन्म लेने वालों में"),
    ("dutiye akusale citte vattamāne", "post", "दूसरे हानिकर मन के चलते समय"),
    ("dutiye citte vattamāne", "post", "दूसरे मन के चलते समय"),
    ("vinā assāsapassāsehi", "mod", "साँस लेने और छोड़ने के बिना"),
    ("vinā vitakkavicārehi", "mod", "आरंभिक विचार और सतत विचार के बिना"),
    ("pavatte", "mod", "जीवन के दौरान"),
    ("tesaṃyeva", "mod", "उन्हीं में"),
    ("nirodhasamāpannānaṃ", "np", "समाप्ति की ध्यान-अवस्था में लीन लोगों में"),
    ("asaññasattānaṃ", "np", "पहचान-रहित प्राणियों में"),
    ("suddhāvāsānaṃ", "np", "शुद्ध निवास लोक के प्राणियों में"),
    ("avitakkaavicārapacchimacittasamaṅgīnaṃ", "np", "आरंभिक विचार और सतत विचार से रहित अंतिम मन से युक्त लोगों में"),
    ("pacchimacittasamaṅgīnaṃ", "np", "अंतिम मन से युक्त लोगों में"),
    ("aggamaggasamaṅgīnaṃ", "np", "सर्वोच्च मार्ग से युक्त लोगों में"),
    ("arahantānaṃ", "np", "अर्हतों में"),
    ("pacchimabhavikānaṃ", "np", "अंतिम जन्म वालों में"),
    ("asaññasatte", "loc", "पहचान-रहित प्राणियों के लोक में"),
    ("arūpe", "loc", "अभौतिक लोक में"),
    ("savitakkasavicārabhūmiyaṃ", "loc", "आरंभिक विचार और सतत विचार वाले स्तर पर"),
    ("avitakkaavicārabhūmiyaṃ", "loc", "आरंभिक विचार और सतत विचार से रहित स्तर पर"),
]

_CITTA_ALT = "|".join(sorted(CITTA_GEN, key=len, reverse=True))
_PLG_ALT = "|".join(sorted(PL_GEN, key=len, reverse=True))
_ORD_ALT = "|".join(ORD)
_SPH_ALT = "kāmāvacar|rūpāvacar|arūpāvacar"
_VOK_ALT = "catuvokār|pañcavokār"
_END = r"(?=,? |,?$)"


def _join(names):
    if len(names) == 1:
        return names[0]
    return ", ".join(names[:-1]) + " और " + names[-1]


def _next_chunk(s, pos):
    rest = s[pos:]
    for p, kind, hi in FIXED_CHUNKS:
        if re.match(re.escape(p) + _END, rest):
            return len(p), kind, hi
    m = re.match(rf"(?:(sabbesaṃ|tassa|kāmāvacarānaṃ) )?({_CITTA_ALT})ssa (uppāda|bhaṅga)kkhaṇe" + _END, rest)
    if m:
        pre, x, k = m.groups()
        return m.end(), "np", (GEN_PRE[pre] if pre else "") + CITTA_GEN[x] + " " + KHANA[k]
    m = re.match(rf"({_PLG_ALT}) (uppāda|bhaṅga)kkhaṇe" + _END, rest)
    if m:
        x, k = m.groups()
        return m.end(), "np", PL_GEN[x] + " " + KHANA[k]
    m = re.match(rf"((?:(?:{_ORD_ALT})jjhānaṃ )+)samāpannānaṃ" + _END, rest)
    if m:
        ords = re.findall(rf"({_ORD_ALT})jjhānaṃ", m.group(1))
        return m.end(), "np", "ध्यान की " + _join([ORD[o] for o in ords]) + " अवस्था में लीन लोगों में"
    m = re.match(rf"(?:(?:{_ORD_ALT})jjhāne(?: |$))+", rest)
    if m:
        ords = re.findall(rf"({_ORD_ALT})jjhāne", m.group(0))
        return len(m.group(0).rstrip()), "loc", "ध्यान की " + _join([ORD[o] for o in ords]) + " अवस्था में"
    m = re.match(rf"(itaresaṃ )?((?:(?:{_SPH_ALT})ānaṃ(?: |$))+)", rest)
    if m and not re.match(r"kāmāvacarānaṃ pacchimacittassa", rest):
        names = [SPHERE[x] for x in re.findall(rf"({_SPH_ALT})ānaṃ", m.group(2))]
        return len(m.group(0).rstrip()), "np", ("बाकी " if m.group(1) else "") + _join(names) + " के प्राणियों में"
    m = re.match(rf"(itaresaṃ )?((?:(?:{_VOK_ALT})ānaṃ(?: |$))+)", rest)
    if m:
        names = [VOKARA[x] for x in re.findall(rf"({_VOK_ALT})ānaṃ", m.group(2))]
        return len(m.group(0).rstrip()), "np", ("बाकी " if m.group(1) else "") + _join(names) + " अस्तित्व के प्राणियों में"
    m = re.match(rf"(?:(?:{_SPH_ALT})e(?: |$))+", rest)
    if m:
        names = [SPHERE[x] for x in re.findall(rf"({_SPH_ALT})e\b", m.group(0))]
        return len(m.group(0).rstrip()), "loc", _join(names) + " में"
    m = re.match(rf"(?:(?:{_VOK_ALT})e(?: |$))+", rest)
    if m:
        names = [VOKARA[x] for x in re.findall(rf"({_VOK_ALT})e\b", m.group(0))]
        return len(m.group(0).rstrip()), "loc", _join(names) + " अस्तित्व में"
    m = re.match(r"itaresaṃ" + _END, rest)
    if m:
        return m.end(), "np", "बाकी सबमें"
    raise ValueError("unknown prefix chunk: " + rest)


def tr_who(who):
    """Translate the who/where/when prefix of an answer sentence."""
    s = who[0].lower() + who[1:]
    pos, chunks = 0, []
    while pos < len(s):
        n, kind, hi = _next_chunk(s, pos)
        chunks.append((kind, hi))
        pos += n
        while pos < len(s) and s[pos] in ", ":
            pos += 1
    out = chunks[0][1]
    for (pk, _), (ck, hi) in zip(chunks, chunks[1:]):
        if pk == "mod" or ck == "post" or (pk == "loc" and ck != "loc"):
            out += " " + hi
        else:
            out += ", " + hi
    return out


# ---------------------------------------------------------------- the per-chapter translator
class Chapter:
    """items: Pāli token -> Hindi; verbs: verb table; norm: function normalising item phrases to one token."""

    def __init__(self, items, verbs, norm=lambda s: s):
        self.items = items
        self.verbs = verbs
        self.norm = norm
        self.short = {"Āmantā.": AMANTA, "No.": NO, "Natthi.": NATTHI, "Āmantā…pe….": "हाँ…।"}
        for p, (pos, neg) in verbs.items():
            self.short[p[0].upper() + p[1:] + "."] = pos + "।"
        self.fixed = {}
        self.pannatti = None   # function(body) -> Hindi or None

    # ---- pavatti questions
    def q_pavatti(self, body):
        body = self.norm(body)
        it = "|".join(re.escape(k) for k in self.items)
        v = r"(?:na )?\S+"
        m = re.fullmatch(rf"(yassa|yattha)( vā pana)?( yattha)? ({it}) ({v}) (tassa tattha|tassa|tattha) ({it}) ({v})\?", body)
        if not m:
            return None
        rel, vp, rel2, x, v1, cor, y, v2 = m.groups()
        rel = rel + (rel2 or "")
        return S.PAVATTI_Q.format(AND=S.VA_PANA if vp else "", REL=S.Q_REL[rel], X=self.items[x],
                                  V1=verb(v1, self.verbs), COR=S.Q_COR[cor], Y=self.items[y],
                                  V2=verb(v2, self.verbs))

    def untie_q(self, q):
        """Drop the quotative -ti of the last word before '?'."""
        words = q[:-1].split(" ")
        w = words[-1]
        known = set(self.items) | set(self.verbs) | {"n" + x for x in self.verbs} | self.known_extra
        if w.endswith("ti") and w not in known:
            base = w[:-2]
            for cand in (base, base[:-1] + {"ā": "a", "ī": "i", "ū": "u"}.get(base[-1:], base[-1:]),
                         base[:-1] + "ṃ" if base.endswith("n") else None):
                if cand and (cand in known or self.norm(cand) in known):
                    words[-1] = cand
                    break
        return " ".join(words) + "?"

    known_extra = set()

    # ---- answers
    def sentence(self, s):
        s = self.norm(s)
        it = "|".join(re.escape(k) for k in self.items)
        loc = "tesaṃ tattha|tesaṃ|tattha"
        v = r"(?:na )?\S+"
        m = re.fullmatch(rf"(.+?) ({loc}) ({it}) ({v}), no ca ({loc}) ({it}) ({v})", s)
        if m:
            who, l1, x, v1, l2, y, v2 = m.groups()
            return S.ANS_BUT.format(WHO=tr_who(who), L1=S.LOC1[l1], X=self.items[x], V1=verb(v1, self.verbs),
                                    L2=S.LOC2[l2], Y=self.items[y], V2=verb_flip(v2, self.verbs))
        m = re.fullmatch(rf"(.+?) ({loc}) ({it}) ca ({v}) ({it}) ca ({v})", s)
        if m:
            who, l1, x, v1, y, v2 = m.groups()
            return S.ANS_BOTH.format(WHO=tr_who(who), L1=S.LOC1[l1], X=self.items[x], V1=verb(v1, self.verbs),
                                     Y=self.items[y], V2=verb(v2, self.verbs))
        # source slip: "X V Y ca V" (the first "ca" missing), translated as written
        m = re.fullmatch(rf"(.+?) ({loc}) ({it}) ({v}) ({it}) ca ({v})", s)
        if m:
            who, l1, x, v1, y, v2 = m.groups()
            return "{W}{L1} {X} {V1} और {Y} भी {V2}।".format(W=tr_who(who), L1=S.LOC1[l1], X=self.items[x],
                                                              V1=verb(v1, self.verbs), Y=self.items[y],
                                                              V2=verb(v2, self.verbs))
        return None

    # ---- stub lines with …pe…
    def stub(self, text):
        """'(Kha) yassa vā pana…pe…? Āmantā.', 'Yattha X V…pe….', 'Yattha X V tattha Y V?…Pe….' …"""
        m = re.fullmatch(r"(?:(\((?:Ka|Kha)\)) )?(.*?)(…pe…|…Pe…)(\?|\.)?(?: (.+))?", text)
        if not m:
            return None
        label, head, _, punct, ans = m.groups()
        head_n = self.norm(head)
        it = "|".join(re.escape(k) for k in self.items)
        v = r"(?:na )?\S+"
        hh = None
        mm = re.fullmatch(r"([Yy]assa|[Yy]attha)( vā pana)?( yattha)?(?: ({it})(?: ({v}))?)?".format(it=it, v=v), head_n)
        if mm:
            rel, vp, rel2, x, v1 = mm.groups()
            rel = rel.lower() + (rel2 or "")
            hh = (S.VA_PANA if vp else "") + S.Q_REL[rel]
            if x:
                hh += " " + self.items[x]
            if v1:
                hh += " " + verb(v1, self.verbs)
        else:
            q = self.q_pavatti(self.untie_q(head_n[0].lower() + head_n[1:])) if head_n.endswith("?") else None
            if q is None:
                return None
            hh = q
        out = (S.LABELS[label] + " " if label else "") + hh + "…"
        if punct == "?":
            out += "?"
        elif punct == ".":
            out += "।"
        if ans:
            out += " " + (self.short.get(ans) or PLAIN[ans])
        return out

    def tr_body(self, text):
        if text in PLAIN:
            return PLAIN[text]
        if text in self.fixed:
            return self.fixed[text]
        st = self.stub(text)
        if st:
            return st
        m = re.match(r"^(?:(\((?:Ka|Kha)\)) )?(.*)$", text)
        label, rest = m.groups()
        if "?" in rest:
            q, ans = rest, None
            if "? " in rest:
                q, ans = rest.split("? ", 1)
                q += "?"
            if not label:
                q = q[0].lower() + q[1:]
            q2 = self.untie_q(q)
            hq = None
            for f in (self.q_pavatti, self.pannatti, self.q_practice):
                if f is None:
                    continue
                try:
                    hq = f(q2)
                except KeyError:
                    hq = None
                if hq:
                    break
            if hq is None:
                raise ValueError("untranslated question: " + text)
            out = (S.LABELS[label] + " " if label else "") + hq
            if ans:
                out += " " + self.tr_body(ans)
            return out
        if text in self.short:
            return self.short[text]
        if self.extra:
            r = self.extra(text)
            if r:
                return r
        sents = re.split(r"(?<=\.) ", text)
        if all(x.endswith(".") for x in sents):
            outs = [self.sentence(x[:-1]) for x in sents]
            if all(outs):
                return " ".join(outs)
        raise ValueError("untranslated line: " + text)

    q_practice = None
    extra = None

    def tr_line(self, line):
        if not line.strip():
            return ""
        m = ID_RE.search(line)
        bid = m.group(1) if m else None
        text = ID_RE.sub("", line) if m else line
        if text.startswith("#"):
            level = len(text) - len(text.lstrip("#"))
            h = text[level:].strip()
            if h not in HEADINGS:
                raise ValueError("untranslated heading: " + h)
            out = "#" * level + " " + HEADINGS[h]
        else:
            out = self.tr_body(text)
        return out + (" " + bid if bid else "")

    def build(self, fname):
        lines = (PALI_DIR / fname).read_text(encoding="utf-8").splitlines()
        hi = [self.tr_line(l) for l in lines]
        (HI_DIR / fname).write_text("\n".join(hi) + "\n", encoding="utf-8", newline="\n")
        print(fname, len([l for l in lines if l.strip()]), "lines")
