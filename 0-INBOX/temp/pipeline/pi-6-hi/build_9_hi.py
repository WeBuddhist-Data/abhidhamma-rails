r"""pi-6 Yamaka, Hindi plain zero-shot: Dhammayamaka (9-01, 9-02, 9-03).

usage: python -I -X utf8 build_9_hi.py
Writes AI_translation\hindi\pi-6-hindi-plain-zeroshot_split_chapters\9-0N-dhammayamaka.md.
"""
import re
import sys

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-hi")
import build_sample_hi as S  # noqa: E402  (import only)
import common_6_9_hi as C    # noqa: E402

ADJ = {"kusalā": "हितकर", "akusalā": "हानिकर", "abyākatā": "नैतिक रूप से अनिर्धारित"}   # core terms
DHAMMA = "परिघटनाएँ"
DHAMMA_OBL = "परिघटनाओं"
# "kusalā dhammā" is one item (feminine plural subject)
ITEMS = {k + "_dhammā": v + " " + DHAMMA for k, v in ADJ.items()}


def norm(s):
    s = re.sub(r"\b(kusalā|akusalā|abyākatā) ca dhammā", r"\1_dhammā ca", s)
    return re.sub(r"\b(kusalā|akusalā|abyākatā) dhammā", r"\1_dhammā", s)


# paṇṇattivāra words: bare adjective / bare "dhammā" / adjective + dhammā; all plural
WORDS = dict(ADJ)
WORDS["dhammā"] = DHAMMA
WORDS.update({k + " dhammā": v + " " + DHAMMA for k, v in ADJ.items()})


def pannatti(body):
    body = body[:-1]
    if body.startswith("na "):
        parts = body[3:].split(" na ")
        if len(parts) != 2:
            return None
        x, y = parts
        if x in WORDS and y in WORDS:
            return S.PANNATTI_Q_PACC.format(X=WORDS[x], Y=WORDS[y], V="हैं", P="वे")
        return None
    t = body.split(" ")
    if len(t) == 2:
        x, y = t
    elif len(t) == 3 and t[2] == "dhammā" and t[1] != "dhammā":
        x, y = t[0], t[1] + " dhammā"
    elif len(t) == 3:
        x, y = t[0] + " " + t[1], t[2]
    else:
        return None
    if x in WORDS and y in WORDS:
        return S.PANNATTI_Q_ANU.format(X=WORDS[x], Y=WORDS[y], V="हैं")
    return None


VP = {   # practice verbs with the object "<adj> परिघटना"
    "bhāveti": "{O} परिघटना का अभ्यास करता है",
    "na bhāveti": "{O} परिघटना का अभ्यास नहीं करता",
    "pajahati": "{O} परिघटना को छोड़ता है",
    "nappajahati": "{O} परिघटना को नहीं छोड़ता",
}
OBJ = {"kusalaṃ": "हितकर", "akusalaṃ": "हानिकर"}


def practice(body):
    vp = "na bhāveti|bhāveti|nappajahati|pajahati"
    m = re.fullmatch(rf"yo( vā pana)? (kusalaṃ|akusalaṃ) dhammaṃ ({vp}) so (kusalaṃ|akusalaṃ) dhammaṃ ({vp})\?", body)
    if not m:
        return None
    and_, o1, v1, o2, v2 = m.groups()
    return ((S.VA_PANA if and_ else "") + "जो " + VP[v1].format(O=OBJ[o1]) + ", क्या वह "
            + VP[v2].format(O=OBJ[o2]) + "?")


QA_ANU_2_PL = "{C}, {B} भी हैं और {C} भी।"   # plural of the sample's QA_ANU_2


def extra(text):
    # C dhammā dhammā ceva C dhammā ca. Avasesā dhammā na C dhammā.
    m = re.fullmatch(r"(\S+) dhammā dhammā ceva (\S+) dhammā ca\. Avasesā dhammā na (\S+) dhammā\.", text)
    if m:
        a, b, c = (x.lower() for x in m.groups())
        assert a == b == c
        cc = ADJ[a] + " " + DHAMMA
        return QA_ANU_2_PL.format(C=cc, B=DHAMMA) + " " + S.AVASESA + " " + DHAMMA + ", " + cc + " नहीं हैं।"
    # Xṃ ṭhapetvā avasesā dhammā na X, dhammā. Xñca dhamme ca ṭhapetvā avasesā na ceva X na ca dhammā.
    m = re.fullmatch(r"(\S+)ṃ ṭhapetvā avasesā dhammā na (\S+), dhammā\. \S+ñca dhamme ca ṭhapetvā avasesā na ceva (\S+) na ca dhammā\.", text)
    if m:
        a, b, c = m.groups()
        a = a.lower()[:-1] + "ā"     # Kusala(ṃ) -> kusalā
        assert a == b == c
        adj = ADJ[a]
        return (S.QA_PACC_1.format(A=S.EXCEPT.format(C=adj) + " " + S.AVASESA + " " + DHAMMA, C=adj, B=DHAMMA, V="हैं")
                + " " + S.QA_PACC_2.format(B=adj, C=DHAMMA_OBL, Bn=adj, Cn=DHAMMA))
    return None


ch = C.Chapter(ITEMS, C.VERBS_FPL, norm)
ch.known_extra = set(ADJ) | {"dhammā", "bhāveti", "pajahati", "nappajahati"}
ch.pannatti = pannatti
ch.q_practice = practice
ch.extra = extra

if __name__ == "__main__":
    for f in ("9-01-dhammayamaka.md", "9-02-dhammayamaka.md", "9-03-dhammayamaka.md"):
        ch.build(f)
