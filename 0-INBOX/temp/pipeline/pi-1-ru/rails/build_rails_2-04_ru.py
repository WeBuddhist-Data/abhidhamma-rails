"""Builder for the Russian rails translation of pi-1 (Dhammasaṅgaṇī, plain audience), chapter 2-04
(the twelve unwholesome minds and the wholesome-resultant indeterminate minds, ^1-1-6-0 … ^1-504).

Writes (only when run as a script):
  AI_translation/russian/pi-1-russian-plain-rails_split_chapters/2-04-cittuppadakandam.md
  0-INBOX/temp/pipeline/pi-1-ru/rails/notes-2-04.md

Every line is translated from the Pāli by fixed strings. The earlier rails builders are imported, never
edited: build_rails_sample_ru.py (S), build_rails_2-03_ru.py (C) and, through C, its extended instance of
build_rails_2-01_2-02_ru.py (B = C.B). B's tables (NAMES, STR, ATTR_M, EXACT) are extended in memory with
the new 2-04 material below, so every passage 2-04 shares with 2-01/2-02/2-03 (definitions, synonym strings,
frames, counted names, the ṭhapetvā line, the «ye vā pana» tail, the jhāna sentences of the fine-material
and immaterial minds) comes out byte-identical. A check rebuilds 2-01, 2-02 and 2-03 in memory with the
extended tables and requires them to equal the finished files byte for byte.
Unknown Pāli raises KeyError, so nothing is guessed silently.
Terms follow the locked termbase AI_translation/russian/pi-1-pali-russian-termbase-plain.md.

usage: python -I -X utf8 build_rails_2-04_ru.py
"""
import importlib.util
import pathlib
import re
import sys

HERE = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-ru\rails")
sys.path.insert(0, str(HERE))
import build_rails_sample_ru as S  # noqa: E402  (importing writes nothing)

_spec = importlib.util.spec_from_file_location("build_rails_2_03_ru", HERE / "build_rails_2-03_ru.py")
C = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(C)        # importing writes nothing; C extends its own B in memory
B = C.B

PART = "2-04-cittuppadakandam.md"
PALI = S.PALI / PART
OUT = S.OUT / PART
TS = S.TS
cap = S.cap
PE, ELL = "…pe…", "…"

# =========================================================================================
# 1. Names (nominative)
# =========================================================================================
NEW_NAMES = {
    "micchādiṭṭhi": "ложное воззрение",
    "micchāsaṅkappo": "ложный помысел",
    "micchāvāyāmo": "ложное усилие",
    "micchāsamādhi": "ложное сосредоточение",
    "ahirikabalaṃ": "сила бессовестности",
    "anottappabalaṃ": "сила отсутствия страха перед дурным",
    "lobho": "жадность",
    "moho": "заблуждение",
    "abhijjhā": "алчность",
    "ahirikaṃ": "бессовестность",
    "anottappaṃ": "отсутствие страха перед дурным",
    "doso": "злоба",
    "byāpādo": "недоброжелательность",
    "dukkhaṃ": "боль",
    "domanassindriyaṃ": "способность уныния",
    "vicikicchā": "колебание",
    "uddhaccaṃ": "беспокойство",
    "sukhindriyaṃ": "способность удовольствия",
    # Koṭṭhāsavāra: counted groups
    "pañcindriyāni": "пять способностей",
    "cattāri indriyāni": "четыре способности",
    "tīṇindriyāni": "три способности",
    "cattāri balāni": "четыре силы",
    "tīṇi balāni": "три силы",
    "tivaṅgiko maggo": "трёхчастный путь",
    "duvaṅgiko maggo": "двухчастный путь",
    "eko hetu": "один корень",
    "ekā cakkhuviññāṇadhātu": "один элемент зрительного сознания",
    "ekā kāyaviññāṇadhātu": "один элемент осязательного сознания",
    "ekā manodhātu": "один элемент ума",
}
for _k in NEW_NAMES:
    assert _k not in B.NAMES, _k
B.NAMES.update(NEW_NAMES)

# sukhaṃ in the body-consciousness passage is defined as bodily (kāyikaṃ sukhaṃ): termbase sense «удовольствие»
SUKHA_BODILY = "удовольствие"
BODILY_SIDS = {f"1-{i}" for i in range(443, 455)}

# =========================================================================================
# 2. Synonym strings
# =========================================================================================


def _cut(s, tail):
    assert s.endswith(tail), (s, tail)
    return s[:-len(tail)]


S_VITAKKA_BARE = _cut(S.S_VITAKKA, ", правильный помысел")
S_SAMADHI_BARE = _cut(S.S_SAMADHI, ", правильное сосредоточение")
S_VIRIYA_BARE = _cut(S.S_VIRIYA, ", правильное усилие")
S_SAMADHI_SHORT = "устойчивость ума"
assert S.S_SAMADHI.startswith(S_SAMADHI_SHORT + ", ")

TAJJA_CAKKHU = S.TAJJA.replace("умственного сознания", "зрительного сознания")
TAJJA_KAYA = S.TAJJA.replace("умственного сознания", "осязательного сознания")
TAJJA_MANODH = S.TAJJA.replace("элемента умственного сознания", "элемента ума")
assert len({S.TAJJA, TAJJA_CAKKHU, TAJJA_KAYA, TAJJA_MANODH}) == 4
CITTA_END = "соответствующий элемент умственного сознания"
assert S.S_CITTA.endswith(CITTA_END)


def s_citta(new_end):
    return S.S_CITTA[:-len(CITTA_END)] + new_end


S_DIITHI_HEAD = ("воззрение, приверженность воззрениям, дебри воззрений, пустыня воззрений, извращённость воззрений, "
                 "метания воззрений, оковы воззрений, хватка, закрепление")
S_DIITHI_TAIL = ("убеждённость, искажение, кривая дорога, ложный путь, ложность, сфера сектантских учений, "
                 "превратная хватка")
S_DIITHI = S_DIITHI_HEAD + ", " + S_DIITHI_TAIL
S_DIITHI_VAR = (S_DIITHI_HEAD + " " + S.reading("Sī., Syā.", "paṭiggāho") + ", " + S_DIITHI_TAIL + " "
                + S.spell("Ka.", "vipariyesagāho"))
S_LOBHA = ("жадность, проявление жадности, состояние жадности, пристрастие, проявление страсти, состояние страсти, "
           "алчность, жадность как неблагой корень")
S_MOHA = ("незнание, отсутствие видения, отсутствие постижения, отсутствие понимания, непробуждённость, "
          "отсутствие проникновения, неохватывание, отсутствие углубления, отсутствие рассмотрения, "
          "отсутствие обдумывания, неспособность видеть воочию, тупость, глупость, отсутствие ясного понимания, "
          "заблуждение, сильное заблуждение, полное заблуждение, неведение, поток неведения, ярмо неведения, "
          "скрытая склонность к неведению, одержимость неведением, засов неведения, заблуждение как неблагой корень")
S_DUKKHA = ("душевная безотрадность, душевная боль, рождённое контактом ума безотрадное болезненное переживание, "
            "рождённое контактом ума безотрадное болезненное чувство")
S_DOSA = ("злоба, проявление злобы, состояние злобы, недоброжелательность, проявление недоброжелательности, "
          "состояние недоброжелательности, вражда, противодействие, свирепость, грубость, недовольство ума")
S_VICIKICCHA = ("сомнение, проявление сомнения, состояние сомнения, неуверенность, колебание, раздвоенность, "
                "распутье, нерешительность, неспособность прийти к определённости, блуждание, беспорядочное "
                "блуждание, отсутствие углубления, оцепенелость ума, терзание ума")
S_UDDHACCA = "беспокойство ума, отсутствие затихания, отвлечение ума, взбудораженность ума"
S_KAYA_SUKHA = ("телесная отрада, телесное удовольствие, рождённое контактом тела отрадное приятное переживание, "
                "рождённое контактом тела отрадное приятное чувство")

P_VITAKKA_BARE = "takko vitakko saṅkappo appanā byappanā cetaso abhiniropanā"
P_SAMADHI_BARE = ("cittassa ṭhiti saṇṭhiti avaṭṭhiti avisāhāro avikkhepo avisāhaṭamānasatā samatho "
                  "samādhindriyaṃ samādhibalaṃ")
P_VIRIYA_BARE = ("cetasiko vīriyārambho nikkamo parakkamo uyyāmo vāyāmo ussāho ussoḷhī thāmo dhiti "
                 "asithilaparakkamatā anikkhittachandatā anikkhittadhuratā dhurasampaggāho vīriyaṃ vīriyindriyaṃ "
                 "vīriyabalaṃ")
P_DIITHI_HEAD = ("diṭṭhi diṭṭhigataṃ diṭṭhigahanaṃ diṭṭhikantāro diṭṭhivisūkāyikaṃ diṭṭhivipphanditaṃ "
                 "diṭṭhisaṃyojanaṃ gāho patiṭṭhāho")
P_DIITHI_TAIL = "abhiniveso parāmāso kummaggo micchāpatho micchattaṃ titthāyatanaṃ vipariyāsaggāho"
P_DUKKHA = ("cetasikaṃ asātaṃ cetasikaṃ dukkhaṃ cetosamphassajaṃ asātaṃ dukkhaṃ vedayitaṃ cetosamphassajā "
            "asātā dukkhā vedanā")
P_KAYA_SUKHA = ("kāyikaṃ sātaṃ kāyikaṃ sukhaṃ kāyasamphassajaṃ sātaṃ sukhaṃ vedayitaṃ kāyasamphassajā sātā sukhā "
                "vedanā")
P_CITTA_HEAD = "cittaṃ mano mānasaṃ hadayaṃ paṇḍaraṃ mano manāyatanaṃ manindriyaṃ viññāṇaṃ viññāṇakkhandho "

NEW_STR = {
    P_VITAKKA_BARE: S_VITAKKA_BARE,
    P_VITAKKA_BARE + " micchāsaṅkappo": S_VITAKKA_BARE + ", " + NEW_NAMES["micchāsaṅkappo"],
    P_SAMADHI_BARE + " micchāsamādhi": S_SAMADHI_BARE + ", " + NEW_NAMES["micchāsamādhi"],
    P_VIRIYA_BARE + " micchāvāyāmo": S_VIRIYA_BARE + ", " + NEW_NAMES["micchāvāyāmo"],
    "cittassa ṭhiti": S_SAMADHI_SHORT,
    P_DIITHI_HEAD + " " + P_DIITHI_TAIL: S_DIITHI,
    P_DIITHI_HEAD + " [paṭiggāho (sī. syā.)] " + P_DIITHI_TAIL + " [vipariyesagāho (ka.)]": S_DIITHI_VAR,
    "lobho lubbhanā lubbhitattaṃ sārāgo sārajjanā sārajjitattaṃ abhijjhā lobho akusalamūlaṃ": S_LOBHA,
    ("aññāṇaṃ adassanaṃ anabhisamayo ananubodho asambodho appaṭivedho asaṃgāhanā apariyogāhanā asamapekkhanā "
     "apaccavekkhanā apaccakkhakammaṃ dummejjhaṃ bālyaṃ asampajaññaṃ moho pamoho sammoho avijjā avijjogho "
     "avijjāyogo avijjānusayo avijjāpariyuṭṭhānaṃ avijjālaṅgī moho akusalamūlaṃ"): S_MOHA,
    P_DUKKHA: S_DUKKHA,
    "tajjāmanoviññāṇadhātusamphassajaṃ " + P_DUKKHA: S.TAJJA.format("ая") + " " + S_DUKKHA,
    ("doso dussanā dussitattaṃ byāpatti byāpajjanā byāpajjitattaṃ virodho paṭivirodho caṇḍikkaṃ asuropo "
     "anattamanatā cittassa"): S_DOSA,
    ("kaṅkhā kaṅkhāyanā kaṅkhāyitattaṃ vimati vicikicchā dveḷhakaṃ dvedhāpatho saṃsayo anekaṃsaggāho āsappanā "
     "parisappanā apariyogāhanā thambhitattaṃ cittassa manovilekho"): S_VICIKICCHA,
    "cittassa uddhaccaṃ avūpasamo cetaso vikkhepo bhantattaṃ cittassa": S_UDDHACCA,
    # eye-consciousness (^1-433 has the mental feeling string, as written)
    "tajjācakkhuviññāṇadhātusamphassajaṃ " + B.P_UPEKKHA: TAJJA_CAKKHU.format("ое") + " " + B.S_UPEKKHA,
    "tajjācakkhuviññāṇadhātusamphassajā saññā sañjānanā sañjānitattaṃ":
        TAJJA_CAKKHU.format("ое") + " " + B.S_SANNA_PLAIN,
    "tajjācakkhuviññāṇadhātusamphassajā cetanā sañcetanā cetayitattaṃ":
        TAJJA_CAKKHU.format("ое") + " " + B.S_CETANA_PLAIN,
    P_CITTA_HEAD + "tajjācakkhuviññāṇadhātu": s_citta("соответствующий элемент зрительного сознания"),
    # body-consciousness
    "tajjākāyaviññāṇadhātusamphassajaṃ " + P_KAYA_SUKHA: TAJJA_KAYA.format("ая") + " " + S_KAYA_SUKHA,
    P_KAYA_SUKHA: S_KAYA_SUKHA,
    "tajjākāyaviññāṇadhātusamphassajā saññā sañjānanā sañjānitattaṃ":
        TAJJA_KAYA.format("ое") + " " + B.S_SANNA_PLAIN,
    "tajjākāyaviññāṇadhātusamphassajā cetanā sañcetanā cetayitattaṃ":
        TAJJA_KAYA.format("ое") + " " + B.S_CETANA_PLAIN,
    P_CITTA_HEAD + "tajjākāyaviññāṇadhātu": s_citta("соответствующий элемент осязательного сознания"),
    # mind element
    "tajjāmanodhātusamphassajaṃ " + B.P_UPEKKHA: TAJJA_MANODH.format("ое") + " " + B.S_UPEKKHA,
    "tajjāmanodhātusamphassajā saññā sañjānanā sañjānitattaṃ": TAJJA_MANODH.format("ое") + " " + B.S_SANNA_PLAIN,
    "tajjāmanodhātusamphassajā cetanā sañcetanā cetayitattaṃ":
        TAJJA_MANODH.format("ое") + " " + B.S_CETANA_PLAIN,
    P_CITTA_HEAD + "tajjāmanodhātu": s_citta("соответствующий элемент ума"),
}
assert P_CITTA_HEAD + "tajjāmanoviññāṇadhātu" in B.STR
for _k in NEW_STR:
    assert dict.get(B.STR, _k) is None, _k
B.STR.update(NEW_STR)

# definitions whose body is a clause, not «есть S» (negated hiri/ottappa)
BODIES = {
    "na hirīyati hiriyitabbena na hirīyati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā":
        f"То, что {TS} не стыдятся того, чего следует стыдиться, не стыдятся допускать в себе дурные неблагие явления",
    "na ottappati ottappitabbena na ottappati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā":
        f"То, что {TS} не боятся того, чего следует бояться, не боятся допускать в себе дурные неблагие явления",
}
assert S.HIRI_BODY.replace(" стыдятся", " не стыдятся") == BODIES[next(iter(BODIES))]
assert S.OTTAPPA_BODY.replace(" боятся", " не боятся") == list(BODIES.values())[1]

_orig_answer = B.answer_ru


def answer_ru(a):
    m = B.ARE.fullmatch(a)
    if m and m.group(1) in BODIES:
        return BODIES[m.group(1)] + ", – " + B.tail_ru(m.group(2))
    return _orig_answer(a)


B.answer_ru = answer_ru

# =========================================================================================
# 3. Tails: «ime dhammā akusalā / abyākatā», the indeterminate roots
# =========================================================================================
AKUSALA_NAME = S.TRIADS["1-M1-1"][1][1]       # неблагие явления
ABYAKATA_NAME = S.TRIADS["1-M1-1"][2][1]      # этически неопределённые явления
Q_AK = S.q_form(AKUSALA_NAME)
Q_ABY = S.q_form(ABYAKATA_NAME)
ABY_ROOT = "как этически неопределённый корень"
TAIL_EXTRA = [
    ("ime dhammā akusalā", S.a_form(AKUSALA_NAME)[:-1]),
    ("ime dhammā abyākatā", S.a_form(ABYAKATA_NAME)[:-1]),
    ("alobho abyākatamūlaṃ", f"{B.NAMES['alobho']} {ABY_ROOT}"),
    ("adoso abyākatamūlaṃ", f"{B.NAMES['adoso']} {ABY_ROOT}"),
]
_orig_tail = B.tail_ru


def tail_ru(t):
    for p, r in TAIL_EXTRA:
        t = t.replace(p, r)
    return _orig_tail(t)


B.tail_ru = tail_ru

# =========================================================================================
# 4. «Katame dhammā akusalā? Yasmiṃ samaye akusalaṃ cittaṃ uppannaṃ hoti …»
# =========================================================================================
AK_P = "Katame dhammā akusalā? Yasmiṃ samaye akusalaṃ cittaṃ uppannaṃ hoti "
AK_R = "В то время, когда возникает неблагой ум"
NEW_ATTR = {   # attributes of the unwholesome mind (masculine, agree with «ум»)
    "somanassasahagataṃ diṭṭhigatasampayuttaṃ": "сопровождаемый радостью, связанный с приверженностью воззрениям",
    "somanassasahagataṃ diṭṭhigatavippayuttaṃ": "сопровождаемый радостью, не связанный с приверженностью воззрениям",
    "upekkhāsahagataṃ diṭṭhigatasampayuttaṃ":
        "сопровождаемый невозмутимостью, связанный с приверженностью воззрениям",
    "upekkhāsahagataṃ diṭṭhigatavippayuttaṃ":
        "сопровождаемый невозмутимостью, не связанный с приверженностью воззрениям",
    "domanassasahagataṃ paṭighasampayuttaṃ": "сопровождаемый унынием, связанный с неприязнью",
    "upekkhāsahagataṃ vicikicchāsampayuttaṃ": "сопровождаемый невозмутимостью, связанный с колебанием",
    "upekkhāsahagataṃ uddhaccasampayuttaṃ": "сопровождаемый невозмутимостью, связанный с беспокойством",
    "yaṃ yaṃ vā panārabbha": "или что бы то ни было",
}
for _k in NEW_ATTR:
    assert _k not in B.ATTR_M, _k
B.ATTR_M.update(NEW_ATTR)
TAIL_RE = re.compile(r"(.*? hoti)(…pe… ime dhammā (?:akusalā|abyākatā).*|; ye vā pana.*)")


def split_at_samaye(body):
    idx = body.index(" tasmiṃ samaye ")
    x, rest = body[:idx].rstrip(), body[idx + len(" tasmiṃ samaye "):]
    assert x.endswith(","), x[-40:]
    return x[:-1], rest


def finish(rest):
    m = TAIL_RE.fullmatch(rest)
    return f", {TS} " + B.there_list(m.group(1)) + B.tail_ru(m.group(2))


def akusala_ru(line):
    x, rest = split_at_samaye(line[len(AK_P):])
    return Q_AK + " " + AK_R + ", " + B.x_kama(x) + finish(rest)


# =========================================================================================
# 5. Resultants of the sense sphere: «… kāmāvacarassa kusalassa kammassa katattā upacitattā vipākaṃ …»
# =========================================================================================
VK_P = "Katame dhammā abyākatā? Yasmiṃ samaye kāmāvacarassa kusalassa kammassa katattā upacitattā "
VK_R = ("В то время, когда вследствие совершённого и накопленного благого действия, относящегося к миру "
        "чувственных желаний,")
RES_N = "являющееся результатом"     # vipākaṃ (with сознание, neuter)
RES_M = "являющийся результатом"     # vipākā (with элемент, masculine)
OBJ_N = {"rūpa": "видимую форму", "sadda": "звук", "gandha": "запах", "rasa": "вкус", "phoṭṭhabba": "осязаемое",
         "dhamma": "объект ума"}
VIP = {
    "vipākaṃ cakkhuviññāṇaṃ uppannaṃ hoti": f"возникает зрительное сознание, {RES_N}",
    "vipākaṃ sotaviññāṇaṃ uppannaṃ hoti": f"возникает слуховое сознание, {RES_N}",
    "ghānaviññāṇaṃ uppannaṃ hoti": "возникает обонятельное сознание",
    "jivhāviññāṇaṃ uppannaṃ hoti": "возникает вкусовое сознание",
    "kāyaviññāṇaṃ uppannaṃ hoti": "возникает осязательное сознание",
    "upekkhāsahagataṃ": "сопровождаемое невозмутимостью",
    "sukhasahagataṃ": "сопровождаемое счастьем",
    "vipākā manodhātu uppannā hoti": f"возникает элемент ума, {RES_M}",
    "vipākā manoviññāṇadhātu uppannā hoti": f"возникает элемент умственного сознания, {RES_M}",
    "upekkhāsahagatā": "сопровождаемый невозмутимостью",
    "somanassasahagatā": "сопровождаемый радостью",
    "ñāṇasampayuttā": "связанный со знанием",
    "ñāṇavippayuttā": "не связанный со знанием",
    "sasaṅkhārena": B.ATTR_M["sasaṅkhārena"],
    "rūpārammaṇā vā": B.ATTR_M["rūpārammaṇaṃ vā"],
    "phoṭṭhabbārammaṇā vā yaṃ yaṃ vā panārabbha": f"или {OBJ_N['phoṭṭhabba']}, или что бы то ни было",
    "dhammārammaṇā vā yaṃ yaṃ vā panārabbha": B.ATTR_M["dhammārammaṇaṃ vā yaṃ yaṃ vā panārabbha"],
}
for _o in ("rūpa", "sadda", "gandha", "rasa", "phoṭṭhabba"):
    VIP[f"{_o[:-1]}ārammaṇaṃ"] = f"имеющее объектом {OBJ_N[_o]}"
assert B.ATTR_M["rūpārammaṇaṃ vā"] == "имеющий объектом " + OBJ_N["rūpa"]
assert B.ATTR_M["dhammārammaṇaṃ vā yaṃ yaṃ vā panārabbha"] == f"или {OBJ_N['dhamma']}, или что бы то ни было"
assert B.OBJ_FULL_R.startswith("имеющий объектом видимую форму, или звук, или запах, или вкус, или осязаемое, "
                               "или объект ума")


def x_vip(x):
    out = []
    for i, part in enumerate(re.split(r"(\s*…pe…\s*)", x)):
        if i % 2:
            out.append(ELL + " ")
        elif part.strip():
            res = []
            for key, v in B.match(B.words_of(part), VIP):
                assert not v
                res.append(VIP[key])
            out.append(", ".join(res))
    return "".join(out)


def vipaka_kama_ru(line):
    x, rest = split_at_samaye(line[len(VK_P):])
    return Q_ABY + " " + VK_R + " " + x_vip(x) + finish(rest)


# =========================================================================================
# 6. Resultants of the fine-material and immaterial spheres (two sentences on one line)
# =========================================================================================
VJ_P = "Katame dhammā abyākatā? Yasmiṃ samaye "
TASSEVA = {
    "rūpāvacarassa": ("Вследствие того же совершённого и накопленного благого действия, относящегося к миру форм, "
                      "в качестве его результата, когда кто-либо"),
    "arūpāvacarassa": ("Вследствие того же совершённого и накопленного благого действия, относящегося к миру без "
                       "форм, в качестве его результата, когда кто-либо"),
}
TASSEVA_RE = re.compile(r"(rūpāvacarassa|arūpāvacarassa) kusalassa kammassa katattā upacitattā vipākaṃ (.+?), "
                        r"tasmiṃ samaye (.*)")


def vipaka_jh_ru(line):
    a, b = line.split(" Tasseva ", 1)
    ra = B.kusala_ru("Katame dhammā kusalā? " + a[len("Katame dhammā abyākatā? "):])
    assert ra.startswith(S.Q_KUSALA + " ")
    ra = Q_ABY + ra[len(S.Q_KUSALA):]
    sphere, x, rest = TASSEVA_RE.fullmatch(b).groups()
    xr = B.x_jh(x)
    assert xr.startswith(" и"), xr[:20]
    return ra + " " + TASSEVA[sphere] + xr[2:] + finish(rest)


# =========================================================================================
# 7. Headings and closing lines
# =========================================================================================
RES_KUS = "являющийся результатом благих действий"
H = {
    "Kusalavipākapañcaviññāṇāni": "Пять видов сознания, являющихся результатом благих действий",
    "Kusalavipākamanodhātu": f"Элемент ума, {RES_KUS}",
    "Kusalavipākamanoviññāṇadhātusomanassasahagatā": f"Элемент умственного сознания, {RES_KUS}, "
                                                     "сопровождаемый радостью",
    "Kusalavipākamanoviññāṇadhātuupekkhāsahagatā": f"Элемент умственного сознания, {RES_KUS}, "
                                                   "сопровождаемый невозмутимостью",
    "Aṭṭhamahāvipākā": "Восемь великих результатов действий",
    "Rūpāvacaravipākā": "Результаты действий, относящиеся к миру форм",
    "Arūpāvacaravipākā": "Результаты действий, относящиеся к миру без форм",
}
CLOSE = {   # closing line Pāli -> heading key
    "Kusalavipākāni pañcaviññāṇāni.": "Kusalavipākapañcaviññāṇāni",
    "Kusalavipākā manodhātu.": "Kusalavipākamanodhātu",
    "Kusalavipākā manoviññāṇadhātu somanassasahagatā.": "Kusalavipākamanoviññāṇadhātusomanassasahagatā",
    "Kusalavipākā upekkhāsahagatā manoviññāṇadhātu.": "Kusalavipākamanoviññāṇadhātuupekkhāsahagatā",
    "Aṭṭhamahāvipākā.": "Aṭṭhamahāvipākā",
    "Rūpāvacaravipākā.": "Rūpāvacaravipākā",
    "Arūpāvacaravipākā.": "Arūpāvacaravipākā",
}
NEW_EXACT = {
    "#### Dvādasa akusalāni": "#### Двенадцать неблагих видов ума",
    "Dvādasa akusalacittāni.": "Двенадцать видов неблагого ума.",
    "#### Abyākatavipāko": "#### Этически неопределённый результат действий",
}
for _p, _r in H.items():
    NEW_EXACT[f"##### {_p}"] = f"##### {_r}"
for _p, _k in CLOSE.items():
    NEW_EXACT[_p] = H[_k] + "."
for _k in NEW_EXACT:
    assert _k not in B.EXACT, _k
B.EXACT.update(NEW_EXACT)


# =========================================================================================
# 8. Line dispatch, render, build
# =========================================================================================
def translate_line(line):
    line = line.replace(" " + PE, PE)          # stray space before «…pe…» (^1-429, ^1-498): dropped
    if line in B.EXACT:
        return B.EXACT[line]
    if line.startswith(AK_P):
        return akusala_ru(line)
    if line.startswith(VK_P):
        return vipaka_kama_ru(line)
    if line.startswith(VJ_P) and " Tasseva " in line:
        return vipaka_jh_ru(line)
    m = re.match(r"(Katam\S+ tasmiṃ samaye \S+ hoti)\. (Y[oāa]ṃ? tasmiṃ samaye )", line)
    if m:   # ^1-473: the question ends with «.» in the Pāli; kept as written
        r = C.translate_line(line.replace(m.group(1) + ". ", m.group(1) + "? ", 1))
        q = r.index(f" {TS}? ") + len(TS) + 1
        return r[:q] + "." + r[q + 1:]
    return C.translate_line(line)


def render(segs):
    blocks = []
    for sid, plines in segs:
        rlines = []
        if sid in BODILY_SIDS:
            B.NAMES["sukhaṃ"] = SUKHA_BODILY
        try:
            for p in plines:
                r = cap(translate_line(p))
                B.check_ru(r)
                assert len(p) - len(p.lstrip("#")) == len(r) - len(r.lstrip("#")), sid
                assert p.count("–") + p.count("—") == r.count("–"), ("dash", sid, p[:60], r[:60])
                assert p.count("…pe…") <= r.count("…"), ("pe", sid)
                assert p.endswith("?") == r.endswith("?"), ("question", sid)
                assert "  " not in r and " ," not in r and ",," not in r and "..." not in r, ("spacing", sid, r)
                assert " … " not in r and r.count("?") == p.count("?"), ("form", sid, r)
                rlines.append(r)
        finally:
            B.NAMES["sukhaṃ"] = S.FN["sukhaṃ"]
        rlines[-1] += f" ^{sid}"
        blocks.append("\n".join(rlines))
    return blocks


def check_earlier_unchanged():
    """The extended tables must leave 2-01, 2-02 and 2-03 exactly as finished."""
    for fn_name, fn in (("2-01-cittuppadakandam.md", B.build_2_01), ("2-02-cittuppadakandam.md", B.build_2_02),
                        ("2-03-cittuppadakandam.md", C.build)):
        text, _ = fn()
        assert text == (S.OUT / fn_name).read_bytes().decode("utf-8"), fn_name
    print("2-01, 2-02, 2-03: rebuilt in memory with the 2-04 tables, byte-identical to the finished files")


def build():
    segs = B.segments(PALI)
    return "\n\n".join(render(segs)) + "\n", len(segs)


def notes():
    L = ["# pi-1 Russian rails: new formulas of 2-04", "",
         "Generated by build_rails_2-04_ru.py from its fixed strings; import that file instead of retyping. "
         "Strings already in ru-rails-formulas.md, notes-2-01_2-02.md or notes-2-03.md are not repeated.", "",
         "## Frames", "",
         f"Katame dhammā akusalā? = {Q_AK}",
         f"Katame dhammā abyākatā? = {Q_ABY}",
         f"ime dhammā akusalā = {TAIL_EXTRA[0][1]}",
         f"ime dhammā abyākatā = {TAIL_EXTRA[1][1]}",
         f"…pe… alobho abyākatamūlaṃ…pe… adoso abyākatamūlaṃ…pe… = … {TAIL_EXTRA[2][1]}… {TAIL_EXTRA[3][1]}…",
         f"Yasmiṃ samaye akusalaṃ cittaṃ uppannaṃ hoti A, tasmiṃ samaye … = {AK_R}, A, {TS} …",
         f"Yasmiṃ samaye kāmāvacarassa kusalassa kammassa katattā upacitattā X, tasmiṃ samaye … = {VK_R} X, {TS} …",
         f"… ime dhammā kusalā. Tasseva rūpāvacarassa kusalassa kammassa katattā upacitattā vipākaṃ J, tasmiṃ "
         f"samaye … = … это благие явления. {TASSEVA['rūpāvacarassa']}[,] J, {TS} … (J as in the jhāna sentences, "
         "without the leading «и»)",
         f"… Tasseva arūpāvacarassa … = {TASSEVA['arūpāvacarassa']}[,] J, …",
         "Yā tasmiṃ samaye cittassa ṭhiti – (abbreviated string) = "
         f"То, что {TS} есть {S_SAMADHI_SHORT}, –",
         f"Katamaṃ … ahirikabalaṃ/ahirikaṃ hoti? Yaṃ tasmiṃ samaye na hirīyati … = {list(BODIES.values())[0]}, – …",
         f"Katamaṃ … anottappabalaṃ/anottappaṃ hoti? Yaṃ tasmiṃ samaye na ottappati … = "
         f"{list(BODIES.values())[1]}, – …",
         "Katamā tasmiṃ samaye cetanā hoti. Yā … (^1-473, «.» as written) = Что такое намерение в это время. То, что …",
         "«X hoti …pe…» with a space (^1-429, ^1-498) = «есть X…» (space dropped, as in 2-01)",
         f"sukhaṃ in the body-consciousness passage (^1-443, ^1-449, defined as kāyikaṃ sukhaṃ) = {SUKHA_BODILY}",
         "", "### Attributes of the unwholesome mind (masculine)", ""]
    for p, r in NEW_ATTR.items():
        L.append(f"{p} = {r}")
    L += ["", "### Pieces of the sense-sphere resultant sentences (сознание neuter, элемент masculine)", ""]
    for p, r in VIP.items():
        L.append(f"{p} = {r}")
    L += ["", "## Synonym strings", ""]
    for p, r in NEW_STR.items():
        L.append(f"{p} = {r}")
    L += ["", "## Names (nominative)", ""]
    for p, r in NEW_NAMES.items():
        L.append(f"{p} = {r}")
    L += ["", "## Headings and closing lines", ""]
    for p, r in NEW_EXACT.items():
        L.append(f"{p} = {r}")
    (HERE / "notes-2-04.md").write_text("\n".join(L) + "\n", encoding="utf-8", newline="\n")
    print("wrote", HERE / "notes-2-04.md")


def main():
    text, n = build()
    check_earlier_unchanged()
    OUT.write_text(text, encoding="utf-8", newline="\n")
    print("wrote", OUT, n, "segments")
    notes()


if __name__ == "__main__":
    main()
