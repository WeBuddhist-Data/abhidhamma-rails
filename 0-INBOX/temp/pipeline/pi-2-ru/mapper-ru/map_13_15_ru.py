"""Build the Pāli->Russian keyword maps for pi-2 (Vibhaṅga) chapters 13-appamannavibhango,
14-sikkhapadavibhango and 15-patisambhidavibhango.

usage: python -I -X utf8 map_13_15_ru.py [PART ...]           (writes <part>.mapped.md and verifies; default: all three,
                                                             in book order)
       python -I -X utf8 map_13_15_ru.py --dump PART [--miss]  (prints every keyword=value with a presence flag;
                                                             --miss: only the flagged ones; no writing)

Resolution order per keyword: OVERRIDES[bid][kw]  ->  context rules (resolve())  ->  per-chapter table (CH13 / CH14 /
CH15)  ->  T (this file: map_10_12_ru.T + the chapter 13-15 additions)  ->  pi-1 CH2 / MATRIX.
Conventions: ru-map-conventions-pi2.md (+ the pi-1 file), notes-map-2-3.md … notes-map-10-12.md; new decisions:
notes-map-13-15.md.
"""
import pathlib
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import map_10_12_ru as M1012  # noqa: E402  (read-only: its table T, CH12, _PANHA, CHOICES, EXC)
from map_common_pi2_ru import (GAP, NDE, build_part, hetuko_value, lc, present,  # noqa: E402,F401
                               read_keywords, read_pali, read_russian, value, verify)

PARTS = ["13-appamannavibhango", "14-sikkhapadavibhango", "15-patisambhidavibhango"]

# ---------------------------------------------------------------------------- table
T = dict(M1012.T)
assert not any(v.startswith("классификация") for v in T.values())

T.update({
    # ================================================================ ch. 13 Appamaññā
    # ---- names (pi-3 appamaññā = безмерное состояние; pi-1 mettā / muditā; stem singular as Khandha)
    "appamaññā": "безмерное состояние", "appamaññāyo": "безмерные состояния",
    "appamaññānaṃ": "безмерные состояния", "mettā": "доброжелательность", "muditā": "сорадование",
    # ---- 2-642 / 2-699: «… пребывает, наполнив одну сторону света умом, сопровождаемым доброжелательностью, так же
    # вторую … Так вверх, вниз, в стороны, повсюду, ко всем как к себе, он пребывает, наполнив весь мир умом, …
    # обширным, возвышенным, безмерным, свободным от вражды, свободным от неприязни»
    "sahagatena": "сопровождаемый",
    "mettāsahagatena": "сопровождаемый доброжелательностью",
    "karuṇāsahagatena": "сопровождаемый состраданием",
    "muditāsahagatena": "сопровождаемый сорадованием",
    "upekkhāsahagatena": "сопровождаемый невозмутимостью",
    "mettāsahagatena cetasā": "ум сопровождаемый доброжелательностью",
    "karuṇāsahagatena cetasā": "ум сопровождаемый состраданием",
    "muditāsahagatena cetasā": "ум сопровождаемый сорадованием",
    "upekkhāsahagatena cetasā": "ум сопровождаемый невозмутимостью",
    # gerund kept, as disvā = увидев / sutvā = услышав (pi-1, pi-4); 2-645 glosses the gerund itself
    "pharitvā": "наполнив", "pharitvā viharati": "пребывать наполнив",
    "ekaṃ disaṃ pharitvā": "наполнив одну сторону света", "adhimuccitvā": "утвердившись в решимости",
    "pharitvā adhimuccitvā": "наполнив утвердившись в решимости",
    "disaṃ": "сторона света", "tathā": "так же", "tathā catutthaṃ": "так же четвёртый",
    "catutthaṃ disaṃ": "четвёртая сторона света", "tiriyaṃ": "в стороны", "vidisaṃ": "промежуточная сторона света",
    "sabbadhi": "повсюду", "sabbattatāya": "ко всем как к себе", "sabbāvantaṃ": "весь",
    "sabbāvantaṃ lokaṃ": "весь мир", "sabbāvantaṃ loka": "весь мир",
    "vipulena": "обширный", "vipulaṃ": "обширный", "mahaggatena": "возвышенный", "mahaggataṃ": "возвышенный",
    "appamāṇena": "безмерный", "appamāṇaṃ": "безмерный",
    "averena": "свободный от вражды", "avero": "свободный от вражды",
    "abyāpajjena": "свободный от неприязни",
    # ---- 2-643 …: «Подобно тому как кто-либо, увидев одного человека, дорогого и приятного, проникся бы к нему
    # доброжелательностью, так же он наполняет доброжелательностью всех существ»
    "puggalaṃ": "человек", "piyaṃ": "дорогой", "disvā": "увидев", "pharati": "наполнять",
    "mettāyeyya": "проникнуться доброжелательностью", "karuṇāyeyya": "проникнуться состраданием",
    "mudito": "порадоваться", "duggataṃ": "бедствующий", "durūpetaṃ": "обездоленный",
    "mettāyitattaṃ": "состояние доброжелательности", "muditāyitattaṃ": "состояние сорадования",
    "karuṇāyanā": "проявление сострадания", "muditāyanā": "проявление сорадования",
    "upekkhāyanā": "проявление невозмутимости",
    "muditācetovimutti": "освобождение ума сорадованием",
    "upekkhācetovimutti": "освобождение ума невозмутимостью",
    "ceto": "ум",
    # ---- 2-644: «или восточную сторону света, или западную …, или промежуточную сторону света»
    "puratthimaṃ": "восточный", "puratthimaṃ vā disaṃ": "или восточная сторона света",
    "pacchimaṃ vā disaṃ": "или западная сторона света", "uttaraṃ vā disaṃ": "или северная сторона света",
    "dakkhiṇaṃ": "южный", "dakkhiṇaṃ vā disaṃ": "или южная сторона света",
    # ---- 2-648: «Это выражение, охватывающее всё»
    "pariyādāya": "охватывающий всё", "vacana": "выражение",
    # ---- Abhidhamma (2-684 …)
    "mettāsahagataṃ": "сопровождаемый доброжелательностью", "karuṇāsahagataṃ": "сопровождаемый состраданием",
    "muditāsahagataṃ": "сопровождаемый сорадованием", "vicārānaṃ": "удержание мысли", "pītiyā": "восторг",
    # ---- Pañhāpucchaka 2-701: nevasekkhanāsekkhā «не относятся ни к обучающимся, ни к завершившим обучение»
    # (as ch. 4 2-217)
    "āsekkhā": "относящийся" + GAP + "к завершившим обучение",
    # ================================================================ ch. 14 Sikkhāpada
    # ---- names: «правило обучения о воздержании от …» (sikkhā = обучение, pi-4/5; pada = правило, pi-5)
    "sikkhāpada": "правило обучения", "sikkhāpadaṃ": "правило обучения", "sikkhāpadāni": "правила обучения",
    "sikkhāpadānaṃ": "правила обучения", "pada": "правило", "padaṃ": "правило", "padāni": "правила",
    "padānaṃ": "правила", "veramaṇī sikkhāpadaṃ": "правило обучения о воздержании",
    # ---- precepts (pi-4 / pi-5): «употребления спиртного, браги и опьяняющих напитков, ведущего к беспечности»
    "surā": "спиртное", "meraya": "брага", "majja": "опьяняющие напитки", "pamāda": "беспечность",
    "ṭṭhānā": "ведущий", "vādā": "ложь",
    # ---- virati string (pi-1, ch. 4 / 11): «отстранение, воздержание, полное воздержание, уклонение, неделание,
    # несовершение, невпадение в проступок, непереступание границы, разрушение моста»
    "akiriyā": "неделание", "akaraṇaṃ": "несовершение", "anajjhāpatti": "невпадение в проступок",
    "anatikkamo": "непереступание", "velā": "граница", "ārati": "отстранение", "paṭivirati": "полное воздержание",
    "setu": "мост", "ghāto": "разрушение", "ātipātā": "убийство", "ādānā": "взятие",
    "micchācārā": "неправильное поведение",
    # ---- «низший… средний… высший… с преобладанием желания… усердия… ума… пытливости»
    "ādhipateyyaṃ": "преобладание", "chandādhipateyyaṃ": "с преобладанием желания",
    "vīriyādhipateyyaṃ": "с преобладанием усердия", "cittādhipateyyaṃ": "с преобладанием ума",
    "vīmaṃsādhipateyyaṃ": "с преобладанием пытливости", "majjhimaṃ": "средний",
    "kāmāvacare": "относящийся к миру чувственных желаний", "āvacare": "относящийся к миру",
    # ---- 2-712 / 2-713: «Какие явления являются обучением? … Эти явления являются обучением»
    "sikkhā": "обучение", "dhammā sikkhā": "явления являющиеся обучением",
    # «имеющий объектом видимую форму… или объект ума, или что бы то ни было» (pi-1 yaṃ yaṃ = что бы то ни было)
    "yaṃ yaṃ vā panārabbha": "или что бы то ни было", "cetanāya": "намерение",
    # «развивает надмирское медитативное погружение»
    "jhānaṃ bhāveti": "развивать" + GAP + "медитативное погружение", "lokuttaraṃ": "надмирский",
    # ---- Pañhāpucchaka 2-716: «Являются только благими»
    "kusalāyeva": "только благой", "parittā": "ограниченный",
    # ================================================================ ch. 15 Paṭisambhidā
    # ---- names (pi-5 paṭisambhidā = аналитическое знание): «аналитическое знание смысла / явлений / выражений /
    # находчивости»
    "paṭisambhidā": "аналитическое знание", "paṭisambhidānaṃ": "аналитические знания",
    "atthapaṭisambhidā": "аналитическое знание смысла", "dhammapaṭisambhidā": "аналитическое знание явлений",
    "niruttipaṭisambhidā": "аналитическое знание выражений",
    "paṭibhānapaṭisambhidā": "аналитическое знание находчивости",
    "paṭisambhidā aniyatā": "аналитическое знание" + GAP + "непредопределённый",   # «Три аналитических знания
    # являются непредопределёнными» (as khandhā siyā / Rūpakkhandho hetuvippayutto)
    "attha": "смысл", "atthe": "смысл", "atthaṃ": "смысл", "nirutti": "выражение", "niruttiyā": "выражение",
    "paṭibhāna": "находчивость", "dhamme": "явление",
    # «знание высказывания этого выражения явлений» (dhammaniruttābhilāpe); «знание знаний» (ñāṇesu ñāṇaṃ)
    "ābhilāpe": "высказывание", "ñāṇaṃ": "знание", "ñāṇesu": "знания",
    # ---- section names: «Раздел обобщения / об истинах / о причине / о явлениях / о возникновении в зависимости от
    # условий / об изучении Учения / о благом / о неблагом / о функциональном»
    "vāro": "раздел", "saṅgaha": "обобщение", "saṅgahavāro": "раздел обобщения", "sacca": "истина",
    "saccavāro": "раздел об истинах", "dhammavāro": "раздел о явлениях",
    "samuppāda": "возникновение", "samuppādavāro": "раздел о возникновении",
    "pariyatti": "изучение Учения", "pariyattivāro": "раздел об изучении Учения", "kiriya": "функциональный",
    # ---- 2-719 … 2-723 (pi-1 / ch. 4 / ch. 6 values)
    "dukkhe": "страдание", "nirodhe": "прекращение", "samudaye": "возникновение",
    "dukkhanirodhe": "прекращение страдания", "dukkhasamudaye": "возникновение страдания",
    "hetumhi": "причина", "phale": "плод",
    "jarāmaraṇe": "старение и смерть", "maraṇe": "смерть", "jarāmaraṇe ñāṇaṃ": "знание старения и смерти",
    "jarāmaraṇanirodhe": "прекращение старения и смерти", "jātiyā": "рождение", "bhave": "существование",
    "upādāne": "цепляние", "taṇhāya": "жажда", "phasse": "контакт", "āyatane": "сфера восприятия",
    "nāmarūpe": "умственное и материальная форма", "rūpe": "материальная форма", "viññāṇe": "сознание",
    "saṅkhāresu": "формирующие факторы", "viññāṇe ñāṇaṃ": "знание сознания",
    "saṅkhāresu ñāṇaṃ": "знание формирующих факторов", "saṅkhāranirodhe": "прекращение формирующих факторов",
    # ---- 2-724 (pi-4 nine-limbed teaching; here «беседы, прозу со стихами, разъяснения, строфы, вдохновенные
    # изречения, изречения «Так было сказано», истории о прошлых рождениях, рассказы о чудесном, вопросы и ответы»)
    "suttaṃ": "беседы", "geyyaṃ": "проза со стихами", "veyyākaraṇaṃ": "разъяснения", "gāthaṃ": "строфы",
    "udānaṃ": "вдохновенные изречения", "itivuttakaṃ": "изречения Так было сказано",
    "jātakaṃ": "истории о прошлых рождениях", "abbhutadhammaṃ": "рассказы о чудесном", "abbhuta": "чудесный",
    "vedallaṃ": "вопросы и ответы", "jānāti": "знать", "bhāsitassa": "сказанное",
    # ---- 2-725 …: «которым эти явления обозначаются» / «Эти знания проясняют этот смысл» (finite verb ->
    # infinitive; the subject noun kept, as Rūpakkhandho hetuvippayutto)
    "paññatti": "обозначаться", "dhammānaṃ paññatti": "явления обозначаться",
    "jotakānī": "прояснять", "idamatthajotakānī": "прояснять этот смысл",
    "ñāṇāni idamatthajotakānī": "знания прояснять этот смысл",
    "yaṃ yaṃ": "что бы то ни было",
    "nevasaññānāsaññāyatanasaññāsahagataṃ": "в сопровождении восприятия сферы ни восприятия ни невосприятия",
    "diṭṭhigata": "приверженность воззрениям", "paṭigha": "неприязнь",
    # ---- vipāka / kiriya (pi-1 cittuppāda strings)
    "ye vā pana": "или же какой бы" + GAP + "ни", "samādhindriyaṃ": "способность сосредоточения",
    # ---- 2-746: «Три аналитических знания возникают в четырёх видах благого ума, относящегося к миру чувственных
    # желаний, связанных со знанием, и в четырёх видах функционального ума … возникает в четырёх путях и четырёх
    # плодах» (pi-1 kusalato / kiriyato = благой / функциональный ум, uppādesu = виды)
    "uppajjanti": "возникать", "uppajjati": "возникать", "uppādesu": "виды", "cittuppādesu": "виды" + GAP + "ума",
    "sampayuttesu": "связанный", "phalesu": "плоды", "maggesu": "пути", "kusalato": "благой ум",
    "kiriyato": "функциональный ум", "kāmāvacara": "относящийся к миру чувственных желаний",
    # ---- Pañhāpucchaka 2-749 / 2-750
    "apacayagāminī": "ведущий к убыванию",
    "anidassanaapaṭighā": "невидимый и не способный к соударению",   # spelling variant of -appaṭighā
    "apaṭighā": "не способный к соударению",
})

# ch. 13 values for keys that earlier chapters map differently (applied after the per-segment OVERRIDES)
CH13 = {
    "uttaraṃ": "северный",                               # «северную сторону света» (matrix fragment: надмирский)
    "āyatanaṃ": "сфера",                                 # manāyatanaṃ «сфера ума», as ch. 12
    "abyāpajjo": "свободный от неприязни",               # «то и свободно от неприязни» (pi-1 отсутствие неприязни)
}
# ch. 14: «правило обучения о воздержании от X» (ch. 4 / 11 «уклонение от X» for the path factors); veramaṇī alone =
# воздержание, уклонение where the segment has the virati string (context rule in resolve())
CH14 = {
    "veramaṇī": "воздержание",
    "pāṇātipātā veramaṇī": "воздержание от убийства живых существ",
    "adinnādānā veramaṇī": "воздержание от взятия того что не дано",
    "kāmesumicchācārā veramaṇī": "воздержание от неправильного поведения в чувственных удовольствиях",
    "musāvādā veramaṇī": "воздержание от лжи",
    "surāmerayamajjapamādaṭṭhānā veramaṇī":
        "воздержание от употребления спиртного браги и опьяняющих напитков ведущего к беспечности",
}
# ch. 15 values for keys that earlier chapters map differently
CH15 = {
    "sahagataṃ": "сопровождение",        # «в сопровождении восприятия сферы ни восприятия …» (as ch. 12)
    "āyatanaṃ": "сфера",                 # «сферу отсутствия чего-либо»
    "dukkha": "трудный",                 # dukkhapaṭipadaṃ «с трудным способом практики» (as ch. 12)
    "paṭicca": "в зависимости от условий",
    "dhammaṃ": "Учение",                 # 2-724 «монах знает Учение»
    # «элемент ума, функциональный, ни благой, ни неблагой» (singular text; ch. 4 plural text «ни благие, ни
    # неблагие»; masculine singular as ch. 12 / 13 neva kusalaṃ nākusalaṃ)
    "neva kusalā nākusalā": "ни благой ни неблагой",
}
CHAPTER = {PARTS[0]: CH13, PARTS[1]: CH14, PARTS[2]: CH15}

_PANHA = dict(M1012._PANHA)

# «Этот ум сопровождается этой доброжелательностью, рождён вместе с ней, соединён с ней, связан с ней» (as ch. 12
# 2-567: sahagataṃ = сопровождаться, saha = вместе)
_WITH = {"sahagataṃ": "сопровождаться", "saha": "вместе"}
# 2-721 «Знание тех явлений, которые родились, стали существовать, зародились, возникли, полностью возникли,
# проявились» (as ch. 12 _BORN); Ye = который
_BORN = {**M1012._BORN, "Ye": "который"}

OVERRIDES = {
    # ---- ch. 13
    "2-643": dict(_WITH), "2-649": dict(_WITH), "2-653": dict(_WITH), "2-659": dict(_WITH),
    "2-663": dict(_WITH), "2-669": dict(_WITH), "2-673": dict(_WITH), "2-679": dict(_WITH),
    "2-701": {**_PANHA, "appamāṇārammaṇā": "с безмерным объектом"},   # «ни как «явления с безмерным объектом»»
    "2-702": {**_PANHA, "hetu": "корень"},
    # ---- ch. 14
    "2-716": dict(_PANHA), "2-717": dict(_PANHA),
    # ---- ch. 15
    "2-15-1-3-0": {"Hetu": "причина"},                     # «Раздел о причине»
    "2-721": dict(_BORN),
    "2-725": {"sahagataṃ": "сопровождаемый"}, "2-726": {"sahagataṃ": "сопровождаемый"},
    "2-730": {"sahagataṃ": "сопровождаемый"}, "2-731": {"sahagataṃ": "сопровождаемый"},
    "2-732": {"sahagataṃ": "сопровождаемый"}, "2-741": {"sahagataṃ": "сопровождаемый", "dukkhaṃ": "боль"},
    "2-733": {"sahagataṃ": "сопровождаемый", "sukhaṃ": "удовольствие",
              "sukhasahagataṃ": "сопровождаемый удовольствием"},
    # «Три аналитических знания … имеют ограниченный / возвышенный / безмерный объект»
    "2-749": {**_PANHA, "parittārammaṇā": "имеющий ограниченный объект",
              "mahaggatārammaṇā": "имеющий возвышенный объект", "appamāṇārammaṇā": "имеющий безмерный объект"},
    "2-750": dict(_PANHA),
}
CHOICES = dict(M1012.CHOICES)
EXC = {**M1012.EXC,
       "mettāyeyya": "проникнуться ~ проникся бы (past stem without -ну-)",
       "karuṇāyeyya": "проникнуться ~ проникся бы (past stem without -ну-)",
       "vādā": "ложь ~ лжи (fleeting vowel), as musā / musāvādā (pi-4 vādā = ложь)"}
EXC_SEG = {}


def resolver_for(part):
    ru, pi = read_russian(part), read_pali(part)
    chap = CHAPTER.get(part, {})

    def resolve(bid, kw, kws):
        k = lc(kw)
        text = ru.get(bid, "")
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        if k in ov:
            return ov[k]
        lkws = {lc(x) for x in kws}
        if k == "vattati" and "iriyati" in lkws:
            return "жить"
        if k == "parisodheti" and "sodheti" in lkws:
            return "полностью очищать"
        # «отстранение, воздержание, полное воздержание, уклонение …» (ārati virati paṭivirati veramaṇī …), as pi-1
        if part == PARTS[1] and k == "veramaṇī" and "ārati" in lkws:
            return "уклонение"
        if k in chap:
            return chap[k]
        if kw == "hetuko":
            return hetuko_value(pi.get(bid, ""))
        if k in CHOICES:
            for cand in CHOICES[k]:
                if present(cand, text):
                    return cand
            return CHOICES[k][0]
        return value(kw, kws, T)
    return resolve


def allowed(part):
    out = {(bid, kw): EXC[lc(kw)] for bid, kws in read_keywords(part) for kw in kws if lc(kw) in EXC}
    out.update({(bid, kw): EXC_SEG[(bid, kw)] for bid, kws in read_keywords(part) for kw in kws
                if (bid, kw) in EXC_SEG})
    return out


def dump(part, only_miss=False):
    ru, res = read_russian(part), resolver_for(part)
    for bid, kws in read_keywords(part):
        out = []
        for kw in kws:
            try:
                v = res(bid, kw, kws)
            except KeyError:
                v = "???"
            bad = (v == "???" or not (v == NDE or present(v, ru.get(bid, "")))) and lc(kw) not in EXC \
                and (bid, kw) not in EXC_SEG
            if bad or not only_miss:
                out.append(f"{kw}={v}" + (" !!" if bad else ""))
        if out:
            print(f"[{bid}] " + " | ".join(out))


if __name__ == "__main__":
    args = sys.argv[1:]
    if args[:1] == ["--dump"]:
        for p in [a for a in args[1:] if not a.startswith("--")]:
            dump(p, only_miss="--miss" in args)
        sys.exit()
    for p in (args or PARTS):
        build_part(p, resolver_for(p))
        verify(p, show=300, allowed=allowed(p))
