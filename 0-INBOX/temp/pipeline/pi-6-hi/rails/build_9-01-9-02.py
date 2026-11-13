"""pi-6 Yamaka, Dhammayamaka 9-01 / 9-02: Pāli -> Hindi plain RAILS builder.

Imports build_rails_sample.py read-only (constants and helpers); adds the Dhammayamaka formulas
(paṇṇatti words kusalā / dhammā, feminine plural process verbs, moment and being chunks).
Every Pāli line must match a formula; an unknown line raises ValueError.

usage: python -I -X utf8 build_9-01-9-02.py [9-01-dhammayamaka.md 9-02-dhammayamaka.md]
"""
import re
import sys

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-hi\rails")
import build_rails_sample as S  # noqa: E402  (read-only)

# ------------------------------------------------------------------------------------------------
# Headings and closings (additions to S.HEADINGS / S.CLOSINGS)
# ------------------------------------------------------------------------------------------------
HEADINGS = dict(S.HEADINGS)
HEADINGS["Pavattivāro"] = "प्रक्रिया का खंड"                 # NEW (bare heading; cf. «प्रक्रिया का खंड 1. …»)
CLOSINGS = dict(S.CLOSINGS)
CLOSINGS["Uppādavāro."] = "उत्पन्न होने का खंड।"            # NEW (cf. Nirodhavāro. = समाप्त होने का खंड।)

# ------------------------------------------------------------------------------------------------
# Paṇṇattivāra: kusalā / akusalā / abyākatā (bare) and … dhammā; all plural (copula «हैं», «वे»)
# ------------------------------------------------------------------------------------------------
T_BARE = {"kusalā": "हितकर", "akusalā": "हानिकर", "abyākatā": "नैतिक रूप से अनिर्धारित"}
DW = {"dhammā": ("परिघटनाएँ", "परिघटनाओं")}
for _k, _v in T_BARE.items():
    DW[_k] = (_v, _v)
    DW[_k + " dhammā"] = (S.MULA_T_DHAMMA[_k[:-1] + "a"], _v + " परिघटनाओं")
# neuter singular before ṭhapetvā (Kusalaṃ / Kusalañca)
T_NEUT = {"kusalaṃ": "kusalā", "akusalaṃ": "akusalā", "abyākataṃ": "abyākatā"}


def _strip_ti(w):
    if w.endswith("āti"):
        return w[:-2]
    return w


def _ab(tokens):
    """Split the term tokens of a paṇṇatti question into (A, B)."""
    if len(tokens) == 2:
        return tokens[0], tokens[1]
    if len(tokens) == 3:
        if tokens[2] == "dhammā":
            return tokens[0], tokens[1] + " dhammā"
        if tokens[1] == "dhammā":
            return tokens[0] + " dhammā", tokens[2]
    raise ValueError(f"paṇṇatti tokens: {tokens}")


def pannatti_question(s):
    m = re.fullmatch(rf"{S._LAB} (.+)\?", s)
    if not m:
        return None
    body = m.group(2)
    words = body.split(" ")
    words[-1] = _strip_ti(words[-1])
    if any(w not in ("na", "dhammā") and w not in T_BARE for w in words):
        return None
    lab = S.LABELS[f"({m.group(1)})"]
    if words[0] == "na":
        # na A na B
        j = words.index("na", 1)
        a, b = " ".join(words[1:j]), " ".join(words[j + 1:])
        if a not in DW or b not in DW:
            raise ValueError(f"paṇṇatti neg: {s}")
        return f"{lab} जो {DW[a][0]} नहीं हैं, क्या वे {DW[b][0]} नहीं हैं?"
    a, b = _ab(words)
    return f"{lab} क्या {DW[a][0]}, {DW[b][0]} हैं?"


def pannatti_sentence(s):
    m = re.fullmatch(r"(Kusalā|Akusalā|Abyākatā) dhammā dhammā ceva (\S+) dhammā ca\.", s)
    if m and m.group(1).lower() == m.group(2):
        c = DW[m.group(2) + " dhammā"][0]
        return f"{c}, परिघटनाएँ भी हैं और {c} भी।"
    m = re.fullmatch(r"Avasesā dhammā na (\S+) dhammā\.", s)
    if m:
        return f"{S.AVASESA} परिघटनाएँ, {DW[m.group(1) + ' dhammā'][0]} नहीं हैं।"
    m = re.fullmatch(r"(\S+) ṭhapetvā avasesā dhammā na (\S+), dhammā\.", s)
    if m and T_NEUT.get(m.group(1).lower()) == m.group(2):
        t = DW[m.group(2)][1]
        return f"{S.CHHODKAR.format(x=t)} परिघटनाएँ, {DW[m.group(2)][0]} नहीं हैं, पर परिघटनाएँ हैं।"
    m = re.fullmatch(r"(\S+)ñca dhamme ca ṭhapetvā avasesā na ceva (\S+) na ca dhammā\.", s)
    if m and T_NEUT.get(m.group(1).lower() + "ṃ") == m.group(2):
        t = DW[m.group(2)][1]
        return f"{t} और परिघटनाओं को छोड़कर {S.AVASESA} न तो {DW[m.group(2)][0]} हैं, न परिघटनाएँ।"
    return None


# ------------------------------------------------------------------------------------------------
# Pavattivāra: subjects «… परिघटनाएँ» (feminine plural) -> NEW verb column
# ------------------------------------------------------------------------------------------------
VERBS_FPL = {
    "uppajjati": ("उत्पन्न होती हैं", "उत्पन्न नहीं होतीं"),
    "uppajjittha": ("उत्पन्न हुई थीं", "उत्पन्न नहीं हुई थीं"),
    "uppajjissati": ("उत्पन्न होंगी", "उत्पन्न नहीं होंगी"),
    "nirujjhati": ("समाप्त होती हैं", "समाप्त नहीं होतीं"),
    "nirujjhittha": ("समाप्त हुई थीं", "समाप्त नहीं हुई थीं"),
    "nirujjhissati": ("समाप्त होंगी", "समाप्त नहीं होंगी"),
}
_VT = set(S.VERB_FORMS)


def vfpl(tok, flip=False):
    neg = tok.startswith("na ")
    w = tok[3:] if neg else tok
    w = S.strip_ti(w, _VT)
    stem, n = S.VERB_FORMS[w]
    neg = neg or n
    pos_s, neg_s = VERBS_FPL[stem]
    return neg_s if (neg != flip) else pos_s


def subj(t):
    if t not in T_BARE:
        raise ValueError(f"subject: {t}")
    return DW[t + " dhammā"][0]


_V = r"((?:na )?\S+)"


def pavatti_question(s):
    m = re.fullmatch(rf"{S._LAB} {S._REL} (\S+) dhammā {_V} {S._COR} (\S+) dhammā {_V}\?", s)
    if not m:
        return None
    lab, rel, k1, v1, cor, k2, v2 = m.groups()
    rel_hi, cor_hi = S.REL_FRAMES[(rel, cor)]
    return S.Q_FRAME.format(label=S.LABELS[f"({lab})"], rel=rel_hi, k1=subj(k1), v1=vfpl(v1),
                            corr=cor_hi, k2=subj(k2), v2=vfpl(v2))


def abbreviated_question(s):
    """'Yattha X dhammā V1 tattha Y dhammā V2ti?…Pe….' -> «जिस स्थान पर X V1, क्या वहाँ Y V2?…» (NEW)"""
    m = re.fullmatch(rf"Yattha (\S+) dhammā {_V} tattha (\S+) dhammā {_V}\?…Pe…\.", s)
    if not m:
        return None
    k1, v1, k2, v2 = m.groups()
    return f"जिस स्थान पर {subj(k1)} {vfpl(v1)}, क्या वहाँ {subj(k2)} {vfpl(v2)}?…"


# ---- beings / moments --------------------------------------------------------------------------
MIND = {  # genitive heads of the moment phrases (termbase)
    "cittassa": "मन",
    "kusalavippayuttacittassa": "हितकर से अलग मन",
    "akusalavippayuttacittassa": "हानिकर से अलग मन",
    "kusalavippayuttaakusalavippayuttacittassa": "हितकर से अलग और हानिकर से अलग मन",
    "akusalavippayuttakusalavippayuttacittassa": "हानिकर से अलग और हितकर से अलग मन",
    "kusalānaṃ": "हितकर परिघटनाओं",
    "akusalānaṃ": "हानिकर परिघटनाओं",
    "kusalākusalānaṃ": "हितकर और हानिकर परिघटनाओं",
    "aggamaggassa": "सर्वोच्च मार्ग",
    "pacchimacittassa": "अंतिम मन",
}
KHANA = {"uppādakkhaṇe": "के उत्पन्न होने के क्षण में", "bhaṅgakkhaṇe": "के भंग होने के क्षण में"}
PLACE_LOC = {"arūpe": "अभौतिक लोक में", "pañcavokāre": "पाँच समूहों वाले अस्तित्व में"}
ANANTARA = "जो इस मन के ठीक बाद सर्वोच्च मार्ग प्राप्त करेंगे, उनमें"     # yassa cittassa anantarā aggamaggaṃ paṭilabhissanti (B6)
ANANTARA_TASSA = "जिस मन के ठीक बाद लोग सर्वोच्च मार्ग प्राप्त करेंगे, उस मन {k}"   # … tassa cittassa <khaṇe>
DUTIYE = "शुद्ध निवास लोक के प्राणियों में दूसरे {a}मन के चलते समय"           # Suddhāvāsānaṃ dutiye [akusale] citte vattamāne (B4)
PERSONS = {
    "nirodhasamāpannānaṃ": "समाप्ति की ध्यान-अवस्था में लीन लोगों में",
    "asaññasattānaṃ": S.BEINGS["asaññasattānaṃ"],
    "aggamaggasamaṅgīnaṃ": "सर्वोच्च मार्ग से युक्त लोगों में",
    "arahantānaṃ": "अर्हतों में",
    "pacchimacittasamaṅgīnaṃ": "अंतिम मन से युक्त लोगों में",
}
CATUPANCA_BEINGS = "चार या पाँच समूहों वाले अस्तित्व के प्राणियों में"   # catuvokārānaṃ pañcavokārānaṃ (I3)

_MIND_RE = "|".join(sorted(map(re.escape, MIND), key=len, reverse=True))
CHUNK_RES = [
    (re.compile(r"sabbesaṃ upapajjantānaṃ"), lambda m: f"{S.SABBESAM} {S.PARTICIPLES['upapajjantānaṃ']}"),
    (re.compile(r"sabbesaṃ cavantānaṃ"), lambda m: f"{S.SABBESAM} {S.PARTICIPLES['cavantānaṃ']}"),
    (re.compile(r"sabbesaṃ cittassa (uppādakkhaṇe|bhaṅgakkhaṇe)"),
     lambda m: f"{S.SABBESAM} के मन {KHANA[m.group(1)]}"),
    (re.compile(r"suddhāvāsaṃ upapajjantānaṃ"),
     lambda m: f"{S.PLACE_NOUN['suddhāvāsa']} में {S.PARTICIPLES['upapajjantānaṃ']}"),
    (re.compile(r"suddhāvāsānaṃ dutiye (akusale )?citte vattamāne"),
     lambda m: DUTIYE.format(a="हानिकर " if m.group(1) else "")),
    (re.compile(r"itaresaṃ catuvokārānaṃ pañcavokārānaṃ"), lambda m: f"{S.ITARESAM} {CATUPANCA_BEINGS}"),
    (re.compile(r"yassa cittassa anantarā aggamaggaṃ paṭilabhissanti tassa cittassa (uppādakkhaṇe|bhaṅgakkhaṇe)"),
     lambda m: ANANTARA_TASSA.format(k=KHANA[m.group(1)])),
    (re.compile(r"yassa cittassa anantarā aggamaggaṃ paṭilabhissanti"), lambda m: ANANTARA),
    (re.compile(rf"(itaresaṃ |pavatte |arūpe |pañcavokāre )?({_MIND_RE}) (uppādakkhaṇe|bhaṅgakkhaṇe)"),
     lambda m: ({"itaresaṃ ": S.ITARESAM_ALONE + " ", "pavatte ": "जीवन के दौरान "}.get(m.group(1) or "")
                or (PLACE_LOC[m.group(1).strip()] + " " if m.group(1) else ""))
     + f"{MIND[m.group(2)]} {KHANA[m.group(3)]}"),
    (re.compile("(" + "|".join(PERSONS) + ")"), lambda m: PERSONS[m.group(1)]),
]


def who(s):
    s = s[0].lower() + s[1:]
    if s == "itaresaṃ":
        return S.ITARESAM_ALONE
    chunks, rest = [], s
    while rest:
        for rx, fn in CHUNK_RES:
            m = rx.match(rest)
            if m and (m.end() == len(rest) or rest[m.end()] == " "):
                chunks.append(fn(m))
                rest = rest[m.end():].lstrip(" ")
                break
        else:
            raise ValueError(f"who: cannot parse {rest!r} in {s!r}")
    if len(chunks) == 1:
        return chunks[0]
    return S.JOIN.join(chunks[:-1]) + S.JOIN_LAST + chunks[-1]


_T3 = r"(tesaṃ tattha|tesaṃ|tattha)"


def pavatti_sentence(s):
    m = re.fullmatch(rf"(.+?) {_T3} (\S+) dhammā {_V}, no ca (?:tesaṃ tattha|tesaṃ|tattha) (\S+) dhammā {_V}\.", s)
    if m:
        wh, t, k1, v1, k2, v2 = m.groups()
        a = dict(k1=subj(k1), v1=vfpl(v1), k2=subj(k2), v2=vfpl(v2, flip=True))
        if t == "tattha":
            return S.BUT_PLACE.format(place=S.place(wh), **a)
        return (S.BUT_BEINGS_T if t == "tesaṃ tattha" else S.BUT_BEINGS).format(who=who(wh), **a)
    m = re.fullmatch(rf"(.+?) {_T3} (\S+) ca dhammā {_V} (\S+) ca dhammā {_V}\.", s)
    if m:
        wh, t, k1, v1, k2, v2 = m.groups()
        a = dict(k1=subj(k1), v1=vfpl(v1), k2=subj(k2), v2=vfpl(v2))
        if t == "tattha":
            return S.BOTH_PLACE.format(place=S.place(wh), **a)
        return (S.BOTH_BEINGS_T if t == "tesaṃ tattha" else S.BOTH_BEINGS).format(who=who(wh), **a)
    return None


def short_answer(s):
    if s in ("Āmantā.", "No.", "Natthi."):
        return CLOSINGS[s]
    w = s[:-1]
    w = w[0].lower() + w[1:]
    if w in S.VERB_FORMS:
        return vfpl(w) + "।"
    return None


# ------------------------------------------------------------------------------------------------
def translate_sentence(s):
    if s in CLOSINGS:
        return CLOSINGS[s]
    for fn in (abbreviated_question, pavatti_question, pannatti_question,
               pannatti_sentence, pavatti_sentence, short_answer):
        r = fn(s)
        if r:
            return r
    raise ValueError(f"no formula for: {s}")


def translate_line(line):
    if not line.strip():
        return ""
    bid = ""
    m = S.ID_RE.search(line)
    if m:
        bid = " " + m.group(1)
        line = line[: m.start()]
    line = line.strip()
    if line.startswith("#"):
        hashes, text = line.split(" ", 1)
        num = ""
        mm = re.fullmatch(r"(\d+) (.+)", text)
        if mm and mm.group(2) in HEADINGS:
            num, text = mm.group(1) + " ", mm.group(2)
        if text not in HEADINGS:
            raise ValueError(f"unknown heading: {text}")
        return f"{hashes} {num}{HEADINGS[text]}{bid}"
    if line in HEADINGS:  # heading text standing as an ordinary line ("(Kha) niddeso ^6-9-16")
        return HEADINGS[line] + bid
    out = [translate_sentence(x) for x in S._split_sentences(line)]
    return " ".join(out) + bid


def translate_text(pali_text):
    out, prev_blank = [], True
    for line in pali_text.splitlines():
        if not line.strip():
            if not prev_blank:
                out.append("")
            prev_blank = True
            continue
        out.append(translate_line(line))
        prev_blank = False
    while out and out[-1] == "":
        out.pop()
    return "\n".join(out) + "\n"


def main(files):
    for f in files:
        pali = (S.PALI_DIR / f).read_text(encoding="utf-8")
        (S.HI_DIR / f).write_text(translate_text(pali), encoding="utf-8", newline="\n")
        print("built", f)


if __name__ == "__main__":
    main(sys.argv[1:] or ["9-01-dhammayamaka.md", "9-02-dhammayamaka.md"])
