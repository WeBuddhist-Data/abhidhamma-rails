"""pi-6 Indriyayamaka 10-07, 10-08, 10-09: Pāli -> Hindi plain RAILS.

Imports build_rails_sample.py read-only (frames, verbs, headings, places) and adds the faculty names and the
being/moment chains of these three files. Every unknown token raises ValueError.

usage: python -I -X utf8 build_10-07-10-09.py [10-07 10-08 10-09]   (writes the Hindi files)
       python -I -X utf8 build_10-07-10-09.py --dry                 (prints, writes nothing)
"""
import re
import sys

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-hi\rails")
import build_rails_sample as S  # noqa: E402

# ---------------------------------------------------------------------------------------------------
# Faculties (termbase; all feminine «क्षमता»)
# ---------------------------------------------------------------------------------------------------
INDRIYA = {
    "cakkhundriya": "आँख की क्षमता",
    "sotindriya": "कान की क्षमता",
    "ghānindriya": "नाक की क्षमता",
    "ghānandriya": "नाक की क्षमता",          # variant spelling (Ghānandriyamūlakaṃ)
    "itthindriya": "स्त्रीत्व की क्षमता",
    "purisindriya": "पुरुषत्व की क्षमता",
    "jīvitindriya": "जीवन-क्षमता",
    "somanassindriya": "प्रसन्नता की क्षमता",
    "upekkhindriya": "समभाव की क्षमता",
    "saddhindriya": "श्रद्धा की क्षमता",
    "paññindriya": "प्रज्ञा की क्षमता",
    "manindriya": "मन की क्षमता",
}
G = "f"


def ind(word):
    """'cakkhundriyaṃ' / 'cakkhundriyañca' -> Hindi."""
    for end in ("ñca", "ṃ"):
        if word.endswith(end) and word[: -len(end)] in INDRIYA:
            return INDRIYA[word[: -len(end)]]
    raise ValueError(f"faculty: {word}")


def ind_list(s):
    """'saddhindriyaṃ…pe… paññindriyaṃ…pe… manindriyaṃ' -> «श्रद्धा की क्षमता… प्रज्ञा की क्षमता… मन की क्षमता»"""
    return "… ".join(ind(w) for w in s.split("…pe… "))


def mulaka(word):
    """'Cakkhundriyamūlakaṃ' -> «आँख की क्षमता पर आधारित»"""
    w = word[0].lower() + word[1:]
    assert w.endswith("mūlakaṃ"), word
    return INDRIYA[w[: -len("mūlakaṃ")]] + " पर आधारित"


# ---------------------------------------------------------------------------------------------------
# Verbs
# ---------------------------------------------------------------------------------------------------
def split_verb(s):
    """'X na uppajjati' -> ('X', 'na uppajjati'); 'X uppajjati' -> ('X', 'uppajjati')."""
    toks = s.split(" ")
    if len(toks) >= 3 and toks[-2] == "na":
        return " ".join(toks[:-2]), "na " + toks[-1]
    return " ".join(toks[:-1]), toks[-1]


def v(tok, flip=False):
    return S.verb_hi(tok, G, flip)


# ---------------------------------------------------------------------------------------------------
# Questions
# ---------------------------------------------------------------------------------------------------
RELS = ["yassa vā pana yattha", "yassa yattha", "yassa vā pana", "yassa", "yattha vā pana", "yattha"]
CORS = {"yassa vā pana yattha": "tassa tattha", "yassa yattha": "tassa tattha", "yassa vā pana": "tassa",
        "yassa": "tassa", "yattha vā pana": "tattha", "yattha": "tattha"}


def question(s):
    m = re.fullmatch(r"(?:\((Ka|Kha)\) )?(.+)\?", s)
    if not m:
        return None
    lab = S.LABELS[f"({m.group(1)})"] + " " if m.group(1) else ""
    body = m.group(2)
    body = body[0].lower() + body[1:]
    rel = next((r for r in RELS if body.startswith(r + " ")), None)
    if rel is None:
        return None
    cor = CORS[rel]
    rest = body[len(rel) + 1:]
    a, sep, b = rest.partition(f" {cor} ")
    if not sep:
        raise ValueError(f"question without correlative: {s}")
    a = a.rstrip(",")                       # 10-09 ^6-10-369: stray comma before tassa
    k1, v1 = split_verb(a)
    k2, v2 = split_verb(b)
    neg2 = v2.startswith("na ")
    v2w = S.strip_ti(v2[3:] if neg2 else v2, S._VERB_TI)
    v2 = ("na " if neg2 else "") + v2w
    rel_hi, cor_hi = S.REL_FRAMES[(rel, cor)]
    return S.Q_FRAME.format(label=lab.strip(), rel=rel_hi, k1=ind_list(k1), v1=v(v1), corr=cor_hi,
                            k2=ind_list(k2), v2=v(v2)).lstrip()


# ---------------------------------------------------------------------------------------------------
# Being / place / moment chains
# ---------------------------------------------------------------------------------------------------
MOD = {  # modifiers before a participle (harmonise I1: «X वाले / X से रहित»)
    "sacakkhukānaṃ": "आँख वाले", "acakkhukānaṃ": "आँख से रहित",
    "saghānakānaṃ": "नाक वाले", "aghānakānaṃ": "नाक से रहित",
    "sahetukānaṃ": "मूल वाले", "ñāṇasampayuttānaṃ": "ज्ञान से जुड़े",
    "na itthīnaṃ": "स्त्रियों से भिन्न", "na purisānaṃ": "पुरुषों से भिन्न",   # as in 10-10/11
    "upekkhāya": "समभाव के साथ", "somanassena": "प्रसन्नता के साथ",
}
COMP = {"somanassa": "प्रसन्नता", "upekkhā": "समभाव", "saddhā": "श्रद्धा", "ñāṇa": "ज्ञान"}
YUTTA = {"sampayutta": "से जुड़े", "vippayutta": "से अलग"}
KHANA = {"uppāda": "उत्पन्न होने", "bhaṅga": "भंग होने"}
BEINGS = dict(S.BEINGS)
BEINGS.update({
    "nirodhasamāpannānaṃ": "समाप्ति की ध्यान-अवस्था में लीन लोगों में",
    "pacchimacittasamaṅgīnaṃ": "अंतिम मन से युक्त लोगों में",
})
PARTICIPLE_FIX = {"cavantāna": "cavantānaṃ"}   # 10-08 ^6-10-361: source slip

_C = "|".join(COMP)
_K = "uppāda|bhaṅga"
_PL = "|".join(sorted(S.PLACE_FORMS, key=len, reverse=True))


def place_hi(words):
    """'rūpāvacaraṃ arūpāvacaraṃ' -> «सूक्ष्म भौतिक लोक या अभौतिक लोक» (several accusative places: «या»)."""
    keys = [S.PLACE_FORMS[w][0] for w in words.split(" ")]
    if keys == ["catuvokāra", "pañcavokāra"]:
        return S.PLACE_NOUN["catupañcavokāra"]
    return " या ".join(S.PLACE_NOUN[k] for k in keys)


def moment(m_comp, m_yutta, pacchima, khana):
    if m_comp:
        return f"{COMP[m_comp]} {YUTTA[m_yutta]} {'अंतिम ' if pacchima else ''}मन के {KHANA[khana]} के क्षण में"
    return f"{'अंतिम ' if pacchima else ''}मन के {KHANA[khana]} के क्षण में"


def anantara_obj(comp, yutta):
    """'upekkhāsampayuttapacchimacittaṃ' (nominative) -> «समभाव से जुड़ा अंतिम मन» (termbase)"""
    return f"{COMP[comp]} {'से जुड़ा' if yutta == 'sampayutta' else 'से अलग'} अंतिम मन"


# Each pattern: (regex, function(match) -> chunk text, or ('YE', text, tail))
def _p_ye(m):
    rel, subj, bhava, how, places, upap, tail = m.group(1), m.group(2), m.group(3), m.group(4), m.group(5), \
        m.group(6), m.group(7)
    fem = rel == "yā"
    sub = {"purisā": "पुरुष", "itthiyo": "स्त्रियाँ", "sacakkhukā": "आँख वाले", "saghānakā": "नाक वाले",
           None: None}[subj]
    parts = ["जो"] + ([sub] if sub else [])
    if bhava:
        assert subj in ("purisā", "itthiyo"), m.group(0)
        # eteneva bhāvena katici bhave dassetvā = «इसी लिंग में कुछ जन्म बिताकर» (as in 10-05/06, 10-10/11/12)
        parts.append("इसी लिंग में कुछ जन्म बिताकर")
    if upap:
        if how:
            parts.append(MOD[how])
        elif places:
            parts.append(place_hi(places) + " में")
        parts.append("जन्म लेकर")
    parts.append("पूर्ण निर्वाण पाएँगी" if fem else "पूर्ण निर्वाण पाएँगे")
    return ("YE", " ".join(parts), tail)


def _p_mod(m):
    pre = m.group(1)
    place = m.group(2)
    s = MOD[pre]
    if place:
        s += " " + place_hi(place) + " में"
    return s + " जन्म लेने वालों में"


PATTERNS = [
    # ye / yā clauses (B3, B9)
    (r"(ye|yā)(?: ca)?(?: (purisā|itthiyo|sacakkhukā|saghānakā))?( eteneva bhāvena katici bhave dassetvā)?"
     rf"(?: (upekkhāya|somanassena)| ((?:(?:{_PL}) ?)+?))?( upapajjitvā)? parinibbāyissanti"
     r"(?: (?:tesaṃ|tāsaṃ) (upapajjantānaṃ|upapajjantīnaṃ|cavantānaṃ))?", _p_ye),
    # moments
    (rf"sabbesaṃ cittassa ({_K})kkhaṇe", lambda m: f"सभी के मन के {KHANA[m.group(1)]} के क्षण में"),
    (rf"pavatte (?:({_C})(sampayutta|vippayutta))?cittassa ({_K})kkhaṇe",
     lambda m: "जीवन के दौरान " + moment(m.group(1), m.group(2), False, m.group(3))),
    (rf"suddhāvāsānaṃ upapatticittassa ({_K})kkhaṇe",
     lambda m: f"{S.BEINGS['suddhāvāsānaṃ']} जन्म के मन के {KHANA[m.group(1)]} के क्षण में"),
    (rf"upapatticittassa ({_K})kkhaṇe", lambda m: f"जन्म के मन के {KHANA[m.group(1)]} के क्षण में"),
    (rf"yassa cittassa anantarā ({_C})(sampayutta|vippayutta)pacchimacittaṃ uppajjissati tassa cittassa "
     rf"({_K})kkhaṇe",
     lambda m: f"जिस मन के ठीक बाद {anantara_obj(m.group(1), m.group(2))} उत्पन्न होगा, "
               f"उस मन के {KHANA[m.group(3)]} के क्षण में"),
    (rf"yassa cittassa anantarā ({_C})(sampayutta|vippayutta)pacchimacittaṃ uppajjissati",
     lambda m: f"जिनमें इस मन के ठीक बाद {anantara_obj(m.group(1), m.group(2))} उत्पन्न होगा, उनमें"),
    (rf"(?:({_C})(sampayutta|vippayutta))?(pacchima)?cittassa ({_K})kkhaṇe",
     lambda m: moment(m.group(1), m.group(2), m.group(3), m.group(4))),
    # last existence (B2)
    (rf"pacchimabhavikānaṃ ({_PL}) upapajjantānaṃ",
     lambda m: f"{place_hi(m.group(1))} में {S.PACCHIMA_UPAPAJJ}"),
    (r"pacchimabhavikānaṃ itthīnaṃ upapajjantīnaṃ", lambda m: "अंतिम जन्म लेने वाली स्त्रियों में"),
    (r"pacchimabhavikānaṃ purisānaṃ upapajjantānaṃ", lambda m: "अंतिम जन्म लेने वाले पुरुषों में"),
    (rf"({_PL}) pacchimabhavikānaṃ", lambda m: f"{place_hi(m.group(1))} में अंतिम जन्म वालों में"),
    (r"pacchimabhavikānaṃ", lambda m: "अंतिम जन्म वालों में"),
    # all / women / men
    (r"sabbesaṃ (cavantānaṃ|upapajjantānaṃ)", lambda m: f"सभी {S.PARTICIPLES[m.group(1)]}"),
    (r"itthīnaṃ upapajjantīnaṃ", lambda m: "जन्म लेने वाली स्त्रियों में"),
    (r"purisānaṃ upapajjantānaṃ", lambda m: "जन्म लेने वाले पुरुषों में"),
    # modifier + [place] + upapajjantānaṃ
    (rf"({'|'.join(MOD)})(?: ((?:(?:{_PL}) ?)+?))? upapajjantānaṃ", _p_mod),
    # place + participle
    (rf"((?:(?:{_PL}) ?)+?) (upapajjantānaṃ|cavantānaṃ|parinibbantānaṃ)",
     lambda m: f"{place_hi(m.group(1))} {S.CASE_POST[S.PLACE_FORMS[m.group(1).split(' ')[0]][1]]} "
               f"{S.PARTICIPLES[m.group(2)]}"),
    (r"upapajjantānaṃ", lambda m: S.PARTICIPLES["upapajjantānaṃ"]),
    # genitive beings
    (r"(" + "|".join(BEINGS) + r")", lambda m: BEINGS[m.group(1)]),
]
PATTERNS = [(re.compile(p), f) for p, f in PATTERNS]


def who(s):
    s = s[0].lower() + s[1:]
    for a, b in PARTICIPLE_FIX.items():
        s = re.sub(rf"\b{a}\b(?!ṃ)", b, s)
    if s == "itaresaṃ":
        return S.ITARESAM_ALONE
    items, pos = [], 0
    pre = None
    while pos < len(s):
        rest = s[pos:]
        if rest.startswith(("itaresaṃ ", "itarāsaṃ ")):
            pre = S.ITARESAM
            pos += len("itaresaṃ ")
            continue
        for rx, fn in PATTERNS:
            m = rx.match(rest)
            if m and (m.end() == len(rest) or rest[m.end()] == " "):
                r = fn(m)
                if isinstance(r, tuple):
                    items.append(r)
                else:
                    items.append(("CH", (pre + " " if pre else "") + r, None))
                pre = None
                pos += m.end() + 1
                break
        else:
            raise ValueError(f"who: cannot parse {rest!r} in {s!r}")
    if pre:
        raise ValueError(f"who: dangling itaresaṃ in {s!r}")
    # closing of ye-clauses: «, उनमें[ से <participle>]» after the last ye of a run
    chunks = []
    for i, (kind, text, tail) in enumerate(items):
        if kind == "YE":
            nxt = items[i + 1][0] if i + 1 < len(items) else None
            if nxt != "YE":
                text += ", उनमें"
                if tail:
                    part = {"upapajjantānaṃ": "जन्म लेने वालों में", "cavantānaṃ": "मरने वालों में",
                            "upapajjantīnaṃ": "जन्म लेने वाली स्त्रियों में"}[tail]
                    text += " से " + part
            elif tail:
                raise ValueError(f"who: tail inside a ye run: {s!r}")
        chunks.append(text)
    if len(chunks) == 1:
        return chunks[0]
    return S.JOIN.join(chunks[:-1]) + S.JOIN_LAST + chunks[-1]


# ---------------------------------------------------------------------------------------------------
# Answer sentences
# ---------------------------------------------------------------------------------------------------
TES = r"(tesaṃ|tāsaṃ)( tattha)?"


def answer(s):
    if not s.endswith("."):
        return None
    body = s[:-1]
    first, sep, second = body.partition(", no ca ")
    if sep:  # BUT frame
        m = re.fullmatch(rf"(.+) {TES} (.+)", first)
        m2 = re.fullmatch(rf"{TES} (.+)", second)
        if not m or not m2 or bool(m.group(3)) != bool(m2.group(2)):
            raise ValueError(f"but-frame: {s}")
        k1, v1 = split_verb(m.group(4))
        k2, v2 = split_verb(m2.group(3))
        frame = S.BUT_BEINGS_T if m.group(3) else S.BUT_BEINGS
        return frame.format(who=who(m.group(1)), k1=ind(k1), v1=v(v1), k2=ind(k2), v2=v(v2, flip=True))
    # BOTH frame: <who> tesaṃ [tattha] K1ñca [na] V1 K2ñca [na] V2
    m = re.fullmatch(rf"(.+) {TES} (\S+?(?:ñca)?) ((?:na )?\S+) (\S+?ñca) ((?:na )?\S+)", body)
    if m:
        # 10-09 ^6-10-376: "manindriyaṃ uppajjissati cakkhundriyañca" (first -ñca missing) read as the both-frame
        frame = S.BOTH_BEINGS_T if m.group(3) else S.BOTH_BEINGS
        return frame.format(who=who(m.group(1)), k1=ind(m.group(4)), v1=v(m.group(5)), k2=ind(m.group(6)),
                            v2=v(m.group(7)))
    return None


def short(s):
    if s in ("Āmantā.", "No.", "Natthi."):
        return S.CLOSINGS[s]
    if s == "Natthi…pe….":
        return S.NATTHI[:-1] + "…।"
    w = s[:-1]
    w = w[0].lower() + w[1:]
    if w in S.VERB_FORMS:
        return v(w) + "।"
    return None


def sentence(s):
    r = short(s)
    if r:
        return r
    m = re.fullmatch(r"\((\S+mūlakaṃ)\)", s)
    if m:
        return f"({mulaka(m.group(1))})"
    if s == "(Sadisaṃ )":
        return f"({S.NOTES['sadisaṃ']})"
    if s.endswith("?…Pe…."):
        return question(s[: -len("…Pe….")]) + "…"
    if s.endswith("?"):
        r = question(s)
        if r:
            return r
    r = answer(s)
    if r:
        return r
    raise ValueError(f"no formula for: {s}")


def text_line(line):
    return " ".join(sentence(x) for x in S._split_sentences(line))


def translate_line(line):
    if not line.strip():
        return ""
    bid = ""
    m = S.ID_RE.search(line)
    if m:
        bid = " " + m.group(1)
        line = line[: m.start()]
    if line.startswith("#"):
        hashes, txt = line.split(" ", 1)
        return f"{hashes} {S.HEADINGS[txt.strip()]}{bid}"
    return text_line(line.strip()) + bid


def translate_text(pali):
    out, prev_blank = [], True
    for line in pali.splitlines():
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


FILES = ["10-07", "10-08", "10-09"]


def main():
    dry = "--dry" in sys.argv
    names = [a for a in sys.argv[1:] if not a.startswith("--")] or FILES
    for n in names:
        f = f"{n}-indriyayamaka.md"
        pali = (S.PALI_DIR / f).read_text(encoding="utf-8")
        hi = translate_text(pali)
        if dry:
            print(hi)
        else:
            (S.HI_DIR / f).write_text(hi, encoding="utf-8", newline="\n")
            print("written", f)


if __name__ == "__main__":
    main()
