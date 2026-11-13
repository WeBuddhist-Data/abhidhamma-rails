"""pi-6 Indriyayamaka 10-03 / 10-04 (uppādavāra, paccuppanna: (Ga) … (Ca)) -> Hindi plain RAILS.

Imports build_rails_sample.py read-only for the approved formula strings; adds the faculty names,
the being modifiers and the moments of the Indriyayamaka (recorded in notes-10-03-10-04.md).
Run: python -I -X utf8 build_10-03_10-04.py
"""
import re
import sys

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-hi\rails")
import build_rails_sample as S  # noqa: E402  (read-only)

FILES = ["10-03-indriyayamaka.md", "10-04-indriyayamaka.md"]

# ---------------------------------------------------------------- faculties (termbase; all feminine)
INDRIYA = {
    "cakkhundriya": "आँख की क्षमता",
    "sotindriya": "कान की क्षमता",
    "ghānindriya": "नाक की क्षमता",
    "itthindriya": "स्त्रीत्व की क्षमता",
    "purisindriya": "पुरुषत्व की क्षमता",
    "jīvitindriya": "जीवन-क्षमता",
    "somanassindriya": "प्रसन्नता की क्षमता",
    "upekkhindriya": "समभाव की क्षमता",
    "saddhindriya": "श्रद्धा की क्षमता",
    "paññindriya": "प्रज्ञा की क्षमता",
    "manindriya": "मन की क्षमता",
}
G = "f"   # क्षमता is feminine


def ind(tok):
    """'cakkhundriyaṃ' / 'cakkhundriyañca' -> Hindi."""
    for suf in ("ñca", "ṃ"):
        if tok.endswith(suf) and tok[: -len(suf)] in INDRIYA:
            return INDRIYA[tok[: -len(suf)]]
    raise ValueError(f"faculty: {tok}")


def ind_list(s):
    """'itthindriyaṃ…pe… purisindriyaṃ' -> 'स्त्रीत्व की क्षमता… पुरुषत्व की क्षमता'."""
    return "… ".join(ind(p.strip()) for p in s.split("…pe…"))


MULAKA = {k[0].upper() + k[1:] + "mūlakaṃ": f"({v} पर आधारित)" for k, v in INDRIYA.items()}

# ---------------------------------------------------------------- beings: modifiers (masc/plain, fem)
MOD = {
    "sacakkhukānaṃ": ("आँख वाले", "आँख वाली"),
    "acakkhukānaṃ": ("आँख से रहित", "आँख से रहित"),
    "sasotakānaṃ": ("कान वाले", "कान वाली"),
    "asotakānaṃ": ("कान से रहित", "कान से रहित"),
    "saghānakānaṃ": ("नाक वाले", "नाक वाली"),
    "aghānakānaṃ": ("नाक से रहित", "नाक से रहित"),
    "sahetukānaṃ": ("मूल वाले", "मूल वाली"),
    "ahetukānaṃ": ("मूल से रहित", "मूल से रहित"),
    "ñāṇasampayuttānaṃ": ("ज्ञान से जुड़े", "ज्ञान से जुड़ी"),
    "ñāṇavippayuttānaṃ": ("ज्ञान से अलग", "ज्ञान से अलग"),
    "sacittakānaṃ": ("मन वाले", "मन वाली"),
    "acittakānaṃ": ("मन से रहित", "मन से रहित"),
    "somanassena": ("प्रसन्नता के साथ", "प्रसन्नता के साथ"),
    "vinā somanassena": ("प्रसन्नता के बिना", "प्रसन्नता के बिना"),
    "upekkhāya": ("समभाव के साथ", "समभाव के साथ"),
    "vinā upekkhāya": ("समभाव के बिना", "समभाव के बिना"),
    "na itthīnaṃ": ("स्त्री न होने वाले", None),
    "na purisānaṃ": ("पुरुष न होने वाले", None),
}
UPAPAJJ_M = "जन्म लेने वालों में"            # upapajjantānaṃ (S.PARTICIPLES)
UPAPAJJ_MEN = "जन्म लेने वाले पुरुषों में"    # purisānaṃ … upapajjantānaṃ
UPAPAJJ_F = "जन्म लेने वाली स्त्रियों में"     # itthīnaṃ … upapajjantīnaṃ (S.PARTICIPLES)
assert S.PARTICIPLES["upapajjantānaṃ"] == UPAPAJJ_M and S.PARTICIPLES["upapajjantīnaṃ"] == UPAPAJJ_F

# ---------------------------------------------------------------- moments
PAVATTE = "जीवन के दौरान"
ASSOC_NAME = {"somanassa": "प्रसन्नता", "upekkhā": "समभाव", "saddhā": "श्रद्धा", "ñāṇa": "ज्ञान"}
ASSOC_KIND = {"sampayutta": "से जुड़े", "vippayutta": "से अलग"}
KHANA = {"uppādakkhaṇe": "उत्पन्न होने के क्षण में", "bhaṅgakkhaṇe": "भंग होने के क्षण में"}


def citta_mod(w):
    """'somanassasampayuttasaddhāvippayuttacittassa' -> 'प्रसन्नता से जुड़े और श्रद्धा से अलग मन के'."""
    assert w.endswith("cittassa"), w
    core = w[: -len("cittassa")]
    parts = re.findall(r"(somanassa|upekkhā|saddhā|ñāṇa)(sampayutta|vippayutta)", core)
    if "".join(a + b for a, b in parts) != core:
        raise ValueError(f"citta compound: {w}")
    mods = [f"{ASSOC_NAME[a]} {ASSOC_KIND[b]}" for a, b in parts]
    return (" और ".join(mods) + " " if mods else "") + "मन के"


def who(s):
    """Being / moment chain before tesaṃ / tāsaṃ -> Hindi chunks, each ending in «में», last joined «और»."""
    s = s[0].lower() + s[1:]
    s = s.replace("vinā somanassena", "vinā_somanassena").replace("vinā upekkhāya", "vinā_upekkhāya")
    s = re.sub(r"(?<!\S)na (itthīnaṃ|purisānaṃ)", r"na_\1", s)
    toks = s.split(" ")
    chunks, mods, head, pre, i = [], [], None, [], 0
    while i < len(toks):
        w = toks[i].replace("_", " ")
        if w in MOD:
            mods.append(w)
        elif w == "itthīnaṃ":
            head = "f"
        elif w == "purisānaṃ":
            head = "men"
        elif w in ("upapajjantānaṃ", "upapajjantīnaṃ", "uppajjantīnaṃ"):
            fem = w != "upapajjantānaṃ"
            if fem != (head == "f"):
                raise ValueError(f"who: gender of participle in {s!r}")
            g = 1 if fem else 0
            words = [MOD[m][g] for m in mods]
            if None in words:
                raise ValueError(f"who: no feminine form in {s!r}")
            part = UPAPAJJ_F if fem else (UPAPAJJ_MEN if head == "men" else UPAPAJJ_M)
            chunks.append(" ".join(([" और ".join(words)] if words else []) + [part]))
            mods, head = [], None
        elif w == "sabbesaṃ":
            pre.append(w)
        elif w == "cavantānaṃ":
            if pre != ["sabbesaṃ"] or mods or head:
                raise ValueError(f"who: cavantānaṃ in {s!r}")
            chunks.append(f"{S.SABBESAM} {S.PARTICIPLES['cavantānaṃ']}")
            pre = []
        elif w == "pavatte" or w.endswith("cittassa"):
            lead = []
            if w == "pavatte":
                lead.append(PAVATTE)
                i += 1
                w = toks[i]
            if pre == ["sabbesaṃ"]:
                lead.append("सभी के")
                pre = []
            k = toks[i + 1]
            chunks.append(" ".join(lead + [citta_mod(w), KHANA[k]]))
            i += 1
        elif w in S.BEINGS:          # asaññasattānaṃ
            chunks.append(S.BEINGS[w])
        elif w == "nirodhasamāpannānaṃ":
            chunks.append("समाप्ति की ध्यान-अवस्था में लीन लोगों में")
        else:
            raise ValueError(f"who: unknown token {w!r} in {s!r}")
        i += 1
    if mods or head or pre:
        raise ValueError(f"who: dangling tokens in {s!r}")
    if len(chunks) == 1:
        return chunks[0]
    return S.JOIN.join(chunks[:-1]) + S.JOIN_LAST + chunks[-1]


# ---------------------------------------------------------------- sentences
_REL = r"(yassa vā pana yattha|yassa yattha|yassa vā pana|yassa|yattha vā pana|yattha)"
_COR = r"(tassa tattha|tassa|tattha)"
_VB = r"((?:na )?uppajjati)"
_T = r"(tesaṃ tattha|tāsaṃ tattha|tesaṃ|tāsaṃ|tattha)"


def question(s):
    m = re.fullmatch(rf"(?:\((Ka|Kha)\) )?{_REL} (\S+) {_VB} {_COR} (.+?) ((?:na )?uppajjatīti)\?",
                     s[0].lower() + s[1:] if not s.startswith("(") else s)
    if not m:
        return None
    lab, rel, k1, v1, cor, k2, v2 = m.groups()
    v2 = v2[:-3] + "i"   # uppajjatīti -> uppajjati
    rel_hi, cor_hi = S.REL_FRAMES[(rel, cor)]
    out = S.Q_FRAME.format(label=S.LABELS[f"({lab})"] if lab else "", rel=rel_hi, k1=ind(k1),
                           v1=S.verb_hi(v1, G), corr=cor_hi, k2=ind_list(k2), v2=S.verb_hi(v2, G))
    return out.strip()


def answer(s):
    m = re.fullmatch(rf"(.+?) {_T} (\S+) {_VB}, no ca {_T} (\S+) {_VB}\.", s)
    if m:
        wh, t, k1, v1, t2, k2, v2 = m.groups()
        args = dict(k1=ind(k1), v1=S.verb_hi(v1, G), k2=ind(k2), v2=S.verb_hi(v2, G, flip=True))
        if t == "tattha":
            return S.BUT_PLACE.format(place=S.place(wh), **args)
        frame = S.BUT_BEINGS_T if t.endswith("tattha") else S.BUT_BEINGS
        return frame.format(who=who(wh), **args)
    m = re.fullmatch(rf"(.+?) {_T} (\S+ñca) {_VB} (\S+ñca) {_VB}\.", s)
    if m:
        wh, t, k1, v1, k2, v2 = m.groups()
        args = dict(k1=ind(k1), v1=S.verb_hi(v1, G), k2=ind(k2), v2=S.verb_hi(v2, G))
        if t == "tattha":
            return S.BOTH_PLACE.format(place=S.place(wh), **args)
        frame = S.BOTH_BEINGS_T if t.endswith("tattha") else S.BOTH_BEINGS
        return frame.format(who=who(wh), **args)
    return None


def sentence(s):
    if s in S.CLOSINGS:
        return S.CLOSINGS[s]
    if s == "Āmantā …pe….":
        return "हाँ …।"
    if s.startswith("(") and s.endswith(")") and s[1:-1] in MULAKA:
        return MULAKA[s[1:-1]]
    for fn in (question, answer):
        r = fn(s)
        if r:
            return r
    r = S.short_answer(s, G)
    if r:
        return r
    raise ValueError(f"no formula for: {s}")


def translate_line(line):
    bid = ""
    m = S.ID_RE.search(line)
    if m:
        bid = " " + m.group(1)
        line = line[: m.start()]
    if line.startswith("#"):
        hashes, text = line.split(" ", 1)
        return f"{hashes} {S.HEADINGS[text.strip()]}{bid}"
    return " ".join(sentence(x) for x in S._split_sentences(line.strip())) + bid


def build(name):
    pali = (S.PALI_DIR / name).read_bytes().decode("utf-8")
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
    (S.HI_DIR / name).write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")
    print("built", name, len([x for x in out if x]), "lines")


if __name__ == "__main__":
    for f in (sys.argv[1:] or FILES):
        build(f)
