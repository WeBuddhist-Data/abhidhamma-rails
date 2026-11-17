"""Build the Pāli->Russian keyword map for pi-2 (Vibhaṅga) chapter 18-dhammahadayavibhango (the last chapter).

usage: python -I -X utf8 map_18_ru.py                    (writes 18-dhammahadayavibhango.mapped.md and verifies)

Resolution order per keyword: OVERRIDES[bid][kw]  ->  context rules (resolve())  ->  T (this file: map_17_ru.T +
the chapter 18 additions)  ->  pi-1 CH2 / MATRIX.
Conventions: ru-map-conventions-pi2.md (+ the pi-1 file), notes-map-2-3.md … notes-map-17.md; new decisions:
notes-map-18.md. Repeated strings take the pi-1 values (hetu string ^1-1068: vipākato = результат, Kusalānaṃ vā
dhammānaṃ = благие явления; aggregates / bases / elements / faculties) and the earlier pi-2 values (ch3 elements,
ch4 truths, ch5 faculties). Presence-check exceptions: only the ones this chapter's segments need (EXC / EXC_SEG),
nothing inherited wholesale.
Helpers: draft_18.py (prior-map suggestions, --diff consistency check), uniq_18.py (distinct keyword=value list).
"""
import pathlib
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import map_17_ru as M17  # noqa: E402  (read-only: its table T, CHOICES)
from map_common_pi2_ru import (GAP, NDE, build_part, hetuko_value, lc, present,  # noqa: E402,F401
                               read_keywords, read_pali, read_russian, value, verify)

PART = "18-dhammahadayavibhango"

T = dict(M17.T)
T.update({
    # ================================================================ headings, colophon
    "hadaya": "суть", "dhamma": "явление", "saṅgāhika": "охватывающий", "sabba": "всё", "vāro": "раздел",
    "ānuppatti": "не возникать",
    "uppattānuppattivāro": "раздел о том что возникает и что не возникает",
    "apariyāpannaṃ": "не принадлежащий к кругам существования",
    "dassanavāro": "раздел", "dassana": NDE,      # «Раздел о …»: dassana has no word of its own (2-18-4-0 overridden)
    "antara": "различие", "bhūmantaradassanavāro": "раздел о различии уровней",
    "uppādaka": "порождающий", "uppādakakamma": "порождающие действия", "uppādakakammaṃ": "порождающие действия",
    "āyu": "жизнь", "pamāṇa": "продолжительность", "pamāṇaṃ": "продолжительность",
    "āyuppamāṇa": "продолжительность жизни", "āyuppamāṇaṃ": "продолжительность жизни",
    "abhiññeyyādivāro": "раздел о том что следует постичь высшим знанием и прочем", "ādi": "прочее",
    "sārammaṇānārammaṇavāro": "раздел об имеющем объект и не имеющем объекта", "ārammaṇa": "объект",
    "diṭṭhasutādidassanavāro": "раздел об увиденном услышанном и прочем",
    "tikādidassanavāro": "раздел о тройках и прочем",
    "tikaṃ": "тройка", "dukaṃ": "пара", "vipākattikaṃ": "тройка о результате действий",
    "upādinna": "охваченный цеплянием", "lokiya": "мирской",
    "pakaraṇaṃ": "книга", "vibhaṅgapakaraṇaṃ": "книга «Подробный разбор»", "abhiññā": "высшее знание",
    "upādinnā": "охваченный цеплянием", "vitakkaṃ": "направленная мысль",
    # ================================================================ realms (dhātu = мир; rūpa / arūpa = форма / без форм)
    "kāma": "чувственные желания", "kāmadhātu": "мир чувственных желаний", "kāmadhātuyā": "мир чувственных желаний",
    "rūpadhātuyā": "мир форм", "arūpadhātu": "мир без форм", "arūpadhātuyā": "мир без форм",
    "arūpa": "без форм", "dhātuyā": "мир",
    "dhātuyo kāmadhātupariyāpannā": "элементы принадлежащие к миру чувственных желаний",
    # ================================================================ counts (pi-1: āyatanāni = сферы восприятия …)
    "āyatanāni": "сферы восприятия", "āyatanānaṃ": "сферы восприятия", "indriyā": "способности",
    "phassā": "виды контакта", "phasso": "вид контакта", "cittā": "виды ума", "cittānaṃ": "виды ума",
    "cittaṃ": "вид ума", "dhātūnaṃ": "элементы", "saccānaṃ": "истины",
    "aṭṭhārasannaṃ": "восемнадцать", "aṭṭhārasannaṃ dhātūnaṃ": "восемнадцать элементов",
    "dvādasannaṃ": "двенадцать", "dvādasannaṃ āyatanānaṃ": "двенадцать сфер восприятия",
    "ekādasāyatanāni": "одиннадцать сфер восприятия", "dasāyatanāni": "десять сфер восприятия",
    "cuddasindriyāni": "четырнадцать способностей", "terasindriyāni": "тринадцать способностей",
    "dvādasindriyāni": "двенадцать способностей", "ekādasindriyāni": "одиннадцать способностей",
    "dasindriyāni": "десять способностей", "bāvīsatindriyā": "двадцать две способности", "terasa": "тринадцать",
    # ================================================================ hetu, āhāra, phassa
    "hetu": "корень", "hetū": "корни", "kusalahetu": "благой корень", "kusalahetū": "благие корни",
    "akusalahetu": "неблагой корень", "akusalahetū": "неблагие корни",
    "abyākatahetū": "этически неопределённые корни", "vipākato": "результат",
    "kiriyābyākatesu": "этически неопределённый функциональный",
    "vipāka": "результат действий", "vipākahetu": "корень являющийся результатом действий",
    "kabaḷīkārāhāro": "съедаемая пища", "phassāhāro": "питание контактом",
    "manosañcetanāhāro": "питание умственным намерением", "viññāṇāhāro": "питание сознанием",
    "samphasso": "контакт", "manodhātusamphasso": "контакт элемента ума", "manodhātusamphassa": "контакт элемента ума",
    "manodhātusamphassajā": "рождённый контактом элемента ума",
    "manoviññāṇadhātusamphassajā": "рождённый контактом элемента умственного сознания",
    "manoviññāṇadhātusamphassajā vedanā": "рождённое контактом элемента умственного сознания чувство",
    "manoviññāṇadhātusamphassajā saññā": "рождённое контактом элемента умственного сознания восприятие",
    "manoviññāṇadhātusamphassajā cetanā": "рождённое контактом элемента умственного сознания намерение",
    "magga": "путь", "maggā": "пути", "phalāni": "плоды",
    # ================================================================ rebirth (2-1007 … 2-1019)
    "pātubhavanti": "появляться", "pātubhavati": "появляться", "upapatti": "перерождение",
    "upapattikkhaṇe": "момент перерождения", "devānaṃ": "боги", "devā": "боги", "deve": "боги",
    "kappikānaṃ": "эпоха", "manussānaṃ": "люди", "opapātikānaṃ": "рождающийся самопроизвольно",
    "petānaṃ": "духи умерших", "asurānaṃ": "асуры", "tiracchānagatānaṃ": "животные",
    "opapātikānaṃ petānaṃ": "рождающиеся самопроизвольно духи умерших",
    "opapātikānaṃ asurānaṃ": "рождающиеся самопроизвольно асуры",
    "opapātikānaṃ tiracchānagatānaṃ": "рождающиеся самопроизвольно животные",
    "nerayikānaṃ": "обитатели ада", "paripuṇṇāyatanānaṃ": "обладающий полным набором сфер восприятия",
    "jaccandhānaṃ": "слепой от рождения", "badhirānaṃ": "глухой", "gabbhaseyyakānaṃ": "рождающийся из утробы",
    "kāmāvacarānaṃ": "относящийся к миру чувственных желаний", "āvacarānaṃ": "относящийся к миру",
    "sahetukānaṃ": "имеющий корни", "sampayuttānaṃ": "связанный", "vippayuttānaṃ": "не связанный",
    "ñāṇavippayuttānaṃ": "не связанный со знанием", "napuṃsakānaṃ": "бесполый", "avasesānaṃ": "остальной",
    "asañña": "без восприятия", "asaññasattānaṃ": "без восприятия",
    "asaññasattānaṃ devānaṃ": "боги без восприятия",
    "ahetukā": "без корней", "anāhārā": "без питания", "aphassakā": "без контакта", "avedanakā": "без чувства",
    "asaññakā": "без восприятия", "acetanakā": "без намерения", "acittakā": "без ума",
    # ================================================================ planes (2-1020)
    "khandha": "совокупность", "pariyantaṃ": "граница", "antare": "предел",
    "deve antokaritvā": "включить в эти пределы богов", "akaniṭṭhe deve": "высочайшие боги",
    "paranimmitavasavattī": "властвующий над творениями других",
    "paranimmitavasavattī deve": "боги властвующие над творениями других",
    "āyatanūpage": "достигший сферы", "ākāsānañcāyatanūpage": "достигший сферы бесконечного пространства",
    "nevasaññānāsaññāyatanūpage": "достигший сферы ни восприятия ни невосприятия",
    "sukhavihārissa": "пребывать в счастье",
    "kusalākusalabyākatā": "благие неблагие и этически неопределённые",
    "kāmāvacarā dhammā": "явления относящиеся к миру чувственных желаний",
    "asaṅkhatā ca dhātu": "необусловленный элемент",
    # ================================================================ gods (2-1021 … 2-1028)
    "arahanto": "архаты", "brāhmaṇa": "брахманы", "gahapati": "домохозяева", "khattiya": "знатные правители",
    "mahāsālānaṃ": "богатый", "sammuti": "общее признание", "rājāno": "цари", "deviyo": "царицы",
    "kumārā": "царевичи", "mahārājike": "Великие Цари", "mahārājikānaṃ": "Великие Цари", "tadupari": "выше",
    "dānaṃ": "подаяние", "sīlaṃ": "нравственность", "samādiyitvā": "взять на себя", "uposatha": "постный день",
    "katvā": "соблюдать", "upapajjanti": "перерождаться",
    "tāvatiṃsānaṃ": "Тридцать три", "yāmānaṃ devānaṃ": "боги Ямы", "tusitānaṃ": "Тушита",
    "tusitānaṃ devānaṃ": "боги Тушиты", "nimmāna": "творение", "ratīnaṃ": "наслаждающийся",
    "nimmānaratīnaṃ devānaṃ": "боги наслаждающиеся творением",
    "paranimmitavasavattīnaṃ": "властвующий над творениями других",
    "paranimmitavasavattīnaṃ devānaṃ": "боги властвующие над творениями других", "vasavattīnaṃ": "властвующий",
    "sataṃ": "сто",
    # lifespans (2-1023)
    "mānusakāni": "человеческий", "mānusakaṃ vassasataṃ": "сто человеческих лет", "paññāsa": "пятьдесят",
    "vassāni": "год", "vassasatāni": "год", "satāni": NDE, "sahassaṃ": "тысяча", "sahassāni": "тысяча",
    "dibbāni": "божественный", "rattindivo": "сутки", "rattiyo": "ночи",
    "rattiyo māso": "ночи составляют месяц", "māso": "месяц", "saṃvaccharo": "год",
    "dvādasamāsiyo saṃvaccharo": "двенадцать" + GAP + "месяцы составляют год",
    "tiṃsa": "тридцать", "dvādasa": "двенадцать", "soḷasa": "шестнадцать",
    "manussānaṃ gaṇanāya": "человеческий счёт", "gaṇanāya": "счёт",
    "samiddhino": "изобиловать", "saṅkhāto": "сложить вместе", "koṭiyo": "миллионы",
    "aṭṭhavīsañca": "двести восемьдесят", "pakāsitāti": "возвещённый",
    # brahmā worlds (2-1024 … 2-1028)
    "jhānaṃ": "медитативное погружение", "bhāvetvā": "развить", "parittaṃ": "ограниченный",
    "majjhimaṃ": "средний", "paṇītaṃ": "высший", "kappassa": "эпоха", "kappā": "эпохи",
    "pārisajjānaṃ": "свита", "purohitānaṃ": "советники", "brahmānaṃ devānaṃ": "Брахмы",
    "mahābrahmānaṃ": "Великие Брахмы", "mahābrahmānaṃ devānaṃ": "Великие Брахмы",
    "ābhānaṃ": "сияние", "appamāṇābhānaṃ": "безмерное сияние", "ābhassarānaṃ": "струящееся сияние",
    "subhānaṃ": "великолепие", "kiṇhānaṃ": "сплошной", "appamāṇa": "безмерный",
    "catusaṭṭhi": "шестьдесят четыре", "bāttiṃsa": "тридцать два",
    "nānattatā": "различие", "abhinīhāra": "направленность", "akaniṭṭhānaṃ devānaṃ": "высочайшие боги",
    "vehapphalānaṃ": "великий плод", "vehapphalānaṃ devānaṃ": "боги великого плода",
    "avihānaṃ": "не отпадающий от своего мира", "avihānaṃ devānaṃ": "боги не отпадающие от своего мира",
    "atappānaṃ": "невозмутимый", "atappānaṃ devānaṃ": "невозмутимые боги",
    "sudassānaṃ": "прекрасный облик", "sudassānaṃ devānaṃ": "боги прекрасного облика",
    "sudassīnaṃ devānaṃ": "боги ясного видения",
    "āyatanūpagānaṃ": "достигший сферы", "ākāsānañcāyatanūpagānaṃ": "достигший сферы бесконечного пространства",
    "viññāṇañcāyatanūpagānaṃ": "достигший сферы бесконечного сознания",
    "ākiñcaññāyatanūpagānaṃ": "достигший сферы отсутствия чего-либо",
    "nevasaññānāsaññāyatanūpagānaṃ": "достигший сферы ни восприятия ни невосприятия",
    "kappasahassāni": "тысяча эпох", "kappasahassaṃ": "тысяча эпох",
    "vīsati": "двадцать", "cattārīsa": "сорок", "saṭṭhi": "шестьдесят", "caturāsīti": "восемьдесят четыре",
    # verse (2-1029)
    "ukkhittā": "вознесённый", "puñña": "заслуги", "tejena": "сила", "gatiṃ": "удел", "gatā": "ушедший",
    "bhavaggatampi": "вершина существования", "punāgacchanti": "вновь приходить", "duggatiṃ": "дурной удел",
    "dīghāyukā": "долгоживущий", "sattā": "существа", "cavanti": "умирать",
    "āyusaṅkhayā": "исчерпанный срок жизни", "saṅkhayā": "исчерпанный",
    "koci": "никакой", "bhavo": "существование", "nicco": "постоянный", "mahesinā": "великий мудрец",
    "tasmā": "поэтому", "dhīrā": "мудрый", "nipakā": "благоразумный", "nipuṇā": "проницательный",
    "cintakā": "размышляющий", "jarā": "старение", "maraṇa": "смерть", "jarāmaraṇa": "старение и смерть",
    "mokkhāya": "освобождение", "bhāventi": "развивать", "maggaṃ": "путь", "uttamaṃ": "высший",
    "bhāvayitvā": "развить", "suciṃ": "чистый", "nibbānogadhagāminaṃ": "ведущий к погружению в нирвану",
    "āsave": "влечения", "pariññāya": "полностью понять", "parinibbanti": "достигать окончательного угасания",
    "anāsavāti": "свободный от влечений",
    # ================================================================ abhiññeyya … (2-1030, 2-1031)
    "abhiññeyyā": "следует постичь высшим знанием", "abhiññeyyo": "следует постичь высшим знанием",
    "pariññeyyā": "следует полностью понять", "pariññeyyo": "следует полностью понять",
    "pahātabbā": "следует устранить", "pahātabbo": "следует устранить",
    "bhāvetabbā": "следует развивать", "bhāvetabbo": "следует развивать",
    "sacchikātabbā": "следует осуществить", "sacchikātabbo": "следует осуществить",
    # ================================================================ objects, seen / heard (2-1032 … 2-1037)
    "ārammaṇā": "имеющий объектом", "ārammaṇo": "имеющий объектом",   # -ārammaṇā «имеют объектом» (pi-1)
    "sārammaṇārammaṇā": "имеющий объектом то что имеет объект",
    "anārammaṇārammaṇā": "имеющий объектом то что не имеет объекта",
    "sutā": "услышанный", "suto": "услышанный", "mutā": "ощущённый", "muto": "ощущённый",
    "viññātā": "познанный", "viññāto": "познанный",
    # ================================================================ triads (2-1038 … 2-1044)
    "nevavipākanavipākadhammadhammo": "не являющийся результатом действий и не способный приносить результаты",
    "rūpā": "материальный",
})

_REALM_HEAD = {"dhātu": "мир", "Rūpa": "форма", "Kāmadhātu": "мир чувственных желаний",
               "Rūpadhātu": "мир форм", "Arūpadhātu": "мир без форм"}
OVERRIDES = {
    "2-18-4-0": {"dassanavāro": "раздел о проявлении", "dassana": "проявление"},   # «Раздел о проявлении явлений»
    "2-18-1-0": {"Sabba": "всё"},
    "2-18-10-6-0": {"Rūpa": "материальный"},     # «Пара о материальном»
    # rūpa: realm «мир форм» = форма; Rūpakkhandho = материальная форма; rūpadhātu (element) = видимая форма
    "2-993": {"Rūpa": "форма"}, "2-994": {"Rūpa": "материальная форма", "rūpa": "форма"},
    "2-1001": {"rūpa": "форма", "rūpadhātu": "мир форм"},
    "2-1002": {"Rūpa": "материальная форма", "rūpa": "форма", "rūpadhātu": "мир форм"},
    "2-1015": {"Rūpa": "форма"}, "2-1016": {"Rūpa": "форма"},
    "2-1017": {"rūpa": "материальная форма"},
    "2-1029": {"rūpa": "мир форм"},              # kāmarūpagatiṃ «уделы мира чувственных желаний и мира форм» (ch17)
    "2-1023": {"kāma": "чувственные блага", "sabba": "весь", "āyu": "срок жизни"},   # verse: «срок жизни их всех»
    "2-1044": {"sārammaṇā": "раздел об объекте"},  # summary verse «два раздела об объекте»
    "2-1020": {"dhātu": "элемент"},
    "2-981": {"dhamma": "объекты ума"}, "2-1010": {"dhamma": "объекты ума"},   # with dhammadhātu (pi-1 rule)
    "2-1021": {"upapatti": "рождение"},          # upapattidevā «боги по рождению»
}
for _b in ("2-1024", "2-1025", "2-1026"):           # «Какова продолжительность их жизни?»
    OVERRIDES.setdefault(_b, {})["āyuppamāṇaṃ"] = "продолжительность" + GAP + "жизни"
for _b in ("2-18-2-1-0", "2-18-2-2-0", "2-18-2-3-0", "2-18-3-1-0", "2-18-3-2-0", "2-18-3-3-0", "2-18-4-1-0",
           "2-18-4-2-0", "2-18-4-4-0"):
    OVERRIDES.setdefault(_b, {}).update(_REALM_HEAD)
for _b in ("2-999", "2-1000", "2-1001", "2-1002", "2-1003", "2-1004"):   # «принадлежат к миру …»
    OVERRIDES.setdefault(_b, {})["dhātu"] = "мир"
for _b in ("2-1000", "2-1002", "2-1004", "2-1006", "2-1008") + tuple(f"2-{n}" for n in range(1031, 1045)):
    OVERRIDES.setdefault(_b, {}).setdefault("Rūpa", "материальная форма")    # Rūpakkhandho
for _b in ("2-979", "2-992"):
    OVERRIDES.setdefault(_b, {})["Rūpa"] = "материальная форма"
# «upapattikkhaṇe N X» = «в момент перерождения появляются N X»
for _k, _v in {"ekādasāyatanāni": "одиннадцать сфер восприятия", "dasāyatanāni": "десять сфер восприятия",
               "ekādasa": "одиннадцать", "ekādasa dhātuyo": "одиннадцать элементов", "dasa": "десять",
               "dasa dhātuyo": "десять элементов", "dasindriyāni": "десять способностей",
               "terasindriyāni": "тринадцать способностей"}.items():
    T[f"upapattikkhaṇe {_k}"] = "момент перерождения" + GAP + _v
CHOICES = dict(M17.CHOICES)
EXC = {   # only what this chapter's segments need
    "samāpannassa": "войти ~ вошёл (suppletive past stem), = pi-1 / pi-2 KH value",
    "punāgacchanti": "вновь приходить ~ вновь приходят (2nd conjugation -ить / -ят)",
}
EXC_SEG = {("2-1023", "sabba"): "весь ~ всеми / всех (suppletive pronoun), as tadekajjhaṃ"}


def resolver():
    ru, pi = read_russian(PART), read_pali(PART)

    def resolve(bid, kw, kws):
        k = lc(kw)
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        if k in ov:
            return ov[k]
        if k == "āhāro":   # «съедаемая пища» where kabaḷīkāra is in the segment, else «питание контактом …»
            return "пища" if any(lc(x).startswith("kabaḷīkār") for x in kws) else "питание"
        if kw == "hetuko":
            return hetuko_value(pi.get(bid, ""))
        if k in CHOICES:
            text = ru.get(bid, "")
            for cand in CHOICES[k]:
                if present(cand, text):
                    return cand
            return CHOICES[k][0]
        return value(kw, kws, T)
    return resolve


def allowed():
    out = {(bid, kw): EXC[lc(kw)] for bid, kws in read_keywords(PART) for kw in kws if lc(kw) in EXC}
    out.update({(bid, kw): EXC_SEG[(bid, kw)] for bid, kws in read_keywords(PART) for kw in kws
                if (bid, kw) in EXC_SEG})
    return out


if __name__ == "__main__":
    build_part(PART, resolver())
    verify(PART, show=300, allowed=allowed())
