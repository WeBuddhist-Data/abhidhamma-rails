# -*- coding: utf-8 -*-
"""pi-2 chapter 18 (Dhammahadayavibhaṅga), Hindi plain zero-shot.

usage: python -I -X utf8 build_18-dhammahadayavibhango_hi.py
Writes AI_translation\\hindi\\pi-2-hindi-plain-zeroshot_split_chapters\\18-dhammahadayavibhango.md
Block IDs are copied from the Pāli at build time (S.assemble).
"""
import re
import sys
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-hi")
from common_ch8_ch18_hi import (S, DASH, Subj, sent, parts, nv, inf, write_chapter,  # noqa: E402
                                pi1_line, check_pi1)

FNAME = "18-dhammahadayavibhango.md"
D_ = DASH

NUMW = {1: "एक", 2: "दो", 3: "तीन", 4: "चार", 5: "पाँच", 6: "छह", 7: "सात", 8: "आठ", 9: "नौ", 10: "दस",
        11: "ग्यारह", 12: "बारह", 13: "तेरह", 14: "चौदह", 15: "पंद्रह", 16: "सोलह", 18: "अठारह", 22: "बाईस"}

# ------------------------------------------------------------ names (pi-1 / pi-3 / pi-4)
AY = {  # āyatana
    "cakkhu": "आँख", "rupa": "दृश्य रूप", "sota": "कान", "sadda": "ध्वनि", "ghana": "नाक", "gandha": "गंध",
    "jivha": "जीभ", "rasa": "स्वाद", "kaya": "शरीर", "photthabba": "स्पर्श", "mana": "मन", "dhamma": "मन के विषयों",
}
AY_ORDER = ["cakkhu", "rupa", "sota", "sadda", "ghana", "gandha", "jivha", "rasa", "kaya", "photthabba", "mana", "dhamma"]


def ay(k):
    return f"{AY[k]} का इंद्रिय-क्षेत्र"


def ays(keys):
    return ", ".join(ay(k) for k in keys)


def dh(k):
    """dhātu: cakkhu … ; 'cakkhuvi' = आँख की चेतना का तत्व; 'mano' = मन का तत्व; 'manovi'"""
    if k.endswith("vi"):
        base = {"cakkhuvi": "आँख", "sotavi": "कान", "ghanavi": "नाक", "jivhavi": "जीभ", "kayavi": "शरीर",
                "manovi": "मन"}[k]
        return f"{base} की चेतना का तत्व"
    if k == "mano":
        return "मन का तत्व"
    return f"{AY[k]} का तत्व"


def dhs(keys):
    return ", ".join(dh(k) for k in keys)


DH18 = ["cakkhu", "rupa", "cakkhuvi", "sota", "sadda", "sotavi", "ghana", "gandha", "ghanavi", "jivha", "rasa",
        "jivhavi", "kaya", "photthabba", "kayavi", "mano", "dhamma", "manovi"]
SACCA = {"dukkha": "दुःख का सत्य", "samudaya": "दुःख की उत्पत्ति का सत्य", "nirodha": "दुःख के अंत का सत्य",
         "magga": "दुःख के अंत के मार्ग का सत्य"}
IN = {
    "cakkhu": "आँख की क्षमता", "sota": "कान की क्षमता", "ghana": "नाक की क्षमता", "jivha": "जीभ की क्षमता",
    "kaya": "शरीर की क्षमता", "mana": "मन की क्षमता", "itthi": "स्त्रीत्व की क्षमता", "purisa": "पुरुषत्व की क्षमता",
    "jivita": "जीवन-क्षमता", "sukha": "सुख की क्षमता", "dukkha": "दुःख की क्षमता", "somanassa": "प्रसन्नता की क्षमता",
    "domanassa": "उदासी की क्षमता", "upekkha": "समभाव की क्षमता", "saddha": "श्रद्धा की क्षमता",
    "viriya": "उत्साह की क्षमता", "sati": "सजगता की क्षमता", "samadhi": "एकाग्रता की क्षमता",
    "panna": "प्रज्ञा की क्षमता", "ananna": "“जो अब तक नहीं जाना उसे मैं जान लूँगा” की क्षमता",
    "anna": "पूर्ण ज्ञान की क्षमता", "annatavi": "पूर्ण ज्ञान पा चुके की क्षमता",
    "ip": "स्त्रीत्व की क्षमता या पुरुषत्व की क्षमता", "su": "प्रसन्नता की क्षमता या समभाव की क्षमता",
}
IN22 = ["cakkhu", "sota", "ghana", "jivha", "kaya", "mana", "itthi", "purisa", "jivita", "sukha", "dukkha",
        "somanassa", "domanassa", "upekkha", "saddha", "viriya", "sati", "samadhi", "panna", "ananna", "anna",
        "annatavi"]


def ins(keys):
    return ", ".join(IN[k] for k in keys)


SENSES = ["आँख", "कान", "नाक", "जीभ", "शरीर"]
CONTACT_BASES = SENSES + ["मन के तत्व", "मन की चेतना के तत्व"]
PHASSA = {b: f"{b} का संपर्क" for b in CONTACT_BASES}
PHASSA7 = ", ".join(PHASSA[b] for b in CONTACT_BASES)


def born7(noun):
    return ", ".join(f"{b} के संपर्क से उत्पन्न {noun}" for b in CONTACT_BASES)


VEDANA7, SANNA7, CETANA7 = born7("अनुभूति"), born7("पहचान"), born7("इरादा")
CITTA_N = {b: f"{b} की चेतना" for b in SENSES}
CITTA_N["mano"] = "मन का तत्व"
CITTA_N["manovi"] = "मन की चेतना का तत्व"
CITTA7 = ", ".join(CITTA_N[k] for k in SENSES + ["mano", "manovi"])
KAB = "कौर-कौर खाया जाने वाला भोजन"                               # pi-1
AHARA3 = "संपर्क रूपी आहार, मानसिक इरादा रूपी आहार, चेतना रूपी आहार"  # pi-1 ^1-70
AHARA4 = KAB + ", " + AHARA3
MVDS = PHASSA["मन की चेतना के तत्व"]                                 # manoviññāṇadhātusamphasso
MDS = PHASSA["मन के तत्व"]
KVDS = "शरीर की चेतना के तत्व का संपर्क"
MVD = dh("manovi")
KHANDHA = ["भौतिक रूप का समूह", "अनुभूति का समूह", "पहचान का समूह", "मानसिक रचनाओं का समूह", "चेतना का समूह"]
K5 = ", ".join(KHANDHA)
K4 = ", ".join(KHANDHA[1:])

# hetus
KH = "हितकर मूल"
AKH = "हानिकर मूल"
ABH = "नैतिक रूप से अनिर्धारित मूल"
VH = "कर्म-फल रूपी मूल"
ROOT = {"alobha": "लोभ का अभाव", "adosa": "द्वेष का अभाव", "amoha": "मोह का अभाव",
        "lobha": "लोभ", "dosa": "द्वेष", "moha": "मोह"}


def named(root, kind):
    return f"{ROOT[root]} नामक {kind}"


# ------------------------------------------------------------ counted nouns
# (singular, plural, oblique plural, gender, interrogative)
CNT = {
    "khandha": ("समूह", "समूह", "समूहों", "m", "कितने समूह"),
    "ayatana": ("इंद्रिय-क्षेत्र", "इंद्रिय-क्षेत्र", "इंद्रिय-क्षेत्रों", "m", "कितने इंद्रिय-क्षेत्र"),
    "dhatu": ("तत्व", "तत्व", "तत्वों", "m", "कितने तत्व"),
    "sacca": ("सत्य", "सत्य", "सत्यों", "m", "कितने सत्य"),
    "indriya": ("क्षमता", "क्षमताएँ", "क्षमताओं", "f", "कितनी क्षमताएँ"),
    "hetu": ("मूल", "मूल", "मूलों", "m", "कितने मूल"),
    "ahara": ("आहार", "आहार", "आहारों", "m", "कितने आहार"),
    "phassa": ("संपर्क", "संपर्क", "संपर्कों", "m", "कितने संपर्क"),
    "vedana": ("अनुभूति", "अनुभूतियाँ", "अनुभूतियों", "f", "कितनी अनुभूतियाँ"),
    "sanna": ("पहचान", "पहचानें", "पहचानों", "f", "कितनी पहचानें"),
    "cetana": ("इरादा", "इरादे", "इरादों", "m", "कितने इरादे"),
    "citta": ("प्रकार का मन", "प्रकार के मन", "प्रकार के मन", "m", "कितने प्रकार के मन"),
}
KINDS = ["khandha", "ayatana", "dhatu", "sacca", "indriya", "hetu", "ahara", "phassa", "vedana", "sanna", "cetana",
         "citta"]


def cnt(kind, n, other=False):
    sg, pl, _, g, _ = CNT[kind]
    if n == 1:
        return f"एक {sg}"
    o = ("दूसरी " if g == "f" else "दूसरे ") if other else ""
    return f"{o}{NUMW[n]} {pl}"


def gn(kind, n):
    return CNT[kind][3], ("sg" if n == 1 else "pl")


def C(kind, n):
    """Subj for a counted noun"""
    sg, pl, obl, g, _ = CNT[kind]
    if n == 1:
        return Subj(f"एक {sg}", g, "sg")
    return Subj(f"{NUMW[n]} {pl}", g, "pl", obl=f"{NUMW[n]} {obl}")


def N(nom, g="m", n="sg", obl=None):
    return Subj(nom, g, n, obl)


RK = N("भौतिक रूप का समूह", obl="भौतिक रूप के समूह")
SANKHARAK = N("मानसिक रचनाओं का समूह", obl="मानसिक रचनाओं के समूह")
MANAY = N(ay("mana"), obl="मन के इंद्रिय-क्षेत्र")
DHAMMAY = N(ay("dhamma"), obl="मन के विषयों के इंद्रिय-क्षेत्र")
RUPAY = N(ay("rupa"))
SADDAY = N(ay("sadda"))
GRP_AY = N(f"{ay('gandha')}… {ay('rasa')}… {ay('photthabba')}")
MANOD = N(dh("mano"))
MVD_S = N(MVD, obl="मन की चेतना के तत्व")
DHD = N(dh("dhamma"), obl="मन के विषयों के तत्व")
KVD = N(dh("kayavi"))
RUPAD = N(dh("rupa"))
SADDAD = N(dh("sadda"))
GRP_D = N(f"{dh('gandha')}… {dh('rasa')}… {dh('photthabba')}")
SAMUDAYA = N(SACCA["samudaya"])
MAGGA = N(SACCA["magga"])
NIRODHA = N(SACCA["nirodha"], obl="दुःख के अंत के सत्य")
DUKKHA = N(SACCA["dukkha"], obl="दुःख के सत्य")
DOMAN = N(IN["domanassa"], "f")
ANANNA = N(IN["ananna"], "f")
ANNA = N(IN["anna"], "f")
ANNATAVI = N(IN["annatavi"], "f")
JIVITA = N(IN["jivita"], "f", obl="जीवन-क्षमता")
UPEKKHA = N(IN["upekkha"], "f")
DOSO = N(named("dosa", AKH))
MOHO = N(named("moha", AKH))
KABS = N(KAB, obl="कौर-कौर खाए जाने वाले भोजन")
MVDS_S = N(MVDS)
MDS_S = N(MDS)
KVDS_S = N(KVDS)
MVDS_VED = N("मन की चेतना के तत्व के संपर्क से उत्पन्न अनुभूति", "f")
MVDS_SAN = N("मन की चेतना के तत्व के संपर्क से उत्पन्न पहचान", "f")
MVDS_CET = N("मन की चेतना के तत्व के संपर्क से उत्पन्न इरादा")


def FOUR_MENTAL(n, sep="… "):
    """Cha vedanā… cha saññā… cha cetanā… cha cittā (agreement with the last item, m.pl)"""
    return Subj(sep.join([cnt("vedana", n), cnt("sanna", n), cnt("cetana", n)]) + sep + cnt("citta", n), "m", "pl")


# ------------------------------------------------------------ question / answer helpers
def kaun(g, n):
    if g == "f":
        return "कौन-सी"
    return "कौन-से" if n == "pl" else "कौन-सा"


def kaha(g, n):
    if g == "f":
        return "कही जाती हैं" if n == "pl" else "कही जाती है"
    return "कहे जाते हैं" if n == "pl" else "कहा जाता है"


def ye(n):
    return "ये" if n == "pl" else "यह"


def appear(g, n):
    if g == "f":
        return "प्रकट होती हैं" if n == "pl" else "प्रकट होती है"
    return "प्रकट होते हैं" if n == "pl" else "प्रकट होता है"


def qa(loc, kind, n, members, quoted=True, dash=True):
    """Tattha katame <loc> <N X>? <members> – ime vuccanti "<loc> <N X>"."""
    g, num = gn(kind, n)
    x = cnt(kind, n)
    name = f"{loc}{x}"
    q = f"यहाँ {name} {kaun(g, num)} {'हैं' if num == 'pl' else 'है'}?"
    nm = f"“{name}”" if quoted else name
    sep = f" {D_} " if dash else " "
    return f"{q} {members}{sep}{ye(num)} {nm} {kaha(g, num)}।"


KATI_ALL = [CNT[k][4] for k in KINDS]


def kati_line(loc=""):
    """Kati khandhā, kati āyatanāni, … kati cittāni?"""
    first = KATI_ALL[0] + " हैं"
    return loc + ", ".join([first] + KATI_ALL[1:]) + "?"


def kati_short(loc, upto=None):
    """Rūpadhātuyā kati khandhā, … kati indriyāni…pe… kati cittāni?  (upto = number of kinds before the …)"""
    first = KATI_ALL[0] + " हैं"
    items = [first] + KATI_ALL[1:upto]
    return loc + ", ".join(items) + "… " + KATI_ALL[-1] + "?"


def counts_line(loc, spec):
    """Pañcakkhandhā, dvādasāyatanāni, …  spec: list of (kind, n)"""
    return loc + ", ".join(cnt(k, n) for k, n in spec) + "।"


# ------------------------------------------------------------ 1. Sabbasaṅgāhikavāra
ALL_SPEC = [("khandha", 5), ("ayatana", 12), ("dhatu", 18), ("sacca", 4), ("indriya", 22), ("hetu", 9),
            ("ahara", 4), ("phassa", 7), ("vedana", 7), ("sanna", 7), ("cetana", 7), ("citta", 7)]

ABY_HETU_DEF = pi1_line("1-1068")      # यहाँ तीन नैतिक रूप से अनिर्धारित मूल कौन-से हैं? … – ये तीन … मूल हैं।
ABY_HETU_Q = "यहाँ तीन नैतिक रूप से अनिर्धारित मूल कौन-से हैं?"
assert ABY_HETU_DEF.startswith(ABY_HETU_Q)
KUSALA_HETU_Q = pi1_line("1-1060").split("?")[0] + "?"   # यहाँ तीन हितकर मूल कौन-से हैं?


def hetu_lines(loc, n_total, akusala=("lobha", "dosa", "moha"), aby_def=None, closing_quoted=True,
               with_akusala=True):
    """the 3–4 lines on the hetus; returns list of lines"""
    g, num = gn("hetu", n_total)
    L = []
    head_items = [f"तीन {KH}"]
    if with_akusala:
        head_items.append(f"{NUMW[len(akusala)]} {AKH}")
    head_items.append(f"तीन {ABH}")
    L.append(f"यहाँ {loc}{cnt('hetu', n_total)} कौन-से हैं? " + ", ".join(head_items) + "।")
    L.append(f"{KUSALA_HETU_Q} " + ", ".join(named(r, KH) for r in ("alobha", "adosa", "amoha"))
             + f" {D_} ये तीन {KH} हैं।")
    if with_akusala:
        a = NUMW[len(akusala)]
        L.append(f"यहाँ {a} {AKH} कौन-से हैं? " + ", ".join(named(r, AKH) for r in akusala)
                 + f" {D_} ये {a} {AKH} हैं।")
    name = f"{loc}{cnt('hetu', n_total)}"
    nm = f"“{name}”" if closing_quoted else name
    L.append(f"{aby_def or ABY_HETU_DEF} ये {nm} {kaha(g, num)}।")
    return L


def sabbasangahika():
    L = [
        "#### सब कुछ समेटने वाला खंड",
        kati_line(),
        counts_line("", ALL_SPEC),
        qa("", "khandha", 5, K5),
        qa("", "ayatana", 12, ays(AY_ORDER)),
        qa("", "dhatu", 18, dhs(DH18)),
        qa("", "sacca", 4, ", ".join(SACCA[k] for k in ("dukkha", "samudaya", "nirodha", "magga"))),
        qa("", "indriya", 22, ins(IN22)),
    ]
    L += hetu_lines("", 9)
    L += [
        qa("", "ahara", 4, f"{KAB} [वर्तनी-भेद (Sī., Syā.): kabaḷiṃkāro āhāro], {AHARA3}"),
        qa("", "phassa", 7, PHASSA7),
        qa("", "vedana", 7, VEDANA7),
        qa("", "sanna", 7, SANNA7),
        qa("", "cetana", 7, CETANA7),
        qa("", "citta", 7, CITTA7),
    ]
    return L


# ------------------------------------------------------------ 2. Uppattānuppattivāra
KAMA = "इंद्रिय-सुखों के लोक में "
RUPA = "सूक्ष्म भौतिक लोक में "
ARUPA = "अभौतिक लोक में "
APAR = "अस्तित्व के लोकों में न समाई हुई परिघटनाओं में "


def uppatti():
    L = ["#### होने और न होने का खंड", "##### इंद्रिय-सुखों का लोक",
         kati_line(KAMA),
         counts_line(KAMA, [("khandha", 5), ("ayatana", 12), ("dhatu", 18), ("sacca", 3), ("indriya", 22),
                            ("hetu", 9), ("ahara", 4), ("phassa", 7), ("vedana", 7), ("sanna", 7), ("cetana", 7),
                            ("citta", 7)]),
         qa(KAMA, "khandha", 5, K5),
         qa(KAMA, "ayatana", 12, ays(AY_ORDER)),
         qa(KAMA, "dhatu", 18, dhs(DH18)),
         qa(KAMA, "sacca", 3, ", ".join(SACCA[k] for k in ("dukkha", "samudaya", "magga"))),
         qa(KAMA, "indriya", 22, f"{IN['cakkhu']}, {IN['sota']}… {IN['annatavi']}"),
         (f"यहाँ {KAMA}{cnt('hetu', 9)} कौन-से हैं? तीन {KH}, तीन {AKH}, तीन {ABH}… "
          f"ये “{KAMA}{cnt('hetu', 9)}” कहे जाते हैं।"),
         qa(KAMA, "ahara", 4, AHARA4),
         qa(KAMA, "phassa", 7, PHASSA7),
         qa(KAMA, "vedana", 7, VEDANA7),
         qa(KAMA, "sanna", 7, SANNA7),
         qa(KAMA, "cetana", 7, CETANA7),
         qa(KAMA, "citta", 7, CITTA7),
         ]
    # Rūpadhātu
    L += ["##### सूक्ष्म भौतिक लोक",
          kati_short(RUPA, 5),
          counts_line(RUPA, [("khandha", 5), ("ayatana", 6), ("dhatu", 9), ("sacca", 3), ("indriya", 14),
                             ("hetu", 8), ("ahara", 3), ("phassa", 4), ("vedana", 4), ("sanna", 4), ("cetana", 4),
                             ("citta", 4)]),
          qa(RUPA, "khandha", 5, K5),
          qa(RUPA, "ayatana", 6, ays(["cakkhu", "rupa", "sota", "sadda", "mana", "dhamma"])),
          qa(RUPA, "dhatu", 9, dhs(["cakkhu", "rupa", "cakkhuvi", "sota", "sadda", "sotavi", "mano", "dhamma",
                                    "manovi"])),
          qa(RUPA, "sacca", 3, ", ".join(SACCA[k] for k in ("dukkha", "samudaya", "magga"))),
          qa(RUPA, "indriya", 14, ins(["cakkhu", "sota", "mana", "jivita", "somanassa", "upekkha", "saddha", "viriya",
                                       "sati", "samadhi", "panna", "ananna", "anna", "annatavi"])),
          ]
    L += hetu_lines(RUPA, 8, akusala=("lobha", "moha"), closing_quoted=False)
    L += [qa(RUPA, "ahara", 3, AHARA3),
          qa(RUPA, "phassa", 4, ", ".join(PHASSA[b] for b in ("आँख", "कान", "मन के तत्व", "मन की चेतना के तत्व"))),
          (f"यहाँ {RUPA}{cnt('vedana', 4)}… {cnt('sanna', 4)}… {cnt('cetana', 4)}… {cnt('citta', 4)} कौन-से हैं? "
           f"{CITTA_N['आँख']}, {CITTA_N['कान']}, {CITTA_N['mano']}, {CITTA_N['manovi']} {D_} "
           f"ये “{RUPA}{cnt('citta', 4)}” कहे जाते हैं।"),
          ]
    # Arūpadhātu
    L += ["##### अभौतिक लोक",
          f"{ARUPA}{KATI_ALL[0]} हैं… {KATI_ALL[-1]}?",
          counts_line(ARUPA, [("khandha", 4), ("ayatana", 2), ("dhatu", 2), ("sacca", 3), ("indriya", 11),
                              ("hetu", 8), ("ahara", 3), ("phassa", 1), ("vedana", 1), ("sanna", 1), ("cetana", 1),
                              ("citta", 1)]),
          qa(ARUPA, "khandha", 4, K4),
          qa(ARUPA, "ayatana", 2, ays(["mana", "dhamma"])),
          qa(ARUPA, "dhatu", 2, dhs(["manovi", "dhamma"])),
          qa(ARUPA, "sacca", 3, ", ".join(SACCA[k] for k in ("dukkha", "samudaya", "magga"))),
          qa(ARUPA, "indriya", 11, ins(["mana", "jivita", "somanassa", "upekkha", "saddha", "viriya", "sati",
                                        "samadhi", "panna", "anna", "annatavi"])),
          (f"यहाँ {ARUPA}{cnt('hetu', 8)} कौन-से हैं? तीन {KH}, दो {AKH}, तीन {ABH}… "
           f"ये “{ARUPA}{cnt('hetu', 8)}” कहे जाते हैं।"),
          qa(ARUPA, "ahara", 3, AHARA3),
          qa(ARUPA, "phassa", 1, MVDS),
          (f"यहाँ {ARUPA}{cnt('vedana', 1)}… {cnt('sanna', 1)}… {cnt('cetana', 1)}… {cnt('citta', 1)} कौन-सा है? "
           f"{MVD} {D_} यह “{ARUPA}{cnt('citta', 1)}” कहा जाता है।"),
          ]
    # Apariyāpanna
    L += ["##### अस्तित्व के लोकों में न समाया हुआ",
          f"{APAR}{KATI_ALL[0]} हैं… {KATI_ALL[-1]}?",
          counts_line(APAR, [("khandha", 4), ("ayatana", 2), ("dhatu", 2), ("sacca", 2), ("indriya", 12),
                             ("hetu", 6), ("ahara", 3), ("phassa", 1), ("vedana", 1), ("sanna", 1), ("cetana", 1),
                             ("citta", 1)]),
          qa(APAR, "khandha", 4, K4),
          qa(APAR, "ayatana", 2, ays(["mana", "dhamma"])),
          qa(APAR, "dhatu", 2, dhs(["manovi", "dhamma"])),
          qa(APAR, "sacca", 2, ", ".join(SACCA[k] for k in ("magga", "nirodha"))),
          qa(APAR, "indriya", 12, ins(["mana", "jivita", "somanassa", "upekkha", "saddha", "viriya", "sati",
                                       "samadhi", "panna", "ananna", "anna", "annatavi"])),
          ]
    L += hetu_lines(APAR, 6, with_akusala=False,
                    aby_def=(f"{ABY_HETU_Q} हितकर कर्म के फल रूपी परिघटनाओं में लोभ का अभाव, द्वेष का अभाव, "
                             f"मोह का अभाव {D_} ये तीन नैतिक रूप से अनिर्धारित मूल हैं।"))
    L += [qa(APAR, "ahara", 3, AHARA3),
          qa(APAR, "phassa", 1, MVDS),
          (f"यहाँ {APAR}{cnt('vedana', 1)}… {cnt('sanna', 1)}… {cnt('cetana', 1)}… {cnt('citta', 1)} कौन-सा है? "
           f"{MVD} {D_} यह “{APAR}{cnt('citta', 1)}” कहा जाता है।"),
          ]
    return L


# ------------------------------------------------------------ 3. Pariyāpannāpariyāpannavāra
def incl(realm):
    return {"kama": "इंद्रिय-सुखों के लोक में समा{ya} हु{ua}",
            "rupa": "सूक्ष्म भौतिक लोक में समा{ya} हु{ua}",
            "arupa": "अभौतिक लोक में समा{ya} हु{ua}",
            "par": "अस्तित्व के लोकों में समा{ya} हु{ua}"}[realm]


APARIY = "अस्तित्व के लोकों में न समा{ya} हु{ua}"


def kati_pair(p, q, neg_q=True, plural_verb="हैं"):
    """«पाँच समूहों में से कितने P हैं, कितने Q नहीं हैं… सात प्रकार के मन में से कितने P हैं, कितने Q नहीं हैं?»"""
    P = inf(p, "m", "pl")
    Q = inf(q, "m", "pl")
    tail = f"कितने {Q} नहीं हैं" if neg_q else f"कितने {Q} हैं"
    one = lambda who: f"{who} में से कितने {P} हैं, {tail}"
    return f"{one('पाँच समूहों')}… {one('सात प्रकार के मन')}?"


def pariyapanna_realm(realm, heading):
    P = incl(realm)
    neg = [("siyanot", [P])]
    pos_or_not = lambda subj, is_in: parts(subj, [("is", [P])] if is_in else [("not", [P])])
    s = lambda subj: f"{subj.nom} " + parts(subj, [("siya", P)] + neg)
    k = realm == "kama"
    L = [f"##### {heading}", kati_pair(P, P)]
    L.append(f"{RK.nom} {pos_or_not(RK, k)}; {s(C('khandha', 4))}।")
    L.append(f"{C('ayatana', 10).nom} {pos_or_not(C('ayatana', 10), k)}; {s(C('ayatana', 2))}।")
    L.append(f"{C('dhatu', 16).nom} {pos_or_not(C('dhatu', 16), k)}; {s(C('dhatu', 2))}।")
    if k:
        L.append(f"{SAMUDAYA.nom} {pos_or_not(SAMUDAYA, True)}; {C('sacca', 2).nom} {pos_or_not(C('sacca', 2), False)}; "
                 f"{s(DUKKHA)}।")
        L.append(f"{C('indriya', 10).nom} {pos_or_not(C('indriya', 10), True)}; "
                 f"{C('indriya', 3).nom} {pos_or_not(C('indriya', 3), False)}; {s(C('indriya', 9))}।")
    elif realm == "rupa":
        L.append(f"{C('sacca', 3).nom} {pos_or_not(C('sacca', 3), False)}; {s(DUKKHA)}।")
        L.append(f"{C('indriya', 13).nom} {pos_or_not(C('indriya', 13), False)}; {s(C('indriya', 9))}।")
    else:  # arūpa: «Tīṇi saccāni na …pariyāpannāni.» and «Dukkhasaccaṃ siyā …» on separate lines
        L.append(f"{C('sacca', 3).nom} {pos_or_not(C('sacca', 3), False)}।")
        L.append(f"{s(DUKKHA)}।")
        L.append(f"{C('indriya', 14).nom} {pos_or_not(C('indriya', 14), False)}; {s(C('indriya', 8))}।")
    akh = Subj(f"तीन {AKH}", "m", "pl")
    L.append(f"{akh.nom} {pos_or_not(akh, k)}; {s(C('hetu', 6))}।")
    L.append(f"{KABS.nom} {pos_or_not(KABS, k)}; {s(C('ahara', 3))}।")
    L.append(f"{C('phassa', 6).nom} {pos_or_not(C('phassa', 6), k)}; {s(MVDS_S)}।")
    fm = FOUR_MENTAL(6)
    L.append(f"{fm.nom} {pos_or_not(fm, k)}; {s(MVD_S)}।")
    return L


def pariyapanna_par():
    P, Q = incl("par"), APARIY
    s = lambda subj: f"{subj.nom} " + parts(subj, [("siya", P), ("siya", Q)])
    is_ = lambda subj, x: f"{subj.nom} " + parts(subj, [("is", [x])])
    akh = Subj(f"तीन {AKH}", "m", "pl")
    return [
        "##### अस्तित्व के लोकों में समाया हुआ और न समाया हुआ",
        kati_pair(P, Q, neg_q=False),
        f"{is_(RK, P)}; {s(C('khandha', 4))}।",
        f"{is_(C('ayatana', 10), P)}; {s(C('ayatana', 2))}।",
        f"{is_(C('dhatu', 16), P)}; {s(C('dhatu', 2))}।",
        f"{is_(C('sacca', 2), P)}; {is_(C('sacca', 2), Q)}।",
        f"{is_(C('indriya', 10), P)}, {is_(C('indriya', 3), Q)}; {s(C('indriya', 9))}।",
        f"{is_(akh, P)}; {s(C('hetu', 6))}।",
        f"{is_(KABS, P)}; {s(C('ahara', 3))}।",
        f"{is_(C('phassa', 6), P)}; {s(MVDS_S)}।",
        f"{is_(FOUR_MENTAL(6), P)}; {s(MVD_S)}।",
    ]


def pariyapanna():
    L = ["#### समाए हुए और न समाए हुए का खंड"]
    L += pariyapanna_realm("kama", "इंद्रिय-सुखों का लोक")
    L += pariyapanna_realm("rupa", "सूक्ष्म भौतिक लोक")
    L += pariyapanna_realm("arupa", "अभौतिक लोक")
    L += pariyapanna_par()
    return L


# ------------------------------------------------------------ 4. Dhammadassanavāra
KB = "इंद्रिय-सुखों के लोक में जन्म के क्षण में"
RB = "सूक्ष्म भौतिक लोक में जन्म के क्षण में"
AB = "अभौतिक लोक में जन्म के क्षण में"
KAMADEVA = "इंद्रिय-सुखों के लोक के देवताओं"
FIRSTMEN = "कल्प के आरंभ के मनुष्यों"
LOWER = ("स्वतः जन्म लेने वाले प्रेतों, स्वतः जन्म लेने वाले असुरों, स्वतः जन्म लेने वाले पशुओं "
         "और नरक के प्राणियों")
WOMB = "गर्भ में रहने वाले प्राणियों"
ASANNA = "पहचान-रहित देवताओं"


def who(groups, qual=None, extra=""):
    """«<g1>, <g2> और <g3> में से जो <qual> हैं, उनके जन्म के क्षण में» / «<g> के जन्म के क्षण में»"""
    if len(groups) == 1:
        gtxt = groups[0]
    elif " और " in groups[-1]:   # LOWER already ends with «… और नरक के प्राणियों»
        gtxt = ", ".join(groups)
    else:
        gtxt = ", ".join(groups[:-1]) + " और " + groups[-1]
    if qual is None:
        return f"{gtxt} के जन्म के क्षण में"
    return f"{gtxt} में से जो {qual} हैं,{extra} उनके जन्म के क्षण में"


FULL = "पूर्ण इंद्रिय-क्षेत्रों वाले"
BLIND, DEAF, BLINDDEAF = "जन्म से अंधे", "जन्म से बहरे", "जन्म से अंधे और बहरे"
SK = "मूल वाले और ज्ञान से जुड़े"
SV = "मूल वाले और ज्ञान से अलग"
AH = "मूल से रहित"


def kassa(kind, n, whotxt, members, other=False):
    """Kāmadhātuyā upapattikkhaṇe kassa <N X> pātubhavanti? <who> <N X> pātubhavanti – <members>.
    Kāmadhātuyā upapattikkhaṇe etesaṃ imāni <N X> pātubhavanti."""
    g, num = gn(kind, n)
    x = cnt(kind, n)
    q = f"{KB} किसके लिए {cnt(kind, n, other)} {appear(g, num)}?"
    a = f"{whotxt} {x} {appear(g, num)} {D_} {members}।"
    c = f"{KB} इनके लिए {ye(num)} {x} {appear(g, num)}।"
    return f"{q} {a} {c}"


def sabbesam(kind, n, members, loc=KB, all_=True, end_q="?"):
    """<loc> sabbesaṃ katame <N X> pātubhavanti? <members> – <loc> sabbesaṃ ime <N X> pātubhavanti."""
    g, num = gn(kind, n)
    x = cnt(kind, n)
    sb = " सबके लिए" if all_ else ""
    return (f"{loc}{sb} {kaun(g, num)} {x} {appear(g, num)}{end_q} {members} {D_} "
            f"{loc}{sb} {ye(num)} {x} {appear(g, num)}।")


ONE_MIND_Q = f"{cnt('vedana', 1)}… {cnt('sanna', 1)}… {cnt('cetana', 1)}… {cnt('citta', 1)}"


def dhammadassana():
    ap = appear
    L = ["#### परिघटनाओं के प्रकट होने को दिखाने वाला खंड", "##### इंद्रिय-सुखों का लोक",
         f"{KB} {KATI_ALL[0]} {ap('m', 'pl')}… {KATI_ALL[-1]} {ap('m', 'pl')}?"]
    some = lambda kind, n, other=False: f"किसी के लिए {cnt(kind, n, other)} {ap(*gn(kind, n))}"
    allx = lambda kind, n: f"सबके लिए {cnt(kind, n)} {ap(*gn(kind, n))}"
    items = [allx("khandha", 5),
             some("ayatana", 11), some("ayatana", 10), some("ayatana", 10, True), some("ayatana", 9),
             some("ayatana", 7),
             some("dhatu", 11), some("dhatu", 10), some("dhatu", 10, True), some("dhatu", 9), some("dhatu", 7),
             allx("sacca", 1),
             some("indriya", 14), some("indriya", 13), some("indriya", 13, True), some("indriya", 12),
             some("indriya", 10), some("indriya", 9), some("indriya", 9, True), some("indriya", 8),
             some("indriya", 8, True), some("indriya", 7), some("indriya", 5), some("indriya", 4),
             some("hetu", 3), some("hetu", 2),
             f"किसी के लिए [पाठभेद (Syā.): keci] वे {AH} {ap('m', 'pl')}",
             allx("ahara", 4), allx("phassa", 1),
             f"सबके लिए {ONE_MIND_Q} {ap('m', 'sg')}"]
    L.append(f"{KB} " + "; ".join(items) + "।")
    L.append(sabbesam("khandha", 5, f"{KHANDHA[0]}… {KHANDHA[-1]}"))
    # āyatana
    L.append(kassa("ayatana", 11, who([KAMADEVA, FIRSTMEN, LOWER], FULL),
                   ays(["cakkhu", "rupa", "sota", "ghana", "gandha", "jivha", "rasa", "kaya", "photthabba", "mana",
                        "dhamma"])))
    L.append(kassa("ayatana", 10, who([LOWER], BLIND),
                   ays(["rupa", "sota", "ghana", "gandha", "jivha", "rasa", "kaya", "photthabba", "mana", "dhamma"])))
    L.append(kassa("ayatana", 10, who([LOWER], DEAF),
                   ays(["cakkhu", "rupa", "ghana", "gandha", "jivha", "rasa", "kaya", "photthabba", "mana",
                        "dhamma"]), other=True))
    L.append(kassa("ayatana", 9, who([LOWER], BLINDDEAF),
                   ays(["rupa", "ghana", "gandha", "jivha", "rasa", "kaya", "photthabba", "mana", "dhamma"])))
    L.append(kassa("ayatana", 7, who([WOMB]),
                   ays(["rupa", "gandha", "rasa", "kaya", "photthabba", "mana", "dhamma"])))
    # dhātu
    L.append(kassa("dhatu", 11, who([KAMADEVA, FIRSTMEN, LOWER], FULL),
                   dhs(["cakkhu", "rupa", "sota", "ghana", "gandha", "jivha", "rasa", "kaya", "photthabba", "manovi",
                        "dhamma"])))
    L.append(kassa("dhatu", 10, who([LOWER], BLIND),
                   dhs(["rupa", "sota", "ghana", "gandha", "jivha", "rasa", "kaya", "photthabba", "manovi",
                        "dhamma"])))
    L.append(kassa("dhatu", 10, who([LOWER], DEAF),
                   dhs(["cakkhu", "rupa", "ghana", "gandha", "jivha", "rasa", "kaya", "photthabba", "manovi",
                        "dhamma"]), other=True))
    L.append(kassa("dhatu", 9, who([LOWER], BLINDDEAF),
                   dhs(["rupa", "ghana", "gandha", "jivha", "rasa", "kaya", "photthabba", "manovi", "dhamma"])))
    L.append(kassa("dhatu", 7, who([WOMB]),
                   dhs(["rupa", "gandha", "rasa", "kaya", "photthabba", "manovi", "dhamma"])))
    # sacca
    L.append(sabbesam("sacca", 1, SACCA["dukkha"]))
    # indriya
    base6 = ["cakkhu", "sota", "ghana", "jivha", "kaya", "mana"]
    five = ["saddha", "viriya", "sati", "samadhi"]
    L.append(kassa("indriya", 14, who([KAMADEVA], SK), ins(base6 + ["ip", "jivita", "su"] + five + ["panna"])))
    L.append(kassa("indriya", 13, who([KAMADEVA], SV), ins(base6 + ["ip", "jivita", "su"] + five)))
    L.append(kassa("indriya", 13, who([FIRSTMEN], SK), ins(base6 + ["jivita", "su"] + five + ["panna"]), other=True))
    L.append(kassa("indriya", 12, who([FIRSTMEN], SV), ins(base6 + ["jivita", "su"] + five)))
    L.append(kassa("indriya", 10, who([WOMB], SK), ins(["kaya", "mana", "ip", "jivita", "su"] + five + ["panna"])))
    L.append(kassa("indriya", 9, who([WOMB], SV), ins(["kaya", "mana", "ip", "jivita", "su"] + five)))
    L.append(kassa("indriya", 9, who([LOWER], FULL), ins(base6 + ["ip", "jivita", "upekkha"]), other=True))
    L.append(kassa("indriya", 8, who([LOWER], BLIND),
                   ins(["sota", "ghana", "jivha", "kaya", "mana", "ip", "jivita", "upekkha"])))
    L.append(kassa("indriya", 8, who([LOWER], DEAF),
                   ins(["cakkhu", "ghana", "jivha", "kaya", "mana", "ip", "jivita", "upekkha"]), other=True))
    L.append(kassa("indriya", 7, who([LOWER], BLINDDEAF),
                   ins(["ghana", "jivha", "kaya", "mana", "ip", "jivita", "upekkha"])))
    L.append(kassa("indriya", 5, who([WOMB], AH, extra=" नपुंसकों को छोड़कर,"),
                   ins(["kaya", "mana", "ip", "jivita", "upekkha"])))
    L.append(kassa("indriya", 4, who([WOMB], AH + " और नपुंसक"), ins(["kaya", "mana", "jivita", "upekkha"])))
    # hetu
    vh = lambda roots: ", ".join(named(r, VH) for r in roots)
    L.append(kassa("hetu", 3, who([KAMADEVA, FIRSTMEN, WOMB], SK), vh(["alobha", "adosa", "amoha"])))
    L.append(kassa("hetu", 2, who([KAMADEVA, FIRSTMEN, WOMB], SV), vh(["alobha", "adosa"]))
             + f" शेष प्राणियों के लिए [पाठभेद (?): avasesā sattā] वे {AH} {ap('m', 'pl')}।")
    # āhāra, phassa, citta (the Pāli asks the āhāra question with «.»; see notes)
    L.append(sabbesam("ahara", 4, AHARA4))
    L.append(sabbesam("phassa", 1, MVDS))
    L.append(f"{KB} सबके लिए कौन-सी {ONE_MIND_Q} {ap('m', 'sg')}? {MVD} {D_} "
             f"{KB} सबके लिए यह {cnt('citta', 1)} {ap('m', 'sg')}।")
    # Rūpadhātu
    L += ["##### सूक्ष्म भौतिक लोक",
          f"{RB} {KATI_ALL[0]} {ap('m', 'pl')}… {KATI_ALL[-1]} {ap('m', 'pl')}?",
          (f"{RB}, {ASANNA} को छोड़कर, " + ", ".join(
              f"{cnt(k, n)} {ap(*gn(k, n))}" for k, n in
              [("khandha", 5), ("ayatana", 5), ("dhatu", 5), ("sacca", 1), ("indriya", 10), ("hetu", 3),
               ("ahara", 3), ("phassa", 1)]) + f", {ONE_MIND_Q} {ap('m', 'sg')}।"),
          sabbesam("khandha", 5, K5, loc=RB, all_=False),
          sabbesam("ayatana", 5, ays(["cakkhu", "rupa", "sota", "mana", "dhamma"]), loc=RB, all_=False),
          sabbesam("dhatu", 5, dhs(["cakkhu", "rupa", "sota", "manovi", "dhamma"]), loc=RB, all_=False),
          sabbesam("sacca", 1, SACCA["dukkha"], loc=RB, all_=False),
          sabbesam("indriya", 10, ins(["cakkhu", "sota", "mana", "jivita", "su"] + five + ["panna"]), loc=RB,
                   all_=False),
          sabbesam("hetu", 3, vh(["alobha", "adosa", "amoha"]), loc=RB, all_=False),
          sabbesam("ahara", 3, AHARA3, loc=RB, all_=False),
          sabbesam("phassa", 1, MVDS, loc=RB, all_=False),
          (f"{RB} कौन-सी {ONE_MIND_Q} {ap('m', 'sg')}? {MVD} {D_} {RB} यह {cnt('citta', 1)} {ap('m', 'sg')}।"),
          ]
    # Asaññasattā
    AS = f"{ASANNA} के जन्म के क्षण में"
    L += ["##### पहचान-रहित प्राणी",
          f"{AS} {KATI_ALL[0]} {ap('m', 'pl')}… {KATI_ALL[-1]} {ap('m', 'pl')}?",
          (f"{AS} {cnt('khandha', 1)} {ap('m', 'sg')} {D_} {KHANDHA[0]}; "
           f"{cnt('ayatana', 2)} {ap('m', 'pl')} {D_} {ays(['rupa', 'dhamma'])}; "
           f"{cnt('dhatu', 2)} {ap('m', 'pl')} {D_} {dhs(['rupa', 'dhamma'])}; "
           f"{cnt('sacca', 1)} {ap('m', 'sg')} {D_} {SACCA['dukkha']}; "
           f"{cnt('indriya', 1)} {ap('f', 'sg')} {D_} भौतिक जीवन-क्षमता। "
           f"पहचान-रहित देवता मूल से रहित, आहार से रहित, संपर्क से रहित, अनुभूति से रहित, पहचान से रहित, "
           f"इरादे से रहित और मन से रहित {ap('m', 'pl')}।"),
          ]
    # Arūpadhātu
    L += ["##### अभौतिक लोक",
          f"{AB} {KATI_ALL[0]} {ap('m', 'pl')}… {KATI_ALL[-1]} {ap('m', 'pl')}?",
          (f"{AB} " + ", ".join(
              f"{cnt(k, n)} {ap(*gn(k, n))}" for k, n in
              [("khandha", 4), ("ayatana", 2), ("dhatu", 2), ("sacca", 1), ("indriya", 8), ("hetu", 3),
               ("ahara", 3), ("phassa", 1)]) + f", {ONE_MIND_Q} {ap('m', 'sg')}।"),
          sabbesam("khandha", 4, K4, loc=AB, all_=False),
          sabbesam("ayatana", 2, ays(["mana", "dhamma"]), loc=AB, all_=False),
          sabbesam("dhatu", 2, dhs(["manovi", "dhamma"]), loc=AB, all_=False),
          sabbesam("sacca", 1, SACCA["dukkha"], loc=AB, all_=False),
          sabbesam("indriya", 8, ins(["mana", "jivita", "upekkha"] + five + ["panna"]), loc=AB, all_=False),
          sabbesam("hetu", 3, vh(["alobha", "adosa", "amoha"]), loc=AB, all_=False),
          sabbesam("ahara", 3, AHARA3, loc=AB, all_=False),
          sabbesam("phassa", 1, MVDS, loc=AB, all_=False),
          (f"{AB} कौन-सी {ONE_MIND_Q} {ap('m', 'sg')}? {MVD} {D_} {AB} यह {cnt('citta', 1)} {ap('m', 'sg')}।"),
          ]
    return L


# ------------------------------------------------------------ 5. Bhūmantaradassanavāra (pi-1 ^1-1287 … ^1-1294)
def bhumantara():
    p1287 = pi1_line("1-1287").replace("इंद्रिय-क्षेत्र, भौतिक रूप", "इंद्रिय-क्षेत्र; भौतिक रूप")
    p1293 = pi1_line("1-1293").replace("भौतिक रूप का समूह… चेतना का समूह", K5)
    assert ";" in p1287 and K5 in p1293
    return [
        "#### अस्तित्व के स्तरों के भेद को दिखाने वाला खंड",
        ", ".join(["इंद्रिय-सुखों के लोक से संबंधित परिघटनाएँ", "इंद्रिय-सुखों के लोक से संबंधित न होने वाली परिघटनाएँ",
                   "सूक्ष्म भौतिक लोक से संबंधित परिघटनाएँ", "सूक्ष्म भौतिक लोक से संबंधित न होने वाली परिघटनाएँ",
                   "अभौतिक लोक से संबंधित परिघटनाएँ", "अभौतिक लोक से संबंधित न होने वाली परिघटनाएँ",
                   "अस्तित्व के लोकों में समाई हुई परिघटनाएँ", "अस्तित्व के लोकों में न समाई हुई परिघटनाएँ"]) + "।",
        p1287, pi1_line("1-1288"), pi1_line("1-1289"), pi1_line("1-1290"), pi1_line("1-1291"), pi1_line("1-1292"),
        p1293, pi1_line("1-1294"),
    ]


# ------------------------------------------------------------ 6. Uppādakakamma / Āyuppamāṇa
DEV = {  # pi-5 10-dutiyavaggo ^… deva list; paranimmitavasavattī from pi-1 ^1-1287
    "catu": "चार महाराजाओं के देवताओं", "tava": "तैंतीस देवताओं", "yama": "याम देवताओं", "tusita": "तुषित देवताओं",
    "nimm": "सृजन में आनंद लेने वाले देवताओं", "para": "दूसरों की रची गई चीज़ों पर अधिकार रखने वाले देवताओं",
    "parisajja": "ब्रह्मा की सभा के देवताओं", "purohita": "ब्रह्मा के पुरोहित देवताओं", "maha": "महाब्रह्मा देवताओं",
    "parittabha": "सीमित आभा वाले देवताओं", "appamanabha": "असीम आभा वाले देवताओं",
    "abhassara": "दीप्तिमान आभा वाले देवताओं", "parittasubha": "सीमित शोभा वाले देवताओं",
    "appamanasubha": "असीम शोभा वाले देवताओं", "subhakinha": "पूर्ण शोभा वाले देवताओं",
    "asanna": ASANNA, "vehapphala": "महान फल वाले देवताओं", "aviha": "अपने लोक से न डिगने वाले देवताओं",
    "atappa": "न तपने वाले देवताओं", "sudassa": "सुंदर दिखने वाले देवताओं", "sudassi": "सुंदर देखने वाले देवताओं",
    "akanittha": "सबसे ऊँचे अकनिष्ठ देवताओं",
    "akasa": "अनंत आकाश के क्षेत्र में पहुँचे देवताओं", "vinnana": "अनंत चेतना के क्षेत्र में पहुँचे देवताओं",
    "akinc": "कुछ भी न होने के क्षेत्र में पहुँचे देवताओं",
    "nevasanna": "न पहचान, न अ-पहचान के क्षेत्र में पहुँचे देवताओं",
}
GIFT = "दान देकर, सदाचार ग्रहण करके, उपवास-व्रत का पालन करके"


def among(x):
    return f"कुछ लोग {x} के बीच जन्म लेते हैं"


def life(key, human_years, divine, human_count, rest_short=False):
    d = DEV[key]
    return (f"{d} की आयु की अवधि कितनी है? मनुष्यों के जो {human_years} हैं, वह {d} का एक दिन-रात है। "
            f"उस रात से तीस रातों का एक महीना होता है। उस महीने से बारह महीनों का एक वर्ष होता है। "
            f"उस वर्ष से {divine} {d} की आयु की अवधि है। मनुष्यों की गणना से यह कितना होता है? {human_count}।")


def jhana_life(ordinal, grade, key, span):
    q = f"{ordinal} ध्यान का {grade} रूप में अभ्यास करके"
    return (f"{q} कहाँ जन्म लेते हैं? {q} {DEV[key]} के बीच जन्म लेते हैं। "
            f"उनकी आयु की अवधि कितनी है? {span}।")


def span_line(key, span, plus=None):
    who_ = DEV[key] if plus is None else f"{DEV[key][:-len(' देवताओं')]} और {DEV[plus]}"
    return f"{who_} की आयु की अवधि कितनी है? {span}।"


def uppadaka():
    L = ["#### जन्म देने वाले कर्म और आयु की अवधि का खंड", "##### जन्म देने वाला कर्म",
         (f"“देवता”। देवता तीन प्रकार के हैं {D_} लोक-मान्यता से देवता [वर्तनी-भेद (Syā.): sammatidevā], "
          f"जन्म से देवता, शुद्धि से देवता।"),
         f"लोक-मान्यता से देवता {D_} राजा, रानियाँ, राजकुमार।",
         (f"जन्म से देवता {D_} चार महाराजाओं के देवताओं [वर्तनी-भेद (Sī., Syā.): cātummahārājike] से लेकर "
          f"उनसे ऊपर के देवता।"),
         f"शुद्धि से देवता {D_} अर्हत् कहे जाते हैं।",
         (f"{GIFT} लोग कहाँ जन्म लेते हैं? {GIFT} " + ", ".join(
             [among("धनी क्षत्रियों"), among("धनी ब्राह्मणों"), among("धनी गृहस्थों")]
             + [among(DEV[k]) for k in ("catu", "tava", "yama", "tusita", "nimm", "para")]) + "।"),
         "##### आयु की अवधि",
         ("मनुष्यों की आयु की अवधि कितनी है? सौ वर्ष या उससे थोड़ा अधिक "
          "[पाठभेद (Syā., Ka.): appaṃ vā bhiyyo vā; दीघ निकाय 2.7]।"),
         (f"{DEV['catu']} की आयु की अवधि कितनी है? मनुष्यों के जो पचास वर्ष हैं, वह {DEV['catu']} का एक दिन-रात है "
          f"[वर्तनी-भेद (Ka.): rattidivo; अंगुत्तर निकाय 3.71]। उस रात से तीस रातों का एक महीना होता है। "
          f"उस महीने से बारह महीनों का एक वर्ष होता है। उस वर्ष से दिव्य पाँच सौ वर्ष {DEV['catu']} की आयु की अवधि है। "
          f"मनुष्यों की गणना से यह कितना होता है? नब्बे लाख वर्ष।"),
         life("tava", "सौ वर्ष", "दिव्य एक हज़ार वर्ष", "तीन करोड़ और साठ लाख वर्ष"),
         life("yama", "दो सौ वर्ष", "दिव्य दो हज़ार वर्ष", "चौदह करोड़ और चालीस लाख वर्ष"),
         life("tusita", "चार सौ वर्ष", "दिव्य चार हज़ार वर्ष", "सत्तावन करोड़ और साठ लाख वर्ष"),
         life("nimm", "आठ सौ वर्ष", "दिव्य आठ हज़ार वर्ष", "दो सौ तीस करोड़ और चालीस लाख वर्ष"),
         life("para", "सोलह सौ वर्ष", "दिव्य सोलह हज़ार वर्ष", "नौ सौ इक्कीस करोड़ और साठ लाख वर्ष"),
         "इंद्रिय-सुखों के लोक के ये छह [पाठभेद (Syā.): chapi te] देवलोक, जो सभी इंद्रिय-सुखों से भरपूर हैं;",
         "उन सबकी आयु एक साथ गिनी जाए तो कितनी होती है?",
         "उनकी आयु बारह सौ करोड़ और अट्ठाईस करोड़,",
         "और पचास लाख वर्ष की गिनती में बताई गई है।",
         jhana_life("पहले", "सीमित", "parisajja", "कल्प का तीसरा भाग"),
         jhana_life("पहले", "मध्यम", "purohita", "आधा कल्प"),
         jhana_life("पहले", "उत्तम", "maha", "एक कल्प [पाठभेद (Syā.): eko kappo]"),
         jhana_life("दूसरे", "सीमित", "parittabha", "दो कल्प"),
         jhana_life("दूसरे", "मध्यम", "appamanabha", "चार कल्प"),
         jhana_life("दूसरे", "उत्तम", "abhassara", "आठ कल्प"),
         jhana_life("तीसरे", "सीमित", "parittasubha", "सोलह कल्प"),
         jhana_life("तीसरे", "मध्यम", "appamanasubha", "बत्तीस कल्प"),
         jhana_life("तीसरे", "उत्तम", "subhakinha", "चौंसठ कल्प"),
         ("चौथे ध्यान का अभ्यास करके, विषय की भिन्नता से, मनोयोग की भिन्नता से, चाह की भिन्नता से, "
          "आकांक्षा की भिन्नता से, निश्चय की भिन्नता से, मन को लक्ष्य की ओर मोड़ने की भिन्नता से, प्रज्ञा की भिन्नता से "
          + ", ".join(among(DEV[k]) for k in ("asanna", "vehapphala", "aviha", "atappa", "sudassa", "sudassi",
                                                "akanittha", "akasa", "vinnana", "akinc", "nevasanna")) + "।"),
         span_line("asanna", "पाँच सौ कल्प", plus="vehapphala"),
         span_line("aviha", "एक हज़ार कल्प"),
         span_line("atappa", "दो हज़ार कल्प"),
         span_line("sudassa", "चार हज़ार कल्प"),
         span_line("sudassi", "आठ हज़ार कल्प"),
         span_line("akanittha", "सोलह हज़ार कल्प"),
         span_line("akasa", "बीस हज़ार कल्प"),
         span_line("vinnana", "चालीस हज़ार कल्प"),
         span_line("akinc", "साठ हज़ार कल्प"),
         span_line("nevasanna", "चौरासी हज़ार कल्प"),
         "पुण्य के तेज से ऊपर उठकर वे इंद्रिय-सुखों के लोक और सूक्ष्म भौतिक लोक की गति को प्राप्त होते हैं।",
         ("अस्तित्व के शिखर [पाठभेद (Syā.): bhavaggaṃ vāpi] तक पहुँचकर भी वे फिर दुर्गति में लौट आते हैं "
          "[वर्तनी-भेद (Syā.): puna gacchanti]।"),
         "इतनी लंबी आयु वाले प्राणी भी आयु का क्षय होने पर मर जाते हैं;",
         "कोई भी अस्तित्व नित्य नहीं है, ऐसा महान ऋषि ने कहा है।",
         "इसलिए धीर, विवेकी, कुशल और अर्थ पर चिंतन करने वाले लोग",
         "बुढ़ापे और मृत्यु से मुक्ति के लिए उत्तम मार्ग का अभ्यास करते हैं।",
         "निर्वाण में डुबकी लगाने की ओर ले जाने वाले शुद्ध मार्ग का अभ्यास करके,",
         "मन के सभी मैलों को पूरी तरह समझकर, वे मन के मैलों से रहित होकर पूर्ण निर्वाण पाते हैं।",
         ]
    return L


# ------------------------------------------------------------ 7. Abhiññeyyādivāra
A_, P_, H_, B_, X_ = ("प्रत्यक्ष जानने योग्य", "पूरी तरह समझे जाने योग्य", "छोड़े जाने योग्य",
                      "विकसित किए जाने योग्य", "साक्षात्कार करने योग्य")
AP = ("is", [A_, P_])
NOT3 = ("not", [H_, B_, X_])
SIYA4 = [("siya", H_), ("siya", B_), ("siya", X_), ("siyanot", [H_, B_, X_])]


def kati_abhi():
    one = (lambda who_: f"{who_} में से कितने {A_} हैं, कितने {P_}, कितने {H_}, कितने {B_}, कितने {X_}, "
                        f"कितने न {H_}, न {B_}, न {X_}")
    return f"{one('पाँच समूहों')}… {one('सात प्रकार के मन')}?"


def abhinneyya():
    akh = Subj(f"तीन {AKH}", "m", "pl")
    kh = Subj(f"तीन {KH}", "m", "pl")
    abh = Subj(f"तीन {ABH}", "m", "pl")
    L = ["#### प्रत्यक्ष जानने योग्य आदि का खंड",
         kati_abhi(),
         sent(RK, [AP, NOT3]) + " " + sent(C("khandha", 4), [AP] + SIYA4),
         sent(C("ayatana", 10), [AP, NOT3]) + " " + sent(C("ayatana", 2), [AP] + SIYA4),
         sent(C("dhatu", 16), [AP, NOT3]) + " " + sent(C("dhatu", 2), [AP] + SIYA4),
         " ".join([sent(SAMUDAYA, [("is", [A_, P_, H_]), ("not", [B_, X_])]),
                   sent(MAGGA, [AP, ("not", [H_]), ("is", [B_]), ("not", [X_])]),
                   sent(NIRODHA, [AP, ("not", [H_, B_]), ("is", [X_])]),
                   sent(DUKKHA, [AP, ("siya", H_), ("not", [B_]), ("not", [X_]), ("siyanot", [H_])])]),
         " ".join([sent(C("indriya", 9), [AP, NOT3]),
                   sent(DOMAN, [("is", [A_, P_, H_]), ("not", [B_, X_])]),
                   sent(ANANNA, [AP, ("not", [H_]), ("is", [B_]), ("not", [X_])]),
                   sent(ANNA, [AP, ("not", [H_]), ("siya", B_), ("siya", X_)]),
                   sent(ANNATAVI, [AP, ("not", [H_, B_]), ("is", [X_])]),
                   sent(C("indriya", 3), [AP, ("not", [H_]), ("siya", B_), ("siya", X_), ("siyanotbut", (B_, X_))]),
                   sent(C("indriya", 6), [AP] + SIYA4)]),
         " ".join([sent(akh, [("is", [A_, P_, H_]), ("not", [B_, X_])]),
                   sent(kh, [AP, ("not", [H_]), ("siya", B_), ("not", [X_]), ("siyanot", [B_])]),
                   sent(abh, [AP, ("not", [H_, B_]), ("siya", X_), ("siyanot", [X_])])]),
         sent(KABS, [AP, NOT3]) + " " + sent(C("ahara", 3), [AP] + SIYA4),
         sent(C("phassa", 6), [AP, NOT3]) + " " + sent(MVDS_S, [AP] + SIYA4),
         sent(FOUR_MENTAL(6), [AP, NOT3]) + " " + sent(MVD_S, [AP] + SIYA4),
         ]
    return L


# ------------------------------------------------------------ 8. Sārammaṇānārammaṇavāra
SAR, ANAR = "विषय वाल{a}", "विषय से रहित"
SARAR, ANARAR = "विषय वाली परिघटनाओं को विषय बनाने वाल{a}", "विषय से रहित परिघटनाओं को विषय बनाने वाल{a}"


def is1(subj, p):
    return sent(subj, [("is", [p])])


def siya(subj, *ps):
    return sent(subj, [("siya", p) for p in ps])


def kati2(p, q):
    one = lambda who_: f"{who_} में से कितने {inf(p, 'm', 'pl')} हैं, कितने {inf(q, 'm', 'pl')}"
    return f"{one('पाँच समूहों')}… {one('सात प्रकार के मन')}?"


def sarammana():
    seven = FOUR_MENTAL(7)
    seven_ph = Subj(f"{cnt('phassa', 7)}… " + seven.nom, "m", "pl")
    L = ["#### विषय वाले और विषय से रहित का खंड",
         kati2(SAR, ANAR),
         is1(RK, ANAR) + " " + is1(C("khandha", 4), SAR),
         " ".join([is1(C("ayatana", 10), ANAR), is1(MANAY, SAR), siya(DHAMMAY, SAR, ANAR)]),
         " ".join([is1(C("dhatu", 10), ANAR), is1(C("dhatu", 7), SAR), siya(DHD, SAR, ANAR)]),
         " ".join([is1(C("sacca", 2), SAR), is1(NIRODHA, ANAR), siya(DUKKHA, SAR, ANAR)]),
         " ".join([is1(C("indriya", 7), ANAR), is1(C("indriya", 14), SAR), siya(JIVITA, SAR, ANAR),
                   is1(C("hetu", 9), SAR), is1(KABS, ANAR), is1(C("ahara", 3), SAR), is1(seven_ph, SAR)]),
         kati2(SARAR, ANARAR),
         is1(RK, ANAR) + " " + siya(C("khandha", 4), SARAR, ANARAR),
         " ".join([is1(C("ayatana", 10), ANAR), siya(MANAY, SARAR, ANARAR), siya(DHAMMAY, SARAR, ANARAR, ANAR)]),
         " ".join([is1(C("dhatu", 10), ANAR), is1(C("dhatu", 6), ANARAR), siya(MVD_S, SARAR, ANARAR),
                   siya(DHD, SARAR, ANARAR, ANAR)]),
         " ".join([is1(NIRODHA, ANAR), is1(MAGGA, ANARAR), siya(SAMUDAYA, SARAR, ANARAR),
                   siya(DUKKHA, SARAR, ANARAR, ANAR)]),
         " ".join([is1(C("indriya", 7), ANAR), is1(C("indriya", 5), ANARAR), siya(C("indriya", 9), SARAR, ANARAR),
                   siya(JIVITA, SARAR, ANARAR, ANAR)]),
         " ".join([siya(C("hetu", 9), SARAR, ANARAR), is1(KABS, ANAR), siya(C("ahara", 3), SARAR, ANARAR),
                   is1(C("phassa", 6), ANARAR), siya(MVDS_S, SARAR, ANARAR),
                   is1(Subj(" ".join([cnt('vedana', 6) + "…", cnt('sanna', 6) + "…", cnt('cetana', 6) + "…",
                                      cnt('citta', 6)]), "m", "pl"), ANARAR),
                   siya(MVD_S, SARAR, ANARAR)]),
         ]
    return L


# ------------------------------------------------------------ 9. Diṭṭhasutādidassanavāra
DS = ["देख{a} हु{ua}", "सुन{a} हु{ua}", "अनुभव {kiya} हु{ua}", "जान{a} हु{ua}"]


def dsv(subj, flags):
    """flags for diṭṭha, suta, muta, viññāta (viññāta is always positive here)"""
    g, n = subj.g, subj.n
    words = [inf(w, g, n) for w in DS]
    out = []
    for i, (w, f) in enumerate(zip(words, flags)):
        t = w if f else "न " + w
        if i == 3:
            t = ("पर " if not flags[2] else "और ") + t
        out.append(t)
    s = ", ".join(out[:3]) + (", " if not flags[2] else " ") + out[3]
    return f"{subj.nom} {s} {'हैं' if n == 'pl' else 'है'}।"


def dsv_siya(subj):
    g, n = subj.g, subj.n
    w = [inf(x, g, n) for x in DS]
    h = {"m": {"sg": "होता है", "pl": "होते हैं"}, "f": {"sg": "होती है", "pl": "होती हैं"}}[g][n]
    return (f"{subj.nom} कभी {w[0]} {h}, कभी {w[1]} {h}, कभी {w[2]} {h}, कभी {w[3]} {h}, "
            f"कभी न {w[0]}, न {w[1]}, न {w[2]}, पर {w[3]} {h}।")


def kati_ds():
    w = [inf(x, "m", "pl") for x in DS]
    one = (lambda who_: f"{who_} में से कितने {w[0]} हैं, कितने {w[1]}, कितने {w[2]}, कितने {w[3]}, "
                        f"कितने न {w[0]}, न {w[1]}, न {w[2]}, न {w[3]}")
    return f"{one('पाँच समूहों')}… {one('सात प्रकार के मन')}?"


def dittha():
    N4 = (0, 0, 0, 1)
    return ["#### देखे, सुने आदि को दिखाने वाला खंड",
            kati_ds(),
            dsv_siya(RK) + " " + dsv(C("khandha", 4), N4),
            " ".join([dsv(RUPAY, (1, 0, 0, 1)), dsv(SADDAY, (0, 1, 0, 1)), dsv(GRP_AY, (0, 0, 1, 1)),
                      dsv(C("ayatana", 7), N4)]),
            " ".join([dsv(RUPAD, (1, 0, 0, 1)), dsv(SADDAD, (0, 1, 0, 1)), dsv(GRP_D, (0, 0, 1, 1)),
                      dsv(C("dhatu", 13), N4)]),
            dsv(C("sacca", 3), N4) + " " + dsv_siya(DUKKHA),
            " ".join([dsv(C("indriya", 22), N4), dsv(C("hetu", 9), N4), dsv(C("ahara", 4), N4),
                      dsv(C("phassa", 7), N4), dsv(FOUR_MENTAL(7), N4)]),
            ]


# ------------------------------------------------------------ 10. Tikādidassanavāra
K_, AK_, ABY_ = "हितकर", "हानिकर", "नैतिक रूप से अनिर्धारित"
VS, VD_, VA = "सुखद अनुभूति से जुड़{a}", "दुःखद अनुभूति से जुड़{a}", "न दुःखद, न सुखद अनुभूति से जुड़{a}"
VDM = "दुःखद-असुखद अनुभूति से जुड़{a}"   # Pāli «dukkhamasukhāya» (sic) at ^2-1039, translated as written
NV3 = [VS, VD_, VA]
VP, VPD, NVP = "कर्म-फल रूपी", "कर्म-फल उत्पन्न करने वाल{a}", "न कर्म-फल रूपी, न कर्म-फल उत्पन्न करने वाल{a}"
U1 = "कर्म से उत्पन्न और आसक्ति का विषय बनने वाल{a}"
U2 = "कर्म से उत्पन्न न होकर भी आसक्ति का विषय बनने वाल{a}"
U3 = "न कर्म से उत्पन्न, न आसक्ति का विषय बनने वाल{a}"
T1 = "आरंभिक विचार और सतत विचार वाल{a}"
T2 = "आरंभिक विचार से रहित, केवल सतत विचार वाल{a}"
T3 = "आरंभिक विचार और सतत विचार दोनों से रहित"


def kati3(ps):
    w = [inf(p, "m", "pl") for p in ps]
    one = lambda who_: f"{who_} में से कितने {w[0]} हैं, " + ", ".join(f"कितने {x}" for x in w[1:])
    return f"{one('पाँच समूहों')}… {one('सात प्रकार के मन')}?"


def nvs(subj, ps=NV3):
    return nv(subj, ps) + "।"


def siya_nv(subj, ps, nvps):
    return f"{subj.nom} " + parts(subj, [("siya", p) for p in ps] + [("siyanv", nvps)]) + "।"


def tika():
    akh = Subj(f"तीन {AKH}", "m", "pl")
    kh = Subj(f"तीन {KH}", "m", "pl")
    abh = Subj(f"तीन {ABH}", "m", "pl")
    L = ["#### तीन-तीन आदि के वर्गीकरणों को दिखाने वाला खंड",
         "##### हितकर आदि का तीन-तीन वर्गीकरण",
         kati3([K_, AK_, ABY_]),
         " ".join([is1(RK, ABY_), siya(C("khandha", 4), K_, AK_, ABY_), is1(C("ayatana", 10), ABY_),
                   siya(C("ayatana", 2), K_, AK_, ABY_), is1(C("dhatu", 16), ABY_), siya(C("dhatu", 2), K_, AK_, ABY_),
                   is1(SAMUDAYA, AK_), is1(MAGGA, K_), is1(NIRODHA, ABY_), siya(DUKKHA, K_, AK_, ABY_)]),
         " ".join([is1(C("indriya", 10), ABY_), is1(DOMAN, AK_), is1(ANANNA, K_), siya(C("indriya", 4), K_, ABY_),
                   siya(C("indriya", 6), K_, AK_, ABY_)]),
         " ".join([is1(kh, K_), is1(akh, AK_), is1(abh, ABY_), is1(KABS, ABY_), siya(C("ahara", 3), K_, AK_, ABY_),
                   is1(C("phassa", 6), ABY_), siya(MVDS_S, K_, AK_, ABY_), is1(FOUR_MENTAL(6), ABY_),
                   siya(MVD_S, K_, AK_, ABY_)]),
         "##### अनुभूति का तीन-तीन वर्गीकरण",
         kati3(NV3),
         nvs(C("khandha", 2)) + " " + siya(C("khandha", 3), *NV3),
         " ".join([nvs(C("ayatana", 10)), siya(MANAY, *NV3), siya_nv(DHAMMAY, NV3, NV3)]),
         " ".join([nvs(C("dhatu", 10)),
                   is1(C("dhatu", 5), VA)[:-1] + ", " + siya(KVD, VS, VD_),
                   siya(MVD_S, *NV3), siya_nv(DHD, NV3, NV3)]),
         " ".join([siya(C("sacca", 2), VS, VA), nvs(NIRODHA), siya_nv(DUKKHA, NV3, NV3)]),
         " ".join([nvs(C("indriya", 12)), siya(C("indriya", 6), VS, VA), siya(C("indriya", 3), *NV3),
                   siya_nv(JIVITA, NV3, NV3)]),
         " ".join([is1(DOSO, VD_), siya(C("hetu", 7), VS, VA), siya(MOHO, VS, VD_, VDM)]),
         nvs(KABS) + " " + siya(C("ahara", 3), *NV3),
         " ".join([is1(C("phassa", 5), VA), siya(KVDS_S, VS, VD_), siya(MVDS_S, *NV3)]),
         " ".join([nvs(C("vedana", 7)),
                   is1(FOUR_MENTAL_NO_VED(5), VA)[:-1] + ", " + siya(KVD, VS, VD_),
                   siya(MVD_S, *NV3)]),
         "##### कर्म-फल का तीन-तीन वर्गीकरण",
         kati3([VP, VPD, NVP]),
         is1(RK, NVP) + " " + siya(C("khandha", 4), VP, VPD, NVP),
         is1(C("ayatana", 10), NVP) + " " + siya(C("ayatana", 2), VP, VPD, NVP),
         " ".join([is1(C("dhatu", 10), NVP), is1(C("dhatu", 5), VP), siya(MANOD, VP, NVP),
                   siya(C("dhatu", 2), VP, VPD, NVP)]),
         " ".join([is1(C("sacca", 2), VPD), is1(NIRODHA, NVP), siya(DUKKHA, VP, VPD, NVP)]),
         " ".join([is1(C("indriya", 7), NVP), is1(C("indriya", 3), VP), is1(C("indriya", 2), VPD),
                   siya(ANNA, VP, VPD), siya(C("indriya", 9), VP, VPD, NVP)]),
         is1(C("hetu", 6), VPD) + " " + siya(abh, VP, NVP),
         " ".join([is1(KABS, NVP), siya(C("ahara", 3), VP, VPD, NVP), is1(C("phassa", 5), VP),
                   siya(MDS_S, VP, NVP), siya(MVDS_S, VP, VPD, NVP), is1(FOUR_MENTAL(5), VP),
                   siya(MANOD, VP, NVP), siya(MVD_S, VP, VPD, NVP)]),
         "##### कर्म से उत्पन्न का तीन-तीन वर्गीकरण",
         kati3([U1, U2, U3]),
         siya(RK, U1, U2)[:-1] + " 4। " + siya(C("khandha", 4), U1, U2, U3),
         " ".join([is1(C("ayatana", 5), U1), is1(SADDAY, U2), siya(C("ayatana", 4), U1, U2),
                   siya(C("ayatana", 2), U1, U2, U3)]),
         " ".join([is1(C("dhatu", 10), U1), is1(SADDAD, U2), siya(C("dhatu", 5), U1, U2),
                   siya(C("dhatu", 2), U1, U2, U3)]),
         " ".join([is1(SAMUDAYA, U2), is1(C("sacca", 2), U3), siya(DUKKHA, U1, U2)]),
         " ".join([is1(C("indriya", 9), U1), is1(DOMAN, U2), is1(C("indriya", 3), U3),
                   siya(C("indriya", 9), U1, U2, U3), is1(akh, U2), siya(kh, U2, U3), siya(abh, U1, U2, U3)]),
         siya(KABS, U1, U2) + " " + siya(C("ahara", 3), U1, U2, U3),
         " ".join([is1(C("phassa", 5), U1), siya(MDS_S, U1, U2), siya(MVDS_S, U1, U2, U3),
                   is1(FOUR_MENTAL(5), U1), siya(MANOD, U1, U2), siya(MVD_S, U1, U2, U3)]),
         "##### आरंभिक विचार का तीन-तीन वर्गीकरण",
         kati3([T1, T2, T3]),
         " ".join([is1(RK, T3), siya(C("khandha", 3), T1, T2, T3), siya_nv(SANKHARAK, [T1, T2, T3], [T1, T2, T3])]),
         " ".join([is1(C("ayatana", 10), T3), siya(MANAY, T1, T2, T3), siya_nv(DHAMMAY, [T1, T2, T3], [T1, T2, T3])]),
         " ".join([is1(C("dhatu", 15), T3), is1(MANOD, T1), siya(MVD_S, T1, T2, T3),
                   siya_nv(DHD, [T1, T2, T3], [T1, T2, T3])]),
         " ".join([is1(SAMUDAYA, T1), is1(NIRODHA, T3), siya(MAGGA, T1, T2, T3),
                   siya_nv(DUKKHA, [T1, T2, T3], [T1, T2, T3])]),
         " ".join([is1(C("indriya", 9), T3), is1(DOMAN, T1), siya(UPEKKHA, T1, T3), siya(C("indriya", 11), T1, T2, T3)]),
         " ".join([is1(akh, T1), siya(C("hetu", 6), T1, T2, T3), is1(KABS, T3), siya(C("ahara", 3), T1, T2, T3),
                   is1(C("phassa", 5), T3), is1(MDS_S, T1), siya(MVDS_S, T1, T2, T3),
                   is1(FOUR_MENTAL(5), T3)[:-1] + ", " + is1(MANOD, T1)[:-1] + ", " + siya(MVD_S, T1, T2, T3)]),
         "##### (1) भौतिक का दो-दो वर्गीकरण",
         kati3(["भौतिक", "अभौतिक"]),
         " ".join([is1(RK, "भौतिक"), is1(C("khandha", 4), "अभौतिक"), is1(C("ayatana", 10), "भौतिक"),
                   is1(MANAY, "अभौतिक"), siya(DHAMMAY, "भौतिक", "अभौतिक"), is1(C("dhatu", 10), "भौतिक"),
                   is1(C("dhatu", 7), "अभौतिक"), siya(DHD, "भौतिक", "अभौतिक"), is1(C("sacca", 3), "अभौतिक"),
                   siya(DUKKHA, "भौतिक", "अभौतिक"), is1(C("indriya", 7), "भौतिक"), is1(C("indriya", 14), "अभौतिक"),
                   siya(JIVITA, "भौतिक", "अभौतिक"), is1(C("hetu", 9), "अभौतिक"), is1(KABS, "भौतिक"),
                   is1(C("ahara", 3), "अभौतिक"), is1(C("phassa", 7), "अभौतिक"), is1(FOUR_MENTAL(7), "अभौतिक")]),
         "##### (2) लौकिक का दो-दो वर्गीकरण",
         " ".join(f"{w} में से कितने लौकिक हैं, कितने लोकोत्तर?" for w in
                  ("पाँच समूहों", "बारह इंद्रिय-क्षेत्रों", "अठारह तत्वों"))
         + " चार सत्यों में से कितने लौकिक हैं, कितने लोकोत्तर… सात प्रकार के मन में से कितने लौकिक हैं, कितने लोकोत्तर?",
         " ".join([is1(RK, "लौकिक"), siya(C("khandha", 4), "लौकिक", "लोकोत्तर"), is1(C("ayatana", 10), "लौकिक"),
                   siya(C("ayatana", 2), "लौकिक", "लोकोत्तर"), is1(C("dhatu", 16), "लौकिक"),
                   siya(C("dhatu", 2), "लौकिक", "लोकोत्तर"), is1(C("sacca", 2), "लौकिक"),
                   is1(C("sacca", 2), "लोकोत्तर")]),
         " ".join([is1(C("indriya", 10), "लौकिक"), is1(C("indriya", 3), "लोकोत्तर"),
                   siya(C("indriya", 9), "लौकिक", "लोकोत्तर"), is1(akh, "लौकिक"),
                   siya(C("hetu", 6), "लौकिक", "लोकोत्तर"), is1(KABS, "लौकिक"),
                   siya(C("ahara", 3), "लौकिक", "लोकोत्तर"), is1(C("phassa", 6), "लौकिक"),
                   siya(MVDS_S, "लौकिक", "लोकोत्तर"), is1(C("vedana", 6), "लौकिक"),
                   siya(MVDS_VED, "लौकिक", "लोकोत्तर"), is1(C("sanna", 6), "लौकिक"),
                   siya(MVDS_SAN, "लौकिक", "लोकोत्तर"), is1(C("cetana", 6), "लौकिक"),
                   siya(MVDS_CET, "लौकिक", "लोकोत्तर"), is1(C("citta", 6), "लौकिक"),
                   siya(MVD_S, "लौकिक", "लोकोत्तर")]),
         "प्रत्यक्ष जानना, विषय वाले दो खंड, देखा हुआ, हितकर, अनुभूति;",
         "कर्म-फल, कर्म से उत्पन्न, आरंभिक विचार, भौतिक और लौकिक।",
         S.CHAPTER_TITLES[18] + " पूरा हुआ।",
         f"{S.BOOK_TITLE_QUOTED} ग्रंथ पूरा हुआ।",
         ]
    return L


def FOUR_MENTAL_NO_VED(n):
    """Pañca saññā… pañca cetanā… pañca cittā (m.pl, agreement with the last)"""
    return Subj(f"{cnt('sanna', n)}… {cnt('cetana', n)}… {cnt('citta', n)}", "m", "pl")


# ------------------------------------------------------------ assemble
def lines():
    L = ["### " + S.CHAPTER_TITLES[18]]
    L += sabbasangahika()
    L += uppatti()
    L += pariyapanna()
    L += dhammadassana()
    L += bhumantara()
    L += uppadaka()
    L += abhinneyya()
    L += sarammana()
    L += dittha()
    L += tika()
    return L


PI1_REUSED = [KUSALA_HETU_Q, KAB, AHARA3, "आँख का संपर्क", "मन के तत्व के संपर्क से उत्पन्न",
              IN["ananna"], IN["annatavi"], IN["jivita"], "अनंत चेतना का क्षेत्र", "कुछ भी न होने का क्षेत्र",
              "अनंत आकाश के क्षेत्र में पहुँचे देवताओं", "न पहचान, न अ-पहचान के क्षेत्र में पहुँचे देवताओं",
              DEV["para"], "मन के मैलों का विषय बनने वाली", "मन से घुली-मिली"]

if __name__ == "__main__":
    check_pi1(PI1_REUSED)
    write_chapter(FNAME, lines())
