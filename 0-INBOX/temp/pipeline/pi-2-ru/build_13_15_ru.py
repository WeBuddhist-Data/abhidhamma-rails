# -*- coding: utf-8 -*-
"""pi-2 Vibhaṅga, Russian plain zero-shot: chapters 13 (Appamaññā), 14 (Sikkhāpada), 15 (Paṭisambhidā).

usage: python -I -X utf8 build_13_15_ru.py
Writes AI_translation\\russian\\pi-2-russian-plain-zeroshot_split_chapters\\13-…, 14-…, 15-….md.
Imports build_10_12_ru (X) and through it S, B, T, F, G, Z; extends their tables in memory only
(X.ATERM / X.ADEF / X.QUAL / X.JH_HEAD / X.ASENT / X.PFIX, T.SUBJ2 / T.SURF2, G.TOKENS, X.pq_chunk wrapper).
Reused strings: mettā / karuṇā bodies (ch3 T.METTA / T.KARUNA), the appamaññā jhānas (pi-1 ^1-251 …, ch12 openings),
citta definition (pi-1 ^1-6), the abstention list (pi-1 ^1-299 … ^1-301, ch4), cetanā (pi-1 ^1-5), the kāma-sphere,
vipāka and kiriya mind-type openings (pi-1, ch6 G.desc), the Pañhāpucchaka lexicon (B/T, ch12 X.pq_line).
Every line is translated sentence by sentence from fixed strings; unknown Pāli raises KeyError.
Importing this module writes nothing.
"""
import os, re, sys

HERE = r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-ru"
sys.path.insert(0, HERE)
import build_10_12_ru as X  # noqa: E402

S, B, T, F, G, Z = X.S, X.B, X.T, X.F, X.G, X.Z
DASH = S.DASH
cap, low, lc = S.cap, S.low, X.lc
edit, in_pi1 = F.edit, F.in_pi1
PI1 = T.PI1
SEC = S.SECTION_TITLES
TATTHA = S.TATTHA                 # Что такое здесь
TENA = X.TENA                     # Поэтому и говорится:
SPLIT = X.SPLIT
called = X.called

# ================================================================ 1. the four immeasurables (chapter 13)
K4 = ["mettā", "karuṇā", "muditā", "upekkhā"]
AP = {   # Pāli -> (nom, ins, gender of the Russian noun)
    "mettā": ("доброжелательность", "доброжелательностью", "f"),       # pi-1 / ch3
    "karuṇā": ("сострадание", "состраданием", "n"),                    # pi-1 termbase / ch3
    "muditā": ("сорадование", "сорадованием", "n"),                    # pi-1 termbase
    "upekkhā": ("невозмутимость", "невозмутимостью", "f"),             # core
}
in_pi1("сопровождаемое доброжелательностью", "сопровождаемое состраданием", "сопровождаемое сорадованием",
       "сопровождаемое невозмутимостью")
FOUR_AP = "Четыре безмерных состояния"                                # catasso appamaññāyo [pi-3 «безмерное состояние»]
FOUR_AP_LINE = f"{FOUR_AP} {DASH} " + T.enum([AP[k][0] for k in K4]) + "."
SYN = {k: f"{k if k != 'mettā' else 'metti'} {k}yanā {k}yitattaṃ {k}cetovimutti" for k in K4}
SYN["mettā"] = "metti mettāyanā mettāyitattaṃ mettācetovimutti"
BODY_S = {   # "Yā sattesu …" (Suttanta)
    "mettā": T.METTA,                                                   # ch3 ^2-182
    "karuṇā": T.KARUNA,                                                 # ch3 ^2-182
    "muditā": "То, что есть сорадование существам, проявление сорадования, состояние сорадования, освобождение ума "
              "сорадованием",
    "upekkhā": "То, что есть невозмутимость по отношению к существам, проявление невозмутимости, состояние "
               "невозмутимости, освобождение ума невозмутимостью",
}
assert T.METTA == ("То, что есть доброжелательность к существам, проявление доброжелательности, состояние "
                   "доброжелательности, освобождение ума доброжелательностью")
BODY_A = {   # "Yā tasmiṃ samaye …" (Abhidhamma): the same without «… существам»
    "mettā": edit(T.METTA, " к существам", ""),
    "karuṇā": edit(T.KARUNA, " к существам", ""),
    "muditā": edit(BODY_S["muditā"], " существам", ""),
    "upekkhā": edit(BODY_S["upekkhā"], " по отношению к существам", ""),
}
SAHA = {k: f"умом, сопровождаемым {AP[k][1]}" for k in K4}           # "<k>sahagatena cetasā"
PRON_INS = {"f": "ней", "n": "ним"}
THIS_INS = {"f": "этой", "n": "этим"}
CITTA_FULL = G.BODY["Yaṃ cittaṃ mano mānasaṃ hadayaṃ paṇḍaraṃ mano manāyatanaṃ manindriyaṃ viññāṇaṃ viññāṇakkhandho "
                    "tajjāmanoviññāṇadhātu"][0]                        # pi-1 ^1-6
CITTA_PE = X.CITTA_PE
ONE_DIR = "одну сторону света"
MIND_TAIL = "обширным, возвышенным, безмерным, свободным от вражды, свободным от неприязни"   # vipula … abyāpajja [new]
ALL_WORLD = "так вверх, вниз, в стороны, повсюду, ко всем как к себе, он пребывает, наполнив весь мир"
VAR_CATUTTHI = " [вариант написания (Sī.): catutthiṃ]"
VAR_ABYAPAJJHENA = " [вариант написания (Sī., Syā.): abyāpajjhena]"
VAR_ABYAPAJJHO = " [вариант написания (Sī., Syā.): abyāpajjho]"


def root_parts(k, first, pana_sep):
    """the brahmavihāra formula for one immeasurable: (Pāli, Russian) for ^2-642 (pana_sep False) / ^2-699 (True)."""
    v1 = VAR_CATUTTHI if (first and not pana_sep) else ""
    v2 = VAR_ABYAPAJJHENA if (first and not pana_sep) else ""
    pv1 = " [catutthiṃ (sī.)]" if v1 else ""
    pv2 = " [abyāpajjhena (sī. syā.)]" if v2 else ""
    if pana_sep:
        p1 = (f"{k}sahagatena cetasā ekaṃ disaṃ pharitvā viharati tathā dutiyaṃ tathā tatiyaṃ tathā catutthaṃ, iti "
              f"uddhamadho tiriyaṃ sabbadhi sabbattatāya sabbāvantaṃ lokaṃ {k}sahagatena cetasā vipulena mahaggatena "
              f"appamāṇena averena abyāpajjena pharitvā viharati")
    else:
        p1 = (f"{k}sahagatena cetasā ekaṃ disaṃ pharitvā viharati, tathā dutiyaṃ, tathā tatiyaṃ, tathā catutthaṃ{pv1}. "
              f"Iti uddhamadho tiriyaṃ sabbadhi sabbattatāya sabbāvantaṃ lokaṃ {k}sahagatena cetasā vipulena "
              f"mahaggatena appamāṇena averena abyāpajjena{pv2} pharitvā viharati.")
    if not first:
        p1 = cap(p1) if not pana_sep else p1
    r_a = (f"пребывает, наполнив {ONE_DIR} {SAHA[k]}, так же вторую, так же третью, так же четвёртую")
    r_b = f"{ALL_WORLD} {SAHA[k]}, {MIND_TAIL}"
    if pana_sep:
        r = f"{r_a}, {r_b}"
    else:
        r = f"{r_a}{v1}. {cap(r_b)}{v2}."
    r = ("вот монах " if first else ("он " if pana_sep else "Он ")) + r
    return p1, r


def root_line(pana_sep):
    ps, rs = [], []
    for i, k in enumerate(K4):
        p, r = root_parts(k, i == 0, pana_sep)
        ps.append(p)
        rs.append(r)
    sep = "; " if pana_sep else " "
    return ("Catasso appamaññāyo – idha bhikkhu " + sep.join(ps) + ("." if pana_sep else ""),
            f"{FOUR_AP} {DASH} " + sep.join(rs) + ("." if pana_sep else ""))


ROOT642_P, ROOT642_R = root_line(False)
ROOT699_P, ROOT699_R = root_line(True)

SENT13 = {
    "Tattha katamaṃ cittaṃ?": f"{TATTHA} ум?",
    "Yaṃ cittaṃ mano mānasaṃ hadayaṃ paṇḍaraṃ mano manāyatanaṃ manindriyaṃ viññāṇaṃ viññāṇakkhandho "
    "tajjāmanoviññāṇadhātu – idaṃ vuccati \"cittaṃ\".": f"{CITTA_FULL}, {DASH} {called('умом')}.",
    "Yaṃ cittaṃ mano mānasaṃ…pe… tajjāmanoviññāṇadhātu – idaṃ vuccati \"cittaṃ\".": f"{CITTA_PE}, {DASH} {called('умом')}.",
    '"Ekaṃ disa"nti puratthimaṃ vā disaṃ pacchimaṃ vā disaṃ uttaraṃ vā disaṃ dakkhiṇaṃ vā disaṃ uddhaṃ vā adho vā '
    'tiriyaṃ vā vidisaṃ vā.':
        f"«{cap(ONE_DIR)}»: или восточную сторону света, или западную сторону света, или северную сторону света, или "
        f"южную сторону света, или вверх, или вниз, или в стороны, или промежуточную сторону света.",
    '"Pharitvā"ti pharitvā adhimuccitvā.': "«Наполнив»: наполнив, утвердившись в решимости.",
    '"Tathā dutiya"nti yatheva ekaṃ disaṃ tathā dutiyaṃ disaṃ tathā tatiyaṃ disaṃ tathā catutthaṃ disaṃ tathā uddhaṃ '
    'tathā adho tathā tiriyaṃ tathā vidisaṃ.':
        f"«Так же вторую»: как {ONE_DIR}, так же вторую сторону света, так же третью сторону света, так же четвёртую "
        f"сторону света, так же вверх, так же вниз, так же в стороны, так же промежуточную сторону света.",
    '"Sabbadhi sabbattatāya sabbāvantaṃ loka"nti sabbena sabbaṃ sabbathā sabbaṃ asesaṃ nissesaṃ.':
        "«Повсюду, ко всем как к себе, весь мир»: всецело, во всех отношениях, без остатка, полностью.",
    'Pariyādāyavacanametaṃ – "sabbadhi sabbattatāya sabbāvantaṃ loka"nti.':
        f"Это выражение, охватывающее всё, {DASH} «повсюду, ко всем как к себе, весь мир».",
}
_VIPULA = ("«Обширным»: то, что обширно, то и возвышенно; то, что возвышенно, то и безмерно; то, что безмерно, то и "
           "свободно от вражды; то, что свободно от вражды, то и свободно от неприязни")
SENT13['"Vipulenā"ti yaṃ vipulaṃ taṃ mahaggataṃ, yaṃ mahaggataṃ taṃ appamāṇaṃ, yaṃ appamāṇaṃ so avero, yo avero so '
       'abyāpajjo [abyāpajjho (sī. syā.)].'] = _VIPULA + VAR_ABYAPAJJHO + "."
SENT13['"Vipulenā"ti yaṃ vipulaṃ taṃ mahaggataṃ, yaṃ mahaggataṃ taṃ appamāṇaṃ, yaṃ appamāṇaṃ so avero, yo avero so '
       'abyāpajjo.'] = _VIPULA + "."
assert X.SENT12["Iti imāsu sikkhāsu sabbena sabbaṃ sabbathā sabbaṃ asesaṃ nissesaṃ samādāya vattati."].count(
    "всецело, во всех отношениях, без остатка, полностью") == 1
KATHAM_TAIL = {   # Seyyathāpi … sentence
    "mettā": ("Seyyathāpi nāma ekaṃ puggalaṃ piyaṃ manāpaṃ disvā mettāyeyya, evameva sabbe satte mettāya pharati.",
              "увидев одного человека, дорогого и приятного, проникся бы к нему доброжелательностью"),
    "karuṇā": ("Seyyathāpi nāma ekaṃ puggalaṃ duggataṃ durūpetaṃ disvā karuṇāyeyya, evameva sabbe satte karuṇāya "
               "pharati.", "увидев одного человека, бедствующего и обездоленного, проникся бы к нему состраданием"),
    "muditā": ("Seyyathāpi nāma ekaṃ puggalaṃ piyaṃ manāpaṃ disvā mudito assa, evameva sabbe satte muditāya pharati.",
               "увидев одного человека, дорогого и приятного, порадовался бы за него"),
    "upekkhā": ("Seyyathāpi nāma ekaṃ puggalaṃ neva manāpaṃ na amanāpaṃ disvā upekkhako assa, evameva sabbe satte "
                "upekkhāya pharati.", "увидев одного человека, ни приятного, ни неприятного, остался бы к нему "
                                      "невозмутимым"),
}
for k in K4:
    nom, ins, g = AP[k]
    kc = cap(k)
    SENT13[f"Kathañca bhikkhu {k}sahagatena cetasā ekaṃ disaṃ pharitvā viharati?"] = (
        f"Как монах пребывает, наполнив {ONE_DIR} {SAHA[k]}?")
    SENT13[KATHAM_TAIL[k][0]] = (f"Подобно тому как кто-либо, {KATHAM_TAIL[k][1]}, так же он наполняет {ins} всех "
                                 f"существ.")
    SENT13[f"Tattha katamā {k}?"] = f"{TATTHA} {nom}?"
    SENT13[f'"{kc}sahagatena cetasā"ti tattha katamā {k}?'] = f"«{cap(SAHA[k])}»: {lc(TATTHA)} {nom}?"
    SENT13[f'"{kc}sahagatena cetasā"ti, tattha katamā {k}?'] = f"«{cap(SAHA[k])}»: {lc(TATTHA)} {nom}?"   # ^2-679
    SENT13[f'Yā sattesu {SYN[k]} – ayaṃ vuccati "{k}".'] = f"{BODY_S[k]}, {DASH} {called(ins)}."
    SENT13[f"Idaṃ cittaṃ imāya {k[:-1]}āya sahagataṃ hoti sahajātaṃ saṃsaṭṭhaṃ sampayuttaṃ."] = (
        f"Этот ум сопровождается {THIS_INS[g]} {ins}, рождён вместе с {PRON_INS[g]}, соединён с {PRON_INS[g]}, связан "
        f"с {PRON_INS[g]}.")
    SENT13[f'Tena vuccati "{k}sahagatena cetasā"ti.'] = f"{TENA} «{SAHA[k]}»."
assert X.SENT12["Idaṃ sukhaṃ imāya pītiyā sahagataṃ hoti sahajātaṃ saṃsaṭṭhaṃ sampayuttaṃ."].endswith(
    "рождено вместе с ним, соединено с ним, связано с ним.")


def sent13(s):
    if s in SENT13:
        return SENT13[s]
    if s.startswith('"Viharatī"ti') or s.startswith("Tena vuccati \"viharatī\""):
        return X.sent12(s)
    raise KeyError("ch13 sentence: " + s[:120])


# Abhidhamma of ch. 13: extend the ch. 12 machinery (in memory only)
for k in K4:
    nom, ins, g = AP[k]
    X.ATERM[k] = (nom, ins)
    X.ADEF[f"Yā {SYN[k]}"] = BODY_A[k]
    X.QUAL[f"{k}sahagataṃ"] = f", сопровождаемое {ins},"
    X.ASENT[f"Avasesā dhammā {k[:-1]}āya sampayuttā."] = f"Остальные явления связаны с {ins}."
X.JH_HEAD["sukhassa ca pahānā dukkhassa ca pahānā…pe…"] = (False, "с устранением приятного и с устранением болезненного…")
in_pi1("с устранением приятного и с устранением болезненного")
X.ASENT["Catasso appamaññāyo – mettā, karuṇā, muditā, upekkhā."] = FOUR_AP_LINE
X.ASENT["Tattha katamā karuṇā…pe… tattha katamā muditā…pe… tattha katamā upekkhā?"] = (
    f"{TATTHA} {AP['karuṇā'][0]}… {lc(TATTHA)} {AP['muditā'][0]}… {lc(TATTHA)} {AP['upekkhā'][0]}?")

# ================================================================ 2. the training rules (chapter 14)
PRECEPT = {   # Pāli ablative -> Russian genitive after «от»
    "pāṇātipātā": "убийства живых существ",                                         # pi-4 / pi-5
    "adinnādānā": "взятия того, что не дано",                                        # pi-4 words
    "kāmesumicchācārā": "неподобающего поведения в чувственных удовольствиях",      # pi-4
    "musāvādā": "лжи",                                                             # pi-4
    "surāmerayamajjapamādaṭṭhānā": "употребления спиртного, браги и опьяняющих напитков, ведущего к беспечности",  # pi-5
}
P5 = list(PRECEPT)
RULE = "правило обучения о воздержании от "            # X veramaṇī sikkhāpadaṃ [pi-5 veramaṇī «воздержание»]
RULE_INS = "правилом обучения о воздержании от "
FIVE_RULES = "Пять правил обучения"
FIVE_RULES_P = "Pañca sikkhāpadāni – " + ", ".join(f"{p} veramaṇī sikkhāpadaṃ" for p in P5) + "."
FIVE_RULES_R = f"{FIVE_RULES} {DASH} " + T.enum([RULE + PRECEPT[p] for p in P5]) + "."
ABST_TAIL = ("воздержание, полное воздержание, уклонение, неделание, несовершение, невпадение в проступок, "
             "непереступание границы, разрушение моста")                         # pi-1 ^1-299 … ^1-301
in_pi1("отстранение от четырёх видов дурного речевого поведения, " + ABST_TAIL)
ABST_P = "ārati virati paṭivirati veramaṇī akiriyā akaraṇaṃ anajjhāpatti velāanatikkamo setughāto"
CETANA_R = G.CETANA                                      # намерение, проявление намерения, состояние намеренности
in_pi1(CETANA_R)
PHASSA_PAGGAHA = "контакт… напряжение сил, отсутствие отвлечения"                # phasso…pe… paggāho avikkhepo [pi-1]
in_pi1("напряжение сил, отсутствие отвлечения")

# extra mind-type tokens (pi-1 ^1-269: hīna … vīmaṃsādhipateyya)
_ADHIP = {"chand": "желания", "vīriy": "усердия", "citt": "ума", "vīmaṃs": "пытливости"}
G.TOKENS += [(re.compile(p), f) for p, f in [
    (r"hīnaṃ", lambda m, g: ("низший", g, None)),
    (r"majjhimaṃ", lambda m, g: ("средний", g, None)),
    (r"paṇītaṃ", lambda m, g: ("высший", g, None)),
    (r"(chand|vīriy|citt|vīmaṃs)ādhipateyyaṃ", lambda m, g: (f"с преобладанием {_ADHIP[m.group(1)]}", g, None)),
]]
in_pi1("связанный со знанием, низший… средний… высший… с преобладанием желания… с преобладанием усердия… с "
       "преобладанием ума… с преобладанием пытливости… с преобладанием желания, низший…")


def mind(d):
    """the mind-type description after "Yasmiṃ samaye " (kāma sphere, possibly with "… " separators)."""
    return G.desc(re.sub(r"(?<!pe)… ", "…pe… ", d))


def rule_q(s):
    """'Tattha katamaṃ X veramaṇī sikkhāpadaṃ[…pe… Y veramaṇī sikkhāpadaṃ …]?'"""
    m = re.match(r"^Tattha katamaṃ (.+)\?$", s)
    items = m.group(1).split("…pe… ")
    out = []
    for it in items:
        mm = re.match(r"^(\S+) veramaṇī sikkhāpadaṃ$", it)
        out.append(RULE + PRECEPT[mm.group(1)])
    return f"{TATTHA} " + "… ".join(out) + "?"


def rule_open(s):
    """'Yasmiṃ samaye <mind> <X> viramantassa' -> «В то время, когда у того, кто воздерживается от …, возникает …»"""
    m = re.match(r"^Yasmiṃ samaye (.+) (\S+) viramantassa$", s)
    d, x = m.group(1), m.group(2)
    return f"В то время, когда у того, кто воздерживается от {PRECEPT[x]}, {mind(d)}"


def rule_tail(t, x_called):
    """after the opening: ', yā tasmiṃ samaye … – idaṃ vuccati "…"' etc."""
    m = re.match(r"^, yā tasmiṃ samaye (\S+) " + ABST_P + r" – idaṃ vuccati \"(.+)\"$", t)
    if m:
        return f", то, что в это время есть отстранение от {PRECEPT[m.group(1)]}, {ABST_TAIL}, {DASH} {x_called(m.group(2))}"
    m = re.match(r"^, yā tasmiṃ samaye cetanā sañcetanā sañcetayitattaṃ – idaṃ vuccati \"(.+)\"$", t)
    if m:
        return f", то, что в это время есть {CETANA_R}, {DASH} {x_called(m.group(1))}"
    m = re.match(r"^, yo tasmiṃ samaye phasso…pe… paggāho avikkhepo – idaṃ vuccati \"(.+)\"$", t)
    if m:
        return f", то, что в это время есть {PHASSA_PAGGAHA}, {DASH} {x_called(m.group(1))}"
    m = re.match(r"^ phasso…pe… paggāho avikkhepo – idaṃ vuccati \"(.+)\"$", t)   # ^2-705: as written
    if m:
        return f", {PHASSA_PAGGAHA} {DASH} {x_called(m.group(1))}"
    raise KeyError("rule tail: " + t[:120])


def rule_called(term):
    m = re.match(r"^(\S+) veramaṇī sikkhāpadaṃ$", term)
    return called(RULE_INS + PRECEPT[m.group(1)])


AVAS14 = {"veramaṇiyā": "воздержанием", "cetanāya": "намерением"}


def avas14(s):
    """'Avasesā dhammā X sampayuttā[…pe… avasesā dhammā Y sampayuttā…pe… phasso…pe… paggāho avikkhepo – idaṃ …].'"""
    parts = s[:-1].split("…pe… ")
    out = []
    i = 0
    while i < len(parts):
        x = parts[i]
        m = re.match(r"^[Aa]vasesā dhammā (\S+) sampayuttā$", x)
        if m:
            out.append(f"остальные явления связаны с {AVAS14[m.group(1)]}")
            i += 1
            continue
        if x == "phasso" and re.match(r"^paggāho avikkhepo – idaṃ vuccati \"(.+)\"$", parts[i + 1]):
            mm = re.match(r"^paggāho avikkhepo – idaṃ vuccati \"(.+)\"$", parts[i + 1])
            out.append(f"{PHASSA_PAGGAHA} {DASH} {rule_called(mm.group(1))}")
            i += 2
            continue
        raise KeyError("avas14: " + x[:80])
    return cap("… ".join(out)) + "."


def rule_line(t):
    """'Tattha katamaṃ …? Yasmiṃ samaye … viramantassa<tail>. [Avasesā …]'"""
    m = re.match(r"^(Tattha katamaṃ .+?\?) (Yasmiṃ samaye .+? viramantassa)((?:,| phasso…pe…) .+?)\.(?: (.+))?$", t)
    if not m:
        raise KeyError("rule line: " + t[:120])
    q, op, tl, rest = m.groups()
    r = f"{rule_q(q)} {rule_open(op)}{rule_tail(tl, rule_called)}."
    if rest:
        r += " " + avas14(rest)
    return r


# ================================================================ 3. analytical knowledges (chapter 15)
PS = {"attha": ("аналитическое знание смысла", "аналитическим знанием смысла"),
      "dhamma": ("аналитическое знание явлений", "аналитическим знанием явлений"),
      "nirutti": ("аналитическое знание выражений", "аналитическим знанием выражений"),
      "paṭibhāna": ("аналитическое знание находчивости", "аналитическим знанием находчивости")}   # pi-5 paṭisambhidā
PS4 = ["attha", "dhamma", "nirutti", "paṭibhāna"]
FOUR_PS = "Четыре аналитических знания"
THREE_PS = "Три аналитических знания"
VAR_PATIBHANA = " [вариант написания (Syā.): paṭibhāṇapaṭisambhidā; так же и далее]"   # "evamuparipi" as ch12
FOUR_PS_P = "Catasso paṭisambhidā – " + ", ".join(k + "paṭisambhidā" for k in PS4) + "."
FOUR_PS_R = f"{FOUR_PS} {DASH} " + T.enum([PS[k][0] for k in PS4]) + "."
THREE_PS_P = "Tisso paṭisambhidā – atthapaṭisambhidā, niruttipaṭisambhidā, paṭibhānapaṭisambhidā."
THREE_PS_R = f"{THREE_PS} {DASH} " + T.enum([PS[k][0] for k in ("attha", "nirutti", "paṭibhāna")]) + "."


def kn(gen, k):
    return f"знание {gen} является {PS[k][1]}"


TATRA = kn("высказывания этого выражения явлений", "nirutti")        # tatra dhammaniruttābhilāpe ñāṇaṃ …
NANESU = kn("знаний", "paṭibhāna")                                    # ñāṇesu ñāṇaṃ paṭibhānapaṭisambhidā
YAYA = cap(kn("высказывания того выражения явлений, которым эти явления обозначаются,", "nirutti"))
YENA = (f"Знание, которым он знает эти знания {DASH} «Эти знания проясняют этот смысл», то есть знание знаний, является "
        f"{PS['paṭibhāna'][1]}")
LOC = {   # Pāli locative (+ " ñāṇaṃ") -> Russian genitive
    "Atthe": "смысла", "dhamme": "явлений",
    "Dukkhe": "страдания", "dukkhasamudaye": "возникновения страдания", "dukkhanirodhe": "прекращения страдания",
    "dukkhanirodhagāminiyā paṭipadāya": "способа практики, ведущего к прекращению страдания,",
    "Hetumhi": "причины", "hetuphale": "плода причины",
    "Jarāmaraṇe": "старения и смерти", "jarāmaraṇasamudaye": "возникновения старения и смерти",
    "jarāmaraṇanirodhe": "прекращения старения и смерти",
    "jarāmaraṇanirodhagāminiyā paṭipadāya": "способа практики, ведущего к прекращению старения и смерти,",
    "Jātiyā": "рождения", "bhave": "существования", "upādāne": "цепляния", "taṇhāya": "жажды", "vedanāya": "чувства",
    "phasse": "контакта", "saḷāyatane": "шести сфер восприятия", "nāmarūpe": "умственного и материальной формы",
    "viññāṇe": "сознания", "saṅkhāresu": "формирующих факторов", "saṅkhārasamudaye": "возникновения формирующих факторов",
    "saṅkhāranirodhe": "прекращения формирующих факторов",
    "saṅkhāranirodhagāminiyā paṭipadāya": "способа практики, ведущего к прекращению формирующих факторов,",
}
in_pi1("способа практики, ведущего к прекращению страдания")
JATA6 = "родились, стали существовать, зародились, возникли, полностью возникли, проявились"   # ch12 JATA + bhūtā
assert X.JATA == "родились, зародились, возникли, полностью возникли, проявились"
HEAD15 = {"Saṅgahavāro": "Раздел обобщения", "Saccavāro": "Раздел об истинах", "Hetuvāro": "Раздел о причине",
          "Dhammavāro": "Раздел о явлениях",
          "Paṭiccasamuppādavāro": "Раздел о возникновении в зависимости от условий",
          "Pariyattivāro": "Раздел об изучении Учения", "Kusalavāro": "Раздел о благом",
          "Akusalavāro": "Раздел о неблагом", "Vipākavāro": "Раздел о результатах действий",
          "Kiriyavāro": "Раздел о функциональном"}


def ps_clause(c):
    """'<loc> ñāṇaṃ <k>paṭisambhidā' / tatra … / ñāṇesu …"""
    if c in ("tatra dhammaniruttābhilāpe ñāṇaṃ niruttipaṭisambhidā", "Tatra dhammaniruttābhilāpe ñāṇaṃ niruttipaṭisambhidā"):
        return TATRA
    if c in ("ñāṇesu ñāṇaṃ paṭibhānapaṭisambhidā", "Ñāṇesu ñāṇaṃ paṭibhānapaṭisambhidā"):
        return NANESU
    m = re.match(r"^(.+) ñāṇaṃ (attha|dhamma)paṭisambhidā$", c)
    if m:
        return kn(LOC[m.group(1)], m.group(2))
    raise KeyError("ps clause: " + c)


def ps_clauses(body):
    """comma / semicolon separated clauses, with '…pe…' runs ("Jātiyā ñāṇaṃ…pe… bhave ñāṇaṃ…pe… …")."""
    out = []
    for part in re.split(r"(, |; )", body):
        if part in (", ", "; "):
            out.append(part)
            continue
        if "…pe… " in part:
            bits = part.split("…pe… ")
            rr = [f"знание {LOC[b[:-len(' ñāṇaṃ')]]}" for b in bits[:-1]]
            out.append("… ".join(rr + [ps_clause(bits[-1])]))
        else:
            out.append(ps_clause(part))
    return cap("".join(out))


SENT15 = {
    FOUR_PS_P.replace("paṭibhānapaṭisambhidā.", "paṭibhānapaṭisambhidā [paṭibhāṇapaṭisambhidā (syā.) evamuparipi]."):
        FOUR_PS_R[:-1] + VAR_PATIBHANA + ".",
    FOUR_PS_P: FOUR_PS_R,
    FOUR_PS_P.replace("dhammapaṭisambhidā, niruttipaṭisambhidā", "dhammapaṭisambhidā niruttipaṭisambhidā"): FOUR_PS_R,
    THREE_PS_P: THREE_PS_R,
    "Ayaṃ saṅgahavāro.": "Это раздел обобщения.", "Ayaṃ saccavāro.": "Это раздел об истинах.",
    "Ayaṃ hetuvāro.": "Это раздел о причине.", "Ayaṃ dhammavāro.": "Это раздел о явлениях.",
    "Ayaṃ paṭiccasamuppādavāro.": "Это раздел о возникновении в зависимости от условий.",
    "Ayaṃ pariyattivāro.": "Это раздел об изучении Учения.",
    "Ye dhammā jātā bhūtā sañjātā nibbattā abhinibbattā pātubhūtā, imesu dhammesu ñāṇaṃ atthapaṭisambhidā; yamhā "
    "dhammā te dhammā jātā bhūtā sañjātā nibbattā abhinibbattā pātubhūtā, tesu dhammesu ñāṇaṃ dhammapaṭisambhidā; "
    "tatra dhammaniruttābhilāpe ñāṇaṃ niruttipaṭisambhidā; ñāṇesu ñāṇaṃ paṭibhānapaṭisambhidā.":
        f"{cap(kn(f'тех явлений, которые {JATA6},', 'attha'))}; {kn(f'тех явлений, из которых эти явления {JATA6},', 'dhamma')}; "
        f"{TATRA}; {NANESU}.",
    # Pariyattivāra
    "Tattha katamā dhammapaṭisambhidā?": f"{TATTHA} {PS['dhamma'][0]}?",
    "Idha bhikkhu dhammaṃ jānāti – suttaṃ geyyaṃ veyyākaraṇaṃ gāthaṃ udānaṃ itivuttakaṃ jātakaṃ abbhutadhammaṃ vedallaṃ.":
        f"Вот монах знает Учение {DASH} беседы, прозу со стихами, разъяснения, строфы, вдохновенные изречения, изречения "
        f"«Так было сказано», истории о прошлых рождениях, рассказы о чудесном, вопросы и ответы.",
    'Ayaṃ vuccati "dhammapaṭisambhidā".': cap(called(PS["dhamma"][1])) + ".",
    'So tassa tasseva bhāsitassa atthaṃ jānāti – "ayaṃ imassa bhāsitassa attho, ayaṃ imassa bhāsitassa attho"ti.':
        f"Он знает смысл того или иного сказанного {DASH} «Это смысл этого сказанного, это смысл этого сказанного».",
    'Ayaṃ vuccati "atthapaṭisambhidā".': cap(called(PS["attha"][1])) + ".",
    "Tatra dhammaniruttābhilāpe ñāṇaṃ niruttipaṭisambhidā.": cap(TATRA) + ".",
    "Ñāṇesu ñāṇaṃ paṭibhānapaṭisambhidā.": cap(NANESU) + ".",
    # Abhidhamma
    "Katame dhammā kusalā?": "Что такое благие явления?",
    "Katame dhammā akusalā?": "Что такое неблагие явления?",
    "Katame dhammā abyākatā?": "Что такое этически неопределённые явления?",
    "Katame dhammā sikkhā?": "Какие явления являются обучением?",
    "Ime dhammā kusalā.": "Это благие явления.", "Ime dhammā akusalā.": "Это неблагие явления.",
    "Ime dhammā abyākatā.": "Это этически неопределённые явления.",
    "Ime dhammā sikkhā.": "Эти явления являются обучением.",
    "Imesu dhammesu ñāṇaṃ dhammapaṭisambhidā.": cap(kn("этих явлений", "dhamma")) + ".",
    "Imesu dhammesu ñāṇaṃ atthapaṭisambhidā.": cap(kn("этих явлений", "attha")) + ".",
    "Tesaṃ vipāke ñāṇaṃ atthapaṭisambhidā.": cap(kn("их результата", "attha")) + ".",
    "Tesaṃ vipāke ñāṇaṃ atthapaṭisambhidā, yāya niruttiyā tesaṃ dhammānaṃ paññatti hoti, tatra dhammaniruttābhilāpe "
    "ñāṇaṃ niruttipaṭisambhidā.": cap(kn("их результата", "attha")) + ", " + lc(YAYA) + ".",
    "Yāya niruttiyā tesaṃ dhammānaṃ paññatti hoti tatra dhammaniruttābhilāpe ñāṇaṃ niruttipaṭisambhidā.": YAYA + ".",
    'Yena ñāṇena tāni ñāṇāni jānāti – "imāni ñāṇāni idamatthajotakānī"ti, ñāṇesu ñāṇaṃ paṭibhānapaṭisambhidā.': YENA + ".",
    # ^2-746
    "Tisso paṭisambhidā kāmāvacarakusalato catūsu ñāṇasampayuttesu cittuppādesu, kiriyato catūsu ñāṇasampayuttesu "
    "cittuppādesu uppajjanti.":
        f"{THREE_PS} возникают в четырёх видах благого ума, относящегося к миру чувственных желаний, связанных со "
        f"знанием, и в четырёх видах функционального ума, связанных со знанием.",
    "Atthapaṭisambhidā etesu ceva uppajjati, catūsu maggesu catūsu phalesu ca uppajjati.":
        f"{cap(PS['attha'][0])} возникает и в них, и возникает в четырёх путях и четырёх плодах.",
}
in_pi1("Двенадцать видов неблагого ума")      # cittuppāda = вид ума [pi-1 ^1-1385]

# full phenomenon lists of the vipāka / kiriya minds [pi-1 ^1-443, ^1-469, ^1-556 words]
PH = {"phasso": "контакт", "vedanā": "чувство", "saññā": "восприятие", "cetanā": "намерение", "cittaṃ": "ум",
      "vitakko": "направленная мысль", "vicāro": "удержание мысли", "pīti": "восторг", "dukkhaṃ": "боль",
      "upekkhā": "невозмутимость", "cittassekaggatā": "однонаправленность ума", "manindriyaṃ": "способность ума",
      "upekkhindriyaṃ": "способность невозмутимости", "sukhindriyaṃ": "способность удовольствия",
      "dukkhindriyaṃ": "способность боли", "somanassindriyaṃ": "способность радости",
      "jīvitindriyaṃ": "жизненная способность", "vīriyindriyaṃ": "способность усердия",
      "samādhindriyaṃ": "способность сосредоточения"}
YE_VA_P = "ye vā pana tasmiṃ samaye aññepi atthi paṭiccasamuppannā arūpino dhammā"
YE_VA_R = "или же какие бы другие нематериальные явления, возникшие в зависимости от условий, ни были в это время"
in_pi1(YE_VA_R, "есть контакт, есть чувство, есть восприятие, есть намерение, есть ум, есть удовольствие, есть "
       "однонаправленность ума, есть способность ума, есть способность удовольствия, есть жизненная способность",
       "есть ум, есть боль, есть однонаправленность ума, есть способность ума, есть способность боли",
       "есть восторг, есть счастье, есть однонаправленность ума, есть способность ума, есть способность радости",
       "есть невозмутимость, есть однонаправленность ума, есть способность ума, есть способность невозмутимости")


def ph_list(p):
    """'phasso hoti, vedanā hoti, …, jīvitindriyaṃ hoti, ye vā pana …' -> «есть контакт, есть чувство, …, или же …»"""
    if p == "phasso hoti…pe… avikkhepo hoti":
        return "есть контакт… есть отсутствие отвлечения"
    items = p.split(", ")
    assert items[-1] == YE_VA_P, p[-80:]
    words = [x[:-len(" hoti")] for x in items[:-1]]
    assert all(x.endswith(" hoti") for x in items[:-1])
    sukha = "удовольствие" if "sukhindriyaṃ" in words else "счастье"
    return ", ".join("есть " + (sukha if w == "sukhaṃ" else PH[w]) for w in words) + ", " + YE_VA_R


LOK_V_KAMMA = edit(G.LOK_V_SUNNA, "надмирского благого медитативного погружения", "надмирского благого действия")
TASSEVA15 = dict(G.TASSEVA)
TASSEVA15["lokuttarassa kusalassa kammassa katattā bhāvitattā vipākaṃ vivicceva kāmehi…pe… paṭhamaṃ jhānaṃ upasampajja "
          "viharati dukkhapaṭipadaṃ dandhābhiññaṃ suññataṃ"] = LOK_V_KAMMA                # ^2-740 as written
_ARUPA_F_TAIL = G.ARUPA_F[G.ARUPA_F.index("медитативное погружение, относящееся к миру без форм"):]
KIRIYA745_P = ("…pe… rūpāvacaraṃ jhānaṃ bhāveti…pe… arūpāvacaraṃ jhānaṃ bhāveti kiriyaṃ neva kusalaṃ nākusalaṃ na ca "
               "kammavipākaṃ diṭṭhadhammasukhavihāraṃ…pe… sabbaso ākiñcaññāyatanaṃ samatikkamma "
               "nevasaññānāsaññāyatanasaññāsahagataṃ sukhassa ca pahānā…pe… catutthaṃ jhānaṃ upasampajja viharati")
KIRIYA745_R = ("… кто-либо развивает медитативное погружение, относящееся к миру форм… развивает "
               + edit(_ARUPA_F_TAIL, "для пребывания в счастье в этой жизни и, полностью преодолев",
                      "для пребывания в счастье в этой жизни… полностью преодолев"))
in_pi1("кто-либо развивает медитативное погружение, относящееся к миру форм")
SIKKHA713_P = ("rūpūpapattiyā maggaṃ bhāveti…pe… arūpūpapattiyā maggaṃ bhāveti…pe… " + G.P_LOK)
SIKKHA713_R = ("кто-либо развивает путь к рождению в мире форм… развивает путь к рождению в мире без форм… "
               + G.LOK_K[len("кто-либо "):])


def when15(d):
    if d == SIKKHA713_P:
        return "В то время, когда " + SIKKHA713_R
    if d.endswith(KIRIYA745_P):
        return "В то время, когда " + mind(d[:-len(KIRIYA745_P)]) + KIRIYA745_R
    if d in G.JHANA:
        return "В то время, когда " + G.JHANA[d]
    return "В то время, когда " + mind(d)


def ps_sentence(s):
    if s in SENT15:
        return SENT15[s]
    m = re.match(r"^Yasmiṃ samaye (.+?), tasmiṃ samaye (.+?)(, ime dhammā (kusalā))?\.$", s)
    if m:
        r = f"{when15(m.group(1))}, в это время {ph_list(m.group(2))}"
        if m.group(3):
            r += ", это благие явления"
        return r + "."
    m = re.match(r"^Tasseva (.+?), tasmiṃ samaye phasso hoti…pe… avikkhepo hoti\.$", s)
    if m:
        return f"{TASSEVA15[m.group(1)]}, в это время есть контакт… есть отсутствие отвлечения."
    m = re.match(r"^(Catasso paṭisambhidā – .+?\.|Tisso paṭisambhidā – .+?\.) (.+)$", s)
    if m:   # the list sentence and the next one on one Pāli line (^2-734)
        return ps_sentence(m.group(1)) + " " + ps_sentence(m.group(2))
    m = re.match(r"^(.+ ñāṇaṃ (?:attha|dhamma)paṭisambhidā(?:, |; ).+)\.$", s)
    if m:
        return ps_clauses(m.group(1)) + "."
    raise KeyError("ch15 sentence: " + s[:140])


def ps_line(t):
    out = []
    for s in SPLIT.split(t):
        out.append(ps_sentence(s))
    return " ".join(out)


# ================================================================ 4. Pañhāpucchaka (extend the ch. 12 machinery)
NEW_SUBJ = {
    "Tisso appamaññāyo": (FOUR_AP.replace("Четыре", "Три"), FOUR_AP.replace("Четыре", "Три"), "pl", None),
    "tisso appamaññāyo": ("три безмерных состояния", "три безмерных состояния", "pl", None),
    "Mettā": ("Доброжелательность", "Доброжелательность", "sg", "f"),
    "mettā": ("доброжелательность", "доброжелательность", "sg", "f"),
    "Upekkhā": ("Невозмутимость", "Невозмутимость", "sg", "f"),
    "upekkhā": ("невозмутимость", "невозмутимость", "sg", "f"),
    "Tisso paṭisambhidā": (THREE_PS, THREE_PS, "pl", None),
    "tisso paṭisambhidā": (low(THREE_PS), low(THREE_PS), "pl", None),
    "dve paṭisambhidā": ("два аналитических знания", "два аналитических знания", "pl", None),
    "atthapaṭisambhidā": (PS["attha"][0], PS["attha"][0], "sg", "n"),
    "Niruttipaṭisambhidā": (cap(PS["nirutti"][0]), cap(PS["nirutti"][0]), "sg", "n"),
}
for _k, _v in NEW_SUBJ.items():
    assert _k not in T.SUBJ2 or T.SUBJ2[_k] == _v, _k
    T.SUBJ2[_k] = _v
T.SUBJ_RE2 = re.compile(r"^(" + "|".join(map(re.escape, sorted(T.SUBJ2, key=len, reverse=True))) + r") (.+)$")
T.alias("acaya", "ācayagāminī")                     # feminine singular forms (atthapaṭisambhidā)
T.alias("apacaya", "apacayagāminī")
T.alias("nevacaya", "nevācayagāmināpacayagāminī")
T.alias("maggadhipati", "maggādhipatinī")
T.alias("hetu_sahetuka", "hetū ceva sahetukā ca")
T.alias("hetu_hetusampayutta", "hetū ceva hetusampayuttā ca")
X.PFIX += [   # spelling / spacing slips in the Pāli (reported), rendered as meant
    ("anidassanaapaṭighā", "anidassanaappaṭighā"),                 # ^2-749
    ("Anidassanaapaṭighā", "Anidassanaappaṭighā"),
    ("nahetūahetukātipi", "na hetūahetukātipi"),                   # ^2-750
    ("na hetu sahetūkā", "na hetu sahetukā"),                      # ^2-717
    ("na bhāvanāyapahātabbā", "na bhāvanāya pahātabbā"),           # ^2-717
]
_PQ_CHUNK = X.pq_chunk


def pq_chunk(c, st):
    """adds 'X na vattabbā – Ytipi' (ch. 15 ^2-749: unquoted, with a dash)."""
    m = re.match(r"^(\S+) na vattabbā – (.+?)(n?ti(?:pi)?)$", c)
    if m and m.group(1) in T.SUBJ2:
        subj = T.SUBJ2[m.group(1)]
        st["num"], st["g"] = subj[2], subj[3]
        st["nv"] = True
        return f"{subj[1]} {Z.NV} {DASH} {X.quote(m.group(2), m.group(3), st)}"
    return _PQ_CHUNK(c, st)


X.pq_chunk = pq_chunk
T.KEEP_OI.add("собой")      # «имеет над собой высшее»: masc() must not touch «собой» (neuter subject, ch. 15)

POST = {   # context: after "atthapaṭisambhidā … siyā lokuttarā" the Pāli "kenaci (na) viññeyyā" is about all four
    "иногда является надмирским, познаётся тем или иным видом сознания, не познаётся тем или иным видом сознания":
        "иногда является надмирским, познаются тем или иным видом сознания, не познаются тем или иным видом сознания",
}

VAR_ASAVO_P = " [āsavā (sī.) dhātuvibhaṅge pana pāṭhanānattaṃ natthi]"
VAR_ASAVO_Q = " [вариант чтения (Sī.): āsavā; но в „Разборе элементов“ разночтений нет]"   # inside «…»
VAR_ASAVO_R = " [вариант чтения (Sī.): āsavā; но в «Разборе элементов» разночтений нет]"
assert S.CHAPTER_TITLES[3] == "Разбор элементов"


def pq(t):
    if VAR_ASAVO_P in t:
        assert t.count(VAR_ASAVO_P) == 2
        r = X.pq_line(t.replace(VAR_ASAVO_P, ""), LABELS)
        a = "«явление, являющееся влечением и подверженное влечениям»"
        b = "иногда подвержено влечениям, но не является влечением"
        assert r.count(a) == 1 and r.count(b) == 1, r
        r = r.replace(a, a.replace("влечением и", "влечением" + VAR_ASAVO_Q + " и"))
        return r.replace(b, b + VAR_ASAVO_R)
    r = X.pq_line(t, LABELS)
    for a, b in POST.items():
        if a in r:
            assert r.count(a) == 1
            r = r.replace(a, b)
    return r


LABELS = {
    "##### Tikaṃ": B.LABELS["##### Tikaṃ"], "##### Dukaṃ": B.LABELS["##### Dukaṃ"],
    "Pañhāpucchakaṃ.": SEC["Pañhāpucchakaṃ"] + ".",
    "Catunnaṃ appamaññānaṃ kati kusalā, kati akusalā, kati abyākatā…pe… kati saraṇā, kati araṇā?":
        T.how_many_q("четырёх безмерных состояний"),
    "Pañcannaṃ sikkhāpadānaṃ kati kusalā, kati akusalā, kati abyākatā…pe… kati saraṇā, kati araṇā?":
        T.how_many_q("пяти правил обучения"),
    "Catunnaṃ paṭisambhidānaṃ kati kusalā, kati akusalā, kati abyākatā…pe… kati saraṇā, kati araṇā?":
        T.how_many_q("четырёх аналитических знаний"),
    ROOT699_P: ROOT699_R, FIVE_RULES_P: FIVE_RULES_R, FOUR_PS_P: FOUR_PS_R,
}

# ================================================================ 5. chapters
TITLE = {"Appamaññāvibhaṅgo": 13, "Sikkhāpadavibhaṅgo": 14, "Paṭisambhidāvibhaṅgo": 15}
HEAD13 = {"Mettā": cap(AP["mettā"][0]), "Karuṇā": cap(AP["karuṇā"][0]), "Muditā": cap(AP["muditā"][0]),
          "Upekkhā": cap(AP["upekkhā"][0])}
FIXES = [   # (Pāli as written, as meant): punctuation / spelling slips only, all reported
    ('"Viharatī"ti …pe…', '"Viharatī"ti…pe…'),                                    # ^2-672
    ("muditā muditāyatanā muditāyitattaṃ", "muditā muditāyanā muditāyitattaṃ"),  # ^2-688
    ("majjhimaṃ … paṇītaṃ", "majjhimaṃ… paṇītaṃ"),                                 # ^2-709
    ("vīriyādhipateyyaṃ … cittādhipateyyaṃ", "vīriyādhipateyyaṃ… cittādhipateyyaṃ"),   # ^2-710
    ("veramaṇiyā sampayuttā …pe…", "veramaṇiyā sampayuttā…pe…"),                  # ^2-710
    ("veramaṇī sikkhāpadaṃ, yasmiṃ samaye", "veramaṇī sikkhāpadaṃ? Yasmiṃ samaye"),   # ^2-706
    ("Yasmiṃ samaye kāmāvacare kusalaṃ", "Yasmiṃ samaye kāmāvacaraṃ kusalaṃ"),     # ^2-711
]


def text_line(t, ch, section, head):
    for a, b in FIXES:
        t = t.replace(a, b)
    if section == "Pañhāpucchakaṃ":
        return pq(t)
    if ch == 13:
        if t == ROOT642_P:
            return ROOT642_R
        if section == "Abhidhammabhājanīyaṃ":
            if t in X.ASENT:
                return X.ASENT[t]
            return X.abhi_line(t)
        return " ".join(sent13(s) for s in SPLIT.split(t))
    if ch == 14:
        if t == FIVE_RULES_P:
            return FIVE_RULES_R
        if t.startswith("Tattha katamaṃ "):
            return rule_line(t)
        return ps_line(t)
    return ps_line(t)


def build_chapter(pali, ch):
    out = []
    section = head = None
    for t in pali:
        if t.startswith("### "):
            out.append("### " + S.CHAPTER_TITLES[TITLE[t[4:]]])
        elif t.startswith("#### "):
            section = t[5:]
            out.append("#### " + SEC[section])
        elif t.startswith("##### "):
            head = t[6:]
            if t in LABELS:
                out.append(LABELS[t])
            else:
                out.append("##### " + (HEAD13.get(head) or HEAD15[head]))
        elif t.endswith(".") and t[:-1] in SEC:
            out.append(SEC[t[:-1]] + ".")
        elif t.endswith(" niṭṭhito."):
            out.append(S.CHAPTER_CLOSING.format(title=S.CHAPTER_TITLES[TITLE[t[:-len(" niṭṭhito.")]]]))
        else:
            out.append(text_line(t, ch, section, head))
    return out


def build(fn, ch):
    pali = open(os.path.join(S.PALI_DIR, fn), encoding="utf-8").read().rstrip("\n").split("\n")
    nonempty = [S.ID.sub("", l).rstrip() for l in pali if l.strip()]
    ru = build_chapter(nonempty, ch)
    assert len(ru) == len(nonempty), (fn, len(ru), len(nonempty))
    for p, r in zip(nonempty, ru):
        assert p.count(DASH) + p.count("—") == r.count(DASH), ("dash count", p[:70], r[:70])
        assert "—" not in r and "\x01" not in r and "\x02" not in r and "  " not in r, r[:80]
        assert p.startswith("#") == r.startswith("#") and p.split(" ")[0].count("#") == r.split(" ")[0].count("#"), (p[:40], r[:40])
        assert not re.search(r"[A-Za-zĀāĪīŪūṬṭḌḍÑñṆṇṄṅṂṃḶḷ]", re.sub(r"\[[^\]]*\]", "", r)), ("latin", r[:120])
        assert not re.search(r"\bли\b", r), r[:80]
    lines = S.attach_ids(pali, ru)
    S.write(os.path.join(S.RU_DIR, fn), lines)
    print("OK:", fn, "|", len(ru), "non-empty lines")


def main():
    build("13-appamannavibhango.md", 13)
    build("14-sikkhapadavibhango.md", 14)
    build("15-patisambhidavibhango.md", 15)


if __name__ == "__main__":
    main()
