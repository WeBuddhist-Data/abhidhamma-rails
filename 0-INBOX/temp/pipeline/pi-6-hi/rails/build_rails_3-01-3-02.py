"""pi-6 Āyatanayamaka 3-01 / 3-02: Pāli -> Hindi plain RAILS.

Imports build_rails_sample.py read-only (constants and the beings/places/verbs tables) and adds the āyatana
word tables, the organ modifiers (harmonise I1) and hand-checked fixed lines. Writes only
AI_translation\\hindi\\pi-6-hindi-plain-rails_split_chapters\\3-01-ayatanayamaka.md and 3-02-ayatanayamaka.md.

usage: python -I -X utf8 build_rails_3-01-3-02.py
"""
import re
import sys

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-hi\rails")
import build_rails_sample as S  # noqa: E402  (read-only)

FILES = ["3-01-ayatanayamaka.md", "3-02-ayatanayamaka.md"]

# ------------------------------------------------------------------------------------------------
# Words (termbase)
# ------------------------------------------------------------------------------------------------
IK = "इंद्रिय-क्षेत्र"
# bare words of the word-checking pairs: nominative key -> (Hindi, number)
BARE = {
    "cakkhu": ("आँख", "sg"), "sotaṃ": ("कान", "sg"), "ghānaṃ": ("नाक", "sg"), "jivhā": ("जीभ", "sg"),
    "kāyo": ("शरीर", "sg"), "rūpaṃ": ("रूप", "sg"), "saddo": ("ध्वनि", "sg"), "gandho": ("गंध", "sg"),
    "raso": ("स्वाद", "sg"), "phoṭṭhabbo": ("स्पर्श", "sg"), "mano": ("मन", "sg"),
    "dhammo": ("परिघटना", "sg"),          # no termbase entry: core term dhamma = परिघटना
    "āyatanaṃ": (IK, "sg"), "āyatanā": (IK, "pl"),
}
# sense bases: Pāli stem -> Hindi noun (genitive: "<noun> का इंद्रिय-क्षेत्र")
AYAT_STEMS = {
    "cakkh": "आँख", "sot": "कान", "ghān": "नाक", "jivh": "जीभ", "kāy": "शरीर", "rūp": "दृश्य रूप",
    "sadd": "ध्वनि", "gandh": "गंध", "ras": "स्वाद", "phoṭṭhabb": "स्पर्श", "man": "मन",
    "dhamm": "मन के विषयों",
}
AYAT = {f"{s}āyatanaṃ": f"{n} का {IK}" for s, n in AYAT_STEMS.items()}
AYAT_OBL = {f"{s}āyatanaṃ": f"{n} के {IK}" for s, n in AYAT_STEMS.items()}
WORDS = {**BARE, **{k: (v, "sg") for k, v in AYAT.items()}}
OBL = {**{k: v[0] for k, v in BARE.items()}, **AYAT_OBL}
# accusative bare forms -> nominative key
ACC = {"cakkhuṃ": "cakkhu", "sotaṃ": "sotaṃ", "ghānaṃ": "ghānaṃ", "jivhaṃ": "jivhā", "kāyaṃ": "kāyo",
       "rūpaṃ": "rūpaṃ", "saddaṃ": "saddo", "gandhaṃ": "gandho", "rasaṃ": "raso", "phoṭṭhabbaṃ": "phoṭṭhabbo",
       "manaṃ": "mano", "dhammaṃ": "dhammo", "āyatanaṃ": "āyatanaṃ", **{k: k for k in AYAT}}
# figurative subjects of the niddesa answers (termbase; harmonise I2, B11)
SPECIAL = {
    "dibbacakkhu paññācakkhu": ("दिव्य आँख और प्रज्ञा की आँख", "pl"),
    "dibbasotaṃ taṇhāsotaṃ": ("दिव्य कान और तृष्णा की धारा", "pl"),
    "sīlagandho samādhigandho paññāgandho": ("सदाचार की गंध, एकाग्रता की गंध और प्रज्ञा की गंध", "pl"),
    "attharaso dhammaraso vimuttiraso": ("अर्थ का स्वाद, शिक्षा का स्वाद और मुक्ति का स्वाद", "pl"),
}
AVASESA_NUM = {"avaseso": "sg", "avasesaṃ": "sg", "avasesā": "pl"}

# process subjects (masculine इंद्रिय-क्षेत्र)
PROC = {k: (v, "m") for k, v in AYAT.items()}

# organ modifiers, harmonise I1: sa-X-ka «X वाले», a-X-ka «X से रहित», several joined « और », before the place
MODS = {
    "sacakkhukānaṃ": "आँख वाले", "acakkhukānaṃ": "आँख से रहित",
    "sasotakānaṃ": "कान वाले", "asotakānaṃ": "कान से रहित",
    "saghānakānaṃ": "नाक वाले", "aghānakānaṃ": "नाक से रहित",
    "sarūpakānaṃ": "भौतिक रूप वाले", "arūpakānaṃ": "भौतिक रूप से रहित",
    "sacittakānaṃ": "मन वाले", "acittakānaṃ": "मन से रहित",
}
CATUPANCA_BEINGS = "चार या पाँच समूहों वाले अस्तित्व के प्राणियों में"   # catuvokārānaṃ pañcavokārānaṃ (I3)
YE_TWO = "जो {p1} या {p2} में जन्म लेकर पूर्ण निर्वाण पाएँगे, उनमें"     # Ye X Y upapajjitvā parinibbāyissanti (new)

MULAKA = "({x} पर आधारित)"            # (Cakkhāyatanamūlakaṃ)
CAKKAM = "(चक्र पूरा करना चाहिए)"     # (Cakkaṃ bandhitabbaṃ)
SAMKHITTAM = "संक्षिप्त किया गया है"

SLIPS = [  # source slips, read as (report)
    ("uppajjittharūpāyatanañca", "uppajjittha rūpāyatanañca"),   # 3-01 ^6-3-43
    ("rūpāyatanañca ca uppajjittha", "rūpāyatanañca uppajjittha"),  # 3-02 ^6-3-75
    ("sotāyananti", "sotāyatananti"),                              # 3-01 ^6-3-13
]

# ------------------------------------------------------------------------------------------------
# Fixed lines (whole Pāli line without block ID -> Hindi), read and translated one by one
# ------------------------------------------------------------------------------------------------
FIXED_LINES = {
    # 3-01 ^6-3-1 (comma missing after sotāyatanaṃ in the Pāli)
    "Dvādasāyatanāni – cakkhāyatanaṃ, sotāyatanaṃ ghānāyatanaṃ, jivhāyatanaṃ, kāyāyatanaṃ, rūpāyatanaṃ, "
    "saddāyatanaṃ, gandhāyatanaṃ, rasāyatanaṃ, phoṭṭhabbāyatanaṃ, manāyatanaṃ, dhammāyatanaṃ.":
        "बारह इंद्रिय-क्षेत्र – आँख का इंद्रिय-क्षेत्र, कान का इंद्रिय-क्षेत्र, नाक का इंद्रिय-क्षेत्र, "
        "जीभ का इंद्रिय-क्षेत्र, शरीर का इंद्रिय-क्षेत्र, दृश्य रूप का इंद्रिय-क्षेत्र, ध्वनि का इंद्रिय-क्षेत्र, "
        "गंध का इंद्रिय-क्षेत्र, स्वाद का इंद्रिय-क्षेत्र, स्पर्श का इंद्रिय-क्षेत्र, मन का इंद्रिय-क्षेत्र, "
        "मन के विषयों का इंद्रिय-क्षेत्र।",
    # 3-01 ^6-3-12
    "(Ekekapadamūlakaṃ cakkaṃ bandhitabbaṃ asammohantena).":
        "(हर एक शब्द पर आधारित चक्र बिना भ्रम के पूरा करना चाहिए)।",
    # 3-01 ^6-3-13
    "(Cakkaṃ bandhantena sabbattha āmantāti kātabbaṃ).":
        "(चक्र पूरा करते समय हर जगह “हाँ” कहना चाहिए)।",
    # 3-01 ^6-3-23 line 3
    "(Yattha ghānāyatanaṃ uppajjati tattha manāyatanaṃ dhammāyatanañca ekasadisaṃ, nānaṃ natthi, upari pana "
    "vārasaṅkhepo [uparivāre saṅkhepo (syā.), uparivāre saṅkhepaṃ (sī. ka.)] tīti jānitabbaṃ.)":
        "(जिस स्थान पर नाक का इंद्रिय-क्षेत्र उत्पन्न होता है, वहाँ मन का इंद्रिय-क्षेत्र और मन के विषयों का "
        "इंद्रिय-क्षेत्र बिलकुल समान हैं, कोई अंतर नहीं है, पर आगे खंड संक्षेप में है "
        "[पाठभेद (Syā.): uparivāre saṅkhepo; (Sī., Ka.): uparivāre saṅkhepaṃ], ऐसा जानना चाहिए।)",
    # 3-01 ^6-3-40
    "(Ka) yattha cakkhāyatanaṃ uppajjittha…pe… (yatthakaṃ paccuppannepi atītepi anāgatepi paccuppannātītepi "
    "paccuppannānāgatepi atītānāgatepi sabbattha sadisaṃ, uppajjati uppajjitthāti nāmaṃ atirekaṃ kātabbaṃ).":
        "(क) जिस स्थान पर आँख का इंद्रिय-क्षेत्र उत्पन्न हुआ था… (स्थान वाला भाग वर्तमान में भी, अतीत में भी, "
        "भविष्य में भी, वर्तमान और अतीत में भी, वर्तमान और भविष्य में भी, अतीत और भविष्य में भी, हर जगह समान है; "
        "केवल “उत्पन्न होता है”, “उत्पन्न हुआ था” शब्द अलग से जोड़ने चाहिए)।",
    # 3-02 ^6-3-52 line 8
    "Yassa cakkhāyatanaṃ uppajjissati (tassa manāyatanañca dhammāyatanañca sadisaṃ, ime dve sadisāyeva honti).":
        "जिस व्यक्ति में आँख का इंद्रिय-क्षेत्र उत्पन्न होगा (उसमें मन का इंद्रिय-क्षेत्र और मन के विषयों का "
        "इंद्रिय-क्षेत्र समान हैं, ये दोनों समान ही होते हैं)।",
}
# fixed sentences inside longer lines (variant brackets)
FIXED_SENTENCES = {
    "Cakkhuñca cakkhāyatanañca ṭhapetvā avasesaṃ [avasesā (syā. pī.)] na ceva cakkhu na ca cakkhāyatanaṃ.":
        "आँख और आँख के इंद्रिय-क्षेत्र को छोड़कर शेष [वर्तनी-भेद (Syā., Pī.): avasesā] न तो आँख है, "
        "न आँख का इंद्रिय-क्षेत्र।",
    "Kāyañca kāyāyatanañca ṭhapetvā avasesaṃ [avaseso (syā.)] na ceva kāyo na ca kāyāyatanaṃ.":
        "शरीर और शरीर के इंद्रिय-क्षेत्र को छोड़कर शेष [वर्तनी-भेद (Syā.): avaseso] न तो शरीर है, "
        "न शरीर का इंद्रिय-क्षेत्र।",
    "Gandhañca gandhāyatanañca ṭhapetvā avasesaṃ [avasesā (syā.)] na ceva gandho na ca gandhāyatanaṃ.":
        "गंध और गंध के इंद्रिय-क्षेत्र को छोड़कर शेष [वर्तनी-भेद (Syā.): avasesā] न तो गंध है, "
        "न गंध का इंद्रिय-क्षेत्र।",
}
# a parenthetical note glued to the end of a sentence (no full stop before it in the Pāli)
TAIL_NOTES = {
    " (saṃkhittaṃ yassakasadisaṃ [yassakampi sadisaṃ (sī.), yassekasadisaṃ (syā.)] ).":
        f" ({SAMKHITTAM}, व्यक्ति वाले भाग के समान [पाठभेद (Sī.): yassakampi sadisaṃ; "
        f"वर्तनी-भेद (Syā.): yassekasadisaṃ])।",
}


# ------------------------------------------------------------------------------------------------
# Helpers
# ------------------------------------------------------------------------------------------------
def strip_ti(w, vocab):
    if w in vocab:
        return w
    for c in (w[:-2], w[:-3] + "ṃ", w[:-3] + "i", w[:-3] + "a", w[:-3] + "ā", w[:-3] + "u"):
        if c in vocab:
            return c
    raise ValueError(f"-ti: {w}")


def term(tok):
    """'na cakkhu' / 'nāyatanā' / 'cakkhāyatananti' -> (key, neg)."""
    neg = False
    if tok.startswith("na "):
        neg, tok = True, tok[3:]
    elif tok.startswith("nāyatan"):
        neg, tok = True, "ā" + tok[2:]
    return strip_ti(tok, WORDS), neg


def lab_prefix(lab):
    return (S.LABELS[f"({lab})"] + " ") if lab else ""


_QTERM = r"((?:na )?\S+)"


def pannatti_q(s):
    """(Ka) X Y? / na X na Y? (label optional, sentence capitalised when unlabelled)."""
    if not s.startswith("("):
        s = s[0].lower() + s[1:]
    m = re.fullmatch(rf"(?:\((Ka|Kha)\) )?{_QTERM} {_QTERM}\?", s)
    if not m:
        return None
    lab, a, b = m.groups()
    try:
        (ak, an), (bk, bn) = term(a), term(b)
    except ValueError:
        return None
    if an != bn:
        raise ValueError(f"mixed polarity: {s}")
    (ad, anum), (bd, bnum) = WORDS[ak], WORDS[bk]
    n2 = "pl" if "pl" in (anum, bnum) else "sg"
    if an:
        return f"{lab_prefix(lab)}जो {ad} नहीं {S.COP[anum]}, क्या {S.PRON[anum]} {bd} नहीं {S.COP[n2]}?"
    return f"{lab_prefix(lab)}क्या {ad}, {bd} {S.COP[n2]}?"


def _subject(a):
    a0 = a[0].lower() + a[1:]
    if a0 in SPECIAL:
        return SPECIAL[a0]
    m = re.fullmatch(r"(\S+) ṭhapetvā (avaseso|avasesaṃ|avasesā)( āyatanā)?", a0)
    if m:
        x = OBL[ACC[m.group(1)]]
        return S.CHHODKAR.format(x=x) + (f" {IK}" if m.group(3) else ""), AVASESA_NUM[m.group(2)]
    raise ValueError(f"subject: {a}")


def _acc_ca(w):
    w = w[0].lower() + w[1:]
    for suf in ("ñceva", "ñca"):
        if w.endswith(suf):
            return ACC[w[: -len(suf)] + "ṃ"]
    raise ValueError(f"ca-form: {w}")


def pannatti_a(s):
    """Answers of the niddesa (sentence without its final full stop)."""
    m = re.fullmatch(r"(.+?) (\S+), na (\S+)", s)                     # A B, na C
    if m and m.group(2) in WORDS and m.group(3) in WORDS:
        a, n = _subject(m.group(1))
        return f"{a}, {WORDS[m.group(2)][0]} {S.COP[n]}, पर {WORDS[m.group(3)][0]} नहीं {S.COP[n]}।"
    m = re.fullmatch(r"(.+?) na (\S+), (\S+)", s)                     # A na C, B
    if m and m.group(2) in WORDS and m.group(3) in WORDS:
        a, n = _subject(m.group(1))
        return f"{a}, {WORDS[m.group(2)][0]} नहीं {S.COP[n]}, पर {WORDS[m.group(3)][0]} {S.COP[n]}।"
    m = re.fullmatch(r"(\S+) (\S+?)(ñceva| ceva) (\S+)ñca", s)          # C B ceva C ca
    if m:
        c = m.group(1)[0].lower() + m.group(1)[1:]
        b = m.group(2) if m.group(3) == " ceva" else _acc_ca(m.group(2) + "ñceva")
        if c in WORDS and _acc_ca(m.group(4) + "ñca") == c and b in WORDS:
            n = "pl" if "pl" in (WORDS[b][1], WORDS[c][1]) else "sg"
            return f"{WORDS[c][0]}, {WORDS[b][0]} भी {S.COP[n]} और {WORDS[c][0]} भी।"
    m = re.fullmatch(r"(\S+ñca) (\S+ñca) ṭhapetvā (avasesaṃ|avasesā) na ceva (\S+) na ca (\S+)", s)
    if m:
        b, c = _acc_ca(m.group(1)), _acc_ca(m.group(2))
        n = AVASESA_NUM[m.group(3)]
        return (f"{OBL[b]} और {OBL[c]} को छोड़कर {S.AVASESA} न तो {WORDS[m.group(4)][0]} {S.COP[n]}, "
                f"न {WORDS[m.group(5)][0]}।")
    m = re.fullmatch(r"[Aa]vasesā āyatanā na (\S+)", s)                # Avasesā āyatanā na C
    if m and m.group(1) in WORDS:
        return f"{S.AVASESA} {IK}, {WORDS[m.group(1)][0]} नहीं हैं।"
    return None


# ---------------- Pavattivāra ----------------
def _place_noun(tok):
    key, _ = S.PLACE_FORMS[tok]
    return S.PLACE_NOUN[key]


def who(s):
    s = s[0].lower() + s[1:]
    if s == "itaresaṃ":
        return S.ITARESAM_ALONE
    ye_chunks = {}

    def _ye(mm):
        p1, p2 = mm.group(2), mm.group(3)
        if p2:
            txt = YE_TWO.format(p1=_place_noun(p1), p2=_place_noun(p2))
        else:
            txt = S.YE_PARINIBBAYISSANTI.format(place=_place_noun(p1))
        tok = f"§{len(ye_chunks)}"
        ye_chunks[tok] = txt
        return tok
    s = re.sub(r"\bye( ca)? (\S+)(?: (\S+))? upapajjitvā parinibbāyissanti", _ye, s)
    toks = s.split(" ")
    chunks, pre, mods, places, i = [], [], [], [], 0

    def flush(core):
        nonlocal pre, mods, places
        parts = pre + ([" और ".join(mods)] if mods else []) + [core]
        chunks.append(" ".join(parts))
        pre, mods, places = [], [], []

    while i < len(toks):
        w = toks[i]
        if w in ye_chunks:
            if pre or mods or places:
                raise ValueError(f"who: dangling before ye-clause: {s}")
            chunks.append(ye_chunks[w])
        elif w == "sabbesaṃ":
            pre.append(S.SABBESAM)
        elif w == "itaresaṃ":
            pre.append(S.ITARESAM)
        elif w in MODS:
            mods.append(MODS[w])
        elif w in S.PLACE_FORMS:
            places.append(S.PLACE_FORMS[w])
        elif w == "catuvokārānaṃ" and i + 1 < len(toks) and toks[i + 1] == "pañcavokārānaṃ" and not places:
            flush(CATUPANCA_BEINGS)
            i += 1
        elif w in S.BEINGS and not places:
            flush(S.BEINGS[w])
        elif w in S.PARTICIPLES:
            if places:
                keys = [k for k, _ in places]
                case = places[0][1]
                key = "catupañcavokāra" if keys == ["catuvokāra", "pañcavokāra"] else keys[0]
                if len(keys) > 1 and key != "catupañcavokāra":
                    raise ValueError(f"who: several places: {s}")
                flush(f"{S.PLACE_NOUN[key]} {S.CASE_POST[case]} {S.PARTICIPLES[w]}")
            else:
                flush(S.PARTICIPLES[w])
        else:
            raise ValueError(f"who: unknown token {w!r} in {s!r}")
        i += 1
    if pre or mods or places:
        raise ValueError(f"who: dangling tokens in {s!r}")
    if len(chunks) == 1:
        return chunks[0]
    return S.JOIN.join(chunks[:-1]) + S.JOIN_LAST + chunks[-1]


_T = r"(tesaṃ tattha|tesaṃ|tattha)"
_VB = r"((?:na )?\S+)"


def pavatti_a(s):
    m = re.fullmatch(rf"(.+?) {_T} (\S+) {_VB}, no ca {_T} (\S+) {_VB}", s)
    if m:
        wh, t, k1, v1, _, k2, v2 = m.groups()
        (k1h, g1), (k2h, g2) = PROC[k1], PROC[k2]
        v1h, v2h = S.verb_hi(v1, g1), S.verb_hi(v2, g2, flip=True)
        if t == "tattha":
            return S.BUT_PLACE.format(place=S.place(wh), k1=k1h, v1=v1h, k2=k2h, v2=v2h)
        fr = S.BUT_BEINGS_T if t == "tesaṃ tattha" else S.BUT_BEINGS
        return fr.format(who=who(wh), k1=k1h, v1=v1h, k2=k2h, v2=v2h)
    m = re.fullmatch(rf"(.+?) {_T} (\S+?)ñca {_VB} (\S+?)ñca {_VB}", s)
    if m:
        wh, t, k1, v1, k2, v2 = m.groups()
        (k1h, g1), (k2h, g2) = PROC[k1 + "ṃ"], PROC[k2 + "ṃ"]
        v1h, v2h = S.verb_hi(v1, g1), S.verb_hi(v2, g2)
        if t == "tattha":
            return S.BOTH_PLACE.format(place=S.place(wh), k1=k1h, v1=v1h, k2=k2h, v2=v2h)
        fr = S.BOTH_BEINGS_T if t == "tesaṃ tattha" else S.BOTH_BEINGS
        return fr.format(who=who(wh), k1=k1h, v1=v1h, k2=k2h, v2=v2h)
    return None


_REL = r"(yassa vā pana yattha|yassa yattha|yassa vā pana|yassa|yattha vā pana|yattha)"
_COR = r"(tassa tattha|tassa|tattha)"
REL_HI = {"yassa": "जिस व्यक्ति में", "yattha": "जिस स्थान पर", "yassa yattha": "जिस व्यक्ति में जिस स्थान पर"}
COR_HI = {"tassa": "उसमें", "tattha": "वहाँ", "tassa tattha": "उसमें वहाँ"}


def _clause(c, last):
    toks = c.split(" ")
    if len(toks) >= 2 and toks[-2] == "na":
        verb, subj = "na " + toks[-1], toks[:-2]
    else:
        verb, subj = toks[-1], toks[:-1]
    if last:
        neg = verb.startswith("na ")
        verb = ("na " if neg else "") + strip_ti(verb[3:] if neg else verb, S._VERB_TI)
    subs = " ".join(subj).replace("…pe…", "…").split("… ")
    keys = [x.rstrip("…") for x in subs]
    for k in keys:
        if k not in PROC:
            raise ValueError(f"process subject {k!r} in {c!r}")
    return keys, verb


def pavatti_q(s):
    m = re.fullmatch(rf"(?:\((Ka|Kha)\) )?{_REL} (.+?) {_COR} (.+)\?", s[0].lower() + s[1:] if not s.startswith("(") else s)
    if not m:
        return None
    lab, rel, c1, cor, c2 = m.groups()
    k1, v1 = _clause(c1, False)
    k2, v2 = _clause(c2, True)
    vp = " vā pana" in rel
    rel_hi = ("और " if vp else "") + REL_HI[rel.replace(" vā pana", "")]
    k1h = "… ".join(PROC[k][0] for k in k1)
    k2h = "… ".join(PROC[k][0] for k in k2)
    return (f"{lab_prefix(lab)}{rel_hi} {k1h} {S.verb_hi(v1, 'm')}, क्या {COR_HI[cor]} {k2h} "
            f"{S.verb_hi(v2, 'm')}?")


def abbreviated(s):
    m = re.fullmatch(r"(Yassa yattha|Yattha|Yassa) (\S+) ((?:na )?\S+)", s)
    if m and m.group(2) in PROC:
        return f"{S.ABBR_Q[m.group(1).lower()]} {PROC[m.group(2)][0]} {S.verb_hi(m.group(3), 'm')}"
    return None


def label_note(s):
    m = re.fullmatch(r"\((\S+?)āyatanamūlakaṃ\)(\.?)", s)
    if m:
        x = AYAT_OBL[m.group(1).lower() + "āyatanaṃ"]
        return MULAKA.format(x=x) + ("।" if m.group(2) else "")
    if s == "(Cakkaṃ bandhitabbaṃ)":
        return CAKKAM
    if s == "(Saṃkhittaṃ).":
        return f"({SAMKHITTAM})।"
    return None


# ------------------------------------------------------------------------------------------------
# Sentence / line driver
# ------------------------------------------------------------------------------------------------
_SPLIT = re.compile(r"(?<=[.?]) (?=[A-ZĀĪŪṬḌṆÑṄ(])")


def sentence(s):
    if s in FIXED_SENTENCES:
        return FIXED_SENTENCES[s]
    if s in S.CLOSINGS:
        return S.CLOSINGS[s]
    r = label_note(s)
    if r:
        return r
    for tail, hi in TAIL_NOTES.items():
        if s.endswith(tail):
            return sentence(s[: -len(tail)] + ".")[:-1] + hi
    # abbreviation marks
    for pe in ("…pe….", "…Pe…."):
        if s.endswith(pe):
            core = s[: -len(pe)]
            if core.endswith((".", "?")):          # 'Āmantā.…Pe….'
                return sentence(core) + "…"
            r = abbreviated(core)
            if r:
                return r + "…।"
            return sentence(core + ".")[:-1] + "…।"
    for pe in ("…pe…", "…Pe…"):
        if s.endswith(pe):
            return sentence(s[: -len(pe)]) + "…"
    if s.endswith("…."):                          # '… na ca āyatanā….' (dots without pe)
        return sentence(s[:-2] + ".")[:-1] + "…।"
    if s.endswith("?"):
        r = pavatti_q(s) if re.match(r"(\((Ka|Kha)\) )?[Yy](assa|attha) ", s) else pannatti_q(s)
        if r:
            return r
    if s.endswith("."):
        core = s[:-1]
        for fn in (pannatti_a, pavatti_a):
            r = fn(core)
            if r:
                return r
        w = core[0].lower() + core[1:]
        if w in S.VERB_FORMS:
            return S.verb_hi(w, "m") + "।"
    raise ValueError(f"no formula for: {s}")


def translate_text_line(line):
    if line in FIXED_LINES:
        return FIXED_LINES[line]
    for a, b in SLIPS:
        line = line.replace(a, b)
    if line in FIXED_LINES:
        return FIXED_LINES[line]
    return " ".join(sentence(s) for s in _SPLIT.split(line))


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
        return f"{hashes} {S.HEADINGS[text.strip()]}{bid}"
    return translate_text_line(line.strip()) + bid


def translate_text(pali, overrides):
    out, prev_blank, errors = [], True, []
    for n, line in enumerate(pali.splitlines(), 1):
        if not line.strip():
            if not prev_blank:
                out.append("")
            prev_blank = True
            continue
        key = S.ID_RE.sub("", line).strip()
        try:
            if key in overrides:
                m = S.ID_RE.search(line)
                out.append(overrides[key] + (" " + m.group(1) if m else ""))
            else:
                out.append(translate_line(line))
        except (ValueError, KeyError) as e:
            errors.append(f"line {n}: {e!r}: {line[:120]}")
            out.append("@@ " + line)
        prev_blank = False
    while out and out[-1] == "":
        out.pop()
    return "\n".join(out) + "\n", errors


if __name__ == "__main__":
    from overrides_3_01_3_02 import OVERRIDES   # hand-translated irregular lines (same folder)
    total = 0
    for f in FILES:
        pali = (S.PALI_DIR / f).read_text(encoding="utf-8")
        hi, errs = translate_text(pali, OVERRIDES)
        (S.HI_DIR / f).write_text(hi, encoding="utf-8", newline="\n")
        print(f, "errors:", len(errs))
        for e in errs:
            print("  ", e)
        total += len(errs)
    sys.exit(1 if total else 0)
