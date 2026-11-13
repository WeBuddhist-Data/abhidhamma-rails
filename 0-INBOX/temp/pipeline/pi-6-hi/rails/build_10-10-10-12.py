"""pi-6 Indriyayamaka 10-10, 10-11, 10-12: Pāli -> Hindi plain RAILS.

Imports the approved sample constants read-only (build_rails_sample as S) and adds the indriya tables
and the being/moment chunks of these files. Every line must match a formula; unknown -> ValueError.
usage: python -I -X utf8 build_10-10-10-12.py [--dry]
"""
import re
import sys

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-hi\rails")
import build_rails_sample as S  # noqa: E402  (read-only)

FILES = ["10-10-indriyayamaka.md", "10-11-indriyayamaka.md", "10-12-indriyayamaka.md"]

# ---------------------------------------------------------------- indriya names (termbase), all feminine
IND = {
    "cakkhundriy": "आँख की क्षमता",
    "sotindriy": "कान की क्षमता",
    "ghānindriy": "नाक की क्षमता",
    "itthindriy": "स्त्रीत्व की क्षमता",
    "purisindriy": "पुरुषत्व की क्षमता",
    "jīvitindriy": "जीवन-क्षमता",
    "somanassindriy": "प्रसन्नता की क्षमता",
    "upekkhindriy": "समभाव की क्षमता",
    "saddhindriy": "श्रद्धा की क्षमता",
    "paññindriy": "प्रज्ञा की क्षमता",
    "manindriy": "मन की क्षमता",
}
_IND = "(" + "|".join(IND) + ")"
MULAKA = {k[:1].upper() + k[1:] + "amūlakaṃ": f"({v} पर आधारित)" for k, v in IND.items()}  # (Cakkhundriyamūlakaṃ)

# ---------------------------------------------------------------- source slips (normalised before translating)
SLIPS = [
    # 10-10 ^6-10-393: full stop missing between the two answer sentences
    ("no ca tesaṃ manindriyaṃ na uppajjissati pacchimacittassa bhaṅgakkhaṇe",
     "no ca tesaṃ manindriyaṃ na uppajjissati. Pacchimacittassa bhaṅgakkhaṇe"),
    # 10-11 ^6-10-398: uppajjantānaṃ for upapajjantānaṃ (termbase: variant spelling)
    ("Pacchimabhavikānaṃ purisānaṃ uppajjantānaṃ", "Pacchimabhavikānaṃ purisānaṃ upapajjantānaṃ"),
]

# ---------------------------------------------------------------- being / moment chunks (new for these files)
MOD = {  # modifier of a «जन्म लेने वालों में» chunk, before the place (harmonise I1)
    "acakkhukānaṃ": "आँख से रहित",
    "aghānakānaṃ": "नाक से रहित",
    "saghānakānaṃ": "नाक वाले",
    "na itthīnaṃ": "स्त्रियों से भिन्न",    # as notes-10-01-10-02 (termbase nakāmadhātu- «से भिन्न»)
    "na purisānaṃ": "पुरुषों से भिन्न",
}
YE_SUBJ = {None: "जो", "sacakkhukā": "जो आँख वाले", "saghānakā": "जो नाक वाले",
           "purisā": "जो पुरुष", "itthiyo": "जो स्त्रियाँ"}
YE_MANNER = {"upekkhāya": "समभाव के साथ", "somanassena": "प्रसन्नता के साथ"}
YE_VERB = {"m": "जन्म लेकर पूर्ण निर्वाण पाएँगे", "f": "जन्म लेकर पूर्ण निर्वाण पाएँगी"}
BHAVENA = {"m": "इसी लिंग में कुछ जन्म बिताकर पूर्ण निर्वाण पाएँगे", "f": "इसी लिंग में कुछ जन्म बिताकर पूर्ण निर्वाण पाएँगी"}
YE_TAIL = {  # resumptive of a ye-clause
    None: ", उनमें",
    "cavantānaṃ": ", उनमें से मरने वालों में",
    "upapajjantānaṃ": ", उनमें से जन्म लेने वालों में",
    "cavantīnaṃ": ", उनमें से मरने वाली स्त्रियों में",
    "upapajjantīnaṃ": ", उनमें से जन्म लेने वाली स्त्रियों में",
}
MIND_X = {"somanassa": "प्रसन्नता", "upekkhā": "समभाव", "saddhā": "श्रद्धा", "ñāṇa": "ज्ञान"}
MOMENT = {"bhaṅgakkhaṇe": "भंग होने के क्षण में", "uppādakkhaṇe": "उत्पन्न होने के क्षण में"}
ANANTARA_REL = "जिनमें इस मन के ठीक बाद {y} उत्पन्न होगा"                 # B6 (… , उनमें)
ANANTARA_TASSA = "जिस मन के ठीक बाद {y} उत्पन्न होगा, उस मन के {moment}"   # … tassa cittassa <moment>
DUTIYE = "शुद्ध निवास लोक के प्राणियों में दूसरे मन के चलते समय"            # B4
NIRODHA = "समाप्ति की ध्यान-अवस्था में लीन लोगों में"
CATUPANCA_BEINGS = "चार या पाँच समूहों वाले अस्तित्व के प्राणियों में"       # I3
PLACE_OR = " या "   # several places of one chunk


def _mind(prefix):
    """'' मन; pacchima अंतिम मन; Xsampayuttapacchima X से जुड़े अंतिम मन; Xvippayutta X से अलग मन (oblique)."""
    if prefix == "":
        return "मन"
    if prefix == "pacchima":
        return "अंतिम मन"
    m = re.fullmatch(r"(somanassa|upekkhā)sampayuttapacchima", prefix)
    if m:
        return f"{MIND_X[m.group(1)]} से जुड़े अंतिम मन"
    m = re.fullmatch(r"(somanassa|upekkhā|saddhā|ñāṇa)vippayutta", prefix)
    if m:
        return f"{MIND_X[m.group(1)]} से अलग मन"
    raise ValueError(f"mind prefix: {prefix}")


def _places(toks, case=None):
    keys = []
    for t in toks:
        k, c = S.PLACE_FORMS[t]
        if case and c != case:
            raise ValueError(f"place case {t} != {case}")
        keys.append(k)
    if keys == ["catuvokāra", "pañcavokāra"]:
        keys = ["catupañcavokāra"]
    return PLACE_OR.join(S.PLACE_NOUN[k] for k in keys)


_PL = r"(?:(?:" + "|".join(re.escape(p) for p in S.PLACE_FORMS) + r") )"


def who(s):
    s = s[0].lower() + s[1:]
    if s == "itaresaṃ":
        return S.ITARESAM_ALONE
    ph = {}   # placeholder -> (kind, text, tail)

    def put(kind, text, tail=None):
        tok = f"§{len(ph)}"
        ph[tok] = (kind, text, tail)
        return tok

    # ye / yā ca … upapajjitvā parinibbāyissanti [tesaṃ|tāsaṃ participle]
    def _ye(m):
        gen = "f" if m.group(1) == "yā" else "m"
        subj = YE_SUBJ[m.group(2)]
        parts = [subj]
        if m.group(3):
            parts.append(YE_MANNER[m.group(3)])
        if m.group(4):
            parts.append(_places(m.group(4).split(), "acc") + " में")
        parts.append(YE_VERB[gen])
        return put("ye", " ".join(parts), m.group(6))
    s = re.sub(r"(ye|yā) ca (?:(sacakkhukā|saghānakā|purisā|itthiyo) )?(?:(upekkhāya|somanassena) )?"
               r"((?:(?:rūpāvacaraṃ|arūpāvacaraṃ|arūpaṃ|kāmāvacaraṃ|pañcavokāraṃ) )*)upapajjitvā parinibbāyissanti"
               r"(?: (tesaṃ|tāsaṃ) (cavantānaṃ|upapajjantānaṃ|cavantīnaṃ|upapajjantīnaṃ))?", _ye, s)

    def _bhavena(m):
        gen = "f" if m.group(1) == "yā" else "m"
        return put("ye", f"{YE_SUBJ[m.group(2)]} {BHAVENA[gen]}", m.group(4))
    s = re.sub(r"(ye|yā) ca (purisā|itthiyo) eteneva bhāvena katici bhave dassetvā parinibbāyissanti"
               r"(?: (tesaṃ|tāsaṃ) (cavantānaṃ|upapajjantānaṃ|cavantīnaṃ|upapajjantīnaṃ))?", _bhavena, s)

    # yassa cittassa anantarā Y uppajjissati [tassa cittassa <moment>]
    def _anan(m):
        y = f"{MIND_X[m.group(1)]} से जुड़ा अंतिम मन"
        if m.group(2):
            return put("chunk", ANANTARA_TASSA.format(y=y, moment=MOMENT[m.group(2)]))
        return put("ye", ANANTARA_REL.format(y=y), None)
    s = re.sub(r"yassa cittassa anantarā (somanassa|upekkhā)sampayuttapacchimacittaṃ uppajjissati"
               r"(?: tassa cittassa (bhaṅgakkhaṇe|uppādakkhaṇe))?", _anan, s)

    # moments: [sabbesaṃ] [pavatte] <prefix>cittassa <moment>
    def _mom(m):
        pre = ("सभी के " if m.group(1) else "") + ("जीवन के दौरान " if m.group(2) else "")
        return put("chunk", f"{pre}{_mind(m.group(3))} के {MOMENT[m.group(4)]}")
    s = re.sub(r"(sabbesaṃ )?(pavatte )?(\S*?)cittassa (bhaṅgakkhaṇe|uppādakkhaṇe)", _mom, s)

    s = re.sub(r"(somanassa|upekkhā)sampayuttapacchimacittasamaṅgīnaṃ",
               lambda m: put("chunk", f"{MIND_X[m.group(1)]} से जुड़े अंतिम मन से युक्त लोगों में"), s)
    s = re.sub(r"pacchimacittasamaṅgīnaṃ", lambda m: put("chunk", "अंतिम मन से युक्त लोगों में"), s)
    s = s.replace("suddhāvāsānaṃ dutiye citte vattamāne", put("chunk", DUTIYE))
    s = s.replace("nirodhasamāpannānaṃ", put("chunk", NIRODHA))
    s = s.replace("catuvokārānaṃ pañcavokārānaṃ", put("being", CATUPANCA_BEINGS))

    # pacchimabhavikānaṃ [mod] [place] upapajjantānaṃ (B2)
    def _pacch(m):
        mid = m.group(1)
        if mid == "itthīnaṃ ":
            return put("chunk", "अंतिम जन्म लेने वाली स्त्रियों में")
        if mid == "purisānaṃ ":
            return put("chunk", "अंतिम जन्म लेने वाले पुरुषों में")
        if mid == "saghānakānaṃ ":
            return put("chunk", f"{MOD['saghānakānaṃ']} {S.PACCHIMA_UPAPAJJ}")
        if mid:
            return put("chunk", f"{_places(mid.split(), 'acc')} में {S.PACCHIMA_UPAPAJJ}")
        return put("chunk", S.PACCHIMA_UPAPAJJ)
    s = re.sub(rf"pacchimabhavikānaṃ (itthīnaṃ |purisānaṃ |saghānakānaṃ |{_PL})?(?:upapajjantānaṃ|upapajjantīnaṃ)",
               _pacch, s)

    # <mod> [place] upapajjantānaṃ (I1)
    def _mod(m):
        txt = MOD[m.group(1)]
        if m.group(2):
            txt += " " + _places(m.group(2).split(), "acc") + " में"
        return put("chunk", f"{txt} {S.PARTICIPLES['upapajjantānaṃ']}")
    s = re.sub(rf"(acakkhukānaṃ|aghānakānaṃ|saghānakānaṃ|na itthīnaṃ|na purisānaṃ) ({_PL}+)?upapajjantānaṃ", _mod, s)

    # remaining: sabbesaṃ / itaresaṃ, places + participle, genitive beings, placeholders
    toks = s.split(" ")
    items, pre, places = [], [], []   # items: (kind, text, tail)
    for w in toks:
        if w in ph:
            kind, text, tail = ph[w]
            if pre:
                text = " ".join(pre + [text])
                pre = []
            items.append((kind, text, tail))
        elif w == "sabbesaṃ":
            pre.append(S.SABBESAM)
        elif w == "itaresaṃ":
            pre.append(S.ITARESAM)
        elif w in S.PLACE_FORMS:
            places.append(w)
        elif w in S.BEINGS and not places:
            items.append(("chunk", " ".join(pre + [S.BEINGS[w]]), None))
            pre = []
        elif w in ("upapajjantānaṃ", "cavantānaṃ", "parinibbantānaṃ", "pacchimabhavikānaṃ"):
            if places:
                case = S.PLACE_FORMS[places[0]][1]
                txt = f"{_places(places, case)} {S.CASE_POST[case]} {S.PARTICIPLES[w]}"
            else:
                txt = S.PARTICIPLES[w]
            items.append(("chunk", " ".join(pre + [txt]), None))
            pre, places = [], []
        else:
            raise ValueError(f"who: unknown token {w!r} in {s!r}")
    if pre or places:
        raise ValueError(f"who: dangling tokens in {s!r}")
    out = []
    for i, (kind, text, tail) in enumerate(items):
        if kind == "ye":
            nxt = items[i + 1][0] if i + 1 < len(items) else None
            if tail is None and nxt == "ye":
                out.append(text)
            else:
                out.append(text + YE_TAIL[tail])
        else:
            out.append(text)
    if len(out) == 1:
        return out[0]
    return S.JOIN.join(out[:-1]) + S.JOIN_LAST + out[-1]


# ---------------------------------------------------------------- sentences
_TES = r"(tesaṃ tattha|tāsaṃ tattha|tesaṃ|tāsaṃ)"
_VB = r"((?:na )?uppajj[^\s,?.]+)"
BUT_RE = re.compile(rf"(.+?) {_TES} {_IND}aṃ {_VB},? no ca {_TES} {_IND}aṃ {_VB}\.")
BOTH_RE = re.compile(rf"(.+?) {_TES} {_IND}añca {_VB} {_IND}añca {_VB}\.")


def answer(s):
    m = BUT_RE.fullmatch(s)
    if m:
        wh, t1, k1, v1, _t2, k2, v2 = m.groups()
        frame = S.BUT_BEINGS_T if t1.endswith("tattha") else S.BUT_BEINGS
        return frame.format(who=who(wh), k1=IND[k1], v1=S.verb_hi(v1, "f"),
                            k2=IND[k2], v2=S.verb_hi(v2, "f", flip=True))
    m = BOTH_RE.fullmatch(s)
    if m:
        wh, t1, k1, v1, k2, v2 = m.groups()
        frame = S.BOTH_BEINGS_T if t1.endswith("tattha") else S.BOTH_BEINGS
        return frame.format(who=who(wh), k1=IND[k1], v1=S.verb_hi(v1, "f"), k2=IND[k2], v2=S.verb_hi(v2, "f"))
    return None


def _ind_list(k):
    """'saddhindriyaṃ…pe… paññindriyaṃ…pe… manindriyaṃ' -> «श्रद्धा की क्षमता… प्रज्ञा की क्षमता… मन की क्षमता»"""
    out = re.sub(rf"{_IND}aṃ", lambda m: IND[m.group(1)], k).replace("…pe…", "…")
    if re.search(r"[A-Za-zāīūṃñṅṭḍṇḷ]", out):
        raise ValueError(f"indriya list: {k}")
    return out


def _strip_ti(v):
    neg = v.startswith("na ")
    w = v[3:] if neg else v
    if w.endswith("īti"):
        w = w[:-3] + "i"
    elif w.endswith("āti"):
        w = w[:-3] + "a"
    if w not in S.VERB_FORMS:
        raise ValueError(f"verb: {v}")
    return ("na " if neg else "") + w


Q_RE = re.compile(rf"(?:\((Ka|Kha)\) )?{S._REL} (.+?) {_VB} {S._COR} (.+?) {_VB}\?(…Pe…\.)?")


def question(s):
    s2 = s[0].lower() + s[1:] if s[0] != "(" else s
    m = Q_RE.fullmatch(s2)
    if not m:
        return None
    lab, rel, k1, v1, cor, k2, v2, pe = m.groups()
    rel_hi, cor_hi = S.REL_FRAMES[(rel, cor)]
    head = (S.LABELS[f"({lab})"] + " ") if lab else ""
    rel_hi = rel_hi[0].upper() + rel_hi[1:]
    out = (f"{head}{rel_hi} {_ind_list(k1)} {S.verb_hi(v1, 'f')}, क्या {cor_hi} {_ind_list(k2)} "
           f"{S.verb_hi(_strip_ti(v2), 'f')}?")
    return out + ("…" if pe else "")


def short(s):
    if s in ("Āmantā.", "Natthi.", "No."):
        return S.CLOSINGS[s]
    if s in ("Uppajjittha.", "Uppajjissati.", "Uppajjati."):
        return S.verb_hi(s[:-1].lower(), "f") + "।"
    if s == "Pavattivāro niṭṭhito.":
        return S.CLOSINGS[s]
    m = re.fullmatch(r"(\(\S+mūlakaṃ\))(…pe…\.)?", s)
    if m:
        return MULAKA[m.group(1)[1:-1]] + ("…।" if m.group(2) else "")
    return None


def translate_sentence(s):
    for fn in (question, answer, short):
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
        return f"{hashes} {S.HEADINGS[text]}{bid}"
    for a, b in SLIPS:
        line = line.replace(a, b)
    return " ".join(translate_sentence(x) for x in S._split_sentences(line)) + bid


def translate_text(txt):
    out, prev_blank = [], True
    for line in txt.splitlines():
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


def main():
    dry = "--dry" in sys.argv
    for f in FILES:
        hi = translate_text((S.PALI_DIR / f).read_text(encoding="utf-8"))
        if not dry:
            (S.HI_DIR / f).write_text(hi, encoding="utf-8", newline="\n")
        print(f, "ok", len(hi.splitlines()), "lines", "(dry)" if dry else "")


if __name__ == "__main__":
    main()
