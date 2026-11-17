# -*- coding: utf-8 -*-
"""pi-2 Vibhaṅga, Russian plain zero-shot: chapters 7 (Satipaṭṭhāna), 8 (Sammappadhāna), 9 (Iddhipāda).

usage: python -I -X utf8 build_7_9_ru.py
Writes AI_translation\\russian\\pi-2-russian-plain-zeroshot_split_chapters\\7-…, 8-…, 9-….md.
Reuses build_ch1_sample_ru (S), build_1_ru (B), build_2_3_ru (T), build_4_5_ru (F), build_6_ru (G):
lokuttara opening (pi-1 ^1-277), vipāka opening (pi-1 ^1-505), path-factor bodies (pi-1 ^1-297 …), the four
efforts (pi-1 ^1-1377), the satipaṭṭhāna tail (ch. 4), body-part lists (ch. 3), domanassa (pi-1 ^1-415),
rāga / citta strings (ch. 6), the Pañhāpucchaka lexicon (B/T/F, extended in memory only).
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

DASH = S.DASH
cap, low = S.cap, S.low
PE = "\x01"
PI1 = T.PI1
edit, in_pi1 = F.edit, F.in_pi1
SEC = S.SECTION_TITLES
TATTHA = S.TATTHA            # Что такое здесь
NV = B.NV                    # нельзя определить


def called(ins, quoted=True):
    return T.called(ins, quoted)


def pali_text(fn):
    return open(os.path.join(S.PALI_DIR, fn), encoding="utf-8").read()


# ================================================================ 1. definition bodies («То, что есть …»)
def cut(body, end):
    return body[:body.index(end) + len(end)]


VIRIYA_FULL = F.VIRIYA_B                                    # pi-1 ^1-13 (thāmo ṭhiti «стойкость, устойчивость», ch. 5)
VIRIYA_PE = cut(F.FACTOR_BODY["Yo cetasiko vīriyārambho…pe… sammāvāyāmo vīriyasambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ"],
                "правильное усилие")                        # «То, что есть душевное приложение усердия… правильное усилие»
SAMADHI_FULL = F.SAMADHI_B                                  # pi-1 ^1-15
SAMADHI_PE = F.pe(F.SAMADHI_B, 2, "правильное сосредоточение")
SATI_PE = F.pe(F.SATI_B, 2, "правильная осознанность")
PANNA_PE = F.PANNA_B
DOMANASSA = "То, что есть " + T.FEEL["domanassa"]           # pi-1 ^1-415
CHANDA = "То, что есть желание, проявление желания, желание действовать, благое стремление к Учению"
VAR_CHANDI = " [вариант написания (Syā.): chandīkatā]"
SATI_LOK = ("То, что есть осознанность, припоминание, правильная осознанность, фактор пробуждения осознанности, "
            "фактор пути, входящий в путь")                # sati anussati sammāsati satisambojjhaṅgo … (no …pe…)
assert F.FACTOR_BODY["Yā sati anussati…pe… sammāsati satisambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ"].replace(
    "…", ",") == SATI_LOK
_p5 = pali_text("5-indriyavibhango.md")
for _b in ("Yā cittassa ṭhiti saṇṭhiti avaṭṭhiti avisāhāro avikkhepo avisāhaṭamānasatā samatho samādhindriyaṃ "
           "samādhibalaṃ sammāsamādhi – ",
           "Yo cetasiko vīriyārambho nikkamo parakkamo uyyāmo vāyāmo ussāho ussoḷhī thāmo ṭhiti asithilaparakkamatā "
           "anikkhittachandatā anikkhittadhuratā dhurasampaggāho vīriyaṃ vīriyindriyaṃ vīriyabalaṃ"):
    assert _b in _p5, _b[:40]
assert VIRIYA_FULL.endswith("сила усердия, правильное усилие")   # pi-2 ^2-433 ends "vīriyabalaṃ sammāvāyāmo" (as pi-1 ^1-13)
assert F.PALI3["domanassa"] == ("Yaṃ cetasikaṃ asātaṃ cetasikaṃ dukkhaṃ cetosamphassajaṃ asātaṃ dukkhaṃ vedayitaṃ "
                                "cetosamphassajā asātā dukkhā vedanā")

DEF = {   # Pāli body (between the question / comma and " – ayaṃ vuccati") -> Russian «То, что есть …»
    "Yā paññā pajānanā…pe… amoho dhammavicayo sammādiṭṭhi": PANNA_PE,
    "Yo cetasiko vīriyārambho…pe… sammāvāyāmo": VIRIYA_PE,
    "Yā sati anussati…pe… sammāsati": SATI_PE,
    "Yā sati anussati sammāsati satisambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ": SATI_LOK,
    "Yo rāgo sārāgo…pe… cittassa sārāgo": G.BODY["Yo rāgo sārāgo…pe… cittassa sārāgo"][0],
    F.PALI3["domanassa"]: DOMANASSA,
    "Yo chando chandikatā kattukamyatā kusalo dhammacchando": CHANDA,
    "Yo chando chandikatā [chandīkatā (syā.)] kattukamyatā kusalo dhammacchando":
        edit(CHANDA, "проявление желания", "проявление желания" + VAR_CHANDI),
    "Yaṃ cittaṃ mano mānasaṃ…pe… tajjāmanoviññāṇadhātu":
        G.BODY["Yaṃ cittaṃ mano mānasaṃ…pe… tajjāmanoviññāṇadhātu"][0],
    "Yā cittassa ṭhiti saṇṭhiti avaṭṭhiti avisāhāro avikkhepo avisāhaṭamānasatā samatho samādhindriyaṃ samādhibalaṃ "
    "sammāsamādhi": SAMADHI_FULL,
    "Yā cittassa ṭhiti saṇṭhiti…pe… sammāsamādhi": SAMADHI_PE,
    "Yo cetasiko vīriyārambho nikkamo parakkamo uyyāmo vāyāmo ussāho ussoḷhī thāmo ṭhiti asithilaparakkamatā "
    "anikkhittachandatā anikkhittadhuratā dhurasampaggāho vīriyaṃ vīriyindriyaṃ vīriyabalaṃ sammāvāyāmo": VIRIYA_FULL,
}
for _k in ("Yā paññā pajānanā…pe… amoho dhammavicayo sammādiṭṭhi dhammavicayasambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ",
           "Yo cetasiko vīriyārambho…pe… sammāvāyāmo vīriyasambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ",
           "Yā cittassa ṭhiti saṇṭhiti…pe… sammāsamādhi samādhisambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ"):
    DEF[_k] = F.FACTOR_BODY[_k]                             # pi-1 ^1-297, ^1-302, ^1-304 without «в это время»
for _k, _v in DEF.items():
    assert _v.startswith("То, что есть "), _k


def defn(body, tasmim=False):
    """'Yo/Yā/Yaṃ [tasmiṃ samaye] X' -> «То, что есть …» / «то, что в это время есть …»."""
    if tasmim:
        m = re.match(r"^(Yo|Yā|Yaṃ) tasmiṃ samaye (.+)$", body)
        ru = DEF[m.group(1) + " " + m.group(2)]
        return "то, что в это время есть " + ru[len("То, что есть "):]
    return DEF[body]


# ================================================================ 2. terms: question (nom) / answer (ins)
TERM = {
    "anupassanā": ("созерцание", "созерцанием"),
    "ātāpo": ("ревностность", "ревностностью"),
    "sampajaññaṃ": ("ясное понимание", "ясным пониманием"),
    "sati": ("осознанность", "осознанностью"),
    "loko": ("мир", "миром"),
    "abhijjhā": ("алчность", "алчностью"),
    "domanassaṃ": ("уныние", "унынием"),
    "satipaṭṭhānaṃ": ("основа осознанности", "основой осознанности"),
    "chando": ("желание", "желанием"),
    "vāyāmo": ("усилие", "усилием"),
    "vīriyaṃ": ("усердие", "усердием"),
    "cittaṃ": ("ум", "умом"),
    "padhānaṃ": ("усилие", "усилием"),
    "sammappadhānaṃ": ("правильное усилие", "правильным усилием"),
    "samādhi": ("сосредоточение", "сосредоточением"),
    "padhānasaṅkhāro": ("формирующий фактор усилия", "формирующим фактором усилия"),
    "padhānasaṅkhārā": ("формирующие факторы усилия", "формирующими факторами усилия"),
    "vīmaṃsā": ("пытливость", "пытливостью"),
    "anuppannā pāpakā akusalā dhammā": ("невозникшие дурные неблагие явления", "невозникшими дурными неблагими явлениями"),
    "uppannā pāpakā akusalā dhammā": ("возникшие дурные неблагие явления", "возникшими дурными неблагими явлениями"),
    "anuppannā kusalā dhammā": ("невозникшие благие явления", "невозникшими благими явлениями"),
    "uppannā kusalā dhammā": ("возникшие благие явления", "возникшими благими явлениями"),
}
# iddhipāda: chanda / vīriya / citta / vīmaṃsā (pi-1 «желание», «усердие», «ум», «пытливость» from …ādhipateyya)
IP = {   # key: (Pāli compound stem, Pāli acc, Russian acc after «через», adjective ending for «главенствующ-»)
    "chanda": ("chanda", "Chandaṃ", "желание", "им"),
    "vīriya": ("vīriya", "Vīriyaṃ", "усердие", "им"),
    "citta": ("citta", "Cittaṃ", "ум", "им"),
    "vīmaṃsā": ("vīmaṃsā", "Vīmaṃsaṃ", "пытливость", "ей"),
}
in_pi1("с преобладанием желания", "с преобладанием усердия", "с преобладанием ума", "с преобладанием пытливости")
IP_NAME = {"chanda": ("желание как основа сверхспособностей", "желанием как основой сверхспособностей", "n"),
           "vīriya": ("усердие как основа сверхспособностей", "усердием как основой сверхспособностей", "n"),
           "citta": ("ум как основа сверхспособностей", "умом как основой сверхспособностей", "m"),
           "vīmaṃsā": ("пытливость как основа сверхспособностей", "пытливостью как основой сверхспособностей", "f")}
IP_PALI = {"chanda": "chandiddhipādo", "vīriya": "vīriyiddhipādo", "citta": "cittiddhipādo", "vīmaṃsā": "vīmaṃsiddhipādo"}
IDDHIPADA = ("основа сверхспособностей", "основу сверхспособностей")   # iddhipāda [pi-1, pi-5]
for k, (stem, _a, x, _e) in IP.items():
    TERM[stem + "samādhi"] = (f"сосредоточение через {x}", f"сосредоточением через {x}")
    TERM[IP_PALI[k]] = IP_NAME[k][:2]


def ip_adj(k):   # chandasamādhipadhānasaṅkhārasamannāgataṃ (iddhipādaṃ)
    return f"наделённую сосредоточением через {IP[k][2]} и формирующим фактором усилия"


def ip_name(k):  # chandasamādhipadhānasaṅkhāro
    return f"сосредоточение через {IP[k][2]} и формирующий фактор усилия"


def ip_lemma(k):  # chandasamādhipadhānasaṅkhārasamannāgato
    return f"наделённый сосредоточением через {IP[k][2]} и формирующим фактором усилия"


SAMP = {"satipaṭṭhāna": "основой осознанности", "sammappadhāna": "правильным усилием"}
for k in IP:
    SAMP[IP_PALI[k][:-1] + "a"] = IP_NAME[k][1]

# ================================================================ 3. satipaṭṭhāna phrases
DOM = {   # domain: (Pāli locative, Pāli anupassī stem, {region: Russian locative}, «созерцая …», {region: target acc})
    "kāya": ("kāye", "kāyā", {"": "в теле", "ajjhattaṃ": "во внутреннем теле", "bahiddhā": "во внешнем теле",
                              "ajjhattabahiddhā": "во внутреннем и внешнем теле"}, "созерцая тело",
             {"bahiddhā": "на внешнее тело", "ajjhattabahiddhā": "на внутреннее и внешнее тело"}),
    "vedanā": ("vedanāsu", "vedanā", {"": "в чувствах", "ajjhattaṃ": "во внутренних чувствах",
                                      "bahiddhā": "во внешних чувствах",
                                      "ajjhattabahiddhā": "во внутренних и внешних чувствах"}, "созерцая чувства",
               {"bahiddhā": "на внешние чувства", "ajjhattabahiddhā": "на внутренние и внешние чувства"}),
    "citta": ("citte", "cittā", {"": "в уме", "ajjhattaṃ": "во внутреннем уме", "bahiddhā": "во внешнем уме",
                                 "ajjhattabahiddhā": "во внутреннем и внешнем уме"}, "созерцая ум",
              {"bahiddhā": "на внешний ум", "ajjhattabahiddhā": "на внутренний и внешний ум"}),
    "dhamma": ("dhammesu", "dhammā", {"": "в явлениях", "ajjhattaṃ": "во внутренних явлениях",
                                      "bahiddhā": "во внешних явлениях",
                                      "ajjhattabahiddhā": "во внутренних и внешних явлениях"}, "созерцая явления",
               {"bahiddhā": "на внешние явления", "ajjhattabahiddhā": "на внутренние и внешние явления"}),
}
DOMS = ["kāya", "vedanā", "citta", "dhamma"]
SATI_TAIL = F.SATI_TAIL               # ревностный, ясно понимающий, осознанный, устранив алчность и уныние в отношении мира
SATI_TAIL_P = "ātāpī sampajāno satimā vineyya loke abhijjhādomanassaṃ"
assert F.SATI_S.startswith(f"Вот монах пребывает в теле, созерцая тело, {SATI_TAIL}.")


def anu_p(d, region=""):
    loc, stem = DOM[d][0], DOM[d][1]
    return (region + " " if region else "") + f"{loc} {stem}nupassī"


def dwell(d, region=""):
    return f"пребывает {DOM[d][2][region]}, {DOM[d][3]}"


def dwell_jhana(d):   # "… dandhābhiññaṃ kāye kāyānupassī" (no viharati): «в теле созерцая тело»
    return f"{DOM[d][2]['']} {DOM[d][3]}"


FOUR_SP = "Четыре основы осознанности"
FOUR_SPP = "Четыре правильных усилия"
FOUR_IP = "Четыре основы сверхспособностей"


def opener_sp(kind):
    """'Cattāro satipaṭṭhānā – idha bhikkhu …' (Sutta ^2-355, Abhidhamma ^2-374, Pañhāpucchaka ^2-386)."""
    if kind == "sutta":
        p = ", ".join(" ".join(f"{anu_p(d, r)} viharati" for r in ("ajjhattaṃ", "bahiddhā", "ajjhattabahiddhā"))
                      + " " + SATI_TAIL_P for d in DOMS)
        r = "; ".join(", ".join(dwell(d, x) for x in ("ajjhattaṃ", "bahiddhā", "ajjhattabahiddhā")) + ", " + SATI_TAIL
                      for d in DOMS)
    elif kind == "abhi":
        p = ", ".join(f"{anu_p(d)} viharati" for d in DOMS)
        r = "; ".join(dwell(d) for d in DOMS)
    else:
        p = ", ".join(f"{anu_p(d)} viharati {SATI_TAIL_P}" for d in DOMS)
        r = "; ".join(f"{dwell(d)}, {SATI_TAIL}" for d in DOMS)
    return f"Cattāro satipaṭṭhānā – idha bhikkhu {p}.", f"{FOUR_SP} {DASH} вот монах {r}."


# body parts (ch. 3 lists, pi-1 words)
PARTS_P = ("kesā lomā nakhā dantā taco maṃsaṃ nhāru{v1} aṭṭhi aṭṭhimiñjaṃ{v2} vakkaṃ hadayaṃ yakanaṃ kilomakaṃ "
           "pihakaṃ papphāsaṃ antaṃ antaguṇaṃ udariyaṃ karīsaṃ pittaṃ semhaṃ pubbo lohitaṃ sedo medo assu vasā kheḷo "
           "siṅghāṇikā lasikā mutta")
PARTS_R_VAR = T.LISTS[("pathavī", "int")] + ", " + T.LISTS[("āpo", "int")]
PARTS_R = PARTS_R_VAR.replace(" [вариант написания (Sī.): nahāru]", "").replace(" [вариант написания (Sī.): aṭṭhimiñjā]", "")
KAYA_ACC = {"ajjhattaṃ": "внутреннее тело", "bahiddhā": "внешнее тело", "ajjhattabahiddhā": "внутреннее и внешнее тело"}
KAYA_Q = {"atthi imasmiṃ kāye": "В этом теле есть", "atthissa kāye": "В его теле есть"}


def kaya_sentence(s):
    for region in KAYA_ACC:
        for qp, qr in KAYA_Q.items():
            for var in (False, True):
                parts = PARTS_P.format(v1=" [nahāru (sī.)]" if var else "", v2=" [aṭṭhimiñjā (sī.)]" if var else "")
                p = (f"Idha bhikkhu {region} kāyaṃ uddhaṃ pādatalā adho kesamatthakā tacapariyantaṃ pūraṃ "
                     f"nānappakārassa asucino paccavekkhati – \"{qp} {parts}\"nti.")
                if p == s:
                    return (f"Вот монах рассматривает {KAYA_ACC[region]} от подошв ног вверх и от кончиков волос на "
                            f"голове вниз, ограниченное кожей и полное разного рода нечистот {DASH} "
                            f"«{qr} {PARTS_R_VAR if var else PARTS_R}».")
    return None


# feelings
FEEL_R = {"sukh": "приятное чувство", "dukkh": "болезненное чувство",
          "adukkhamasukh": "чувство, которое ни болезненно, ни приятно"}        # [pi-1]
AMISA = {None: "", "sāmis": "плотское ", "nirāmis": "неплотское "}              # sāmisa / nirāmisa [new]
FEEL_ITEMS = [(None, "sukh"), (None, "dukkh"), (None, "adukkhamasukh"), ("sāmis", "sukh"), ("nirāmis", "sukh"),
              ("sāmis", "dukkh"), ("nirāmis", "dukkh"), ("sāmis", "adukkhamasukh"), ("nirāmis", "adukkhamasukh")]


def feel_sentence(s):
    for mode in ("int", "ext", "both"):
        ps, rs = [], []
        for am, v in FEEL_ITEMS:
            acc = (f"{am}aṃ vā " if am else "") + f"{v}aṃ vedanaṃ"
            fr = AMISA[am] + FEEL_R[v]
            if mode == "int":
                ps.append(f'{acc} vedayamāno "{am + "aṃ " if am else ""}{v}aṃ vedanaṃ vedayāmī"ti pajānāti')
                rs.append(f"{'или, ' if am else ''}испытывая {fr}, понимает: «Я испытываю {fr}»")
            elif mode == "ext":
                ps.append(f'{acc} vedayamānaṃ "{am + "aṃ " if am else ""}{v}aṃ vedanaṃ vedayatī"ti pajānāti')
                rs.append(f"{'или ' if am else ''}о том, кто испытывает {fr}, понимает: «Он испытывает {fr}»")
            else:
                ps.append(f'{acc} "{am + "ā " if am else ""}{v}ā vedanā"ti pajānāti')
                comma = "," if fr.endswith("приятно") else ""
                rs.append(f"{'или ' if am else ''}{fr}{comma} понимает как «{fr}»")
        p = "Idha bhikkhu " + ", ".join(ps) + "."
        if p == s:
            first = rs[0]
            head = "Вот монах, " if mode == "int" else "Вот монах "
            return head + "; ".join(rs) + "."
    return None


# mind states
CITTA_ST = [("sarāg", "охвачен страстью"), ("vītarāg", "свободен от страсти"), ("sados", "охвачен злобой"),
            ("vītados", "свободен от злобы"), ("samoh", "охвачен заблуждением"), ("vītamoh", "свободен от заблуждения"),
            ("saṃkhitt", "сжат"), ("vikkhitt", "рассеян"), ("mahaggat", "возвышен"), ("amahaggat", "невозвышен"),
            ("sauttar", "имеет над собой высшее"), ("anuttar", "не имеет над собой высшего"),
            ("samāhit", "сосредоточен"), ("asamāhit", "несосредоточен"), ("vimutt", "освобождён"),
            ("avimutt", "неосвобождён")]


def citta_sentence(s):
    for mode in ("int", "ext", "both"):
        ps, rs = [], []
        for st, pr in CITTA_ST:
            if mode == "int":
                ps.append(f'{st}aṃ vā cittaṃ "{st}aṃ me citta"nti pajānāti')
                rs.append(f"когда ум {pr}, понимает: «Мой ум {pr}»")
            elif mode == "ext":
                ps.append(f'{st}aṃ vāssa cittaṃ "{st}amassa citta"nti pajānāti')
                rs.append(f"когда ум кого-то {pr}, понимает: «Его ум {pr}»")
            else:
                ps.append(f'{st}aṃ vā cittaṃ "{st}aṃ citta"nti pajānāti')
                rs.append(f"когда ум {pr}, понимает: «Ум {pr}»")
        if "Idha bhikkhu " + ", ".join(ps) + "." == s:
            return "Вот монах, " + "; ".join(rs) + "."
    return None


# mental objects: hindrances and factors of awakening
NOUN = {   # Pāli stem -> (acc, nom, gen Pāli endings stem-based), Russian nom, Russian gen
    "kāmacchand": ("чувственное желание", "чувственного желания"),       # pi-1 kāmacchando
    "byāpād": ("недоброжелательность", "недоброжелательности"),
    "thinamiddh": ("вялость и сонливость", "вялости и сонливости"),
    "uddhaccakukkucc": ("беспокойство и угрызения", "беспокойства и угрызений"),
    "vicikicch": ("колебание", "колебания"),
    "satisambojjhaṅg": ("фактор пробуждения осознанности", "фактора пробуждения осознанности"),
    "dhammavicayasambojjhaṅg": ("фактор пробуждения исследования явлений", "фактора пробуждения исследования явлений"),
    "vīriyasambojjhaṅg": ("фактор пробуждения усердия", "фактора пробуждения усердия"),
    "pītisambojjhaṅg": ("фактор пробуждения восторга", "фактора пробуждения восторга"),
    "passaddhisambojjhaṅg": ("фактор пробуждения безмятежности", "фактора пробуждения безмятежности"),
    "samādhisambojjhaṅg": ("фактор пробуждения сосредоточения", "фактора пробуждения сосредоточения"),
    "upekkhāsambojjhaṅg": ("фактор пробуждения невозмутимости", "фактора пробуждения невозмутимости"),
}
in_pi1("фактор пробуждения осознанности", "фактор пробуждения исследования явлений", "фактор пробуждения усердия",
       "фактор пробуждения восторга", "фактор пробуждения безмятежности", "фактор пробуждения сосредоточения",
       "чувственное желание", "помеха вялости и сонливости", "помеха беспокойства и угрызений")
# upekkhāsambojjhaṅga: not in pi-1; «фактор пробуждения невозмутимости» [new, upekkhā = невозмутимость]
NOUN_VAR = {"thinamiddhaṃ [thīnamiddhaṃ (sī. syā.)]": ("thinamiddhaṃ", " [вариант написания (Sī., Syā.): thīnamiddhaṃ]"),
            "vīriyasambojjhaṅgaṃ [viriyasambojjhaṅgaṃ (sī. syā.)]":
                ("vīriyasambojjhaṅgaṃ", " [вариант написания (Sī., Syā.): viriyasambojjhaṅgaṃ]")}


def noun(w):
    """Pāli word in any case (…aṃ / …o / …ā / …assa / …āya) -> (Russian nom, Russian gen)."""
    var = ""
    if w in NOUN_VAR:
        w, var = NOUN_VAR[w]
    for end in ("aṃ", "assa", "āya", "o", "ā"):
        if w.endswith(end) and w[:-len(end)] in NOUN:
            nom, gen = NOUN[w[:-len(end)]]
            return nom + var, gen + var
    raise KeyError("noun: " + w)


def dhamma_clause(c, mode):
    """one comma-separated clause of the dhammānupassanā lines."""
    W = r"(\S+(?: \[[^\]]+\])?)"
    loc = {"int": ("внутри него ", "Внутри меня "), "ext": ("у кого-то ", "У него "), "both": ("", "")}[mode]
    m = re.match(r"^(santaṃ|asantaṃ) (?:vā|vāssa) (?:ajjhattaṃ )?" + W + r'(?: "(?:atthi|natthi)(?: me ajjhattaṃ |ssa | )(\S+)"ti pajānāti)?$', c)
    if m:
        nom, gen = noun(m.group(2))
        pos = m.group(1) == "santaṃ"
        what = f"есть {nom}" if pos else f"нет {gen}"
        r = f"когда {loc[0]}{what}"
        if m.group(3):
            r += f", понимает: «{loc[1]}{what}»" if loc[1] else f", понимает: «{cap(what)}»"
        return r
    m = re.match(r"^yathā ca (anuppann|uppann|pahīn)(?:assa|āya) (\S+) (uppādo|pahānaṃ|āyatiṃ anuppādo|bhāvanāya pāripūrī) hoti tañca pajānāti$", c)
    if m:
        _nom, gen = noun(m.group(2))
        kind = (m.group(1), m.group(3))
        what = {("anuppann", "uppādo"): f"происходит возникновение невозникшего {gen}",
                ("uppann", "pahānaṃ"): f"происходит устранение возникшего {gen}",
                ("pahīn", "āyatiṃ anuppādo"): f"в будущем не происходит возникновения устранённого {gen}",
                ("uppann", "bhāvanāya pāripūrī"): f"происходит завершённость развития возникшего {gen}"}[kind]
        return f"понимает и то, как {what}"
    raise KeyError("dhamma clause: " + c)


def dhamma_sentence(s, mode):
    """'Idha bhikkhu santaṃ vā …' / 'Santaṃ vā …' sentences."""
    first = s.startswith("Idha bhikkhu ")
    body = s[len("Idha bhikkhu "):] if first else s
    assert body.endswith("."), s[-30:]
    body = low(body[:-1]).replace(" …pe…", "…pe…")
    parts = re.split(r"(, |…pe… )", body)
    out = []
    for i, x in enumerate(parts):
        if i % 2:
            out.append("; " if x == ", " else "… ")
        else:
            out.append(dhamma_clause(x, mode))
    r = "".join(out)
    return ("Вот монах, " + r if first else cap(r)) + "."


NIMITTA = "Этот признак он практикует, развивает, многократно повторяет, чётко устанавливает."   # So taṃ nimittaṃ āsevati …
NIMITTA_P = "So taṃ nimittaṃ āsevati bhāveti bahulīkaroti svāvatthitaṃ vavatthapeti."


def upasamharati(s):
    m = re.match(r"^So taṃ nimittaṃ āsevitvā bhāvetvā bahulīkaritvā svāvatthitaṃ vavatthapetvā (bahiddhā|ajjhattabahiddhā) "
                 r"(\S+) cittaṃ upasaṃharati\.$", s)
    if not m:
        return None
    d = next(k for k in DOMS if DOM[k][0] == m.group(2))
    return (f"После того как он практиковал этот признак, развил, многократно повторил и чётко установил его, "
            f"он направляет ум {DOM[d][4][m.group(1)]}.")


# ================================================================ 4. lemmas and fixed sentences
LEMMA = {
    "anupassī": "созерцая", "viharatī": "пребывает", "ātāpī": "ревностный", "sampajāno": "ясно понимающий",
    "satimā": "осознанный", "vineyya loke abhijjhādomanassaṃ": "устранив алчность и уныние в отношении мира",
    "chandaṃ janetī": "порождает желание", "vāyamatī": "прилагает усилие", "vīriyaṃ ārabhatī": "пробуждает усердие",
    "cittaṃ paggaṇhātī": "напрягает ум", "padahatī": "прилагает старания", "ṭhitiyā": "ради сохранения",
    "iddhī": "сверхспособность", "iddhipādo": "основа сверхспособностей",
    "iddhipādaṃ bhāvetī": "развивает основу сверхспособностей",
}
for _k, (_stem, _a, _x, _e) in IP.items():
    LEMMA[_stem + "samādhipadhānasaṅkhārasamannāgato"] = ip_lemma(_k)
SP_EFFORT = F.SP_EFFORT          # порождает желание, прилагает усилие, пробуждает усердие, напрягает ум, прилагает старания
assert SATI_TAIL == "ревностный, ясно понимающий, осознанный, устранив алчность и уныние в отношении мира"
assert SP_EFFORT == ("порождает желание, прилагает усилие, пробуждает усердие, напрягает ум, прилагает старания")


def lemma(p):
    """Pāli lemma text (as quoted, "nti" folded to "ṃ") -> Russian."""
    return LEMMA[low(p)]


UPETO_FULL = "он обладает, вполне обладает, снабжён, вполне снабжён, обеспечен, оснащён, наделён"
UPETO_PE = "он обладает… наделён"
UPETO_INS = {"Imāya anupassanāya": "Этим созерцанием", "Iminā ātāpena": "Этой ревностностью",
             "Iminā sampajaññena": "Этим ясным пониманием", "Imāya satiyā": "Этой осознанностью",
             "Iminā vāyāmena": "Этим усилием", "Iminā padhānena": "Этим усилием",
             "Iti iminā ca chandena, iminā ca samādhinā, iminā ca padhānasaṅkhārena":
                 "Таким образом, и этим желанием, и этим сосредоточением, и этим формирующим фактором усилия",
             "Iti iminā ca vīriyena, iminā ca samādhinā, iminā ca padhānasaṅkhārena":
                 "Таким образом, и этим усердием, и этим сосредоточением, и этим формирующим фактором усилия",
             "Iti iminā ca cittena, iminā ca samādhinā, iminā ca padhānasaṅkhārena":
                 "Таким образом, и этим умом, и этим сосредоточением, и этим формирующим фактором усилия",
             "Iti imāya ca vīmaṃsāya, iminā ca samādhinā, iminā ca padhānasaṅkhārena":
                 "Таким образом, и этой пытливостью, и этим сосредоточением, и этим формирующим фактором усилия"}

VERBS = {   # object + verb strings (the object first, «он», the verbs)
    "Imaṃ vīriyaṃ ārabhati samārabhati āsevati bhāveti bahulīkaroti.":
        "Это усердие он пробуждает, полностью пробуждает, практикует, развивает, многократно повторяет.",
    "Imaṃ chandaṃ janeti sañjaneti uṭṭhapeti samuṭṭhapeti nibbatteti abhinibbatteti.":
        "Это желание он порождает, полностью порождает, поднимает, полностью поднимает, вызывает, полностью вызывает.",
    "Imaṃ chandaṃ janeti sañjaneti uṭṭhapeti samuṭṭhapeti [uṭṭhāpeti samuṭṭhāpeti (syā.) evamuparipi] nibbatteti "
    "abhinibbatteti.":
        "Это желание он порождает, полностью порождает, поднимает, полностью поднимает [вариант написания (Syā.): "
        "uṭṭhāpeti samuṭṭhāpeti; так же и далее], вызывает, полностью вызывает.",
    "Imaṃ cittaṃ paggaṇhāti sampaggaṇhāti upatthambheti paccupatthambheti.":
        "Этот ум он напрягает, полностью напрягает, поддерживает, всячески поддерживает.",
    "Te dhamme āsevati bhāveti bahulīkaroti.": "Эти явления он практикует, развивает, многократно повторяет.",
    NIMITTA_P: NIMITTA,
}
VIHARATI = "Он принимает положения тела, живёт, оберегает себя, поддерживает себя, продлевает существование, действует, пребывает."
VINITA = ("Таким образом, и эта алчность, и это уныние в этом мире устранены, полностью устранены, успокоены, усмирены, "
          "умиротворены, угасли, полностью угасли, прекращены, полностью прекращены, иссушены, полностью иссушены, "
          "сведены на нет.")
WORLD5 = "И пять совокупностей, служащих объектом цепляния, являются миром"    # Pañcapi upādānakkhandhā loko [ch. 4 words]
IDDHI = ("То, что у этих явлений есть сверхспособность, успех, преуспевание, полное преуспевание, обретение, получение, "
         "достижение, полное достижение, касание, непосредственное постижение, вхождение.")
THUS = "У того, кто таков, это"                                                 # Tathābhūtassa
AGG4 = ", ".join(S.AGG[a]["khandha"] for a in ("vedana", "sanna", "sankhara"))   # совокупность чувств, … формирующих факторов
VINN_K = S.AGG["vinnana"]["khandha"]
ROOTS_A = "Три неблагих корня – жадность, злоба, заблуждение."                  # pi-1 ^1-986
ROOTS_K = "Три благих корня – отсутствие жадности, отсутствие злобы, отсутствие заблуждения."   # pi-1 ^1-985
TADEKATTHA = "И омрачения, пребывающие вместе с ними."                          # pi-1 ^1-986 «и омрачения, пребывающие вместе с ними»
ASSOC = f"Связанные с ними {AGG4} и {VINN_K}"                                     # pi-1 ^1-985
ORIG = "порождённые ими телесное действие, речевое действие и умственное действие"   # pi-1 ^1-985
in_pi1(ROOTS_A[:-1], ROOTS_K[:-1], low(TADEKATTHA[:-1]), low(ASSOC), ORIG)
STHITI = ("То, что есть сохранение, есть неутрата; то, что есть неутрата, есть умножение; то, что есть умножение, есть "
          "обширность; то, что есть обширность, есть развитие; то, что есть развитие, есть завершённость.")

SENT = {
    "Iriyati vattati pāleti yapeti yāpeti carati viharati.": VIHARATI,
    "Sveva kāyo loko.": "Само это тело является миром.",
    "Sāyeva vedanā loko.": "Само это чувство является миром.",
    "Taṃyeva cittaṃ loko.": "Сам этот ум является миром.",
    "Teva dhammā loko.": "Сами эти явления являются миром.",
    "Pañcapi upādānakkhandhā loko.": WORLD5 + ".",
    "Pañcapi upādānakkhandhā loko – tattha katamā abhijjhā?":           # as written (reported)
        f"{WORLD5} {DASH} {low(TATTHA)} {TERM['abhijjhā'][0]}?",
    "Iti ayañca abhijjhā idañca domanassaṃ imamhi loke vinītā honti paṭivinītā santā samitā vūpasantā atthaṅgatā "
    "abbhatthaṅgatā appitā byappitā sositā visositā byantīkatā.": VINITA,
    "Ime dhammā kusalā.": "Это благие явления.",
    "Yā ṭhiti so asammoso, yo asammoso so bhiyyobhāvo, yo bhiyyobhāvo taṃ vepullaṃ, yaṃ vepullaṃ sā bhāvanā, yā bhāvanā "
    "sā pāripūrī.": STHITI,
    "Yā tesaṃ dhammānaṃ iddhi samiddhi ijjhanā samijjhanā lābho paṭilābho patti sampatti phusanā sacchikiriyā "
    "upasampadā.": IDDHI,
    "Tathābhūtassa vedanākkhandho, saññākkhandho, saṅkhārakkhandho, viññāṇakkhandho.": f"{THUS} {AGG4} и {VINN_K}.",
    "Tathābhūtassa vedanākkhandho…pe… viññāṇakkhandho.": f"{THUS} {S.AGG['vedana']['khandha']}… {VINN_K}.",
    "Tathābhūtassa phasso…pe… paggāho avikkhepo.": f"{THUS} контакт… напряжение сил, отсутствие отвлечения.",
    "Tīṇi akusalamūlāni – lobho, doso, moho.": ROOTS_A,
    "Tadekaṭṭhā ca kilesā.": TADEKATTHA,
    "Tīṇi kusalamūlāni – alobho, adoso, amoho.": ROOTS_K,
    "Taṃsampayutto vedanākkhandho, saññākkhandho, saṅkhārakkhandho, viññāṇakkhandho.": ASSOC + ".",
}
in_pi1("напряжение сил", "есть отсутствие отвлечения")
FIXES = [   # (Pāli as written, as meant): punctuation / spelling slips only, all reported
    ("Tathābhūtasa ", "Tathābhūtassa "),                                     # ^2-450
    ("viññāṇakhandho.", "viññāṇakkhandho."),                                  # ^2-443
    ("maggariyāpannaṃ", "maggapariyāpannaṃ"),                                 # ^2-459
    ("abhisaññahitvā", "abhisaññūhitvā"),                                     # ^2-432 (one-off spelling)
    ("samannāgato\"ti", "samannāgato\"ti."),                                  # ^2-455 final full stop
    ("samannāgato\"ti..", "samannāgato\"ti."),
    ("Siyā vipākā siyā vipākadhammadhammā", "Siyā vipākā, siyā vipākadhammadhammā"),   # ^2-388 comma
    ("sāsavācātipi", "sāsavā cātipi"), ("āsavasampayuttācātipi", "āsavasampayuttā cātipi"),   # ^2-389 spaces
    ("Anupassīti …pe…", "Anupassīti…pe…"),                                    # ^2-364 space
    (" …pe…", "…pe…"),                                                         # stray spaces before …pe…
]

# ================================================================ 5. four efforts
SP_P = ["anuppannānaṃ pāpakānaṃ akusalānaṃ dhammānaṃ anuppādāya", "uppannānaṃ pāpakānaṃ akusalānaṃ dhammānaṃ pahānāya",
        "anuppannānaṃ kusalānaṃ dhammānaṃ uppādāya",
        "uppannānaṃ kusalānaṃ dhammānaṃ ṭhitiyā asammosāya bhiyyobhāvāya vepullāya bhāvanāya pāripūriyā"]
SP_R = F.SP                      # pi-1 ^1-1377
EFFORT_P = "chandaṃ janeti vāyamati vīriyaṃ ārabhati cittaṃ paggaṇhāti padahati"
SP_THESE = ["ради невозникновения этих невозникших дурных неблагих явлений",
            "ради устранения этих возникших дурных неблагих явлений",
            "ради возникновения этих невозникших благих явлений",
            "ради сохранения, неутраты, умножения, обширности, развития и завершённости этих возникших благих явлений"]
for _a, _b in zip(SP_R, SP_THESE):
    assert _b.replace("этих ", "") == _a


def efforts(body):
    """'P0 EFFORT, P1 EFFORT, …' / 'P0 EFFORT, P1…pe… P2…pe… P3 EFFORT' -> Russian («; » / «… »)."""
    parts = re.split(r"(, |…pe… )", body)
    out = []
    for i, x in enumerate(parts):
        if i % 2:
            out.append("; " if x == ", " else "… ")
            continue
        eff = x.endswith(" " + EFFORT_P)
        p = x[:-len(EFFORT_P) - 1] if eff else x
        r = SP_R[SP_P.index(p)]
        out.append(r + (" " + SP_EFFORT if eff else ""))
    return "".join(out)


# ================================================================ 6. lokuttara sentences (Abhidhammabhājanīya)
LOK_P = F.LOKUTTARA_P[:-len(", tasmiṃ samaye ")]          # Idha bhikkhu yasmiṃ samaye lokuttaraṃ … dandhābhiññaṃ
LOK_R = F.LOKUTTARA[:-2]                                  # Вот в то время, когда монах … и пребывает в нём
assert F.LOKUTTARA.endswith("и пребывает в нём, ")
VIP_P = ("Tasseva lokuttarassa kusalassa jhānassa katattā bhāvitattā vipākaṃ vivicceva kāmehi…pe… paṭhamaṃ jhānaṃ "
         "upasampajja viharati dukkhapaṭipadaṃ dandhābhiññaṃ suññataṃ")
VIP_R = edit(G.LOK_V_SUNNA, "когда кто-либо,", "когда монах,")   # pi-1 ^1-505, «кто-либо» -> «монах» (as ch. 4)
assert VIP_R in edit(PI1["^1-505"], "когда кто-либо,", "когда монах,")


def jhana_tail(rest):
    """the Pāli after LOK_P / VIP_P (Russian continues after «… и пребывает в нём»)."""
    m = re.match(r"^ (kāye|vedanāsu|citte|dhammesu) \S+nupassī, (.+)$", rest)
    pre = ""
    if m:
        d = next(k for k in DOMS if DOM[k][0] == m.group(1))
        pre, rest = ", " + dwell_jhana(d), ", " + m.group(2)
    if rest == ", tasmiṃ samaye phasso hoti…pe… avikkhepo hoti.":
        return pre + ", " + F.TAIL_SENT["phasso hoti…pe… avikkhepo hoti."]
    m = re.match(r"^, tasmiṃ samaye (.+)\.$", rest)
    if m:
        x = m.group(1)
        m2 = re.match(r"^(\S+)samādhipadhānasaṅkhārasamannāgataṃ iddhipādaṃ bhāveti$", x)
        if m2:
            k = next(k for k in IP if IP[k][0] == m2.group(1))
            return f"{pre}, в это время он развивает {IDDHIPADA[1]}, {ip_adj(k)}."
        return f"{pre}, в это время он {efforts(x)}."
    m = re.match(r"^, ((?:yo|yā|yaṃ) tasmiṃ samaye .+?) – (?:ayaṃ|idaṃ) vuccati (\"?)(.+?)\"?\.$", rest)
    if m:
        body = cap(m.group(1))
        return f"{pre}, {defn(body, tasmim=True)}, {DASH} {called(TERM[m.group(3)][1], bool(m.group(2)))}."
    raise KeyError("jhana tail: " + rest[:100])


# ================================================================ 7. sentence dispatcher
SPLIT = re.compile(r'(?<=[.?])\s+(?=[A-ZĀĪŪṬḌÑṆṄ"])')
DEF_RE = re.compile(r'^(.+?),? – (ayaṃ|idaṃ) vuccati ("?)(.+?)"?\.$')


def sentence(s):
    if s in SENT:
        return SENT[s]
    if s in VERBS:
        return VERBS[s]
    for f in (kaya_sentence, feel_sentence, citta_sentence, upasamharati):
        r = f(s)
        if r:
            return r
    if s.startswith(LOK_P):
        return LOK_R + jhana_tail(s[len(LOK_P):])
    if s.startswith(VIP_P):
        return VIP_R + jhana_tail(s[len(VIP_P):])
    if re.match(r"^(Idha bhikkhu )?[Ss]antaṃ vā(?:ssa)? ", s):
        mode = "ext" if " vāssa " in s else ("int" if " ajjhattaṃ " in s else "both")
        return dhamma_sentence(s, mode)
    m = re.match(r"^Kathañca bhikkhu (.+)\?$", s)
    if m:
        return "Как монах " + how(m.group(1)) + "?"
    m = re.match(r"^Evaṃ bhikkhu ajjhattabahiddhā (\S+) \S+nupassī viharati " + SATI_TAIL_P + r"\.$", s)
    if m:
        d = next(k for k in DOMS if DOM[k][0] == m.group(1))
        return f"Так монах {dwell(d, 'ajjhattabahiddhā')}, {SATI_TAIL}."
    m = re.match(r"^Tattha katam(?:o|ā|aṃ|e) (.+?)( \[katamaṃ ātāpaṃ \(sabbattha\)\])?\?$", s)
    if m:
        var = " [вариант чтения (все издания): katamaṃ ātāpaṃ]" if m.group(2) else ""
        return f"{TATTHA} {TERM[m.group(1)][0]}{var}?"
    m = re.match(r'^Tena vuccati "(.+?)"(n?)ti\.$', s)
    if m:
        return f"{cap(G.TENA)} «{lemma(m.group(1) + ('ṃ' if m.group(2) else ''))}»."
    m = re.match(r'^(?:Ayaṃ|Idaṃ) vuccati "(.+)"\.$|^Ime vuccanti "(.+)"\.$', s)
    if m:
        return cap(called(TERM[m.group(1) or m.group(2)][1])) + "."
    m = re.match(r"^Avasesā dhammā (\S+)sampayuttā\.$", s)
    if m:
        return f"Остальные явления связаны с {SAMP[m.group(1)]}."
    m = re.match(r"^(.+?) upeto hoti( samupeto upāgato samupāgato upapanno sampanno samannāgato|…pe… samannāgato)\.$", s)
    if m:
        return f"{UPETO_INS[m.group(1)]} {UPETO_FULL if m.group(2).startswith(' ') else UPETO_PE}."
    m = re.match(r"^(Iti imesaṃ )(.+) " + EFFORT_P + r"\.$", s)
    if m:
        p = m.group(2)
        return f"Таким образом, {SP_THESE[SP_P.index(p)]} он {SP_EFFORT}."
    m = re.match(r"^So (.+)\.$", s)
    if m and m.group(1).startswith(tuple(SP_P)):
        return f"Он {efforts(m.group(1))}."
    m = re.match(r"^Taṃsampayutto vedanākkhandho, saññākkhandho, saṅkhārakkhandho, viññāṇakkhandho, taṃsamuṭṭhānaṃ "
                 r'kāyakammaṃ vacīkammaṃ manokammaṃ – ime vuccanti "(.+)"\.$', s)
    if m:
        return f"{ASSOC}; {ORIG} {DASH} {called(TERM[m.group(1)][1])}."
    m = re.match(r'^Taṃsamuṭṭhānaṃ kāyakammaṃ, vacīkammaṃ, manokammaṃ – ime vuccanti "(.+)"\.$', s)
    if m:
        return f"{cap(ORIG)} {DASH} {called(TERM[m.group(1)][1])}."
    m = re.match(r"^(\S+) ce bhikkhu adhipatiṃ karitvā labhati samādhiṃ,? labhati cittassekaggataṃ"
                 r"( \[cittassa ekaggataṃ \(sī\. syā\.\)\])? – ayaṃ vuccati \"(\S+)samādhi\"\.$", s)
    if m:
        k = next(k for k in IP if IP[k][1] == m.group(1))
        assert IP[k][0] == m.group(3)
        var = " [вариант написания (Sī., Syā.): cittassa ekaggataṃ]" if m.group(2) else ""
        return (f"Если монах, сделав {IP[k][2]} главенствующ{IP[k][3]}, обретает сосредоточение, обретает "
                f"однонаправленность ума{var}, {DASH} {called(TERM[IP[k][0] + 'samādhi'][1])}.")
    m = re.match(r"^Iti ayañca (\S+)samādhi, ime ca padhānasaṅkhārā(\.|; (.+))$", s)
    if m:
        k = next(k for k in IP if IP[k][0] == m.group(1))
        head = f"Таким образом, есть и это {TERM[IP[k][0] + 'samādhi'][0]}, и эти {TERM['padhānasaṅkhārā'][0]}"
        if m.group(2) == ".":
            return head + "."
        return head + "; " + low(together(cap(m.group(3)), k))
    if s.startswith("Tadekajjhaṃ "):
        k = next(k for k in IP if IP[k][0] + "samādhipadhānasaṅkhārotveva" in s)
        return together(s, k)
    m = re.match(r"^Cattāro iddhipādā – (.+)\.$", s)
    if m:
        return ip_opener(s)
    m = re.match(r'^"?(.+?)"?(n?)ti\.$', s)
    if m and low(m.group(1) + ("ṃ" if m.group(2) else "")) in LEMMA:
        return f"«{cap(lemma(m.group(1) + ('ṃ' if m.group(2) else '')))}»."
    if "ti…pe…" in s and " – " not in s:   # Anupassīti…pe… viharatīti…pe… … abhijjhādomanassanti.
        items = s[:-1].split("…pe… ")
        ru = []
        for x in items:
            m = re.match(r"^(.+?)(n?)ti$", x)
            r = lemma(m.group(1) + ('ṃ' if m.group(2) else ''))
            ru.append(f"«{cap(r) if not ru else r}»")
        return "… ".join(ru) + "."
    m = DEF_RE.match(s)
    if m and m.group(1) in DEF:
        return f"{DEF[m.group(1)]}, {DASH} {called(TERM[m.group(4)][1], bool(m.group(3)))}."
    raise KeyError("sentence: " + s[:120])


def together(s, k):
    m = re.match(r"^Tadekajjhaṃ abhisaññūhitvā abhisaṅkhipitvā (\S+)samādhipadhānasaṅkhārotveva saṅkhyaṃ"
                 r"( \[saṅkhaṃ \(sī\.\)\])? gacchati\.$", s)
    assert m and m.group(1) == IP[k][0], s
    var = " [вариант написания (Sī.): saṅkhaṃ]" if m.group(2) else ""
    return f"{cap(S.KHANDHA_TOGETHER['n'])}, получает название{var} «{ip_name(k)}»."


def how(x):
    """the question body after 'Kathañca bhikkhu'."""
    m = re.match(r"^(?:(ajjhattaṃ|bahiddhā|ajjhattabahiddhā) )?(\S+) \S+nupassī viharati$", x)
    if m:
        d = next(k for k in DOMS if DOM[k][0] == m.group(2))
        return dwell(d, m.group(1) or "")
    m = re.match(r"^(\S+)samādhipadhānasaṅkhārasamannāgataṃ iddhipādaṃ bhāveti$", x)
    if m:
        k = next(k for k in IP if IP[k][0] == m.group(1))
        return f"развивает {IDDHIPADA[1]}, {ip_adj(k)}"
    return efforts(x)


def ip_opener(s):
    """Cattāro iddhipādā – … (^2-431, ^2-444, ^2-457, ^2-462)."""
    full = ", ".join(f"{IP[k][0]}samādhipadhānasaṅkhārasamannāgataṃ iddhipādaṃ bhāveti" for k in IP)
    if s == f"Cattāro iddhipādā – idha bhikkhu {full}.":
        return (f"{FOUR_IP} {DASH} вот монах " + "; ".join(f"развивает {IDDHIPADA[1]}, {ip_adj(k)}" for k in IP) + ".")
    if s == "Cattāro iddhipādā – chandiddhipādo, vīriyiddhipādo, cittiddhipādo, vīmaṃsiddhipādo.":
        return f"{FOUR_IP} {DASH} " + T.enum([IP_NAME[k][0] for k in IP]) + "."
    if s == ("Cattāro iddhipādā – idha bhikkhu chandasamādhipadhānasaṅkhārasamannāgataṃ iddhipādaṃ bhāveti, "
             "vīriyasamādhi…pe… cittasamādhi…pe… vīmaṃsāsamādhipadhānasaṅkhārasamannāgataṃ iddhipādaṃ bhāveti."):
        return (f"{FOUR_IP} {DASH} вот монах развивает {IDDHIPADA[1]}, {ip_adj('chanda')}; "
                f"{TERM['vīriyasamādhi'][1]}… {TERM['cittasamādhi'][1]}… развивает {IDDHIPADA[1]}, {ip_adj('vīmaṃsā')}.")
    raise KeyError("ip opener: " + s[:80])


def text_line(t):
    for a, b in FIXES:
        t = t.replace(a, b)
    if t.startswith("Cattāro satipaṭṭhānā – "):
        for kind in ("sutta", "abhi", "q"):
            p, r = opener_sp(kind)
            if p == t:
                return r
        raise KeyError("sp opener: " + t[:80])
    if t.startswith("Cattāro sammappadhānā – idha bhikkhu "):
        return f"{FOUR_SPP} {DASH} вот монах {efforts(t[len('Cattāro sammappadhānā – idha bhikkhu '):-1])}."
    return " ".join(sentence(s) for s in SPLIT.split(t))


# ================================================================ 8. Pañhāpucchaka
T.new("kusala_eva", ["kusalāyeva"], None, "является только благим", "являются только благими")
T.new("na_maggadhipati", ["na maggādhipatino", "na maggādhipati"], None, "не находится под главенством пути",
      "не находятся под главенством пути")
for p, v in (("Vīmaṃsiddhipādo", (cap(IP_NAME["vīmaṃsā"][0]), "Пытливость как основу сверхспособностей", "sg", "f")),
             ("vīmaṃsiddhipādo", (IP_NAME["vīmaṃsā"][0], "пытливость как основу сверхспособностей", "sg", "f")),
             ("cittiddhipādo", (IP_NAME["citta"][0], "ум как основу сверхспособностей", "sg", "m")),
             ("Tayo iddhipādā", ("Три основы сверхспособностей", "Три основы сверхспособностей", "pl", None)),
             ("tayo iddhipādā", ("три основы сверхспособностей", "три основы сверхспособностей", "pl", None))):
    assert p not in T.SUBJ2 or T.SUBJ2[p] == v, p
    T.SUBJ2[p] = v
T.SUBJ_RE2 = re.compile(r"^(" + "|".join(map(re.escape, sorted(T.SUBJ2, key=len, reverse=True))) + r") (.+)$")
T.alias("hetu_sahetuka", "hetu ceva sahetuko ca")
T.alias("hetu_hetusampayutta", "hetu ceva hetusampayutto ca")
T.alias("acetasika", "acetasiko")
T.alias("no_css", "no cittasaṃsaṭṭhasamuṭṭhāno")
Q_MASC = {"связанную с умом": "связанный с умом", "не связанную с умом": "не связанный с умом",
          "соединённую с умом": "соединённый с умом", "не соединённую с умом": "не соединённый с умом"}
QFIX = [("Araṇāti.", "Araṇā.")]        # closing "ti" of the question list (as ch. 2–5)
LABELS = {
    "##### Tikaṃ": B.LABELS["##### Tikaṃ"], "##### Dukaṃ": B.LABELS["##### Dukaṃ"],
    "Pañhāpucchakaṃ.": SEC["Pañhāpucchakaṃ"] + ".",
    "Catunnaṃ satipaṭṭhānānaṃ kati kusalā, kati akusalā, kati abyākatā…pe… kati saraṇā, kati araṇā?":
        T.how_many_q("четырёх основ осознанности"),
    "Catunnaṃ sammappadhānānaṃ kati kusalā, kati akusalā, kati abyākatā…pe… kati saraṇā, kati araṇā?":
        T.how_many_q("четырёх правильных усилий"),
    "Catunnaṃ iddhipādānaṃ kati kusalā, kati akusalā, kati abyākatā…pe… kati saraṇā, kati araṇā?":
        T.how_many_q("четырёх основ сверхспособностей"),
    "Satipaṭṭhānavibhaṅgo niṭṭhito.": S.CHAPTER_CLOSING.format(title=S.CHAPTER_TITLES[7]),
    "Sammappadhānavibhaṅgo niṭṭhito.": S.CHAPTER_CLOSING.format(title=S.CHAPTER_TITLES[8]),
    "Iddhipādavibhaṅgo niṭṭhito.": S.CHAPTER_CLOSING.format(title=S.CHAPTER_TITLES[9]),
}
UNQ_NV = re.compile(r"^(siyā )?na vattabb(?:o|ā|aṃ) (.+?)(n?ti(?:pi)?)$")
UNQ_TI = re.compile(r"^(.+?)(n?ti(?:pi)?)$")


def quote(text, ti, st):
    qt = T.quote2(f'"{text}"{ti}', st)
    if st["num"] == "sg" and st["g"] == "m":
        for a, b in Q_MASC.items():
            qt = qt.replace(f"«{a}»", f"«{b}»")
    return qt


def q_chunk(c, st):
    """one comma-separated chunk; unquoted 'na vattabbā X(n)ti(pi)' (pi-2 ch. 7–9 have no dash and no quotes there)."""
    subj = None
    m = T.SUBJ_RE2.match(c)
    rest = c
    if m:
        subj = T.SUBJ2[m.group(1)]
        rest = m.group(2)
    m = UNQ_NV.match(low(rest))
    if m:
        if subj:
            st["num"], st["g"] = subj[2], subj[3]
        st["nv"] = True
        qt = quote(m.group(2), m.group(3), st)
        pron = T.PRON[(st["num"], st["g"])]
        if m.group(1):
            return f"иногда {pron} {NV} {qt}"
        return f"{subj[1] if subj else pron} {NV} {qt}"
    if st.get("nv") and not subj:
        m = UNQ_TI.match(rest)
        if m and m.group(2).endswith("pi"):
            return quote(m.group(1), m.group(2), st)
    st["nv"] = False
    return F.chunk(c, st)


def q_line(t):
    if t in LABELS:
        return LABELS[t]
    if t.startswith("Cattāro "):
        return text_line(t)
    for a, b in FIXES + QFIX:
        t = t.replace(a, b)
    out = []
    for sent in re.split(r"(?<=\.) (?=[A-ZĀ])", t):
        assert sent.endswith("."), sent[-40:]
        body = sent[:-1].replace("…pe…", PE)
        parts = re.split(r"(, |; |\x01 ?)", body)
        st = {"num": "pl", "g": None}
        ru = []
        for i, x in enumerate(parts):
            if i % 2:
                ru.append(x.replace(PE, "…"))
            else:
                ru.append(q_chunk(x, st))
        out.append(cap("".join(ru)) + ".")
    return " ".join(out)


# ================================================================ 9. chapters
HEAD5 = {"Kāyānupassanāniddeso": "Разъяснение созерцания тела", "Vedanānupassanāniddeso": "Разъяснение созерцания чувств",
         "Cittānupassanāniddeso": "Разъяснение созерцания ума", "Dhammānupassanāniddeso": "Разъяснение созерцания явлений"}
for k in IP:
    HEAD5[cap(IP_PALI[k])] = cap(IP_NAME[k][0])
TITLE = {"Satipaṭṭhānavibhaṅgo": 7, "Sammappadhānavibhaṅgo": 8, "Iddhipādavibhaṅgo": 9}


def build_chapter(pali):
    out = []
    section = None
    for t in pali:
        if t.startswith("### "):
            out.append("### " + S.CHAPTER_TITLES[TITLE[t[4:]]])
        elif t.startswith("#### "):
            section = t[5:]
            out.append("#### " + SEC[section])
        elif t.startswith("##### ") and t in LABELS:
            out.append(LABELS[t])
        elif t.startswith("##### "):
            out.append("##### " + HEAD5[t[6:]])
        elif t.endswith(".") and t[:-1] in HEAD5:
            out.append(HEAD5[t[:-1]] + ".")
        elif t.endswith(".") and t[:-1] in SEC:
            out.append(SEC[t[:-1]] + ".")
        elif section == "Pañhāpucchakaṃ":
            out.append(q_line(t))
        else:
            out.append(text_line(t))
    return out


def build(fn):
    pali = open(os.path.join(S.PALI_DIR, fn), encoding="utf-8").read().rstrip("\n").split("\n")
    nonempty = [S.ID.sub("", l).rstrip() for l in pali if l.strip()]
    ru = build_chapter(nonempty)
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
    for fn in ("7-satipatthanavibhango.md", "8-sammappadhanavibhango.md", "9-iddhipadavibhango.md"):
        build(fn)


if __name__ == "__main__":
    main()
