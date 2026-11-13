"""pi-6 5-02-saccayamaka.md (Saccayamaka, Pavatti 2 nirodhavāra from (1) Paccuppannavāro, and Pavatti 3
uppādanirodhavāra to (4) Paccuppannātītavāro) -> Hindi plain RAILS.

Imports build_rails_sample.py read-only (constants: headings, closings, frames, verbs). Every Pāli line must be
matched by a formula; an unknown line raises ValueError. New recurring formulas are listed in notes-5-02.md.
usage: python -I -X utf8 build_5-02.py [--dry]
"""
import re
import sys

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-hi\rails")
import build_rails_sample as S  # noqa: E402

FILE = "5-02-saccayamaka.md"

# ---------------------------------------------------------------------------------------------------
# Truths (process subjects; masculine «सत्य»)
# ---------------------------------------------------------------------------------------------------
TRUTHS = {
    "dukkhasaccaṃ": ("दुःख का सत्य", "m"),
    "samudayasaccaṃ": ("उत्पत्ति का सत्य", "m"),
    "maggasaccaṃ": ("मार्ग का सत्य", "m"),
    "nirodhasaccaṃ": ("अंत का सत्य", "m"),
}
TRUTH_OBL = {k: v[0].replace(" का सत्य", " के सत्य") for k, v in TRUTHS.items()}
_TR = "|".join(t[:-1] for t in TRUTHS)            # stems without the final ṃ: dukkhasacca …
VERB_SLIPS = {"nirujjhiti": "nirujjhati"}          # ^6-5-125: source slip (termbase: variant spelling)

# ---------------------------------------------------------------------------------------------------
# Being / moment chunks of this chapter (every chunk ends in «में», «चलते समय» as B4)
# ---------------------------------------------------------------------------------------------------
MOMENT = {"uppāda": "उत्पन्न होने", "bhaṅga": "भंग होने"}
CITTA = {"": "मन", "taṇhāvippayutta": "तृष्णा से अलग मन", "maggavippayutta": "मार्ग से अलग मन",
         "taṇhāvippayuttamaggavippayutta": "तृष्णा से अलग और मार्ग से अलग मन",
         "maggavippayuttataṇhāvippayutta": "मार्ग से अलग और तृष्णा से अलग मन",
         "upapatti": "जन्म के मन", "pacchima": "अंतिम मन"}
PAVATTE = "जीवन के दौरान"
KSHANE = "{x} के {m} के क्षण में"
VATTAMANE = "{x} के चलते समय"                       # <x>citte vattamāne (B4)
DUTIYE = "दूसरे मन"
ARAHANTA = "अर्हतों में"
AGGA_SAMANGI = "सर्वोच्च मार्ग से युक्त लोगों में"
PACCHIMA_SAMANGI = "अंतिम मन से युक्त लोगों में"
NIRODHA_SAMAPANNA = "समाप्ति की ध्यान-अवस्था में लीन लोगों में"
ABHISAMETA = {"ab": "सत्यों का बोध पा चुके लोगों में", "anab": "सत्यों का बोध न पाए लोगों में"}
UNMEN_SE = "से"                                       # «… लोगों में से मरने वालों में» (B3 shape)
CATUPANCA_BEINGS = "चार या पाँच समूहों वाले अस्तित्व के प्राणियों में"   # catuvokārānaṃ pañcavokārānaṃ (I3)
MAGGA = {"": "मार्ग", "agga": "सर्वोच्च मार्ग"}
PHALA = "फल"
# relative clauses (they share one correlative «उनमें»)
REL_ANANTARA = "जो इस मन के ठीक बाद सर्वोच्च मार्ग प्राप्त करेंगे"          # yassa cittassa anantarā aggamaggaṃ paṭilabhissanti (B6)
TASSA_CITTASSA = "जिस मन के ठीक बाद वे सर्वोच्च मार्ग प्राप्त करेंगे, उस मन के {m} के क्षण में"
REL_PUTHUJJANA = "जो साधारण व्यक्ति मार्ग प्राप्त नहीं करेंगे"            # ye (ca) puthujjanā maggaṃ na paṭilabhissanti
REL_ANNE = "जो दूसरे लोग मार्ग प्राप्त करेंगे"                              # ye caññe maggaṃ paṭilabhissanti
REL_YE = "जो मार्ग प्राप्त करेंगे"                                         # ye maggaṃ paṭilabhissanti
UNMEN = "उनमें"
REL_JOIN = " और "


def sigla(s):
    """'(sī. syā.)' -> '(Sī., Syā.)'"""
    parts = [p.strip().rstrip(".") for p in s.strip("()").split(" ") if p.strip()]
    return "(" + ", ".join(p[0].upper() + p[1:] + "." for p in parts) + ")"


def bracket(b):
    """Variant bracket of this file -> Hindi bracket."""
    if not b:
        return ""
    b = b.strip()
    m = re.fullmatch(r"\[(.+?) (\([^)]*\))( uppādavāre pana pāṭhantaraṃ natthi)?\]", b)
    if not m:
        raise ValueError(f"bracket: {b}")
    note = "; पर उत्पन्न होने के खंड में पाठभेद नहीं है" if m.group(3) else ""
    return f" [पाठभेद {sigla(m.group(2))}: {m.group(1)}{note}]"


_M = r"(uppāda|bhaṅga)kkhaṇe"
_CP = "|".join(sorted((k for k in CITTA if k), key=len, reverse=True))
_BR = r"( \[[^\]]*\])?"

# (regex, kind, builder) ; kind: chunk | rel | itaresam
RULES = [
    (rf"yassa cittassa anantarā aggamaggaṃ paṭilabhissanti tassa cittassa {_M}", "chunk",
     lambda m: TASSA_CITTASSA.format(m=MOMENT[m.group(1)])),
    (rf"yassa cittassa anantarā aggamaggaṃ paṭilabhissanti{_BR}", "rel",
     lambda m: REL_ANANTARA + bracket(m.group(1))),
    (r"ye (?:ca )?puthujjanā maggaṃ na paṭilabhissanti", "rel", lambda m: REL_PUTHUJJANA),
    (r"ye caññe maggaṃ paṭilabhissanti", "rel", lambda m: REL_ANNE),
    (r"ye maggaṃ paṭilabhissanti", "rel", lambda m: REL_YE),
    (r"sabbesaṃ (cavantānaṃ|upapajjantānaṃ)", "chunk",
     lambda m: f"{S.SABBESAM} {S.PARTICIPLES[m.group(1)]}"),
    (rf"sabbesaṃ cittassa {_M}", "chunk",
     lambda m: KSHANE.format(x="सभी के मन", m=MOMENT[m.group(1)])),
    (r"(ab|anab)hisametāvīnaṃ (cavantānaṃ|upapajjantānaṃ)", "chunk",
     lambda m: f"{ABHISAMETA[m.group(1)]} {UNMEN_SE} {S.PARTICIPLES[m.group(2)]}"),
    (rf"(ab|anab)hisametāvīnaṃ taṇhāya {_M}", "chunk",
     lambda m: f"{ABHISAMETA[m.group(1)]} " + KSHANE.format(x="तृष्णा", m=MOMENT[m.group(2)])),
    (rf"suddhāvāsānaṃ upapatticittassa {_M}", "chunk",
     lambda m: f"{S.BEINGS['suddhāvāsānaṃ']} " + KSHANE.format(x=CITTA["upapatti"], m=MOMENT[m.group(1)])),
    (r"suddhāvāsānaṃ dutiye citte vattamāne", "chunk",
     lambda m: f"{S.BEINGS['suddhāvāsānaṃ']} " + VATTAMANE.format(x=DUTIYE)),
    (r"(catuvokāraṃ pañcavokāraṃ|asaññasattaṃ|suddhāvāsaṃ) upapajjantānaṃ", "chunk",
     lambda m: place_part(m.group(1), "upapajjantānaṃ")),
    (r"(catuvokārā pañcavokārā|asaññasattā) cavantānaṃ", "chunk",
     lambda m: place_part(m.group(1), "cavantānaṃ")),
    (r"catuvokārānaṃ pañcavokārānaṃ", "chunk", lambda m: CATUPANCA_BEINGS),
    (rf"(pavatte )?({_CP})?cittassa {_M}", "chunk",
     lambda m: (PAVATTE + " " if m.group(1) else "") +
     KSHANE.format(x=CITTA[m.group(2) or ""], m=MOMENT[m.group(3)])),
    (rf"(arūpe |pañcavokāre )?(agga)?maggassa( ca phalassa ca)? {_M}", "chunk",
     lambda m: (place_loc(m.group(1)) + KSHANE.format(
         x=MAGGA[m.group(2) or ""] + (f" और {PHALA}" if m.group(3) else ""), m=MOMENT[m.group(4)]))),
    (rf"(arūpe )?phalassa {_M}", "chunk",
     lambda m: place_loc(m.group(1)) + KSHANE.format(x=PHALA, m=MOMENT[m.group(2)])),
    (rf"taṇhāya {_M}", "chunk", lambda m: KSHANE.format(x="तृष्णा", m=MOMENT[m.group(1)])),
    (rf"taṇhāvippayuttacitte vattamāne{_BR}", "chunk",
     lambda m: VATTAMANE.format(x=CITTA["taṇhāvippayutta"]) + bracket(m.group(1))),
    (rf"arahantānaṃ cittassa {_M}", "chunk", lambda m: KSHANE.format(x="अर्हतों के मन", m=MOMENT[m.group(1)])),
    (r"arahantānaṃ", "chunk", lambda m: ARAHANTA),
    (r"aggamaggasamaṅgīnaṃ", "chunk", lambda m: AGGA_SAMANGI),
    (r"pacchimacittasamaṅgīnaṃ", "chunk", lambda m: PACCHIMA_SAMANGI),
    (r"nirodhasamāpannānaṃ", "chunk", lambda m: NIRODHA_SAMAPANNA),
    (r"(asaññasattānaṃ|āpāyikānaṃ)", "chunk", lambda m: S.BEINGS[m.group(1)]),
    (r"(cavantānaṃ|upapajjantānaṃ)", "chunk", lambda m: S.PARTICIPLES[m.group(1)]),
    (r"itaresaṃ", "itaresam", None),
]
RULES = [(re.compile(p + r"(?= |$)"), k, f) for p, k, f in RULES]


def place_loc(s):
    if not s:
        return ""
    key, _ = S.PLACE_FORMS[s.strip()]
    return f"{S.PLACE_NOUN[key]} में "


def place_part(pl, part):
    toks = pl.split(" ")
    keys = [S.PLACE_FORMS[t][0] for t in toks]
    case = S.PLACE_FORMS[toks[0]][1]
    key = "catupañcavokāra" if keys == ["catuvokāra", "pañcavokāra"] else keys[0]
    return f"{S.PLACE_NOUN[key]} {S.CASE_POST[case]} {S.PARTICIPLES[part]}"


def _next(s, i):
    """Match one rule at position i -> (kind, hindi, new_i)."""
    for rx, kind, fn in RULES:
        m = rx.match(s, i)
        if m:
            return kind, (fn(m) if fn else None), m.end()
    return None


def who(s):
    """Being / moment chain (before the final tesaṃ [tattha]) -> Hindi chunks joined «, » and « और »."""
    s = s[0].lower() + s[1:]
    if s == "itaresaṃ":
        return S.ITARESAM_ALONE
    chunks, i, n = [], 0, len(s)
    itaresam = False
    while i < n:
        if s[i] == " ":
            i += 1
            continue
        r = _next(s, i)
        if not r:
            raise ValueError(f"who: no rule at {s[i:i+40]!r} in {s!r}")
        kind, hi, i = r
        if kind == "itaresam":
            itaresam = True
            continue
        if kind == "rel":
            rels = [hi]
            while True:          # consecutive relatives share one correlative
                j = i + 1
                r2 = _next(s, j) if j < n else None
                if r2 and r2[0] == "rel":
                    rels.append(r2[1])
                    i = r2[2]
                    continue
                break
            text = REL_JOIN.join(rels) + ", " + UNMEN
            if s.startswith(" tesaṃ ", i) or s[i:] == " tesaṃ":
                j = i + len(" tesaṃ ")
                r3 = _next(s, j) if j < n else None
                if r3 and r3[0] == "chunk":
                    nxt = r3[1]
                    if nxt in (S.PARTICIPLES["cavantānaṃ"], S.PARTICIPLES["upapajjantānaṃ"]):
                        text += f" {UNMEN_SE} {nxt}"           # B3: «…, उनमें से मरने वालों में»
                    else:
                        text += f" {nxt}"
                    i = r3[2]
                else:
                    raise ValueError(f"who: inner tesaṃ without chunk in {s!r}")
            hi = text
        if itaresam:
            hi = f"{S.ITARESAM} {hi}"
            itaresam = False
        chunks.append(hi)
    if itaresam:
        raise ValueError(f"who: dangling itaresaṃ in {s!r}")
    if len(chunks) == 1:
        return chunks[0]
    return S.JOIN.join(chunks[:-1]) + S.JOIN_LAST + chunks[-1]


# ---------------------------------------------------------------------------------------------------
# Verbs
# ---------------------------------------------------------------------------------------------------
def verb(tok, flip=False):
    neg = tok.startswith("na ")
    w = tok[3:] if neg else tok
    w = VERB_SLIPS.get(w, w)
    return S.verb_hi(("na " if neg else "") + w, "m", flip)


_VTI = set(S.VERB_FORMS) | set(VERB_SLIPS)


def strip_v(tok):
    neg = tok.startswith("na ")
    w = tok[3:] if neg else tok
    return ("na " if neg else "") + S.strip_ti(w, _VTI)


# ---------------------------------------------------------------------------------------------------
# Sentences
# ---------------------------------------------------------------------------------------------------
_REL = r"(yassa vā pana yattha|yassa yattha|yassa vā pana|yassa|yattha vā pana|yattha)"
_COR = r"(tassa tattha|tassa|tattha)"
_V = r"((?:na )?\S+)"
Q_RE = re.compile(rf"(?:\((Ka|Kha)\) )?{_REL} ({_TR})ṃ {_V} {_COR} ({_TR})ṃ {_V}[?.]")
ABBR_RE = re.compile(rf"(?:\((Ka|Kha)\) )?(yassa vā pana|yassa yattha|yassa|yattha)(?: ({_TR})ṃ {_V})?…pe…[?.]")
BUT_RE = re.compile(rf"(.+?) (tesaṃ tattha|tesaṃ|tattha) ({_TR})ṃ {_V}, no ca (?:tesaṃ tattha|tesaṃ|tattha) "
                    rf"({_TR})ṃ ((?:na )?\S+?)(…pe…)?\.")
BOTH_RE = re.compile(rf"(.+?) (tesaṃ tattha|tesaṃ|tattha) ({_TR})ñca {_V} ({_TR})ñca ((?:na )?\S+?)(…pe…)?\.")


def question(s):
    s0 = s[0].lower() + s[1:] if not s.startswith("(") else s
    m = Q_RE.fullmatch(s0)
    if m:
        lab, rel, k1, v1, cor, k2, v2 = m.groups()
        rel_hi, cor_hi = S.REL_FRAMES[(rel, cor)]
        lab_hi = S.LABELS[f"({lab})"] + " " if lab else ""
        return (f"{lab_hi}{rel_hi} {TRUTHS[k1 + 'ṃ'][0]} {verb(v1)}, क्या {cor_hi} "
                f"{TRUTHS[k2 + 'ṃ'][0]} {verb(strip_v(v2))}?")
    m = ABBR_RE.fullmatch(s0)
    if m:
        lab, rel, k, v = m.groups()
        lab_hi = S.LABELS[f"({lab})"] + " " if lab else ""
        rel_hi = {"yassa vā pana": "और जिस व्यक्ति में", **S.ABBR_Q}[rel]
        if k:   # «Yattha X V…pe….» = §8 formula «जिस स्थान पर X V…।»
            end = "?" if s0.endswith("?") else "।"
            return f"{lab_hi}{rel_hi} {TRUTHS[k + 'ṃ'][0]} {verb(v)}…{end}"
        return f"{lab_hi}{rel_hi}…?"       # (Kha) yassa vā pana…pe…? / …pe….  (§0: abbreviated question «…?»)
    return None


def answer(s):
    m = BUT_RE.fullmatch(s)
    if m:
        wh, t, k1, v1, k2, v2, pe = m.groups()
        a = dict(k1=TRUTHS[k1 + "ṃ"][0], v1=verb(v1), k2=TRUTHS[k2 + "ṃ"][0], v2=verb(v2, flip=True))
        if t == "tattha":
            out = S.BUT_PLACE.format(place=S.place(wh), **a)
        else:
            out = (S.BUT_BEINGS_T if t == "tesaṃ tattha" else S.BUT_BEINGS).format(who=who(wh), **a)
        return out[:-1] + "…।" if pe else out
    m = BOTH_RE.fullmatch(s)
    if m:
        wh, t, k1, v1, k2, v2, pe = m.groups()
        a = dict(k1=TRUTHS[k1 + "ṃ"][0], v1=verb(v1), k2=TRUTHS[k2 + "ṃ"][0], v2=verb(v2))
        if t == "tattha":
            out = S.BOTH_PLACE.format(place=S.place(wh), **a)
        else:
            out = (S.BOTH_BEINGS_T if t == "tesaṃ tattha" else S.BOTH_BEINGS).format(who=who(wh), **a)
        return out[:-1] + "…।" if pe else out
    m = PLACE_PE_RE.fullmatch(s)          # Asaññasatte tattha X V…pe….
    if m:
        return f"{S.place(m.group(1))} {TRUTHS[m.group(2) + 'ṃ'][0]} {verb(m.group(3))}…।"
    return None


PLACE_PE_RE = re.compile(rf"(\S+) tattha ({_TR})ṃ ((?:na )?\S+?)…pe…\.")


def short(s):
    if s in S.CLOSINGS:
        return S.CLOSINGS[s]
    w = s[:-1]
    w = w[0].lower() + w[1:]
    if w in S.VERB_FORMS:
        return verb(w) + "।"
    return None


# ---------------------------------------------------------------------------------------------------
# Notes in round brackets and other fixed lines
# ---------------------------------------------------------------------------------------------------
YASSAKA_YASSAYATTHAKA = "व्यक्ति वाला भाग भी और व्यक्ति और स्थान वाला भाग भी समान है"   # Yassakampi yassayatthakampi sadisaṃ
NATTHI_NANA = "कोई अंतर नहीं है"                                                        # natthi nānākaraṇaṃ
NIRODHA_Q = "‘समाप्ति की ध्यान-अवस्था में लीन लोगों में’"                               # nirodhasamāpannānanti
L427_CHAIN = None   # filled below from who()

FIXED = {
    "(Yatthakaṃ uppādepi nirodhepi uppādanirodhepi sadisaṃ, natthi nānākaraṇaṃ).":
        "(स्थान वाला भाग उत्पन्न होने में भी, समाप्त होने में भी और उत्पन्न होने और समाप्त होने में भी समान है, "
        f"{NATTHI_NANA})।",
    "(Yassayatthakampi sadisaṃ vitthāretabbaṃ).":
        "(व्यक्ति और स्थान वाले भाग का भी समान रूप से विस्तार करना चाहिए)।",
    "(Yassakampi [yassakampi yatthakampi (sī. syā.)] yassayatthakampi sadisaṃ, yassayatthakepi "
    "nirodhasamāpannānanti cetaṃ na kātabbaṃ).":
        "(व्यक्ति वाला भाग [पाठभेद (Sī., Syā.): yassakampi yatthakampi] भी और व्यक्ति और स्थान वाला भाग भी समान है, "
        f"और व्यक्ति और स्थान वाले भाग में भी {NIRODHA_Q}, यह नहीं जोड़ना चाहिए)।",
    "(Yathā uppādavāre atītā pucchā anulomampi paccanīkampi vibhattā evaṃ nirodhepi vibhajitabbā, "
    "natthi nānākaraṇaṃ).":
        "(जैसे उत्पन्न होने के खंड में अतीत के प्रश्नों का सकारात्मक भी और नकारात्मक भी विभाजन किया गया है, "
        f"वैसे ही समाप्त होने में भी उनका विभाजन करना चाहिए, {NATTHI_NANA})।",
    "(Yassakampi yassayatthakampi sadisaṃ).": f"({YASSAKA_YASSAYATTHAKA})।",
    "(Yatthakaṃ uppādavārepi nirodhavārepi uppādanirodhavārepi sadisaṃ natthi nānākaraṇaṃ).":
        "(स्थान वाला भाग उत्पन्न होने के खंड में भी, समाप्त होने के खंड में भी और उत्पन्न होने और समाप्त होने के "
        f"खंड में भी समान है, {NATTHI_NANA})।",
    "(Yassakampi yassayatthakampi sadisaṃ, yassayatthakepi nirodhasamāpannānanti na kātabbaṃ).":
        f"({YASSAKA_YASSAYATTHAKA}, व्यक्ति और स्थान वाले भाग में भी {NIRODHA_Q} नहीं जोड़ना चाहिए)।",
    "(Atītā pucchā yathā uppādavāre vibhattā evaṃ uppādanirodhavārepi anulomampi paccanīkampi vibhajitabbaṃ).":
        "(अतीत के प्रश्नों का जैसे उत्पन्न होने के खंड में विभाजन किया गया है, वैसे ही उत्पन्न होने और समाप्त होने "
        "के खंड में भी उनका सकारात्मक भी और नकारात्मक भी विभाजन करना चाहिए)।",
    "(Paccuppannaatītā [paccuppannenātītā (syā.)] pucchā uppādavārepi uppādanirodhavārepi yassakampi yatthakampi "
    "yassayatthakampi anulomampi paccanīkampi sadisaṃ, asammohantena vibhajitabbā).":
        "(वर्तमान और अतीत के प्रश्न [पाठभेद (Syā.): paccuppannenātītā] उत्पन्न होने के खंड में भी और उत्पन्न "
        "होने और समाप्त होने के खंड में भी, व्यक्ति वाले भाग में भी, स्थान वाले भाग में भी, व्यक्ति और स्थान वाले "
        "भाग में भी, सकारात्मक में भी और नकारात्मक में भी समान हैं, बिना भ्रम के उनका विभाजन करना चाहिए)।",
}


def fixed_lines():
    d = dict(FIXED)
    chain = who("aggamaggassa bhaṅgakkhaṇe arahantānaṃ asaññasattānaṃ")
    d["(Yassakampi yassayatthakampi sadisaṃ, samudayasaccaṃ maggasaccaṃ nānākaraṇaṃ, aggamaggassa bhaṅgakkhaṇe, "
      "arahantānaṃ asaññasattānaṃ tesaṃ tattha maggasaccañca na nirujjhissati samudayasaccañca nuppajjissati)."] = (
        f"({YASSAKA_YASSAYATTHAKA}, {TRUTH_OBL['samudayasaccaṃ']} और {TRUTH_OBL['maggasaccaṃ']} में यह अंतर है कि "
        f"{chain} वहाँ {TRUTHS['maggasaccaṃ'][0]} भी {verb('na nirujjhissati')} और "
        f"{TRUTHS['samudayasaccaṃ'][0]} भी {verb('nuppajjissati')})।")
    w1 = who("Aggamaggasamaṅgīnaṃ arahantānaṃ yassa cittassa anantarā aggamaggaṃ paṭilabhissanti asaññasattānaṃ")
    w2 = who("itaresaṃ catuvokārānaṃ pañcavokārānaṃ")
    d["Aggamaggasamaṅgīnaṃ arahantānaṃ yassa cittassa anantarā aggamaggaṃ paṭilabhissanti asaññasattānaṃ tesaṃ "
      "tattha …pe… itaresaṃ catuvokārānaṃ pañcavokārānaṃ tesaṃ tattha…pe…. (Yassakampi yassayatthakampi sadisaṃ)."] = (
        f"{w1} वहाँ … {w2} वहाँ…। ({YASSAKA_YASSAYATTHAKA})।")
    return d


FIXED_ALL = None


def translate_text_line(line):
    global FIXED_ALL
    if FIXED_ALL is None:
        FIXED_ALL = fixed_lines()
    if line in FIXED_ALL:
        return FIXED_ALL[line]
    out = []
    for s in S._split_sentences(line):
        r = None
        if s.endswith("?") or s.startswith(("(Ka)", "(Kha)", "Yassa ", "Yattha ")):
            r = question(s)
        if r is None:
            r = answer(s) or short(s)
        if r is None:
            raise ValueError(f"no formula for: {s}")
        out.append(r)
    return " ".join(out)


def translate_line(line):
    if not line.strip():
        return ""
    bid = ""
    m = S.ID_RE.search(line)
    if m:
        bid = " " + m.group(1)
        line = line[: m.start()]
    if line.startswith("#"):
        hashes, text = line.split(" ", 1)
        return f"{hashes} {S.HEADINGS[text]}{bid}"
    return translate_text_line(line.strip()) + bid


def main():
    dry = "--dry" in sys.argv
    pali = (S.PALI_DIR / FILE).read_text(encoding="utf-8")
    out, prev_blank, fails = [], True, []
    for n, line in enumerate(pali.splitlines(), 1):
        if not line.strip():
            if not prev_blank:
                out.append("")
            prev_blank = True
            continue
        try:
            out.append(translate_line(line))
        except (ValueError, KeyError) as e:
            fails.append(f"{n}: {e}")
            out.append("@@FAIL@@")
        prev_blank = False
    while out and out[-1] == "":
        out.pop()
    for f in fails:
        print(f)
    print(f"lines {len(out)}, failures {len(fails)}")
    if not dry and not fails:
        (S.HI_DIR / FILE).write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")
        print("written", S.HI_DIR / FILE)


if __name__ == "__main__":
    main()
