"""Builder for the Russian rails translation of pi-2 (Vibhaṅga, plain audience), chapters 2 and 3
(Āyatanavibhaṅgo, Dhātuvibhaṅgo).

Writes (only when run as a script):
  AI_translation/russian/pi-2-russian-plain-rails_split_chapters/2-ayatanavibhango.md
  AI_translation/russian/pi-2-russian-plain-rails_split_chapters/3-dhatuvibhango.md
  0-INBOX/temp/pipeline/pi-2-ru/rails/notes-2-3.md   (new recurring formulas, Pāli = Russian)

Every Russian string comes from the fixed tables and functions below, so identical Pāli gives identical Russian.
Imported read-only: the approved sample builder (S) and the chapter-1 builder (K1: matrix items, chain(), abhi_line(),
panha_question(), fixed strings). The Pāli passages shared with the Dhammasaṅgaṇī take their Russian from the approved
pi-1 Russian rails (read from the pi-1 files by block ID, or asserted to occur there).

usage: python -I -X utf8 build_rails_2_3_ru.py
"""
import itertools
import pathlib
import re
import sys

RAILS = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-ru\rails")
sys.path.insert(0, str(RAILS))
import build_rails_sample_ru as S  # noqa: E402  (importing writes nothing)
import build_rails_1_ru as K1      # noqa: E402  (importing writes nothing)

NOTES_PATH = RAILS / "notes-2-3.md"
P1RU = S.PI1_RU
cap, low = S.cap, K1.low
SLIPS = []


def slip(msg):
    if msg not in SLIPS:
        SLIPS.append(msg)


# =========================================================================== pi-1 Russian (shared Dhammasaṅgaṇī passages)
_P1 = {}


def p1(fname, sid):
    if fname not in _P1:
        _P1[fname] = {k: v for k, v in S.segs((P1RU / fname).read_text(encoding="utf-8"))}
    return re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", _P1[fname][sid][0])


def p1_body(sid):
    """the answer of a pi-1 «Что такое материальная форма, являющаяся …? <body>, – это материальная форма …»"""
    t = p1("3-02-rupakandam.md", sid)
    body = t.split("? ", 1)[1]
    return body.rsplit(", – это материальная форма", 1)[0]


PI1_ALL = None


def assert_pi1(*strings):
    global PI1_ALL
    if PI1_ALL is None:
        PI1_ALL = "\n".join(p.read_text(encoding="utf-8") for p in sorted(P1RU.glob("*.md")))
    for s in strings:
        assert s in PI1_ALL, f"not in pi-1 Russian: {s}"


# =========================================================================== names
# sense bases (āyatana): name, instrumental (for «это называется …»)
AY = {
    "cakkhu": "сфера глаза", "sota": "сфера уха", "ghāna": "сфера носа", "jivhā": "сфера языка",
    "kāya": "сфера тела", "mana": "сфера ума", "rūpa": "сфера видимых форм", "sadda": "сфера звуков",
    "gandha": "сфера запахов", "rasa": "сфера вкусов", "phoṭṭhabba": "сфера осязаемого",
    "dhamma": "сфера объектов ума",
}
AY_ORDER_S = ["cakkhu", "rūpa", "sota", "sadda", "ghāna", "gandha", "jivhā", "rasa", "kāya", "phoṭṭhabba", "mana",
              "dhamma"]                       # Suttanta and Pañhāpucchaka order
AY_ORDER_A = ["cakkhu", "sota", "ghāna", "jivhā", "kāya", "mana", "rūpa", "sadda", "gandha", "rasa", "phoṭṭhabba",
              "dhamma"]                       # Abhidhamma order


def ins(name):
    """«сфера глаза» -> «сферой глаза»; «элемент глаза» -> «элементом глаза»"""
    if name == "необусловленный элемент":
        return "необусловленным элементом"
    w, rest = name.split(" ", 1)
    w = {"сфера": "сферой", "элемент": "элементом", "совокупность": "совокупностью"}[w]
    return f"{w} {rest}"


def nlist(items):
    """«a, b, c» -> «a, b и c» (noun-phrase lists, K1 rule)"""
    return ", ".join(items[:-1]) + " и " + items[-1]


# elements (dhātu)
DH = {
    "cakkhu": "элемент глаза", "rūpa": "элемент видимых форм", "cakkhuviññāṇa": "элемент зрительного сознания",
    "sota": "элемент уха", "sadda": "элемент звуков", "sotaviññāṇa": "элемент слухового сознания",
    "ghāna": "элемент носа", "gandha": "элемент запахов", "ghānaviññāṇa": "элемент обонятельного сознания",
    "jivhā": "элемент языка", "rasa": "элемент вкусов", "jivhāviññāṇa": "элемент вкусового сознания",
    "kāya": "элемент тела", "phoṭṭhabba": "элемент осязаемого", "kāyaviññāṇa": "элемент осязательного сознания",
    "mano": "элемент ума", "dhamma": "элемент объектов ума", "manoviññāṇa": "элемент умственного сознания",
    "pathavī": "элемент земли", "āpo": "элемент воды", "tejo": "элемент огня", "vāyo": "элемент ветра",
    "ākāsa": "элемент пространства", "viññāṇa": "элемент сознания",
    "sukha": "элемент удовольствия", "dukkha": "элемент боли", "somanassa": "элемент радости",
    "domanassa": "элемент уныния", "upekkhā": "элемент невозмутимости", "avijjā": "элемент неведения",
    "kāma": "элемент чувственных желаний", "byāpāda": "элемент недоброжелательности",
    "vihiṃsā": "элемент жестокости", "nekkhamma": "элемент отречения",
    "abyāpāda": "элемент отсутствия недоброжелательности", "avihiṃsā": "элемент отсутствия жестокости",
    "asaṅkhatā": "необусловленный элемент",
}
DH18 = ["cakkhu", "rūpa", "cakkhuviññāṇa", "sota", "sadda", "sotaviññāṇa", "ghāna", "gandha", "ghānaviññāṇa",
        "jivhā", "rasa", "jivhāviññāṇa", "kāya", "phoṭṭhabba", "kāyaviññāṇa", "mano", "dhamma", "manoviññāṇa"]


def q(name):
    return f"Что такое {S.TATTHA} {name}?"


def called_q(name):
    """Idaṃ / Ayaṃ vuccati "X". = Это называется «X(ins)»."""
    return f"это называется «{ins(name)}»."


# =========================================================================== chapter 2: Suttantabhājanīya
AY12_S = f"Двенадцать сфер восприятия – {nlist([AY[k] for k in AY_ORDER_S])}."      # Dvādasāyatanāni – … (Suttanta)
AY12_A = f"Двенадцать сфер восприятия – {nlist([AY[k] for k in AY_ORDER_A])}."      # (Abhidhamma order)
# Cakkhuṃ aniccaṃ dukkhaṃ anattā vipariṇāmadhammaṃ. (termbase: aniccaṃ «непостоянный», dukkhaṃ «страдание»,
# anattā «лишённый самости», vipariṇāmadhammaṃ «подверженный изменению»)
IMPERM = {"m": "непостоянен, является страданием, лишён самости и подвержен изменению",
          "n": "непостоянно, является страданием, лишено самости и подвержено изменению",
          "p": "непостоянны, являются страданием, лишены самости и подвержены изменению"}
IMPERM_ITEMS = [("Глаз", "m"), ("Видимые формы", "p"), ("Ухо", "n"), ("Звуки", "p"), ("Нос", "m"), ("Запахи", "p"),
                ("Язык", "m"), ("Вкусы", "p"), ("Тело", "n"), ("Осязаемое", "n"), ("Ум", "m"),
                ("Объекты ума", "p")]
IMPERM_LINE = " ".join(f"{n} {IMPERM[g]}." for n, g in IMPERM_ITEMS)

# =========================================================================== shared sense-base definitions (pi-1)
SENSE_P1 = {"cakkhu": "1-596", "sota": "1-600", "ghāna": "1-604", "jivhā": "1-608", "kāya": "1-612",
            "rūpa": "1-616", "sadda": "1-620", "gandha": "1-624", "rasa": "1-628", "phoṭṭhabba": "1-647"}
EYE_VAR_P1 = "[вариант написания (Sī., Syā.): cakkhuṃ]"
EYE_VAR = "[вариант написания (Sī., Syā., Ka.): cakkhuṃ; см. «Перечисление явлений», 596-599]"
# [cakkhuṃ (sī. syā. ka.) dha. sa. 596-599]: dha. sa. = Dhammasaṅgaṇī, pi-1 title «Перечисление явлений»


def sub1(text, old, new):
    assert text.count(old) == 1, (old, text[:80])
    return text.replace(old, new)


def ay_body(k):
    """pi-2 answer of «Tattha katamaṃ <X>āyatanaṃ?» (Suttanta wording = pi-1 with the pi-2 variants)"""
    b = p1_body(SENSE_P1[k])
    if k == "cakkhu":
        b = sub1(b, EYE_VAR_P1, EYE_VAR)
    elif k == "rūpa":
        b = sub1(b, "красное, белое", "красное [вариант чтения (Sī.): pītaṃ lohitaṃ], белое")
        b = sub1(b, " [вариант написания (Sī., Ka.): caturassaṃ]", "")
        b = sub1(b, "[вариант написания (Sī., Syā.): suriyamaṇḍalassa]",
                 "[вариант написания (Sī., Syā., Kaṃ.): suriyamaṇḍalassa]")
    elif k == "sadda":
        b = sub1(b, "звук малых барабанов,", "звук малых барабанов [вариант написания (Sī.): mutiṅgasaddho],")
    elif k == "rasa":
        b = sub1(b, "солёный, щелочной, кисловатый [вариант чтения (Sī.): lapilakaṃ],",
                 "солёный [вариант чтения (Sī.): lapilakaṃ; (Ka., Sī.): lampikaṃ], щелочной, кисловатый,")
    return b


def ay_segment(k):
    return f"{q(AY[k])} {ay_body(k)}. {cap(called_q(AY[k]))}"


def dh_pe(k):
    """Abhidhamma of ch. 3: the same definitions cut by …pe… («Yaṃ cakkhu … pasādo…pe… suñño gāmopeso»)"""
    if k == "phoṭṭhabba":
        return "Элемент земли… это элемент осязаемого"
    b = re.sub(r" \[вариант[^\]]*\]", "", p1_body(SENSE_P1[k]))
    if k in ("cakkhu", "sota", "ghāna", "jivhā", "kāya"):
        head = b.split("производной от четырёх великих элементов", 1)[0] + "производной от четырёх великих элементов"
        return f"{head}… это пустая деревня"
    if k == "rūpa":
        head = b.split("производными от четырёх великих элементов", 1)[0] + "производными от четырёх великих элементов"
        return f"{head}… это элемент видимых форм"
    head = b.split("невидимый и способный к соударению", 1)[0] + "невидимый и способный к соударению"
    return f"{head}… это {DH[k]}"


# =========================================================================== Abhidhammabhājanīya helpers
MANA = AY["mana"]


def mana_head(n):
    return f"{cap(MANA)} {K1.NUMW[n]} –"


def mana_end(n):
    return f"Такова {MANA} {K1.NUMW[n]}."


MANA_RX = re.compile(r"^(Tattha katamaṃ manāyatanaṃ\? )?(\S+?)[vb]idhena manāyatanaṃ – (.*?)"
                     r"(?: Evaṃ (\S+?)[vb]idhena manāyatanaṃ\.)?$")


def mana_line(p):
    """the manāyatana classification lines of ^2-161"""
    tail = ""
    m13 = re.match(r'^(.*)…pe…\. Evaṃ bahuvidhena manāyatanaṃ\. Idaṃ vuccati "manāyatanaṃ"\.$', p)
    if m13:
        p = m13.group(1)
        tail = f"…. {mana_end('many')} {cap(called_q(MANA))}"
    m = MANA_RX.match(p)
    assert m, p
    qq, nw, body, nw2 = m.groups()
    body = re.sub(r"^phassasampayuttaṃ\.", "phassasampayutto.", body)   # neuter of the K1 item key
    out = f"{q(MANA)} " if qq else ""
    out += f"{mana_head(K1.NUMP[nw.lower()])} {K1.chain(body)}"
    if nw2:
        assert nw2.lower() == nw.lower(), p
        out += f" {mana_end(K1.NUMP[nw2.lower()])}"
    return out + tail


KH_RX = re.compile(r'^Tattha katamo (\S+kkhandho)\? (Ekavidhena .*?\.) (Duvidhena .*?\.) (Tividhena \S+ – .*?)'
                   r'…pe… evaṃ dasavidhena (\S+)…pe… evaṃ bahuvidhena (\S+)( – ayaṃ vuccati|\. Ayaṃ vuccati) "(\S+)"\.$')


def khandha_line(p):
    """Tattha katamo vedanākkhandho? Ekavidhena … …pe… evaṃ bahuvidhena vedanākkhandho. Ayaṃ vuccati "…"."""
    if "atthi hetu, atthi ahetu." in p:
        slip("^2-184 «atthi hetu, atthi ahetu» (elsewhere «atthi na hetu»): ahetu «не корень» gives the same Russian "
             "«бывает не корнем»")
        p = p.replace("atthi hetu, atthi ahetu.", "atthi hetu, atthi na hetu.")
    m = KH_RX.match(p)
    assert m, p
    kh, eka, du, ti, kh10, khb, sep, khq = m.groups()
    k = K1.KHP[kh]
    assert K1.KHP[kh10] == K1.KHP[khb] == K1.KHP[khq] == k, p
    end10 = low(K1.vidha_end(10, k))[:-1]
    endb = low(K1.vidha_end("many", k))[:-1]
    called = f"«{S.kh_ins(k)}»."
    close = f". Это называется {called}" if sep.startswith(".") else f" – это называется {called}"
    return (f"{S.agg_q(k)} {K1.abhi_line(eka)} {K1.abhi_line(du)} {K1.abhi_line(ti)}… {end10}… {endb}{close}")


DHAMMA_MEMBERS = (f"{cap(S.KH['vedana'])}, {S.KH['sanna']}, {S.KH['sankhara']}, "
                  "та материальная форма, которая является невидимой и не способной к соударению и принадлежит к сфере "
                  f"объектов ума, и {DH['asaṅkhatā']}")
# Vedanākkhandho, saññākkhandho, saṅkhārakkhandho, yañca rūpaṃ anidassanaappaṭighaṃ dhammāyatanapariyāpannaṃ,
# asaṅkhatā ca dhātu. (the «та материальная форма, которая …» clause = pi-1 ^1-593 / ^1-1058)
ANID_Q = "невидимая материальная форма, не способная к соударению и принадлежащая к сфере объектов ума"  # pi-1 ^1-984
ANID_INS = "материальной формой, «невидимой, не способной к соударению и принадлежащей к сфере объектов ума»"
# Idaṃ vuccati rūpaṃ "anidassanaappaṭighaṃ dhammāyatanapariyāpannaṃ" (the quote covers the attributes only)
FEM_PUR = "способность женственности, способность мужественности… съедаемая пища"   # Itthindriyaṃ purisindriyaṃ…pe…
NIBBANA = "Уничтожение страсти, уничтожение злобы и уничтожение заблуждения"         # Rāgakkhayo, dosakkhayo, mohakkhayo


# =========================================================================== chapter 3: Suttantabhājanīya
CORE = {  # pi-1 ^1-967 / 651 / 969 / 970 / 637 wording
    "pathavī": "твёрдое, то, что считается жёстким, твёрдость, свойство твёрдости",
    "āpo": "вода, то, что считается водой, влага, то, что считается влагой{v}, связующее свойство материальной формы",
    "tejo": "огонь, то, что считается огнём, тепло, то, что считается теплом, жар, то, что считается жаром",
    "vāyo": "ветер, то, что считается ветром, состояние напряжённости материальной формы",
    "ākāsa": "пространство, то, что считается пространством, незаполненное, то, что считается незаполненным, просвет, "
             "то, что считается просветом, не затронутое {by}",
}
SNEHO_VAR = " [вариант написания (Syā.): sneho snehagataṃ]"
BY_FLESH = "плотью и кровью"                      # maṃsalohitehi
BY_GREAT = "четырьмя великими элементами"          # catūhi mahābhūtehi (pi-1 ^1-637)
INT_ATTR = "внутреннее, охваченное цеплянием"      # ajjhattaṃ upādinnaṃ
EXT_ATTR = "внешнее, не охваченное цеплянием"      # bahiddhā anupādinnaṃ


def head_int(core):
    """Yaṃ ajjhattaṃ paccattaṃ <core> ajjhattaṃ upādinnaṃ"""
    return f"То внутреннее, собственное, что есть {core}, {INT_ATTR}"


def other_int(core):
    """yaṃ vā panaññampi atthi ajjhattaṃ paccattaṃ <core> ajjhattaṃ upādinnaṃ"""
    return f"или же любое другое внутреннее, собственное, что есть {core}, {INT_ATTR}"


def head_ext(core):
    """Yaṃ bāhiraṃ <core> bahiddhā anupādinnaṃ"""
    return f"То относящееся к внешнему, что есть {core}, {EXT_ATTR}"


def other_ext(core):
    return f"или же любое другое относящееся к внешнему, что есть {core}, {EXT_ATTR}"


def gen_pl(name):
    """«элемент земли» -> «элементов земли» (Pathavīdhātudvayaṃ = «Элементов земли два»)"""
    return name.replace("элемент", "элементов", 1)


def int_name(k):
    return f"{DH[k]}, относящийся к внутреннему"


def ext_name(k):
    return f"{DH[k]}, относящийся к внешнему"


def int_ins(k):
    return f"{ins(DH[k])}, относящимся к внутреннему"


def ext_ins(k):
    return f"{ins(DH[k])}, относящимся к внешнему"


NAMELY = "а именно –"                               # seyyathidaṃ –
LISTS = {
    "pathavī_i": ("волосы на голове, волосы на теле, ногти, зубы, кожа, плоть, сухожилия [вариант написания (Sī.): "
                  "nahāru], кости, костный мозг [вариант чтения (Sī.): aṭṭhimiñjā], почки, сердце, печень, плевра, "
                  "селезёнка, лёгкие, кишечник, брыжейка, содержимое желудка, кал"),
    "pathavī_e": ("железо, медь, олово, свинец, серебро [вариант чтения (Syā.): sajjhu], жемчуг, драгоценные камни, "
                  "берилл, раковина, кристалл, коралл, монеты, золото, рубин [вариант написания (Syā., Ka.): "
                  "lohitaṅgo; вариант чтения (?): lohitako], кошачий глаз, трава, дерево, гравий, черепки [вариант "
                  "написания (Ka.): kathalaṃ], земля, камень, гора"),
    "āpo_i": "желчь, слизь, гной, кровь, пот, жир, слёзы, жидкий жир, слюна, сопли, суставная жидкость, моча",
    "āpo_e": ("сок корней, сок стеблей, сок коры, сок листьев, сок цветов, сок плодов, молоко, простокваша, "
              "топлёное масло, сливочное масло, растительное масло, мёд, патока, воды в земле или воды в небе"),
    "tejo_i": ("то, от чего согреваются, то, от чего стареют, то, от чего сгорают в жару, и то, благодаря чему "
               "съеденное, выпитое, разжёванное и отведанное правильно переваривается"),
    "tejo_e": ("огонь от дров, огонь от соломы [вариант чтения (во всех изданиях): sakalikaggi], огонь от травы, "
               "огонь от навоза, огонь от мякины, огонь от мусора, огонь молнии, жар огня, жар солнца, жар от кучи "
               "дров, жар от кучи травы, жар от кучи зерна, жар от кучи товаров"),
    "vāyo_i": ("ветры, идущие вверх, ветры, идущие вниз, ветры в животе, ветры в кишечнике [вариант написания "
               "(Sī., Syā.): koṭṭhasayā], ветры, проходящие по всем членам тела, режущие как нож ветры, режущие как "
               "бритва ветры, колющие ветры, вдох, выдох и тому подобное"),
    "vāyo_e": ("восточные ветры, западные ветры, северные ветры, южные ветры, пыльные ветры, ветры без пыли, "
               "холодные ветры, горячие ветры, слабые ветры, сильные ветры, грозовые ветры, ветры поднебесья, "
               "ветры от крыльев, ветры гаруды, ветры от опахал из пальмовых листьев, ветры от вееров"),
    "ākāsa_i": ("ушное отверстие, носовое отверстие, отверстие рта, то, через что проглатывают съеденное, выпитое, "
                "разжёванное и отведанное, то, где съеденное, выпитое, разжёванное и отведанное пребывает, и то, через "
                "что съеденное, выпитое, разжёванное и отведанное выходит вниз"),
}
TOGETHER = "всё вместе, собранное воедино и обобщённое,"   # tadekajjhaṃ abhisaññūhitvā abhisaṅkhipitvā (sample)


def element_segment(k):
    core = CORE[k].format(v=SNEHO_VAR if k == "āpo" else "", by=BY_FLESH)
    core_plain = CORE[k].format(v="", by=BY_FLESH)
    core_e = CORE[k].format(v="", by=BY_GREAT)
    l1 = (f"{q(DH[k])} {cap(gen_pl(DH[k]))} два – есть относящийся к внутреннему, есть относящийся к внешнему. "
          f"{q(int_name(k))} {head_int(core)}, {NAMELY} {LISTS[k + '_i']}, {other_int(core_plain)}, "
          f"– это называется «{int_ins(k)}».")
    if k == "ākāsa":
        ext_body = f"{head_ext(core_e)},"
    else:
        ext_body = f"{head_ext(core_e)}, {NAMELY} {LISTS[k + '_e']}, {other_ext(core_e)},"
    l2 = (f"{q(ext_name(k))} {ext_body} – это называется «{ext_ins(k)}». "
          f"{cap(int_name(k))}, и {ext_name(k)}, {TOGETHER} – это называется «{ins(DH[k])}».")
    return [l1, l2]


SIX_A = ["pathavī", "āpo", "tejo", "vāyo", "ākāsa", "viññāṇa"]
SIX_B = ["sukha", "dukkha", "somanassa", "domanassa", "upekkhā", "avijjā"]
SIX_C = ["kāma", "byāpāda", "vihiṃsā", "nekkhamma", "abyāpāda", "avihiṃsā"]
THESE_SIX = "Таковы шесть элементов."              # Imā cha dhātuyo.
MORE_SIX = "Ещё шесть элементов –"                 # Aparāpi cha dhātuyo –
VINN6 = nlist([DH[k + "viññāṇa"] for k in ("cakkhu", "sota", "ghāna", "jivhā", "kāya", "mano")])

FEELING_P1 = {  # Yaṃ kāyikaṃ sātaṃ … vedanā (pi-1 ^1-445, 558, 3, 415, 152 without the «tajjā…samphassajaṃ» prefix)
    "sukha": ("телесная отрада, телесное удовольствие, рождённое контактом тела отрадное приятное переживание, "
              "рождённое контактом тела отрадное приятное чувство"),
    "dukkha": ("телесная безотрадность, телесная боль, рождённое контактом тела безотрадное болезненное переживание, "
               "рождённое контактом тела безотрадное болезненное чувство"),
    "somanassa": ("душевная отрада, душевное счастье, рождённое контактом ума отрадное приятное переживание, "
                  "рождённое контактом ума отрадное приятное чувство"),
    "domanassa": ("душевная безотрадность, душевная боль, рождённое контактом ума безотрадное болезненное "
                  "переживание, рождённое контактом ума безотрадное болезненное чувство"),
    "upekkhā": ("душевное состояние, которое ни отрадно, ни безотрадно, рождённое контактом ума переживание, которое "
                "ни болезненно, ни приятно, рождённое контактом ума чувство, которое ни болезненно, ни приятно"),
}
MOHA_P1 = ("незнание, отсутствие видения, отсутствие постижения, отсутствие понимания, непробуждённость, отсутствие "
           "проникновения, неохватывание, отсутствие углубления, отсутствие рассмотрения, отсутствие обдумывания, "
           "неспособность видеть воочию, тупость, глупость, отсутствие ясного понимания, заблуждение, сильное "
           "заблуждение, полное заблуждение, неведение, поток неведения, ярмо неведения, скрытая склонность к "
           "неведению, одержимость неведением, засов неведения, заблуждение как неблагой корень")   # pi-1 ^1-390
VITAKKA7 = ("мышление, направленная мысль, помысел, прикрепление мысли, усиленное прикрепление мысли, "
            "направление ума на объект")                                                          # pi-1 ^1-7
MICCHA = "ложный помысел"
SAMMA = "правильный помысел"
CONNECTED = {"kāma": "связанные с чувственными желаниями", "byāpāda": "связанные с недоброжелательностью",
             "vihiṃsā": "связанные с жестокостью", "nekkhamma": "связанные с отречением",
             "abyāpāda": "связанные с отсутствием недоброжелательности",
             "avihiṃsā": "связанные с отсутствием жестокости"}   # Xpaṭisaṃyutto (said of the whole thought series)
DOSA_LIST = ("досада ума в связи с десятью поводами для досады, раздражение, неприязнь, противодействие, "
             "негодование, сильное негодование, крайнее негодование, злоба, сильная злоба, крайняя злоба, "
             "недоброжелательность ума, сильная злоба ума, гнев, гневливость, состояние гнева, злоба, проявление "
             "злобы, состояние злобы, недоброжелательность, проявление недоброжелательности, вражда, "
             "противодействие, свирепость, грубость, недовольство ума")
# Dasasu vā āghātavatthūsu cittassa āghāto … anattamanatā cittassa (pi-1 ^1-1066 list; pi-2 has no byāpajjitattaṃ)


def thought(k, full):
    """Xpaṭisaṃyutto takko vitakko (saṅkappo … abhiniropanā | …pe…) micchā/sammāsaṅkappo"""
    last = MICCHA if k in ("kāma", "byāpāda", "vihiṃsā") else SAMMA
    series = f"{VITAKKA7}, {last}" if full else f"мышление, направленная мысль… {last}"
    return f"{cap(series)}, {CONNECTED[k]},"


def called_dh(k):
    return f"это называется «{ins(DH[k])}»."


# =========================================================================== Abhidhamma of ch. 3: the mind series
CITTA_SYN = ("ум, разум, умственная деятельность, сердце, чистота, разум, сфера ума, способность ума, сознание, "
             "совокупность сознания")      # cittaṃ mano mānasaṃ hadayaṃ paṇḍaraṃ mano manāyatanaṃ … (pi-1 ^1-6)
CITTA_SHORT = "ум, разум, умственная деятельность…"   # cittaṃ mano mānasaṃ…pe…
TAJJA = "соответствующий"                             # tajjā-
GEN = {"cakkhu": "элемента зрительного сознания", "sota": "элемента слухового сознания",
       "ghāna": "элемента обонятельного сознания", "jivhā": "элемента вкусового сознания",
       "kāya": "элемента осязательного сознания", "mano": "элемента ума"}
AFTER = "сразу после возникновения и прекращения"     # X-dhātuyā uppajjitvā niruddhasamanantarā
DEPEND = {"cakkhu": "глаза и видимых форм", "sota": "уха и звуков", "ghāna": "носа и запахов",
          "jivhā": "языка и вкусов", "kāya": "тела и осязаемого", "mano": "ума и объектов ума"}
# Cakkhuñca paṭicca rūpe ca = «В зависимости от глаза и видимых форм» (paṭicca: no termbase entry)


def arises(tajja_name):
    """uppajjati cittaṃ … tajjā<X>"""
    return f"возникает {CITTA_SYN}, {TAJJA} {tajja_name}"


def vinnana_line(k):
    nm = DH[k + "viññāṇa"]
    return f"{q(nm)} В зависимости от {DEPEND[k]} {arises(nm)} – {called_q(nm)}"


def manodhatu_line():
    t = DH["mano"]
    return (f"{q(t)} {cap(AFTER)} {GEN['cakkhu']} {arises(t)}; после {GEN['sota']}… {GEN['ghāna']}… {GEN['jivhā']}… "
            f"{AFTER} {GEN['kāya']} {arises(t)}, или же при первом обращении внимания ко всем явлениям {arises(t)} – "
            f"{called_q(t)}")


def manovinnana_line():
    t = DH["manoviññāṇa"]
    short = f"возникает {CITTA_SHORT} {TAJJA} {t}"
    return (f"{q(t)} {cap(AFTER)} {GEN['cakkhu']} возникает {DH['mano']}, {AFTER} {GEN['mano']} {short}; после "
            f"{GEN['sota']}… {GEN['ghāna']}… {GEN['jivhā']}… {AFTER} {GEN['kāya']} возникает {DH['mano']}, {AFTER} "
            f"также {GEN['mano']} {short}, в зависимости от {DEPEND['mano']} {arises(t)} – {called_q(t)}")


# =========================================================================== Pañhāpucchaka
GROUPS = dict(K1.GROUP_GEN)
GROUPS.update({"Dvādasannaṃ āyatanānaṃ": "из двенадцати сфер восприятия",
               "Aṭṭhārasannaṃ dhātūnaṃ": "из восемнадцати элементов"})
SUBJ = {}   # Pāli subject -> (Russian nominative, number s/p, gender f/m/p, accusative)
for _p, (_r, _n) in K1.SUBJ.items():
    SUBJ[_p] = (_r, _n, "f" if _n == "s" else "p", _r)
for _p, _n in (("Dasāyatanā", "Десять"), ("Ekādasāyatanā", "Одиннадцать"), ("Pañcāyatanā", "Пять"),
               ("Navāyatanā", "Девять"), ("Chāyatanā", "Шесть")):
    SUBJ[_p] = (f"{_n} сфер восприятия", "p", "p", f"{_n} сфер восприятия")
for _p, _n in (("Dvāyatanā", "Две"), ("Cattāro āyatanā", "Четыре")):
    SUBJ[_p] = (f"{_n} сферы восприятия", "p", "p", f"{_n} сферы восприятия")
for _p, _k in (("Manāyatanaṃ", "mana"), ("Dhammāyatanaṃ", "dhamma"), ("Saddāyatanaṃ", "sadda"),
               ("Rūpāyatanaṃ", "rūpa")):
    SUBJ[_p] = (cap(AY[_k]), "s", "f", "Сферу " + AY[_k].split(" ", 1)[1])
for _p, _n in (("Soḷasa", "Шестнадцать"), ("Dasa", "Десять"), ("Pañca", "Пять"), ("Pannarasa", "Пятнадцать"),
               ("Cha", "Шесть"), ("Sattarasa", "Семнадцать"), ("Nava", "Девять"), ("Aṭṭha", "Восемь"),
               ("Satta", "Семь"), ("Ekādasa", "Одиннадцать"), ("Dvādasa", "Двенадцать")):
    SUBJ[f"{_p} dhātuyo"] = (f"{_n} элементов", "p", "p", f"{_n} элементов")
SUBJ["Sattadhātuyo"] = ("Семь элементов", "p", "p", "Семь элементов")      # source writes it as one word
SUBJ["Dve dhātuyo"] = ("Два элемента", "p", "p", "Два элемента")
SUBJ["Tisso dhātuyo"] = ("Три элемента", "p", "p", "Три элемента")
for _p, _k in (("Kāyaviññāṇadhātu", "kāyaviññāṇa"), ("Manoviññāṇadhātu", "manoviññāṇa"), ("Dhammadhātu", "dhamma"),
               ("Manodhātu", "mano"), ("Saddadhātu", "sadda"), ("Rūpadhātu", "rūpa")):
    SUBJ[_p] = (cap(DH[_k]), "s", "m", cap(DH[_k]))
PRON = {"f": "её", "m": "его", "p": "их"}

# ---- matrix items missing from K1 (dyads of conditions / the conditioned) and two slips of the source
LOCAL = {
    "sappaccayo": K1.A("имеющая условия", v="имеет условия"),              # termbase sappaccayaṃ «иметь условия»
    "appaccayo": K1.A("не имеющая условий", v="не имеет условий"),         # no termbase entry (negated sibling)
    "saṅkhato": K1.A("обусловленная"),                                     # termbase saṅkhataṃ «обусловленный»
    "asaṅkhato": K1.A("необусловленная"),                                  # termbase asaṅkhataṃ «необусловленный»
    # ^2-171 Manāyatanaṃ na vattabbaṃ – "upādāniyañceva upādānasampayuttañcā"ti (for upādānañceva …): as written
    "upādāniyo ceva upādānasampayutto ca": K1.A("служащая объектом цепляния и связанная с цепляниями",
                                               v="служит объектом цепляния и связана с цепляниями"),
    # ^2-171 Dvāyatanā siyā upādānasampayuttaupādāniyā (for upādānavippayutta…): as written
    "upādānasampayuttaupādāniyo": K1.A("связанная с цепляниями и служащая объектом цепляния",
                                       v="связана с цепляниями и служит объектом цепляния"),
}
LOCAL_SLIP = {
    "upādāniyo ceva upādānasampayutto ca": "^2-171 Manāyatanaṃ na vattabbaṃ – \"upādāniyañceva upādānasampayuttañcā\"ti "
                                           "(the pattern has upādānañceva): translated as written «служащая объектом "
                                           "цепляния и связанная с цепляниями»",
    "upādānasampayuttaupādāniyo": "^2-171 Dvāyatanā siyā upādānasampayuttaupādāniyā (the pattern has "
                                  "upādānavippayuttaupādāniyā): translated as written «связанными с цепляниями и "
                                  "служащими объектом цепляния»",
}


def get(key):
    if key in LOCAL:
        if key in LOCAL_SLIP:
            slip(LOCAL_SLIP[key])
        return LOCAL[key]
    if key in K1.ALIAS:
        slip(f"«{key}» written as one word (elsewhere «{K1.ALIAS[key]}»; rendered the same)")
        key = K1.ALIAS[key]
    return K1.ITEMS[key]


def known(key):
    return key in LOCAL or key in K1.ITEMS or key in K1.ALIAS


PLK = dict(K1.PL_KEY)
for _k in LOCAL:
    PLK.setdefault(K1.pali_plural(_k), _k)
PLK["na hetuahetukā"] = "na hetuahetuko"          # one word in the source (ch. 3)
PLK["na hetūahetukā"] = "na hetuahetuko"          # one word in the source (ch. 2)


# ---- masculine forms («элемент …» subjects)
_MASC_SPECIAL = {"благая": "благой", "неблагая": "неблагой", "мирская": "мирской", "та": "тот", "которой": "которому",
                 "соединённой": "соединённым", "порождённой": "порождённым", "сосуществующей": "сосуществующим",
                 "следующей": "следующим"}


def _mword(w):
    if w in _MASC_SPECIAL:
        return _MASC_SPECIAL[w]
    if w.endswith("аяся"):
        return w[:-4] + "ийся"
    if w.endswith("яя"):
        return w[:-2] + "ий"
    if w.endswith("ая"):
        s = w[:-2]
        return s + ("ий" if s[-1] in "гкхжшщч" else "ый")
    return w


SHORT_M = {"связана": "связан", "подвержена": "подвержен", "свободна": "свободен", "способна": "способен",
           "затронута": "затронут", "охвачена": "охвачен", "омрачена": "омрачён", "соединена": "соединён",
           "порождена": "порождён", "познаваема": "познаваем",
           "соединённой": "соединённым", "порождённой": "порождённым", "сосуществующей": "сосуществующим",
           "следующей": "следующим"}


def masc_f(it):
    return re.sub(r"[А-Яа-яЁё]+", lambda m: _mword(m.group(0)), it["f"])


def masc_v(it):
    v = it["v"]
    if v == "является " + it["ins"]:
        return "является " + it["nins"]
    return re.sub(r"[А-Яа-яЁё]+", lambda m: SHORT_M.get(m.group(0), m.group(0)), v)


# ---- Pāli predicate -> key
def _word_opts(w):
    o = [w]
    if w.endswith("añceva"):
        o.append(w[:-6] + "o ceva")
    if w.endswith("añca"):
        o.append(w[:-4] + "o ca")
    if w.endswith("aṃ"):
        o.append(w[:-2] + "o")
    if w.endswith("ā"):
        o += [w[:-1] + "o", w[:-1] + "aṃ"]
    if w.endswith("inī"):
        o.append(w[:-3] + "ī")
    elif w.endswith("ī"):
        o.append(w[:-1] + "i")
    if w.endswith("i") and not w.endswith("hetu"):
        o.append(w[:-1] + "ī")
    return o


def sg_key(t):
    """Pāli predicate said of a singular subject (neuter -aṃ, feminine -ā or masculine) -> ITEMS key"""
    t = re.sub(r"hetū$", "hetu", t)
    if known(t):
        return t
    words = t.split(" ")
    cands = []
    for combo in itertools.product(*[_word_opts(w) for w in words]):
        c = " ".join(combo)
        if known(c):
            cands.append((sum(a != b for a, b in zip(combo, words)), c))
    if not cands and known(t + " ca"):
        slip(f"«{t}» in a quote without «ca» (rendered like «{t} ca»)")
        return t + " ca"
    if not cands:
        for combo in itertools.product(*[_word_opts(w) for w in words]):
            c = " ".join(combo) + " ca"
            if known(c):
                slip(f"«{t}» in a quote without «ca» (rendered like «{c}»)")
                return c
    assert cands, t
    key = sorted(cands)[0][1]
    it = get(key)
    nouns = {K1.CL[c][0] for c in K1.CL} | {"cittaṃ"}
    if key.split(" ")[-1] in nouns and len(key.split(" ")) <= 2 and t == K1.pali_plural(key) and t != key:
        slip(f"«{t}» (plural noun) with a singular subject (rendered in the singular)")
    return key


def pl_key(t):
    if t in PLK:
        return PLK[t]
    t2 = re.sub(r"^hetu ", "hetū ", t)
    if t2 in PLK:
        slip(f"«{t}» with a plural subject («hetu» for «hetū»; rendered in the plural)")
        return PLK[t2]
    raise KeyError(t)


def pred(word, num, gen):
    if num == "s":
        it = get(sg_key(word))
        return masc_v(it) if gen == "m" else it["v"]
    return get(pl_key(word))["vp"]


def qkey(text, num, suffix):
    t = text
    if suffix and suffix.startswith("n"):
        t += "ṃ"
    t = re.sub(r"cā$", "ca", t)
    if num == "s":
        return sg_key(t)
    return pl_key(t)


def quote(key, num, gen):
    it = get(key)
    if num == "p":
        return f"«{it['pl']}»"
    return f"«{masc_f(it) if gen == 'm' else it['f']}»"


QUOTE = K1.QUOTE
NV = K1.NV
PANHA_FIX = [  # plain typographic slips of the source, rendered as meant (reported)
    ('"kilesasampayuttā ceva no ca na kilesā"tipi', '"kilesasampayuttā ceva no ca kilesā"tipi',
     '^2-171 "kilesasampayuttā ceva no ca na kilesā"tipi: the negation is doubled («no ca na»); rendered as meant '
     '(«…, но не являющиеся омрачениями»)'),
    ('"parāmāsā ceva parāmaṭṭhā cāti parāmaṭṭhā ceva no ca parāmāsā"',
     '"parāmāsā ceva parāmaṭṭhā cā"ti, "parāmaṭṭhā ceva no ca parāmāsā"',
     '^2-188 "parāmāsā ceva parāmaṭṭhā cāti parāmaṭṭhā ceva no ca parāmāsā": both items inside one quote; '
     'rendered as the parallel lines («как «…», затронуты искажениями, но не являются искажениями»)'),
]


def render_nv(nv):
    many = any(s and s.startswith(("tipi", "ti pi", "ntipi")) for _, s in nv["q"])
    if many:
        body = ", ".join(f"ни как {x}" for x, _ in nv["q"])
    else:
        body = "как " + ", ".join(x for x, _ in nv["q"])
    return f"{nv['head']} {body}"


def sentence(sent):
    """one Pañhāpucchaka sentence (without its final full stop); port of K1._sentence for neuter / feminine Pāli
    predicates and for masculine Russian subjects («элемент …»)"""
    m = re.match(r"^(" + "|".join(sorted(SUBJ, key=len, reverse=True)) + r") (.*)$", sent)
    assert m, sent
    subj, num, gen, acc = SUBJ[m.group(1)]
    body = m.group(2)
    if body.endswith("āti"):                       # closing «…ti» of the whole section
        body = body[:-2]
    toks = re.split(r"(, |; |…pe… )", body)
    out, prev_v, first, nv = [], None, True, None
    for i, tok in enumerate(toks):
        if i % 2 == 1:
            if nv is None:
                out.append("…" if tok == "…pe… " else tok.strip())
            else:
                nv["pending"] = "…" if tok == "…pe… " else tok.strip()
            if tok.strip() == ";":
                prev_v = None
            continue
        qm = QUOTE.match(tok)
        if qm and qm.group(2) is None:             # «na vattabbo – "A"ti, "B".»: B is a plain predicate (coordinator)
            assert nv is not None, sent
            out.append(render_nv(nv))
            out.append(nv["pending"] or ",")
            nv, prev_v = None, None
            out.append(pred(qm.group(1), num, gen) if num == "s" else get(pl_key(qm.group(1)))["vp"])
            continue
        if qm:
            assert nv is not None, sent
            nv["q"].append((quote(qkey(qm.group(1), num, qm.group(2)), num, gen), qm.group(2)))
            nv["pending"] = None
            continue
        if nv is not None:
            out.append(render_nv(nv))
            if nv["pending"]:
                out.append(nv["pending"])
            nv, prev_v = None, None
        mv = re.match(r'^(siyā )?na vattabb[oaā]ṃ? – (.*)$', tok)
        if mv:
            qm = QUOTE.match(mv.group(2))
            assert qm, tok
            k = qkey(qm.group(1), num, qm.group(2))
            if mv.group(1):
                head = f"иногда {PRON[gen]} {NV}"
            elif first:
                head = f"{acc} {NV}"
            else:                                  # «…, siyā Y, na vattabbā – "Z"ti» (no siyā)
                head = f"{PRON[gen]} {NV}"
            nv = dict(head=head, q=[(quote(k, num, gen), qm.group(2))], pending=None)
            first = False
            continue
        siya = tok.startswith("siyā ")
        word = tok[5:] if siya else tok
        v = pred(word, num, gen)
        shown = v
        if prev_v is not None and prev_v[1] == siya:
            for verb in ("является ", "являются "):
                if v.startswith(verb) and prev_v[0].startswith(verb):
                    shown = v[len(verb):]
        prev_v = (v, siya)
        shown = ("иногда " + shown) if siya else shown
        out.append(f"{subj} {shown}" if first else shown)
        first = False
    if nv is not None:
        out.append(render_nv(nv))
    res = ""
    for x in out:
        if x in (",", ";", "…"):
            res += x
        else:
            res += (" " if res else "") + x
    res = res.replace("познаваемы тем или иным видом сознания, не познаваемы",
                      "познаваемы тем или иным видом сознания и не познаваемы")
    return res


def panha_line(p):
    p = p.replace('"ti pi', '"tipi')
    for bad, good, note in PANHA_FIX:
        if bad in p:
            p = p.replace(bad, good)
            slip(note)
    if "Sattadhātuyo" in p:
        slip("^2-188 «Sattadhātuyo» written as one word (= Satta dhātuyo, «Семь элементов»)")
    sents = re.split(r"(?<=\.) (?=[A-Z])", p)
    return " ".join(sentence(s[:-1]) + "." for s in sents)


def panha_question(p):
    return K1.panha_question(p, GROUPS)


# =========================================================================== chapters
FIXED = dict(K1.FIXED)
FIXED.update({
    "Āyatanavibhaṅgo niṭṭhito.": f"{S.CH_TITLE[2][1]} {S.DONE}.",
    "Dhātuvibhaṅgo niṭṭhito.": f"{S.CH_TITLE[3][1]} {S.DONE}.",
    "Imā cha dhātuyo.": THESE_SIX,
})


def heading(ln, section):
    lvl, text = ln.split(" ", 1)
    T = {"Āyatanavibhaṅgo": S.CH_TITLE[2][1], "Dhātuvibhaṅgo": S.CH_TITLE[3][1],
         "Suttantabhājanīyaṃ": S.SUTTANTA_BH, "Abhidhammabhājanīyaṃ": S.ABHI_BH, "Pañhāpucchakaṃ": S.PANHA,
         "Tikaṃ": S.TIKA_H, "Dukaṃ": S.DUKA_H}
    return f"{lvl} {T[text]}"


def build_ch2():
    h = {}
    h["2-154"] = [AY12_S, IMPERM_LINE, f"{S.SUTTANTA_BH}."]
    h["2-155"] = [AY12_A]
    for sid, k in (("2-156", "cakkhu"), ("2-157", "sota"), ("2-158", "ghāna"), ("2-159", "jivhā"), ("2-160", "kāya"),
                   ("2-162", "rūpa"), ("2-163", "sadda"), ("2-164", "gandha"), ("2-165", "rasa"),
                   ("2-166", "phoṭṭhabba")):
        h[sid] = [ay_segment(k)]
    return h


def build_ch3():
    h = {}
    h["2-172"] = [f"Шесть элементов – {DH['pathavī']} [вариант написания (Sī., Syā.): paṭhavīdhātu, так же и далее], "
                  + nlist([DH[k] for k in SIX_A[1:]]) + "."]
    for sid, k in (("2-173", "pathavī"), ("2-174", "āpo"), ("2-175", "tejo"), ("2-176", "vāyo"), ("2-177", "ākāsa")):
        h[sid] = element_segment(k)
    h["2-178"] = [f"{q(DH['viññāṇa'])} {cap(VINN6)} – {called_dh('viññāṇa')}", THESE_SIX]
    h["2-179"] = [f"{MORE_SIX} {nlist([DH[k] for k in SIX_B])}."]
    L = [f"{q(DH[k])} То, что есть {FEELING_P1[k]}, – {called_dh(k)}" for k in SIX_B[:5]]
    L.append(f"{q(DH['avijjā'])} То, что есть {MOHA_P1}, – {called_dh('avijjā')}")
    L.append(THESE_SIX)
    h["2-180"] = L
    h["2-181"] = [f"{MORE_SIX} {nlist([DH[k] for k in SIX_C])}."]
    kama2 = ("Если взять снизу границей ад Авичи, а сверху включить в эти пределы богов, властвующих над творениями "
             "других, то всё, что находится в этих пределах, относится к этому миру и принадлежит к нему: совокупности, "
             "элементы и сферы восприятия, материальные формы [вариант чтения (Syā.): rūpaṃ], чувство, восприятие, "
             "формирующие факторы и сознание")
    # Heṭṭhato avīcinirayaṃ pariyantaṃ karitvā uparito paranimmitavasavattī deve anto karitvā yaṃ etasmiṃ antare
    # etthāvacarā ettha pariyāpannā khandhadhātuāyatanā rūpā [rūpaṃ (syā.)] vedanā saññā saṅkhārā viññāṇaṃ
    vihimsa2 = ("Здесь некий человек мучает существ рукой, комом земли, палкой, оружием, верёвкой или чем-либо ещё; "
                "такое мучение, сильное мучение, насилие, жестокое обращение, досаждение, сильное досаждение, "
                "причинение вреда другим")
    metta = "Доброжелательность к существам, проявление доброжелательности, состояние доброжелательности, " \
            "освобождение ума доброжелательностью"
    karuna = "Сострадание к существам, проявление сострадания, состояние сострадания, освобождение ума состраданием"
    h["2-182"] = [
        f"{q(DH['kāma'])} {thought('kāma', True)} – это называется {ins(DH['kāma'])}. {kama2} – {called_dh('kāma')}",
        f"{q(DH['byāpāda'])} {thought('byāpāda', False)} – {called_dh('byāpāda')} Или же {DOSA_LIST} – "
        f"{called_dh('byāpāda')}",
        f"{q(DH['vihiṃsā'])} {thought('vihiṃsā', False)} – {called_dh('vihiṃsā')} {vihimsa2} – {called_dh('vihiṃsā')}",
        f"{q(DH['nekkhamma'])} {thought('nekkhamma', False)} – {called_dh('nekkhamma')} Все благие явления тоже "
        f"являются «{ins(DH['nekkhamma'])}».",
        f"{q(DH['abyāpāda'])} {thought('abyāpāda', False)} – {called_dh('abyāpāda')} {metta} – "
        f"{called_dh('abyāpāda')}",
        f"{q(DH['avihiṃsā'])} {thought('avihiṃsā', True)} – {called_dh('avihiṃsā')} {karuna} – "
        f"{called_dh('avihiṃsā')}",
        THESE_SIX,
        "Так эти три шестёрки, все вместе, собранные воедино и обобщённые, составляют восемнадцать элементов.",
        f"{S.SUTTANTA_BH}.",
    ]
    h["2-183"] = [f"Восемнадцать элементов – {nlist([DH[k] for k in DH18])}."]
    return h


def build(part, chapter):
    pali = (S.PALI / part).read_text(encoding="utf-8")
    h = build_ch2() if chapter == 2 else build_ch3()
    section = None
    for sid, lines in S.segs(pali):
        lines = [re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", ln) for ln in lines]
        if lines[0].startswith("#"):
            assert len(lines) == 1
            text = lines[0].split(" ", 1)[1]
            if text in ("Suttantabhājanīyaṃ", "Abhidhammabhājanīyaṃ", "Pañhāpucchakaṃ"):
                section = text
            h[sid] = [heading(lines[0], section)]
            continue
        if sid in h:
            continue
        ru = []
        for ln in lines:
            if ln in FIXED:
                ru.append(FIXED[ln])
            elif section == "Pañhāpucchakaṃ":
                if ln.startswith(("Dvādasāyatanāni – ", "Aṭṭhārasa dhātuyo – ")):
                    ru.append(AY12_S if chapter == 2 else h["2-183"][0])
                elif ln.endswith("?"):
                    ru.append(panha_question(ln))
                else:
                    ru.append(panha_line(ln))
            else:
                ru.append(abhi(ln, chapter))
        h[sid] = ru
    return pali, h


DH_PE_RX = re.compile(r"^Tattha katamā (\S+)dhātu\? (.*?) – ayaṃ vuccati \"\S+\"\.$")
VINN_RX = re.compile(r"^Tattha katamā (cakkhu|sota|ghāna|jivhā|kāya)viññāṇadhātu\? ")


def abhi(ln, chapter):
    """Abhidhammabhājanīya lines of both chapters"""
    if ln.startswith("Tattha katamaṃ manāyatanaṃ?") or re.match(r"^\S+?[vb]idhena manāyatanaṃ – ", ln):
        return mana_line(ln)
    if ln.startswith("Tattha katamo ") and "kkhandho?" in ln:
        return khandha_line(ln)
    if ln.startswith("Tattha katamaṃ dhammāyatanaṃ?") or ln.startswith("Tattha katamā dhammadhātu?"):
        name = AY["dhamma"] if chapter == 2 else DH["dhamma"]
        return f"{q(name)} {DHAMMA_MEMBERS}."
    if ln.startswith("Tattha katamaṃ rūpaṃ anidassanaappaṭighaṃ"):
        if "purisindriyaṃ" in ln:     # ch. 2: «… āhāro. Idaṃ vuccati rūpaṃ "…".»
            return f"Что такое {S.TATTHA} {ANID_Q}? {cap(FEM_PUR)}. Это называется {ANID_INS}."
        return f"Что такое {S.TATTHA} {ANID_Q}? {cap(S.fem_to_food())} – это называется {ANID_INS}."
    if ln.startswith("Tattha katamā asaṅkhatā dhātu?"):
        out = f"{q(DH['asaṅkhatā'])} {NIBBANA} – {called_q(DH['asaṅkhatā'])}"
        if ln.endswith('Ayaṃ vuccati "dhammadhātu".'):
            out += f" {cap(called_q(DH['dhamma']))}"
        return out
    if ln == "Idaṃ vuccati dhammāyatanaṃ.":
        return f"Это называется {ins(AY['dhamma'])}."
    if ln.startswith("Tattha katamā manodhātu?"):
        return manodhatu_line()
    if ln.startswith("Tattha katamā manoviññāṇadhātu?"):
        return manovinnana_line()
    m = VINN_RX.match(ln)
    if m:
        return vinnana_line(m.group(1))
    m = DH_PE_RX.match(ln)
    if m:
        k = m.group(1)
        return f"{q(DH[k])} {dh_pe(k)}, – {called_q(DH[k])}"
    raise ValueError(ln)


def render(pali, h):
    blocks = []
    for sid, plines in S.segs(pali):
        ru = h[sid]
        assert len(ru) == len(plines), (sid, len(ru), len(plines))
        if plines[0].startswith("#"):
            assert ru[0].split(" ", 1)[0] == plines[0].split(" ", 1)[0], (sid, "heading level")
        lines = list(ru)
        lines[-1] = f"{lines[-1]} ^{sid}"
        blocks.append("\n".join(lines))
    return "\n\n".join(blocks) + "\n"


# =========================================================================== pi-1 checks and notes
def check_pi1():
    assert_pi1(CITTA_SYN, VITAKKA7, MOHA_P1, *FEELING_P1.values(), ANID_Q, "Способность женственности… съедаемая пища",
               "твёрдое, то, что считается жёстким", "твёрдость, свойство твёрдости",
               "вода, то, что считается водой, влага, то, что считается влагой, связующее свойство материальной формы",
               CORE["tejo"], CORE["vāyo"], CORE["ākāsa"].format(by=BY_GREAT),
               "та материальная форма, которая является невидимой и не способной к соударению и принадлежит к сфере "
               "объектов ума", "раздражение, неприязнь, противодействие, негодование, сильное негодование, крайнее "
               "негодование, злоба, сильная злоба, крайняя злоба, недоброжелательность ума, сильная злоба ума, гнев, "
               "гневливость, состояние гнева, злоба, проявление злобы, состояние злобы, недоброжелательность, "
               "проявление недоброжелательности", "вражда, противодействие, свирепость, грубость, недовольство ума",
               "доброжелательность, проявление доброжелательности, состояние доброжелательности")


def notes_md():
    L = ["# pi-2 Russian rails: new formulas of chapters 2 and 3 (^2-154 … ^2-188)", "",
         "Generated by build_rails_2_3_ru.py; import it instead of retyping. Strings already in ru-rails-formulas.md "
         "(sample) or notes-1.md are not repeated.", "",
         "## Āyatanavibhaṅga", "",
         f"Dvādasāyatanāni – cakkhāyatanaṃ, rūpāyatanaṃ, … dhammāyatanaṃ. = {AY12_S}",
         f"(Abhidhamma order) = {AY12_A}",
         "Cakkhuṃ aniccaṃ dukkhaṃ anattā vipariṇāmadhammaṃ. = Глаз непостоянен, является страданием, лишён самости и "
         "подвержен изменению. (neuter: непостоянно …; plural: непостоянны, являются страданием, лишены самости и "
         "подвержены изменению)",
         f"Tattha katamaṃ <X>āyatanaṃ? = {q('сфера X')}",
         "Idaṃ vuccati \"<X>āyatanaṃ\". = Это называется «сферой X».",
         "Yaṃ cakkhu … suñño gāmopeso / Yaṃ rūpaṃ … rūpadhātupesā (sense-base definitions) = the pi-1 Russian "
         "(^1-596, 600, 604, 608, 612, 616, 620, 624, 628, 647) with the pi-2 variant brackets",
         f"[cakkhuṃ (sī. syā. ka.) dha. sa. 596-599] = {EYE_VAR}",
         f"<N>vidhena manāyatanaṃ – = {mana_head(2).replace('на два вида', '<N>')}",
         f"Evaṃ <N>vidhena manāyatanaṃ. = {mana_end(2).replace('на два вида', '<N>')}",
         "Tattha katamo vedanākkhandho? Ekavidhena … …pe… evaṃ dasavidhena vedanākkhandho…pe… evaṃ bahuvidhena "
         "vedanākkhandho. Ayaṃ vuccati \"vedanākkhandho\". = " + khandha_line(
             'Tattha katamo vedanākkhandho? Ekavidhena vedanākkhandho – phassasampayutto. Duvidhena vedanākkhandho – '
             'atthi sahetuko, atthi ahetuko. Tividhena vedanākkhandho – atthi kusalo, atthi akusalo, atthi abyākato'
             '…pe… evaṃ dasavidhena vedanākkhandho…pe… evaṃ bahuvidhena vedanākkhandho. Ayaṃ vuccati '
             '"vedanākkhandho".'),
         f"Vedanākkhandho, saññākkhandho, saṅkhārakkhandho, yañca rūpaṃ anidassanaappaṭighaṃ "
         f"dhammāyatanapariyāpannaṃ, asaṅkhatā ca dhātu. = {DHAMMA_MEMBERS}.",
         f"Tattha katamaṃ rūpaṃ anidassanaappaṭighaṃ dhammāyatanapariyāpannaṃ? = Что такое здесь {ANID_Q}? (pi-1 ^1-984)",
         f"Idaṃ vuccati rūpaṃ \"anidassanaappaṭighaṃ dhammāyatanapariyāpannaṃ\". = Это называется {ANID_INS}.",
         f"Rāgakkhayo, dosakkhayo, mohakkhayo = {NIBBANA}",
         f"asaṅkhatā dhātu = {DH['asaṅkhatā']}",
         f"Dvādasannaṃ āyatanānaṃ kati …? = Сколько {GROUPS['Dvādasannaṃ āyatanānaṃ']} являются …?",
         "Dasāyatanā / Ekādasāyatanā / Pañcāyatanā / Navāyatanā / Chāyatanā = Десять / Одиннадцать / Пять / Девять / "
         "Шесть сфер восприятия; Dvāyatanā / Cattāro āyatanā = Две / Четыре сферы восприятия",
         "Manāyatanaṃ / Dhammāyatanaṃ / Saddāyatanaṃ / Rūpāyatanaṃ = Сфера ума / Сфера объектов ума / Сфера звуков / "
         "Сфера видимых форм (accusative before «нельзя определить»: Сферу ума …)",
         "na vattabbā – \"X\"ti after other predicates, without siyā = их / её / его нельзя определить – как «X»",
         f"sappaccayo / appaccayo / saṅkhato / asaṅkhato = {LOCAL['sappaccayo']['v']} / {LOCAL['appaccayo']['v']} / "
         f"{LOCAL['saṅkhato']['v']} / {LOCAL['asaṅkhato']['v']}",
         f"Āyatanavibhaṅgo niṭṭhito. = {FIXED['Āyatanavibhaṅgo niṭṭhito.']}",
         "", "## Dhātuvibhaṅga", "",
         f"Cha dhātuyo – pathavīdhātu, … viññāṇadhātu. = Шесть элементов – {DH['pathavī']}, … {DH['viññāṇa']}.",
         "Pathavīdhātudvayaṃ – atthi ajjhattikā, atthi bāhirā. = Элементов земли два – есть относящийся к "
         "внутреннему, есть относящийся к внешнему.",
         f"Tattha katamā ajjhattikā pathavīdhātu? = {q(int_name('pathavī'))}",
         f"Yaṃ ajjhattaṃ paccattaṃ X ajjhattaṃ upādinnaṃ = {head_int('X')}",
         f"yaṃ vā panaññampi atthi ajjhattaṃ paccattaṃ X ajjhattaṃ upādinnaṃ = {other_int('X')}",
         f"Yaṃ bāhiraṃ X bahiddhā anupādinnaṃ = {head_ext('X')}",
         f"yaṃ vā panaññampi atthi bāhiraṃ X bahiddhā anupādinnaṃ = {other_ext('X')}",
         f"seyyathidaṃ – = {NAMELY}",
         f"– ayaṃ vuccati ‘ajjhattikā pathavīdhātu’. = – это называется «{int_ins('pathavī')}».",
         f"Yā ca ajjhattikā X yā ca bāhirā X, tadekajjhaṃ abhisaññūhitvā abhisaṅkhipitvā = X, относящийся к "
         f"внутреннему, и X, относящийся к внешнему, {TOGETHER}",
         "cores (pi-1): " + " | ".join(CORE[k].format(v="", by="…") for k in CORE),
         f"Imā cha dhātuyo. = {THESE_SIX}", f"Aparāpi cha dhātuyo – = {MORE_SIX}",
         "Yaṃ kāyikaṃ sātaṃ … vedanā (and the four other feelings), Yaṃ aññāṇaṃ … akusalamūlaṃ = «То, что есть …, – "
         "это называется …» with the pi-1 lists (^1-445, 558, 3, 415, 152, 390)",
         f"Xpaṭisaṃyutto takko vitakko saṅkappo appanā byappanā cetaso abhiniropanā micchāsaṅkappo = "
         f"{thought('kāma', True)}",
         f"Xpaṭisaṃyutto takko vitakko…pe… sammāsaṅkappo = {thought('nekkhamma', False)}",
         f"Dasasu vā āghātavatthūsu cittassa āghāto … anattamanatā cittassa = Или же {DOSA_LIST}",
         f"Tattha katamā cakkhuviññāṇadhātu? Cakkhuñca paṭicca rūpe ca uppajjati cittaṃ … tajjācakkhuviññāṇadhātu – "
         f"ayaṃ vuccati \"cakkhuviññāṇadhātu\". = {vinnana_line('cakkhu')}",
         f"X-dhātuyā uppajjitvā niruddhasamanantarā = {AFTER} X(gen)",
         f"cittaṃ mano mānasaṃ…pe… = {CITTA_SHORT}",
         f"Yaṃ cakkhu catunnaṃ mahābhūtānaṃ upādāya pasādo…pe… suñño gāmopeso = {dh_pe('cakkhu')}",
         f"Yaṃ rūpaṃ catunnaṃ mahābhūtānaṃ upādāya vaṇṇanibhā…pe… rūpadhātupesā = {dh_pe('rūpa')}",
         f"Yo saddo catunnaṃ mahābhūtānaṃ upādāya anidassano sappaṭigho…pe… saddadhātupesā = {dh_pe('sadda')}",
         f"Pathavīdhātu…pe… phoṭṭhabbadhātupesā = {dh_pe('phoṭṭhabba')}",
         f"Aṭṭhārasannaṃ dhātūnaṃ kati …? = Сколько {GROUPS['Aṭṭhārasannaṃ dhātūnaṃ']} являются …?",
         "<N> dhātuyo = <N> элементов (Dve dhātuyo = Два элемента, Tisso dhātuyo = Три элемента)",
         "Kāyaviññāṇadhātu / Manoviññāṇadhātu / Dhammadhātu / Manodhātu / Saddadhātu / Rūpadhātu (subject) = "
         "masculine predicates: «является благим», «связан с …», «нельзя определить – как «связанный с …»», "
         "«иногда его нельзя определить»",
         f"Dhātuvibhaṅgo niṭṭhito. = {FIXED['Dhātuvibhaṅgo niṭṭhito.']}",
         "", "## Masculine forms of the matrix items (key = f masc / v masc)", ""]
    for k, it in list(K1.ITEMS.items()) + list(LOCAL.items()):
        if "#" in k:
            continue
        L.append(f"{k} = {masc_f(it)} / {masc_v(it)}")
    return "\n".join(L) + "\n"


def main():
    check_pi1()
    for part, ch in (("2-ayatanavibhango.md", 2), ("3-dhatuvibhango.md", 3)):
        pali, h = build(part, ch)
        (S.OUT / part).write_text(render(pali, h), encoding="utf-8", newline="\n")
        print(f"wrote {part}: {len(S.segs(pali))} segments")
    NOTES_PATH.write_text(notes_md(), encoding="utf-8", newline="\n")
    for s in SLIPS:
        print("slip:", s)


if __name__ == "__main__":
    main()
