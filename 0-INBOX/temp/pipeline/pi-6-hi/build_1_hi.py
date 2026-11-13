r"""pi-6 Yamaka, Hindi plain zero-shot: Mūlayamaka (1-mulayamaka.md) builder.

usage: python -I -X utf8 build_1_hi.py
The uddesa (non-empty lines 1-122) is the approved sample and is produced by the sample's own
translator; the niddesa answers are composed from the frames below. Unknown lines raise an error.
"""
import re
import sys

HERE = r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-hi"
sys.path.insert(0, HERE)
import build_sample_hi as S  # noqa: E402  (import only)
import build_2_hi as K       # noqa: E402  (shared engine: build, check_sample)

T_ALT = S._TYPE_ALT                  # akusala|abyākata|kusala|nāma
KIND_ALT = S._KIND_ALT               # mūlamūlak|mūlamūl|mūlak|mūl
R = {t: v[1] for t, v in S.MULA_TYPES.items()}       # root phrase: हितकर मूल / मानसिक पक्ष के मूल
ADJ = {t: v[0] for t, v in S.MULA_TYPES.items()}     # हितकर / मानसिक पक्ष की
NOUN = {"kusala": "हितकर", "akusala": "हानिकर", "abyākata": "नैतिक रूप से अनिर्धारित",
        "nāma": "मानसिक पक्ष"}                       # kusalaṃ / nāmaṃ as a noun
NUM = {"Tīṇeva": "तीन", "Naveva": "नौ", "Tayo eva": "तीन"}

# kind of root-word, masculine singular (भौतिक रूप …) and masculine plural (मूल …)
KIND_SG = {"mūla": "मूल वाला", "mūlamūla": "मूल के मूल वाला",
           "mūlaka": "मूल पर आधारित", "mūlamūlaka": "मूल के मूल पर आधारित"}
KIND_PL = {"mūla": "मूल वाले", "mūlamūla": "मूल के मूल वाले",
           "mūlaka": "मूल पर आधारित", "mūlamūlaka": "मूल के मूल पर आधारित"}

ONLY = "{R} {N} ही हैं। शेष {A} परिघटनाएँ {R} नहीं हैं।"   # Tīṇeva kusalamūlāni. Avasesā kusalā dhammā na kusalamūlā.
BORN = "{T} से उत्पन्न भौतिक रूप, {P} है, पर {N} नहीं है। {N}, {P} भी है और {N} भी।"
ROOTLESS = "मूल से रहित {N}, {P} नहीं है। मूल वाला {N}, {P} है।"   # Ahetukaṃ … na … Sahetukaṃ …
MUTUAL = ("जो मूल एक साथ उत्पन्न होते हैं, वे {R} एक ही {KP} भी हैं और परस्पर {KP} भी। "
          "शेष {R} के साथ उत्पन्न परिघटनाएँ {R} के साथ एक ही {KF} हैं, पर परस्पर {KF} नहीं हैं।")


def pred_sg(tok):
    """'kusalamūlena ekamūlaṃ' / 'kusalamūlakaṃ' -> (type, Hindi masc. sg.)."""
    m = re.fullmatch(rf"({T_ALT})mūlena eka({KIND_ALT})aṃ", tok)
    if m:
        t, k = m.groups()
        return t, f"{R[t]} के साथ एक ही {KIND_SG[k + 'a']}"
    m = re.fullmatch(rf"({T_ALT})({KIND_ALT})aṃ", tok)
    if m:
        t, k = m.groups()
        return t, S.MULA_KIND_ALONE[k + "a"].format(R=R[t])
    return None


def a_mula(s):
    # Tīṇeva kusalamūlāni. Avasesā kusalā dhammā na kusalamūlā.   (both sentences)
    m = re.fullmatch(rf"(Tīṇeva|Naveva) ({T_ALT})({KIND_ALT})āni\. Avasesā (\S+) dhammā na \2\3ā\.", s)
    if m:
        n, t, k, _ = m.groups()
        return ONLY.format(R=S.MULA_KIND_ALONE[k + "a"].format(R=R[t]), N=NUM[n], A=ADJ[t])
    # Kusalasamuṭṭhānaṃ rūpaṃ P, na kusalaṃ. Kusalaṃ Pñceva kusalañca.
    m = re.fullmatch(rf"({T_ALT})samuṭṭhānaṃ rūpaṃ (.+?),? na \1ṃ\. ({T_ALT})ṃ (.+?)ñceva \1ñca\.", s, re.I)
    if m:
        t, p, _, p2 = m.groups()
        t = t.lower()
        tp = pred_sg(p)
        if tp and pred_sg(p2 + "ṃ") == tp:
            return BORN.format(T=NOUN[t], P=tp[1], N=NOUN[t])
    # Ahetukaṃ akusalaṃ akusalamūlena na ekamūlaṃ. Sahetukaṃ akusalaṃ akusalamūlena ekamūlaṃ.
    m = re.fullmatch(rf"Ahetukaṃ ({T_ALT})ṃ (.+)\. Sahetukaṃ \1ṃ (.+)\.", s)
    if m:
        t, neg, pos = m.groups()
        neg2 = re.sub(r"(^| )na ", r"\1", neg)
        if neg2 == neg:
            return None
        a, b = pred_sg(neg2), pred_sg(pos)
        if a and b and a == b:
            return ROOTLESS.format(N=NOUN[t], P=a[1])
    # Mūlāni yāni ekato uppajjanti … Avasesā …sahajātā dhammā …, na ca ….
    m = re.fullmatch(rf"Mūlāni yāni ekato uppajjanti ({T_ALT})mūlāni eka({KIND_ALT})āni ceva aññamañña\2āni ca\. "
                     rf"Avasesā \1mūlasahajātā dhammā \1mūlena eka\2ā,? na ca aññamañña\2ā\.", s)
    if m:
        t, k = m.groups()
        return MUTUAL.format(R=R[t], KP=KIND_PL[k + "a"], KF=S.MULA_KIND_REL[k + "a"])
    return None


def lc_first(s):
    return s[:1].lower() + s[1:]


def tr_answer(text):
    if text in FIXED:
        return FIXED[text]
    if text in K.SHORT:
        return K.SHORT[text]
    r = a_mula(text)
    if r is None:
        raise ValueError("untranslated answer: " + text)
    return r


Q_KA_DOTS = "जो भी {S} परिघटनाएँ हैं, क्या वे सब {P} हैं…?"
FIXED = dict(S.FIXED)
FIXED.update({
    "Mūlavāraniddeso.": "मूल के खंड की व्याख्या।",
    # Hetuvārādi, niddesa
    "Ye keci kusalā dhammā, sabbe te kusalahetūti…?":
        Q_KA_DOTS.format(S=ADJ["kusala"], P="हितकर हेतु"),
    "Tayo eva kusalahetū, avasesā kusalā dhammā na kusalahetū…pe… kusalanidānā… kusalasambhavā… kusalappabhavā… kusalasamuṭṭhānā… kusalāhārā… kusalārammaṇā… kusalapaccayā… kusalasamudayā….":
        "हितकर हेतु तीन ही हैं, शेष हितकर परिघटनाएँ हितकर हेतु नहीं हैं… हितकर स्रोत… हितकर उद्भव… हितकर उद्गम… हितकर उत्पादक… हितकर आहार… हितकर विषय… हितकर कारण… हितकर उत्पत्ति…।",
    "Ye keci akusalā dhammā… ye keci abyākatā dhammā… ye keci nāmā dhammā, sabbe te nāmahetū ti… nāmanidānā… nāmasambhavā… nāmappabhavā… nāmasamuṭṭhānā… nāmāhārā… nāmārammaṇā… nāmapaccayā… nāmasamudayā….":
        "जो भी हानिकर परिघटनाएँ हैं… जो भी नैतिक रूप से अनिर्धारित परिघटनाएँ हैं… जो भी मानसिक पक्ष की परिघटनाएँ हैं, क्या वे सब मानसिक पक्ष के हेतु हैं… मानसिक पक्ष के स्रोत… मानसिक पक्ष के उद्भव… मानसिक पक्ष के उद्गम… मानसिक पक्ष के उत्पादक… मानसिक पक्ष के आहार… मानसिक पक्ष के विषय… मानसिक पक्ष के कारण… मानसिक पक्ष की उत्पत्ति…।",
})


def tr_body(text):
    if text in FIXED:
        return FIXED[text]
    m = re.match(r"^(\((?:Ka|Kha)\)) (.*)$", text)
    if m:
        label, rest = m.groups()
        q, ans = (rest.split("? ", 1) + [None])[:2] if "? " in rest else (rest[:-1], None)
        hq = S.tr_mula_question(q + "?")
        if hq is None:
            raise ValueError("untranslated question: " + text)
        out = S.LABELS[label] + " " + hq
        if ans:
            out += " " + tr_answer(ans)
        return out
    return tr_answer(text)


def main():
    K.build("1-mulayamaka.md", tr_body)
    print("built 1-mulayamaka.md")
    K.check_sample("1-mulayamaka.md", "s1-mula", 1, 122)


if __name__ == "__main__":
    main()
