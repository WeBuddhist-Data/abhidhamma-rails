"""pi-6 Hindi plain RAILS: builder for 3-05-ayatanayamaka.md and 3-06-ayatanayamaka.md.

Imports build_rails_sample.py read-only for every shared formula string; adds the āyatana names, the
sa-/a-X-ka modifiers (harmonise I1), multi-place chunks, pariññā answers and the notes of these two files.
usage: python -I -X utf8 build_3-05-3-06.py [--dry]
"""
import re
import sys

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-hi\rails")
import build_rails_sample as S  # noqa: E402

FILES = ["3-05-ayatanayamaka.md", "3-06-ayatanayamaka.md"]

# ------------------------------------------------------------------ āyatana names (termbase), all masculine
AYATANA = {
    "cakkh": "आँख का इंद्रिय-क्षेत्र",
    "sot": "कान का इंद्रिय-क्षेत्र",
    "ghān": "नाक का इंद्रिय-क्षेत्र",
    "rūp": "दृश्य रूप का इंद्रिय-क्षेत्र",
    "man": "मन का इंद्रिय-क्षेत्र",
    "dhamm": "मन के विषयों का इंद्रिय-क्षेत्र",
}
NAME_RE = re.compile(r"(cakkh|sot|ghān|rūp|man|dhamm)āyatana(?:ṃ|ñca)?")


def nm(w):
    m = re.fullmatch(r"(cakkh|sot|ghān|rūp|man|dhamm)āyatana(?:ṃ|ñca)?", w)
    if not m:
        raise ValueError(f"name: {w}")
    return AYATANA[m.group(1)]


def nm_obl(w):
    return nm(w).replace(" का इंद्रिय-क्षेत्र", " के इंद्रिय-क्षेत्र")


# cycle labels (termbase)
CYCLE = {
    "(Cakkhāyatanamūlakaṃ)": "(आँख के इंद्रिय-क्षेत्र पर आधारित)",
    "(Ghānāyatanamūlakaṃ)": "(नाक के इंद्रिय-क्षेत्र पर आधारित)",
    "(Rūpāyatanamūlakaṃ)": "(दृश्य रूप के इंद्रिय-क्षेत्र पर आधारित)",
}

# sa-X-ka / a-X-ka modifiers (termbase; harmonise I1: «X वाले» / «X से रहित», before the place)
MODS = {
    "sacakkhukānaṃ": "आँख वाले", "acakkhukānaṃ": "आँख से रहित",
    "sasotakānaṃ": "कान वाले", "asotakānaṃ": "कान से रहित",
    "saghānakānaṃ": "नाक वाले", "aghānakānaṃ": "नाक से रहित",
    "sarūpakānaṃ": "भौतिक रूप वाले", "arūpakānaṃ": "भौतिक रूप से रहित",
    "sacittakānaṃ": "मन वाले", "acittakānaṃ": "मन से रहित",
}
PLACE_OR = " या "        # several places in one chunk (rūpāvacare arūpāvacare …), as harmonise I3 «चार या पाँच»
CATUPANCA_BEINGS = "चार या पाँच समूहों वाले अस्तित्व के प्राणियों में"   # catuvokārānaṃ pañcavokārānaṃ (I3)
TOKEN_SLIPS = {"parinibbāntānaṃ": "parinibbantānaṃ", "tasaṃ": "tesaṃ"}
VERB_SLIPS = {"upapajjissati": "uppajjissati"}


def places_hi(places):
    keys = [k for k, _ in places]
    if keys == ["catuvokāra", "pañcavokāra"]:
        keys = ["catupañcavokāra"]
    return PLACE_OR.join(S.PLACE_NOUN[k] for k in keys) + " " + S.CASE_POST[places[0][1]]


def who(s):
    """Being chain (before the resumptive tesaṃ) -> Hindi; every chunk ends in «में», last joined «और»."""
    s = s.strip()
    s = s[0].lower() + s[1:]
    toks = [TOKEN_SLIPS.get(t, t) for t in s.split(" ")]
    if toks == ["itaresaṃ"]:
        return S.ITARESAM_ALONE
    chunks, pre, places, i = [], [], [], 0
    while i < len(toks):
        w = toks[i]
        if w == "ye":
            # ye [ca] <places> upapajjitvā parinibbāyissanti [tesaṃ cavantānaṃ|upapajjantānaṃ]
            j = i + 1
            if toks[j] == "ca":
                j += 1
            pl = []
            while toks[j] in S.PLACE_FORMS:
                pl.append(S.PLACE_FORMS[toks[j]])
                j += 1
            assert toks[j:j + 2] == ["upapajjitvā", "parinibbāyissanti"], s
            j += 2
            txt = S.YE_PARINIBBAYISSANTI.format(place=places_hi(pl)[: -len(" में")])
            if j + 1 < len(toks) and toks[j] == "tesaṃ" and toks[j + 1] in ("cavantānaṃ", "upapajjantānaṃ"):
                txt += " से " + S.PARTICIPLES[toks[j + 1]]
                j += 2
            chunks.append(" ".join(pre + [txt]))
            pre = []
            i = j
            continue
        if w == "sabbesaṃ":
            pre.append(S.SABBESAM)
        elif w == "itaresaṃ":
            pre.append(S.ITARESAM)
        elif w in MODS:
            pre.append(MODS[w])
        elif w in S.PLACE_FORMS:
            places.append(S.PLACE_FORMS[w])
        elif w == "catuvokārānaṃ" and i + 1 < len(toks) and toks[i + 1] == "pañcavokārānaṃ" and not places:
            chunks.append(" ".join(pre + [CATUPANCA_BEINGS]))
            pre = []
            i += 1
        elif w in S.BEINGS and not places:
            chunks.append(" ".join(pre + [S.BEINGS[w]]))
            pre = []
        elif w == "pacchimabhavikānaṃ" and i + 1 < len(toks) and (
                toks[i + 1] == "upapajjantānaṃ" or (toks[i + 1] in S.PLACE_FORMS and i + 2 < len(toks)
                                                    and toks[i + 2] == "upapajjantānaṃ")):
            if toks[i + 1] in S.PLACE_FORMS:
                key, _ = S.PLACE_FORMS[toks[i + 1]]
                chunks.append(" ".join(pre + [f"{S.PLACE_NOUN[key]} में {S.PACCHIMA_UPAPAJJ}"]))
                i += 2
            else:
                chunks.append(" ".join(pre + [S.PACCHIMA_UPAPAJJ]))
                i += 1
            pre = []
        elif w in S.PARTICIPLES:
            if places:
                chunks.append(" ".join(pre + [places_hi(places) + " " + S.PARTICIPLES[w]]))
            else:
                chunks.append(" ".join(pre + [S.PARTICIPLES[w]]))
            pre, places = [], []
        else:
            raise ValueError(f"who: unknown token {w!r} in {s!r}")
        i += 1
    if pre or places:
        raise ValueError(f"who: dangling tokens in {s!r}")
    if len(chunks) == 1:
        return chunks[0]
    return S.JOIN.join(chunks[:-1]) + S.JOIN_LAST + chunks[-1]


# ------------------------------------------------------------------ verbs
def verb(tok, flip=False):
    tok = tok.strip()
    neg = tok.startswith("na ")
    w = tok[3:] if neg else tok
    w = S.VERB_SLIPS.get(VERB_SLIPS.get(w, w), VERB_SLIPS.get(w, w))
    if w not in S.VERB_FORMS:
        w = S.strip_ti(w, set(S.VERB_FORMS))
    stem, n = S.VERB_FORMS[w]
    pos_s, neg_s = S.VERBS[(stem, "m")]
    return neg_s if ((neg or n) != flip) else pos_s


def subj_hi(text):
    """'cakkhāyatanaṃ…pe… ghānāyatanaṃ… manāyatanaṃ' -> Hindi (names, '…pe…' -> '…')."""
    t = re.sub(r"\s*…pe…\s*", "… ", text.strip())
    t = re.sub(r"…\s+", "… ", t)
    t = NAME_RE.sub(lambda m: AYATANA[m.group(1)], t)
    return t.strip()


# ------------------------------------------------------------------ questions
_REL = r"([Yy]assa vā pana yattha|[Yy]assa yattha|[Yy]assa vā pana|[Yy]assa|[Yy]attha vā pana|[Yy]attha)"
_COR = r"(tassa tattha|tassa|tattha)"
_VQ = r"((?:na )?(?:n?uppajj|nirujjh|upapajj)\S*)"
_LABQ = r"(?:\((Ka|Kha)\) )?"


def rel_hi(rel, cor=None):
    rel = rel[0].lower() + rel[1:]
    if cor is None:
        cor = "tassa tattha" if "yassa" in rel and "yattha" in rel else ("tattha" if rel.startswith("yattha") else "tassa")
    return S.REL_FRAMES[(rel, cor)]


def question(s):
    m = re.fullmatch(rf"{_LABQ}{_REL} (.+?) {_VQ} {_COR} (.+?) {_VQ}\?", s)
    if not m:
        return None
    lab, rel, k1, v1, cor, k2, v2 = m.groups()
    r, c = rel_hi(rel, cor)
    out = f"{r} {subj_hi(k1)} {verb(v1)}, क्या {c} {subj_hi(k2)} {verb(v2)}?"
    return (S.LABELS[f"({lab})"] + " " + out) if lab else out


def abbr_question(s):
    """'(Kha) yassa vā pana ghānāyatanaṃ…pe….' / 'Yattha cakkhāyatanaṃ nirujjhati…pe….' / '(Kha) yassa vā pana…pe…?'"""
    m = re.fullmatch(rf"{_LABQ}{_REL}((?: \S+)?)((?: (?:na )?\S+)?)…pe…([.?])", s)
    if not m:
        return None
    lab, rel, k, v, end = m.groups()
    r, _ = rel_hi(rel)
    out = r
    if k.strip():
        out += " " + nm(k.strip())
    if v.strip():
        out += " " + verb(v.strip())
    out += "…" + ("?" if end == "?" else "।")
    return (S.LABELS[f"({lab})"] + " " + out) if lab else out


# ------------------------------------------------------------------ answers
_T = r"(tesaṃ tattha|tesaṃ|tasaṃ tattha)"
_V = r"((?:na )?[^\s,]+)"
_NM = r"((?:cakkh|sot|ghān|rūp|man|dhamm)āyatana)"


def answer(s):
    if "…pe…" in s:
        return None
    m = re.fullmatch(rf"(.+?) {_T} {_NM}ṃ {_V}, no ca {_T} {_NM}ṃ {_V}\.", s)
    if m:
        wh, t, k1, v1, _, k2, v2 = m.groups()
        frame = S.BUT_BEINGS_T if t.endswith("tattha") else S.BUT_BEINGS
        return frame.format(who=who(wh), k1=nm(k1), v1=verb(v1), k2=nm(k2), v2=verb(v2, flip=True))
    m = re.fullmatch(rf"(.+?) {_T} {_NM}ñca {_V},? {_NM}ñca {_V}\.", s)
    if m:
        wh, t, k1, v1, k2, v2 = m.groups()
        frame = S.BOTH_BEINGS_T if t.endswith("tattha") else S.BOTH_BEINGS
        return frame.format(who=who(wh), k1=nm(k1), v1=verb(v1), k2=nm(k2), v2=verb(v2))
    return None


def abbr_piece(p):
    """A piece of an answer cut by '…pe…' (without the '…pe…')."""
    p = p.strip()
    m = re.fullmatch(rf"(.+?) {_T} {_NM}ṃ {_V}, no ca {_T}", p)
    if m:
        wh, t, k1, v1, t2 = m.groups()
        tt = " वहाँ" if t.endswith("tattha") else ""
        return f"{who(wh)}{tt} {nm(k1)} {verb(v1)}, पर उनमें{tt}"
    m = re.fullmatch(rf"(.+?) {_T} {_NM}ṃ", p)
    if m:
        return who(m.group(1)) + (" वहाँ " if m.group(2).endswith("tattha") else " ") + nm(m.group(3))
    m = re.fullmatch(rf"(.+?) {_T}", p)
    if m:
        return who(m.group(1)) + (" वहाँ" if m.group(2).endswith("tattha") else "")
    raise ValueError(f"abbr piece: {p}")


def abbr_answer(s):
    if "…pe…" not in s or s.startswith(("(", "Yassa", "Yattha", "yassa", "yattha")):
        return None
    pieces = s.split("…pe…")
    out = []
    for j, p in enumerate(pieces):
        p = p.strip()
        if j == len(pieces) - 1:
            if p in ("", "."):
                out[-1] += "।"          # the piece already ends with «…»
                break
            p = p[0].upper() + p[1:]
            r = answer(p)
            if r is None:
                raise ValueError(f"abbr last piece: {p}")
            r = r[0] + r[1:]
            out.append(r)
        else:
            out.append(abbr_piece(p) + "…")
    return " ".join(out)


# ------------------------------------------------------------------ pariññā
PARI_PL = {"parijānāti": ("पूरी तरह समझते हैं", "पूरी तरह नहीं समझते"),
           "parijānittha": ("पूरी तरह समझा था", "पूरी तरह नहीं समझा था"),
           "parijānissati": ("पूरी तरह समझेंगे", "पूरी तरह नहीं समझेंगे")}
PARI_FORMS = {"parijānāti": ("parijānāti", "sg"), "parijānittha": ("parijānittha", "sg"),
              "parijānissati": ("parijānissati", "sg"), "parijānanti": ("parijānāti", "pl"),
              "parijānissanti": ("parijānissati", "pl")}


def pari_v(tok, flip=False, num=None):
    neg = tok.startswith("na ")
    w = tok[3:] if neg else tok
    stem, n = PARI_FORMS[w]
    n = num or n
    table = S.PARIJANATI if n == "sg" else PARI_PL
    return table[stem][1 if (neg != flip) else 0], stem == "parijānittha"


def pari_question(s):
    m = re.fullmatch(rf"\((Ka|Kha)\) yo( vā pana)? {_NM}ṃ ((?:na )?\S+) so {_NM}ṃ ((?:na )?\S+)\?", s)
    if not m:
        return None
    lab, vp, o1, v1, o2, v2 = m.groups()
    neg2 = v2.startswith("na ")
    v2 = ("na " if neg2 else "") + S.strip_ti(v2[3:] if neg2 else v2, set(S.PARIJANATI))
    v1h, past1 = pari_v(v1)
    v2h, past2 = pari_v(v2)
    rel = ("और " if vp else "") + ("जिस व्यक्ति ने" if past1 else "जो व्यक्ति")
    cor = "उसने" if past2 else "वह"
    return f"{S.LABELS[f'({lab})']} {rel} {nm_obl(o1)} को {v1h}, क्या {cor} {nm_obl(o2)} को {v2h}?"


PARI_SG = {"Arahā": ("अर्हत्", "अर्हत् ने"),
           "Aggamaggasamaṅgī": ("सर्वोच्च मार्ग से युक्त व्यक्ति", "सर्वोच्च मार्ग से युक्त व्यक्ति ने")}
PARI_PL_SUBJ = {   # (direct, ergative)
    "Ye maggaṃ paṭilabhissanti te": ("जो मार्ग प्राप्त करेंगे, वे", "जो मार्ग प्राप्त करेंगे, उन्होंने"),
    "Aggamaggasamaṅgiñca arahantañca ṭhapetvā avasesā puggalā":
        ("सर्वोच्च मार्ग से युक्त व्यक्ति और अर्हत् को छोड़कर शेष व्यक्ति",
         "सर्वोच्च मार्ग से युक्त व्यक्ति और अर्हत् को छोड़कर शेष व्यक्तियों ने"),
    "Arahā ye ca puthujjanā maggaṃ na paṭilabhissanti te":
        ("अर्हत् और जो साधारण व्यक्ति मार्ग प्राप्त नहीं करेंगे, वे",
         "अर्हत् और जो साधारण व्यक्ति मार्ग प्राप्त नहीं करेंगे, उन्होंने"),
    "Aggamaggasamaṅgī ye ca puthujjanā maggaṃ na paṭilabhissanti te":
        ("सर्वोच्च मार्ग से युक्त व्यक्ति और जो साधारण व्यक्ति मार्ग प्राप्त नहीं करेंगे, वे",
         "सर्वोच्च मार्ग से युक्त व्यक्ति और जो साधारण व्यक्ति मार्ग प्राप्त नहीं करेंगे, उन्होंने"),
}


def pari_answer(s):
    m = re.fullmatch(rf"(Arahā|Aggamaggasamaṅgī) {_NM}ṃ (na \S+), no ca {_NM}ṃ (na \S+)\.", s)
    if m:
        sb, o1, v1, o2, v2 = m.groups()
        v1h, p1 = pari_v(v1, num="sg")
        v2h, p2 = pari_v(v2, flip=True, num="sg")
        subj = PARI_SG[sb][1 if p1 else 0]
        pron = "उसने" if p2 else "वह"
        return f"{subj} {nm_obl(o1)} को {v1h}, पर {pron} {nm_obl(o2)} को {v2h}।"
    m = re.fullmatch(rf"(Ye maggaṃ paṭilabhissanti te) {_NM}ṃ (na \S+), no ca {_NM}ṃ (na \S+)\.", s)
    if m:
        sb, o1, v1, o2, v2 = m.groups()
        v1h, p1 = pari_v(v1, num="pl")
        v2h, p2 = pari_v(v2, flip=True, num="pl")
        subj = PARI_PL_SUBJ[sb][1 if p1 else 0]
        pron = "उन्होंने" if p2 else "वे"
        return f"{subj} {nm_obl(o1)} को {v1h}, पर {pron} {nm_obl(o2)} को {v2h}।"
    m = re.fullmatch(rf"(.+?) {_NM}ñca (na \S+) {_NM}ñca (na \S+)\.", s)
    if m and m.group(1) in PARI_PL_SUBJ:
        sb, o1, v1, o2, v2 = m.groups()
        v1h, p1 = pari_v(v1, num="pl")
        v2h, p2 = pari_v(v2, num="pl")
        subj = PARI_PL_SUBJ[sb][1 if p1 else 0]
        pron2 = "" if p1 == p2 else ("उन्होंने " if p2 else "वे ")
        return f"{subj} {nm_obl(o1)} को भी {v1h} और {pron2}{nm_obl(o2)} को भी {v2h}।"
    return None


# ------------------------------------------------------------------ fixed lines (notes)
FIXED_LINES = {
    "(Kha) yassa vā pana yattha ghānāyatanaṃ…pe… (yathā paccuppannātītepi tividhaṃ vitthāritaṃ evaṃ idampi "
    "vitthāretabbaṃ).":
        "(ख) और जिस व्यक्ति में जिस स्थान पर नाक का इंद्रिय-क्षेत्र… (जैसे वर्तमान और अतीत के खंड में भी तीन "
        "प्रकार से विस्तार किया गया है, वैसे ही इसका भी विस्तार करना चाहिए)।",
    "Yattha cakkhāyatanaṃ uppajjati…pe… (yatthakaṃ noti na kātabbaṃ, yatthakaṃ itaresaṃ yatthakānaṃ sadisaṃ "
    "kātabbaṃ, yatthakaṃ tīsupi vāresu sadisaṃ).":
        "जिस स्थान पर आँख का इंद्रिय-क्षेत्र उत्पन्न होता है… (स्थान वाले भाग में “नहीं” उत्तर नहीं देना चाहिए, "
        "स्थान वाले भाग को बाकी स्थान वाले भागों के समान करना चाहिए, स्थान वाला भाग तीनों खंडों में समान है)।",
    "(Yassakampi yassayatthakampi sadisaṃ).":
        "(व्यक्ति वाला भाग भी और व्यक्ति और स्थान वाला भाग भी समान हैं)।",
    "(Atītā pucchā uppādepi nirodhepi uppādanirodhepi anulomampi paccanīkampi sadisaṃ).":
        "(अतीत के प्रश्न उत्पन्न होने में भी, समाप्त होने में भी और उत्पन्न होने और समाप्त होने में भी "
        "सकारात्मक भी और नकारात्मक भी समान हैं)।",
    "(Yathā uppādavāre paccuppannātītā pucchā vibhattā evaṃ uppādanirodhepi paccuppannātītā pucchā anulomampi "
    "paccanīkampi vibhajitabbā [vibhajitabbaṃ (sī syā. ka.)] ).":
        "(जैसे उत्पन्न होने के खंड में वर्तमान और अतीत के प्रश्नों का विभाजन किया गया है, वैसे ही उत्पन्न होने "
        "और समाप्त होने में भी वर्तमान और अतीत के प्रश्नों का सकारात्मक भी और नकारात्मक भी विभाजन करना चाहिए "
        "[वर्तनी-भेद (Sī., Syā., Ka.): vibhajitabbaṃ])।",
    "(Yathā nirodhavāre atītānāgatā [atītenānāgatā (syā.)] pucchā yassakampi yatthakampi yassayatthakampi "
    "anulomampi paccanīkampi vibhattaṃ, evaṃ uppādanirodhepi atītānāgatā pucchā vibhajitabbā.)":
        "(जैसे समाप्त होने के खंड में अतीत और भविष्य [पाठभेद (Syā.): atītenānāgatā] के प्रश्नों का व्यक्ति वाले "
        "भाग में भी, स्थान वाले भाग में भी, व्यक्ति और स्थान वाले भाग में भी, सकारात्मक भी और नकारात्मक भी "
        "विभाजन किया गया है, वैसे ही उत्पन्न होने और समाप्त होने में भी अतीत और भविष्य के प्रश्नों का विभाजन "
        "करना चाहिए।)",
}
CLOSINGS = dict(S.CLOSINGS)
CLOSINGS["Āyatanayamakaṃ niṭṭhitaṃ."] = S.CHAPTER_END.format(title=S.CHAPTER_TITLES["Āyatanayamakaṃ"])
SHORT = {"Nirujjhati.": "समाप्त होता है।", "Nirujjhittha.": "समाप्त हुआ था।", "Nirujjhissati.": "समाप्त होगा।",
         "No …pe….": "नहीं …।", "Āmantā …pe….": "हाँ …।"}


def sentence(s):
    if s in CLOSINGS:
        return CLOSINGS[s]
    if s in SHORT:
        return SHORT[s]
    if s in CYCLE:
        return CYCLE[s]
    for fn in (pari_question, question, abbr_question, pari_answer, answer, abbr_answer):
        r = fn(s)
        if r:
            return r
    raise ValueError(f"no formula: {s}")


_SPLIT = re.compile(r"(?<=[.?]) (?=[A-ZĀĪŪṬḌṆÑṄ(])")


def text_line(line):
    if line in FIXED_LINES:
        return FIXED_LINES[line]
    return " ".join(sentence(s) for s in _SPLIT.split(line))


def tr_line(line):
    bid = ""
    m = S.ID_RE.search(line)
    if m:
        bid = " " + m.group(1)
        line = line[: m.start()]
    line = line.strip()
    if line.startswith("#"):
        hashes, text = line.split(" ", 1)
        return f"{hashes} {S.HEADINGS[text]}{bid}"
    return text_line(line) + bid


def tr_text(pali):
    out, prev_blank = [], True
    for line in pali.splitlines():
        if not line.strip():
            if not prev_blank:
                out.append("")
            prev_blank = True
            continue
        out.append(tr_line(line))
        prev_blank = False
    while out and out[-1] == "":
        out.pop()
    return "\n".join(out) + "\n"


def main():
    dry = "--dry" in sys.argv
    for f in FILES:
        pali = (S.PALI_DIR / f).read_text(encoding="utf-8")
        hi = tr_text(pali)
        if dry:
            print(f, "OK", hi.count("\n"), "lines")
        else:
            (S.HI_DIR / f).write_text(hi, encoding="utf-8", newline="\n")
            print("wrote", f)


if __name__ == "__main__":
    main()
