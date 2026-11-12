# -*- coding: utf-8 -*-
"""Chapter 17, part D: exposition of the wanderings of craving (taṇhāvicaritaniddesa) and the closing."""
import sys
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-hi")
import build_ch1_sample_hi as S
from khuddaka17_f import *
from khuddaka17_a import TOGETHER, VIC, BRAHMAJALA

LINES = []


def L(p, h):
    LINES.append((p, h))


# the 18 forms; "iminā" (external) puts "इसके कारण " in front
FORMS = ["मैं हूँ", "मैं ऐसा हूँ", "मैं वैसा ही हूँ", "मैं अलग तरह का हूँ",
         "मैं होऊँगा", "मैं ऐसा होऊँगा", "मैं वैसा ही होऊँगा", "मैं अलग तरह का होऊँगा",
         "मैं शाश्वत हूँ", "मैं नश्वर हूँ",
         "मैं होऊँ", "मैं ऐसा होऊँ", "मैं वैसा ही होऊँ", "मैं अलग तरह का होऊँ",
         "काश मैं होता", "काश मैं ऐसा होता", "काश मैं वैसा ही होता", "काश मैं अलग तरह का होता"]
IMINA = "इसके कारण "


def form(i, ext):
    return (IMINA if ext else "") + FORMS[i]


def hoti(i, ext):
    return f"“{form(i, ext)}” ऐसा होता है"


# identity sentences: tense t in {"am", "shall", "may", "would"}
VERB = {"am": "हूँ", "shall": "होऊँगा", "may": "होऊँ"}


def ittha(x, t, ext):
    """khattiyosmi / khattiyo bhavissaṃ / khattiyo siyaṃ / apāhaṃ khattiyo siyaṃ"""
    pre = IMINA if ext else ""
    if t == "would":
        return f"“{pre}काश मैं {x} होता”"
    return f"“{pre}मैं {x} {VERB[t]}”"


def eva(x, t, ext):
    """yathā so khattiyo [iminā] tathāhaṃ khattiyosmi / apāhaṃ tathā ..."""
    pre = IMINA if ext else ""
    if t == "would":
        return f"“जैसे वह {x} है, {pre}काश मैं भी वैसा ही {x} होता”"
    return f"“जैसे वह {x} है, वैसे ही {pre}मैं {x} {VERB[t]}”"


NEG = {"am": "नहीं हूँ", "shall": "नहीं होऊँगा", "may": "न होऊँ"}


def anna(x, t, ext):
    """yathā so khattiyo [iminā] nāhaṃ tathā khattiyosmi / apāhaṃ na tathā ..."""
    pre = IMINA if ext else ""
    if t == "would":
        return f"“जैसे वह {x} है, {pre}काश मैं वैसा {x} न होता”"
    return f"“जैसे वह {x} है, {pre}वैसा {x} मैं {NEG[t]}”"


def items(fn, t, ext, mode):
    """mode 'full': all 13; 'pe': first two …pe… last; 'pe6': first …pe… arūpī, saññī, asaññī, nevasaññī"""
    xs = [fn(x, t, ext) for x in ID13]
    if mode == "full":
        return ", या ".join(xs)
    if mode == "pe":
        return f"{xs[0]}, या {xs[1]}… या {xs[12]}"
    return f"{xs[0]}… या " + ", या ".join(xs[9:])


SKANDHA = "भौतिक रूप… अनुभूति… पहचान… मानसिक रचनाओं… चेतना को"
CMP = "दूसरे व्यक्ति से तुलना करके"


def kath(n, i, ext):
    lead = f"({n}) " if n else ""
    return f"{lead}और {hoti(i, ext).replace(' ऐसा होता है', ' ऐसा कैसे होता है?')}"


def close(i, ext, iti=True):
    return f"{D} {'इस तरह ' if iti else ''}{hoti(i, ext)}।"


def root(n, i, ext, var=""):
    """(1)/(5)/(11)/(15): chanda, māna, diṭṭhi and the three papañcitas"""
    pre = "किसी परिघटना को, " + SKANDHA + (", अलग करके" if ext else ", अलग किए बिना") + var
    f = form(i, ext)
    return (f"{kath(n, i, ext)} {pre} “{f}” ऐसी चाह पाता है, “{f}” ऐसा अहंकार पाता है, “{f}” ऐसी दृष्टि पाता है। उसके होने पर "
            f"ये मानसिक फैलाव होते हैं {D} " + ", या ".join(f"“{form(j, ext)}”" for j in (i + 1, i + 2, i + 3)) + "।")


def sassata(n, i, ext, words, var=""):
    pre = "किसी परिघटना को, " + SKANDHA + (", अलग करके" if ext else ", अलग किए बिना") + var
    p = IMINA if ext else ""
    return f"{kath(n, i, ext)} {pre}, “{p}{words}” {close(i, ext)}"


def kind(n, i, ext, fn, t, mode, iti=True):
    cmp = "" if fn is ittha else (CMP + " ")
    return f"{kath(n, i, ext)} {cmp}{items(fn, t, ext, mode)} {close(i, ext, iti)}"


NICCA = "मैं नित्य हूँ, स्थिर हूँ, शाश्वत हूँ, न बदलने वाला हूँ"
UCCH = "मैं नष्ट हो जाऊँगा, विनष्ट हो जाऊँगा, नहीं रहूँगा"
INT = "आंतरिक को आधार बनाकर"
EXT = "बाह्य को आधार बनाकर"
VIC18 = VIC.format(n="अठारह")

L("#### Taṇhāvicaritaniddeso", "#### तृष्णा के विचरणों की व्याख्या")
L("##### (1) Ajjhattikassa upādāya", "##### (1) " + INT)
L("Tattha katamāni aṭṭhārasa taṇhāvicaritāni ajjhattikassa",
  f"यहाँ {INT} {VIC18} कौन-से हैं? " + ", ".join(hoti(i, False) for i in range(18)) + "।")
# internal: 18 lines
L("Kathañca asmīti hoti?", root(None, 0, False, " [वर्तनी-भेद (Sī., Ka.): anavakārī]"))
L("(2) Kathañca itthasmīti", kind(2, 1, False, ittha, "am", "full"))
L("(3) Kathañca evasmīti",
  kind(3, 2, False, eva, "am", "full").replace(CMP, "दूसरे व्यक्ति से [वर्तनी-भेद (Syā.): paraṃ puggalaṃ] तुलना करके", 1))
L("(4) Kathañca aññathāsmīti", kind(4, 3, False, anna, "am", "full"))
L("(5) Kathañca bhavissanti", root(5, 4, False))
L("(6) Kathañca itthaṃ bhavissanti", kind(6, 5, False, ittha, "shall", "full"))
L("(7) Kathañca evaṃ bhavissanti", kind(7, 6, False, eva, "shall", "pe", iti=False))   # Pāli closes "evaṃ bhavissanti hoti"
L("(8) Kathañca aññathā bhavissanti", kind(8, 7, False, anna, "shall", "pe"))
L("(9) Kathañca asasmīti", sassata(9, 8, False, NICCA))
L("(10) Kathañca sātasmīti", sassata(10, 9, False, UCCH))
L("(11) Kathañca siyanti", root(11, 10, False))
L("(12) Kathañca itthaṃ siyanti", kind(12, 11, False, ittha, "may", "full"))
L("(13) Kathañca evaṃ siyanti", kind(13, 12, False, eva, "may", "pe"))
L("(14) Kathañca aññathā siyanti", kind(14, 13, False, anna, "may", "pe"))
L("(15) Kathañca apāhaṃ siyanti", root(15, 14, False))
L("(16) Kathañca apāhaṃ itthaṃ siyanti",
  kind(16, 15, False, ittha, "would", "full") + " " + kind(17, 16, False, eva, "would", "pe"))
L("(18) Kathañca apāhaṃ aññathā siyanti", kind(18, 17, False, anna, "would", "pe"))
L("Imāni aṭṭhārasa taṇhāvicaritāni ajjhattikassa upādāya.", f"ये {INT} {VIC18} हैं।")

L("##### (2) Bāhirassa upādāya", "##### (2) " + EXT)
L("Tattha katamāni aṭṭhārasa taṇhāvicaritāni bāhirassa",
  f"यहाँ {EXT} {VIC18} कौन-से हैं? " + ", ".join(hoti(i, True) for i in range(18)) + "।")
L("(1) Kathañca iminā asmīti", root(1, 0, True))
L("(2) Kathañca iminā itthasmīti", kind(2, 1, True, ittha, "am", "full"))
L("(3) Kathañca iminā evasmīti", kind(3, 2, True, eva, "am", "pe"))
L("(4) Kathañca iminā aññathāsmīti", kind(4, 3, True, anna, "am", "pe"))
L("(5) Kathañca iminā bhavissanti", root(5, 4, True))
L("(6) Kathañca iminā itthaṃ bhavissanti", kind(6, 5, True, ittha, "shall", "pe6"))
L("(7) Kathañca iminā evaṃ bhavissanti", kind(7, 6, True, eva, "shall", "pe"))
L("(8) Kathañca iminā aññathā bhavissanti", kind(8, 7, True, anna, "shall", "pe"))
L("(9) Kathañca iminā asasmīti", sassata(9, 8, True, NICCA, " [वर्तनी-भेद (Sī.): avakārī]"))
L("(10) Kathañca iminā sātasmīti", sassata(10, 9, True, UCCH))
L("(11) Kathañca iminā siyanti", root(11, 10, True))
L("(12) Kathañca iminā itthaṃ siyanti", kind(12, 11, True, ittha, "may", "full"))
L("(13) Kathañca iminā evaṃ siyanti", kind(13, 12, True, eva, "may", "pe"))
L("(14) Kathañca iminā aññathā siyanti", kind(14, 13, True, anna, "may", "pe"))
L("(15) Kathañca iminā apāhaṃ siyanti", root(15, 14, True))
L("(16) Kathañca iminā apāhaṃ itthaṃ siyanti", kind(16, 15, True, ittha, "would", "full"))
L("(17) Kathañca iminā apāhaṃ evaṃ siyanti", kind(17, 16, True, eva, "would", "pe"))
L("(18) Kathañca iminā apāhaṃ aññathā siyanti", kind(18, 17, True, anna, "would", "pe"))
L("Imāni aṭṭhārasa taṇhāvicaritāni bāhirassa upādāya.", f"ये {EXT} {VIC18} हैं।")
L("Iti imāni aṭṭhārasa",
  f"इस तरह {INT} तृष्णा के ये अठारह विचरण, {EXT} तृष्णा के ये अठारह विचरण, {TOGETHER} {VIC.format(n='छत्तीस')} होते हैं। "
  f"इस तरह इस प्रकार के अतीत के {VIC.format(n='छत्तीस')}, भविष्य के {VIC.format(n='छत्तीस')}, वर्तमान के "
  f"{VIC.format(n='छत्तीस')}, {TOGETHER} {VIC.format(n='एक सौ आठ')} होते हैं।")
L("Tattha katamāni dvāsaṭṭhi diṭṭhigatāni",
  f"यहाँ {BRAHMAJALA} कौन-सी हैं? शाश्वतता के चार मत, आंशिक शाश्वतता के चार मत, सीमित और असीम के चार मत, गोलमोल जवाब देने के "
  f"चार मत, संयोग से उत्पत्ति के दो मत, आत्मा को पहचान वाली बताने वाले सोलह मत, आत्मा को पहचान से रहित बताने वाले आठ मत, "
  f"आत्मा को न पहचान वाली, न पहचान से रहित बताने वाले आठ मत, विनाश के सात मत, इसी जीवन में निर्वाण के पाँच मत {D} "
  f"ये {BRAHMAJALA} हैं।")
L("Khuddakavatthuvibhaṅgo niṭṭhito.", S.CHAPTER_TITLES[17] + " पूरा हुआ।")
