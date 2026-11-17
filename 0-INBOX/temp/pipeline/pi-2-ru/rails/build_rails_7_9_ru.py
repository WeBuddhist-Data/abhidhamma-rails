"""Builder for the Russian rails translation of pi-2 (Vibhaṅga, plain audience), chapters 7, 8 and 9
(Satipaṭṭhānavibhaṅgo ^2-7-0 … ^2-389, Sammappadhānavibhaṅgo ^2-8-0 … ^2-430, Iddhipādavibhaṅgo ^2-9-0 … ^2-465).

Writes (only when run as a script):
  AI_translation/russian/pi-2-russian-plain-rails_split_chapters/7-satipatthanavibhango.md
  AI_translation/russian/pi-2-russian-plain-rails_split_chapters/8-sammappadhanavibhango.md
  AI_translation/russian/pi-2-russian-plain-rails_split_chapters/9-iddhipadavibhango.md
  0-INBOX/temp/pipeline/pi-2-ru/rails/notes-7-9.md   (new recurring formulas, Pāli = Russian)

Every Russian string comes from the fixed tables and functions below, so identical Pāli gives identical Russian.
Imported read-only: the approved sample builder (S), the chapter-1 builder (K1: matrix items, question helpers), the
chapters 2-3 builder (K23: the question-section sentence engine, the body-part lists of ch. 3, the pi-1 feeling and
citta strings), the chapters 4-5 builder (K45: the four right efforts, the satipaṭṭhāna formula, the supramundane
path opener, the pi-1 wisdom / energy / concentration lists, subjectless question sentences) and the chapter-6 builder
(K6: «Поэтому это называется:», the supramundane jhāna pieces, the Tasseva … vipākaṃ opener, the greed and grief
definitions). Their tables are extended only in memory, here.

The question sections of chapters 7-9 write «na vattabbā X ti» without the dash of chapters 1-5: the Russian drops
the dash too («Нельзя определить как «…»») under the dash rule.

usage: python -I -X utf8 build_rails_7_9_ru.py
"""
import pathlib
import re
import sys

RAILS = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-ru\rails")
sys.path.insert(0, str(RAILS))
import build_rails_sample_ru as S  # noqa: E402  (importing writes nothing)
import build_rails_1_ru as K1      # noqa: E402  (importing writes nothing)
import build_rails_2_3_ru as K23   # noqa: E402  (importing writes nothing)
import build_rails_4_5_ru as K45   # noqa: E402  (importing writes nothing)
import build_rails_6_ru as K6      # noqa: E402  (importing writes nothing)

PARTS = {7: "7-satipatthanavibhango.md", 8: "8-sammappadhanavibhango.md", 9: "9-iddhipadavibhango.md"}
NOTES_PATH = RAILS / "notes-7-9.md"
cap, low, q = S.cap, K1.low, K23.q
SLIPS = []


def slip(msg):
    if msg not in SLIPS:
        SLIPS.append(msg)


def strip_var(s):
    return re.sub(r" \[[^\]]*\]", "", s)


# =========================================================================== shared strings (imported)
MONK = K45.MONK                        # Idha bhikkhu = Здесь монах
CONTEMPL = K45.CONTEMPL                # ātāpī sampajāno satimā vineyya loke abhijjhādomanassaṃ
EFFORT = K45.EFFORT                    # chandaṃ janeti vāyamati vīriyaṃ ārabhati cittaṃ paggaṇhāti padahati
TENA = K6.TENA                         # Tena vuccati "…"ti = Поэтому это называется: «…».
PATH_TAIL = K45.PATH_TAIL              # maggaṅgaṃ maggapariyāpannaṃ
TOGETHER = K23.TOGETHER                # tadekajjhaṃ abhisaññūhitvā abhisaṅkhipitvā
KH4 = K6.KH4                           # vedanākkhandho … viññāṇakkhandho (lower case)
CONTACT_PE = K6.CONTACT_PE             # phasso hoti…pe… avikkhepo hoti
HOW = "И как монах"                    # Kathañca bhikkhu …?
ALL_THIS = "Это благие явления."       # Ime dhammā kusalā. (pi-1 «– это благие явления» without the dash)
SUPRA_OPEN = "В то время, когда здесь монах развивает "     # Idha bhikkhu yasmiṃ samaye … (K45.SUPRA_HEAD frame)
TASSEVA_OPEN = ("Вследствие того же совершённого и развитого надмирского благого медитативного погружения, в "
                "качестве его результата, когда кто-либо, ")   # K6.TASSEVA frame
AT_TIME = K6.AT_TIME                   # tasmiṃ samaye = в это время
WHAT_AT_TIME = "то, что в это время есть"   # yo / yā / yaṃ tasmiṃ samaye …


def supra(field=""):
    """the supramundane first-jhāna opener (K6 pieces); field = «в теле созерцая тело, » …"""
    return f"{SUPRA_OPEN}{K6.SUPRA}{K6.J1_SUPRA.format(s=field)}"


def tasseva(field=""):
    return f"{TASSEVA_OPEN}{K6.J1_SUPRA.format(s='пустое, ' + field)}"


# =========================================================================== the four foundations of mindfulness
FIELD = {  # Pāli locative + Xānupassī -> «в теле созерцая тело»
    "kāye kāyānupassī": "в теле созерцая тело", "vedanāsu vedanānupassī": "в чувствах созерцая чувства",
    "citte cittānupassī": "в уме созерцая ум", "dhammesu dhammānupassī": "в явлениях созерцая явления",
}
OBJ_KEY = {"kāye": "kāya", "vedanāsu": "vedanā", "citte": "citta", "dhammesu": "dhamma"}
# ajjhattaṃ / bahiddhā / ajjhattabahiddhā + locative: «во внутреннем теле», … (termbase: внутреннее тело …)
LOC = {
    ("ajjhattaṃ", "kāya"): "во внутреннем теле", ("bahiddhā", "kāya"): "во внешнем теле",
    ("ajjhattabahiddhā", "kāya"): "во внутреннем и внешнем теле",
    ("ajjhattaṃ", "vedanā"): "во внутренних чувствах", ("bahiddhā", "vedanā"): "во внешних чувствах",
    ("ajjhattabahiddhā", "vedanā"): "во внутренних и внешних чувствах",
    ("ajjhattaṃ", "citta"): "во внутреннем уме", ("bahiddhā", "citta"): "во внешнем уме",
    ("ajjhattabahiddhā", "citta"): "во внутреннем и внешнем уме",
    ("ajjhattaṃ", "dhamma"): "во внутренних явлениях", ("bahiddhā", "dhamma"): "во внешних явлениях",
    ("ajjhattabahiddhā", "dhamma"): "во внутренних и внешних явлениях",
}
SEEN = {"kāya": "созерцая тело", "vedanā": "созерцая чувства", "citta": "созерцая ум", "dhamma": "созерцая явления"}
TARGET = {  # … cittaṃ upasaṃharati = он направляет ум на …
    ("bahiddhā", "kāya"): "на внешнее тело", ("ajjhattabahiddhā", "kāya"): "на внутреннее и внешнее тело",
    ("bahiddhā", "vedanā"): "на внешние чувства", ("ajjhattabahiddhā", "vedanā"): "на внутренние и внешние чувства",
    ("bahiddhā", "citta"): "на внешний ум", ("ajjhattabahiddhā", "citta"): "на внутренний и внешний ум",
    ("bahiddhā", "dhamma"): "на внешние явления", ("ajjhattabahiddhā", "dhamma"): "на внутренние и внешние явления",
}
NIMITTA = "Он практикует этот признак, развивает его, многократно повторяет и хорошо устанавливает его."
NIMITTA_THEN = ("Попрактиковав этот признак, развив его, многократно повторив и хорошо установив его, он направляет "
                "ум {t}.")
SATIP4 = "Четыре основы осознанности"     # Cattāro satipaṭṭhānā

# body parts: the ch. 3 earth and water lists (K23.LISTS) in the order of the text
BODY32_V = f"{K23.LISTS['pathavī_i']}, {K23.LISTS['āpo_i']}"
BODY32 = strip_var(BODY32_V)
BODY_SCAN = ("от подошв ног вверх и от кончиков волос на голове вниз, ограниченное кожей, полное разного рода "
             "нечистоты,")   # uddhaṃ pādatalā adho kesamatthakā tacapariyantaṃ pūraṃ nānappakārassa asucino
BODY_OBJ = {"ajjhattaṃ": "внутреннее тело", "bahiddhā": "внешнее тело", "ajjhattabahiddhā": "внутреннее и внешнее тело"}
IN_BODY = {"atthi imasmiṃ kāye": "Есть в этом теле", "atthissa kāye": "Есть в его теле"}

# feelings
FEEL_BASE = {"sukhaṃ": "приятное чувство", "dukkhaṃ": "болезненное чувство", "adukkhamasukhaṃ": S.ADM}
FEEL_PRE = {"": "", "sāmisaṃ": "плотское ", "nirāmisaṃ": "неплотское "}

# minds: (attribute, predicate)
MIND = {
    "sarāgaṃ": ("охваченный страстью", "охвачен страстью"), "vītarāgaṃ": ("свободный от страсти", "свободен от страсти"),
    "sadosaṃ": ("охваченный злобой", "охвачен злобой"), "vītadosaṃ": ("свободный от злобы", "свободен от злобы"),
    "samohaṃ": ("охваченный заблуждением", "охвачен заблуждением"),
    "vītamohaṃ": ("свободный от заблуждения", "свободен от заблуждения"),
    "saṃkhittaṃ": ("сжатый", "сжат"), "vikkhittaṃ": ("рассеянный", "рассеян"),
    "mahaggataṃ": ("возвышенный", "возвышен"), "amahaggataṃ": ("невозвышенный", "невозвышен"),
    "sauttaraṃ": ("имеющий над собой высшее", "имеет над собой высшее"),
    "anuttaraṃ": ("не имеющий над собой высшего", "не имеет над собой высшего"),
    "samāhitaṃ": ("сосредоточенный", "сосредоточен"), "asamāhitaṃ": ("несосредоточенный", "несосредоточен"),
    "vimuttaṃ": ("освобождённый", "освобождён"), "avimuttaṃ": ("неосвобождённый", "неосвобождён"),
}


def mind_attr(a):
    return f"{a} ум" if " " not in a else f"ум, {a}"


# phenomena: hindrances and factors of awakening: (nominative = accusative, genitive, gender, termbase)
BOJJH = {"sati": "осознанности", "dhammavicaya": "исследования явлений", "vīriya": "усердия", "pīti": "восторга",
         "passaddhi": "безмятежности", "samādhi": "сосредоточения", "upekkhā": "невозмутимости"}
DH_NOUN = {
    "kāmacchand": ("чувственное желание", "чувственного желания", "n"),
    "byāpād": ("недоброжелательность", "недоброжелательности", "f"),
    "thinamiddh": ("вялость и сонливость", "вялости и сонливости", "p"),
    "uddhaccakukkucc": ("беспокойство и угрызения", "беспокойства и угрызений", "p"),
    "vicikicch": ("колебание", "колебания", "n"),
}
for _k, _g in BOJJH.items():
    DH_NOUN[f"{_k}sambojjhaṅg"] = (f"фактор пробуждения {_g}", f"фактора пробуждения {_g}", "m")
EXIST = {"m": "имеющийся", "n": "имеющееся", "f": "имеющуюся", "p": "имеющиеся"}      # santaṃ (termbase «есть»)
ABSENT = {"m": "отсутствующий", "n": "отсутствующее", "f": "отсутствующую", "p": "отсутствующие"}
INNER_ACC = {"m": "внутренний", "n": "внутреннее", "f": "внутреннюю", "p": "внутренние"}
INNER_NOM = {"m": "внутренний", "n": "внутреннее", "f": "внутренняя", "p": "внутренние"}
INNER_GEN = {"m": "внутреннего", "n": "внутреннего", "f": "внутренней", "p": "внутренних"}
YATHA = {  # yathā ca <participle> X <event> tañca pajānāti
    "uppādo hoti": "понимает и то, как происходит возникновение {p} {x}",
    "pahānaṃ hoti": "понимает и то, как происходит устранение {p} {x}",
    "āyatiṃ anuppādo hoti": "понимает и то, как в будущем не происходит возникновения {p} {x}",
    "bhāvanāya pāripūrī hoti": "понимает и то, как происходит завершённость развития {p} {x}",
}
PTCP_GEN = {"anuppann": "невозникшего", "uppann": "возникшего", "pahīn": "устранённого"}   # m / n genitive

# =========================================================================== definitions (topics, nouns, bodies)
TOPIC = {  # Xti. (the word explained) / Tena vuccati "X"ti
    "anupassī": "Созерцающий", "viharatī": "Пребывает", "ātāpī": "Ревностный", "sampajāno": "Ясно понимающий",
    "satimā": "Осознанный", "vineyya loke abhijjhādomanassa": "Устранив алчность и уныние в отношении мира",
    "chandaṃ janetī": "Порождает желание", "vāyamatī": "Прилагает усилие", "vīriyaṃ ārabhatī": "Пробуждает усердие",
    "cittaṃ paggaṇhātī": "Напрягает ум", "padahatī": "Прилагает старания", "ṭhitiyā": "Ради сохранения",
    "iddhī": "Сверхспособность", "iddhipādo": "Основа сверхспособностей",
    "iddhipādaṃ bhāvetī": "Развивает основу сверхспособностей",
}
SAMADHI_THROUGH = {"chanda": "желание", "vīriya": "усердие", "citta": "ум", "vīmaṃsā": "пытливость"}
for _k, _r in SAMADHI_THROUGH.items():
    TOPIC[f"{_k}samādhipadhānasaṅkhārasamannāgato"] = (f"Наделённый сосредоточением через {_r} и формирующим "
                                                       "фактором усилия")
NOUN = {  # Pāli term -> (nominative, instrumental)
    "anupassanā": ("созерцание", "созерцанием"), "ātāpo": ("ревностность", "ревностностью"),
    "sampajaññaṃ": ("ясное понимание", "ясным пониманием"), "sati": ("осознанность", "осознанностью"),
    "loko": ("мир", "миром"), "abhijjhā": ("алчность", "алчностью"), "domanassaṃ": ("уныние", "унынием"),
    "chando": ("желание", "желанием"), "vāyāmo": ("усилие", "усилием"), "vīriyaṃ": ("усердие", "усердием"),
    "cittaṃ": ("ум", "умом"), "padhānaṃ": ("усилие", "усилием"),
    "sammappadhānaṃ": ("правильное усилие", "правильным усилием"),
    "satipaṭṭhānaṃ": ("основа осознанности", "основой осознанности"),
    "samādhi": ("сосредоточение", "сосредоточением"),
    "padhānasaṅkhāro": ("формирующий фактор усилия", "формирующим фактором усилия"),
    "padhānasaṅkhārā": ("формирующие факторы усилия", "формирующими факторами усилия"),
    "vīmaṃsā": ("пытливость", "пытливостью"),
    "anuppannā pāpakā akusalā dhammā": ("невозникшие дурные неблагие явления", "невозникшими дурными неблагими явлениями"),
    "uppannā pāpakā akusalā dhammā": ("возникшие дурные неблагие явления", "возникшими дурными неблагими явлениями"),
    "anuppannā kusalā dhammā": ("невозникшие благие явления", "невозникшими благими явлениями"),
    "uppannā kusalā dhammā": ("возникшие благие явления", "возникшими благими явлениями"),
}
IDDHIPADA = {"chand": "желание", "vīriy": "усердие", "citt": "ум", "vīmaṃs": "пытливость"}
IDDHIPADA_INS = {"chand": "желанием", "vīriy": "усердием", "citt": "умом", "vīmaṃs": "пытливостью"}
IP = "основа сверхспособностей"
for _k in IDDHIPADA:
    NOUN[f"{_k}iddhipādo"] = (f"{IDDHIPADA[_k]} как {IP}", f"{IDDHIPADA_INS[_k]} как основой сверхспособностей")
for _k, _r in SAMADHI_THROUGH.items():
    NOUN[f"{_k}samādhi"] = (f"сосредоточение через {_r}", f"сосредоточением через {_r}")
DEM_INS = {  # Imāya / Iminā X (upeto hoti …)
    "anupassanāya": "Этим созерцанием", "ātāpena": "Этой ревностностью", "sampajaññena": "Этим ясным пониманием",
    "satiyā": "Этой осознанностью", "vāyāmena": "Этим усилием", "padhānena": "Этим усилием",
}
UPETO = "обладает, вполне обладает, располагает, вполне располагает, обеспечен, оснащён, наделён"
UPETO_PE = "обладает… наделён"
# upeto «обладать», samupeto «вполне обладать», upapanno «обеспеченный», sampanno «оснащённый», samannāgato
# «наделённый» (termbase); upāgato / samupāgato: no entry («располагать» / «вполне располагать», reported)

LISTS = {  # Yo / Yā / Yaṃ <list> = То, что есть <Russian>
    "paññā pajānanā…pe… amoho dhammavicayo sammādiṭṭhi": K45.WISDOM_SHORT,
    "paññā pajānanā…pe… amoho dhammavicayo sammādiṭṭhi dhammavicayasambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ":
        K45.WISDOM_PATH,
    "cetasiko vīriyārambho…pe… sammāvāyāmo": f"{K45.VIRIYA_HEAD}… правильное усилие",
    "cetasiko vīriyārambho…pe… sammāvāyāmo vīriyasambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ":
        f"{K45.VIRIYA_HEAD}… правильное усилие, фактор пробуждения усердия, {PATH_TAIL}",
    ("cetasiko vīriyārambho nikkamo parakkamo uyyāmo vāyāmo ussāho ussoḷhī thāmo ṭhiti asithilaparakkamatā "
     "anikkhittachandatā anikkhittadhuratā dhurasampaggāho vīriyaṃ vīriyindriyaṃ vīriyabalaṃ sammāvāyāmo"):
        f"{K45.VIRIYA_LIST}, правильное усилие",
    "sati anussati…pe… sammāsati": "осознанность, припоминание… правильная осознанность",
    "sati anussati sammāsati satisambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ":
        f"осознанность, припоминание, правильная осознанность, фактор пробуждения осознанности, {PATH_TAIL}",
    "rāgo sārāgo…pe… cittassa sārāgo": "страсть, пристрастие… пристрастие ума",
    ("cetasikaṃ asātaṃ cetasikaṃ dukkhaṃ cetosamphassajaṃ asātaṃ dukkhaṃ vedayitaṃ cetosamphassajā asātā dukkhā "
     "vedanā"): K23.FEELING_P1["domanassa"],
    "chando chandikatā kattukamyatā kusalo dhammacchando":
        "желание, проявление желания, желание действовать, благое стремление к Учению",
    "chando chandikatā [chandīkatā (syā.)] kattukamyatā kusalo dhammacchando":
        ("желание, проявление желания [вариант написания (Syā.): chandīkatā], желание действовать, благое "
         "стремление к Учению"),
    "cittaṃ mano mānasaṃ…pe… tajjāmanoviññāṇadhātu":
        f"{K23.CITTA_SHORT} {K23.TAJJA} {K23.DH['manoviññāṇa']}",
    ("cittassa ṭhiti saṇṭhiti avaṭṭhiti avisāhāro avikkhepo avisāhaṭamānasatā samatho samādhindriyaṃ samādhibalaṃ "
     "sammāsamādhi"): K45.SAMADHI_LIST,
    "cittassa ṭhiti saṇṭhiti…pe… sammāsamādhi": "устойчивость ума, собранность… правильное сосредоточение",
    "cittassa ṭhiti saṇṭhiti…pe… sammāsamādhi samādhisambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ":
        f"устойчивость ума, собранность… правильное сосредоточение, фактор пробуждения сосредоточения, {PATH_TAIL}",
}

# the four right efforts (K45 strings) and their aims
AIM = {
    "anuppannānaṃ pāpakānaṃ akusalānaṃ dhammānaṃ anuppādāya": ("ради невозникновения", "невозникших дурных неблагих явлений"),
    "uppannānaṃ pāpakānaṃ akusalānaṃ dhammānaṃ pahānāya": ("ради устранения", "возникших дурных неблагих явлений"),
    "anuppannānaṃ kusalānaṃ dhammānaṃ uppādāya": ("ради возникновения", "невозникших благих явлений"),
    ("uppannānaṃ kusalānaṃ dhammānaṃ ṭhitiyā asammosāya bhiyyobhāvāya vepullāya bhāvanāya pāripūriyā"):
        ("ради сохранения, неутраты, умножения, обширности, развития и завершённости", "возникших благих явлений"),
}
EFFORT_P = "chandaṃ janeti vāyamati vīriyaṃ ārabhati cittaṃ paggaṇhāti padahati"


def aim(p, these=False):
    a, b = AIM[p]
    return f"{a} {'этих ' if these else ''}{b}"


AIM_RX = "(" + "|".join(re.escape(k) for k in sorted(AIM, key=len, reverse=True)) + ")"
SAMMAP4 = "Четыре правильных усилия"      # Cattāro sammappadhānā
IDDHIP4 = "Четыре основы сверхспособностей"   # Cattāro iddhipādā


def ip_acc(k):
    """Xsamādhipadhānasaṅkhārasamannāgataṃ iddhipādaṃ"""
    return (f"основу сверхспособностей, наделённую сосредоточением через {SAMADHI_THROUGH[k]} и формирующим фактором "
            "усилия")


ADHIPATI = {  # Xṃ ce bhikkhu adhipatiṃ karitvā (karitvā «взять», adhipatiṃ «главенствующий»)
    "Chandaṃ": "взяв желание как главенствующее", "Vīriyaṃ": "взяв усердие как главенствующее",
    "Cittaṃ": "взяв ум как главенствующий", "Vīmaṃsaṃ": "взяв пытливость как главенствующую",
}
ADHIPATI_K = {"Chandaṃ": "chanda", "Vīriyaṃ": "vīriya", "Cittaṃ": "citta", "Vīmaṃsaṃ": "vīmaṃsā"}
ITI_INS = {"iminā ca chandena": "этим желанием", "iminā ca vīriyena": "этим усердием",
           "iminā ca cittena": "этим умом", "imāya ca vīmaṃsāya": "этой пытливостью"}
IDDHI_DEF = ("То, что у этих явлений есть сверхспособность, успех, преуспевание, полное преуспевание, обретение, "
             "получение, достижение, полное достижение, касание, непосредственное постижение, вхождение.")
TATHA = "У того, кто стал таким:"     # Tathābhūtassa (bhūtaṃ «ставший», sample)
VINITA = ("Итак, эта алчность и это уныние в этом мире устранены, полностью устранены, успокоены, усмирены, "
          "умиротворены, угасли, полностью угасли, прекращены, полностью прекращены, иссушены, полностью иссушены, "
          "сведены на нет.")
FIVE_LOKO = "Пять совокупностей, служащих объектом цепляния, тоже являются миром"   # Pañcapi upādānakkhandhā loko
UPEKKHA_THIS = {"Sveva kāyo loko.": "Это самое тело является миром.",
                "Sāyeva vedanā loko.": "Это самое чувство является миром.",
                "Taṃyeva cittaṃ loko.": "Этот самый ум является миром.",
                "Teva dhammā loko.": "Эти самые явления являются миром."}
ROOTS_A = "Три неблагих корня – жадность, злоба, заблуждение."                 # pi-1 ^1-986
ROOTS_K = "Три благих корня – отсутствие жадности, отсутствие злобы, отсутствие заблуждения."   # pi-1 ^1-985
TADEKATTHA = "И омрачения, пребывающие вместе с ними."                         # pi-1 ^1-986
SAMPAY = f"Связанные с ними {KH4}"                                              # pi-1 ^1-985
SAMUTTH = "порождённые ими телесное действие, речевое действие и умственное действие"   # pi-1 ^1-985
THITI_CHAIN = ("Сохранение является неутратой, неутрата является умножением, умножение является обширностью, "
               "обширность является развитием, развитие является завершённостью.")

SUBHEAD = {
    "Kāyānupassanāniddeso": "Разъяснение созерцания тела", "Vedanānupassanāniddeso": "Разъяснение созерцания чувств",
    "Cittānupassanāniddeso": "Разъяснение созерцания ума", "Dhammānupassanāniddeso": "Разъяснение созерцания явлений",
}
for _k in IDDHIPADA:
    SUBHEAD[f"{cap(_k)}iddhipādo"] = cap(NOUN[f"{_k}iddhipādo"][0])

SENT = {
    "Suttantabhājanīyaṃ.": f"{S.SUTTANTA_BH}.", "Abhidhammabhājanīyaṃ.": f"{S.ABHI_BH}.",
    "Pañhāpucchakaṃ.": f"{S.PANHA}.",
    "Satipaṭṭhānavibhaṅgo niṭṭhito.": f"{S.CH_TITLE[7][1]} {S.DONE}.",
    "Sammappadhānavibhaṅgo niṭṭhito.": f"{S.CH_TITLE[8][1]} {S.DONE}.",
    "Iddhipādavibhaṅgo niṭṭhito.": f"{S.CH_TITLE[9][1]} {S.DONE}.",
    "Ime dhammā kusalā.": ALL_THIS,
    "Iriyati vattati pāleti yapeti yāpeti carati viharati.":
        ("Принимает положения тела, живёт, оберегает себя, поддерживает себя, продлевает существование, действует, "
         "пребывает."),
    "So taṃ nimittaṃ āsevati bhāveti bahulīkaroti svāvatthitaṃ vavatthapeti.": NIMITTA,
    "Pañcapi upādānakkhandhā loko.": f"{FIVE_LOKO}.",
    ("Iti ayañca abhijjhā idañca domanassaṃ imamhi loke vinītā honti paṭivinītā santā samitā vūpasantā atthaṅgatā "
     "abbhatthaṅgatā appitā byappitā sositā visositā byantīkatā."): VINITA,
    "Tīṇi akusalamūlāni – lobho, doso, moho.": ROOTS_A,
    "Tīṇi kusalamūlāni – alobho, adoso, amoho.": ROOTS_K,
    "Tadekaṭṭhā ca kilesā.": TADEKATTHA,
    "Taṃsampayutto vedanākkhandho, saññākkhandho, saṅkhārakkhandho, viññāṇakkhandho.": f"{SAMPAY}.",
    ("Imaṃ chandaṃ janeti sañjaneti uṭṭhapeti samuṭṭhapeti [uṭṭhāpeti samuṭṭhāpeti (syā.) evamuparipi] nibbatteti "
     "abhinibbatteti."):
        ("Это желание он порождает, полностью порождает, поднимает, полностью поднимает [вариант написания (Syā.): "
         "uṭṭhāpeti samuṭṭhāpeti, так же и далее], вызывает, полностью вызывает."),
    "Imaṃ chandaṃ janeti sañjaneti uṭṭhapeti samuṭṭhapeti nibbatteti abhinibbatteti.":
        "Это желание он порождает, полностью порождает, поднимает, полностью поднимает, вызывает, полностью вызывает.",
    "Imaṃ vīriyaṃ ārabhati samārabhati āsevati bhāveti bahulīkaroti.":
        "Это усердие он пробуждает, полностью пробуждает, практикует, развивает, многократно повторяет.",
    "Imaṃ cittaṃ paggaṇhāti sampaggaṇhāti upatthambheti paccupatthambheti.":
        "Этот ум он напрягает, полностью напрягает, поддерживает, всячески поддерживает.",
    ("Ṭhitiyāti. Yā ṭhiti so asammoso, yo asammoso so bhiyyobhāvo, yo bhiyyobhāvo taṃ vepullaṃ, yaṃ vepullaṃ sā "
     "bhāvanā, yā bhāvanā sā pāripūrī."): f"«{TOPIC['ṭhitiyā']}». {THITI_CHAIN}",
    "Ime vuccanti \"padhānasaṅkhārā\".": f"Это называется «{NOUN['padhānasaṅkhārā'][1]}».",
    ("Yā tesaṃ dhammānaṃ iddhi samiddhi ijjhanā samijjhanā lābho paṭilābho patti sampatti phusanā sacchikiriyā "
     "upasampadā."): IDDHI_DEF,
    "Tathābhūtassa vedanākkhandho, saññākkhandho, saṅkhārakkhandho, viññāṇakkhandho.": f"{TATHA} {KH4}.",
    "Tathābhūtassa vedanākkhandho…pe… viññāṇakkhandho.": f"{TATHA} совокупность чувств… совокупность сознания.",
    "Tathābhūtassa phasso…pe… paggāho avikkhepo.": f"{TATHA} контакт… напряжение сил, отсутствие отвлечения.",
    "Te dhamme āsevati bhāveti bahulīkaroti.": "Эти явления он практикует, развивает, многократно повторяет.",
    "Cattāro iddhipādā – chandiddhipādo, vīriyiddhipādo, cittiddhipādo, vīmaṃsiddhipādo.":
        f"{IDDHIP4} – " + K45.nlist([NOUN[f'{k}iddhipādo'][0] for k in IDDHIPADA]) + ".",
}
SENT.update(UPEKKHA_THIS)
for _p, _r in SUBHEAD.items():
    SENT[f"{_p}."] = f"{_r}."
SENT_SLIP = {  # source slips: (as meant, note)
    "Tathābhūtassa vedanākkhandho, saññākkhandho, saṅkhārakkhandho, viññāṇakhandho.":
        ("Tathābhūtassa vedanākkhandho, saññākkhandho, saṅkhārakkhandho, viññāṇakkhandho.",
         "^2-443 «viññāṇakhandho» (single k; viññāṇakkhandho elsewhere, both in the termbase): same Russian"),
    "Tathābhūtasa phasso…pe… paggāho avikkhepo.":
        ("Tathābhūtassa phasso…pe… paggāho avikkhepo.",
         "^2-450 «Tathābhūtasa» (for Tathābhūtassa): rendered as meant"),
}


# =========================================================================== sentence engine
def topic(raw):
    """Anupassīti / "Iddhipādo"ti / vineyya loke abhijjhādomanassanti -> Russian (capitalised)"""
    t = raw.strip()
    t = re.sub(r'"?n?ti$', "", t).strip('"')
    return TOPIC[low(t)]


def body_ru(b):
    m = re.match(r"^(Yo|Yā|Yaṃ) (.*)$", b)
    if m and m.group(2) in LISTS:
        return f"То, что есть {LISTS[m.group(2)]}", True
    if b == ("Taṃsampayutto vedanākkhandho, saññākkhandho, saṅkhārakkhandho, viññāṇakkhandho, taṃsamuṭṭhānaṃ "
             "kāyakammaṃ vacīkammaṃ manokammaṃ"):
        return f"{SAMPAY}; {SAMUTTH}", False
    if b == "Taṃsamuṭṭhānaṃ kāyakammaṃ, vacīkammaṃ, manokammaṃ":
        return cap(SAMUTTH), False
    m = re.match(r"^(Chandaṃ|Vīriyaṃ|Cittaṃ|Vīmaṃsaṃ) ce bhikkhu adhipatiṃ karitvā labhati samādhiṃ,? labhati "
                 r"cittassekaggataṃ( \[cittassa ekaggataṃ \(sī\. syā\.\)\])?$", b)
    if m:
        v = " [вариант написания (Sī., Syā.): cittassa ekaggataṃ]" if m.group(2) else ""
        return (f"Если монах, {ADHIPATI[m.group(1)]}, обретает сосредоточение, обретает однонаправленность ума{v}",
                True)
    raise KeyError(b)


def called(raw, sid):
    t = raw.strip()
    quoted = t.startswith('"') and t.endswith('"')
    t = t.strip('"')
    ins = NOUN[t][1]
    if not quoted:
        slip(f"^{sid} «… vuccati {t}» without quotation marks: rendered without «»")
        return f"это называется {ins}."
    return f"это называется «{ins}»."


def sentence(s, sid):
    if s in SENT_SLIP:
        s2, note = SENT_SLIP[s]
        slip(note)
        s = s2
    if s in SENT:
        return SENT[s]
    s = s.replace("kāmehi …pe…", "kāmehi…pe…").replace("vīriyārambho …pe…", "vīriyārambho…pe…")
    if s in SENT:
        return SENT[s]
    # ---- topic lines (one or a …pe… run)
    if re.match(r'^"?[A-ZĀĪŪṬ][^?]*?"?n?ti\.$', s) and " vuccati " not in s:
        parts = [p.strip() for p in s[:-1].split("…pe…")]
        if all(low(re.sub(r'"?n?ti$', "", p).strip('"')) in TOPIC for p in parts):
            out = [topic(p) for p in parts]
            return "«" + "»… «".join([out[0]] + [low(x) for x in out[1:]]) + "»."
    # ---- Tena vuccati
    m = re.match(r'^Tena vuccati (".*"n?ti)\.$', s)
    if m:
        return f"{TENA} «{topic(m.group(1))}»."
    # ---- questions
    m = re.match(r"^Tattha katam(?:o|ā|aṃ|e) (.+?)( \[katamaṃ ātāpaṃ \(sabbattha\)\])?\?$", s)
    if m:
        v = " [вариант чтения (во всех изданиях): katamaṃ ātāpaṃ]" if m.group(2) else ""
        return f"Что такое {S.TATTHA} {NOUN[m.group(1)][0]}{v}?"
    m = re.match(r"^Kathañca bhikkhu (?:(ajjhattaṃ|bahiddhā|ajjhattabahiddhā) )?(kāye|vedanāsu|citte|dhammesu) "
                 r"(\S+)ānupassī viharati\?$", s)
    if m:
        o = OBJ_KEY[m.group(2)]
        f = f"{LOC[(m.group(1), o)]} {SEEN[o]}" if m.group(1) else FIELD[f"{m.group(2)} {m.group(3)}ānupassī"]
        return f"{HOW} пребывает, {f}?"
    m = re.match(rf"^Kathañca bhikkhu {AIM_RX} {EFFORT_P}\?$", s)
    if m:
        return f"{HOW} {aim(m.group(1))} {EFFORT}?"
    m = re.match(r"^Kathañca bhikkhu (chanda|vīriya|citta|vīmaṃsā)samādhipadhānasaṅkhārasamannāgataṃ iddhipādaṃ "
                 r"bhāveti\?$", s)
    if m:
        return f"{HOW} развивает {ip_acc(m.group(1))}?"
    # ---- answers «<body> – ayaṃ vuccati "X".»
    m = re.match(r'^(.*) – (?:ayaṃ|idaṃ|ime) (?:vuccati|vuccanti) (.+)\.$', s)
    if m and not s.startswith("Idha bhikkhu yasmiṃ samaye") and not s.startswith("Tasseva"):
        ru, comma = body_ru(m.group(1))
        return f"{ru}{',' if comma else ''} – {called(m.group(2), sid)}"
    m = re.match(r'^(?:Ayaṃ|Idaṃ) vuccati (.+)\.$', s)
    if m:
        return cap(called(m.group(1), sid))
    m = re.match(r'^Avasesā dhammā (\S+)sampayuttā\.$', s)
    if m:
        return f"Остальные явления связаны с {NOUN[_sampay_key(m.group(1))][1]}."
    # ---- upeto hoti …
    m = re.match(r"^(Imāya|Iminā) (\S+) upeto hoti( samupeto upāgato samupāgato upapanno sampanno samannāgato|"
                 r"…pe… samannāgato)\.$", s)
    if m:
        return f"{DEM_INS[m.group(2)]} он {UPETO if 'samupeto' in m.group(3) else UPETO_PE}."
    m = re.match(r"^Iti (iminā ca chandena|iminā ca vīriyena|iminā ca cittena|imāya ca vīmaṃsāya), iminā ca "
                 r"samādhinā, iminā ca padhānasaṅkhārena upeto hoti( samupeto upāgato samupāgato upapanno sampanno "
                 r"samannāgato|…pe… samannāgato)\.$", s)
    if m:
        u = UPETO if "samupeto" in m.group(2) else UPETO_PE
        return f"Итак, {ITI_INS[m.group(1)]}, этим сосредоточением и этим формирующим фактором усилия он {u}."
    # ---- the world
    m = re.match(r"^Pañcapi upādānakkhandhā loko – tattha katamā abhijjhā\?$", s)
    if m:
        slip(f"^{sid} «Pañcapi upādānakkhandhā loko – tattha katamā abhijjhā?»: «Ayaṃ vuccati \"loko\".» missing "
             "and a dash before the next question (translated as written)")
        return f"{FIVE_LOKO} – что такое {S.TATTHA} {NOUN['abhijjhā'][0]}?"
    # ---- right efforts
    m = re.match(rf"^Iti imesaṃ {AIM_RX} {EFFORT_P}\.$", s)
    if m:
        return f"Итак, {aim(m.group(1), these=True)} он {EFFORT}."
    m = re.match(r"^(Cattāro sammappadhānā – idha bhikkhu|So) (.*)\.$", s)
    if m and EFFORT_P in s:
        head = f"{SAMMAP4} – здесь монах" if m.group(1) != "So" else "Он"
        return f"{head} {efforts(m.group(2))}."
    # ---- bases of power
    m = re.match(r"^Iti ayañca (chanda|vīriya|citta|vīmaṃsā)samādhi, ime ca padhānasaṅkhārā([.;])(.*)$", s)
    if m:
        k = m.group(1)
        first = f"Итак, это {NOUN[k + 'samādhi'][0]} и эти {NOUN['padhānasaṅkhārā'][0]}"
        if m.group(2) == ".":
            assert m.group(3) == ""
            return first + "."
        return f"{first}; {low(together(m.group(3).strip(), k))}"
    m = re.match(r"^Tadekajjhaṃ .*$", s)
    if m:
        k = re.search(r"(chanda|vīriya|citta|vīmaṃsā)samādhipadhānasaṅkhārotveva", s).group(1)
        return together(s, k)
    m = re.match(r"^Cattāro iddhipādā – idha bhikkhu (.*)\.$", s)
    if m:
        return f"{IDDHIP4} – здесь монах {iddhi_list(m.group(1))}."
    # ---- the four foundations of mindfulness: summary lines
    m = re.match(r"^Cattāro satipaṭṭhānā – idha bhikkhu (.*)\.$", s)
    if m:
        return f"{SATIP4} – здесь монах {satip_list(m.group(1))}."
    # ---- the supramundane opener
    r = supra_sentence(s, sid)
    if r:
        return r
    raise KeyError(s)


def _sampay_key(p):
    """satipaṭṭhāna / sammappadhāna / chandiddhipāda … (compound member) -> NOUN key"""
    for k in NOUN:
        if k in (p + "ṃ", p[:-1] + "o", p):
            return k
    raise KeyError(p)


def together(s, k):
    m = re.match(r"^[Tt]adekajjhaṃ (abhisaññahitvā|abhisaññūhitvā) abhisaṅkhipitvā (chanda|vīriya|citta|vīmaṃsā)"
                 r"samādhipadhānasaṅkhārotveva saṅkhyaṃ( \[saṅkhaṃ \(sī\.\)\])? gacchati\.$", s)
    assert m and m.group(2) == k, s
    if m.group(1) == "abhisaññahitvā":
        slip("^2-432 «abhisaññahitvā» (abhisaññūhitvā elsewhere; the termbase has both, «собранный воедино»): same "
             "Russian")
    v = " [вариант написания (Sī.): saṅkhaṃ]" if m.group(3) else ""
    name = f"сосредоточение через {SAMADHI_THROUGH[k]} и формирующий фактор усилия"
    return f"{cap(TOGETHER)} получает название{v} «{name}»."


def efforts(body):
    """<aim> chandaṃ janeti …, <aim>…pe… <aim> chandaṃ janeti … (the four right efforts)"""
    out = []
    rest = body
    while rest:
        m = re.match(rf"^{AIM_RX}(?: {EFFORT_P}(?:, )?|…pe… )", rest)
        assert m, rest
        full = m.group(0).startswith(m.group(1) + " " + EFFORT_P)
        out.append((aim(m.group(1)), full))
        rest = rest[m.end():]
    res = ""
    for i, (a, full) in enumerate(out):
        piece = f"{a} {EFFORT}" if full else a
        if i == 0:
            res = piece
        else:
            res += ("; " if out[i - 1][1] else "… ") + piece
    return res


def iddhi_list(body):
    """Xsamādhipadhānasaṅkhārasamannāgataṃ iddhipādaṃ bhāveti, … (with …pe… runs)"""
    toks = re.split(r"(, |…pe… )", body)
    res = ""
    for i in range(0, len(toks), 2):
        t = toks[i]
        sep = toks[i - 1] if i else ""
        m = re.match(r"^(chanda|vīriya|citta|vīmaṃsā)samādhipadhānasaṅkhārasamannāgataṃ iddhipādaṃ bhāveti$", t)
        if m:
            piece = f"развивает {ip_acc(m.group(1))}"
        else:
            m = re.match(r"^(chanda|vīriya|citta|vīmaṃsā)samādhi$", t)
            assert m, t
            piece = f"наделённую сосредоточением через {SAMADHI_THROUGH[m.group(1)]}"
        res += ("" if not i else ("; " if sep == ", " else "… ")) + piece
    return res


def satip_list(body):
    """kāye kāyānupassī viharati [ātāpī …], vedanāsu … (the summary of the four foundations)"""
    out = []
    for grp in body.split(", "):
        m = re.match(r"^(?:(ajjhattaṃ|bahiddhā|ajjhattabahiddhā) )?(kāye|vedanāsu|citte|dhammesu) (\S+)ānupassī viharati"
                     r"(.*)$", grp)
        assert m, grp
        pieces = []
        rest = grp
        while rest:
            m = re.match(r"^(?:(ajjhattaṃ|bahiddhā|ajjhattabahiddhā) )?(kāye|vedanāsu|citte|dhammesu) (\S+)ānupassī "
                         r"viharati ?", rest)
            if not m:
                break
            o = OBJ_KEY[m.group(2)]
            f = f"{LOC[(m.group(1), o)]} {SEEN[o]}" if m.group(1) else FIELD[f"{m.group(2)} {m.group(3)}ānupassī"]
            pieces.append(f"пребывает, {f}")
            rest = rest[m.end():]
        tail = ""
        if rest:
            assert rest == "ātāpī sampajāno satimā vineyya loke abhijjhādomanassaṃ", rest
            tail = f", {CONTEMPL}"
        out.append(", ".join(pieces) + tail)
    return "; ".join(out)


SUPRA_P = ("Idha bhikkhu yasmiṃ samaye lokuttaraṃ jhānaṃ bhāveti niyyānikaṃ apacayagāmiṃ diṭṭhigatānaṃ pahānāya "
           "paṭhamāya bhūmiyā pattiyā vivicceva kāmehi…pe… paṭhamaṃ jhānaṃ upasampajja viharati dukkhapaṭipadaṃ "
           "dandhābhiññaṃ")
TASSEVA_P = ("Tasseva lokuttarassa kusalassa jhānassa katattā bhāvitattā vipākaṃ vivicceva kāmehi…pe… paṭhamaṃ jhānaṃ "
             "upasampajja viharati dukkhapaṭipadaṃ dandhābhiññaṃ suññataṃ")
FIELD_RX = r"(?: (kāye kāyānupassī|vedanāsu vedanānupassī|citte cittānupassī|dhammesu dhammānupassī))?"


def supra_tail(rest, sid):
    """the part after «…dandhābhiññaṃ[ field], »"""
    m = re.match(r"^tasmiṃ samaye phasso hoti…pe… avikkhepo hoti\.$", rest)
    if m:
        return f", {AT_TIME} {CONTACT_PE}."
    m = re.match(rf"^tasmiṃ samaye {AIM_RX} {EFFORT_P}\.$", rest)
    if m:
        return f", {AT_TIME} {aim(m.group(1))} {EFFORT}."
    m = re.match(r"^tasmiṃ samaye (chanda|vīriya|citta|vīmaṃsā)samādhipadhānasaṅkhārasamannāgataṃ iddhipādaṃ "
                 r"bhāveti\.$", rest)
    if m:
        return f", {AT_TIME} развивает {ip_acc(m.group(1))}."
    m = re.match(r'^(?:yo|yā|yaṃ) tasmiṃ samaye (.*?) – (?:idaṃ|ayaṃ) vuccati (.+)\.$', rest)
    if m:
        lst = m.group(1)
        if "maggariyāpannaṃ" in lst:
            slip(f"^{sid} «maggariyāpannaṃ» (for maggapariyāpannaṃ): rendered as meant")
            lst = lst.replace("maggariyāpannaṃ", "maggapariyāpannaṃ")
        return f", {WHAT_AT_TIME} {LISTS[lst]}, – {called(m.group(2), sid)}"
    raise KeyError(rest)


def supra_sentence(s, sid):
    m = re.match(rf"^{re.escape(SUPRA_P)}{FIELD_RX}, (.*)$", s)
    if m:
        f = FIELD[m.group(1)] + ", " if m.group(1) else ""
        return supra(f) + supra_tail(m.group(2), sid)
    m = re.match(rf"^{re.escape(TASSEVA_P)}{FIELD_RX}, (.*)$", s)
    if m:
        f = FIELD[m.group(1)] + ", " if m.group(1) else ""
        return tasseva(f) + supra_tail(m.group(2), sid)
    return None


# =========================================================================== the long contemplation lines
def split_sents(line):
    return K45.split_sents(line)


def kaya_sentence(s):
    m = re.match(r'^Idha bhikkhu (ajjhattaṃ|bahiddhā|ajjhattabahiddhā) kāyaṃ uddhaṃ pādatalā adho kesamatthakā '
                 r'tacapariyantaṃ pūraṃ nānappakārassa asucino paccavekkhati – "(atthi imasmiṃ kāye|atthissa kāye) '
                 r'(.*)"nti\.$', s)
    if not m:
        return None
    lst = m.group(3)
    plain = ("kesā lomā nakhā dantā taco maṃsaṃ nhāru aṭṭhi aṭṭhimiñjaṃ vakkaṃ hadayaṃ yakanaṃ kilomakaṃ pihakaṃ "
             "papphāsaṃ antaṃ antaguṇaṃ udariyaṃ karīsaṃ pittaṃ semhaṃ pubbo lohitaṃ sedo medo assu vasā kheḷo "
             "siṅghāṇikā lasikā mutta")
    if lst == plain:
        ru = BODY32
    else:
        assert lst == plain.replace("nhāru", "nhāru [nahāru (sī.)]").replace("aṭṭhimiñjaṃ",
                                                                           "aṭṭhimiñjaṃ [aṭṭhimiñjā (sī.)]"), lst
        ru = BODY32_V
    return f"{MONK} рассматривает {BODY_OBJ[m.group(1)]} {BODY_SCAN} – «{IN_BODY[m.group(2)]} {ru}»."


def feel_sentence(s):
    m = re.match(r"^Idha bhikkhu (.*) pajānāti\.$", s)
    if not m or "vedanaṃ" not in s:
        return None
    units = m.group(1).split(" pajānāti, ")
    out = []
    for u in units:
        m1 = re.match(r'^(?:(sāmisaṃ|nirāmisaṃ) vā )?(sukhaṃ|dukkhaṃ|adukkhamasukhaṃ) vedanaṃ (vedayamāno|vedayamānaṃ)? ?'
                      r'"(.*)"ti$', u)
        assert m1, u
        pre, base, ptc, quote = m1.groups()
        pre = pre or ""
        ph = f"{FEEL_PRE[pre]}{FEEL_BASE[base]}"
        pp = f"{pre} " if pre else ""
        if ptc == "vedayamāno":
            assert quote == f"{pp}{base} vedanaṃ vedayāmī", u
            out.append(f"испытывая {ph}, понимает: «Я испытываю {ph}»")
        elif ptc == "vedayamānaṃ":
            assert quote == f"{pp}{base} vedanaṃ vedayatī", u
            out.append(f"про того, кто испытывает {ph}, понимает: «Он испытывает {ph}»")
        else:
            fem = {"sukhaṃ": "sukhā", "dukkhaṃ": "dukkhā", "adukkhamasukhaṃ": "adukkhamasukhā"}[base]
            pf = {"": "", "sāmisaṃ": "sāmisā ", "nirāmisaṃ": "nirāmisā "}[pre]
            assert quote == f"{pf}{fem} vedanā", u
            out.append(f"понимает {ph}{',' if ph.endswith(' приятно') else ''} как «{ph}»")
    sep = ", " if out[0].startswith("испытывая") else " "
    return f"{MONK}{sep}" + "; ".join(out) + "."


def mind_sentence(s):
    m = re.match(r"^Idha bhikkhu (.*) pajānāti\.$", s)
    if not m or "cittaṃ" not in s:
        return None
    out = []
    for u in m.group(1).split(" pajānāti, "):
        m1 = re.match(r'^(\S+) (vā|vāssa) cittaṃ "(.*)"nti$', u)
        assert m1, u
        adj, va, quote = m1.groups()
        attr, pred = MIND[adj]
        if va == "vāssa":
            assert quote == adj[:-1] + "massa citta", u
            out.append(f"понимает его {mind_attr(attr)}: «Его ум {pred}»")
        elif quote == f"{adj} me citta":
            out.append(f"понимает {mind_attr(attr)}: «Мой ум {pred}»")
        else:
            assert quote == f"{adj} citta", u
            out.append(f"понимает {mind_attr(attr)}: «Ум {pred}»")
    return f"{MONK} " + "; ".join(out) + "."


def dh_noun(w):
    for k, v in DH_NOUN.items():
        if w.startswith(k):
            return k, v
    raise KeyError(w)


DH_UNIT_RX = re.compile(r'^(santaṃ|asantaṃ) (vā ajjhattaṃ|vāssa|vā) (\S+?)( \[[^\]]+\])?(?: "(.*)"ti pajānāti)?$')
YATHA_RX = re.compile(r"^yathā ca (anuppann|uppann|pahīn)(?:assa|āya) (\S+) (uppādo hoti|pahānaṃ hoti|"
                      r"āyatiṃ anuppādo hoti|bhāvanāya pāripūrī hoti) tañca pajānāti$")
VAR_RU = {"[thīnamiddhaṃ (sī. syā.)]": "[вариант написания (Sī., Syā.): thīnamiddhaṃ]",
          "[viriyasambojjhaṅgaṃ (sī. syā.)]": "[вариант написания (Sī., Syā.): viriyasambojjhaṅgaṃ]"}


def dh_unit(u, after_pe):
    m = DH_UNIT_RX.match(u)
    if m:
        sa, how, w, var, quote = m.groups()
        k, (nom, gen, g) = dh_noun(w)
        v = (" " + VAR_RU[var.strip()]) if var else ""
        ex = (EXIST if sa == "santaṃ" else ABSENT)[g]
        if how == "vā ajjhattaṃ":
            np = f"{ex} {INNER_ACC[g]} {nom}{v}"
            q_ = (f"У меня есть {INNER_NOM[g]} {nom}" if sa == "santaṃ" else f"У меня нет {INNER_GEN[g]} {gen}")
            want = ("atthi" if sa == "santaṃ" else "natthi") + " me ajjhattaṃ "
        elif how == "vāssa":
            np = f"{ex} у него {nom}{v}"
            q_ = f"У него есть {nom}" if sa == "santaṃ" else f"У него нет {gen}"
            want = ("atthissa " if sa == "santaṃ" else "natthissa ")
        else:
            np = f"{ex} {nom}{v}"
            q_ = f"Есть {nom}" if sa == "santaṃ" else f"Нет {gen}"
            want = ("atthi " if sa == "santaṃ" else "natthi ")
        if quote is not None:
            assert quote.startswith(want), (u, want)
            ru = f"{np}: «{q_}»"
        else:
            ru = np
        return ru if after_pe else f"понимает {ru}"
    m = YATHA_RX.match(u)
    assert m, u
    ptc, w, ev = m.groups()
    k, (nom, gen, g) = dh_noun(w)
    assert g in ("m", "n"), u
    return YATHA[ev].format(p=PTCP_GEN[ptc], x=gen)


def dh_sentence(s):
    s0 = s
    start = ""
    if s.startswith("Idha bhikkhu "):
        start, s = MONK + " ", s[len("Idha bhikkhu "):]
    elif s.startswith("Santaṃ "):
        s = "s" + s[1:]
    else:
        return None
    if not s.startswith(("santaṃ ", "asantaṃ ")):
        return None
    assert s.endswith(" pajānāti."), s0
    body = s[:-1]
    toks = re.split(r"(, (?=santaṃ|asantaṃ|yathā)|\s*…pe…\s*)", body)
    out, prev_pe = [], False
    for i in range(0, len(toks), 2):
        sep = toks[i - 1].strip() if i else ""
        piece = dh_unit(toks[i].strip(), sep == "…pe…")
        if i:
            out.append("… " if sep == "…pe…" else "; ")
        out.append(piece)
    ru = "".join(out)
    return (start + ru if start else cap(ru)) + "."


def long_line(ln, sid):
    """a line of the Suttanta contemplation sections (several sentences)"""
    out = []
    for s in split_sents(ln):
        r = (kaya_sentence(s) or feel_sentence(s) or mind_sentence(s) or dh_sentence(s))
        if r is None:
            m = re.match(r"^So taṃ nimittaṃ āsevitvā bhāvetvā bahulīkaritvā svāvatthitaṃ vavatthapetvā "
                         r"(bahiddhā|ajjhattabahiddhā) (kāye|vedanāsu|citte|dhammesu) cittaṃ upasaṃharati\.$", s)
            if m:
                r = NIMITTA_THEN.format(t=TARGET[(m.group(1), OBJ_KEY[m.group(2)])])
        if r is None:
            m = re.match(r"^Evaṃ bhikkhu (ajjhattabahiddhā) (kāye|vedanāsu|citte|dhammesu) \S+ānupassī viharati ātāpī "
                         r"sampajāno satimā vineyya loke abhijjhādomanassaṃ\.$", s)
            if m:
                o = OBJ_KEY[m.group(2)]
                r = f"Так монах пребывает, {LOC[(m.group(1), o)]} {SEEN[o]}, {CONTEMPL}."
        if r is None:
            r = sentence(s, sid)
        out.append(r)
    return " ".join(out)


def def_line(ln, sid):
    if ln in SENT:
        return SENT[ln]
    # a …pe… run of topics followed by a question: split before «Tattha»
    out = []
    for s in split_sents(ln):
        out.append(sentence(s, sid))
    return " ".join(out)


# =========================================================================== Pañhāpucchaka (K23 / K45 engine)
GROUPS79 = dict(K45.GROUPS45)
GROUPS79.update({"Catunnaṃ satipaṭṭhānānaṃ": "из четырёх основ осознанности",
                 "Catunnaṃ sammappadhānānaṃ": "из четырёх правильных усилий",
                 "Catunnaṃ iddhipādānaṃ": "из четырёх основ сверхспособностей"})
SUBJ79 = {
    "Vīmaṃsiddhipādo": (cap(NOUN["vīmaṃsiddhipādo"][0]), "s", "f",
                        "Пытливость как основу сверхспособностей"),
    "Cittiddhipādo": (cap(NOUN["cittiddhipādo"][0]), "s", "m", "Ум как основу сверхспособностей"),
    "Tayo iddhipādā": ("Три основы сверхспособностей", "p", "p", "Три основы сверхспособностей"),
}
PANHA_SENT = {"Kusalāyeva": "Являются только благими"}     # termbase Kusalāyeva «только благой»
PANHA_FIX79 = [  # (bad, good, note)
    ("Siyā vipākā siyā vipākadhammadhammā.", "Siyā vipākā, siyā vipākadhammadhammā.",
     "^2-388 «Siyā vipākā siyā vipākadhammadhammā»: comma missing (added)"),
    ("sāsavācātipi", "sāsavā cātipi", "^2-389 «sāsavācātipi» written as one word (= sāsavā cātipi)"),
    ("āsavasampayuttācātipi", "āsavasampayuttā cātipi",
     "^2-389 «āsavasampayuttācātipi» written as one word (= āsavasampayuttā cātipi)"),
]
NV_RX = re.compile(r"^(?P<pre>.*?)(?P<nv>[Nn]a vattabb[oā]) (?P<rest>.+)$")


def quote_nv(sent):
    """«na vattabbā X cāti, Y» (no quotes, no dash in ch. 7-9) -> «na vattabbā – "X cā"ti, Y» for the K23 engine"""
    toks = sent.split(", ")
    out, in_nv = [], False
    for t in toks:
        m = NV_RX.match(t)
        if m:
            rest = m.group("rest")
            suf = "tipi" if rest.endswith("tipi") else "ti"
            assert rest.endswith(suf), t
            out.append(f'{m.group("pre")}{m.group("nv")} – "{rest[:-len(suf)]}"{suf}')
            in_nv = True
            continue
        if in_nv and t.endswith("tipi"):
            out.append(f'"{t[:-4]}"tipi')
            continue
        in_nv = False
        out.append(t)
    return ", ".join(out)


SPLIT_SUBJ = re.compile(r"^(.*?), ((?:tayo iddhipādā|cittiddhipādo|vīmaṃsiddhipādo) .*)$")


def panha_sentence(sent):
    if sent in PANHA_SENT:
        return PANHA_SENT[sent]
    m = SPLIT_SUBJ.match(sent)
    if m:
        a = panha_sentence(m.group(1))
        b = panha_sentence(cap(m.group(2)))
        return f"{a}, {low(b)}"
    return K45.panha_sentence(quote_nv(sent), None)


def panha_line(p, sid):
    assert "–" not in p, p
    for bad, good, note in PANHA_FIX79:
        if bad in p:
            p = p.replace(bad, good)
            slip(note)
    sents = re.split(r"(?<=\.) (?=[A-ZĀĪŪṬḌṆÑ])", p)
    out = []
    for s in sents:
        assert s.endswith("."), s
        r = panha_sentence(s[:-1]) + "."
        nv = K1.NV.split(" ", 1)[1]                                 # «определить –»
        out.append(r.replace(f"{nv} ", nv[:-2] + " "))              # no Pāli dash after na vattabbā here
    return " ".join(out)


LOCAL79 = {  # matrix predicates missing from K1 / K23 / K45 (negated siblings of K1 items)
    "na maggādhipati": K1.A("не находящаяся под главенством пути", v="не находится под главенством пути"),
}
PL79 = {"na maggādhipatino": "na maggādhipati"}


def install():
    K45.install()
    K23.SUBJ.update(SUBJ79)
    K23.LOCAL.update(LOCAL79)
    K23.PLK.update(PL79)


# =========================================================================== chapters
def heading(ln, ch):
    lvl, text = ln.split(" ", 1)
    T = {S.CH_TITLE[ch][0]: S.CH_TITLE[ch][1], "Suttantabhājanīyaṃ": S.SUTTANTA_BH, "Abhidhammabhājanīyaṃ": S.ABHI_BH,
         "Pañhāpucchakaṃ": S.PANHA, "Tikaṃ": S.TIKA_H, "Dukaṃ": S.DUKA_H}
    T.update(SUBHEAD)
    return f"{lvl} {T[text]}"


def build(ch):
    pali = (S.PALI / PARTS[ch]).read_text(encoding="utf-8")
    h, section = {}, None
    for sid, lines in S.segs(pali):
        lines = [re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", ln) for ln in lines]
        if lines[0].startswith("#"):
            assert len(lines) == 1
            text = lines[0].split(" ", 1)[1]
            if text in ("Suttantabhājanīyaṃ", "Abhidhammabhājanīyaṃ", "Pañhāpucchakaṃ"):
                section = text
            h[sid] = [heading(lines[0], ch)]
            continue
        ru = []
        for ln in lines:
            if sid == "2-455" and ln.endswith('samannāgato"ti'):
                slip("^2-455 «…samannāgato\"ti» without the final full stop: rendered with it")
                ln += "."
            if ln in SENT:
                ru.append(SENT[ln])
            elif section == "Pañhāpucchakaṃ" and not ln.startswith("Cattāro"):
                ru.append(K1.panha_question(ln, GROUPS79) if ln.endswith("?") else panha_line(ln, sid))
            elif section == "Suttantabhājanīyaṃ" and ch == 7:
                ru.append(long_line(ln, sid))
            else:
                ru.append(def_line(ln, sid))
        h[sid] = ru
    return pali, h


# =========================================================================== pi-1 checks
def check_pi1():
    K45.check_pi1()
    K23.assert_pi1(ROOTS_A[:-1], ROOTS_K[:-1], "и омрачения, пребывающие вместе с ними", low(SAMPAY), SAMUTTH,
                   "напряжение сил, отсутствие отвлечения", CONTACT_PE, K6.J1, "– это благие явления",
                   "с трудным способом практики и медленным высшим знанием, пустое, и пребывает в нём",
                   "Вследствие того же совершённого и развитого надмирского благого медитативного погружения, в "
                   "качестве его результата, когда кто-либо", K45.SADDHA_LIST.split(",")[0])
    assert supra() + f", {AT_TIME}" == K45.SUPRA_HEAD, (supra(), K45.SUPRA_HEAD)
    key = [k for k in K6.TASSEVA if k.endswith("suññataṃ")][0]
    assert tasseva() == K6.TASSEVA[key]


# =========================================================================== notes
def notes_md():
    L = ["# pi-2 Russian rails: new formulas of chapters 7, 8 and 9 (^2-355 … ^2-465)", "",
         "Generated by build_rails_7_9_ru.py; import it instead of retyping. Strings already in ru-rails-formulas.md "
         "(sample), notes-1.md, notes-2-3.md, notes-4-5.md or notes-6.md are not repeated.", "",
         "## Headings and closing labels", ""]
    L += [f"##### {p} = ##### {r}" + (f"  (closing label «{p}.» = «{r}.»)" if p.endswith("niddeso") else "")
          for p, r in SUBHEAD.items()]
    L += ["", "## Satipaṭṭhāna", "",
          f"Cattāro satipaṭṭhānā – idha bhikkhu … = {SATIP4} – здесь монах … (groups joined by «;»)",
          "kāye kāyānupassī / vedanāsu vedanānupassī / citte cittānupassī / dhammesu dhammānupassī = "
          + " / ".join(FIELD.values()),
          "ajjhattaṃ / bahiddhā / ajjhattabahiddhā kāye kāyānupassī = во внутреннем / во внешнем / во внутреннем и "
          "внешнем теле созерцая тело (чувства: во внутренних …; ум: во внутреннем …; явления: во внутренних …)",
          "Kathañca bhikkhu <field> viharati? = И как монах пребывает, <field>?",
          "Evaṃ bhikkhu ajjhattabahiddhā <field> viharati ātāpī … abhijjhādomanassaṃ. = Так монах пребывает, <field>, "
          f"{CONTEMPL}.",
          f"So taṃ nimittaṃ āsevati bhāveti bahulīkaroti svāvatthitaṃ vavatthapeti. = {NIMITTA}",
          "So taṃ nimittaṃ āsevitvā … vavatthapetvā bahiddhā kāye cittaṃ upasaṃharati. = "
          + NIMITTA_THEN.format(t="на внешнее тело") + " (" + "; ".join(f"{a} {b}: {v}" for (a, b), v in TARGET.items())
          + ")",
          "Idha bhikkhu ajjhattaṃ kāyaṃ uddhaṃ pādatalā … asucino paccavekkhati – \"atthi imasmiṃ kāye kesā … mutta\"nti. "
          f"= {MONK} рассматривает внутреннее тело {BODY_SCAN} – «Есть в этом теле {BODY32}». (atthissa kāye = Есть в "
          "его теле; body parts = the ch. 3 earth and water lists)",
          "sukhaṃ vedanaṃ vedayamāno \"sukhaṃ vedanaṃ vedayāmī\"ti pajānāti = испытывая приятное чувство, понимает: «Я "
          "испытываю приятное чувство» (items joined by «;»)",
          "sukhaṃ vedanaṃ vedayamānaṃ \"sukhaṃ vedanaṃ vedayatī\"ti pajānāti = про того, кто испытывает приятное "
          "чувство, понимает: «Он испытывает приятное чувство»",
          "sukhaṃ vedanaṃ \"sukhā vedanā\"ti pajānāti = понимает приятное чувство как «приятное чувство»",
          "sāmisaṃ / nirāmisaṃ vā X vedanaṃ = плотское / неплотское X чувство (vā not rendered)",
          "sarāgaṃ vā cittaṃ \"sarāgaṃ me citta\"nti pajānāti = понимает ум, охваченный страстью: «Мой ум охвачен "
          "страстью» (one-word attributes before «ум»: «понимает сжатый ум: «Мой ум сжат»»)",
          "sarāgaṃ vāssa cittaṃ \"sarāgamassa citta\"nti = понимает его ум, охваченный страстью: «Его ум охвачен "
          "страстью»; sarāgaṃ vā cittaṃ \"sarāgaṃ citta\"nti = понимает ум, охваченный страстью: «Ум охвачен страстью»",
          "mind attributes / predicates: " + "; ".join(f"{k} = {a} / {p}" for k, (a, p) in MIND.items()),
          "santaṃ vā ajjhattaṃ X \"atthi me ajjhattaṃ X\"ti pajānāti = понимает имеющееся внутреннее X: «У меня есть "
          "внутреннее X»; asantaṃ … natthi me … = понимает отсутствующее внутреннее X: «У меня нет внутреннего X(gen)»",
          "santaṃ vāssa X \"atthissa X\"ti = понимает имеющееся у него X: «У него есть X»; santaṃ vā X \"atthi X\"ti = "
          "понимает имеющееся X: «Есть X»",
          "yathā ca anuppannassa X uppādo hoti tañca pajānāti = " + YATHA["uppādo hoti"].format(p="невозникшего", x="X"),
          "yathā ca uppannassa X pahānaṃ hoti tañca pajānāti = " + YATHA["pahānaṃ hoti"].format(p="возникшего", x="X"),
          "yathā ca pahīnassa X āyatiṃ anuppādo hoti tañca pajānāti = "
          + YATHA["āyatiṃ anuppādo hoti"].format(p="устранённого", x="X"),
          "yathā ca uppannassa X bhāvanāya pāripūrī hoti tañca pajānāti = "
          + YATHA["bhāvanāya pāripūrī hoti"].format(p="возникшего", x="X"),
          "Santaṃ vā ajjhattaṃ X…pe… santaṃ vā ajjhattaṃ Y … = Понимает имеющееся внутреннее X… имеющееся внутреннее Y "
          "… (the verb once at the head of a …pe… run)",
          "hindrances / factors of awakening: " + "; ".join(f"{k}- = {v[0]} (gen. {v[1]})" for k, v in DH_NOUN.items()),
          "", "## Definitions (Suttanta)", "",
          "Xti. (the word explained) = «X». ; …pe… runs = «X»… «y»… «z».",
          "topics: " + "; ".join(f"{k} = {v}" for k, v in TOPIC.items()),
          f"Tena vuccati \"X\"ti. = {TENA} «X». (K6)",
          "Tattha katamo/katamā/katamaṃ X? = Что такое здесь X? (nouns: "
          + "; ".join(f"{k} = {v[0]} / {v[1]}" for k, v in NOUN.items()) + ")",
          "[katamaṃ ātāpaṃ (sabbattha)] = [вариант чтения (во всех изданиях): katamaṃ ātāpaṃ]",
          f"Imāya/Iminā X upeto hoti samupeto upāgato samupāgato upapanno sampanno samannāgato. = Этим X(ins) он {UPETO}.",
          f"Iminā X upeto hoti…pe… samannāgato. = Этим X(ins) он {UPETO_PE}.",
          "demonstratives: " + "; ".join(f"{k} = {v}" for k, v in DEM_INS.items()),
          "Iriyati vattati pāleti yapeti yāpeti carati viharati. = "
          + SENT["Iriyati vattati pāleti yapeti yāpeti carati viharati."],
          "Tattha katamo loko? Sveva kāyo loko. Pañcapi upādānakkhandhā loko. Ayaṃ vuccati \"loko\". = Что такое здесь "
          f"мир? Это самое тело является миром. {FIVE_LOKO}. Это называется «миром».",
          "Sāyeva vedanā / Taṃyeva cittaṃ / Teva dhammā loko. = Это самое чувство / Этот самый ум / Эти самые явления "
          "являются миром.",
          f"Iti ayañca abhijjhā idañca domanassaṃ imamhi loke vinītā honti … byantīkatā. = {VINITA}",
          "lists after Yo / Yā / Yaṃ (= То, что есть …): " + "; ".join(f"{k} = {v}" for k, v in LISTS.items()),
          "", "## Sammappadhāna", "",
          f"Cattāro sammappadhānā – idha bhikkhu <aim> chandaṃ janeti … = {SAMMAP4} – здесь монах <aim> {EFFORT}; …",
          "aims (K45): " + "; ".join(f"{k} = {aim(k)}" for k in AIM),
          f"Kathañca bhikkhu <aim> chandaṃ janeti …? = {HOW} <aim> {EFFORT}?",
          f"Iti imesaṃ <aim> chandaṃ janeti … = Итак, <aim with «этих»> он {EFFORT}.",
          f"Tīṇi akusalamūlāni – lobho, doso, moho. = {ROOTS_A} (pi-1 ^1-986)",
          f"Tīṇi kusalamūlāni – alobho, adoso, amoho. = {ROOTS_K} (pi-1 ^1-985)",
          f"Tadekaṭṭhā ca kilesā. = {TADEKATTHA} (pi-1)",
          f"Taṃsampayutto vedanākkhandho, …, viññāṇakkhandho[,.] taṃsamuṭṭhānaṃ kāyakammaṃ … = {SAMPAY}; {SAMUTTH} (pi-1)",
          f"Ime vuccanti \"anuppannā pāpakā akusalā dhammā\". = это называется «{NOUN['anuppannā pāpakā akusalā dhammā'][1]}».",
          "Imaṃ chandaṃ janeti sañjaneti uṭṭhapeti samuṭṭhapeti nibbatteti abhinibbatteti. = "
          + SENT["Imaṃ chandaṃ janeti sañjaneti uṭṭhapeti samuṭṭhapeti nibbatteti abhinibbatteti."],
          "[uṭṭhāpeti samuṭṭhāpeti (syā.) evamuparipi] = [вариант написания (Syā.): uṭṭhāpeti samuṭṭhāpeti, так же и далее]",
          "Imaṃ vīriyaṃ ārabhati samārabhati āsevati bhāveti bahulīkaroti. = "
          + SENT["Imaṃ vīriyaṃ ārabhati samārabhati āsevati bhāveti bahulīkaroti."],
          "Imaṃ cittaṃ paggaṇhāti sampaggaṇhāti upatthambheti paccupatthambheti. = "
          + SENT["Imaṃ cittaṃ paggaṇhāti sampaggaṇhāti upatthambheti paccupatthambheti."],
          f"Ṭhitiyāti. Yā ṭhiti so asammoso, … yā bhāvanā sā pāripūrī. = «{TOPIC['ṭhitiyā']}». {THITI_CHAIN}",
          "", "## Iddhipāda", "",
          f"Cattāro iddhipādā – idha bhikkhu Xsamādhipadhānasaṅkhārasamannāgataṃ iddhipādaṃ bhāveti, … = {IDDHIP4} – "
          f"здесь монах развивает {ip_acc('chanda')}; …",
          "Xsamādhi = " + "; ".join(f"{k} = сосредоточение через {v}" for k, v in SAMADHI_THROUGH.items()),
          "Xṃ ce bhikkhu adhipatiṃ karitvā labhati samādhiṃ, labhati cittassekaggataṃ = Если монах, <взяв X как "
          "главенствующее>, обретает сосредоточение, обретает однонаправленность ума ("
          + "; ".join(f"{k} = {v}" for k, v in ADHIPATI.items()) + ")",
          f"Ime vuccanti \"padhānasaṅkhārā\". = {SENT['Ime vuccanti \"padhānasaṅkhārā\".']}",
          "Iti ayañca Xsamādhi, ime ca padhānasaṅkhārā[.;] = Итак, это сосредоточение через X и эти формирующие "
          "факторы усилия[.;]",
          f"Tadekajjhaṃ abhisaññūhitvā abhisaṅkhipitvā Xsamādhipadhānasaṅkhārotveva saṅkhyaṃ gacchati. = "
          f"{together('Tadekajjhaṃ abhisaññūhitvā abhisaṅkhipitvā chandasamādhipadhānasaṅkhārotveva saṅkhyaṃ gacchati.', 'chanda')}",
          "Iti iminā ca X, iminā ca samādhinā, iminā ca padhānasaṅkhārena upeto hoti … = Итак, этим X, этим "
          f"сосредоточением и этим формирующим фактором усилия он {UPETO}.",
          f"Yā tesaṃ dhammānaṃ iddhi samiddhi … upasampadā. = {IDDHI_DEF}",
          f"Tathābhūtassa vedanākkhandho, … = {TATHA} {KH4}.; Tathābhūtassa phasso…pe… paggāho avikkhepo. = "
          f"{TATHA} контакт… напряжение сил, отсутствие отвлечения.",
          f"Te dhamme āsevati bhāveti bahulīkaroti. = {SENT['Te dhamme āsevati bhāveti bahulīkaroti.']}",
          "chandiddhipādo / vīriyiddhipādo / cittiddhipādo / vīmaṃsiddhipādo = "
          + " / ".join(NOUN[f"{k}iddhipādo"][0] for k in IDDHIPADA),
          "", "## Abhidhammabhājanīya", "",
          f"Idha bhikkhu yasmiṃ samaye lokuttaraṃ jhānaṃ … dandhābhiññaṃ <field>, yā tasmiṃ samaye … = "
          f"{supra('<field>, ')}, {WHAT_AT_TIME} …",
          f"Tasseva lokuttarassa … dandhābhiññaṃ suññataṃ <field>, yā tasmiṃ samaye … = {tasseva('<field>, ')}, "
          f"{WHAT_AT_TIME} …",
          f"Ime dhammā kusalā. = {ALL_THIS}",
          "Avasesā dhammā Xsampayuttā. = Остальные явления связаны с X(ins).",
          "tasmiṃ samaye Xsamādhipadhānasaṅkhārasamannāgataṃ iddhipādaṃ bhāveti = в это время развивает основу "
          "сверхспособностей, наделённую …",
          "", "## Pañhāpucchaka", "",
          "Catunnaṃ satipaṭṭhānānaṃ / sammappadhānānaṃ / iddhipādānaṃ kati …? = Сколько из четырёх основ осознанности / "
          "правильных усилий / основ сверхспособностей являются …?",
          f"Kusalāyeva. = {PANHA_SENT['Kusalāyeva']}.",
          "na vattabbā X(cā)ti / Xtipi, Ytipi (no dash, no quotes in ch. 7-9) = нельзя определить как «X» / нельзя "
          "определить ни как «X», ни как «Y» (the K1 forms without the dash)",
          "subjects: " + "; ".join(f"{k} = {v[0]} (acc. {v[3]})" for k, v in SUBJ79.items()),
          ]
    return "\n".join(L) + "\n"


def main():
    install()
    check_pi1()
    for ch in (7, 8, 9):
        pali, h = build(ch)
        (S.OUT / PARTS[ch]).write_text(K23.render(pali, h), encoding="utf-8", newline="\n")
        print(f"wrote {PARTS[ch]}: {len(S.segs(pali))} segments")
    NOTES_PATH.write_text(notes_md(), encoding="utf-8", newline="\n")
    for s in SLIPS + K23.SLIPS + K1.SLIPS + K45.SLIPS:
        print("slip:", s)


if __name__ == "__main__":
    main()
