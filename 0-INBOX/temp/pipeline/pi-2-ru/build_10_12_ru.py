# -*- coding: utf-8 -*-
"""pi-2 Vibhaṅga, Russian plain zero-shot: chapters 10 (Bojjhaṅga), 11 (Maggaṅga), 12 (Jhāna).

usage: python -I -X utf8 build_10_12_ru.py
Writes AI_translation\\russian\\pi-2-russian-plain-zeroshot_split_chapters\\10-…, 11-…, 12-….md.
Reuses build_ch1_sample_ru (S), build_1_ru (B), build_2_3_ru (T), build_4_5_ru (F), build_6_ru (G), build_7_9_ru (Z):
path-factor bodies (pi-1 ^1-297 …), the Suttanta path definitions (ch. 4), the jhāna formula (pi-1 ^1-160 …, ch. 4),
the lokuttara / rūpāvacara / arūpāvacara openings (pi-1 ^1-277, ^1-499, ^1-505, ^1-577, ch. 6), the four efforts and
the satipaṭṭhāna phrases (ch. 7-8), the Pañhāpucchaka lexicon (B/T/F, extended in memory only).
Sense restraint and moderation in food are pi-1 ^1-1352 … ^1-1355; definitions of thina, middha, uddhacca, kukkucca,
vicikicchā, byāpāda, vitakka, vicāra, pīti, saññā, sati, paññā are pi-1 strings (asserted).
Every line is translated sentence by sentence from fixed strings; unknown Pāli raises KeyError.
Importing this module writes nothing.
"""
import os, re, sys

HERE = r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-ru"
sys.path.insert(0, HERE)
import build_ch1_sample_ru as S  # noqa: E402
import build_1_ru as B  # noqa: E402
import build_2_3_ru as T  # noqa: E402
import build_4_5_ru as F  # noqa: E402
import build_6_ru as G  # noqa: E402
import build_7_9_ru as Z  # noqa: E402

DASH = S.DASH
cap, low = S.cap, S.low
PE = "\x01"
PI1 = T.PI1
edit, in_pi1 = F.edit, F.in_pi1
SEC = S.SECTION_TITLES
TATTHA = S.TATTHA                 # Что такое здесь
VUCC = S.VUCCATI                  # это называется
TENA = cap(G.TENA)                # Поэтому и говорится:
SPLIT = re.compile(r'(?<=[.?])\s+(?=[A-ZĀĪŪṬḌÑṆṄ"])')


def lc(s):
    """lower the first letter (a Russian sentence continuing after a colon / comma)."""
    return s[:1].lower() + s[1:]


def called(ins, quoted=True):
    return T.called(ins, quoted)


def pe(body, n, tail_from):
    return F.pe(body, n, tail_from)


# ================================================================ 1. definition bodies (pi-1 strings)
SATI_FULL = F.SATI_B                                     # pi-1 ^1-14
SATI_PE2 = Z.SATI_PE                                     # осознанность, припоминание… правильная осознанность
SATI_PE3 = pe(F.SATI_B, 3, "правильная осознанность")    # … воспоминание… правильная осознанность
PANNA_FULL = T.pi1_body("^1-16", ", – это способность мудрости в это время").replace("То, что в это время есть ",
                                                                                         "То, что есть ")
PANNA_PE2 = Z.PANNA_PE                                   # мудрость, понимание… отсутствие заблуждения, …
assert PANNA_FULL.endswith("отсутствие заблуждения, исследование явлений, правильное воззрение")
VIRIYA_PE = Z.VIRIYA_PE                                  # душевное приложение усердия… правильное усилие
assert VIRIYA_PE.endswith("… правильное усилие")         # the Pāli of ^2-520 does have sammāvāyāmo
SAMADHI_PE1 = pe(F.SAMADHI_B, 1, "правильное сосредоточение")   # устойчивость ума… правильное сосредоточение
SADDHA4 = G.SADDHA                                       # вера, доверие, уверенность, глубокая убеждённость
VITAKKA_FULL = T.pi1_body("^1-7", ", – это направленная мысль в это время").replace("То, что в это время есть ",
                                                                                     "То, что есть ")
VITAKKA_PE = pe(VITAKKA_FULL, 2, "правильный помысел")
VICARA_FULL = T.pi1_body("^1-8", ", – это удержание мысли в это время").replace("То, что в это время есть ",
                                                                                 "То, что есть ")
VICARA_ANU = edit(VICARA_FULL, "движение мысли, ", "движение мысли, последовательное движение мысли, ")  # anucāro [new]
PITI_FULL = T.pi1_body("^1-9", ", – это восторг в это время").replace("То, что в это время есть ", "То, что есть ")
VAR_ODAGGA = " [вариант написания (Sī.): odaggaṃ; dha. sa. 9]"
PITI_SAMB = PITI_FULL + ", фактор пробуждения восторга"                  # pi-1 ^1-285
assert PITI_SAMB.replace("То, что есть ", "То, что в это время есть ") in PI1["^1-285"]
PITI_SAMB_VAR = edit(PITI_SAMB, "воодушевление,", "воодушевление" + VAR_ODAGGA + ",")
SANNA = "То, что есть восприятие, узнавание, состояние узнавания"        # pi-1 ^1-61
in_pi1(SANNA.replace("То, что есть ", "То, что в это время есть "))
UPEKKHA = "То, что есть невозмутимость, проявление невозмутимости, полная невозмутимость, уравновешенность ума"   # new
PASSADDHI = ("То, что у совокупности чувств, совокупности восприятия, совокупности формирующих факторов и совокупности "
             "сознания есть безмятежность, полная безмятежность, утихание, полное утихание, состояние полного утихания")
in_pi1("есть безмятежность, полная безмятежность, утихание, полное утихание, состояние полного утихания")   # pi-1 ^1-41
THINA = T.pi1_body("^1-1162", ", – это называется вялостью")
assert THINA.startswith("То, что есть неготовность ума,")
VAR_THIYANA = " [вариант написания (Sī., Syā.): thīyanā thīyitattaṃ]"
THINA_VAR = edit(THINA, "состояние вялости ума", "состояние вялости" + VAR_THIYANA + " ума")
MIDDHA = T.pi1_body("^1-1163", ", – это называется сонливостью")
assert MIDDHA.startswith("То, что есть неготовность умственного тела,")
UDDHACCA = "То, что есть " + G.UDDH                                       # pi-1
_K = PI1["^1-1166"]
KUKKUCCA_A = _K[_K.index("Восприятие недопустимого"):_K.index(". То, что есть такие угрызения")]
KUKKUCCA_B = _K[_K.index("то, что есть такие угрызения".capitalize()):_K.index(", – это называется угрызениями")]
KUKKUCCA = KUKKUCCA_A + "; " + lc(KUKKUCCA_B)           # pi-2 joins the two with a comma
VICI_FULL = "То, что есть " + G.VICI
VICI_SHORT = "То, что есть сомнение, проявление сомнения, состояние сомнения, оцепенелость ума, терзание ума"
assert G.VICI.startswith("сомнение, проявление сомнения, состояние сомнения,") and G.VICI.endswith(
    "оцепенелость ума, терзание ума")
BYAPADA = "То, что есть досада ума, " + T.DOSA_PI1                        # pi-1 ^1-1066 without «такая»
VAR_DUSANA = " [вариант написания (Syā.): dūsanā dūsitattaṃ]"
BYAPADA_VAR = edit(BYAPADA, "проявление злобы, состояние злобы,", "проявление злобы, состояние злобы" + VAR_DUSANA + ",")
BYAPADA_PE = "То, что есть досада ума… свирепость, грубость, недовольство ума"
assert BYAPADA.endswith("свирепость, грубость, недовольство ума")
CITTA_PE = G.BODY["Yaṃ cittaṃ mano mānasaṃ…pe… tajjāmanoviññāṇadhātu"][0]
RAGA_PE = G.BODY["Yo rāgo sārāgo…pe… cittassa sārāgo"][0]
SPACE = "То, что есть " + T.SPACE_EXT                                     # pi-1 ^1-637
in_pi1(T.SPACE_EXT)
FEEL = T.FEEL
SUKHA_C = "То, что есть " + FEEL["somanassa"]      # cetasika sukha (= somanassa in the Pāli)
SUKHA_K = "То, что есть " + FEEL["sukha"]
DUKKHA_K = "То, что есть " + FEEL["dukkha"]
DOMANASSA = "То, что есть " + FEEL["domanassa"]
ADM_C = "то, что есть " + FEEL["upekkhā"]
ASSERT_P3 = F.PALI3
CITTACET = "ум и сопутствующие уму явления"                              # cittacetasikā dhammā [pi-1 ^1-1029]
in_pi1(cap(CITTACET))

# ================================================================ 2. factors of awakening and path factors
BOJ = ["sati", "dhammavicaya", "vīriya", "pīti", "passaddhi", "samādhi", "upekkhā"]
BOJ_R = {k: Z.NOUN[k + "sambojjhaṅg"][0] for k in BOJ}
BOJ_INS = {k: "фактором" + BOJ_R[k][len("фактор"):] for k in BOJ}
SEVEN = "Семь факторов пробуждения"                                       # satta bojjhaṅgā [new; pi-1 terms]
SEVEN_INS = "семью факторами пробуждения"
SEVEN_LINE = f"{SEVEN} {DASH} " + T.enum([BOJ_R[k] for k in BOJ]) + "."
SEVEN_PE = f"{SEVEN} {DASH} {BOJ_R['sati']}… {BOJ_R['upekkhā']}."
SEVEN_P = "Satta bojjhaṅgā – " + ", ".join(k + "sambojjhaṅgo" for k in BOJ) + "."
SEVEN_PE_P = "Satta bojjhaṅgā – satisambojjhaṅgo…pe… upekkhāsambojjhaṅgo."
NISSITA = {   # vivekanissitaṃ virāganissitaṃ nirodhanissitaṃ vossaggapariṇāmiṃ [new], by gender of the object
    "m": "опирающийся на уединение, опирающийся на бесстрастие, опирающийся на прекращение, ведущий к отказу",
    "n": "опирающееся на уединение, опирающееся на бесстрастие, опирающееся на прекращение, ведущее к отказу",
    "f": "опирающуюся на уединение, опирающуюся на бесстрастие, опирающуюся на прекращение, ведущую к отказу"}
MAGGA = F.MAGGA
MAGGA_ACC = {"sammādiṭṭhi": ("правильное воззрение", "n"), "sammāsaṅkappo": ("правильный помысел", "m"),
             "sammāvācā": ("правильную речь", "f"), "sammākammanto": ("правильное действие", "n"),
             "sammāājīvo": ("правильный образ жизни", "m"), "sammāvāyāmo": ("правильное усилие", "n"),
             "sammāsati": ("правильную осознанность", "f"), "sammāsamādhi": ("правильное сосредоточение", "n")}
MAGGA_P_ACC = {"sammādiṭṭhi": "sammādiṭṭhiṃ", "sammāsaṅkappo": "sammāsaṅkappaṃ", "sammāvācā": "sammāvācaṃ",
               "sammākammanto": "sammākammantaṃ", "sammāājīvo": "sammāājīvaṃ", "sammāvāyāmo": "sammāvāyāmaṃ",
               "sammāsati": "sammāsatiṃ", "sammāsamādhi": "sammāsamādhiṃ"}
EIGHTFOLD, FIVEFOLD = F.EIGHTFOLD, F.FIVEFOLD
EIGHTFOLD_INS, FIVEFOLD_INS = "восьмичастным путём", "пятичастным путём"   # [new, pi-1 nominatives]
EIGHT_P = ", ".join(MAGGA)
FIVE_P = "sammādiṭṭhi, sammāsaṅkappo, sammāvāyāmo, sammāsati, sammāsamādhi"
assert F.EIGHT_FACTORS == ", ".join(v[0] for v in MAGGA.values())

# ================================================================ 3. jhāna openings
JH1, JH2, JH4 = F.JH1, F.JH2, F.JH4
JH3 = F.JH3                                              # with the dash (Pāli "ācikkhanti – "upekkhako …"")
JH3_NODASH = edit(JH3, f"о нём {DASH} «", "о нём: «")    # ch. 11 ^2-487 has no dash there
ARUPA1 = ("с полным преодолением восприятий материальной формы, с исчезновением восприятий соударения, без внимания к "
          "восприятиям разнообразия, с мыслью «Пространство бесконечно» входит в сферу бесконечного пространства и "
          "пребывает в ней")
ARUPA2 = ("полностью преодолев сферу бесконечного пространства, с мыслью «Сознание бесконечно» входит в сферу "
          "бесконечного сознания и пребывает в ней")
ARUPA3 = ("полностью преодолев сферу бесконечного сознания, с мыслью «Нет ничего» входит в сферу отсутствия чего-либо "
          "и пребывает в ней")
ARUPA4 = "полностью преодолев сферу отсутствия чего-либо, входит в сферу ни восприятия, ни невосприятия и пребывает в ней"
in_pi1("с полным преодолением восприятий материальной формы, с исчезновением восприятий соударения, без внимания к "
       "восприятиям разнообразия", "полностью преодолев сферу бесконечного пространства",
       "полностью преодолев сферу бесконечного сознания", "полностью преодолев сферу отсутствия чего-либо",
       "сферы ни восприятия, ни невосприятия")

OPEN = {   # Pāli after "Idha bhikkhu yasmiṃ samaye " -> Russian after «Вот в то время, когда монах »
    "rūpūpapattiyā maggaṃ bhāveti": "развивает путь к рождению в мире форм",
    "lokuttaraṃ jhānaṃ bhāveti niyyānikaṃ apacayagāmiṃ diṭṭhigatānaṃ pahānāya paṭhamāya bhūmiyā pattiyā":
        "развивает надмирское медитативное погружение, ведущее к освобождению и к убыванию, для устранения приверженности "
        "воззрениям, для достижения первой ступени",
    "rūpāvacaraṃ jhānaṃ bhāveti kiriyaṃ neva kusalaṃ nākusalaṃ na ca kammavipākaṃ diṭṭhadhammasukhavihāraṃ":
        "развивает медитативное погружение, относящееся к миру форм, функциональное, ни благое, ни неблагое и не "
        "являющееся результатом действий, для пребывания в счастье в этой жизни",
}
TASSEVA = {   # "Tasseva … vipākaṃ" -> Russian up to «когда монах»
    "rūpāvacarassa kusalassa kammassa katattā upacitattā vipākaṃ":
        "Вследствие того же совершённого и накопленного благого действия, относящегося к миру форм, в качестве его "
        "результата, когда монах",
    "lokuttarassa kusalassa jhānassa katattā bhāvitattā vipākaṃ":
        "Вследствие того же совершённого и развитого надмирского благого медитативного погружения, в качестве его "
        "результата, когда монах",
}
ORD = {"paṭhamaṃ": ("первое", "в первое", "первым"), "dutiyaṃ": ("второе", "во второе", "вторым"),
       "tatiyaṃ": ("третье", "в третье", "третьим"), "catutthaṃ": ("четвёртое", "в четвёртое", "четвёртым"),
       "pañcamaṃ": ("пятое", "в пятое", "пятым")}
JH_HEAD = {   # Pāli head of the jhāna part (before the ordinal) -> (participle?, Russian)
    "vivicceva kāmehi…pe…": (True, "полностью уединившись от чувственных удовольствий…"),
    "vitakkavicārānaṃ vūpasamā…pe…": (False, "с затиханием направленной мысли и удержания мысли…"),
    "pītiyā ca virāgā…pe…": (False, "с угасанием восторга…"),
    "sukhassa ca pahānā…pe…": (False, "с устранением приятного…"),
    "vivicceva kāmehi vivicca akusalehi dhammehi avitakkaṃ vicāramattaṃ vivekajaṃ pītisukhaṃ": (
        True, "полностью уединившись от чувственных удовольствий, уединившись от неблагих явлений,"),
}
JH_AFTER = {"vivicceva kāmehi vivicca akusalehi dhammehi avitakkaṃ vicāramattaṃ vivekajaṃ pītisukhaṃ":
            ", без направленной мысли, только с удержанием мысли, с восторгом и счастьем, рождёнными уединением"}
in_pi1("без направленной мысли, только с удержанием мысли", "с восторгом и счастьем, рождёнными уединением",
       "с затиханием направленной мысли и удержания мысли… второе медитативное погружение… третье медитативное "
       "погружение… четвёртое медитативное погружение… первое медитативное погружение… входит в пятое медитативное "
       "погружение", "с угасанием восторга… входит в четвёртое", "с устранением приятного… входит в пятое",
       "с затиханием направленной мысли и удержания мысли… входит в третье")
QUAL = {"pathavīkasiṇaṃ": ", со всеохватным объектом земли,",
        "dukkhapaṭipadaṃ dandhābhiññaṃ": ", с трудным способом практики и медленным высшим знанием,",
        "dukkhapaṭipadaṃ dandhābhiññaṃ suññataṃ": ", с трудным способом практики и медленным высшим знанием, пустое,",
        "": ""}
ARUPA_OPEN = {   # whole Pāli openings of the formless fourth jhāna (pi-1 2-04/2-05, ch. 6)
    "Idha bhikkhu yasmiṃ samaye " + G.P_ARUPA: "Вот в то время, когда " + edit(G.ARUPA_K, "кто-либо", "монах"),
    "Tasseva arūpāvacarassa kusalassa kammassa katattā upacitattā vipākaṃ " + G.P_ARUPA[len("arūpūpapattiyā maggaṃ bhāveti "):]:
        edit(G.ARUPA_V, "когда кто-либо", "когда монах"),
    "Idha bhikkhu yasmiṃ samaye arūpāvacaraṃ jhānaṃ bhāveti kiriyaṃ neva kusalaṃ nākusalaṃ na ca kammavipākaṃ "
    "diṭṭhadhammasukhavihāraṃ " + G.P_ARUPA[len("arūpūpapattiyā maggaṃ bhāveti "):]:
        "Вот в то время, когда " + edit(G.ARUPA_F, "кто-либо", "монах"),
}


def jhana_part(p):
    """'<head> <ordinal> jhānaṃ[…pe… <ord> jhānaṃ …] upasampajja viharati[ <qual>]' -> (participle?, Russian)."""
    m = re.match(r"^(.+?) ?((?:(?:paṭhamaṃ|dutiyaṃ|tatiyaṃ|catutthaṃ|pañcamaṃ) jhānaṃ…pe… )*)"
                 r"(paṭhamaṃ|dutiyaṃ|tatiyaṃ|catutthaṃ|pañcamaṃ) jhānaṃ upasampajja viharati ?(.*)$", p)
    if not m:
        raise KeyError("jhāna part: " + p[:120])
    head, mids, last, qual = m.groups()
    part, ru = JH_HEAD[head]
    if mids:
        ru += "".join(f" {ORD[o][0]} медитативное погружение…" for o in re.findall(r"(\S+) jhānaṃ…pe…", mids))
    ru += f" входит {ORD[last][1]} медитативное погружение" + JH_AFTER.get(head, "")
    ru += QUAL[qual] + " и пребывает в нём"
    return part, ru


def opening(s):
    """'Idha bhikkhu yasmiṃ samaye …' / 'Tasseva … vipākaṃ …' up to the comma before 'tasmiṃ samaye' / 'yā tasmiṃ'."""
    for p, r in ARUPA_OPEN.items():
        if s == p:
            return r
    if s.startswith("Idha bhikkhu yasmiṃ samaye "):
        rest = s[len("Idha bhikkhu yasmiṃ samaye "):]
        for p, r in OPEN.items():
            if rest.startswith(p + " "):
                part, jh = jhana_part(rest[len(p) + 1:])
                return f"Вот в то время, когда монах {r} и{', ' if part else ' '}{jh}"
    if s.startswith("Tasseva "):
        rest = s[len("Tasseva "):]
        for p, r in TASSEVA.items():
            if rest.startswith(p + " "):
                part, jh = jhana_part(rest[len(p) + 1:])
                return f"{r}{', ' if part else ' '}{jh}"
    raise KeyError("opening: " + s[:120])


assert opening(Z.LOK_P) == Z.LOK_R
assert opening(Z.VIP_P) == Z.VIP_R
assert opening("Idha bhikkhu yasmiṃ samaye " + G.P_RUPA) == "Вот в то время, когда монах " + G.RUPA_K[len("кто-либо "):]
assert opening("Tasseva rūpāvacarassa kusalassa kammassa katattā upacitattā vipākaṃ vivicceva kāmehi…pe… paṭhamaṃ jhānaṃ "
               "upasampajja viharati pathavīkasiṇaṃ") == edit(G.RUPA_V, "когда кто-либо", "когда монах")
assert opening("Idha bhikkhu yasmiṃ samaye rūpāvacaraṃ jhānaṃ bhāveti kiriyaṃ neva kusalaṃ nākusalaṃ na ca kammavipākaṃ "
               "diṭṭhadhammasukhavihāraṃ vivicceva kāmehi…pe… paṭhamaṃ jhānaṃ upasampajja viharati pathavīkasiṇaṃ"
               ) == "Вот в то время, когда монах " + G.RUPA_F[len("кто-либо "):]
assert opening("Tasseva lokuttarassa kusalassa jhānassa katattā bhāvitattā vipākaṃ vivicceva kāmehi…pe… paṭhamaṃ jhānaṃ "
               "upasampajja viharati dukkhapaṭipadaṃ dandhābhiññaṃ") == edit(G.LOK_V, "когда кто-либо", "когда монах")

ANGA = {"pañcaṅgikaṃ": "пятичастное", "caturaṅgikaṃ": "четырёхчастное", "tivaṅgikaṃ": "трёхчастное",
        "duvaṅgikaṃ": "двухчастное"}
in_pi1(*(f"есть {v} медитативное погружение" for v in ANGA.values()))
JF = {"vitakko": "направленная мысль", "vicāro": "удержание мысли", "pīti": "восторг", "sukhaṃ": "счастье",
      "cittassekaggatā": "однонаправленность ума", "upekkhā": "невозмутимость"}
in_pi1("Направленная мысль, удержание мысли, восторг, счастье, однонаправленность ума.")   # pi-1 ^1-83
JHANA_N = "медитативное погружение"
JHANA_INS = "медитативным погружением"
FOUR_JH = "Четыре медитативных погружения"


def tail(rest):
    """the Pāli after the opening (starting with ', '); Russian continues after the opening."""
    if rest == ", tasmiṃ samaye phasso hoti…pe… avikkhepo hoti.":
        return ", " + F.TAIL_SENT["phasso hoti…pe… avikkhepo hoti."]
    if rest == ", yo tasmiṃ samaye phasso hoti…pe… avikkhepo hoti – ime dhammā kusalā.":   # "yo" as written
        return f", то, что в это время есть контакт… есть отсутствие отвлечения, {DASH} это благие явления."
    if rest == ", tasmiṃ samaye satta bojjhaṅgā honti – satisambojjhaṅgo…pe… upekkhāsambojjhaṅgo.":
        return f", в это время есть {low(SEVEN_PE)}"
    m = re.match(r"^, tasmiṃ samaye ((?:aṭṭhaṅgiko|pañcaṅgiko) maggo hoti – .+)$", rest)
    if m:
        return ", " + F.TAIL_SENT[m.group(1)]
    m = re.match(r"^, tasmiṃ samaye (\S+) jhānaṃ hoti( –|) (.+)\.$", rest)
    if m:
        items = re.split(r", | ", m.group(3)) if m.group(2) == "" else m.group(3).split(", ")
        sep = f" {DASH} " if m.group(2) else ": "   # no dash in the Pāli (^2-629): a colon, commas added (reported)
        return f", в это время есть {ANGA[m.group(1)]} {JHANA_N}{sep}" + ", ".join(JF[x] for x in items) + "."
    m = re.match(r"^, ((?:yo|yā|yaṃ) tasmiṃ samaye .+?) – (?:ayaṃ|idaṃ) vuccati (\"?)(.+?)\"?\.$", rest)
    if m:
        mm = re.match(r"^(Yo|Yā|Yaṃ) tasmiṃ samaye (.+)$", cap(m.group(1)))
        body = ADEF[mm.group(1) + " " + mm.group(2)]
        return (f", то, что в это время есть {body[len('То, что есть '):]}, {DASH} "
                f"{called(ATERM[m.group(3)][1], bool(m.group(2)))}.")
    raise KeyError("tail: " + rest[:120])


def jhana_sentence(s):
    """a whole sentence that starts with an opening."""
    for p in ARUPA_OPEN:
        if s.startswith(p + ","):
            return opening(p) + tail(s[len(p):])
    m = re.match(r"^(.+?(?:upasampajja viharati(?: [^,]+)?)),( (?:yo |yā |yaṃ )?tasmiṃ samaye .+)$", s)
    if not m:
        raise KeyError("jhāna sentence: " + s[:100])
    return opening(m.group(1)) + tail("," + m.group(2))


# ================================================================ 4. Abhidhamma terms and bodies (ch. 10-12)
ATERM = {k: v for k, v in MAGGA.items()}
for k in BOJ:
    ATERM[k + "sambojjhaṅgo"] = (BOJ_R[k], BOJ_INS[k])
ATERM["aṭṭhaṅgiko maggo"] = (EIGHTFOLD, EIGHTFOLD_INS)
ATERM["pañcaṅgiko maggo"] = (FIVEFOLD, FIVEFOLD_INS)
ATERM["satta bojjhaṅgā"] = (low(SEVEN), SEVEN_INS)
for k, (nom, _in, ins) in ORD.items():
    ATERM[k + " jhānaṃ"] = (f"{nom} {JHANA_N}", f"{ins} {JHANA_INS}")

ADEF = {}   # Pāli body (between "? " and " – ayaṃ vuccati") -> Russian «То, что есть …» (comma before the dash)
ADEF.update(F.FACTOR_BODY)
ADEF.update({k: v for k, v in Z.DEF.items()})
ADEF.update({
    "Yā micchāājīvā ārati virati paṭivirati veramaṇī akiriyā akaraṇaṃ anajjhāpatti velāanatikkamo setughāto "
    "sammāājīvo maggaṅgaṃ maggapariyāpannaṃ": F.AJIVA_L,                      # ch. 4 has "micchā ājīvā"
    "Yā catūhi vacīduccaritehi ārati virati paṭivirati veramaṇī akiriyā akaraṇaṃ anajjhāpatti velāanatikkamo setughāto "
    "sammāvācā maggaṅgaṃ maggapariyāpannaṃ": F.VACA_L,
    "Yo takko vitakko saṅkappo appanā byappanā cetaso abhiniropanā sammāsaṅkappo maggaṅgaṃ maggapariyāpannaṃ":
        F.SANKAPPA_L,
    "Yā pīti pāmojjaṃ āmodanā pamodanā hāso pahāso vitti odagyaṃ [odaggaṃ (sī.) dha. sa. 9] attamanatā cittassa "
    "pītisambojjhaṅgo": PITI_SAMB_VAR,
    "Yā vedanākkhandhassa saññākkhandhassa saṅkhārakkhandhassa viññāṇakkhandhassa passaddhi paṭippassaddhi passambhanā "
    "paṭippassambhanā paṭippassambhitattaṃ passaddhisambojjhaṅgo": PASSADDHI + ", " + BOJ_R["passaddhi"],
    "Yā upekkhā upekkhanā ajjhupekkhanā majjhattatā cittassa upekkhāsambojjhaṅgo": UPEKKHA + ", " + BOJ_R["upekkhā"],
    "Yā paññā pajānanā…pe… amoho dhammavicayo sammādiṭṭhi dhammavicayasambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ":
        F.FACTOR_BODY["Yā paññā pajānanā…pe… amoho dhammavicayo sammādiṭṭhi dhammavicayasambojjhaṅgo maggaṅgaṃ "
                      "maggapariyāpannaṃ"],
    "Yā cittassa ṭhiti saṇṭhiti avaṭṭhiti avisāhāro avikkhepo avisāhaṭamānasatā samatho samādhindriyaṃ samādhibalaṃ "
    "sammāsamādhi samādhisambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ": F.SAMADHI_L,
})
for _k, _v in ADEF.items():
    assert _v.startswith("То, что "), _k


def avasesa(s):
    """'Avasesā dhammā X sampayuttā[…pe… avasesā dhammā Y sampayuttā …].'"""
    body = s[:-1]
    parts = body.split("…pe… ")
    out = []
    for x in parts:
        x = cap(x)
        m = re.match(r"^Avasesā dhammā (\S+?)sampayuttā$", x)
        if m:
            k = m.group(1)
            ru = {"jhāna": JHANA_INS}.get(k) or BOJ_INS[k[:-len("sambojjhaṅga")]]
        else:
            m = re.match(r"^Avasesā dhammā (.+) sampayuttā$", x)
            ru = {"sattahi bojjhaṅgehi": SEVEN_INS, "aṭṭhaṅgikena maggena": EIGHTFOLD_INS,
                  "pañcaṅgikena maggena": FIVEFOLD_INS, "sammādiṭṭhiyā": MAGGA["sammādiṭṭhi"][1],
                  "sammāsaṅkappena": MAGGA["sammāsaṅkappo"][1], "sammāvāyāmena": MAGGA["sammāvāyāmo"][1],
                  "sammāsatiyā": MAGGA["sammāsati"][1], "sammāsamādhinā": MAGGA["sammāsamādhi"][1]}[m.group(1)]
        out.append(f"остальные явления связаны с {ru}")
    return cap("… ".join(out))


assert avasesa("Avasesā dhammā sattahi bojjhaṅgehi sampayuttā.") == "Остальные явления связаны с семью факторами пробуждения"


def abhi_sentence(s):
    if s in ASENT:
        return ASENT[s]
    if s.startswith(("Idha bhikkhu yasmiṃ samaye", "Tasseva ")):
        return jhana_sentence(s)
    if re.match(r"^Avasesā dhammā .+sampayuttā(?:ti)?(?:…pe…)?\.$", s):
        end = "…." if s.endswith("…pe….") else "."
        s2 = re.sub(r"(?:ti)?(?:…pe…)?\.$", ".", s)
        return avasesa(s2) + end
    m = re.match(r"^Tattha katam(?:o|ā|aṃ|e) (.+?)\?$", s)
    if m:
        return f"{TATTHA} {ATERM[m.group(1)][0]}?"
    m = re.match(r'^(?:Ayaṃ|Idaṃ) vuccati "(.+)"\.$|^Ime vuccanti "(.+)"\.$', s)
    if m:
        return cap(called(ATERM[m.group(1) or m.group(2)][1])) + "."
    m = re.match(r'^(.+?),? – (?:ayaṃ|idaṃ) vuccati "(.+?)"(…pe…)?\.$', s)
    if m and m.group(1) in ADEF:
        return f"{ADEF[m.group(1)]}, {DASH} {called(ATERM[m.group(2)][1])}{'…' if m.group(3) else ''}."
    raise KeyError("abhi sentence: " + s[:120])


ASENT = {
    "Ime vuccanti satta bojjhaṅgā.": cap(called(SEVEN_INS, False)) + ".",
    "Ime dhammā kusalā.": "Это благие явления.",
}


def abhi_line(t):
    """Abhidhammabhājanīya line: 'Tattha katamo X? <answer>' or a whole opening line."""
    m = re.match(r"^(Tattha katam(?:o|ā|aṃ|e) [^?]+\?) (.+)$", t)
    if m:
        head, rest = m.group(1), m.group(2)
        out = [abhi_sentence(head)]
    else:
        rest = t
        out = []
    for s in SPLIT.split(rest):
        mm = re.match(r'^(.+?),? – (?:ayaṃ|idaṃ) vuccati "(.+?)"(…pe…)?\.$', s)
        if mm and mm.group(1) in ADEF:
            out.append(f"{ADEF[mm.group(1)]}, {DASH} {called(ATERM[mm.group(2)][1])}{'…' if mm.group(3) else ''}.")
        else:
            out.append(abhi_sentence(s))
    return " ".join(out)


# ================================================================ 5. chapter 10 (Bojjhaṅga) Suttanta
AN_P = "abhiññāya sambodhāya nibbānāya saṃvattati"
AN_R = "ведёт к высшему знанию, к полному пробуждению, к нирване"            # abhiññā [pi-1]; sambodha [new]
PAIRS10 = {   # factor: ((Pāli A, Russian A), (Pāli B, Russian B), Pāli A with variant, Russian A with variant, B ditto)
    "sati": (("ajjhattaṃ dhammesu sati", "осознанность в отношении внутренних явлений"),
             ("bahiddhā dhammesu sati", "осознанность в отношении внешних явлений")),
    "dhammavicaya": (("ajjhattaṃ dhammesu pavicayo", "тщательное исследование внутренних явлений"),
                     ("bahiddhā dhammesu pavicayo", "тщательное исследование внешних явлений")),
    "vīriya": (("kāyikaṃ vīriyaṃ", "телесное усердие"), ("cetasikaṃ vīriyaṃ", "душевное усердие")),
    "pīti": (("savitakkasavicārā pīti", "восторг с направленной мыслью и удержанием мысли"),
             ("avitakkaavicārā pīti", "восторг без направленной мысли и без удержания мысли")),
    "passaddhi": (("kāyapassaddhi", "безмятежность умственного тела"), ("cittapassaddhi", "безмятежность ума")),
    "samādhi": (("savitakko savicāro samādhi", "сосредоточение с направленной мыслью и удержанием мысли"),
                ("avitakko avicāro samādhi", "сосредоточение без направленной мысли и без удержания мысли")),
    "upekkhā": (("ajjhattaṃ dhammesu upekkhā", "невозмутимость в отношении внутренних явлений"),
                ("bahiddhā dhammesu upekkhā", "невозмутимость в отношении внешних явлений")),
}
in_pi1("безмятежность умственного тела", "безмятежность ума")
VAR_PASS = {"kāyapassaddhi": " [вариант написания (Syā., Ka.): kāyappassaddhi]",
            "cittapassaddhi": " [вариант написания (Syā., Ka.): cittappassaddhi]"}


def pair_line(k):
    (pa, ra), (pb, rb) = PAIRS10[k]
    va = VAR_PASS.get(pa, "")
    vb = VAR_PASS.get(pb, "")
    pva = f" [{pa.replace('kāyapa', 'kāyappa')} (syā. ka.)]" if va else ""
    pvb = f" [{pb.replace('cittapa', 'cittappa')} (syā. ka.)]" if vb else ""
    x = k + "sambojjhaṅgo"
    p = (f"Tattha katamo {x}? Atthi {pa}{pva}, atthi {pb}{pvb}. Yadapi {pa} tadapi {x} {AN_P}. "
         f"Yadapi {pb} tadapi {x} {AN_P}.")
    r = (f"{TATTHA} {BOJ_R[k]}? Есть {ra}{va}, есть {rb}{vb}. И {ra} является {BOJ_INS[k]} и {AN_R}. "
         f"И {rb} является {BOJ_INS[k]} и {AN_R}.")
    return p, r


NIS_P = "vivekanissitaṃ virāganissitaṃ nirodhanissitaṃ vossaggapariṇāmiṃ"
SUTTA10 = {
    "Tattha katamo satisambojjhaṅgo? Idha bhikkhu satimā hoti paramena satinepakkena samannāgato, cirakatampi "
    "cirabhāsitampi saritā hoti anussaritā – ayaṃ vuccati \"satisambojjhaṅgo\".":
        f"{TATTHA} {BOJ_R['sati']}? Вот монах осознан, наделён высшей осознанностью и благоразумием, он помнит и "
        f"припоминает и то, что сделано давно, и то, что сказано давно, {DASH} {called(BOJ_INS['sati'])}.",
    "So tathā sato viharanto taṃ dhammaṃ paññāya pavicinati pavicarati parivīmaṃsamāpajjati – ayaṃ vuccati "
    "\"dhammavicayasambojjhaṅgo\".":
        f"Пребывая так осознанным, он с помощью мудрости исследует это явление, обдумывает его, подвергает его "
        f"всестороннему изучению {DASH} {called(BOJ_INS['dhammavicaya'])}.",
    "Tassa taṃ dhammaṃ paññāya pavicinato pavicarato parivīmaṃsamāpajjato āraddhaṃ hoti vīriyaṃ asallīnaṃ – ayaṃ "
    "vuccati \"vīriyasambojjhaṅgo\".":
        f"Когда он так с помощью мудрости исследует это явление, обдумывает его, подвергает его всестороннему изучению, "
        f"у него пробуждено неослабное усердие {DASH} {called(BOJ_INS['vīriya'])}.",
    "Āraddhavīriyassa uppajjati pīti nirāmisā – ayaṃ vuccati \"pītisambojjhaṅgo\".":
        f"У того, кто пробудил усердие, возникает неплотский восторг {DASH} {called(BOJ_INS['pīti'])}.",
    "Pītimanassa kāyopi passambhati, cittampi passambhati – ayaṃ vuccati \"passaddhisambojjhaṅgo\".":
        f"У того, чей ум полон восторга, утихает и тело, утихает и ум {DASH} {called(BOJ_INS['passaddhi'])}.",
    "Passaddhakāyassa sukhino cittaṃ samādhiyati – ayaṃ vuccati \"samādhisambojjhaṅgo\".":
        f"У счастливого, чьё тело безмятежно, ум сосредотачивается {DASH} {called(BOJ_INS['samādhi'])}.",
    "So tathā samāhitaṃ cittaṃ sādhukaṃ ajjhupekkhitā hoti – ayaṃ vuccati \"upekkhāsambojjhaṅgo\".":
        f"На так сосредоточенный ум он хорошо взирает с полной невозмутимостью {DASH} "
        f"{called(BOJ_INS['upekkhā'])}.",
    "Tattha katamo satisambojjhaṅgo? Idha bhikkhu satisambojjhaṅgaṃ bhāveti " + NIS_P + ", dhammavicayasambojjhaṅgaṃ "
    "bhāveti…pe… vīriyasambojjhaṅgaṃ bhāveti… pītisambojjhaṅgaṃ bhāveti… passaddhisambojjhaṅgaṃ bhāveti… "
    "samādhisambojjhaṅgaṃ bhāveti… upekkhāsambojjhaṅgaṃ bhāveti " + NIS_P + ".":
        f"{TATTHA} {BOJ_R['sati']}? Вот монах развивает {BOJ_R['sati']}, {NISSITA['m']}, развивает "
        f"{BOJ_R['dhammavicaya']}… развивает {BOJ_R['vīriya']}… развивает {BOJ_R['pīti']}… развивает "
        f"{BOJ_R['passaddhi']}… развивает {BOJ_R['samādhi']}… развивает {BOJ_R['upekkhā']}, {NISSITA['m']}.",
}
for _k in BOJ:
    _p, _r = pair_line(_k)
    SUTTA10[_p] = _r

# ================================================================ 6. chapter 11 (Maggaṅga) Suttanta
SUTTA11 = {}
for _k in ("sammādiṭṭhi", "sammāsaṅkappo", "sammāvācā", "sammākammanto", "sammāājīvo"):
    pass   # identical to ch. 4: F.sutta4 (checked in build_ch11)
_EFF_P = ", ".join(f"{x} {Z.EFFORT_P}" for x in Z.SP_P)
SUTTA11["Tattha katamo sammāvāyāmo? Idha bhikkhu " + _EFF_P + " – ayaṃ vuccati \"sammāvāyāmo\"."] = (
    f"{TATTHA} {MAGGA['sammāvāyāmo'][0]}? Вот монах {Z.efforts(_EFF_P)} {DASH} {called(MAGGA['sammāvāyāmo'][1])}.")
_SATI_P = ", ".join(f"{Z.anu_p(d)} viharati {Z.SATI_TAIL_P}" for d in Z.DOMS)
SUTTA11["Tattha katamā sammāsati? Idha bhikkhu " + _SATI_P + " – ayaṃ vuccati \"sammāsati\"."] = (
    f"{TATTHA} {MAGGA['sammāsati'][0]}? Вот монах " + "; ".join(f"{Z.dwell(d)}, {Z.SATI_TAIL}" for d in Z.DOMS)
    + f", {DASH} {called(MAGGA['sammāsati'][1])}.")
JHANA4_P = ("vivicceva kāmehi vivicca akusalehi dhammehi savitakkaṃ savicāraṃ vivekajaṃ pītisukhaṃ paṭhamaṃ jhānaṃ "
            "upasampajja viharati; vitakkavicārānaṃ vūpasamā ajjhattaṃ sampasādanaṃ cetaso ekodibhāvaṃ avitakkaṃ avicāraṃ "
            "samādhijaṃ pītisukhaṃ dutiyaṃ jhānaṃ upasampajja viharati; pītiyā ca virāgā upekkhako ca viharati sato ca "
            "sampajāno sukhañca kāyena paṭisaṃvedeti, yaṃ taṃ ariyā ācikkhanti{d}\"upekkhako satimā sukhavihārī\"ti "
            "tatiyaṃ jhānaṃ upasampajja viharati; sukhassa ca pahānā dukkhassa ca pahānā pubbeva "
            "somanassadomanassānaṃ atthaṅgamā adukkhamasukhaṃ upekkhāsatipārisuddhiṃ catutthaṃ jhānaṃ upasampajja viharati")
JHANA4_R = "; ".join([JH1, JH2, JH3, JH4])
JHANA4_R_NODASH = "; ".join([JH1, JH2, JH3_NODASH, JH4])
SUTTA11["Tattha katamo sammāsamādhi? Idha bhikkhu " + JHANA4_P.format(d=" ") + " – ayaṃ vuccati \"sammāsamādhi\"."] = (
    f"{TATTHA} {MAGGA['sammāsamādhi'][0]}? Вот монах, {JHANA4_R_NODASH} {DASH} {called(MAGGA['sammāsamādhi'][1])}.")
_DEV_P = ("Tattha katamā sammādiṭṭhi? Idha bhikkhu sammādiṭṭhiṃ bhāveti " + NIS_P + ", "
          + "…pe… ".join(f"{MAGGA_P_ACC[k]} bhāveti" for k in list(MAGGA)[1:]) + " " + NIS_P + ".")
SUTTA11[_DEV_P] = (
    f"{TATTHA} {MAGGA['sammādiṭṭhi'][0]}? Вот монах развивает {MAGGA_ACC['sammādiṭṭhi'][0]}, {NISSITA['n']}, "
    + "… ".join(f"развивает {MAGGA_ACC[k][0]}" for k in list(MAGGA)[1:])
    + f", {NISSITA[MAGGA_ACC['sammāsamādhi'][1]]}.")
ARIYO8_P = "Ariyo aṭṭhaṅgiko maggo, seyyathidaṃ – " + EIGHT_P + "."
ARIYO8_R = f"Благородный {EIGHTFOLD}, а именно {DASH} {F.EIGHT_FACTORS}."
_RU4 = open(os.path.join(S.RU_DIR, "4-saccavibhango.md"), encoding="utf-8").read()
assert "благородный " + EIGHTFOLD + ", а именно " + DASH + " " + F.EIGHT_FACTORS + "." in _RU4   # ch. 4
LINES11 = {
    ARIYO8_P: ARIYO8_R,
    "Aṭṭhaṅgiko maggo – " + EIGHT_P + ".": f"{cap(EIGHTFOLD)} {DASH} {F.EIGHT_FACTORS}.",
    "Pañcaṅgiko maggo – " + FIVE_P + ".": f"{cap(FIVEFOLD)} {DASH} {F.FIVE_FACTORS}.",
    "Aṭṭhaṅgiko maggo – sammādiṭṭhi…pe… sammāsamādhi.":
        f"{cap(EIGHTFOLD)} {DASH} {MAGGA['sammādiṭṭhi'][0]}… {MAGGA['sammāsamādhi'][0]}.",
}

# ================================================================ 7. chapter 12 Suttanta: lemmas, terms, bodies
LEM = {   # Pāli lemma (as quoted; "…"nti -> "…ṃ"), lower case -> Russian (lower case)
    "idhā": "здесь", "bhikkhū": "монах", "pātimokkhaṃ": "свод монашеских правил", "saṃvaro": "сдержанность",
    "saṃvuto": "сдержанный",
    "pātimokkhasaṃvarasaṃvuto": "сдержанный сдержанностью свода монашеских правил",
    "viharatī": "пребывает",
    "ācāragocarasampanno": "обладающий подобающим поведением и подходящими местами посещения",
    "gocaro": "подходящее место посещения",
    "aṇumattesu vajjesu bhayadassāvī": "видящий опасность в малейших проступках",
    "samādāya sikkhati sikkhāpadesū": "принимает на себя правила обучения и обучается им",
    "indriyesu guttadvāro": "охраняющий врата чувств", "bhojane mattaññū": "знающий меру в еде",
    "sātaccaṃ": "постоянство", "nepakkaṃ": "благоразумие",
    "bodhipakkhikānaṃ dhammānaṃ bhāvanānuyogamanuyutto": "преданный развитию явлений, способствующих пробуждению",
    "sampajāno": "ясно понимающий", "vivittaṃ": "уединённое", "senāsanaṃ": "жилище",
    "vivittaṃ senāsanaṃ bhajatī": "выбирает уединённое жилище", "araññaṃ": "лес", "rukkhamūlaṃ": "подножие дерева",
    "vanapatthaṃ": "лесная чаща", "appasaddaṃ": "тихое", "appanigghosaṃ": "бесшумное",
    "araññagato vā rukkhamūlagato vā suññāgāragato vā": "удалившись в лес, или к подножию дерева, или в пустой дом",
    "nisīdati pallaṅkaṃ ābhujitvā": "садится, скрестив ноги", "ujuṃ kāyaṃ paṇidhāyā": "держа тело прямо",
    "parimukhaṃ satiṃ upaṭṭhapetvā": "установив осознанность перед собой",
    "abhijjhaṃ loke pahāyā": "оставив алчность в отношении мира",
    "vigatābhijjhena cetasā": "с умом, свободным от алчности",
    "abhijjhāya cittaṃ parisodhetī": "очищает ум от алчности",
    "byāpādapadosaṃ pahāyā": "оставив недоброжелательность и сильную злобу",
    "abyāpannacitto": "с умом, свободным от недоброжелательности",
    "byāpādapadosā cittaṃ parisodhetī": "очищает ум от недоброжелательности и сильной злобы",
    "thinamiddhaṃ pahāyā": "оставив вялость и сонливость",
    "vigatathinamiddho": "свободный от вялости и сонливости", "ālokasaññī": "воспринимающий свет",
    "sato sampajāno": "осознанный и ясно понимающий", "sato ca sampajāno": "осознанный и ясно понимающий",
    "thinamiddhā cittaṃ parisodhetī": "очищает ум от вялости и сонливости",
    "uddhaccakukkuccaṃ pahāyā": "оставив беспокойство и угрызения", "anuddhato": "без беспокойства",
    "vūpasantacitto": "с успокоенным умом", "ajjhattaṃ vūpasantacitto": "с умом, успокоенным внутри",
    "uddhaccakukkuccā cittaṃ parisodhetī": "очищает ум от беспокойства и угрызений",
    "vicikicchaṃ pahāyā": "оставив колебание", "tiṇṇavicikiccho": "преодолевший колебание",
    "akathaṃkathī kusalesu dhammesū": "свободный от недоумений в отношении благих явлений",
    "vicikicchāya cittaṃ parisodhetī": "очищает ум от колебания",
    "ime pañca nīvaraṇe pahāyā": "оставив эти пять помех", "cetaso upakkilese": "загрязнения ума",
    "paññāya dubbalīkaraṇe": "ослабляющие мудрость",
    "vivicceva kāmehi vivicca akusalehi dhammehī":
        "полностью уединившись от чувственных удовольствий, уединившись от неблагих явлений",
    "savitakkaṃ savicāraṃ": "с направленной мыслью и удержанием мысли", "vivekajaṃ": "рождённые уединением",
    "pītisukhaṃ": "с восторгом и счастьем", "paṭhamaṃ": "первое", "jhānaṃ": "медитативное погружение",
    "upasampajjā": "входит",
    "vitakkavicārānaṃ vūpasamā": "с затиханием направленной мысли и удержания мысли", "ajjhattaṃ": "внутри себя",
    "sampasādanaṃ": "ясность", "cetaso ekodibhāvaṃ": "единение ума",
    "avitakkaṃ avicāraṃ": "без направленной мысли и без удержания мысли", "samādhijaṃ": "рождённые сосредоточением",
    "dutiyaṃ": "второе", "pītiyā ca virāgā": "с угасанием восторга", "upekkhako": "невозмутимый",
    "sukhañca kāyena paṭisaṃvedetī": "испытывает телом счастье",
    "yaṃ taṃ ariyā ācikkhantī": "так что благородные говорят о нём",
    "upekkhako satimā sukhavihārī": "невозмутимый, осознанный, пребывающий в счастье", "tatiyaṃ": "третье",
    "sukhassa ca pahānā dukkhassa ca pahānā": "с устранением приятного и с устранением болезненного",
    "pubbeva somanassadomanassānaṃ atthaṅgamā": "с исчезновением ещё прежде радости и уныния",
    "adukkhamasukhaṃ": "которое ни болезненно, ни приятно",
    "upekkhāsatipārisuddhiṃ": "с чистотой невозмутимости и осознанности", "catutthaṃ": "четвёртое",
    "sabbaso rūpasaññānaṃ samatikkamā": "с полным преодолением восприятий материальной формы",
    "paṭighasaññānaṃ atthaṅgamā": "с исчезновением восприятий соударения",
    "nānattasaññānaṃ amanasikārā": "без внимания к восприятиям разнообразия",
    "ananto ākāso": "пространство бесконечно", "ākāsānañcāyatanaṃ": "сфера бесконечного пространства",
    "sabbaso ākāsānañcāyatanaṃ samatikkammā": "полностью преодолев сферу бесконечного пространства",
    "anantaṃ viññāṇaṃ": "сознание бесконечно", "viññāṇañcāyatanaṃ": "сфера бесконечного сознания",
    "sabbaso viññāṇañcāyatanaṃ samatikkammā": "полностью преодолев сферу бесконечного сознания",
    "natthi kiñcī": "нет ничего", "ākiñcaññāyatanaṃ": "сфера отсутствия чего-либо",
    "sabbaso ākiñcaññāyatanaṃ samatikkammā": "полностью преодолев сферу отсутствия чего-либо",
    "nevasaññīnāsaññī": "ни воспринимающий, ни невоспринимающий",
    "nevasaññānāsaññāyatanaṃ": "сфера ни восприятия, ни невосприятия",
    "pubbarattāpararattaṃ jāgariyānuyogamanuyutto": "в начале и в конце ночи преданный бодрствованию",
}
# root strings (^2-508) built from the lemmas, so lemma and root agree
ROOT_SILA = (f"Здесь монах пребывает {LEM['pātimokkhasaṃvarasaṃvuto'].replace('сдержанный', 'сдержанным', 1)}, "
             "обладающим подобающим поведением и подходящими местами посещения, видящим опасность в малейших проступках; "
             "он принимает на себя правила обучения и обучается им, охраняет врата чувств, знает меру в еде, в начале и "
             "в конце ночи предан бодрствованию, с постоянством и благоразумием предан развитию явлений, способствующих "
             "пробуждению.")
VAR_SAMMINJ = " [вариант написания (Sī., Syā.): sammiñjite]"
SAMPAJ = {   # the sampajānakārī situations (pi-4 ^4-182 words; pi-4 Russian «действует с ясным пониманием»)
    "abhikkante paṭikkante": "идя вперёд и идя назад", "ālokite vilokite": "смотря прямо и смотря по сторонам",
    "samiñjite pasārite": "сгибая и распрямляя руки и ноги",
    "saṅghāṭipattacīvaradhāraṇe": "нося накидку, чашу для подаяния и одеяние",
    "asite pīte khāyite sāyite": "когда ест, пьёт, жуёт и пробует на вкус",
    "uccārapassāvakamme": "справляя большую и малую нужду",
    "gate ṭhite nisinne sutte jāgarite bhāsite tuṇhībhāve": "когда ходит, стоит, сидит, засыпает, бодрствует, говорит и молчит",
}
SK = "действует с ясным пониманием"
ROOT_SAMPAJ = ("Идя вперёд и идя назад, он действует с ясным пониманием, смотря прямо и смотря по сторонам, он действует "
               "с ясным пониманием, сгибая" + VAR_SAMMINJ + " и распрямляя руки и ноги, он действует с ясным пониманием, "
               "нося накидку, чашу для подаяния и одеяние, он действует с ясным пониманием, когда ест, пьёт, жуёт и "
               "пробует на вкус, он действует с ясным пониманием, справляя большую и малую нужду, он действует с ясным "
               "пониманием, когда ходит, стоит, сидит, засыпает, бодрствует, говорит и молчит, он действует с ясным "
               "пониманием.")
_PI4 = "\n".join(open(os.path.join(S.ROOT, r"AI_translation\russian\pi-4-russian-plain-rails_split_chapters", f),
                      encoding="utf-8").read() for f in os.listdir(os.path.join(
                          S.ROOT, r"AI_translation\russian\pi-4-russian-plain-rails_split_chapters")) if f.endswith(".md"))
assert ROOT_SAMPAJ.replace(VAR_SAMMINJ, "") in _PI4
ROOT_SENASANA = ("Он выбирает уединённое жилище: лес, подножие дерева, гору, ущелье, горную пещеру, кладбище, лесную чащу, "
                 "открытое место, копну соломы, тихое, бесшумное, лишённое людской суеты, укрытое от людей "
                 "[вариант написания (Sī., Syā.): manussarāhaseyyakaṃ], подходящее для уединения.")
ROOT_SIT = ("Удалившись в лес, или к подножию дерева, или в пустой дом, он садится, скрестив ноги, держа тело прямо, "
            "установив осознанность перед собой.")
assert "он садится, скрестив ноги, держа тело прямо, установив осознанность перед собой" in _PI4
ROOT_NIV = [
    "Оставив алчность в отношении мира, он пребывает с умом, свободным от алчности, очищает ум от алчности.",
    "Оставив недоброжелательность и сильную злобу, он пребывает с умом, свободным от недоброжелательности, сострадая "
    "всем живым существам и желая им блага, очищает ум от недоброжелательности и сильной злобы.",
    "Оставив вялость и сонливость, он пребывает свободным от вялости и сонливости, воспринимающим свет, осознанным и "
    "ясно понимающим, очищает ум от вялости и сонливости.",
    "Оставив беспокойство и угрызения, он пребывает без беспокойства, с умом, успокоенным внутри, очищает ум от "
    "беспокойства и угрызений.",
    "Оставив колебание, он пребывает преодолевшим колебание, свободным от недоумений в отношении благих явлений, "
    "очищает ум от колебания.",
]
ROOT_JHANA = ("Оставив эти пять помех, загрязнения ума, ослабляющие мудрость, он, " + JHANA4_R + "; "
              + "; ".join([ARUPA1, ARUPA2, ARUPA3, ARUPA4]) + ".")
ROOT_508 = " ".join([ROOT_SILA, ROOT_SAMPAJ, ROOT_SENASANA, ROOT_SIT] + ROOT_NIV + [ROOT_JHANA])

TERM12 = {   # question / answer terms of the word commentary: Pāli -> (nom, ins)
    "anācāro": ("неподобающее поведение", "неподобающим поведением"),
    "ācāro": ("подобающее поведение", "подобающим поведением"),
    "agocaro": ("неподходящее место посещения", "неподходящим местом посещения"),
    "gocaro": ("подходящее место посещения", "подходящим местом посещения"),
    "aṇumattā vajjā": ("малейшие проступки", "малейшими проступками"),
    "sikkhā": ("обучение", "обучением"), "sikkhāyo": ("виды обучения", "видами обучения"),
    "indriyesu aguttadvāratā": ("неохранение врат чувств", "неохранением врат чувств"),
    "indriyesu guttadvāratā": ("охранение врат чувств", "охранением врат чувств"),
    "bhojane amattaññutā": ("незнание меры в еде", "незнанием меры в еде"),
    "bhojane mattaññutā": ("знание меры в еде", "знанием меры в еде"),
    "bodhipakkhikā dhammā": ("явления, способствующие пробуждению", "явлениями, способствующими пробуждению"),
    "sati": ("осознанность", "осознанностью"), "sampajaññaṃ": ("ясное понимание", "ясным пониманием"),
    "abhijjhā": ("алчность", "алчностью"), "loko": ("мир", "миром"), "cittaṃ": ("ум", "умом"),
    "byāpādo": ("недоброжелательность", "недоброжелательностью"), "padoso": ("сильная злоба", "сильной злобой"),
    "thinaṃ": ("вялость", "вялостью"), "middhaṃ": ("сонливость", "сонливостью"),
    "saññā": ("восприятие", "восприятием"), "uddhaccaṃ": ("беспокойство", "беспокойством"),
    "kukkuccaṃ": ("угрызения", "угрызениями"), "vicikicchā": ("колебание", "колебанием"),
    "kāmā": ("чувственные удовольствия", "чувственными удовольствиями"),
    "akusalā dhammā": ("неблагие явления", "неблагими явлениями"),
    "vitakko": ("направленная мысль", "направленной мыслью"), "vicāro": ("удержание мысли", "удержанием мысли"),
    "pīti": ("восторг", "восторгом"), "sukhaṃ": ("счастье", "счастьем"),
    "somanassaṃ": ("радость", "радостью"), "domanassaṃ": ("уныние", "унынием"),
    "upekkhā": ("невозмутимость", "невозмутимостью"), "kāyo": ("тело", "телом"),
    "rūpasaññā": ("восприятие материальной формы", None), "rūpasaññāyo": (None, "восприятиями материальной формы"),
    "paṭighasaññā": ("восприятие соударения", None), "paṭighasaññāyo": (None, "восприятиями соударения"),
    "nānattasaññā": ("восприятие разнообразия", None), "nānattasaññāyo": (None, "восприятиями разнообразия"),
    "ākāso": ("пространство", "пространством"),
}
# ^2-594 (bodily sukha / dukkha after "sukhassa ca pahānā dukkhassa ca pahānā"): «приятное» / «болезненное» (as the lemma)
TERM_594 = {"sukhaṃ": ("приятное", "приятным"), "dukkhaṃ": ("болезненное", "болезненным")}

DEF12 = {   # Pāli body -> (Russian, comma before the dash)
    "Kāyiko vītikkamo, vācasiko vītikkamo, kāyikavācasiko vītikkamo":
        ("Нарушение телом, нарушение речью, нарушение телом и речью", False),                 # pi-1 ^1-1368
    "Kāyiko avītikkamo, vācasiko avītikkamo, kāyikavācasiko avītikkamo":
        ("Отсутствие нарушений телом, отсутствие нарушений речью, отсутствие нарушений телом и речью", False),  # ^1-1370
    "Yā sati anussati paṭissati sati saraṇatā dhāraṇatā apilāpanatā asammusanatā sati satindriyaṃ satibalaṃ sammāsati":
        (SATI_FULL, True),
    "Yā sati anussati paṭissati…pe… sammāsati": (SATI_PE3, True),
    "Yā sati anussati…pe… sammāsati": (SATI_PE2, True),
    "Yā paññā pajānanā vicayo pavicayo dhammavicayo sallakkhaṇā upalakkhaṇā paccupalakkhaṇā paṇḍiccaṃ kosallaṃ "
    "nepuññaṃ vebhabyā cintā upaparikkhā bhūrīmedhā pariṇāyikā vipassanā sampajaññaṃ patodo paññā paññindriyaṃ "
    "paññābalaṃ paññāsatthaṃ paññāpāsādo paññāāloko paññāobhāso paññāpajjoto paññāratanaṃ amoho dhammavicayo "
    "sammādiṭṭhi": (PANNA_FULL, True),
    "Yā paññā pajānanā…pe… amoho dhammavicayo sammādiṭṭhi": (PANNA_PE2, True),
    "Yo rāgo sārāgo…pe… cittassa sārāgo": (RAGA_PE, True),
    "Pañcupādānakkhandhā loko": (Z.WORLD5.replace("И пять", "Пять"), False),
    "Yaṃ cittaṃ mano mānasaṃ…pe… tajjāmanoviññāṇadhātu": (CITTA_PE, True),
    "Yo cittassa āghāto paṭighāto paṭighaṃ paṭivirodho kopo pakopo sampakopo doso padoso sampadoso cittassa byāpatti "
    "manopadoso kodho kujjhanā kujjhitattaṃ doso dussanā dussitattaṃ [dūsanā dūsitattaṃ (syā.)] byāpatti byāpajjanā "
    "byāpajjitattaṃ virodho paṭivirodho caṇḍikkaṃ asuropo anattamanatā cittassa": (BYAPADA_VAR, True),
    "Yo cittassa āghāto…pe… caṇḍikkaṃ asuropo anattamanatā cittassa": (BYAPADA_PE, True),
    "Yā cittassa akalyatā akammaññatā olīyanā sallīyanā līnaṃ līyanā līyitattaṃ thinaṃ thiyanā thiyitattaṃ "
    "[thīyanā thīyitattaṃ (sī. syā.)] cittassa": (THINA_VAR, True),
    "Yā kāyassa akalyatā akammaññatā onāho pariyonāho antosamorodho middhaṃ suppaṃ pacalāyikā suppaṃ suppanā "
    "suppitattaṃ": (MIDDHA, True),
    "Yā saññā sañjānanā sañjānitattaṃ": (SANNA, True),
    "Yaṃ cittassa uddhaccaṃ avūpasamo cetaso vikkhepo bhantattaṃ cittassa": (UDDHACCA, True),
    "Akappiye kappiyasaññitā, kappiye akappiyasaññitā, avajje vajjasaññitā, vajje avajjasaññitā, yaṃ evarūpaṃ "
    "kukkuccaṃ kukkuccāyanā kukkuccāyitattaṃ cetaso vippaṭisāro manovilekhā": (KUKKUCCA, True),
    "Yā kaṅkhā kaṅkhāyanā kaṅkhāyitattaṃ vimati vicikicchā dveḷhakaṃ dvidhāpatho saṃsayo anekaṃsaggāho āsappanā "
    "parisappanā apariyogāhaṇā chambhitattaṃ cittassa manovilekho": (VICI_FULL, True),
    "Yā kaṅkhā kaṅkhāyanā kaṅkhāyitattaṃ chambhitattaṃ cittassa manovilekho": (VICI_SHORT, True),   # as written (no …pe…)
    "Chando kāmo, rāgo kāmo, chandarāgo kāmo, saṅkappo kāmo, rāgo kāmo, saṅkapparāgo kāmo":
        ("Чувственным удовольствием является желание, чувственным удовольствием является страсть, чувственным "
         "удовольствием является страстное желание, чувственным удовольствием является помысел, чувственным "
         "удовольствием является страсть, чувственным удовольствием является страсть к помыслам", False),
    "Kāmacchando, byāpādo, thinaṃ, middhaṃ, uddhaccaṃ, kukkuccaṃ, vicikicchā":
        ("Чувственное желание, недоброжелательность, вялость, сонливость, беспокойство, угрызения, колебание", False),
    "Yo takko vitakko saṅkappo appanā byappanā cetaso abhiniropanā sammāsaṅkappo": (VITAKKA_FULL, True),
    "Yo takko vitakko…pe… sammāsaṅkappo": (VITAKKA_PE, True),
    "Yo cāro vicāro anuvicāro upavicāro cittassa anusandhanatā anupekkhanatā": (VICARA_FULL, True),
    "Yo cāro anucāro vicāro anuvicāro upavicāro cittassa anusandhanatā anupekkhanatā": (VICARA_ANU, True),
    "Yā pīti pāmojjaṃ āmodanā pamodanā hāso pahāso vitti odagyaṃ attamanatā cittassa": (PITI_FULL, True),
    "Yaṃ cetasikaṃ sātaṃ cetasikaṃ sukhaṃ cetosamphassajaṃ sātaṃ sukhaṃ vedayitaṃ cetosamphassajā sātā sukhā vedanā":
        (SUKHA_C, True),
    "Yaṃ cetasikaṃ asātaṃ cetasikaṃ dukkhaṃ cetosamphassajaṃ asātaṃ dukkhaṃ vedayitaṃ cetosamphassajā asātā dukkhā "
    "vedanā": (DOMANASSA, True),
    "Yaṃ kāyikaṃ sātaṃ kāyikaṃ sukhaṃ kāyasamphassajaṃ sātaṃ sukhaṃ vedayitaṃ kāyasamphassajā sātā sukhā vedanā":
        (SUKHA_K, True),
    "Yaṃ kāyikaṃ asātaṃ kāyikaṃ dukkhaṃ kāyasamphassajaṃ asātaṃ dukkhaṃ vedayitaṃ kāyasamphassajā asātā dukkhā vedanā":
        (DUKKHA_K, True),
    "Yā upekkhā upekkhanā ajjhupekkhanā majjhattatā cittassa": (UPEKKHA, True),
    "Saññākkhandho, saṅkhārakkhandho, viññāṇakkhandho":
        (", ".join(cap(S.AGG[a]["khandha"]) if i == 0 else S.AGG[a]["khandha"]
                   for i, a in enumerate(("sanna", "sankhara", "vinnana"))), False),
    "Rūpāvacarasamāpattiṃ samāpannassa vā upapannassa vā diṭṭhadhammasukhavihārissa vā saññā sañjānanā sañjānitattaṃ":
        ("Восприятие, узнавание, состояние узнавания того, кто вошёл в медитативное достижение, относящееся к миру "
         "форм, или того, кто переродился в мире форм, или того, кто пребывает в счастье в этой жизни", True),
    "Rūpasaññā saddasaññā…pe… phoṭṭhabbasaññā": ("Восприятие видимых форм, восприятие звуков… восприятие осязаемого",
                                                 False),
    "Asamāpannassa manodhātu samaṅgissa vā manoviññāṇadhātu samaṅgissa vā saññā sañjānanā sañjānitattaṃ":
        ("Восприятие, узнавание, состояние узнавания того, кто не вошёл в медитативное достижение и наделён элементом "
         "ума или наделён элементом умственного сознания", True),
    "Yo ākāso ākāsagataṃ aghaṃ aghagataṃ vivaro vivaragataṃ asamphuṭṭhaṃ catūhi mahābhūtehi": (SPACE, True),
    "Yāni tāni vajjāni appamattakāni oramattakāni lahusāni lahusammatāni saṃyamakaraṇīyāni saṃvarakaraṇīyāni "
    "cittuppādakaraṇīyāni manasikārapaṭibaddhāni":
        ("Те проступки, которые незначительны, мелки, легки, считаются лёгкими, исправляются обузданием, исправляются "
         "сдержанностью, исправляются решением ума, связаны с вниманием", True),
}
for _k in ("Yā kaṅkhā kaṅkhāyanā kaṅkhāyitattaṃ vimati vicikicchā dveḷhakaṃ dvidhāpatho saṃsayo anekaṃsaggāho āsappanā "
           "parisappanā apariyogāhaṇā chambhitattaṃ cittassa manovilekho",):
    pass
in_pi1("нарушение телом, нарушение речью, нарушение телом и речью",
       "отсутствие нарушений телом, отсутствие нарушений речью, отсутствие нарушений телом и речью")
assert "Восприятие видимых форм в мире… восприятие звуков в мире… " in open(
    os.path.join(S.RU_DIR, "4-saccavibhango.md"), encoding="utf-8").read()   # rūpasaññā … (ch. 4)

SANTA = {   # santā (hoti / honti) samitā vūpasantā atthaṅgatā abbhatthaṅgatā appitā byappitā sositā visositā byantīkatā
    "pl": "успокоены, усмирены, умиротворены, угасли, полностью угасли, прекращены, полностью прекращены, иссушены, "
          "полностью иссушены, сведены на нет",
    "f": "успокоена, усмирена, умиротворена, угасла, полностью угасла, прекращена, полностью прекращена, иссушена, "
         "полностью иссушена, сведена на нет",
    "m": "успокоен, усмирён, умиротворён, угас, полностью угас, прекращён, полностью прекращён, иссушен, полностью "
         "иссушен, сведён на нет",
    "n": "успокоено, усмирено, умиротворено, угасло, полностью угасло, прекращено, полностью прекращено, иссушено, "
         "полностью иссушено, сведено на нет"}
assert SANTA["pl"] in Z.VINITA
SANTA_P = "samitā vūpasantā atthaṅgatā abbhatthaṅgatā appitā byappitā sositā visositā byantīkatā"
SODHETI = "очищает, тщательно очищает, полностью очищает, освобождает, тщательно освобождает, полностью освобождает"
CATTA = "оставлены, извергнуты, отпущены, устранены, отброшены, устранены и отброшены"
LABHA = Z.IDDHI[Z.IDDHI.index("обретение"):-1]   # обретение, получение, достижение, … вхождение
assert LABHA.startswith("обретение, получение, достижение, полное достижение, касание")
JATA = "родились, зародились, возникли, полностью возникли, проявились"         # jātā honti sañjātā nibbattā …
ATIKKANTA = "преодолел, миновал, полностью преодолел"                         # atikkanto hoti vītikkanto samatikkanto
SUBJ_SANTA = {   # Pāli subject before "santā hoti/honti …" -> (Russian, gender)
    "Ayaṃ abhijjhā imamhi loke": ("Эта алчность в этом мире", "f"),
    "Iti ayañca byāpādo ayañca padoso": ("Таким образом, и эта недоброжелательность, и эта сильная злоба", "pl"),
    "Iti idañca thinaṃ idañca middhaṃ": ("Таким образом, и эта вялость, и эта сонливость", "pl"),
    "Iti idañca uddhaccaṃ idañca kukkuccaṃ": ("Таким образом, и это беспокойство, и эти угрызения", "pl"),
    "Ayaṃ vicikicchā": ("Это колебание", "n"),
    "Ime pañca nīvaraṇā": ("Эти пять помех", "pl"),
    "Iti ayañca vitakko ayañca vicāro": ("Таким образом, и эта направленная мысль, и это удержание мысли", "pl"),
    "Ayaṃ pīti": ("Этот восторг", "m"),
    "Iti idañca sukhaṃ idañca dukkhaṃ": ("Таким образом, и это приятное, и это болезненное", "pl"),
    "Iti idañca somanassaṃ idañca domanassaṃ pubbeva": ("Таким образом, и эта радость, и это уныние ещё прежде", "pl"),
    "Imā paṭighasaññāyo": ("Эти восприятия соударения", "pl"),
}
PURIFY_X = {"imāya abhijjhāya": "этой алчности", "imamhā byāpādapadosā": "этих недоброжелательности и сильной злобы",
            "imamhā thinamiddhā": "этих вялости и сонливости", "imamhā uddhaccakukkuccā": "этих беспокойства и угрызений",
            "imāya vicikicchāya": "этого колебания"}
UPETO_SUBJ = {   # "<X> upeto hoti …" -> Russian instrumental phrase
    "Iminā pātimokkhasaṃvarena": "Этой сдержанностью свода монашеских правил",
    "Iti iminā ca ācārena iminā ca gocarena": "Таким образом, и этим подобающим поведением, и этим подходящим местом посещения",
    "Imāya indriyesu guttadvāratāya": "Этим охранением врат чувств",
    "Imāya bhojane mattaññutāya": "Этим знанием меры в еде",
    "Iti imāya ca satiyā iminā ca sampajaññena": "Таким образом, и этой осознанностью, и этим ясным пониманием",
    "Iti iminā ca vitakkena iminā ca vicārena":
        "Таким образом, и этой направленной мыслью, и этим удержанием мысли",
    "Imāya upekkhāya": "Этой невозмутимостью",
}
UPETO_TAIL = {" samupeto upāgato samupāgato upapanno sampanno samannāgato": Z.UPETO_FULL,
              "…pe… samannāgato": Z.UPETO_PE, " samupeto…pe… samannāgato": "он обладает, вполне обладает… наделён"}

# pi-1 sense restraint / food (^1-1352 … ^1-1355), pi-2 quotes the answer term
_A = PI1["^1-1352"]
AGUTTA = _A[_A.index("Вот человек"):_A.index(", – это называется неохранением")]
_G = PI1["^1-1354"]
GUTTA = _G[_G.index("Вот человек"):_G.index(", – это называется охранением")]
_M0 = PI1["^1-1353"]
AMATTA = _M0[_M0.index("Вот человек"):_M0.index(" – это называется незнанием")]
_M1 = PI1["^1-1355"]
MATTA = _M1[_M1.index("Вот человек"):_M1.index(" – это называется знанием")]
assert AMATTA.endswith(",") and MATTA.endswith(",")


def qterm(t, ctx=None):
    if ctx == 594 and t in TERM_594:
        return TERM_594[t]
    return TERM12[t]


def lemma_of(p):
    return LEM[low(p)]


SENT12 = {   # whole sentences (Pāli exactly as split) -> Russian
    # ^2-509, ^2-510
    "Imissā diṭṭhiyā, imissā khantiyā, imissā ruciyā, imasmiṃ ādāye, imasmiṃ dhamme, imasmiṃ vinaye, imasmiṃ "
    "dhammavinaye, imasmiṃ pāvacane, imasmiṃ brahmacariye, imasmiṃ satthusāsane.":
        "В этом воззрении, в этом приятии, в этом предпочтении, в этом выборе, в этом Учении, в этой дисциплине, в этом "
        "Учении и дисциплине, в этом слове, в этой святой жизни, в этом наставлении Учителя.",
    "Samaññāya bhikkhu, paṭiññāya bhikkhu, bhikkhatīti bhikkhu, bhikkhakoti bhikkhu, bhikkhācariyaṃ ajjhupagatoti bhikkhu, "
    "bhinnapaṭadharoti bhikkhu, bhindati pāpake akusale dhammeti bhikkhu, bhinnattā pāpakānaṃ akusalānaṃ dhammānaṃ "
    "bhikkhu, odhiso kilesānaṃ pahānā bhikkhu, anodhiso kilesānaṃ pahānā bhikkhu, sekkho bhikkhu, asekkho bhikkhu, "
    "nevasekkhanāsekkho bhikkhu, aggo bhikkhu, bhadro bhikkhu, maṇḍo bhikkhu, sāro bhikkhu, samaggena saṅghena "
    "ñatticatutthena kammena akuppena ṭhānārahena upasampanno bhikkhu.":
        "Монах по общепринятому названию, монах по собственному заявлению, монах, потому что просит подаяние, монах, "
        "потому что живёт подаянием, монах, потому что избрал жизнь сбора подаяния, монах, потому что носит одежду из "
        "лоскутов, монах, потому что разрушает дурные неблагие явления, монах, потому что дурные неблагие явления "
        "разрушены, монах благодаря частичному устранению омрачений, монах благодаря полному устранению омрачений, "
        "обучающийся монах, монах, завершивший обучение, монах, ни обучающийся, ни завершивший обучение, превосходный "
        "монах, хороший монах, отборный монах, монах-сердцевина, монах, получивший полное посвящение от единой общины "
        "процедурой с предложением и тремя объявлениями, неотменимой и соответствующей правилам.",
    # ^2-511
    "Sīlaṃ patiṭṭhā ādi caraṇaṃ saṃyamo saṃvaro mokkhaṃ pāmokkhaṃ kusalānaṃ dhammānaṃ samāpattiyā.":
        "Нравственность, опора, начало, поведение, обуздание, сдержанность, главное, первейшее для достижения благих "
        "явлений.",
    "Kāyiko avītikkamo, vācasiko avītikkamo, kāyikavācasiko avītikkamo.":
        "Отсутствие нарушений телом, отсутствие нарушений речью, отсутствие нарушений телом и речью.",
    # ^2-512 etc.
    "Iriyati vattati pāleti yapeti yāpeti carati viharati.": Z.VIHARATI,
    # ^2-513
    "Atthi ācāro, atthi anācāro.": "Есть подобающее поведение, есть неподобающее поведение.",
    "Sabbampi dussīlyaṃ anācāro.": "Всякая безнравственность является неподобающим поведением.",
    "Sabbopi sīlasaṃvaro ācāro.": "Всякая нравственная сдержанность является подобающим поведением.",
    # ^2-514
    "Atthi gocaro, atthi agocaro.": "Есть подходящее место посещения, есть неподходящее место посещения.",
    # ^2-515
    "Iti imesu aṇumattesu vajjesu vajjadassāvī ca hoti bhayadassāvī ca ādīnavadassāvī ca nissaraṇadassāvī ca.":
        "Таким образом, в этих малейших проступках он и видит проступок, и видит опасность, и видит вред, и видит "
        "выход.",
    # ^2-516
    "Catasso sikkhā – bhikkhūnaṃ bhikkhusikkhā, bhikkhunīnaṃ bhikkhunisikkhā, upāsakānaṃ upāsakasikkhā, upāsikānaṃ "
    "upāsikasikkhā.":
        f"Четыре вида обучения {DASH} обучение монахов для монахов, обучение монахинь для монахинь, обучение мирян для "
        f"мирян, обучение мирянок для мирянок.",
    "Iti imāsu sikkhāsu sabbena sabbaṃ sabbathā sabbaṃ asesaṃ nissesaṃ samādāya vattati.":
        "Таким образом, приняв эти виды обучения всецело, во всех отношениях, без остатка, полностью, он следует им.",
    # ^2-517, ^2-518
    "Atthi indriyesu guttadvāratā, atthi aguttadvāratā.": "Есть охранение врат чувств, есть неохранение врат чувств.",
    "Atthi bhojane mattaññutā, atthi bhojane amattaññutā.": "Есть знание меры в еде, есть незнание меры в еде.",
    # ^2-522
    "Iti te bodhipakkhike dhamme āsevati bhāveti bahulīkaroti.":
        "Таким образом, эти явления, способствующие пробуждению, он практикует, развивает, многократно повторяет.",
    "Satta bojjhaṅgā – " + ", ".join(k + "sambojjhaṅgo" for k in BOJ) + ".": SEVEN_LINE,
    # ^2-526, ^2-532
    "Santike cepi senāsanaṃ hoti, tañca anākiṇṇaṃ gahaṭṭhehi pabbajitehi.":
        "Даже если жилище находится вблизи, оно не заполнено домохозяевами и ушедшими в бездомность.",
    "Dūre cepi senāsanaṃ hoti, tañca anākiṇṇaṃ gahaṭṭhehi pabbajitehi.":
        "Даже если жилище находится вдали, оно не заполнено домохозяевами и ушедшими в бездомность.",
    "Tena taṃ vivittaṃ.": "Поэтому оно уединённое.",
    "Tena taṃ appasaddaṃ.": "Поэтому оно тихое.",
    # ^2-527
    "Mañcopi senāsanaṃ, pīṭhampi senāsanaṃ, bhisipi senāsanaṃ, bibbohanampi [bimbohanampi (sī. syā.)] senāsanaṃ, "
    "vihāropi senāsanaṃ, aḍḍhayogopi senāsanaṃ, pāsādopi senāsanaṃ, aṭṭopi senāsanaṃ, māḷopi senāsanaṃ, leṇampi "
    "senāsanaṃ, guhāpi senāsanaṃ, rukkhamūlampi senāsanaṃ, veḷugumbopi senāsanaṃ.":
        "И ложе является жилищем, и сиденье является жилищем, и матрас является жилищем, и подушка [вариант написания "
        "(Sī., Syā.): bimbohanampi] является жилищем, и обитель является жилищем, и навес является жилищем, и дворец "
        "является жилищем, и башня является жилищем, и дом с островерхой крышей является жилищем, и скальная келья "
        "является жилищем, и пещера является жилищем, и подножие дерева является жилищем, и бамбуковая роща является "
        "жилищем.",
    "Yattha vā pana bhikkhū paṭikkamanti sabbametaṃ senāsanaṃ.":
        "И где бы ни останавливались монахи, всё это является жилищем.",
    # ^2-528 … ^2-536
    "Imaṃ vivittaṃ senāsanaṃ bhajati sambhajati sevati nisevati saṃsevati.":
        "Это уединённое жилище он выбирает, занимает, посещает, часто посещает, постоянно посещает.",
    "Nikkhamitvā bahi indakhīlā sabbametaṃ araññaṃ.":
        "Всё, что находится за пределами пограничного столба, является лесом.",
    "Rukkhamūlaṃyeva rukkhamūlaṃ.": "Подножие дерева и есть подножие дерева.",
    "Pabbatoyeva pabbato.": "Гора и есть гора.", "Kandarāyeva kandarā.": "Ущелье и есть ущелье.",
    "Giriguhāyeva giriguhā.": "Горная пещера и есть горная пещера.", "Susānaṃyeva susānaṃ.": "Кладбище и есть кладбище.",
    "Abbhokāsoyeva abbhokāso.": "Открытое место и есть открытое место.",
    "Palālapuñjoyeva palālapuñjo.": "Копна соломы и есть копна соломы.",
    "Yadeva taṃ appasaddaṃ tadeva taṃ appanigghosaṃ.": "То, что тихое, то и бесшумное.",
    "Yadeva taṃ appanigghosaṃ tadeva taṃ vijanavātaṃ.": "То, что бесшумное, то и лишённое людской суеты.",
    "Yadeva taṃ vijanavātaṃ tadeva taṃ manussarāhasseyyakaṃ.": "То, что лишённое людской суеты, то и укрытое от людей.",
    "Yadeva taṃ manussarāhasseyyakaṃ tadeva taṃ paṭisallānasāruppaṃ.":
        "То, что укрытое от людей, то и подходящее для уединения.",
    "Araññagato vā hoti rukkhamūlagato vā suññāgāragato vā.":
        "Он удалился в лес, или к подножию дерева, или в пустой дом.",
    "Nisinno hoti pallaṅkaṃ ābhujitvā.": "Он сидит, скрестив ноги.",
    "Ujuko hoti kāyo ṭhito paṇihito.": "Тело прямое, устойчивое, правильно поставленное.",
    "Ayaṃ sati upaṭṭhitā hoti supaṭṭhitā nāsikagge vā mukhanimitte vā.":
        "Эта осознанность установлена, хорошо установлена на кончике носа или в области рта.",
    # ^2-538 …
    "Idaṃ cittaṃ vigatābhijjhaṃ hoti.": "Этот ум свободен от алчности.",
    "Atthi byāpādo, atthi padoso.": "Есть недоброжелательность, есть сильная злоба.",
    "Atthi byāpādo atthi padoso.": "Есть недоброжелательность, есть сильная злоба.",
    "Yo byāpādo so padoso, yo padoso so byāpādo.":
        "То, что есть недоброжелательность, есть сильная злоба; то, что есть сильная злоба, есть недоброжелательность.",
    "Idaṃ cittaṃ abyāpannaṃ hoti.": "Этот ум свободен от недоброжелательности.",
    "Atthi thinaṃ [thīnaṃ (sī. syā.)], atthi middhaṃ.":
        "Есть вялость [вариант написания (Sī., Syā.): thīnaṃ], есть сонливость.",
    "Atthi thinaṃ, atthi middhaṃ.": "Есть вялость, есть сонливость.",
    "Tassa thinamiddhassa cattattā vantattā muttattā pahīnattā paṭinissaṭṭhattā pahīnapaṭinissaṭṭhattā.":
        f"У него вялость и сонливость {CATTA}.",
    "Ayaṃ saññā ālokā hoti vivaṭā parisuddhā pariyodātā.": "Это восприятие светлое, открытое, чистое, ясное.",
    "Atthi uddhaccaṃ, atthi kukkuccaṃ.": "Есть беспокойство, есть угрызения.",
    "Idaṃ cittaṃ ajjhattaṃ santaṃ hoti samitaṃ vūpasantaṃ.": "Этот ум внутри успокоен, усмирён, умиротворён.",
    "Imaṃ vicikicchaṃ tiṇṇo hoti uttiṇṇo nittiṇṇo pāraṅgato pāramanuppatto.":
        "Это колебание он преодолел, превозмог, полностью превозмог, переправился через него, достиг другого берега.",
    "Imāya vicikicchāya kusalesu dhammesu na kaṅkhati na vicikicchati akathaṃkathī hoti nikkathaṃkathī vikathaṃkatho.":
        "Он не испытывает этого колебания в отношении благих явлений: не сомневается, не колеблется, свободен от "
        "недоумений, полностью свободен от недоумений, избавлен от недоумений.",
    "Ime pañca nīvaraṇā cittassa upakkilesā.": "Эти пять помех являются загрязнениями ума.",
    "Imehi pañcahi nīvaraṇehi anuppannā ceva paññā na uppajjati uppannā ca paññā nirujjhati.":
        "Из-за этих пяти помех и невозникшая мудрость не возникает, и возникшая мудрость прекращается.",
    "Iti imehi ca kāmehi imehi ca akusalehi dhammehi vivitto hoti.":
        "Таким образом, он уединён и от этих чувственных удовольствий, и от этих неблагих явлений.",
    "Atthi vitakko, atthi vicāro.": "Есть направленная мысль, есть удержание мысли.",
    "Atthi pīti, atthi sukhaṃ.": "Есть восторг, есть счастье.",
    "Idaṃ sukhaṃ imāya pītiyā sahagataṃ hoti sahajātaṃ saṃsaṭṭhaṃ sampayuttaṃ.":
        "Это счастье сопровождается этим восторгом, рождено вместе с ним, соединено с ним, связано с ним.",
    "Atthi sukhaṃ, atthi dukkhaṃ.": "Есть приятное, есть болезненное.",
    "Atthi somanassaṃ, atthi domanassaṃ.": "Есть радость, есть уныние.",
    "Idaṃ sukhaṃ iminā kāyena paṭisaṃvedeti.": "Это счастье он испытывает этим телом.",
    "Ariyā vuccanti buddhā ca buddhasāvakā ca.": "Благородными называются будды и ученики будд.",
    "Te imaṃ ācikkhanti desenti paññapenti [paññāpenti (sī. syā.)] paṭṭhapenti vivaranti vibhajanti uttāniṃ karonti "
    "pakāsenti.":
        "Они говорят об этом, излагают, сообщают [вариант написания (Sī., Syā.): paññāpenti], устанавливают, раскрывают, "
        "разбирают, проясняют, разъясняют.",
    "Iti imāya ca upekkhāya imāya ca satiyā iminā ca sukhena samannāgato iriyati vattati pāleti yapeti yāpeti carati "
    "viharati.":
        "Таким образом, наделённый и этой невозмутимостью, и этой осознанностью, и этим счастьем, " + lc(Z.VIHARATI),
    "Ayaṃ sati imāya upekkhāya vivaṭā hoti parisuddhā pariyodātā.":
        "Эта осознанность благодаря этой невозмутимости открытая, чистая, ясная.",
    "Imā rūpasaññāyo atikkanto hoti vītikkanto samatikkanto.":
        f"Эти восприятия материальной формы он {ATIKKANTA}.",
    "Imā nānattasaññāyo na manasi karoti.": "Этим восприятиям разнообразия он не уделяет внимания.",
    "Tasmiṃ ākāse cittaṃ ṭhapeti saṇṭhapeti anantaṃ pharati.":
        "В этом пространстве он устанавливает ум, прочно устанавливает его и охватывает его как бесконечное.",
    "Taṃyeva ākāsaṃ viññāṇena phuṭṭhaṃ manasi karoti anantaṃ pharati.":
        "Он уделяет внимание тому самому пространству, охваченному сознанием, и охватывает его как бесконечное.",
    "Taṃyeva viññāṇaṃ bhāveti vibhāveti antarabhāveti, \"natthi kiñcī\"ti passati.":
        "То самое сознание он развивает, рассеивает, делает исчезнувшим и видит: «Нет ничего».",
    "Taṃyeva ākiñcaññāyatanaṃ santato manasi karoti saṅkhārāvasesasamāpattiṃ bhāveti.":
        "Той самой сфере отсутствия чего-либо он уделяет внимание как спокойной, развивает медитативное достижение с "
        "остатком формирующих факторов.",
    "Imaṃ ākāsānañcāyatanaṃ atikkanto hoti vītikkanto samatikkanto.":
        f"Эту сферу бесконечного пространства он {ATIKKANTA}.",
    "Imaṃ viññāṇañcāyatanaṃ atikkanto hoti vītikkanto samatikkanto.": f"Эту сферу бесконечного сознания он {ATIKKANTA}.",
    "Imaṃ ākiñcaññāyatanaṃ atikkanto hoti vītikkanto samatikkanto.": f"Эту сферу отсутствия чего-либо он {ATIKKANTA}.",
    "Tassa uddhaccakukkuccassa cattattā vantattā muttattā pahīnattā paṭinissaṭṭhattā pahīnapaṭinissaṭṭhattā.":
        f"У него беспокойство и угрызения {CATTA}.",
    "Gaṇanānupubbatā [gaṇanānupubbato (syā.) evamuparipi] paṭhamaṃ.":
        "Первое по порядку счёта [вариант написания (Syā.): gaṇanānupubbato; так же и далее].",
    "Idaṃ paṭhamaṃ samāpajjatīti paṭhamaṃ.": "В него он входит первым, поэтому оно первое.",
    "Gaṇanānupubbatā dutiyaṃ.": "Второе по порядку счёта.",
    "Idaṃ dutiyaṃ samāpajjatīti dutiyaṃ.": "В него он входит вторым, поэтому оно второе.",
    "Gaṇanānupubbatā tatiyaṃ.": "Третье по порядку счёта.",
    "Idaṃ tatiyaṃ samāpajjatīti tatiyaṃ.": "В него он входит третьим, поэтому оно третье.",
    "Gaṇanānupubbatā catutthaṃ, idaṃ catutthaṃ samāpajjatīti catutthaṃ.":
        "Четвёртое по порядку счёта, в него он входит четвёртым, поэтому оно четвёртое.",
    "Vitakko, vicāro, pīti, sukhaṃ, cittassekaggatā.": "Направленная мысль, удержание мысли, восторг, счастье, "
                                                         "однонаправленность ума.",
    "Sampasādo, pītisukhaṃ, cittassekaggatā.": "Ясность, восторг и счастье, однонаправленность ума.",
    "Upekkhā, sati, sampajaññaṃ, sukhaṃ, cittassekaggatā.":
        "Невозмутимость, осознанность, ясное понимание, счастье, однонаправленность ума.",
    "Upekkhā, sati, cittassekaggatā.": "Невозмутимость, осознанность, однонаправленность ума.",
    "Yaṃ ajjhattaṃ paccattaṃ.": "То, что " + T.INT_SELF + ".",
    "Yā saddhā saddahanā okappanā abhippasādo.": "То, что есть " + SADDHA4 + ".",
    "Yā cittassa ṭhiti…pe… sammāsamādhi.": SAMADHI_PE1 + ".",
    "Yo cetasiko vīriyārambho…pe… sammāvāyāmo.": VIRIYA_PE + ".",
    "Yā paññā pajānanā…pe… amoho dhammavicayo sammādiṭṭhi.": PANNA_PE2 + ".",
    "Yaṃ cetasikaṃ neva sātaṃ nāsātaṃ cetosamphassajaṃ adukkhamasukhaṃ vedayitaṃ cetosamphassajā adukkhamasukhā vedanā.":
        cap(ADM_C) + ".",
}
assert T.INT_SELF == "внутреннее и собственное"
assert F.PALI3["upekkhā"] == ("Yaṃ cetasikaṃ neva sātaṃ nāsātaṃ cetosamphassajaṃ adukkhamasukhaṃ vedayitaṃ "
                              "cetosamphassajā adukkhamasukhā vedanā")

for _p, _r in (("Dūrānametaṃ", "отдалённых"), ("Vanasaṇḍānametaṃ", "лесных"),
               ("Bhīsanakānametaṃ [bhiṃsanakānametaṃ (sī. syā.)]",
                "пугающих [вариант написания (Sī., Syā.): bhiṃsanakānametaṃ]"),
               ("Salomahaṃsānametaṃ", "наводящих трепет"), ("Pariyantānametaṃ", "находящихся на окраине"),
               ("Na manussūpacārānametaṃ", "удалённых от людских мест"), ("Durabhisambhavānametaṃ", "труднодоступных")):
    SENT12[f"{_p} senāsanānaṃ adhivacanaṃ."] = f"Это наименование {_r} жилищ."   # adhivacana [pi-1 «наименование»]
for _ord in ("paṭhamassa", "dutiyassa", "tatiyassa", "catutthassa"):
    _o = {"paṭhamassa": "первого", "dutiyassa": "второго", "tatiyassa": "третьего", "catutthassa": "четвёртого"}[_ord]
    SENT12[f"Yo {_ord} jhānassa lābho paṭilābho patti sampatti phusanā sacchikiriyā upasampadā."] = (
        f"То, что есть обретение {_o} медитативного погружения, " + LABHA[len("обретение, "):] + ".")
for _p, _r in (("ākāsānañcāyatanassa", "сферы бесконечного пространства"),
               ("viññāṇañcāyatanassa", "сферы бесконечного сознания"),
               ("ākiñcaññāyatanassa", "сферы отсутствия чего-либо"),
               ("nevasaññānāsaññāyatanassa", "сферы ни восприятия, ни невосприятия")):
    SENT12[f"Yo {_p} lābho paṭilābho patti sampatti phusanā sacchikiriyā upasampadā."] = (
        f"То, что есть обретение {_r}, " + LABHA[len("обретение, "):] + ".")
for _p, _r in (("ākāsānañcāyatanaṃ", "в сферу бесконечного пространства"),
               ("viññāṇañcāyatanaṃ", "в сферу бесконечного сознания"),
               ("ākiñcaññāyatanaṃ", "в сферу отсутствия чего-либо"),
               ("nevasaññānāsaññāyatanaṃ", "в сферу ни восприятия, ни невосприятия")):
    SENT12[f"{cap(_p)} samāpannassa vā upapannassa vā diṭṭhadhammasukhavihārissa vā cittacetasikā dhammā."] = (
        f"{cap(CITTACET)} того, кто вошёл {_r}, или того, кто переродился в ней, или того, кто пребывает в ней в "
        f"счастье в этой жизни.")
in_pi1("для пребывания в счастье в этой жизни")


def sent12(s, ctx=None):
    """one sentence of the ch. 12 word commentary."""
    if s in SENT12:
        return SENT12[s]
    # lemma at the start: '"X"ti …' / '"X"nti.' / '"X"ti, …' / '"X"ti…pe… tena vuccati …'
    m = re.match(r'^"([^"]+)"(n?)ti…pe… (tena vuccati .+)$', s)
    if m:
        lem = lemma_of(m.group(1) + ("ṃ" if m.group(2) else ""))
        return f"«{cap(lem)}»… {lc(sent12(cap(m.group(3)), ctx))}"
    m = re.match(r'^"([^"]+)"(n?)ti(\.|,)?(?: (.*))?$', s)
    if m:
        lem = lemma_of(m.group(1) + ("ṃ" if m.group(2) else ""))
        rest = m.group(4)
        if m.group(3) == "." or rest is None:
            assert rest is None, s
            return f"«{cap(lem)}»."
        if rest.startswith("…pe… tena vuccati "):
            return f"«{cap(lem)}»… {lc(sent12(cap(rest[len('…pe… '):]), ctx))}"
        return f"«{cap(lem)}»: {lc(sent12(cap(rest), ctx))}"
    m = re.match(r"^(\S+?)(n?)ti\.$", s)   # unquoted lemma: "Saṃvaroti."
    if m and low(m.group(1) + ("ṃ" if m.group(2) else "")) in LEM:
        return f"«{cap(lemma_of(m.group(1) + ('ṃ' if m.group(2) else '')))}»."
    m = re.match(r'^Tena vuccati "([^"]+)"(n?)ti(?: (\[.+\]))?\.$', s)
    if m:
        note = ""
        if m.group(3):
            assert m.group(3) == "[ayaṃ pāṭho mātikāyaṃ natthi, niddese pana sabbapotthakesu dissati]"
            note = " [этого чтения нет в матрице, но в разъяснении оно встречается во всех рукописях]"
        return f"{TENA} «{lemma_of(m.group(1) + ('ṃ' if m.group(2) else ''))}»{note}."
    m = re.match(r"^Tattha katam(?:o|ā|aṃ|e) ([^?…]+)\?$", s)
    if m:
        if m.group(1) == "ariyā":
            return "Кто здесь благородные?"
        return f"{TATTHA} {qterm(m.group(1), ctx)[0]}?"
    m = re.match(r'^Tattha katam(?:o|ā|aṃ|e) ([^?…]+)…pe… (?:ayaṃ|idaṃ) vuccati "(.+)"\.$', s)
    if m:
        return f"{TATTHA} {qterm(m.group(1), ctx)[0]}… {called(qterm(m.group(2), ctx)[1])}."
    m = re.match(r'^(?:Imā|Ime) vuccanti "(.+)"\.$|^(?:Ayaṃ|Idaṃ) vuccati "(.+)"\.$', s)
    if m:
        return cap(called(qterm(m.group(1) or m.group(2), ctx)[1])) + "."
    m = re.match(r'^(.+?),? – (?:ayaṃ|idaṃ) vuccati (\"?)(.+?)\"?(?:ti)?\.$|^(.+?),? – (?:imā|ime) vuccanti (\"?)(.+?)\"?\.$',
                 s)
    if m:
        body = m.group(1) or m.group(4)
        q = m.group(2) if m.group(1) else m.group(5)
        term = m.group(3) or m.group(6)
        ru, comma = BODY12(body)
        return f"{ru}{',' if comma else ''} {DASH} {called(qterm(term, ctx)[1], bool(q))}."
    m = re.match(r"^(.+?) santā (?:hoti|honti) " + SANTA_P + r"\.$", s)
    if m:
        subj, g = SUBJ_SANTA[m.group(1)]
        return f"{subj} {SANTA[g]}."
    m = re.match(r"^Idaṃ cittaṃ (.+?) sodheti visodheti parisodheti moceti vimoceti parimoceti\.$", s)
    if m:
        return f"Этот ум он очищает от {PURIFY_X[m.group(1)]}, " + SODHETI[len("очищает, "):] + "."
    m = re.match(r"^(.+?) upeto hoti( samupeto upāgato samupāgato upapanno sampanno samannāgato|…pe… samannāgato| "
                 r"samupeto…pe… samannāgato)\.$", s)
    if m:
        return f"{UPETO_SUBJ[m.group(1)]} {UPETO_TAIL[m.group(2)]}."
    m = re.match(r"^(Vitakko, vicāro, pīti, sukhaṃ, cittassekaggatā|Sampasādo pītisukhaṃ) – te imasmiṃ "
                 r"(viveke|samādhimhi) jātā honti sañjātā nibbattā abhinibbattā pātubhūtā\.$", s)
    if m:
        subj = ("Направленная мысль, удержание мысли, восторг, счастье, однонаправленность ума" if m.group(1).startswith(
            "Vitakko") else "Ясность, восторг и счастье")
        where = "в этом уединении" if m.group(2) == "viveke" else "в этом сосредоточении"
        return f"{subj} {DASH} они {JATA.split(', ')[0]} {where}, " + JATA[len("родились, "):] + "."
    raise KeyError("ch12 sentence: " + s[:120])


def BODY12(body):
    if body in DEF12:
        return DEF12[body]
    raise KeyError("ch12 body: " + body[:120])


# sense-restraint / food / ācāra / gocara / wakefulness / sampajañña lines: whole Pāli lines
LINES12 = {}
_SENSE_TAIL = ("Sotena saddaṃ sutvā…pe… ghānena gandhaṃ ghāyitvā…pe… jivhāya rasaṃ sāyitvā…pe… kāyena phoṭṭhabbaṃ "
               "phusitvā…pe… manasā dhammaṃ viññāya ")


def build_lines12():
    L = LINES12
    L["Tattha katamā indriyesu aguttadvāratā? Idhekacco cakkhunā rūpaṃ disvā nimittaggāhī hoti anubyañjanaggāhī. "
      "Yatvādhikaraṇamenaṃ cakkhundriyaṃ asaṃvutaṃ viharantaṃ abhijjhādomanassā pāpakā akusalā dhammā anvāssaveyyuṃ, "
      "tassa saṃvarāya na paṭipajjati, na rakkhati cakkhundriyaṃ, cakkhundriye na saṃvaraṃ āpajjati. " + _SENSE_TAIL +
      "nimittaggāhī hoti anubyañjanaggāhī. Yatvādhikaraṇamenaṃ manindriyaṃ asaṃvutaṃ viharantaṃ abhijjhādomanassā "
      "pāpakā akusalā dhammā anvāssaveyyuṃ, tassa saṃvarāya na paṭipajjati, na rakkhati manindriyaṃ, manindriye na "
      "saṃvaraṃ āpajjati. Yā imesaṃ channaṃ indriyānaṃ agutti agopanā anārakkho asaṃvaro – ayaṃ vuccati \"indriyesu "
      "aguttadvāratā\"."] = (f"{TATTHA} {TERM12['indriyesu aguttadvāratā'][0]}? {AGUTTA}, {DASH} "
                             f"{called(TERM12['indriyesu aguttadvāratā'][1])}.")
    L["Tattha katamā indriyesu guttadvāratā? Idhekacco cakkhunā rūpaṃ disvā na nimittaggāhī hoti nānubyañjanaggāhī. "
      "Yatvādhikaraṇamenaṃ cakkhundriyaṃ asaṃvutaṃ viharantaṃ abhijjhādomanassā pāpakā akusalā dhammā anvāssaveyyuṃ, "
      "tassa saṃvarāya paṭipajjati, rakkhati cakkhundriyaṃ, cakkhundriye saṃvaraṃ āpajjati. " + _SENSE_TAIL +
      "na nimittaggāhī hoti nānubyañjanaggāhī. Ñatvādhikaraṇamenaṃ manindriyaṃ asaṃvutaṃ viharantaṃ abhijjhādomanassā "
      "pāpakā akusalā dhammā anvāssaveyyuṃ, tassa saṃvarāya paṭipajjati, rakkhati manindriyaṃ, manindriye saṃvaraṃ "
      "āpajjati. Yā imesaṃ channaṃ indriyānaṃ gutti gopanā ārakkho saṃvaro – ayaṃ vuccati \"indriyesu guttadvāratā\". "
      "Imāya indriyesu guttadvāratāya upeto hoti samupeto…pe… samannāgato. Tena vuccati \"indriyesu guttadvāro\"ti."] = (
        f"{TATTHA} {TERM12['indriyesu guttadvāratā'][0]}? {GUTTA}, {DASH} {called(TERM12['indriyesu guttadvāratā'][1])}. "
        f"{UPETO_SUBJ['Imāya indriyesu guttadvāratāya']} {UPETO_TAIL[' samupeto…pe… samannāgato']}. "
        f"{TENA} «{LEM['indriyesu guttadvāro']}».")
    L["Tattha katamā bhojane amattaññutā? Idhekacco appaṭisaṅkhā ayoniso āhāraṃ āhāreti davāya madāya maṇḍanāya "
      "vibhūsanāya. Yā tattha asantuṭṭhitā amattaññutā appaṭisaṅkhā bhojane – ayaṃ vuccati \"bhojane amattaññutā\"ti."] = (
        f"{TATTHA} {TERM12['bhojane amattaññutā'][0]}? {AMATTA} {DASH} {called(TERM12['bhojane amattaññutā'][1])}.")
    L["Tattha katamā bhojane mattaññutā? Idhekacco paṭisaṅkhā yoniso āhāraṃ āhāreti – \"neva davāya na madāya na "
      "maṇḍanāya na vibhūsanāya, yāvadeva imassa kāyassa ṭhitiyā yāpanāya vihiṃsūparatiyā brahmacariyānuggahāya, iti "
      "purāṇañca vedanaṃ paṭihaṅkhāmi navañca vedanaṃ na uppādessāmi yātrā ca me bhavissati anavajjatā ca phāsu vihāro "
      "cā\"ti. Yā tattha santuṭṭhitā mattaññutā paṭisaṅkhā bhojane – ayaṃ vuccati \"bhojane mattaññutā\". Imāya bhojane "
      "mattaññutāya upeto hoti…pe… samannāgato. Tena vuccati \"bhojane mattaññū\"ti."] = (
        f"{TATTHA} {TERM12['bhojane mattaññutā'][0]}? {MATTA} {DASH} {called(TERM12['bhojane mattaññutā'][1])}. "
        f"{UPETO_SUBJ['Imāya bhojane mattaññutāya']} {Z.UPETO_PE}. {TENA} «{LEM['bhojane mattaññū']}».")
    # ācāra / gocara
    gifts = ["veḷu", "patta", "puppha", "phala", "sināna", "dantakaṭṭha"]
    gifts_r = ["бамбука", "листьев", "цветов", "плодов", "мыльного порошка", "зубочисток"]
    other_p = ["cāṭukamyatāya", "muggasūpyatāya", "pāribhaṭayatāya", "jaṅghapesanikena"]
    other_r = ["лестью", "угодничеством", "нянченьем чужих детей", "выполнением поручений на побегушках"]
    var_mugga = " [вариант написания (Sī.): muggasuppatāya]"
    neg_list = [f"дарением {g}" for g in gifts_r] + other_r
    pos = ", или ".join(f"дарением {g}" for g in gifts_r) + ", или " + ", или ".join(
        (x + var_mugga if i == 1 else x) for i, x in enumerate(other_r))
    L["Tattha katamo anācāro? Kāyiko vītikkamo, vācasiko vītikkamo, kāyikavācasiko vītikkamo – ayaṃ vuccati "
      "\"anācāro\". Sabbampi dussīlyaṃ anācāro. Idhekacco " + " vā ".join(f"{g}dānena" for g in gifts) + " vā "
      + "cāṭukamyatāya vā muggasūpyatāya [muggasuppatāya (sī.)] vā pāribhaṭayatāya vā jaṅghapesanikena vā "
        "aññataraññatarena vā buddhapaṭikuṭṭhena micchāājīvena jīvikaṃ kappeti – ayaṃ vuccati \"anācāro\"."] = (
        f"{TATTHA} {TERM12['anācāro'][0]}? {DEF12['Kāyiko vītikkamo, vācasiko vītikkamo, kāyikavācasiko vītikkamo'][0]} "
        f"{DASH} {called(TERM12['anācāro'][1])}. {SENT12['Sabbampi dussīlyaṃ anācāro.']} Вот человек поддерживает "
        f"жизнь {pos}, или тем или иным неправильным образом жизни, порицаемым Буддой, {DASH} "
        f"{called(TERM12['anācāro'][1])}.")
    L["Tattha katamo ācāro? Kāyiko avītikkamo, vācasiko avītikkamo, kāyikavācasiko avītikkamo – ayaṃ vuccati "
      "\"ācāro\". Sabbopi sīlasaṃvaro ācāro. Idhekacco na " + " na ".join(f"{g}dānena" for g in gifts) + " na "
      + " na ".join(other_p) + " na aññataraññatarena buddhapaṭikuṭṭhena micchāājīvena jīvikaṃ kappeti – ayaṃ "
        "vuccati \"ācāro\"."] = (
        f"{TATTHA} {TERM12['ācāro'][0]}? {DEF12['Kāyiko avītikkamo, vācasiko avītikkamo, kāyikavācasiko avītikkamo'][0]} "
        f"{DASH} {called(TERM12['ācāro'][1])}. {SENT12['Sabbopi sīlasaṃvaro ācāro.']} Вот человек не поддерживает жизнь "
        f"ни {', ни '.join(neg_list)}, ни тем или иным неправильным образом жизни, порицаемым Буддой, {DASH} "
        f"{called(TERM12['ācāro'][1])}.")
    places_p = ["vesiyā", "vidhavā", "thullakumāri", "paṇḍaka", "bhikkhuni", "pānāgāra"]
    places_r = ["блудниц", "вдов", "старых дев", "евнухов", "монахинь", "питейные дома"]
    KINGS = "с царями, царскими сановниками, иноверцами и учениками иноверцев"
    FOUR = "монахам, монахиням, мирянам и мирянкам"
    L["Tattha katamo agocaro? Idhekacco vesiyāgocaro vā hoti vidhavāgocaro vā thullakumārigocaro vā paṇḍakagocaro vā "
      "bhikkhunigocaro vā pānāgāragocaro vā, saṃsaṭṭho viharati rājūhi rājamahāmattehi titthiyehi titthiyasāvakehi "
      "ananulomikena saṃsaggena; yāni vā pana tāni kulāni assaddhāni appasannāni anopānabhūtāni akkosakaparibhāsakāni "
      "anatthakāmāni ahitakāmāni aphāsukakāmāni ayogakkhemakāmāni bhikkhūnaṃ bhikkhunīnaṃ upāsakānaṃ upāsikānaṃ, "
      "tathārūpāni kulāni sevati bhajati payirupāsati – ayaṃ vuccati \"agocaro\"."] = (
        f"{TATTHA} {TERM12['agocaro'][0]}? Вот человек " + ", или ".join(f"посещает {x}" for x in places_r)
        + f", пребывает в неподобающем общении {KINGS}; или же он посещает, водит знакомство и почитает такие семьи, "
          f"которые лишены веры, лишены доверия, не служат источником поддержки, бранят и поносят, желают вреда, желают "
          f"неблага, желают неудобства, желают утраты безопасности {FOUR}, {DASH} {called(TERM12['agocaro'][1])}.")
    L["Tattha katamo gocaro? Idhekacco na vesiyāgocaro hoti na vidhavāgocaro na thullakumārigocaro na paṇḍakagocaro na "
      "bhikkhunigocaro na pānāgāragocaro, asaṃsaṭṭho viharati rājūhi rājamahāmattehi titthiyehi titthiyasāvakehi "
      "ananulomikena saṃsaggena; yāni vā pana tāni kulāni saddhāni pasannāni opānabhūtāni kāsāvapajjotāni "
      "isivātapaṭivātāni atthakāmāni hitakāmāni phāsukakāmāni yogakkhemakāmāni bhikkhūnaṃ bhikkhunīnaṃ upāsakānaṃ "
      "upāsikānaṃ, tathārūpāni kulāni sevati bhajati payirupāsati – ayaṃ vuccati \"gocaro\". Iti iminā ca ācārena "
      "iminā ca gocarena upeto hoti…pe… samannāgato. Tena vuccati \"ācāragocarasampanno\"ti."] = (
        f"{TATTHA} {TERM12['gocaro'][0]}? Вот человек " + ", ".join(f"не посещает {x}" for x in places_r)
        + f", не пребывает в неподобающем общении {KINGS}; или же он посещает, водит знакомство и почитает такие семьи, "
          f"которые имеют веру, имеют доверие, служат источником поддержки, озарены сиянием жёлтых одежд, овеяны "
          f"дыханием мудрецов, желают пользы, желают блага, желают удобства, желают безопасности {FOUR}, {DASH} "
          f"{called(TERM12['gocaro'][1])}. {UPETO_SUBJ['Iti iminā ca ācārena iminā ca gocarena']} {Z.UPETO_PE}. "
          f"{TENA} «{LEM['ācāragocarasampanno']}».")
    L["Kathañca bhikkhu pubbarattāpararattaṃ jāgariyānuyogamanuyutto hoti? Idha bhikkhu divasaṃ caṅkamena nisajjāya "
      "āvaraṇīyehi dhammehi cittaṃ parisodheti, rattiyā paṭhamayāmaṃ caṅkamena nisajjāya āvaraṇīyehi dhammehi cittaṃ "
      "parisodheti, rattiyā majjhimayāmaṃ dakkhiṇena passena sīhaseyyaṃ kappeti pāde pādaṃ [pādena pādaṃ (syā.)] "
      "accādhāya sato sampajāno uṭṭhānasaññaṃ manasikaritvā, rattiyā pacchimayāmaṃ paccuṭṭhāya caṅkamena nisajjāya "
      "āvaraṇīyehi dhammehi cittaṃ parisodheti. Evaṃ bhikkhu pubbarattāpararattaṃ jāgariyānuyogamanuyutto."] = (
        "Как монах в начале и в конце ночи предан бодрствованию? Вот монах днём, во время хождения и сидения, очищает "
        "ум от явлений, создающих препятствия; в первую стражу ночи, во время хождения и сидения, очищает ум от "
        "явлений, создающих препятствия; в среднюю стражу ночи ложится на правый бок в позе льва, положив ступню на "
        "ступню [вариант чтения (Syā.): pādena pādaṃ], осознанный и ясно понимающий, уделив внимание мысли о вставании; "
        "в последнюю стражу ночи, встав, во время хождения и сидения очищает ум от явлений, создающих препятствия. Так "
        "монах в начале и в конце ночи предан бодрствованию.")
    # sampajañña (^2-523, ^2-525)
    keys = list(SAMPAJ)
    q_p = ", ".join(f"{k} sampajānakārī hoti" for k in keys[:-1]) + f"; {keys[-1]} sampajānakārī hoti"
    # Russian: «;» between the clauses (the Pāli commas), so that each circumstance stays with its verb
    q_r = "; ".join(f"{SAMPAJ[k]}, {SK}" for k in keys)
    acts_p = ("sato sampajāno abhikkamati, sato sampajāno paṭikkamati, sato sampajāno āloketi, sato sampajāno viloketi, "
              "sato sampajāno samiñjeti, sato sampajāno pasāreti, sato sampajānakārī hoti, ")
    OS = "осознанно и с ясным пониманием"
    acts_r = (f"{OS} идёт вперёд, {OS} идёт назад, {OS} смотрит прямо, {OS} смотрит по сторонам, {OS} сгибает руки и "
              f"ноги, {OS} распрямляет их; осознанно {SK}; ")
    rest_p = ", ".join(f"{k} sato sampajānakārī hoti" for k in keys[3:])
    rest_r = "; ".join(f"{SAMPAJ[k]}, осознанно {SK}" for k in keys[3:])
    rest_p2 = ", ".join(f"{k} sato sampajānakārī hoti" for k in keys[3:-1]) + f", {keys[-1]} sampajānakārī hoti"
    rest_r2 = "; ".join(f"{SAMPAJ[k]}, осознанно {SK}" for k in keys[3:-1]) + f"; {SAMPAJ[keys[-1]]}, {SK}"
    L["Kathañca bhikkhu " + q_p + "? Idha bhikkhu " + acts_p + rest_p[:-len("hoti")] + "hotīti."] = (
        f"Как монах, {q_r}? Вот монах {acts_r}{rest_r}.")
    L_525 = ("\"Sampajāno\"ti tattha katamaṃ sampajaññaṃ? " + [k for k in DEF12 if k.startswith("Yā paññā pajānanā vicayo")][0]
             + " – idaṃ vuccati \"sampajaññaṃ\". Iti imāya ca satiyā iminā ca sampajaññena upeto hoti…pe… samannāgato. "
               "Evaṃ bhikkhu " + acts_p + rest_p2 + ".")
    L[L_525] = (f"«{cap(LEM['sampajāno'])}»: {lc(TATTHA)} {TERM12['sampajaññaṃ'][0]}? {PANNA_FULL}, {DASH} "
                f"{called(TERM12['sampajaññaṃ'][1])}. {UPETO_SUBJ['Iti imāya ca satiyā iminā ca sampajaññena']} "
                f"{Z.UPETO_PE}. Так монах {acts_r}{rest_r2}.")


build_lines12()

# ================================================================ 8. chapter 12 Abhidhamma
HEAD12 = {"Rūpāvacarakusalaṃ": "Благой ум, относящийся к миру форм",                       # pi-1 headings
          "Arūpāvacarakusalaṃ": "Благой ум, относящийся к миру без форм",
          "Lokuttarakusalaṃ": "Надмирский благой ум",
          "Rūpāvacaravipākā": "Результаты действий, относящиеся к миру форм",
          "Arūpāvacaravipākā": "Результаты действий, относящиеся к миру без форм",
          "Lokuttaravipākā": "Надмирские результаты действий",
          "Rūpārūpāvacarakiriyā": "Функциональный ум, относящийся к миру форм и к миру без форм",
          "Mātikā": "Матрица", "Tikaṃ": B.LABELS["##### Tikaṃ"][6:], "Dukaṃ": B.LABELS["##### Dukaṃ"][6:]}
in_pi1("##### " + HEAD12["Rūpāvacarakusalaṃ"], "#### " + HEAD12["Lokuttarakusalaṃ"],
       "##### " + HEAD12["Rūpāvacaravipākā"], "##### Функциональный ум, относящийся к миру форм",
       "##### Функциональный ум, относящийся к миру без форм", "Четверичный метод.", "Пятеричный метод.")
ASENT.update({
    "Cattāri jhānāni – paṭhamaṃ jhānaṃ, dutiyaṃ jhānaṃ, tatiyaṃ jhānaṃ, catutthaṃ jhānaṃ.":
        f"{FOUR_JH} {DASH} " + T.enum([f"{ORD[k][0]} {JHANA_N}" for k in ("paṭhamaṃ", "dutiyaṃ", "tatiyaṃ",
                                                                        "catutthaṃ")]) + ".",
    "Catukkaṃ.": "Четверичный метод.", "Pañcakaṃ.": "Пятеричный метод.",       # pi-1 Catukkanayo / Pañcakanayo
})

# ================================================================ 9. Pañhāpucchaka (all three chapters)
NEW_SUBJ = {
    "Pītisambojjhaṅgo": (cap(BOJ_R["pīti"]), cap(BOJ_R["pīti"]), "sg", "m"),
    "Dhammavicayasambojjhaṅgo": (cap(BOJ_R["dhammavicaya"]), cap(BOJ_R["dhammavicaya"]), "sg", "m"),
    "dhammavicayasambojjhaṅgo": (BOJ_R["dhammavicaya"], BOJ_R["dhammavicaya"], "sg", "m"),
    "cha bojjhaṅgā": ("шесть факторов пробуждения", "шесть факторов пробуждения", "pl", None),
    "Cha bojjhaṅgā": ("Шесть факторов пробуждения", "Шесть факторов пробуждения", "pl", None),
    "Sammāsaṅkappo": ("Правильный помысел", "Правильный помысел", "sg", "m"),
    "Sammādiṭṭhi": ("Правильное воззрение", "Правильное воззрение", "sg", "n"),
    "sammādiṭṭhi": ("правильное воззрение", "правильное воззрение", "sg", "n"),
    "satta maggaṅgā": ("семь факторов пути", "семь факторов пути", "pl", None),
    "Satta maggaṅgā": ("Семь факторов пути", "Семь факторов пути", "pl", None),
    "Tīṇi jhānāni": ("Три медитативных погружения", "Три медитативных погружения", "pl", None),
    "tīṇi jhānāni": ("три медитативных погружения", "три медитативных погружения", "pl", None),
    "Dve jhānāni": ("Два медитативных погружения", "Два медитативных погружения", "pl", None),
    "dve jhānāni": ("два медитативных погружения", "два медитативных погружения", "pl", None),
    "Catutthaṃ jhānaṃ": ("Четвёртое медитативное погружение", "Четвёртое медитативное погружение", "sg", "nn"),
    "catutthaṃ jhānaṃ": ("четвёртое медитативное погружение", "четвёртое медитативное погружение", "sg", "nn"),
    "Paṭhamaṃ jhānaṃ": ("Первое медитативное погружение", "Первое медитативное погружение", "sg", "nn"),
}
# "nn": neuter with a neuter Pāli subject (jhānaṃ): a plural Pāli predicate switches back to the plural
for _k, _v in NEW_SUBJ.items():
    assert _k not in T.SUBJ2 or T.SUBJ2[_k] == _v, _k
    T.SUBJ2[_k] = _v
T.SUBJ_RE2 = re.compile(r"^(" + "|".join(map(re.escape, sorted(T.SUBJ2, key=len, reverse=True))) + r") (.+)$")
T.PRON[("sg", "n")] = "его"
T.PRON[("sg", "nn")] = "его"
SHORT_N = {"связан": "связано", "охвачен": "охвачено", "подвержен": "подвержено", "свободен": "свободно",
           "затронут": "затронуто", "омрачён": "омрачено", "соединён": "соединено", "порождён": "порождено",
           "сопряжён": "сопряжено", "способен": "способно"}
assert set(SHORT_N) == set(T.SHORT_M.values())


def neut(s):
    r = T.masc(s)
    return re.sub(r"[А-Яа-яЁё]+", lambda m: SHORT_N.get(m.group(0), m.group(0)), r)


ETTHA = {   # etthuppannaṃ X ṭhapetvā -> Russian genitive phrase with the participle «возникш…»
    "sukhaṃ vedanaṃ": "возникшего в {w} приятного чувства",
    "adukkhamasukhaṃ vedanaṃ": "возникшего в {w} чувства, которое ни болезненно, ни приятно",
    "vitakkavicāre": "возникших в {w} направленной мысли и удержания мысли",
    "pītiṃ": "возникшего в {w} восторга", "sukhaṃ": "возникшего в {w} счастья",
    "upekkhaṃ": "возникшей в {w} невозмутимости", "vitakkaṃ": "возникшей в {w} направленной мысли",
    "vicāraṃ": "возникшего в {w} удержания мысли",
}
in_pi1("кроме возникшего в них приятного чувства", "кроме возникших в них направленной мысли и удержания мысли",
       "кроме возникшего в них восторга", "кроме возникшего в них счастья", "кроме возникшей в них невозмутимости",
       "кроме возникшего в них удержания мысли")
PL_END = re.compile(r"(ā|ino)$")
for _k in ("hetu_sahetuka", "hetu_hetusampayutta"):
    pass
T.alias("hetu_sahetuka", "hetu ceva sahetukā ca")
T.alias("hetu_hetusampayutta", "hetu ceva hetusampayuttā ca")
T.alias("savitakkasavicara", "savitakkaṃ savicāraṃ")
T.alias("asava_vipp_niya", "āsavavippayuttā sāsavā")      # ^2-641 written as two words
T.alias("asava_vipp_aniya", "āsavavippayuttā anāsavā")


def pred(surface, st):
    key = T.key_of(surface)
    if st["num"] == "sg":
        r = T.ITEMS2[key]["s"]
        if r is not None and st["g"] == "m":
            r = T.masc(r)
        elif r is not None and st["g"] in ("n", "nn"):
            r = neut(r)
    else:
        r = T.ITEMS2[key]["p"]
    if r is None:
        raise KeyError(f"no {st['num']} predicate: {surface}")
    return r


def quote(text, ti, st):
    st2 = {"num": st["num"], "g": "m" if st["g"] in ("n", "nn") else st["g"]}
    return Z.quote(text, ti, st2)


def pq_chunk(c, st):
    subj = None
    m = re.match(r"^(.+?) – etthuppann(?:aṃ|e) (.+?) ṭhapetvā (.+)$", c)
    if m:
        subj = T.SUBJ2[m.group(1)]
        st["num"], st["g"] = subj[2], subj[3]
        w = "них" if st["num"] == "pl" else "нём"
        return f"{subj[0]} {DASH} кроме {ETTHA[m.group(2)].format(w=w)}, {pq_pred(m.group(3), st)}"
    m = T.SUBJ_RE2.match(c)
    rest = c
    if m:
        subj = T.SUBJ2[m.group(1)]
        st["num"], st["g"] = subj[2], subj[3]
        rest = m.group(2)
    elif (st["g"] == "nn" and not st.get("nv") and PL_END.search(re.sub(r"(n?ti(?:pi)?)$", "", c))
          and not c.startswith('"')):
        st["num"], st["g"] = "pl", None          # back to all four jhānas (plural Pāli predicate)
    pron = T.PRON[(st["num"], st["g"])] if st["num"] else "их"
    # quoted "na vattabb…" without a dash (ch. 12): (siyā) na vattabbā "X"ti(pi)
    m = re.match(r'^(siyā )?na vattabb(?:o|ā|aṃ) "(.+?)"(n?)ti(pi)?$', low(rest))
    if m:
        st["nv"] = True
        qt = quote(m.group(2), m.group(3) + "ti" + (m.group(4) or ""), st)
        if m.group(1):
            return f"иногда {pron} {Z.NV} {qt}"
        return f"{subj[1] if subj else pron} {Z.NV} {qt}"
    m = Z.UNQ_NV.match(low(rest))
    if m:
        st["nv"] = True
        qt = quote(m.group(2), m.group(3), st)
        if m.group(1):
            return f"иногда {pron} {Z.NV} {qt}"
        return f"{subj[1] if subj else pron} {Z.NV} {qt}"
    if st.get("nv") and not subj:
        m = re.match(r'^"(.+?)"(n?ti(?:pi)?)$', rest)
        if m:
            return quote(m.group(1), m.group(2), st)
        m = Z.UNQ_TI.match(rest)
        if m and m.group(2).endswith("pi"):
            return quote(m.group(1), m.group(2), st)
    m = Z.UNQ_TI.match(low(rest))
    if m and m.group(2).endswith("tipi") and not subj:   # ^2-485 "Āsavā ceva … cātipi, …" without "na vattabbā"
        st["nv"] = True
        return quote(m.group(1), m.group(2), st)
    st["nv"] = False
    r = pq_pred(rest, st)
    return f"{subj[0]} {r}" if subj else r


def pq_pred(rest, st):
    sur = rest
    if sur[:1].isupper():
        sur = low(sur)
    if sur.startswith("siyā "):
        return "иногда " + pred(sur[5:], st)
    return pred(sur, st)


PFIX = [   # punctuation / spelling slips in the Pāli (reported); the words are translated as written
    ("maggahetukantipi maggādhipatītipi", "maggahetukantipi, maggādhipatītipi"),   # ^2-640 comma
    ("paccuppannāramaṇantipi", "paccuppannārammaṇantipi"),                       # ^2-640 spelling
    ('"āsavā ceva āsavasampayuttā cāti"pi', '"āsavā ceva āsavasampayuttā cā"tipi'),   # ^2-641 quote
    ("Araṇāti.", "Araṇā."), ("araṇāti.", "araṇā."),                              # closing "ti" of the question list
    ("Anāsavā āsavavippayuttā.", "Anāsavā, āsavavippayuttā."),                   # ^2-485 comma
    (" …pe…", "…pe…"),
]


def pq_line(t, labels):
    if t in labels:
        return labels[t]
    for a, b in PFIX:
        t = t.replace(a, b)
    out = []
    for sent in re.split(r"(?<=\.) (?=[A-ZĀ])", t):
        assert sent.endswith("."), sent[-40:]
        body = sent[:-1].replace("…pe…", PE)
        parts = re.split(r"(, |; |\x01 ?)", body)
        # "Tīṇi jhānāni – etthuppannaṃ …": the dash belongs to the chunk
        st = {"num": "pl", "g": None}
        ru = []
        for i, x in enumerate(parts):
            if i % 2:
                ru.append(x.replace(PE, "…"))
            else:
                ru.append(pq_chunk(x, st))
        out.append(cap("".join(ru)) + ".")
    return " ".join(out)


LABELS = {
    "##### Tikaṃ": B.LABELS["##### Tikaṃ"], "##### Dukaṃ": B.LABELS["##### Dukaṃ"],
    "Pañhāpucchakaṃ.": SEC["Pañhāpucchakaṃ"] + ".",
    "Sattannaṃ bojjhaṅgānaṃ kati kusalā, kati akusalā, kati abyākatā…pe… kati saraṇā, kati araṇā?":
        T.how_many_q("семи факторов пробуждения"),
    "Aṭṭhannaṃ maggaṅgānaṃ kati kusalā, kati akusalā, kati abyākatā…pe… kati saraṇā, kati araṇā?":
        T.how_many_q("восьми факторов пути"),
    "Catunnaṃ jhānānaṃ kati kusalā, kati akusalā, kati abyākatā…pe… kati saraṇā, kati araṇā?":
        T.how_many_q("четырёх медитативных погружений"),
    "Bojjhaṅgavibhaṅgo niṭṭhito.": S.CHAPTER_CLOSING.format(title=S.CHAPTER_TITLES[10]),
    "Maggaṅgavibhaṅgo niṭṭhito.": S.CHAPTER_CLOSING.format(title=S.CHAPTER_TITLES[11]),
    "Jhānavibhaṅgo niṭṭhito.": S.CHAPTER_CLOSING.format(title=S.CHAPTER_TITLES[12]),
    SEVEN_P: SEVEN_LINE, ARIYO8_P: ARIYO8_R,
    "Cattāri jhānāni – idha bhikkhu " + JHANA4_P.format(d=" – ").replace(" upasampajja viharati; ",
                                                                         " upasampajja viharati…pe… ") + ".":
        f"{FOUR_JH} {DASH} вот монах, " + "… ".join([JH1, JH2, JH3, JH4]) + ".",
}

# ================================================================ 10. chapters
TITLE = {"Bojjhaṅgavibhaṅgo": 10, "Maggaṅgavibhaṅgo": 11, "Jhānavibhaṅgo": 12}
FIXES = [   # (Pāli as written, as meant): punctuation / spelling slips only, all reported
    ("kāmehi …pe…", "kāmehi…pe…"),                         # ^2-478
    ("sampayuttā …pe…", "sampayuttā…pe…"),                 # ^2-481
    ("jhānaṃ …pe…", "jhānaṃ…pe…"),                         # ^2-634
    ("pahānā …pe…", "pahānā…pe…"),                         # ^2-628
    ("anussati …pe…", "anussati…pe…"),                     # ^2-550
    ('"Viharatī"ti …pe…', '"Viharatī"ti…pe…'),            # ^2-554 …
]


def text_line(t, ch, section):
    for a, b in FIXES:
        t = t.replace(a, b)
    if section == "Pañhāpucchakaṃ":
        return pq_line(t, LABELS)
    if ch == 10:
        if t == SEVEN_P:
            return SEVEN_LINE
        if t == SEVEN_PE_P:
            return SEVEN_PE
        if t in SUTTA10:
            return SUTTA10[t]
        return abhi_line(t)
    if ch == 11:
        if t in LINES11:
            return LINES11[t]
        if t in SUTTA11:
            return SUTTA11[t]
        if section == "Suttantabhājanīyaṃ":
            return F.sutta4(t)
        return abhi_line(t)
    # ch. 12
    if section == "Abhidhammabhājanīyaṃ":
        if t in ASENT:
            return ASENT[t]
        return abhi_line(t)
    if t in LINES12:
        return LINES12[t]
    ctx = 594 if t.startswith(("Tattha katamaṃ sukhaṃ? Yaṃ kāyikaṃ", "Tattha katamaṃ dukkhaṃ? Yaṃ kāyikaṃ")) else None
    return " ".join(sent12(s, ctx) for s in SPLIT.split(t))


ROOT_508_P = None


def build_chapter(pali, ch):
    out = []
    section = None
    for t in pali:
        if t.startswith("### "):
            out.append("### " + S.CHAPTER_TITLES[TITLE[t[4:]]])
        elif t.startswith("#### "):
            section = t[5:]
            out.append("#### " + SEC[section])
        elif t.startswith("##### "):
            out.append("##### " + HEAD12[t[6:]])
        elif t.endswith(".") and t[:-1] in SEC:
            out.append(SEC[t[:-1]] + ".")
        elif t.endswith(" niṭṭhito."):
            out.append(LABELS[t])
        elif ch == 12 and t.startswith("Idha bhikkhu pātimokkhasaṃvarasaṃvuto"):
            out.append(ROOT_508)
        else:
            out.append(text_line(t, ch, section))
    return out


def check_root_508(t):
    """the Pāli of ^2-508 must be exactly the parts the Russian covers."""
    exp = ("Idha bhikkhu pātimokkhasaṃvarasaṃvuto viharati, ācāragocarasampanno, aṇumattesu vajjesu bhayadassāvī, "
           "samādāya sikkhati sikkhāpadesu indriyesu guttadvāro bhojane mattaññū pubbarattāpararattaṃ "
           "jāgariyānuyogamanuyutto sātaccaṃ nepakkaṃ bodhipakkhikānaṃ dhammānaṃ bhāvanānuyogamanuyutto. So abhikkante "
           "paṭikkante sampajānakārī hoti, ālokite vilokite sampajānakārī hoti, samiñjite [sammiñjite (sī. syā.)] "
           "pasārite sampajānakārī hoti, saṅghāṭipattacīvaradhāraṇe sampajānakārī hoti, asite pīte khāyite sāyite "
           "sampajānakārī hoti, uccārapassāvakamme sampajānakārī hoti, gate ṭhite nisinne sutte jāgarite bhāsite "
           "tuṇhībhāve sampajānakārī hoti. So vivittaṃ senāsanaṃ bhajati araññaṃ rukkhamūlaṃ pabbataṃ kandaraṃ "
           "giriguhaṃ susānaṃ vanapatthaṃ abbhokāsaṃ palālapuñjaṃ appasaddaṃ appanigghosaṃ vijanavātaṃ "
           "manussarāhasseyyakaṃ [manussarāhaseyyakaṃ (sī. syā.)] paṭisallānasāruppaṃ. So araññagato vā "
           "rukkhamūlagato vā suññāgāragato vā nisīdati pallaṅkaṃ ābhujitvā ujuṃ kāyaṃ paṇidhāya parimukhaṃ satiṃ "
           "upaṭṭhapetvā. So abhijjhaṃ loke pahāya vigatābhijjhena cetasā viharati, abhijjhāya cittaṃ parisodheti. "
           "Byāpādapadosaṃ pahāya abyāpannacitto viharati sabbapāṇabhūtahitānukampī, byāpādapadosā cittaṃ "
           "parisodheti. Thinamiddhaṃ pahāya vigatathinamiddho viharati ālokasaññī sato sampajāno, thinamiddhā cittaṃ "
           "parisodheti. Uddhaccakukkuccaṃ pahāya anuddhato viharati ajjhattaṃ vūpasantacitto, uddhaccakukkuccā "
           "cittaṃ parisodheti. Vicikicchaṃ pahāya tiṇṇavicikiccho viharati akathaṃkathī kusalesu dhammesu, "
           "vicikicchāya cittaṃ parisodheti. So ime pañca nīvaraṇe pahāya cetaso upakkilese paññāya dubbalīkaraṇe "
           + JHANA4_P.format(d=" – ") + "; sabbaso rūpasaññānaṃ samatikkamā paṭighasaññānaṃ atthaṅgamā "
           "nānattasaññānaṃ amanasikārā \"ananto ākāso\"ti ākāsānañcāyatanaṃ upasampajja viharati; sabbaso "
           "ākāsānañcāyatanaṃ samatikkamma \"anantaṃ viññāṇa\"nti viññāṇañcāyatanaṃ upasampajja viharati; sabbaso "
           "viññāṇañcāyatanaṃ samatikkamma \"natthi kiñcī\"ti ākiñcāyatanaṃ upasampajja viharati; sabbaso "
           "ākiñcaññāyatanaṃ samatikkamma nevasaññānāsaññāyatanaṃ upasampajja viharati.")
    assert t == exp, [i for i, (a, b) in enumerate(zip(t, exp)) if a != b][:1]


def build(fn, ch):
    pali = open(os.path.join(S.PALI_DIR, fn), encoding="utf-8").read().rstrip("\n").split("\n")
    nonempty = [S.ID.sub("", l).rstrip() for l in pali if l.strip()]
    if ch == 12:
        check_root_508(nonempty[2])
    ru = build_chapter(nonempty, ch)
    assert len(ru) == len(nonempty), (fn, len(ru), len(nonempty))
    for p, r in zip(nonempty, ru):
        assert p.count(DASH) + p.count("—") == r.count(DASH), ("dash count", p[:70], r[:70])
        assert "—" not in r and "\x01" not in r and "\x02" not in r and "  " not in r, r[:80]
        assert p.startswith("#") == r.startswith("#") and p.split(" ")[0].count("#") == r.split(" ")[0].count("#"), (p[:40], r[:40])
        assert not re.search(r"[A-Za-zĀāĪīŪūṬṭḌḍÑñṆṇṄṅṂṃḶḷ]", re.sub(r"\[[^\]]*\]", "", r)), ("latin", r[:120])
    lines = S.attach_ids(pali, ru)
    S.write(os.path.join(S.RU_DIR, fn), lines)
    print("OK:", fn, "|", len(ru), "non-empty lines")


def main():
    build("10-bojjhangavibhango.md", 10)
    build("11-maggangavibhango.md", 11)
    build("12-jhanavibhango.md", 12)


if __name__ == "__main__":
    main()
