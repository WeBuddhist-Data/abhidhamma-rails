"""Builder for the Russian rails translation of pi-2 (Vibhaṅga, plain audience), chapters 13, 14 and 15
(Appamaññāvibhaṅgo ^2-13-0 … ^2-702, Sikkhāpadavibhaṅgo ^2-14-0 … ^2-717, Paṭisambhidāvibhaṅgo ^2-15-0 … ^2-750).

Writes (only when run as a script):
  AI_translation/russian/pi-2-russian-plain-rails_split_chapters/13-appamannavibhango.md
  AI_translation/russian/pi-2-russian-plain-rails_split_chapters/14-sikkhapadavibhango.md
  AI_translation/russian/pi-2-russian-plain-rails_split_chapters/15-patisambhidavibhango.md
  0-INBOX/temp/pipeline/pi-2-ru/rails/notes-13-15.md   (new recurring formulas, Pāli = Russian)

Every Russian string comes from the fixed tables and functions below, so identical Pāli gives identical Russian.
Imported read-only: the approved sample builder (S) and the builders of chapters 1 (K1), 2-3 (K23), 4-5 (K45), 6 (K6),
7-9 (K79) and 10-12 (K10). Their tables are extended only in memory, here.

Shared passages reuse the earlier Russian: the jhāna openers, fields and Tasseva frames of ch. 6 / ch. 12 (pi-1
^1-251 … ^1-262 for the brahmavihāra jhānas), the mind-type openers of ch. 6 (pi-1 ^1-1, ^1-269, ^1-431 …), the
abstinence list of ch. 4 / ch. 11, the «Viharatī» definition of ch. 12, and the pi-1 Russian of the resultant and
functional mind frames (^1-431, ^1-443, ^1-455, ^1-469, ^1-568).

usage: python -I -X utf8 build_rails_13_15_ru.py
"""
import pathlib
import re
import sys

RAILS = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-ru\rails")
sys.path.insert(0, str(RAILS))
import build_rails_sample_ru as S  # noqa: E402  (importing writes nothing)
import build_rails_1_ru as K1      # noqa: E402
import build_rails_2_3_ru as K23   # noqa: E402
import build_rails_4_5_ru as K45   # noqa: E402
import build_rails_6_ru as K6      # noqa: E402
import build_rails_7_9_ru as K79   # noqa: E402
import build_rails_10_12_ru as K10  # noqa: E402

PARTS = {13: "13-appamannavibhango.md", 14: "14-sikkhapadavibhango.md", 15: "15-patisambhidavibhango.md"}
NOTES_PATH = RAILS / "notes-13-15.md"
cap, low, nlist = S.cap, K1.low, K45.nlist
SLIPS = []


def slip(msg):
    if msg not in SLIPS:
        SLIPS.append(msg)


DONE_LINES = {f"{S.CH_TITLE[c][0]} niṭṭhito.": f"{S.CH_TITLE[c][1]} {S.DONE}." for c in PARTS}
AT_TIME = K6.AT_TIME                       # tasmiṃ samaye = в это время
CONTACT_PE = K6.CONTACT_PE                 # phasso hoti…pe… avikkhepo hoti = есть контакт… есть отсутствие отвлечения
WHAT_AT_TIME = K79.WHAT_AT_TIME            # yo / yā tasmiṃ samaye … = то, что в это время есть …
WHEN = K6.WHEN                             # Yasmiṃ samaye = В то время, когда
KIND_Q = dict(K6.KIND_Q)                   # Katame dhammā kusalā? = Что такое благие явления?
THESE = {"kusalā": K79.ALL_THIS, "akusalā": "Это неблагие явления.",
         "abyākatā": "Это этически неопределённые явления."}       # Ime dhammā X. (pi-1 «– это X явления» without the dash)
ABSTAIN_TAIL = ("воздержание, полное воздержание, уклонение, неделание, несовершение, невпадение в проступок, "
                "непереступание границы, разрушение моста")       # virati … setughāto (ch. 4 / ch. 11)
CETANA3 = "намерение, проявление намерения, состояние намеренности"          # cetanā sañcetanā sañcetayitattaṃ (ch. 6)
PHASSA_PAGGAHA = "контакт… напряжение сил, отсутствие отвлечения"            # phasso…pe… paggāho avikkhepo (ch. 9)
CITTA_FULL = f"{K23.CITTA_SYN}, соответствующий элемент умственного сознания"   # Yaṃ cittaṃ mano … tajjāmanoviññāṇadhātu

# =========================================================================== chapter 13: the measureless states
AP = ["mettā", "karuṇā", "muditā", "upekkhā"]
AP_RU = {   # nominative, instrumental, genitive, «с ней / с ним»
    "mettā": ("доброжелательность", "доброжелательностью", "доброжелательности", "с ней"),
    "karuṇā": ("сострадание", "состраданием", "сострадания", "с ним"),
    "muditā": ("сорадование", "сорадованием", "сорадования", "с ним"),
    "upekkhā": ("невозмутимость", "невозмутимостью", "невозмутимости", "с ней"),
}
FOUR_AP = "Четыре безмерных состояния"                                         # Catasso appamaññāyo
FOUR_AP_LIST = f"{FOUR_AP} – " + nlist([AP_RU[k][0] for k in AP]) + "."


def ap_one(k):
    """X-sahagatena cetasā ekaṃ disaṃ pharitvā viharati, tathā dutiyaṃ, tathā tatiyaṃ, tathā catutthaṃ"""
    return (f"пребывает, наполнив одну сторону света умом, сопровождаемым {AP_RU[k][1]}, так же вторую, так же третью, "
            "так же четвёртую")


def ap_all(k):
    """(iti) uddhamadho tiriyaṃ sabbadhi sabbattatāya sabbāvantaṃ lokaṃ X-sahagatena cetasā vipulena mahaggatena
    appamāṇena averena abyāpajjena pharitvā viharati"""
    return (f"пребывает, наполнив вверх, вниз, в стороны, повсюду, ко всем как к себе, весь мир умом, сопровождаемым "
            f"{AP_RU[k][1]}, обширным, возвышенным, безмерным, свободным от вражды, свободным от неприязни")


V_CATUTTHI = "[вариант написания (Sī.): catutthiṃ]"
V_ABYAPAJJHENA = "[вариант написания (Sī., Syā.): abyāpajjhena]"
V_ABYAPAJJHO = "[вариант написания (Sī., Syā.): abyāpajjho]"


def ap_642():
    out = [f"{FOUR_AP} – здесь монах {ap_one('mettā')} {V_CATUTTHI}.", f"Так он {ap_all('mettā')} {V_ABYAPAJJHENA}."]
    for k in AP[1:]:
        out += [f"Он {ap_one(k)}.", f"Так он {ap_all(k)}."]
    return " ".join(out)


def ap_699():
    parts = [f"здесь монах {ap_one('mettā')}, так он {ap_all('mettā')}"]
    parts += [f"он {ap_one(k)}, так он {ap_all(k)}" for k in AP[1:]]
    return f"{FOUR_AP} – " + "; ".join(parts) + "."


SIMILE = {   # Seyyathāpi nāma ekaṃ puggalaṃ … disvā …, evameva sabbe satte X-āya pharati.
    "mettā": "Подобно тому как он, увидев одного дорогого, приятного человека, проникся бы к нему доброжелательностью",
    "karuṇā": "Подобно тому как он, увидев одного бедствующего, обездоленного человека, проникся бы к нему состраданием",
    "muditā": "Подобно тому как он, увидев одного дорогого, приятного человека, порадовался бы",
    "upekkhā": "Подобно тому как он, увидев одного человека, ни приятного, ни неприятного, был бы невозмутимым",
}
SIMILE_P = {
    "mettā": "Seyyathāpi nāma ekaṃ puggalaṃ piyaṃ manāpaṃ disvā mettāyeyya",
    "karuṇā": "Seyyathāpi nāma ekaṃ puggalaṃ duggataṃ durūpetaṃ disvā karuṇāyeyya",
    "muditā": "Seyyathāpi nāma ekaṃ puggalaṃ piyaṃ manāpaṃ disvā mudito assa",
    "upekkhā": "Seyyathāpi nāma ekaṃ puggalaṃ neva manāpaṃ na amanāpaṃ disvā upekkhako assa",
}
AP_LIST_P = {k: f"{'metti' if k == 'mettā' else k} {k}yanā {k}yitattaṃ {k}cetovimutti" for k in AP}
AP_LIST_RU = {k: f"{AP_RU[k][0]}, проявление {AP_RU[k][2]}, состояние {AP_RU[k][2]}, освобождение ума {AP_RU[k][1]}"
              for k in AP}
AP_LIST_BEINGS_RU = {k: AP_LIST_RU[k].replace(AP_RU[k][0], f"{AP_RU[k][0]} в отношении существ", 1) for k in AP}
TOPIC_SAHA = {k: f"Умом, сопровождаемым {AP_RU[k][1]}" for k in AP}            # "X-sahagatena cetasā"ti
DIRS = ("или восточную сторону света, или западную сторону света, или северную сторону света, или южную сторону "
        "света, или вверх, или вниз, или в стороны, или промежуточную сторону света")
LIKEWISE = ("как одну сторону света, так же вторую сторону света, так же третью сторону света, так же четвёртую "
            "сторону света, так же вверх, так же вниз, так же в стороны, так же промежуточную сторону света")
ALL_WAYS = "всецело, всё во всех отношениях, без остатка, полностью"     # sabbena sabbaṃ sabbathā sabbaṃ asesaṃ nissesaṃ
VIPULA = ("что обширно, то возвышенно, что возвышенно, то безмерно, что безмерно, то свободно от вражды, что свободно "
          "от вражды, то свободно от неприязни")
TOP13 = {
    "ekaṃ disa": "Одну сторону света", "pharitvā": "Наполнив", "tathā dutiya": "Так же вторую",
    "sabbadhi sabbattatāya sabbāvantaṃ loka": "Повсюду, ко всем как к себе, весь мир", "vipulenā": "Обширным",
}
TOP13.update({low(f"{k}sahagatena cetasā"): TOPIC_SAHA[k] for k in AP})
SENT13 = {
    ("Puratthimaṃ vā disaṃ pacchimaṃ vā disaṃ uttaraṃ vā disaṃ dakkhiṇaṃ vā disaṃ uddhaṃ vā adho vā tiriyaṃ vā "
     "vidisaṃ vā."): cap(DIRS) + ".",
    "Pharitvā adhimuccitvā.": "Наполнив, утвердившись в решимости.",
    ("Yatheva ekaṃ disaṃ tathā dutiyaṃ disaṃ tathā tatiyaṃ disaṃ tathā catutthaṃ disaṃ tathā uddhaṃ tathā adho tathā "
     "tiriyaṃ tathā vidisaṃ."): cap(LIKEWISE) + ".",
    "Sabbena sabbaṃ sabbathā sabbaṃ asesaṃ nissesaṃ.": cap(ALL_WAYS) + ".",
    'Pariyādāyavacanametaṃ – "sabbadhi sabbattatāya sabbāvantaṃ loka"nti.':
        f"Это выражение, охватывающее всё, – «{TOP13['sabbadhi sabbattatāya sabbāvantaṃ loka']}».",
    "Yaṃ vipulaṃ taṃ mahaggataṃ, yaṃ mahaggataṃ taṃ appamāṇaṃ, yaṃ appamāṇaṃ so avero, yo avero so abyāpajjo.":
        cap(VIPULA) + ".",
    ("Yaṃ vipulaṃ taṃ mahaggataṃ, yaṃ mahaggataṃ taṃ appamāṇaṃ, yaṃ appamāṇaṃ so avero, yo avero so abyāpajjo "
     "[abyāpajjho (sī. syā.)]."): f"{cap(VIPULA)} {V_ABYAPAJJHO}.",
    "Tattha katamā karuṇā…pe… tattha katamā muditā…pe… tattha katamā upekkhā?":
        "Что такое здесь сострадание… что такое здесь сорадование… что такое здесь невозмутимость?",
}
for _k in AP:
    _ins = AP_RU[_k][1]
    _q = f"Как же монах {ap_one(_k).split(', так же')[0]}?"
    SENT13[(f"Kathañca bhikkhu {_k}sahagatena cetasā ekaṃ disaṃ pharitvā viharati? {SIMILE_P[_k]}, evameva sabbe "
            f"satte {_k}ya pharati.")] = f"{_q} {SIMILE[_k]}, точно так же он наполняет {_ins} всех существ."
for _k in AP:   # «Этот ум сопровождается этой доброжелательностью / этим состраданием, рождён вместе с ней / с ним …»
    _this = "этой" if AP_RU[_k][3] == "с ней" else "этим"
    SENT13[f"Idaṃ cittaṃ imāya {_k}ya sahagataṃ hoti sahajātaṃ saṃsaṭṭhaṃ sampayuttaṃ."] = \
        (f"Этот ум сопровождается {_this} {AP_RU[_k][1]}, рождён вместе {AP_RU[_k][3]}, соединён {AP_RU[_k][3]}, "
         f"связан {AP_RU[_k][3]}.")
LISTS13 = {}
for _k in AP:
    LISTS13[AP_LIST_P[_k]] = AP_LIST_RU[_k]
    LISTS13[f"sattesu {AP_LIST_P[_k]}"] = AP_LIST_BEINGS_RU[_k]
LISTS13[("cittaṃ mano mānasaṃ hadayaṃ paṇḍaraṃ mano manāyatanaṃ manindriyaṃ viññāṇaṃ viññāṇakkhandho "
         "tajjāmanoviññāṇadhātu")] = CITTA_FULL
J_BODY13 = {
    ("vitakkavicārānaṃ vūpasamā…pe… dutiyaṃ jhānaṃ…pe… tatiyaṃ jhānaṃ…pe… paṭhamaṃ jhānaṃ…pe… dutiyaṃ jhānaṃ…pe… "
     "tatiyaṃ jhānaṃ…pe… catutthaṃ jhānaṃ upasampajja viharati"):
        (" ", "с затиханием направленной мысли и удержания мысли… второе медитативное погружение… третье "
              "медитативное погружение… первое медитативное погружение… второе медитативное погружение… третье "
              "медитативное погружение… входит в четвёртое медитативное погружение"),
    "sukhassa ca pahānā dukkhassa ca pahānā…pe… catutthaṃ jhānaṃ upasampajja viharati":
        (" ", "с устранением приятного и с устранением болезненного… входит в четвёртое медитативное погружение"),
}
J_FIELD13 = {f"{k}sahagataṃ": f", сопровождаемое {AP_RU[k][1]}, и пребывает в нём" for k in AP}   # pi-1 ^1-251 …


def install13():
    K10.TOP.update(TOP13)
    for k in AP:
        K10.NOM[k], K10.INS[k] = AP_RU[k][0], AP_RU[k][1]
        K10.SAMP_INS[f"{k}ya"] = AP_RU[k][1]
    K10.SENT.update(SENT13)
    K10.LISTS.update(LISTS13)
    K10.J_BODY.update(J_BODY13)
    K10.J_FIELD.update(J_FIELD13)
    fields = sorted([k for k in K10.J_FIELD if k], key=len, reverse=True)
    K10.J_RX = ("(" + "|".join(re.escape(k) for k in sorted(K10.J_BODY, key=len, reverse=True)) + ")(?: ("
                + "|".join(re.escape(f) for f in fields) + "))?")
    K10.SENT_SLIP["muditāyatanā"] = ("muditāyanā", "^2-688 «muditāyatanā» (for muditāyanā, as in every parallel): "
                                                   "rendered as meant «проявление сорадования»")


# =========================================================================== chapter 14: the training rules
PRECEPT = {   # X-ā (ablative) -> «от X(gen)»
    "pāṇātipātā": "убийства живых существ",
    "adinnādānā": "взятия того, что не дано",
    "kāmesumicchācārā": "неправильного поведения в чувственных удовольствиях",
    "musāvādā": "лжи",
    "surāmerayamajjapamādaṭṭhānā": "употребления спиртного, браги и опьяняющих напитков, ведущего к беспечности",
}
PRECEPT_ORDER = list(PRECEPT)
RULE = "правило обучения о воздержании от {x}"         # X veramaṇī sikkhāpadaṃ (termbase; coordinator: «воздержание»)
RULE_INS = "правилом обучения о воздержании от {x}"
FIVE_RULES = "Пять правил обучения"                     # Pañca sikkhāpadāni
FIVE_RULES_LIST = f"{FIVE_RULES} – " + nlist([RULE.format(x=PRECEPT[k]) for k in PRECEPT_ORDER]) + "."
ABSTAINER = "у того, кто воздерживается от {x}"        # X-ā viramantassa
HINA = {"hīnaṃ": "низший", "majjhimaṃ": "средний", "paṇītaṃ": "высший",
        "chandādhipateyyaṃ": "с преобладанием желания", "vīriyādhipateyyaṃ": "с преобладанием усердия",
        "cittādhipateyyaṃ": "с преобладанием ума", "vīmaṃsādhipateyyaṃ": "с преобладанием пытливости"}   # pi-1 ^1-269
SIKKHA_Q = "Что такое явления, являющиеся обучением?"     # Katame dhammā sikkhā?
SIKKHA_END = "Это явления, являющиеся обучением."        # Ime dhammā sikkhā.
SAMP14 = {"veramaṇiyā": "уклонением", "cetanāya": "намерением"}   # Avasesā dhammā X sampayuttā


def hina_chain(t):
    """hīnaṃ… majjhimaṃ… paṇītaṃ… chandādhipateyyaṃ… … (pi-1 ^1-269 shape)"""
    toks = [x.strip() for x in t.split("…")]
    out = []
    for tok in toks:
        words = tok.split(" ")
        out.append(", ".join(HINA[w] for w in words))
    return "… ".join(out)


def quals14(body):
    """«kāmāvacaraṃ kusalaṃ cittaṃ uppannaṃ hoti …[ hīnaṃ… …]» -> «возникает благой ум, …»"""
    if "kāmāvacare kusalaṃ" in body:
        slip("^2-711 «kāmāvacare kusalaṃ cittaṃ» (locative for kāmāvacaraṃ): rendered as meant")
        body = body.replace("kāmāvacare kusalaṃ", "kāmāvacaraṃ kusalaṃ")
    body = body.replace("majjhimaṃ …", "majjhimaṃ…").replace("vīriyādhipateyyaṃ …", "vīriyādhipateyyaṃ…")
    i = body.find(" hīnaṃ…")
    if i < 0:
        return K6.quals(body)
    head, chain = body[:i], body[i + 1:]
    if "majjhimaṃ paṇītaṃ" in chain:
        slip("^2-711 «cittādhipateyyaṃ hīnaṃ… majjhimaṃ paṇītaṃ»: «…» missing between majjhimaṃ and paṇītaṃ "
             "(written with a comma)")
    return f"{K6.quals(head)}, {hina_chain(chain)}"


def called_rule(raw):
    m = re.match(r'^"(\S+) veramaṇī sikkhāpadaṃ"$', raw)
    return f"это называется «{RULE_INS.format(x=PRECEPT[m.group(1)])}»"


def tail14(t, x):
    """the part after «… viramantassa[,] »"""
    t = t.replace(" …pe…", "…pe…")
    out = []
    for s in K45.split_sents(t):
        m = re.match(r'^yā tasmiṃ samaye (\S+) ārati virati paṭivirati veramaṇī akiriyā akaraṇaṃ anajjhāpatti '
                     r'velāanatikkamo setughāto – idaṃ vuccati (".+")\.$', s)
        if m:
            assert m.group(1) == x, s
            out.append(f"{WHAT_AT_TIME} отстранение от {PRECEPT[x]}, {ABSTAIN_TAIL}, – {called_rule(m.group(2))}.")
            continue
        m = re.match(r'^yā tasmiṃ samaye cetanā sañcetanā sañcetayitattaṃ – idaṃ vuccati (".+")\.$', s)
        if m:
            out.append(f"{WHAT_AT_TIME} {CETANA3}, – {called_rule(m.group(1))}.")
            continue
        m = re.match(r'^yo tasmiṃ samaye phasso…pe… paggāho avikkhepo – idaṃ vuccati (".+")\.$', s)
        if m:
            out.append(f"{WHAT_AT_TIME} {PHASSA_PAGGAHA}, – {called_rule(m.group(1))}.")
            continue
        m = re.match(r'^phasso…pe… paggāho avikkhepo – idaṃ vuccati (".+")\.$', s)
        if m:
            slip("^2-705 «… viramantassa phasso…pe… paggāho avikkhepo – idaṃ vuccati …»: «yo tasmiṃ samaye» (and "
                 "the comma) missing, as against ^2-704 and ^2-707; translated as written («…, контакт… – это "
                 "называется …»)")
            out.append(f"{PHASSA_PAGGAHA} – {called_rule(m.group(1))}.")
            continue
        m = re.match(r'^Avasesā dhammā (\S+) sampayuttā(?:…pe… avasesā dhammā (\S+) sampayuttā…pe… phasso…pe… '
                     r'paggāho avikkhepo – idaṃ vuccati (".+"))?\.$', s)
        if m:
            r = f"Остальные явления связаны с {SAMP14[m.group(1)]}"
            if m.group(2):
                r += (f"… остальные явления связаны с {SAMP14[m.group(2)]}… {PHASSA_PAGGAHA} – "
                      f"{called_rule(m.group(3))}")
            out.append(r + ".")
            continue
        raise KeyError(s)
    return " ".join(out)


def line14(ln):
    if ln.startswith("Pañca sikkhāpadāni – "):
        assert ln == ("Pañca sikkhāpadāni – " + ", ".join(f"{k} veramaṇī sikkhāpadaṃ" for k in PRECEPT_ORDER) + "."), ln
        return FIVE_RULES_LIST
    m = re.match(r"^Tattha katamaṃ (.+?)([?,]) [Yy]asmiṃ samaye (.+?) (\S+) viramantassa(,?) (.*)$", ln)
    if m:
        names, mark, body, x, comma, tail = m.groups()
        keys = re.findall(r"(\S+) veramaṇī sikkhāpadaṃ", names)
        assert names == "…pe… ".join(f"{k} veramaṇī sikkhāpadaṃ" for k in keys), names
        if mark == ",":
            slip("^2-706 «Tattha katamaṃ surāmerayamajjapamādaṭṭhānā veramaṇī sikkhāpadaṃ, yasmiṃ samaye …»: comma "
                 "for the question mark (rendered as a question)")
        q = "Что такое здесь " + "… ".join(RULE.format(x=PRECEPT[k]) for k in keys) + "?"
        head = f"{WHEN} {ABSTAINER.format(x=PRECEPT[x])}, {quals14(body)}"
        if not comma:
            return f"{q} {head}, {tail14(tail, x)}"
        return f"{q} {head}, {tail14(tail, x)}"
    m = re.match(r"^Katame dhammā sikkhā\? Yasmiṃ samaye (.*), tasmiṃ samaye phasso hoti…pe… avikkhepo hoti\. "
                 r"Ime dhammā sikkhā\.$", ln)
    if m:
        body = m.group(1)
        if body.startswith("rūpūpapattiyā maggaṃ bhāveti…pe… arūpūpapattiyā"):
            assert body == (f"rūpūpapattiyā maggaṃ bhāveti…pe… arūpūpapattiyā maggaṃ bhāveti…pe… {K6.P_SUPRA} "
                            f"{K6.P_J1} dukkhapaṭipadaṃ dandhābhiññaṃ"), body
            ru = (f"кто-либо развивает путь к рождению в мире форм… развивает путь к рождению в мире без форм… "
                  f"развивает {K6.SUPRA}{K6.J1_SUPRA.format(s='')}")
        else:
            ru = quals14(body)
        return f"{SIKKHA_Q} {WHEN} {ru}, {AT_TIME} {CONTACT_PE}. {SIKKHA_END}"
    raise KeyError(ln)


# =========================================================================== chapter 15: the analytical knowledges
PS = {"attha": ("аналитическое знание смысла", "аналитическим знанием смысла"),
      "dhamma": ("аналитическое знание явлений", "аналитическим знанием явлений"),
      "nirutti": ("аналитическое знание выражений", "аналитическим знанием выражений"),
      "paṭibhāna": ("аналитическое знание находчивости", "аналитическим знанием находчивости")}
FOUR_PS = "Четыре аналитических знания"                    # Catasso paṭisambhidā
THREE_PS = "Три аналитических знания"                      # Tisso paṭisambhidā
FOUR_PS_LIST = f"{FOUR_PS} – " + nlist([PS[k][0] for k in ("attha", "dhamma", "nirutti", "paṭibhāna")]) + "."
THREE_PS_LIST = f"{THREE_PS} – " + nlist([PS[k][0] for k in ("attha", "nirutti", "paṭibhāna")]) + "."
V_PATIBHANA = "[вариант написания (Syā.): paṭibhāṇapaṭisambhidā, так же и далее]"   # [paṭibhāṇa… (syā.) evamuparipi]


def is_ps(k):
    return f"является {PS[k][1]}"


NIRUTTI_CL = f"при этом знание высказывания выражений, относящихся к явлениям, {is_ps('nirutti')}"
NANESU_CL = f"знание о знаниях {is_ps('paṭibhāna')}"         # ñāṇesu ñāṇaṃ paṭibhānapaṭisambhidā
YAYA = "каким выражением обозначаются эти явления"         # yāya niruttiyā tesaṃ dhammānaṃ paññatti hoti
YENA = ("Знание, которым он знает эти знания – «Эти знания проясняют этот смысл», это знание о знаниях "
        f"{is_ps('paṭibhāna')}.")
KNOW = {   # X-e ñāṇaṃ = знание X(gen)
    "dukkha": "страдания", "dukkhasamudaya": "возникновения страдания", "dukkhanirodha": "прекращения страдания",
    "dukkhanirodhagāminiyā paṭipadāya": "способа практики, ведущего к прекращению страдания",
    "jarāmaraṇa": "старения и смерти", "jarāmaraṇasamudaya": "возникновения старения и смерти",
    "jarāmaraṇanirodha": "прекращения старения и смерти",
    "jarāmaraṇanirodhagāminiyā paṭipadāya": "способа практики, ведущего к прекращению старения и смерти",
    "jāti": "рождения", "bhava": "существования", "upādāna": "цепляния", "taṇhā": "жажды", "vedanā": "чувства",
    "phassa": "контакта", "saḷāyatana": "шести сфер восприятия", "nāmarūpa": "умственного и материальной формы",
    "viññāṇa": "сознания", "saṅkhāra": "формирующих факторов", "saṅkhārasamudaya": "возникновения формирующих факторов",
    "saṅkhāranirodha": "прекращения формирующих факторов",
    "saṅkhāranirodhagāminiyā paṭipadāya": "способа практики, ведущего к прекращению формирующих факторов",
    "hetu": "причины", "hetuphala": "плода причины", "attha": "смысла", "dhamma": "явлений",
}
BORN = "рождены, стали, зародились, появились, полностью появились, проявились"   # jātā bhūtā sañjātā nibbattā …
VARA = {"saṅgahavāro": "раздел обобщения", "saccavāro": "раздел об истинах", "hetuvāro": "раздел о причине",
        "dhammavāro": "раздел о явлениях", "paṭiccasamuppādavāro": "раздел о возникновении в зависимости от условий",
        "pariyattivāro": "раздел об изучении Учения"}
SUBHEAD15 = {"Saṅgahavāro": "Раздел обобщения", "Saccavāro": "Раздел об истинах", "Hetuvāro": "Раздел о причине",
             "Dhammavāro": "Раздел о явлениях",
             "Paṭiccasamuppādavāro": "Раздел о возникновении в зависимости от условий",
             "Pariyattivāro": "Раздел об изучении Учения", "Kusalavāro": "Раздел о благом",
             "Akusalavāro": "Раздел о неблагом", "Vipākavāro": "Раздел о результатах действий",
             "Kiriyavāro": "Раздел о функциональном"}
SUBHEAD13 = {"Mettā": "Доброжелательность", "Karuṇā": "Сострадание", "Muditā": "Сорадование",
             "Upekkhā": "Невозмутимость"}
SCRIPTURE = ("беседы, прозу со стихами, разъяснения, строфы, вдохновенные изречения, изречения «Так было сказано», "
             "истории о прошлых рождениях, рассказы о чудесном, вопросы и ответы")   # suttaṃ geyyaṃ … vedallaṃ
FACT = {"phasso": "контакт", "vedanā": "чувство", "saññā": "восприятие", "cetanā": "намерение", "cittaṃ": "ум",
        "upekkhā": "невозмутимость", "dukkhaṃ": "боль", "vitakko": "направленная мысль", "vicāro": "удержание мысли",
        "pīti": "восторг", "cittassekaggatā": "однонаправленность ума", "manindriyaṃ": "способность ума",
        "upekkhindriyaṃ": "способность невозмутимости", "sukhindriyaṃ": "способность удовольствия",
        "dukkhindriyaṃ": "способность боли", "somanassindriyaṃ": "способность радости",
        "jīvitindriyaṃ": "жизненная способность", "vīriyindriyaṃ": "способность усердия",
        "samādhindriyaṃ": "способность сосредоточения"}          # pi-1 ^1-431 / ^1-443 / ^1-469 / ^1-568
OTHER_ARUPA = ("или же какие бы другие нематериальные явления, возникшие в зависимости от условий, ни были в это "
               "время")                                        # ye vā pana tasmiṃ samaye aññepi atthi … (pi-1)
OTHER_P = "ye vā pana tasmiṃ samaye aññepi atthi paṭiccasamuppannā arūpino dhammā"
TASSEVA15 = dict(K6.TASSEVA)
TASSEVA15[f"Tasseva lokuttarassa kusalassa kammassa katattā bhāvitattā vipākaṃ {K6.P_J1} dukkhapaṭipadaṃ "
          "dandhābhiññaṃ suññataṃ"] = ("Вследствие того же совершённого и развитого надмирского благого действия, "
                                       "в качестве его результата, когда кто-либо, "
                                       f"{K6.J1_SUPRA.format(s='пустое, ')}")
P_745 = ("manoviññāṇadhātu uppannā hoti kiriyā neva kusalā nākusalā na ca kammavipākā somanassasahagatā "
         "ñāṇasampayuttā…pe… somanassasahagatā ñāṇasampayuttā sasaṅkhārena…pe… somanassasahagatā ñāṇavippayuttā…pe… "
         "somanassasahagatā ñāṇavippayuttā sasaṅkhārena…pe… upekkhāsahagatā ñāṇasampayuttā…pe… upekkhāsahagatā "
         "ñāṇasampayuttā sasaṅkhārena…pe… upekkhāsahagatā ñāṇavippayuttā…pe… upekkhāsahagatā ñāṇavippayuttā "
         "sasaṅkhārena")
P_745_REST = ("…pe… rūpāvacaraṃ jhānaṃ bhāveti…pe… arūpāvacaraṃ jhānaṃ bhāveti kiriyaṃ neva kusalaṃ nākusalaṃ na ca "
              f"kammavipākaṃ diṭṭhadhammasukhavihāraṃ…pe… {K6.P_J4}")
RU_745_REST = ("… кто-либо развивает медитативное погружение, относящееся к миру форм… развивает медитативное "
               "погружение, относящееся к миру без форм, "
               f"{K6.KIRIYA_JH[:-len(' и')]}… {K6.J4_ARUPA}")
SENT15 = {
    "Imesu dhammesu ñāṇaṃ dhammapaṭisambhidā.": f"Знание этих явлений {is_ps('dhamma')}.",
    "Imesu dhammesu ñāṇaṃ atthapaṭisambhidā.": f"Знание этих явлений {is_ps('attha')}.",
    "Tesaṃ vipāke ñāṇaṃ atthapaṭisambhidā.": f"Знание их результата {is_ps('attha')}.",
    ("Tesaṃ vipāke ñāṇaṃ atthapaṭisambhidā, yāya niruttiyā tesaṃ dhammānaṃ paññatti hoti, tatra dhammaniruttābhilāpe "
     "ñāṇaṃ niruttipaṭisambhidā."): f"Знание их результата {is_ps('attha')}, {YAYA}, {NIRUTTI_CL}.",
    "Yāya niruttiyā tesaṃ dhammānaṃ paññatti hoti tatra dhammaniruttābhilāpe ñāṇaṃ niruttipaṭisambhidā.":
        f"{cap(YAYA)}, {NIRUTTI_CL}.",
    ('Yena ñāṇena tāni ñāṇāni jānāti – "imāni ñāṇāni idamatthajotakānī"ti, ñāṇesu ñāṇaṃ '
     "paṭibhānapaṭisambhidā."): YENA,
    "Ime dhammā kusalā.": THESE["kusalā"], "Ime dhammā akusalā.": THESE["akusalā"],
    "Ime dhammā abyākatā.": THESE["abyākatā"],
    "Tisso paṭisambhidā – atthapaṭisambhidā, niruttipaṭisambhidā, paṭibhānapaṭisambhidā.": THREE_PS_LIST,
    "Catasso paṭisambhidā – atthapaṭisambhidā, dhammapaṭisambhidā, niruttipaṭisambhidā, paṭibhānapaṭisambhidā.":
        FOUR_PS_LIST,
    ("Tisso paṭisambhidā kāmāvacarakusalato catūsu ñāṇasampayuttesu cittuppādesu, kiriyato catūsu "
     "ñāṇasampayuttesu cittuppādesu uppajjanti."):
        ("Три аналитических знания возникают в четырёх связанных со знанием видах благого ума, относящегося к миру "
         "чувственных желаний, и в четырёх связанных со знанием видах функционального ума."),
    "Atthapaṭisambhidā etesu ceva uppajjati, catūsu maggesu catūsu phalesu ca uppajjati.":
        "Аналитическое знание смысла возникает и в них, и возникает в четырёх путях и в четырёх плодах.",
}


def know(keys):
    return [f"знание {KNOW[k]}" for k in keys]


def suttanta15(ln, sid):
    """the Suttantabhājanīya lines of ch. 15"""
    four_pe = ("Catasso paṭisambhidā – atthapaṭisambhidā, dhammapaṭisambhidā, niruttipaṭisambhidā, "
               "paṭibhānapaṭisambhidā")
    if ln == f"{four_pe}.":
        return FOUR_PS_LIST
    tail_cl = f"{NIRUTTI_CL}, {NANESU_CL}"
    if sid == "2-718":
        assert ln == (f"{four_pe} [paṭibhāṇapaṭisambhidā (syā.) evamuparipi]. Atthe ñāṇaṃ atthapaṭisambhidā, dhamme "
                      "ñāṇaṃ dhammapaṭisambhidā, tatra dhammaniruttābhilāpe ñāṇaṃ niruttipaṭisambhidā, ñāṇesu ñāṇaṃ "
                      "paṭibhānapaṭisambhidā. Ayaṃ saṅgahavāro."), ln
        return (f"{FOUR_PS_LIST[:-1]} {V_PATIBHANA}. {cap(know(['attha'])[0])} {is_ps('attha')}, "
                f"{know(['dhamma'])[0]} {is_ps('dhamma')}, {tail_cl}. Это {VARA['saṅgahavāro']}.")
    if sid in ("2-719", "2-722"):
        x = "dukkha" if sid == "2-719" else "jarāmaraṇa"
        end = f" Это {VARA['saccavāro']}." if sid == "2-719" else ""
        k4 = [x, f"{x}samudaya", f"{x}nirodha", f"{x}nirodhagāminiyā paṭipadāya"]
        kk = know(k4)
        return (f"{FOUR_PS_LIST} {cap(kk[0])} {is_ps('attha')}, {kk[1]} {is_ps('dhamma')}, {kk[2]} {is_ps('attha')}, "
                f"{kk[3]}, {is_ps('dhamma')}, {tail_cl}.{end}")
    if sid == "2-720":
        slip("^2-720 «atthapaṭisambhidā, dhammapaṭisambhidā niruttipaṭisambhidā»: comma missing in the list (the "
             "Russian list is the same as elsewhere)")
        return (f"{FOUR_PS_LIST} {cap(know(['hetu'])[0])} {is_ps('dhamma')}, {know(['hetuphala'])[0]} "
                f"{is_ps('attha')}, {tail_cl}. Это {VARA['hetuvāro']}.")
    if sid == "2-721":
        return (f"{FOUR_PS_LIST} Знание тех явлений, которые {BORN}, {is_ps('attha')}; знание тех явлений, из которых "
                f"эти явления {BORN}, {is_ps('dhamma')}; {NIRUTTI_CL}; {NANESU_CL}. Это {VARA['dhammavāro']}.")
    if sid == "2-723":
        pe = ["jāti", "bhava", "upādāna", "taṇhā", "vedanā", "phassa", "saḷāyatana", "nāmarūpa", "viññāṇa"]
        kk = know(pe)
        s4 = know(["saṅkhāra", "saṅkhārasamudaya", "saṅkhāranirodha", "saṅkhāranirodhagāminiyā paṭipadāya"])
        return (f"{FOUR_PS_LIST} {cap('… '.join(kk))}… {s4[0]} {is_ps('attha')}, {s4[1]} {is_ps('dhamma')}, {s4[2]} "
                f"{is_ps('attha')}, {s4[3]}, {is_ps('dhamma')}, {tail_cl}. Это {VARA['paṭiccasamuppādavāro']}.")
    if sid == "2-724":
        assert ln.startswith("Tattha katamā dhammapaṭisambhidā? Idha bhikkhu dhammaṃ jānāti – suttaṃ"), ln
        return (f"Что такое здесь {PS['dhamma'][0]}? Здесь монах знает Учение – {SCRIPTURE}. Это называется "
                f"«{PS['dhamma'][1]}». Он знает смысл того или иного сказанного – «Это смысл этого сказанного, это "
                f"смысл этого сказанного». Это называется «{PS['attha'][1]}». {cap(NIRUTTI_CL)}. {cap(NANESU_CL)}. "
                f"Это {VARA['pariyattivāro']}.")
    raise KeyError((sid, ln))


def factor_tail(t):
    """«phasso hoti, vedanā hoti, …, jīvitindriyaṃ hoti, ye vā pana …» -> «есть контакт, есть чувство, …; или же …»"""
    assert t.endswith(", " + OTHER_P), t
    items = t[:-len(", " + OTHER_P)].split(", ")
    happy = "удовольствие" if "sukhindriyaṃ hoti" in items else "счастье"
    out = []
    for it in items:
        w = it[:-len(" hoti")]
        assert it.endswith(" hoti"), it
        out.append("есть " + (happy if w == "sukhaṃ" else FACT[w]))
    return ", ".join(out) + f"; {OTHER_ARUPA}"


def tasmim(t):
    """«tasmiṃ samaye …» (no final full stop) -> Russian"""
    m = re.match(r"^tasmiṃ samaye (.*)$", t)
    assert m, t
    t = m.group(1)
    if t == "phasso hoti…pe… avikkhepo hoti":
        return f"{AT_TIME} {CONTACT_PE}"
    if t == "phasso hoti…pe… avikkhepo hoti, ime dhammā kusalā":
        return f"{AT_TIME} {CONTACT_PE}, {low(THESE['kusalā'][:-1])}"
    return f"{AT_TIME} {factor_tail(t)}"


def abhi15(ln):
    out = []
    for s in K45.split_sents(ln):
        if s in SENT15:
            out.append(SENT15[s])
            continue
        m = re.match(r"^Katame dhammā (kusalā|akusalā|abyākatā)\?$", s)
        if m:
            out.append(KIND_Q[m.group(1)])
            continue
        m = re.match(r"^Yasmiṃ samaye (.*?), (tasmiṃ samaye .*)\.$", s)
        if m:
            body, t = m.groups()
            if body == P_745 + P_745_REST:
                ru = K6.quals(P_745) + RU_745_REST
            elif body in K6.JHANA:
                ru = K6.JHANA[body]
            else:
                ru = K6.quals(body)
            out.append(f"{WHEN} {ru}, {tasmim(t)}.")
            continue
        m = re.match(r"^(Tasseva .*?), (tasmiṃ samaye .*)\.$", s)
        if m:
            if "lokuttarassa kusalassa kammassa katattā bhāvitattā" in s:
                slip("^2-740 «Tasseva lokuttarassa kusalassa kammassa katattā bhāvitattā vipākaṃ» (kammassa, where "
                     "ch. 6 and ch. 12 have jhānassa): translated as written «благого действия»")
            out.append(f"{TASSEVA15[m.group(1)]}, {tasmim(m.group(2))}.")
            continue
        raise KeyError(s)
    return " ".join(out)


# =========================================================================== Pañhāpucchaka (K23 / K10 engine)
GROUPS = dict(K10.GROUPS)
GROUPS.update({"Catunnaṃ appamaññānaṃ": "из четырёх безмерных состояний",
               "Pañcannaṃ sikkhāpadānaṃ": "из пяти правил обучения",
               "Catunnaṃ paṭisambhidānaṃ": "из четырёх аналитических знаний"})
SUBJ1315 = {   # Pāli subject -> (Russian nominative, number, gender, accusative)
    "Tisso appamaññāyo": ("Три безмерных состояния", "p", "p", "Три безмерных состояния"),
    "Mettā": ("Доброжелательность", "s", "f", "Доброжелательность"),
    "Upekkhā": ("Невозмутимость", "s", "f", "Невозмутимость"),
    "Tisso paṭisambhidā": ("Три аналитических знания", "p", "p", "Три аналитических знания"),
    "Dve paṭisambhidā": ("Два аналитических знания", "p", "p", "Два аналитических знания"),
    "Atthapaṭisambhidā": (cap(PS["attha"][0]), "s", "n", cap(PS["attha"][0])),
    "Niruttipaṭisambhidā": (cap(PS["nirutti"][0]), "s", "n", cap(PS["nirutti"][0])),
}
PANHA_FIX13 = [   # (bad, good, note)
    (" …pe…", "…pe…", None),
    ("na hetu sahetūkā", "na hetū sahetukā",
     "^2-717 «na hetu sahetūkā» (for na hetū sahetukā, plural subject): rendered as meant «не являются корнями, но "
     "имеют корни»"),
    ("na bhāvanāyapahātabbā", "na bhāvanāya pahātabbā",
     "^2-717 «na bhāvanāyapahātabbā» written as one word (= na bhāvanāya pahātabbā)"),
    ("nahetūahetukātipi", "na hetū ahetukātipi",
     "^2-750 «nahetūahetukātipi» written as one word (= na hetū ahetukātipi)"),
    ("Anidassanaapaṭighā.", "Anidassanaappaṭighā.",
     "^2-749 «Anidassanaapaṭighā» (apaṭighā for appaṭighā): rendered as meant «невидимыми и не способными к "
     "соударению»"),
    ("tisso appamaññāyo na upekkhāsahagatā, na kāmāvacarā", "tisso appamaññāyo na upekkhāsahagatā; @@ na kāmāvacarā",
     "^2-702 «Upekkhā upekkhāsahagatā, tisso appamaññāyo na upekkhāsahagatā, na kāmāvacarā, rūpāvacarā …»: the "
     "predicates of all four run on after the subject «tisso appamaññāyo»; a «;» is set before them in Russian "
     "(no subject added; as ch. 12 ^2-641)"),
    ("siyā lokuttarā, kenaci viññeyyā", "siyā lokuttarā; @@ kenaci viññeyyā",
     "^2-750 «… atthapaṭisambhidā siyā lokiyā, siyā lokuttarā, kenaci viññeyyā, kenaci na viññeyyā»: the "
     "predicates of all four run on after the subject «atthapaṭisambhidā»; a «;» is set before them in Russian "
     "(no subject added; as ch. 12 ^2-641)"),
]
V_ASAVA = "[вариант чтения (Sī.): āsavā; но в «Разборе элементов» разночтений нет]"
P_ASAVA = "[āsavā (sī.) dhātuvibhaṅge pana pāṭhanānattaṃ natthi]"
PANHA_SENT = {"Kusalāyeva.": "Являются только благими."}       # termbase kusalāyeva «только благой»


def subj_split():
    keys = list(K10.SUBJ1012) + list(SUBJ1315)
    return re.compile(r"(, |; )(?=(?:" + "|".join(low(k) for k in keys) + r"|@@) )")


def install():
    K10.install()
    install13()
    K23.SUBJ.update(SUBJ1315)
    K23.LOCAL["maggādhipatinī"] = K1.ITEMS["maggādhipati"]     # feminine singular (atthapaṭisambhidā), ^2-749
    K23.LOCAL["āsavavippayuttā sāsavā"] = K1.ITEMS["āsavavippayuttasāsavo"]      # ^2-750, two words, singular
    K23.LOCAL["āsavavippayuttā anāsavā"] = K1.ITEMS["āsavavippayuttaanāsavo"]
    K10.SUBJ_SPLIT = subj_split()


DASHED_NV = re.compile(r"([Nn]a vattabb(?:o|ā|aṃ)) – (\S+?)(tipi|ti)(?=$)")


def panha_clause(c):
    """one clause; keeps the dash after «нельзя определить» only where the Pāli has one («na vattabbā – X»)"""
    dashed = False
    toks = c.split(", ")
    for i, t in enumerate(toks):
        m = DASHED_NV.search(t)
        if m and '"' not in t:
            toks[i] = t[:m.start()] + f'{m.group(1)} – "{m.group(2)}"{m.group(3)}'
            dashed = True
    c = ", ".join(toks)
    r = K10.panha_clause(c)
    nv = K1.NV.split(" ", 1)[1]                                # «определить –»
    if not dashed:
        r = r.replace(f"{nv} ", nv[:-2] + " ")
    return r


def panha_sentence(s):
    if s in PANHA_SENT:
        return PANHA_SENT[s]
    body = s[:-1]
    body = re.sub(r'([Nn]a vattabb(?:o|ā|aṃ)) "', r'\1 – "', body)
    parts = K10.SUBJ_SPLIT.split(body)
    out = []
    for i in range(0, len(parts), 2):
        c = parts[i]
        sep = parts[i - 1] if i else ""
        if i:
            if not c.startswith("@@"):
                c = cap(c)
            r = panha_clause(c)
            out.append(sep + (r if c.startswith("@@") else low(r)))
        else:
            out.append(panha_clause(c))
    return "".join(out) + "."


def panha_line(p):
    for bad, good, note in PANHA_FIX13 + K10.PANHA_FIX + K79.PANHA_FIX79:
        if bad in p:
            p = p.replace(bad, good)
            if note:
                slip(note)
    var = P_ASAVA in p
    if var:
        p = p.replace(" " + P_ASAVA, "")
    sents = re.split(r"(?<=\.) (?=[A-ZĀĪŪṬḌṆÑ])", p)
    r = " ".join(panha_sentence(s) for s in sents)
    if var:
        a = "нельзя определить как «являющееся влечением и подверженное влечениям»"
        b = "иногда подвержено влечениям, но не является влечением,"
        assert r.count(a) == 1 and r.count(b) == 1, r
        r = r.replace(a, a.replace("влечением и", f"влечением {V_ASAVA} и"))
        r = r.replace(b, b[:-1] + f" {V_ASAVA},")
    return r


# =========================================================================== chapters
def heading(ln, ch):
    lvl, text = ln.split(" ", 1)
    T = {S.CH_TITLE[ch][0]: S.CH_TITLE[ch][1], "Suttantabhājanīyaṃ": S.SUTTANTA_BH, "Abhidhammabhājanīyaṃ": S.ABHI_BH,
         "Pañhāpucchakaṃ": S.PANHA, "Tikaṃ": S.TIKA_H, "Dukaṃ": S.DUKA_H}
    T.update(SUBHEAD13)
    T.update(SUBHEAD15)
    return f"{lvl} {T[text]}"


FIXED = {"Suttantabhājanīyaṃ.": f"{S.SUTTANTA_BH}.", "Abhidhammabhājanīyaṃ.": f"{S.ABHI_BH}.",
         "Pañhāpucchakaṃ.": f"{S.PANHA}.", "Catasso appamaññāyo – mettā, karuṇā, muditā, upekkhā.": FOUR_AP_LIST}
FIXED.update(DONE_LINES)


def line(ln, sid, ch, section):
    if ln in FIXED:
        return FIXED[ln]
    if section == "Pañhāpucchakaṃ":
        if ln.endswith("?"):
            return K1.panha_question(ln, GROUPS)
        if ln.startswith("Catasso appamaññāyo – idha bhikkhu"):
            return ap_699()
        if ln.startswith("Pañca sikkhāpadāni – "):
            return line14(ln)
        if ln in SENT15:
            return SENT15[ln]
        return panha_line(ln)
    if ch == 13:
        if ln.startswith("Catasso appamaññāyo – idha bhikkhu"):
            return ap_642()
        if "maggaṃ bhāveti pītiyā ca virāgā…pe… dutiyaṃ jhānaṃ" in ln:
            slip(f"^{sid} «pītiyā ca virāgā…pe… dutiyaṃ jhānaṃ» (the parallels ^2-684, ^2-688 have «vitakkavicārānaṃ "
                 "vūpasamā…pe… dutiyaṃ jhānaṃ»): translated as written «с угасанием восторга… входит во второе …»")
        return K10.line_ru(ln, sid)
    if ch == 14:
        return line14(ln)
    if section == "Suttantabhājanīyaṃ":
        return suttanta15(ln, sid)
    if ln in SENT15:
        return SENT15[ln]
    m = re.match(r"^(Tisso paṭisambhidā – atthapaṭisambhidā, niruttipaṭisambhidā, paṭibhānapaṭisambhidā\.) (.*)$", ln)
    if m:
        return f"{SENT15[m.group(1)]} {abhi15(m.group(2))}"
    return abhi15(ln)


def build(ch):
    pali = (S.PALI / PARTS[ch]).read_text(encoding="utf-8")
    h, section = {}, None
    for sid, lines in S.segs(pali):
        K10.SID["sid"] = sid
        lines = [re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", ln) for ln in lines]
        if lines[0].startswith("#"):
            assert len(lines) == 1
            text = lines[0].split(" ", 1)[1]
            if text in ("Suttantabhājanīyaṃ", "Abhidhammabhājanīyaṃ", "Pañhāpucchakaṃ"):
                section = text
            h[sid] = [heading(lines[0], ch)]
            continue
        h[sid] = [line(ln, sid, ch, section) for ln in lines]
    return pali, h


# =========================================================================== pi-1 / earlier-chapter checks
def check():
    K10.check()
    p1_431 = ("есть контакт, есть чувство, есть восприятие, есть намерение, есть ум, есть невозмутимость, есть "
              "однонаправленность ума, есть способность ума, есть способность невозмутимости, есть жизненная "
              f"способность; {OTHER_ARUPA}")
    K23.assert_pi1(p1_431, "есть ум, есть удовольствие, есть однонаправленность ума, есть способность ума, есть "
                   "способность удовольствия", "есть ум, есть боль, есть однонаправленность ума, есть способность ума, "
                   "есть способность боли", "есть восторг, есть счастье, есть однонаправленность ума, есть способность "
                   "ума, есть способность радости", "есть способность усердия, есть способность сосредоточения, есть "
                   "способность ума", "сопровождаемый радостью, связанный со знанием, низший… средний… высший… с "
                   "преобладанием желания… с преобладанием усердия… с преобладанием ума… с преобладанием пытливости… "
                   "с преобладанием желания, низший… средний… высший…",
                   ", сопровождаемое доброжелательностью, и пребывает в нём",
                   ", сопровождаемое состраданием, и пребывает в нём", ", сопровождаемое сорадованием, и пребывает в нём",
                   ", сопровождаемое невозмутимостью, и пребывает в нём",
                   "доброжелательность, проявление доброжелательности, состояние доброжелательности",
                   "возникает элемент умственного сознания, функциональный, ни благой, ни неблагой и не являющийся "
                   "результатом действий, сопровождаемый радостью")
    ch4 = "".join((S.OUT / f).read_text(encoding="utf-8") for f in ("4-saccavibhango.md",
                                                                      "6-paticcasamuppadavibhango.md"))
    for s in ("способа практики, ведущего к прекращению страдания", "возникновения страдания"):
        assert s in ch4, s
    ch11 = (S.OUT / "11-maggangavibhango.md").read_text(encoding="utf-8")
    assert f"отстранение от ложного образа жизни, {ABSTAIN_TAIL}" in ch11
    ch9 = (S.OUT / "9-iddhipadavibhango.md").read_text(encoding="utf-8")
    assert PHASSA_PAGGAHA in ch9
    ch12 = (S.OUT / "12-jhanavibhango.md").read_text(encoding="utf-8")
    assert low(K10.IRIYATI[:-1]) in ch12


# =========================================================================== notes
def notes_md():
    L = ["# pi-2 Russian rails: new formulas of chapters 13, 14 and 15 (^2-642 … ^2-750)", "",
         "Generated by build_rails_13_15_ru.py; import it instead of retyping. Strings already in ru-rails-formulas.md "
         "(sample) or notes-1 … notes-10-12 are not repeated.", "",
         "## Headings and closing labels", ""]
    L += [f"##### {p} = ##### {r}" for p, r in list(SUBHEAD13.items()) + list(SUBHEAD15.items())]
    L += [f"Ayaṃ {p}. = Это {r}." for p, r in VARA.items()]
    L += ["", "## Measureless states (ch. 13)", "",
          f"Catasso appamaññāyo – mettā, karuṇā, muditā, upekkhā. = {FOUR_AP_LIST}",
          f"Catunnaṃ appamaññānaṃ kati …? = Сколько {GROUPS['Catunnaṃ appamaññānaṃ']} являются …?",
          "X: " + "; ".join(f"{k} = {v[0]} (ins. {v[1]}, gen. {v[2]})" for k, v in AP_RU.items()),
          f"Xsahagatena cetasā ekaṃ disaṃ pharitvā viharati, tathā dutiyaṃ, tathā tatiyaṃ, tathā catutthaṃ = "
          f"{ap_one('mettā').replace('доброжелательностью', 'X(ins)')}",
          f"Iti uddhamadho tiriyaṃ sabbadhi sabbattatāya sabbāvantaṃ lokaṃ Xsahagatena cetasā vipulena mahaggatena "
          f"appamāṇena averena abyāpajjena pharitvā viharati = Так он "
          f"{ap_all('mettā').replace('доброжелательностью', 'X(ins)')}",
          "Kathañca bhikkhu Xsahagatena cetasā ekaṃ disaṃ pharitvā viharati? = Как же монах пребывает, наполнив одну "
          "сторону света умом, сопровождаемым X(ins)?",
          "Seyyathāpi nāma ekaṃ puggalaṃ … disvā …, evameva sabbe satte Xāya pharati. = " + " / ".join(
              f"{SIMILE[k]}" for k in AP) + ", точно так же он наполняет X(ins) всех существ.",
          "Yā sattesu X Xyanā Xyitattaṃ Xcetovimutti = То, что есть " + AP_LIST_BEINGS_RU["mettā"]
          + " (karuṇā: " + AP_LIST_BEINGS_RU["karuṇā"] + ")",
          "yā tasmiṃ samaye X Xyanā Xyitattaṃ Xcetovimutti = то, что в это время есть " + AP_LIST_RU["mettā"],
          "Idaṃ cittaṃ imāya Xya sahagataṃ hoti sahajātaṃ saṃsaṭṭhaṃ sampayuttaṃ. = "
          + SENT13["Idaṃ cittaṃ imāya mettāya sahagataṃ hoti sahajātaṃ saṃsaṭṭhaṃ sampayuttaṃ."]
          + " (n.: " + SENT13["Idaṃ cittaṃ imāya karuṇāya sahagataṃ hoti sahajātaṃ saṃsaṭṭhaṃ sampayuttaṃ."] + ")",
          f"Yaṃ cittaṃ mano mānasaṃ hadayaṃ … tajjāmanoviññāṇadhātu = То, что есть {CITTA_FULL}",
          "topics: " + "; ".join(f"{k} = {v}" for k, v in TOP13.items()),
          ]
    L += [f"{k} = {v}" for k, v in SENT13.items() if not k.startswith(("Kathañca", "Idaṃ cittaṃ"))]
    L += ["Avasesā dhammā Xya sampayuttā. = Остальные явления связаны с X(ins).",
          "jhāna fields: " + "; ".join(f"{k} = {v}" for k, v in J_FIELD13.items()),
          "jhāna clauses: " + "; ".join(f"{k} = {v[1]}" for k, v in J_BODY13.items()),
          "", "## Training rules (ch. 14)", "",
          f"Pañca sikkhāpadāni – … = {FIVE_RULES_LIST}",
          f"X veramaṇī sikkhāpadaṃ = {RULE.format(x='X(gen)')} (ins. {RULE_INS.format(x='X(gen)')}); X: "
          + "; ".join(f"{k} = {v}" for k, v in PRECEPT.items()),
          f"Yasmiṃ samaye … X viramantassa = {WHEN} {ABSTAINER.format(x='X(gen)')}, возникает …",
          f"yā tasmiṃ samaye X ārati virati paṭivirati veramaṇī akiriyā akaraṇaṃ anajjhāpatti velāanatikkamo setughāto "
          f"= {WHAT_AT_TIME} отстранение от X(gen), {ABSTAIN_TAIL}",
          f"yā tasmiṃ samaye cetanā sañcetanā sañcetayitattaṃ = {WHAT_AT_TIME} {CETANA3}",
          f"yo tasmiṃ samaye phasso…pe… paggāho avikkhepo = {WHAT_AT_TIME} {PHASSA_PAGGAHA}",
          "Avasesā dhammā veramaṇiyā / cetanāya sampayuttā. = Остальные явления связаны с уклонением / с намерением.",
          "hīnaṃ… majjhimaṃ… paṇītaṃ… chandādhipateyyaṃ… … = " + "; ".join(f"{k} = {v}" for k, v in HINA.items())
          + " (pi-1 ^1-269)",
          f"Katame dhammā sikkhā? = {SIKKHA_Q}  Ime dhammā sikkhā. = {SIKKHA_END}",
          f"Pañcannaṃ sikkhāpadānaṃ kati …? = Сколько {GROUPS['Pañcannaṃ sikkhāpadānaṃ']} являются …?",
          f"Kusalāyeva. = {PANHA_SENT['Kusalāyeva.']}",
          "", "## Analytical knowledges (ch. 15)", "",
          f"Catasso paṭisambhidā – … = {FOUR_PS_LIST}", f"Tisso paṭisambhidā – … = {THREE_PS_LIST}",
          "Xpaṭisambhidā = " + "; ".join(f"{k} = {v[0]} (ins. {v[1]})" for k, v in PS.items()),
          f"<X>e ñāṇaṃ Ypaṭisambhidā = знание X(gen) является Y(ins); X: " + "; ".join(
              f"{k} = {v}" for k, v in KNOW.items()),
          f"tatra dhammaniruttābhilāpe ñāṇaṃ niruttipaṭisambhidā = {NIRUTTI_CL}",
          f"ñāṇesu ñāṇaṃ paṭibhānapaṭisambhidā = {NANESU_CL}",
          f"Ye dhammā jātā bhūtā sañjātā nibbattā abhinibbattā pātubhūtā, imesu dhammesu ñāṇaṃ … = Знание тех "
          f"явлений, которые {BORN}, …; yamhā dhammā te dhammā jātā … = знание тех явлений, из которых эти явления "
          f"{BORN}, …",
          f"Idha bhikkhu dhammaṃ jānāti – suttaṃ … vedallaṃ. = Здесь монах знает Учение – {SCRIPTURE}.",
          "So tassa tasseva bhāsitassa atthaṃ jānāti – \"ayaṃ imassa bhāsitassa attho, …\"ti. = Он знает смысл того "
          "или иного сказанного – «Это смысл этого сказанного, это смысл этого сказанного».",
          ]
    L += [f"{k} = {v}" for k, v in SENT15.items()]
    L += [f"tasmiṃ samaye phasso hoti, vedanā hoti, … ye vā pana tasmiṃ samaye aññepi atthi paṭiccasamuppannā "
          f"arūpino dhammā = {AT_TIME} есть контакт, есть чувство, …; {OTHER_ARUPA} (pi-1 ^1-431; factors: "
          + "; ".join(f"{k} = {v}" for k, v in FACT.items()) + "; sukhaṃ = удовольствие beside sukhindriyaṃ, "
          "otherwise счастье)",
          "Tasseva lokuttarassa kusalassa kammassa katattā bhāvitattā vipākaṃ … = Вследствие того же совершённого и "
          "развитого надмирского благого действия, в качестве его результата, когда кто-либо, …",
          f"Catunnaṃ paṭisambhidānaṃ kati …? = Сколько {GROUPS['Catunnaṃ paṭisambhidānaṃ']} являются …?",
          "Pañhāpucchaka subjects: " + "; ".join(f"{k} = {v[0]}" for k, v in SUBJ1315.items()),
          "na vattabbā – Xtipi, Ytipi (dash, no quotes, ^2-749) = нельзя определить – ни как «X», ни как «Y» (the "
          "dash kept)",
          f"{P_ASAVA} = {V_ASAVA}",
          ]
    return "\n".join(L) + "\n"


def main():
    install()
    check()
    for ch in (13, 14, 15):
        pali, h = build(ch)
        (S.OUT / PARTS[ch]).write_text(K23.render(pali, h), encoding="utf-8", newline="\n")
        print(f"wrote {PARTS[ch]}: {len(S.segs(pali))} segments")
    NOTES_PATH.write_text(notes_md(), encoding="utf-8", newline="\n")
    for s in SLIPS + K10.SLIPS + K23.SLIPS + K1.SLIPS + K45.SLIPS + K79.SLIPS:
        print("slip:", s)


if __name__ == "__main__":
    main()
