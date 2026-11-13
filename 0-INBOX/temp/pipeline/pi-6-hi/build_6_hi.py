r"""pi-6 Yamaka, Hindi plain zero-shot: Saṅkhārayamaka (6-01, 6-02).

usage: python -I -X utf8 build_6_hi.py
Writes AI_translation\hindi\pi-6-hindi-plain-zeroshot_split_chapters\6-01-sankharayamaka.md and 6-02-….
"""
import re
import sys

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-hi")
import build_sample_hi as S  # noqa: E402  (import only)
import common_6_9_hi as C    # noqa: E402

# the three formations (pi-2 ch6 / pi-5 Hindi); feminine singular
ITEMS = {
    "kāyasaṅkhāro": "शरीर की रचना",
    "vacīsaṅkhāro": "वाणी की रचना",
    "cittasaṅkhāro": "मन की रचना",
}
# bare words in the word-checking pairs (approved choice: bare word rendered bare); (Hindi, plural?)
BARE = {
    "kāyo": ("शरीर", False),        # pi-2 kāya = शरीर (as in शरीर की रचना)
    "vacī": ("वाणी", False),        # pi-2 vacī = वाणी
    "cittaṃ": ("मन", False),        # citta = मन
    "saṅkhārā": ("रचनाएँ", True),   # sample / terms file
}
SANKHARO = "रचना"                   # saṅkhāro (bare, singular)
ACC = {"kāyasaṅkhāraṃ": ITEMS["kāyasaṅkhāro"], "vacīsaṅkhāraṃ": ITEMS["vacīsaṅkhāro"],
       "cittasaṅkhāraṃ": ITEMS["cittasaṅkhāro"]}


def hi(word):
    word = word[0].lower() + word[1:]
    if word in ITEMS:
        return ITEMS[word]
    return BARE[word][0]


def pannatti(body):
    m = re.fullmatch(r"(na )?(\S+) (na )?(\S+)\?", body)
    if not m:
        return None
    n1, x, n2, y = m.groups()
    if bool(n1) != bool(n2):
        return None
    if x not in ITEMS and x not in BARE or y not in ITEMS and y not in BARE:
        return None
    pl = BARE.get(x, ("", False))[1]
    v = "हैं" if pl else "है"
    if n1:
        return S.PANNATTI_Q_PACC.format(X=hi(x), Y=hi(y), V=v, P="वे" if pl else "वह")
    return S.PANNATTI_Q_ANU.format(X=hi(x), Y=hi(y), V=v)


def practice(body):
    m = re.fullmatch(r"yo( vā pana)? (\S+) parijānāti so (\S+) parijānāti\?", body)
    if not m:
        return None
    vp, x, y = m.groups()
    return (S.VA_PANA if vp else "") + f"जो {ACC[x]} को पूरी तरह समझता है, क्या वह {ACC[y]} को पूरी तरह समझता है?"


VAR_AVASESA = S._var(S.VAR_READ, "Sī., Syā., Kaṃ.", "avasesā saṅkhārā saṅkhārā")


def extra(text):
    # A na C, B. Bañca Cañca ṭhapetvā avasesā na ceva B na ca C.
    m = re.fullmatch(r"(\S+) na (\S+), (\S+)\. \S+ \S+ ṭhapetvā avasesā na ceva (\S+) na ca (\S+)\.", text)
    if m:
        a, c, b, bn, cn = m.groups()
        return (S.QA_PACC_1.format(A=hi(a), C=hi(c), B=hi(b), V="है") + " "
                + S.QA_PACC_2.format(B=hi(bn), C=hi(cn), Bn=hi(bn), Cn=hi(cn)))
    # C saṅkhāro ceva C ca. Avasesā saṅkhārā na C.
    m = re.fullmatch(r"(\S+) saṅkhāro ceva (\S+) ca\. Avasesā saṅkhārā( \[avasesā saṅkhārā saṅkhārā \(sī\. syā\. kaṃ\.\)\])? na (\S+)\.", text)
    if m:
        c1, c2, var, c3 = m.groups()
        assert hi(c1) == hi(c2) == hi(c3)
        return (S.QA_ANU_2.format(C=hi(c2), B=SANKHARO) + " " + S.AVASESA + " " + BARE["saṅkhārā"][0]
                + (" " + VAR_AVASESA if var else "") + ", " + hi(c3) + " नहीं हैं।")
    return None


ch = C.Chapter(ITEMS, S.VERBS_F)
ch.known_extra = set(BARE) | {"parijānāti"}
ch.pannatti = pannatti
ch.q_practice = practice
ch.extra = extra
ch.fixed = {
    "Tayo saṅkhārā – kāyasaṅkhāro, vacīsaṅkhāro, cittasaṅkhāroti. Assāsapassāsā kāyasaṅkhāro, vitakkavicārā vacīsaṅkhāro, saññā ca vedanā ca cittasaṅkhāro. Ṭhapetvā vitakkavicāre sabbepi cittasampayuttakā dhammā cittasaṅkhāro.":
        "तीन रचनाएँ – शरीर की रचना, वाणी की रचना, मन की रचना। साँस लेना और छोड़ना शरीर की रचना है, "
        "आरंभिक विचार और सतत विचार वाणी की रचना हैं, पहचान और अनुभूति मन की रचना हैं। "
        "आरंभिक विचार और सतत विचार को छोड़कर मन से जुड़ी सभी परिघटनाएँ मन की रचना हैं।",
    "Dutiyajjhāne tatiyajjhāne tattha…pe… (itaresaṃ yatthakānaṃ sadisaṃ).":
        C.tr_who("Dutiyajjhāne tatiyajjhāne") + "… (बाकी स्थान वाले भागों के समान)।",
}

if __name__ == "__main__":
    for f in ("6-01-sankharayamaka.md", "6-02-sankharayamaka.md"):
        ch.build(f)
