"""Builder for the Russian rails translation of pi-2 (Vibhaṅga, plain audience), chapter 18
(Dhammahadayavibhaṅgo ^2-18-0 … ^2-1044, the last chapter).

Writes (only when run as a script):
  AI_translation/russian/pi-2-russian-plain-rails_split_chapters/18-dhammahadayavibhango.md
  0-INBOX/temp/pipeline/pi-2-ru/rails/notes-18.md   (new recurring formulas, Pāli = Russian)

Every Russian string comes from the fixed tables and functions below, so identical Pāli gives identical Russian.
Imported read-only: the approved sample builder (S) and the builders of chapters 1-5 (K1 matrix items and question
phrases, K23 names of bases and elements and the question-section engine, K45 truths, faculties and engine tables).
Nothing of theirs is changed (K45.install() only extends the K23 tables in memory, as chapters 6-17 do).

Reused: pi-1 ^1-1068 (the indeterminate roots), ^1-1288 … ^1-1294 (the sphere dyads), ch. 3 ^2-182 (the frame
«Если взять снизу границей …»), ch. 1-5 names and question-section predicates, ch. 17 «– таковы N X» (ime N X).

usage: python -I -X utf8 build_rails_18_ru.py
"""
import pathlib
import re
import sys

RAILS = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-ru\rails")
sys.path.insert(0, str(RAILS))
import build_rails_sample_ru as S   # noqa: E402  (importing writes nothing)
import build_rails_1_ru as K1       # noqa: E402
import build_rails_2_3_ru as K23    # noqa: E402
import build_rails_4_5_ru as K45    # noqa: E402

PART = "18-dhammahadayavibhango.md"
NOTES_PATH = RAILS / "notes-18.md"
cap, low, nlist = S.cap, K1.low, K23.nlist
SLIPS = []


def slip(msg):
    if msg not in SLIPS:
        SLIPS.append(msg)


# =========================================================================== headings
TITLE = S.CH_TITLE[18][1]                                   # Разбор сути явлений
HEAD = {
    "Dhammahadayavibhaṅgo": TITLE,
    "Sabbasaṅgāhikavāro": "Раздел, охватывающий всё",                       # Sabba «весь», saṅgāhika «охватывающий»
    "Uppattānuppattivāro": "Раздел о том, что возникает и что не возникает",  # termbase
    "Kāmadhātu": "Мир чувственных желаний",
    "Rūpadhātu": "Мир форм",
    "Arūpadhātu": "Мир без форм",
    "Apariyāpannaṃ": "Не принадлежащее к кругам существования",
    "Pariyāpannāpariyāpannavāro": "Раздел о принадлежащем и не принадлежащем",
    "Pariyāpannāpariyāpannaṃ": "Принадлежащее и не принадлежащее к кругам существования",
    "Dhammadassanavāro": "Раздел о проявлении явлений",                      # dassana «проявление», Dhamma «явление»
    "Asaññasattā": "Существа без восприятия",
    "Bhūmantaradassanavāro": "Раздел о различии уровней",                     # termbase
    "Uppādakakammaāyuppamāṇavāro": "Раздел о порождающих действиях и продолжительности жизни",
    "Uppādakakammaṃ": "Порождающие действия",
    "Āyuppamāṇaṃ": "Продолжительность жизни",
    "Abhiññeyyādivāro": "Раздел о том, что следует постичь высшим знанием, и прочем",
    "Sārammaṇānārammaṇavāro": "Раздел об имеющем объект и не имеющем объекта",
    "Diṭṭhasutādidassanavāro": "Раздел об увиденном, услышанном и прочем",
    "Tikādidassanavāro": "Раздел о тройках и прочем",
    "Kusalattikaṃ": "Тройка о благом",
    "Vedanātikaṃ": "Тройка о чувстве",
    "Vipākattikaṃ": "Тройка о результате действий",                         # termbase
    "Upādinnattikaṃ": "Тройка об охваченном цеплянием",
    "Vitakkattikaṃ": "Тройка о направленной мысли",
    "(1) Rūpadukaṃ": "(1) Пара о материальной форме",
    "(2) Lokiyadukaṃ": "(2) Пара о мирском",
}

# =========================================================================== names (earlier chapters)
KH = S.KH
KH_P = {"rūpakkhandho": "rupa", "vedanākkhandho": "vedana", "saññākkhandho": "sanna",
        "saṅkhārakkhandho": "sankhara", "viññāṇakkhandho": "vinnana"}
AY = K23.AY
AYK = {"cakkh": "cakkhu", "rūp": "rūpa", "sot": "sota", "sadd": "sadda", "ghān": "ghāna", "gandh": "gandha",
       "jivh": "jivhā", "ras": "rasa", "kāy": "kāya", "phoṭṭhabb": "phoṭṭhabba", "man": "mana", "dhamm": "dhamma"}
DH = K23.DH
IND, IND_P = K45.IND, K45.IND_P
TRUTH = {k: low(v) for k, v in (("dukkha", "Истина о страдании"), ("samudaya", "Истина о возникновении"),
                                ("nirodha", "Истина о прекращении"), ("magga", "Истина о пути"))}
assert set(TRUTH.values()) == {low(v) for v in K45.SUB_H.values()}
PH = {"cakkhu": "контакт глаза", "sota": "контакт уха", "ghāna": "контакт носа", "jivhā": "контакт языка",
      "kāya": "контакт тела", "manodhātu": "контакт элемента ума",
      "manoviññāṇadhātu": "контакт элемента умственного сознания",
      "kāyaviññāṇadhātu": "контакт элемента осязательного сознания"}       # termbase X-samphasso «контакт X»
AHARA = {"kabaḷīkārāhāro": "съедаемая пища", "kabaḷīkāro āhāro": "съедаемая пища",       # S / pi-1
         "phassāhāro": "питание контактом", "manosañcetanāhāro": "питание умственным намерением",
         "viññāṇāhāro": "питание сознанием"}                                                # termbase
FOOD_VAR2 = "[вариант написания (Sī., Syā.): kabaḷiṃkāro āhāro]"
ROOT = {"alobho": "отсутствие жадности", "adoso": "отсутствие злобы", "amoho": "отсутствие заблуждения",
        "lobho": "жадность", "doso": "злоба", "moho": "заблуждение"}
HETU_KIND = {"kusala": "благой корень", "akusala": "неблагой корень",
             "vipāka": "корень, являющийся результатом действий"}                  # termbase vipākahetu
HETU_GROUP = {"tayo kusalahetū": "три благих корня", "tayo akusalahetū": "три неблагих корня",
              "dve akusalahetū": "два неблагих корня", "tayo abyākatahetū": "три этически неопределённых корня"}
VIPAKATO = "в виде результатов благих явлений"                     # Kusalānaṃ dhammānaṃ vipākato (pi-1 ^1-1068)
KIRIYA = "или в этически неопределённых функциональных явлениях"   # kiriyābyākatesu vā dhammesu (pi-1 ^1-1068)
ROOTS3 = "Отсутствие жадности, отсутствие злобы, отсутствие заблуждения"  # alobho, adoso, amoho (pi-1 ^1-1068)

# ---- counted nouns of the Dhammahadaya chapter
# key: (gender, nom sg, gen sg (2-4), gen pl (5+), ins sg, ins pl)
NOUN = {
    "khandha": ("f", "совокупность", "совокупности", "совокупностей", "совокупностью", "совокупностями"),
    "āyatana": ("f", "сфера восприятия", "сферы восприятия", "сфер восприятия", "сферой восприятия",
                "сферами восприятия"),
    "dhātu": ("m", "элемент", "элемента", "элементов", "элементом", "элементами"),
    "sacca": ("f", "истина", "истины", "истин", "истиной", "истинами"),
    "indriya": ("f", "способность", "способности", "способностей", "способностью", "способностями"),
    "hetu": ("m", "корень", "корня", "корней", "корнем", "корнями"),
    "āhāra": ("m", "вид питания", "вида питания", "видов питания", "видом питания", "видами питания"),
    "phassa": ("m", "вид контакта", "вида контакта", "видов контакта", "видом контакта", "видами контакта"),
    "vedanā": ("n", "чувство", "чувства", "чувств", "чувством", "чувствами"),
    "saññā": ("n", "восприятие", "восприятия", "восприятий", "восприятием", "восприятиями"),
    "cetanā": ("n", "намерение", "намерения", "намерений", "намерением", "намерениями"),
    "citta": ("m", "вид ума", "вида ума", "видов ума", "видом ума", "видами ума"),
}
NOUN_STEM = [("kkhandh", "khandha"), ("khandh", "khandha"), ("āyatan", "āyatana"), ("dhātu", "dhātu"),
             ("sacc", "sacca"), ("indriy", "indriya"), ("hetu", "hetu"), ("hetū", "hetu"), ("āhār", "āhāra"),
             ("phass", "phassa"), ("vedanā", "vedanā"), ("saññā", "saññā"), ("cetanā", "cetanā"),
             ("citt", "citta")]
# Russian numerals: nom (m, f, n), ins (m/n, f)
NUMR = {1: (("один", "одна", "одно"), ("одним", "одной")), 2: (("два", "две", "два"), ("двумя", "двумя")),
        3: (("три",) * 3, ("тремя",) * 2), 4: (("четыре",) * 3, ("четырьмя",) * 2),
        5: (("пять",) * 3, ("пятью",) * 2), 6: (("шесть",) * 3, ("шестью",) * 2), 7: (("семь",) * 3, ("семью",) * 2),
        8: (("восемь",) * 3, ("восемью",) * 2), 9: (("девять",) * 3, ("девятью",) * 2),
        10: (("десять",) * 3, ("десятью",) * 2), 11: (("одиннадцать",) * 3, ("одиннадцатью",) * 2),
        12: (("двенадцать",) * 3, ("двенадцатью",) * 2), 13: (("тринадцать",) * 3, ("тринадцатью",) * 2),
        14: (("четырнадцать",) * 3, ("четырнадцатью",) * 2), 18: (("восемнадцать",) * 3, ("восемнадцатью",) * 2),
        22: (("двадцать два", "двадцать две", "двадцать два"), ("двадцатью двумя",) * 2)}
NUMP = {"eko": 1, "ekā": 1, "ekaṃ": 1, "dve": 2, "tayo": 3, "tīṇi": 3, "cattāro": 4, "catasso": 4, "cattāri": 4,
        "pañca": 5, "cha": 6, "satta": 7, "aṭṭha": 8, "nava": 9, "dasa": 10, "ekādasa": 11, "dvādasa": 12,
        "aṭṭhārasa": 18}
NSTEM = {"pañca": 5, "pañc": 5, "dvādas": 12, "ekādas": 11, "das": 10, "nav": 9, "satt": 7, "cuddas": 14,
         "teras": 13, "aṭṭh": 8, "cattār": 4, "bāvīsat": 22, "ek": 1}


def parse_count(p):
    """Pāli count phrase -> (number, noun key)"""
    p = p.strip()
    p = p[0].lower() + p[1:]
    m = re.match(r"^(\w+?)(kkhandhā|āyatanāni|indriyāni|indriyaṃ)$", p)
    if m:
        noun = {"kkhandhā": "khandha", "āyatanāni": "āyatana"}.get(m.group(2), "indriya")
        return NSTEM[m.group(1)], noun
    num, word = p.split(" ")
    for st, k in NOUN_STEM:
        if word.startswith(st):
            return NUMP[num], k
    raise KeyError(p)


def count_ru(p, case="nom"):
    n, k = parse_count(p)
    g, nom1, gen1, genp, ins1, insp = NOUN[k]
    gi = {"m": 0, "f": 1, "n": 2}[g]
    if case == "nom":
        num = NUMR[n][0][gi]
        noun = nom1 if n == 1 else gen1 if n in (2, 3, 4, 22) else genp
    else:
        num = NUMR[n][1][1 if g == "f" else 0]
        noun = ins1 if n == 1 else insp
    return f"{num} {noun}"


def count_gender(p):
    n, k = parse_count(p)
    return "p" if n > 1 else NOUN[k][0]


KATI = {"khandhā": "совокупностей", "āyatanāni": "сфер восприятия", "āyatanā": "сфер восприятия",
        "dhātuyo": "элементов", "saccāni": "истин", "indriyāni": "способностей", "hetū": "корней",
        "āhārā": "видов питания", "phassā": "видов контакта", "vedanā": "чувств", "saññā": "восприятий",
        "cetanā": "намерений", "cittāni": "видов ума"}                    # kati X = сколько X(gen pl)
LOC = {"kāmadhātuyā": "в мире чувственных желаний", "rūpadhātuyā": "в мире форм", "arūpadhātuyā": "в мире без форм",
       "apariyāpanne": "в том, что не принадлежит к кругам существования"}   # pi-1 ^1-1285 «в том, что не …»


# =========================================================================== list items
def item_ru(t):
    t0 = t[0].lower() + t[1:]
    m = re.match(r"^(\w+indriyaṃ) vā (\w+indriyaṃ) vā$", t0)
    if m:
        return f"{IND[IND_P[m.group(1)]]} или {IND[IND_P[m.group(2)]]}"
    if t0 in IND_P:
        return IND[IND_P[t0]]
    if t0 in AHARA:
        return AHARA[t0]
    if t0 in KH_P:
        return KH[KH_P[t0]]
    m = re.match(r"^(\w+?)āyatanaṃ$", t0)
    if m and m.group(1) in AYK:
        return AY[AYK[m.group(1)]]
    m = re.match(r"^(\w+)dhātu$", t0)
    if m and m.group(1) in DH:
        return DH[m.group(1)]
    m = re.match(r"^(\w+)samphasso$", t0)
    if m:
        return PH[m.group(1)]
    m = re.match(r"^(\w+)samphassajā (vedanā|saññā|cetanā)$", t0)
    if m:
        return f"рождённое контактом {K1.SENSE_GEN[m.group(1)]} {K1.JA_NOUN[m.group(2)]}"
    m = re.match(r"^(\w+)viññāṇaṃ$", t0)
    if m:
        return K1.VINN[m.group(1)]
    m = re.match(r"^(\w+)saccaṃ$", t0)
    if m:
        return TRUTH[m.group(1)]
    m = re.match(r"^(alobho|adoso|amoho|lobho|doso|moho) (kusala|akusala|vipāka)hetu$", t0)
    if m:
        return f"{ROOT[m.group(1)]} как {HETU_KIND[m.group(2)]}"
    raise KeyError(t)


def items(text):
    """Pāli list «A, B, C» -> Russian items (two items run together without a comma are split and reported)"""
    out = []
    for t in text.split(", "):
        try:
            out.append(item_ru(t))
        except KeyError:
            a, b = t.split(" ")
            out += [item_ru(a), item_ru(b)]
            slip(f"«{t}»: comma missing between the two list items (rendered as two items)")
    return out


def rlist(text):
    """a Pāli list (possibly with …pe…) as a Russian list: «a, b и c»; «a, b… z» for a …pe… run;
    «a; b; c» when an item has its own comma"""
    if "…" in text:
        return "… ".join(", ".join(items(ch)) for ch in re.split(r"\s*…(?:pe…)?\s*", text))
    its = items(text)
    if any("," in i for i in its):
        return "; ".join(its)
    return nlist(its) if len(its) > 1 else its[0]


def needs_comma(ru):
    """a comma before the dash where a participial / relative clause closes (formulas file rule)"""
    return bool(re.search(r"(результатом действий|ни болезненно, ни приятно)$", ru))


# =========================================================================== sections 1-2: the counts
COUNT_Q = re.compile(r"^(?:(\w+) )?kati (.+)\?$", re.I)
CHAIN = re.compile(r"…pe…\s*|… ?|, ")


def counts_question(ln):
    m = COUNT_Q.match(ln)
    loc = m.group(1)
    body = "kati " + m.group(2)
    parts = re.split(r"(…pe…\s*|, )", body)
    out = ""
    for i, x in enumerate(parts):
        if i % 2 == 1:
            out += "… " if x.startswith("…") else ", "
            continue
        w = x.strip()
        assert w.startswith("kati "), ln
        out += f"сколько {KATI[w[5:]]}"
    if loc:
        return f"{loc_head(low(loc))} {out}?"
    return cap(out) + "?"


def counts_answer(ln):
    body = ln[:-1]
    loc = None
    first = body.split(" ", 1)[0]
    if low(first) in LOC:
        loc, body = low(first), body.split(" ", 1)[1]
    its = [count_ru(x) for x in body.split(", ")]
    text = nlist(its)
    return f"{loc_head(loc)} {text}." if loc else cap(text) + "."


DEF_RX = re.compile(r'^Tattha katam\w+ (?:(kāmadhātuyā|rūpadhātuyā|arūpadhātuyā|apariyāpanne) )?(.+?)\? (.+?) – '
                    r'(?:ime|imāni|imā|ayaṃ|idaṃ) (vucca\w+) "(?:(?:kāmadhātuyā|rūpadhātuyā|arūpadhātuyā|apariyāpanne) )?'
                    r'(.+?)"\.$')
HQ_RX = re.compile(r'^Tattha katame (?:(kāmadhātuyā|rūpadhātuyā|arūpadhātuyā|apariyāpanne) )?((?:nava|aṭṭha|cha) hetū)\? '
                   r'(Tayo kusalahetū(?:, (?:tayo|dve) akusalahetū)?, tayo abyākatahetū)'
                   r'(…pe… ime vuccanti "(?:\w+ )?(?:nava|aṭṭha|cha) hetū"\.|\.)$')
HSUB_RX = re.compile(r"^Tattha katame ((?:tayo|dve) (?:kusala|akusala)hetū)\? (.+) – ime \1\.$")
HABY_RX = re.compile(r'^Tattha katame tayo abyākatahetū\? Kusalānaṃ (vā )?dhammānaṃ vipākato (kiriyābyākatesu vā '
                     r'dhammesu )?alobho, adoso, amoho – ime tayo abyākatahetū\. Ime vuccanti ("?)(?:(\w+) )?'
                     r'((?:nava|aṭṭha|cha) hetū)\3\.$')
THESE = "таковы"                                            # – ime N X. (ch. 17 «– таковы N X»)


def loc_head(loc):
    """LOC opening a sentence; the relative clause of «в том, что …» closes with a comma"""
    r = cap(LOC[loc])
    return r + "," if "," in r else r


def loc_after(loc):
    return f" {LOC[loc]}" if loc else ""


def counts_line(ln):
    if ln.endswith("?") and " kati " in f" {low(ln)}":
        return counts_question(ln)
    if not ln.startswith("Tattha"):
        return counts_answer(ln)
    m = HQ_RX.match(ln)
    if m:
        loc, cnt, groups, tail = m.groups()
        g = nlist([HETU_GROUP[low(x)] for x in groups.split(", ")])
        r = f"Что такое {S.TATTHA} {count_ru(cnt)}{loc_after(loc)}? {cap(g)}"
        if tail == ".":
            return r + "."
        return f"{r}… это называется «{count_ru(cnt, 'ins')}{loc_after(loc)}»."
    m = HSUB_RX.match(ln)
    if m:
        grp, body = m.groups()
        return (f"Что такое {S.TATTHA} {HETU_GROUP[grp]}? {cap(rlist(body))} – {THESE} {HETU_GROUP[grp]}.")
    m = HABY_RX.match(ln)
    if m:
        va, kiriya, qt, loc, cnt = m.groups()
        assert (va is None) == (kiriya is None), ln
        body = f"{ROOTS3} {VIPAKATO}" + (f" {KIRIYA}" if kiriya else "")
        called = f"{count_ru(cnt, 'ins')}{loc_after(loc)}"
        if qt:
            called = f"«{called}»"
        return (f"Что такое {S.TATTHA} {HETU_GROUP['tayo abyākatahetū']}? {body} – {THESE} "
                f"{HETU_GROUP['tayo abyākatahetū']}. Это называется {called}.")
    var = ""
    if " [kabaḷiṃkāro āhāro (sī. syā.)]" in ln:
        ln = ln.replace(" [kabaḷiṃkāro āhāro (sī. syā.)]", "")
        var = FOOD_VAR2
    m = DEF_RX.match(ln)
    assert m, ln
    loc, chain, body, verb, called = m.groups()
    if verb == "vuccatti":
        slip("^2-992 «imā vuccatti» (for vuccanti): rendered as meant («это называется»)")
    cs = re.split(r"\s*…pe…\s*", chain)
    q = f"{count_ru(cs[0])}{loc_after(loc)}" + "".join(f"… {count_ru(c)}" for c in cs[1:])
    lst = cap(rlist(body))
    if var:
        lst = lst.replace(cap(AHARA["kabaḷīkārāhāro"]), f"{cap(AHARA['kabaḷīkārāhāro'])} {var}", 1)
    assert count_ru(called) == count_ru(cs[-1]), ln
    comma = "," if needs_comma(lst) else ""
    return f"Что такое {S.TATTHA} {q}? {lst}{comma} – это называется «{count_ru(called, 'ins')}{loc_after(loc)}»."


# =========================================================================== section 4: what appears at rebirth
APPEAR = {"pātubhavanti": "появляются", "pātubhavati": "появляется"}
LOC4 = {"Kāmadhātuyā": "в мире чувственных желаний", "Rūpadhātuyā": "в мире форм", "Arūpadhātuyā": "в мире без форм",
        "Asaññasattānaṃ devānaṃ": "у богов без восприятия"}
MOMENT = "в момент перерождения"                            # upapattikkhaṇe (termbase)
ALL = "у всех"                                              # sabbesaṃ
SOME = "у некоторых"                                        # kassaci
OTHER = "другие"                                            # aparāni / aparā (with a count)
EXCEPT_ASANNA = "кроме богов без восприятия"                # ṭhapetvā asaññasattānaṃ devānaṃ
ROOTLESS = "появление происходит без корней"                # ahetukā pātubhavanti (after «у …»)
BEINGS = {  # Pāli (commas removed) -> «У …,» (genitive, with the closing comma of a participial clause)
    "Kāmāvacarānaṃ devānaṃ paṭhamakappikānaṃ manussānaṃ opapātikānaṃ petānaṃ opapātikānaṃ asurānaṃ opapātikānaṃ "
    "tiracchānagatānaṃ nerayikānaṃ paripuṇṇāyatanānaṃ":
        "У богов, относящихся к миру чувственных желаний, у людей первой эпохи, у рождающихся самопроизвольно духов "
        "умерших, у рождающихся самопроизвольно асуров, у рождающихся самопроизвольно животных и у обитателей ада, "
        "обладающих полным набором сфер восприятия,",
    "Opapātikānaṃ petānaṃ opapātikānaṃ asurānaṃ opapātikānaṃ tiracchānagatānaṃ nerayikānaṃ paripuṇṇāyatanānaṃ":
        "У рождающихся самопроизвольно духов умерших, у рождающихся самопроизвольно асуров, у рождающихся "
        "самопроизвольно животных и у обитателей ада, обладающих полным набором сфер восприятия,",
    "Opapātikānaṃ petānaṃ opapātikānaṃ asurānaṃ opapātikānaṃ tiracchānagatānaṃ nerayikānaṃ jaccandhānaṃ":
        "У рождающихся самопроизвольно духов умерших, у рождающихся самопроизвольно асуров, у рождающихся "
        "самопроизвольно животных и у обитателей ада, слепых от рождения,",
    "Opapātikānaṃ petānaṃ opapātikānaṃ asurānaṃ opapātikānaṃ tiracchānagatānaṃ nerayikānaṃ jaccabadhirānaṃ":
        "У рождающихся самопроизвольно духов умерших, у рождающихся самопроизвольно асуров, у рождающихся "
        "самопроизвольно животных и у обитателей ада, глухих от рождения,",
    "Opapātikānaṃ petānaṃ opapātikānaṃ asurānaṃ opapātikānaṃ tiracchānagatānaṃ nerayikānaṃ jaccandhabadhirānaṃ":
        "У рождающихся самопроизвольно духов умерших, у рождающихся самопроизвольно асуров, у рождающихся "
        "самопроизвольно животных и у обитателей ада, слепых и глухих от рождения,",
    "Gabbhaseyyakānaṃ sattānaṃ": "У существ, рождающихся из утробы,",
    "Kāmāvacarānaṃ devānaṃ sahetukānaṃ ñāṇasampayuttānaṃ":
        "У богов, относящихся к миру чувственных желаний, имеющих корни и связанных со знанием,",
    "Kāmāvacarānaṃ devānaṃ sahetukānaṃ ñāṇavippayuttānaṃ":
        "У богов, относящихся к миру чувственных желаний, имеющих корни и не связанных со знанием,",
    "Paṭhamakappikānaṃ manussānaṃ sahetukānaṃ ñāṇasampayuttānaṃ":
        "У людей первой эпохи, имеющих корни и связанных со знанием,",
    "Paṭhamakappikānaṃ manussānaṃ sahetukānaṃ ñāṇavippayuttānaṃ":
        "У людей первой эпохи, имеющих корни и не связанных со знанием,",
    "Gabbhaseyyakānaṃ sattānaṃ sahetukānaṃ ñāṇasampayuttānaṃ":
        "У существ, рождающихся из утробы, имеющих корни и связанных со знанием,",
    "Gabbhaseyyakānaṃ sattānaṃ sahetukānaṃ ñāṇavippayuttānaṃ":
        "У существ, рождающихся из утробы, имеющих корни и не связанных со знанием,",
    "Gabbhaseyyakānaṃ sattānaṃ ahetukānaṃ ṭhapetvā napuṃsakānaṃ":
        "У существ, рождающихся из утробы, без корней, кроме бесполых,",
    "Gabbhaseyyakānaṃ sattānaṃ ahetukānaṃ napuṃsakānaṃ": "У существ, рождающихся из утробы, без корней и бесполых,",
    "Kāmāvacarānaṃ devānaṃ paṭhamakappikānaṃ manussānaṃ gabbhaseyyakānaṃ sattānaṃ sahetukānaṃ ñāṇasampayuttānaṃ":
        "У богов, относящихся к миру чувственных желаний, у людей первой эпохи и у существ, рождающихся из утробы, "
        "имеющих корни и связанных со знанием,",
    "Kāmāvacarānaṃ devānaṃ paṭhamakappikānaṃ manussānaṃ gabbhaseyyakānaṃ sattānaṃ sahetukānaṃ ñāṇavippayuttānaṃ":
        "У богов, относящихся к миру чувственных желаний, у людей первой эпохи и у существ, рождающихся из утробы, "
        "имеющих корни и не связанных со знанием,",
}
REMAINING = "У остальных существ [вариант чтения (?): avasesā sattā] " + ROOTLESS + "."   # Avasesānaṃ sattānaṃ …
WHICH = {"p": "Какие", "m": "Какой", "f": "Какая", "n": "Какое"}
THIS = {"p": "эти", "m": "этот", "f": "эта", "n": "это"}


def norm4(ln):
    return re.sub(r"\s*…pe…\s*|\s*…\s*", "… ", ln).replace("… …", "…")


def chain_ru(chain):
    return "… ".join(count_ru(c) for c in chain.split("… "))


def appear_question(ln):
    m = re.match(r"^(Kāmadhātuyā|Rūpadhātuyā|Arūpadhātuyā|Asaññasattānaṃ devānaṃ) upapattikkhaṇe kati (\w+) "
                 r"pātubhavanti… kati cittāni pātubhavanti\?$", ln)
    assert m, ln
    return (f"{cap(LOC4[m.group(1)])} {MOMENT} сколько {KATI[m.group(2)]} появляется… сколько {KATI['cittāni']} "
            f"появляется?")


def appear_summary(ln):
    """^2-1007 (clauses with «;»), ^2-1015 / ^2-1018 (clauses with «,»)"""
    m = re.match(r"^(Kāmadhātuyā|Rūpadhātuyā|Arūpadhātuyā) upapattikkhaṇe(, ṭhapetvā asaññasattānaṃ devānaṃ,)? (.*)\.$",
                 ln)
    loc, exc, body = m.groups()
    head = f"{cap(LOC4[loc])} {MOMENT}" + (f", {EXCEPT_ASANNA}," if exc else "")
    sep = "; " if ";" in body else ", "
    out = []
    for cl in body.split(sep):
        mm = re.match(r"^(?:(sabbesaṃ|kassaci) )?(\[keci \(syā\.\)\] )?(aparāni |aparā )?(.+?) "
                      r"(pātubhavanti|pātubhavati)$", cl)
        who, var, other, what, verb = mm.groups()
        whor = {"sabbesaṃ": ALL, "kassaci": SOME, None: ""}[who]
        if var:
            whor += " [вариант чтения (Syā.): keci]"
        if what == "ahetukā":
            r = f"{whor} {ROOTLESS}"
        else:
            r = (f"{whor} " if whor else "") + f"{APPEAR[verb]} " + (OTHER + " " if other else "") + chain_ru(what)
        out.append(r)
    return f"{head} {sep.join(out)}."


KASSA_RX = re.compile(r"^Kāmadhātuyā upapattikkhaṇe kassa (aparāni |aparā )?(.+?) pātubhavanti\? (.+?),? "
                      r"upapattikkhaṇe (.+?) pātubhavanti – (.+?)\. Kāmadhātuyā upapattikkhaṇe etesaṃ "
                      r"(?:imāni|imā|ime) (.+?) pātubhavanti\.( Avasesānaṃ sattānaṃ \[avasesā sattā \(\?\)\] ahetukā "
                      r"pātubhavanti\.)?$")


def kassa_line(ln):
    m = KASSA_RX.match(ln)
    assert m, ln
    other, c1, beings, c2, lst, c3, rem = m.groups()
    assert parse_count(c1) == parse_count(c2) == parse_count(c3), ln
    loc = LOC4["Kāmadhātuyā"]
    who = BEINGS[beings.replace(",", "")]
    r = (f"У кого {loc} {MOMENT} появляются {OTHER + ' ' if other else ''}{count_ru(c1)}? {who} {MOMENT} появляются "
         f"{count_ru(c2)} – {rlist(lst)}. У них {loc} {MOMENT} появляются эти {count_ru(c3)}.")
    if rem:
        r += " " + REMAINING
    return r


WHICH_RX = re.compile(r"^(Kāmadhātuyā|Rūpadhātuyā|Arūpadhātuyā) upapattikkhaṇe (sabbesaṃ )?katam\w+ (.+?) "
                      r"(pātubhavanti|pātubhavati)([?.]) (.+?) – (?:kāma|rūpa|arūpa)dhātuyā upapattikkhaṇe (sabbesaṃ )?"
                      r"(?:ime|imāni|imā|idaṃ|ayaṃ) (.+?) (pātubhavanti|pātubhavati)\.$")


def which_line(ln):
    m = WHICH_RX.match(ln)
    assert m, ln
    loc, allq, chain, verb, punct, lst, alla, last, verb2 = m.groups()
    if punct == ".":
        slip("^2-1014 «… katame cattāro āhārā pātubhavanti.»: a question closed with a full stop (rendered with «?»)")
    first = chain.split("… ")[0]
    allr = f" {ALL}" if allq else ""
    lr = cap(rlist(lst))
    comma = "," if needs_comma(lr) else ""
    return (f"{WHICH[count_gender(first)]} {chain_ru(chain)} {APPEAR[verb]} {LOC4[loc]} {MOMENT}{allr}? {lr}{comma} – "
            f"{LOC4[loc]} {MOMENT}{allr} {APPEAR[verb2]} {THIS[count_gender(last)]} {count_ru(last)}.")


def appear_line(ln):
    ln = norm4(ln)
    if ln.endswith("?") and " kati " in ln:
        return appear_question(ln)
    if " kassa " in ln:
        return kassa_line(ln)
    if " katam" in ln:
        return which_line(ln)
    return appear_summary(ln)


# =========================================================================== sections 3, 7, 8, 9: predicate engine
# Pāli subject -> (nominative, accusative, number, gender)
SUBJ18 = {}


def _s(p, nom, num, gen, acc=None):
    SUBJ18[p] = (nom, acc or nom, num, gen)


for _p, _k in (("Rūpakkhandho", "rupa"), ("Saṅkhārakkhandho", "sankhara")):
    _s(_p, cap(KH[_k]), "s", "f")
for _p, _r in (("Cattāro khandhā", "Четыре совокупности"), ("Tayo khandhā", "Три совокупности"),
               ("Dve khandhā", "Две совокупности"), ("Dasāyatanā", "Десять сфер восприятия"),
               ("Dve āyatanā", "Две сферы восприятия"), ("Dvāyatanā", "Две сферы восприятия"),
               ("Sattāyatanā", "Семь сфер восприятия"), ("Pañcāyatanā", "Пять сфер восприятия"),
               ("Cattāro āyatanā", "Четыре сферы восприятия"),
               ("Soḷasa dhātuyo", "Шестнадцать элементов"), ("Dve dhātuyo", "Два элемента"),
               ("Dasa dhātuyo", "Десять элементов"), ("Satta dhātuyo", "Семь элементов"),
               ("Cha dhātuyo", "Шесть элементов"), ("Terasa dhātuyo", "Тринадцать элементов"),
               ("Pañca dhātuyo", "Пять элементов"), ("Pannarasa dhātuyo", "Пятнадцать элементов"),
               ("Dve saccā", "Две истины"), ("Tīṇi saccāni", "Три истины"),
               ("Bāvīsatindriyā", "Двадцать две способности"),
               ("Tayo akusalahetū", "Три неблагих корня"), ("Tayo kusalahetū", "Три благих корня"),
               ("Tayo abyākatahetū", "Три этически неопределённых корня"), ("Cha hetū", "Шесть корней"),
               ("Nava hetū", "Девять корней"), ("Satta hetū", "Семь корней"),
               ("Tayo āhārā", "Три вида питания"), ("Cattāro āhārā", "Четыре вида питания"),
               ("Cha phassā", "Шесть видов контакта"), ("Pañca phassā", "Пять видов контакта"),
               ("Satta phassā", "Семь видов контакта"), ("Satta vedanā", "Семь чувств"),
               ("Cha vedanā", "Шесть чувств"), ("Cha saññā", "Шесть восприятий"), ("Cha cetanā", "Шесть намерений"),
               ("Cha cittā", "Шесть видов ума")):
    _s(_p, _r, "p", "p")
for _p, _r in K45.SUBJ45.items():
    if _p.endswith("indriyā") and _r[1] == "p":
        _s(_p, _r[0], "p", "p")
for _p in ("Domanassindriyaṃ", "Anaññātaññassāmītindriyaṃ", "Aññindriyaṃ", "Aññātāvindriyaṃ", "Jīvitindriyaṃ",
           "Upekkhindriyaṃ"):
    _r = cap(IND[IND_P[low(_p)]])
    _s(_p, _r, "s", "f", _r.replace("Жизненная", "Жизненную"))
for _p, _k in (("Manāyatanaṃ", "mana"), ("Dhammāyatanaṃ", "dhamma"), ("Rūpāyatanaṃ", "rūpa"),
               ("Saddāyatanaṃ", "sadda")):
    _s(_p, cap(AY[_k]), "s", "f", "Сферу " + AY[_k].split(" ", 1)[1])
_s("Gandhāyatanaṃ… rasāyatanaṃ… phoṭṭhabbāyatanaṃ", f"{cap(AY['gandha'])}… {AY['rasa']}… {AY['phoṭṭhabba']}", "s",
   "f", f"Сферу {AY['gandha'].split(' ', 1)[1]}… сферу {AY['rasa'].split(' ', 1)[1]}… сферу "
        f"{AY['phoṭṭhabba'].split(' ', 1)[1]}")
for _p, _k in (("Dhammadhātu", "dhamma"), ("Manoviññāṇadhātu", "manoviññāṇa"), ("Manodhātu", "mano"),
               ("Rūpadhātu", "rūpa"), ("Saddadhātu", "sadda"), ("Kāyaviññāṇadhātu", "kāyaviññāṇa")):
    _s(_p, cap(DH[_k]), "s", "m")
_s("Gandhadhātu… rasadhātu… phoṭṭhabbadhātu", f"{cap(DH['gandha'])}… {DH['rasa']}… {DH['phoṭṭhabba']}", "s", "m")
for _p, _k in (("Samudayasaccaṃ", "samudaya"), ("Maggasaccaṃ", "magga"), ("Nirodhasaccaṃ", "nirodha"),
               ("Dukkhasaccaṃ", "dukkha")):
    _s(_p, cap(TRUTH[_k]), "s", "f", cap(TRUTH[_k]).replace("Истина", "Истину"))
_s("Kabaḷīkāro āhāro", cap(AHARA["kabaḷīkāro āhāro"]), "s", "f", "Съедаемую пищу")
for _p, _k in (("Manoviññāṇadhātusamphasso", "manoviññāṇadhātu"), ("Manodhātusamphasso", "manodhātu"),
               ("Kāyaviññāṇadhātusamphasso", "kāyaviññāṇadhātu")):
    _s(_p, cap(PH[_k]), "s", "m")
_s("Doso akusalahetu", cap(item_ru("doso akusalahetu")), "s", "f")
_s("Moho akusalahetu", cap(item_ru("moho akusalahetu")), "s", "n")      # neuter (заблуждение)
for _n in ("vedanā", "saññā", "cetanā"):
    _s(f"Manoviññāṇadhātusamphassajā {_n}", cap(item_ru(f"manoviññāṇadhātusamphassajā {_n}")), "s", "n")
# runs of the counted mental factors («Cha vedanā… cha saññā… cha cetanā… cha cittā» …)
RUN_NOUN = {"phassā": "phassa", "vedanā": "vedanā", "saññā": "saññā", "cetanā": "cetanā", "cittā": "citta"}


def _run(num, words):
    p = "… ".join(f"{num if i else cap(num)} {w}" for i, w in enumerate(words))
    r = "… ".join(count_ru(f"{num} {'cittāni' if w == 'cittā' else w}") for w in words)
    _s(p, cap(r), "p", "p")


for _num, _ws in (("cha", ["vedanā", "saññā", "cetanā", "cittā"]), ("satta", ["vedanā", "saññā", "cetanā", "cittā"]),
                  ("satta", ["phassā", "vedanā", "saññā", "cetanā", "cittā"]),
                  ("pañca", ["vedanā", "saññā", "cetanā", "cittā"]), ("pañca", ["saññā", "cetanā", "cittā"])):
    _run(_num, _ws)


def norm_subj(ln):
    """…pe… inside a subject run = «…»; «saññā …» = «saññā…»"""
    ln = re.sub(r"\s*…pe…\s*", "… ", ln)
    ln = re.sub(r" …", "…", ln)
    if "satta cetanā satta cittā" in ln:
        ln = ln.replace("satta cetanā satta cittā", "satta cetanā… satta cittā")
        slip("^2-1043 «satta cetanā satta cittā»: the «…» of the run is missing (rendered with «…»)")
    return ln


def match_subj(ch):
    c = ch[0].upper() + ch[1:]
    for k in sorted(SUBJ18, key=len, reverse=True):
        if c == k or c.startswith(k + " "):
            return k
    return None


def groups_of(sent):
    """sentence -> [(separator before, subject key, [(separator, token)…])]"""
    chunks = re.split(r"(; |, )", sent)
    groups, sep = [], ""
    for i, ch in enumerate(chunks):
        if i % 2 == 1:
            sep = ch.strip()
            continue
        k = match_subj(ch)
        if k:
            rest = ch[len(k) + 1:]
            groups.append([sep, k, [("", rest)]])
        else:
            assert groups, sent
            groups[-1][2].append((sep, ch))
    return groups


def run_engine(ln, render, use_acc=False):
    out = []
    for sent in re.split(r"(?<=\.) (?=\S)", ln):
        assert sent.endswith("."), sent
        res = ""
        for gi, (sep, k, toks) in enumerate(groups_of(sent[:-1])):
            nom, acc, num, gen = SUBJ18[k]
            subj = acc if use_acc else nom
            body = render(toks, num, gen)
            if gi == 0:
                res = f"{cap(subj)} {body}"
            else:
                res += f"{sep} {low(subj)} {body}"
        out.append(res + ".")
    return " ".join(out)


# ---- section 3: included in the worlds
REALM = {None: "к кругам существования", "kāmadhātu": "к миру чувственных желаний", "rūpadhātu": "к миру форм",
         "arūpadhātu": "к миру без форм"}
BELONG = {"s": "принадлежит", "p": "принадлежат"}            # pariyāpanna «принадлежащий к …» (termbase)


def belong_tok(tok, num):
    m = re.match(r"^(siyā )?(na )?((?:kāma|rūpa|arūpa)dhātu)?(a?)pariyāpann\w+$", tok)
    assert m, tok
    siya, na, realm, a = m.groups()
    neg = bool(na) or a == "a"
    return f"{'иногда ' if siya else ''}{'не ' if neg else ''}{BELONG[num]} {REALM[realm]}"


def belong_render(toks, num, gen):
    return "".join((f"{s} " if s else "") + belong_tok(t, num) for s, t in toks)


# ---- section 7: to be directly known …
GER = [("abhiññeyy", "постичь высшим знанием", None), ("pariññeyy", "полностью понять", None),
       ("pahātabb", "устранить", "устранять"), ("bhāvetabb", "развивать", "развивать"),
       ("sacchikātabb", "осуществить", "осуществлять")]


def _ger(w):
    for st, pos, neg in GER:
        if w.startswith(st):
            return pos, neg
    raise KeyError(w)


def ought_tok(tok):
    words = tok.split(" ")
    siya = words[0] == "siyā"
    if siya:
        words = words[1:]
    seq, i = [], 0
    while i < len(words):
        if words[i] == "na":
            seq.append((True, _ger(words[i + 1])[1]))
            i += 2
        else:
            seq.append((False, _ger(words[i])[0]))
            i += 1
    parts, j = [], 0
    while j < len(seq):
        neg = seq[j][0]
        run = []
        while j < len(seq) and seq[j][0] == neg:
            run.append(seq[j][1])
            j += 1
        if not neg:
            parts.append("следует " + (nlist(run) if len(run) > 1 else run[0]))
        elif len(run) == 1:
            parts.append("не следует " + run[0])
        else:
            parts.append("не следует ни " + ", ни ".join(run))
    return ("иногда " if siya else "") + ", ".join(parts)


def ought_render(toks, num, gen):
    return "".join((f"{s} " if s else "") + ought_tok(t) for s, t in toks)


# ---- section 8: with an object
OBJ = [("sārammaṇārammaṇ", "имеет объектом то, что имеет объект", "имеют объектом то, что имеет объект"),
       ("anārammaṇārammaṇ", "имеет объектом то, что не имеет объекта", "имеют объектом то, что не имеет объекта"),
       ("sārammaṇ", "имеет объект", "имеют объект"), ("anārammaṇ", "не имеет объекта", "не имеют объекта")]


def obj_tok(tok, num):
    m = re.match(r"^(siyā )?(\w+)$", tok)
    assert m, tok
    for st, s, p in OBJ:
        if m.group(2).startswith(st):
            return ("иногда " if m.group(1) else "") + (s if num == "s" else p)
    raise KeyError(tok)


def obj_render(toks, num, gen):
    return "".join((f"{s} " if s else "") + obj_tok(t, num) for s, t in toks)


# ---- section 9: seen, heard, sensed, cognised
SEEN = [("diṭṭh", "увиденн"), ("sut", "услышанн"), ("mut", "ощущённ"), ("viññāt", "познанн")]   # pi-1 ^1-586 forms
INS_END = {"f": "ой", "m": "ым", "n": "ым", "p": "ыми"}
BE = {"s": "является", "p": "являются"}


def _seen(w, gen):
    for st, r in SEEN:
        if w.startswith(st):
            return r + INS_END[gen]
    raise KeyError(w)


def seen_tok(tok, gen):
    """-> (siyā, negative, [instrumentals])"""
    words = tok.split(" ")
    siya = words[0] == "siyā"
    if siya:
        words = words[1:]
    if words[0] == "na":
        assert all(w == "na" for w in words[::2]), tok
        return siya, True, [_seen(w, gen) for w in words[1::2]]
    assert len(words) == 1, tok
    return siya, False, [_seen(words[0], gen)]


def seen_parts(parsed, num):
    out, prev = [], None
    for siya, neg, ins in parsed:
        if neg:
            r = f"не {BE[num]} " + (ins[0] if len(ins) == 1 else "ни " + ", ни ".join(ins))
        else:
            r = f"{BE[num]} {ins[0]}"
            if prev is not None and not prev[1] and prev[0] == siya:
                r = ins[0]
            elif prev is not None and prev[1] and not siya:
                r = "но " + r
        out.append(("иногда " if siya else "") + r)
        prev = (siya, neg)
    return out


def seen_render(toks, num, gen):
    parts = seen_parts([seen_tok(t, gen) for _, t in toks], num)
    return "".join((f"{s} " if s else "") + p for (s, _), p in zip(toks, parts))


# =========================================================================== question lines («kati …?»)
GROUPS = {"pañcannaṃ khandhānaṃ": "из пяти совокупностей", "sattannaṃ cittānaṃ": "из семи видов ума",
          "dvādasannaṃ āyatanānaṃ": "из двенадцати сфер восприятия",
          "aṭṭhārasannaṃ dhātūnaṃ": "из восемнадцати элементов", "catunnaṃ saccānaṃ": "из четырёх истин"}


def q_matrix(its):
    """section 10: «являются благими, сколько неблагими …» (K1 question phrases)"""
    out = []
    for i, w in enumerate(its):
        ins = K1.item(K1.PL_KEY[w])["insp"]
        out.append(f"являются {ins}" if i == 0 else ins)
    return out


def q_belong(its):
    return [belong_tok(w, "p") for w in its]


def q_ought(its):
    return [", ".join(ought_tok(x) for x in w.split(", ")) for w in its]


def q_obj(its):
    return [obj_tok(w, "p") for w in its]


def q_seen(its):
    return seen_parts([seen_tok(w, "p") for w in its], "p")


def kati_question(ln, fn):
    out = []
    for q in re.split(r"(?<=\?) ", ln):
        assert q.endswith("?"), q
        parts = re.split(r"\s*…pe…\s*", q[:-1])
        rs = []
        for part in parts:
            m = re.match(r"^(\S+ \S+) (kati .+)$", part)
            grp, body = m.groups()
            its = re.split(r", (?=kati )", body)
            assert all(x.startswith("kati ") for x in its), part
            r = fn([x[5:] for x in its])
            rs.append(f"сколько {GROUPS[low(grp)]} " + ", сколько ".join(r))
        out.append(cap("… ".join(rs)) + "?")
    return " ".join(out)


# =========================================================================== section 10: the K23 / K45 engine
def install():
    K45.install()
    for p, (nom, acc, num, gen) in SUBJ18.items():
        if p not in K23.SUBJ:
            K23.SUBJ[p] = (nom, num, "m" if gen == "n" else gen, acc)


NEW_SUBJ_RX = re.compile(r"^(.*?), ((?:kāyaviññāṇadhātu|manoviññāṇadhātu) siyā .*)$")
PANHA_FIX18 = [  # (bad, good, note)
    ("sampayuttoti pi,", "sampayuttotipi,", "^2-1039 «sampayuttoti pi» written apart (= sampayuttotipi)"),
    ("siyā dukkhamasukhāya vedanāya sampayutto.", "siyā adukkhamasukhāya vedanāya sampayutto.",
     "^2-1039 «Moho akusalahetu … siyā dukkhamasukhāya vedanāya sampayutto» (initial a- missing): rendered as meant "
     "«с чувством, которое ни болезненно, ни приятно»"),
    ("siyā vipākā siyā vipākadhammadhammā", "siyā vipākā, siyā vipākadhammadhammā",
     "^2-1040 «siyā vipākā siyā vipākadhammadhammā»: comma missing (added)"),
    ("siyā avitakkaavicāro siyā na vattabbo", "siyā avitakkaavicāro, siyā na vattabbo",
     "^2-1042 «siyā avitakkaavicāro siyā na vattabbo»: comma missing (added)"),
    ("pañca cittā avitakkaavicārā manodhātu savitakkasavicārā,", "pañca cittā avitakkaavicārā. Manodhātu savitakkasavicārā,",
     "^2-1042 «… pañca cittā avitakkaavicārā manodhātu savitakkasavicārā»: full stop missing (two sentences in Russian)"),
]


def quote_nv18(sent):
    """«na vattabbā/-o/-aṃ X(n)tipi, Y(n)tipi» (no dash, no quotes here) -> the K23 form with dash and quotes"""
    toks = sent.split(", ")
    out, in_nv = [], False
    for t in toks:
        m = re.match(r"^(.*?\b[Nn]a vattabb(?:o|ā|aṃ)) (.+?)(ntipi|tipi)$", t)
        if m:
            out.append(f'{m.group(1)} – "{m.group(2)}"{m.group(3)}')
            in_nv = True
            continue
        m = re.match(r"^(.+?)(ntipi|tipi)$", t)
        if in_nv and m:
            out.append(f'"{m.group(1)}"{m.group(2)}')
            continue
        in_nv = False
        out.append(t)
    return ", ".join(out)


NV_DASH = K1.NV.split(" ", 1)[1]                          # «определить –»


def panha_sentence(sent):
    m = NEW_SUBJ_RX.match(sent)
    if m:
        slip("^2-1039 / 1042 «…, kāyaviññāṇadhātu / manoviññāṇadhātu siyā …»: a new subject after a comma (kept, "
             "lower case)")
        return f"{panha_sentence(m.group(1))}, {low(panha_sentence(cap(m.group(2))))}"
    r = K23.sentence(quote_nv18(sent))
    if sent.startswith("Moho akusalahetu"):                 # neuter subject: «связано»
        r = re.sub(r"\bсвязан\b", "связано", r)
    return r.replace(f"{NV_DASH} ", NV_DASH[:-2] + " ")   # no Pāli dash after na vattabbā here


def panha_line(ln):
    assert "–" not in ln, ln
    for bad, good, note in PANHA_FIX18:
        if bad in ln:
            ln = ln.replace(bad, good)
            slip(note)
    ln = norm_subj(ln)
    out = []
    for s in re.split(r"(?<=\.) (?=\S)", ln):
        assert s.endswith("."), s
        out.append(panha_sentence(s[:-1]) + ".")
    return " ".join(out)


# =========================================================================== manual segments (sections 5, 6, 10 end)
REALM_FRAME = "Если взять снизу границей {low}, а сверху включить в эти пределы {high}, то всё, что находится в этих " \
              "пределах, относится к этому миру и принадлежит к нему:"      # ch. 3 ^2-182 (pi-1 ^1-1287 «за границу»)
MIND_OF = ("ум и сопутствующие уму явления того, кто вошёл в медитативное достижение, или того, кто переродился, или "
           "того, кто пребывает в счастье в этой жизни")                   # pi-1 ^1-1289
SPHERE = {"kāma": "явления, относящиеся к миру чувственных желаний", "rūpa": "явления, относящиеся к миру форм",
          "arūpa": "явления, относящиеся к миру без форм"}
P1_NOT = {  # pi-1 ^1-1288 / 1290 / 1292 (whole sentences)
    "kāma": ("Что такое явления, не относящиеся к миру чувственных желаний? Явления, относящиеся к миру форм и к "
             "миру без форм, и явления, не принадлежащие к кругам существования, – это явления, не относящиеся к миру "
             "чувственных желаний."),
    "rūpa": ("Что такое явления, не относящиеся к миру форм? Явления, относящиеся к миру чувственных желаний и к миру "
             "без форм, и явления, не принадлежащие к кругам существования, – это явления, не относящиеся к миру форм."),
    "arūpa": ("Что такое явления, не относящиеся к миру без форм? Явления, относящиеся к миру чувственных желаний и к "
              "миру форм, и явления, не принадлежащие к кругам существования, – это явления, не относящиеся к миру без "
              "форм."),
}
P1_PARIY = ("Подверженные влечениям благие, неблагие и этически неопределённые явления, относящиеся к миру "
            "чувственных желаний, к миру форм или к миру без форм")       # pi-1 ^1-1293
P1_APARIY = ("Что такое явления, не принадлежащие к кругам существования? Пути, плоды путей и необусловленный "
             "элемент – это явления, не принадлежащие к кругам существования.")   # pi-1 ^1-1294
CH3_FRAME = ("Если взять снизу границей ад Авичи, а сверху включить в эти пределы богов, властвующих над творениями "
             "других, то всё, что находится в этих пределах, относится к этому миру и принадлежит к нему:")

GODS = {  # genitive plural («в обществе …», «жизни …»)
    "cātumahārājika": "богов Четырёх Великих Царей", "tāvatiṃsa": "богов Тридцати трёх", "yāma": "богов Ямы",
    "tusita": "богов Тушиты", "nimmānarati": "богов, наслаждающихся творением",
    "paranimmitavasavattī": "богов, властвующих над творениями других",
    "brahmapārisajja": "богов из свиты Брахмы", "brahmapurohita": "богов из числа советников Брахмы",
    "mahābrahmā": "богов, Великих Брахм", "parittābha": "богов ограниченного сияния",
    "appamāṇābha": "богов безмерного сияния", "ābhassara": "богов струящегося сияния",
    "parittasubha": "богов ограниченного великолепия", "appamāṇasubha": "богов безмерного великолепия",
    "subhakiṇha": "богов сплошного великолепия", "asaññasatta": "богов без восприятия",
    "vehapphala": "богов великого плода", "aviha": "богов, не отпадающих от своего мира",
    "atappa": "невозмутимых богов", "sudassa": "богов прекрасного облика", "sudassī": "богов ясного видения",
    "akaniṭṭha": "высочайших богов",
    "ākāsānañcāyatanūpaga": "богов, достигших сферы бесконечного пространства",
    "viññāṇañcāyatanūpaga": "богов, достигших сферы бесконечного сознания",
    "ākiñcaññāyatanūpaga": "богов, достигших сферы отсутствия чего-либо",
    "nevasaññānāsaññāyatanūpaga": "богов, достигших сферы ни восприятия, ни невосприятия",
}
REBORN = "перерождаются в обществе"                      # sahabyataṃ upapajjanti
SOME_REBORN = f"некоторые {REBORN}"                       # appekacce … sahabyataṃ upapajjanti
HOW_LONG = "Какова продолжительность жизни"               # kittakaṃ āyuppamāṇaṃ?
HOW_LONG_THEM = "Какова продолжительность их жизни?"      # Tesaṃ kittakaṃ āyuppamāṇaṃ?
HUMAN_COUNT = "Сколько это составляет по человеческому счёту?"   # Manussānaṃ gaṇanāya kittakaṃ hoti?
DAY = "составляют одни сутки"                             # eso eko rattindivo
MONTH = "Тридцать таких ночей составляют месяц."           # Tāya rattiyā tiṃsa rattiyo māso.
YEAR = "Двенадцать таких месяцев составляют год."         # Tena māsena dvādasamāsiyo saṃvaccharo.
JHANA = {"Paṭhamaṃ": "первое", "Dutiyaṃ": "второе", "Tatiyaṃ": "третье"}
DEGREE = {"parittaṃ": "ограниченное", "majjhimaṃ": "среднее", "paṇītaṃ": "высшее"}


def lifespan(god, human, divine, total, var=""):
    g = GODS[god]
    verb = "составляет" if divine.startswith("Тысяча") else "составляют"
    return (f"{HOW_LONG} {g}? {human} человеческих лет {DAY} {g}{var}. {MONTH} {YEAR} {divine} таких божественных лет "
            f"{verb} продолжительность жизни {g}. {HUMAN_COUNT} {total} лет.")


def jhana_line(n, deg, god, life):
    j = f"{DEGREE[deg]} {JHANA[n]} медитативное погружение"
    return (f"Где перерождаются, развив {j}? Развив {j}, {REBORN} {GODS[god]}. {HOW_LONG_THEM} {life}.")


def manual():
    h = {}
    h["2-1020"] = [
        "; ".join(cap(x) if i == 0 else x for i, x in enumerate(
            [SPHERE["kāma"], "явления, не относящиеся к миру чувственных желаний", SPHERE["rūpa"],
             "явления, не относящиеся к миру форм", SPHERE["arūpa"], "явления, не относящиеся к миру без форм",
             "явления, принадлежащие к кругам существования", "явления, не принадлежащие к кругам существования"]))
        + ".",
        f"Что такое {SPHERE['kāma']}? {CH3_FRAME} совокупности, элементы и сферы восприятия; материальная форма, "
        f"чувство, восприятие, формирующие факторы, сознание – это {SPHERE['kāma']}.",
        P1_NOT["kāma"],
        f"Что такое {SPHERE['rūpa']}? "
        + REALM_FRAME.format(low="мир Брахмы", high=GODS["akaniṭṭha"]) + f" {MIND_OF}, – это {SPHERE['rūpa']}.",
        P1_NOT["rūpa"],
        f"Что такое {SPHERE['arūpa']}? "
        + REALM_FRAME.format(low=GODS["ākāsānañcāyatanūpaga"], high=GODS["nevasaññānāsaññāyatanūpaga"])
        + f" {MIND_OF}, – это {SPHERE['arūpa']}.",
        P1_NOT["arūpa"],
        f"Что такое явления, принадлежащие к кругам существования? {P1_PARIY}: {nlist([KH[k] for k in S.ORDER])} – "
        "это явления, принадлежащие к кругам существования.",
        P1_APARIY,
    ]
    gifts = "Совершив даяние, взяв на себя соблюдение нравственности и соблюдя постный день"
    # dānaṃ datvā, sīlaṃ samādiyitvā, uposathakammaṃ katvā
    reborn = ", ".join(f"{SOME_REBORN} {x}" for x in
                       ["богатых знатных правителей", "богатых брахманов", "богатых домохозяев"]
                       + [GODS[g] for g in ("cātumahārājika", "tāvatiṃsa", "yāma", "tusita", "nimmānarati",
                                            "paranimmitavasavattī")])
    h["2-1021"] = [
        "«Боги». Три вида богов – условные боги [вариант написания (Syā.): sammatidevā], боги по рождению и боги по "
        "чистоте.",
        "Условные боги – это цари, царицы и царевичи.",
        f"Боги по рождению – это боги, начиная с {GODS['cātumahārājika']} [вариант написания (Sī., Syā.): "
        "cātummahārājike], и выше.",
        "Боги по чистоте – так называются архаты.",
        f"{gifts}, где перерождаются? {gifts}, {reborn}.",
    ]
    h["2-1022"] = [f"{HOW_LONG} людей? Сто лет, немного меньше или больше [вариант чтения (Syā., Ka.): appaṃ vā "
                   "bhiyyo vā; см. Дигха-никаю, 2.7]."]
    h["2-1023"] = [
        lifespan("cātumahārājika", "Пятьдесят", "Пятьсот", "Девять миллионов",
                 " [вариант написания (Ka.): rattidivo; см. Ангуттара-никаю, 3.71]"),
        lifespan("tāvatiṃsa", "Сто", "Тысяча", "Тридцать шесть миллионов"),
        lifespan("yāma", "Двести", "Две тысячи", "Сто сорок четыре миллиона"),
        lifespan("tusita", "Четыреста", "Четыре тысячи", "Пятьсот семьдесят шесть миллионов"),
        lifespan("nimmānarati", "Восемьсот", "Восемь тысяч", "Два миллиарда триста четыре миллиона"),
        lifespan("paranimmitavasavattī", "Тысяча шестьсот", "Шестнадцать тысяч",
                 "Девять миллиардов двести шестнадцать миллионов"),
        "Эти шесть [вариант чтения (Syā.): chapi te], относящиеся к миру чувственных желаний, изобилуют всеми "
        "чувственными благами;",
        "Вот сколько составляет срок жизни их всех, если сложить вместе.",
        "У них двенадцать миллиардов и двести восемьдесят миллионов;",
        "И пять миллионов лет, как возвещено при подсчёте в годах.",
    ]
    h["2-1024"] = [jhana_line("Paṭhamaṃ", "parittaṃ", "brahmapārisajja", "Третья часть эпохи"),
                   jhana_line("Paṭhamaṃ", "majjhimaṃ", "brahmapurohita", "Половина эпохи"),
                   jhana_line("Paṭhamaṃ", "paṇītaṃ", "mahābrahmā", "Эпоха [вариант чтения (Syā.): eko kappo]")]
    h["2-1025"] = [jhana_line("Dutiyaṃ", "parittaṃ", "parittābha", "Две эпохи"),
                   jhana_line("Dutiyaṃ", "majjhimaṃ", "appamāṇābha", "Четыре эпохи"),
                   jhana_line("Dutiyaṃ", "paṇītaṃ", "ābhassara", "Восемь эпох")]
    h["2-1026"] = [jhana_line("Tatiyaṃ", "parittaṃ", "parittasubha", "Шестнадцать эпох"),
                   jhana_line("Tatiyaṃ", "majjhimaṃ", "appamāṇasubha", "Тридцать две эпохи"),
                   jhana_line("Tatiyaṃ", "paṇītaṃ", "subhakiṇha", "Шестьдесят четыре эпохи")]
    diff = nlist([f"различия {x}" for x in ("объектов", "внимания", "желания", "устремления", "решимости",
                                            "направленности", "мудрости")])
    # ārammaṇa-, manasikāra-, chanda-, paṇidhi-, adhimokkha-, abhinīhāra-, paññā-nānattatā
    fourth = [GODS[g] for g in ("asaññasatta", "vehapphala", "aviha", "atappa", "sudassa", "sudassī", "akaniṭṭha",
                                "ākāsānañcāyatanūpaga", "viññāṇañcāyatanūpaga", "ākiñcaññāyatanūpaga",
                                "nevasaññānāsaññāyatanūpaga")]
    h["2-1027"] = [
        f"Развив четвёртое медитативное погружение, в силу {diff} " + ", ".join(f"{SOME_REBORN} {g}" for g in fourth)
        + ".",
        f"{HOW_LONG} {GODS['asaññasatta']} и {GODS['vehapphala']}? Пятьсот эпох.",
        f"{HOW_LONG} {GODS['aviha']}? Тысяча эпох.",
        f"{HOW_LONG} {GODS['atappa']}? Две тысячи эпох.",
        f"{HOW_LONG} {GODS['sudassa']}? Четыре тысячи эпох.",
        f"{HOW_LONG} {GODS['sudassī']}? Восемь тысяч эпох.",
        f"{HOW_LONG} {GODS['akaniṭṭha']}? Шестнадцать тысяч эпох.",
    ]
    h["2-1028"] = [f"{HOW_LONG} {GODS['ākāsānañcāyatanūpaga']}? Двадцать тысяч эпох.",
                   f"{HOW_LONG} {GODS['viññāṇañcāyatanūpaga']}? Сорок тысяч эпох.",
                   f"{HOW_LONG} {GODS['ākiñcaññāyatanūpaga']}? Шестьдесят тысяч эпох.",
                   f"{HOW_LONG} {GODS['nevasaññānāsaññāyatanūpaga']}? Восемьдесят четыре тысячи эпох."]
    h["2-1029"] = [
        "Вознесённые силой заслуг, ушедшие в удел мира чувственных желаний и мира форм,",
        "Достигшие даже вершины существования [вариант чтения (Syā.): bhavaggaṃ vāpi], вновь приходят [вариант чтения "
        "(Syā.): puna gacchanti] в дурной удел.",
        "Даже столь долгоживущие существа умирают, когда исчерпан срок жизни;",
        "Нет никакого постоянного существования, так сказано великим мудрецом.",
        "Поэтому мудрые, благоразумные, проницательные, размышляющие о смысле,",
        "Ради освобождения от старения и смерти развивают высший путь.",
        "Развив чистый путь, ведущий к погружению в нирвану,",
        "Полностью поняв все влечения, они, свободные от влечений, достигают окончательного угасания.",
    ]
    h["2-1017"] = [
        f"{cap(LOC4['Asaññasattānaṃ devānaṃ'])} {MOMENT} сколько {KATI['khandhā']} появляется… сколько "
        f"{KATI['cittāni']} появляется?",
        f"{cap(LOC4['Asaññasattānaṃ devānaṃ'])} {MOMENT} появляется {count_ru('eko khandho')} – {KH['rupa']}; "
        f"появляются {count_ru('dve āyatanāni')} – {AY['rūpa']} и {AY['dhamma']}; появляются {count_ru('dve dhātuyo')} "
        f"– {DH['rūpa']} и {DH['dhamma']}; появляется {count_ru('ekaṃ saccaṃ')} – {TRUTH['dukkha']}; появляется "
        f"{count_ru('ekindriyaṃ')} – {IND['rūpajīvita']}. Боги без восприятия появляются без корней, без питания, без "
        "контакта, без чувства, без восприятия, без намерения, без ума.",
    ]
    return h


SUMMARY = ["Высшее знание, два раздела об объекте, увиденное, благое и чувство;",     # Abhiññā dve sārammaṇā, …
           "Результат действий и охваченное цеплянием, направленная мысль, материальная форма и мирское."]
DONE_LINES = [f"{TITLE} {S.DONE}.", "Книга «Подробный разбор» завершена."]   # … niṭṭhito. / Vibhaṅgapakaraṇaṃ niṭṭhitaṃ.


# =========================================================================== chapter
def heading(ln):
    lvl, text = ln.split(" ", 1)
    return f"{lvl} {HEAD[text]}"


def build():
    pali = (S.PALI / PART).read_text(encoding="utf-8")
    h = manual()
    section = None
    for sid, lines in S.segs(pali):
        lines = [re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", ln) for ln in lines]
        if lines[0].startswith("#"):
            assert len(lines) == 1
            h[sid] = [heading(lines[0])]
            if lines[0].startswith("#### "):
                section = lines[0].split(" ", 1)[1]
            continue
        if sid in h:
            continue
        ru = []
        for ln in lines:
            if section in ("Sabbasaṅgāhikavāro", "Uppattānuppattivāro"):
                ru.append(counts_line(ln))
            elif section == "Dhammadassanavāro":
                ru.append(appear_line(ln))
            elif ln.endswith("?"):
                fn = {"Pariyāpannāpariyāpannavāro": q_belong, "Abhiññeyyādivāro": q_ought,
                      "Sārammaṇānārammaṇavāro": q_obj, "Diṭṭhasutādidassanavāro": q_seen,
                      "Tikādidassanavāro": q_matrix}[section]
                ru.append(kati_question(re.sub(r" …pe…", "…pe…", ln), fn))
            elif section == "Pariyāpannāpariyāpannavāro":
                if "kāmadhātu pariyāpanno" in ln:
                    ln = ln.replace("kāmadhātu pariyāpanno", "kāmadhātupariyāpanno")
                    slip("^2-1000 «siyā kāmadhātu pariyāpanno» written apart (= kāmadhātupariyāpanno)")
                ru.append(run_engine(norm_subj(ln), belong_render))
            elif section == "Abhiññeyyādivāro":
                ru.append(run_engine(norm_subj(ln), ought_render, use_acc=True))
            elif section == "Sārammaṇānārammaṇavāro":
                if "sārammaṇārammaṇo siyā anārammaṇārammaṇo" in ln:
                    ln = ln.replace("sārammaṇārammaṇo siyā", "sārammaṇārammaṇo, siyā")
                    slip("^2-1035 «siyā sārammaṇārammaṇo siyā anārammaṇārammaṇo»: comma missing (added)")
                ru.append(run_engine(norm_subj(ln), obj_render))
            elif section == "Diṭṭhasutādidassanavāro":
                ru.append(run_engine(norm_subj(ln), seen_render))
            elif section == "Tikādidassanavāro":
                if ln.startswith("Abhiññā dve"):
                    ru.append(SUMMARY[0])
                elif ln.startswith("Vipākā ca"):
                    ru.append(SUMMARY[1])
                elif ln == "Dhammahadayavibhaṅgo niṭṭhito.":
                    ru.append(DONE_LINES[0])
                elif ln == "Vibhaṅgapakaraṇaṃ niṭṭhitaṃ.":
                    ru.append(DONE_LINES[1])
                else:
                    if ln.startswith("Rūpakkhandho siyā upādinnupādāniyo, siyā anupādinnupādāniyo 4."):
                        ln = ln.replace(" 4.", ".", 1)
                        slip("^2-1041 «… siyā anupādinnupādāniyo 4.»: a stray footnote digit «4» (kept as written)")
                        r = panha_line(ln)
                        first, rest = r.split(". ", 1)
                        ru.append(f"{first} 4. {rest}")
                    else:
                        ru.append(panha_line(ln))
            else:
                raise ValueError((sid, ln))
        h[sid] = ru
    # per-line dash check against the Pāli (DASH RULE)
    for sid, lines in S.segs(pali):
        for p, r in zip(lines, h[sid]):
            assert p.count("–") + p.count("—") == r.count("–"), (sid, p, r)
    return pali, h


# =========================================================================== pi-1 / earlier-chapter checks
def check_reuse():
    K23.assert_pi1(f"{ROOTS3} {VIPAKATO} {KIRIYA}", P1_NOT["kāma"], P1_NOT["rūpa"], P1_NOT["arūpa"], P1_PARIY,
                   P1_APARIY, MIND_OF, "Это три неблагих корня.", "жадность как неблагой корень")
    ch3 = (S.OUT / "3-dhatuvibhango.md").read_text(encoding="utf-8")
    assert CH3_FRAME in ch3
    ch1 = (S.OUT / "1-khandhavibhango.md").read_text(encoding="utf-8")
    assert "рождённое контактом элемента ума чувство и рождённое контактом элемента умственного сознания чувство" in ch1
    ch17 = (S.OUT / "17-khuddakavatthuvibhango.md").read_text(encoding="utf-8")
    assert "Таковы три неблагих корня." in ch17


# =========================================================================== notes
def notes_md():
    L = ["# pi-2 Russian rails: new formulas of chapter 18 (^2-978 … ^2-1044)", "",
         "Generated by build_rails_18_ru.py; import it instead of retyping. Strings already in ru-rails-formulas.md "
         "(sample), notes-1 … notes-17 or the pi-1 rails are not repeated.", "",
         "## Headings", ""]
    L += [f"{p} = {r}" for p, r in HEAD.items()]
    L += ["", "## Counts (Dhammahadaya)", "",
          "kati X (khandhā, āyatanāni, dhātuyo, saccāni, indriyāni, hetū, āhārā, phassā, vedanā, saññā, cetanā, "
          "cittāni) = сколько " + ", ".join(KATI[k] for k in ("khandhā", "āyatanāni", "dhātuyo", "saccāni",
                                                             "indriyāni", "hetū", "āhārā", "phassā", "vedanā",
                                                             "saññā", "cetanā", "cittāni")),
          "N phassā / eko phasso = N видов контакта / один вид контакта (senses part 3); N āhārā = N видов питания; "
          "N cittāni / cittā / ekaṃ cittaṃ = N видов ума / один вид ума; N vedanā / saññā / cetanā = N чувств / "
          "восприятий / намерений; N hetū = N корней",
          "instrumental (vuccanti): " + ", ".join(count_ru(x, "ins") for x in
                                                  ("pañcakkhandhā", "dvādasāyatanāni", "aṭṭhārasa dhātuyo",
                                                   "cattāri saccāni", "bāvīsatindriyāni", "nava hetū",
                                                   "cattāro āhārā", "satta phassā", "satta vedanā", "satta saññā",
                                                   "satta cetanā", "satta cittāni", "ekaṃ cittaṃ")),
          "Kāmadhātuyā / Rūpadhātuyā / Arūpadhātuyā / Apariyāpanne (with counts) = " + " / ".join(LOC.values()),
          "Kāmadhātuyā kati khandhā, …? = В мире чувственных желаний сколько совокупностей, …?",
          "Tattha katame kāmadhātuyā pañcakkhandhā? … – ime vuccanti \"kāmadhātuyā pañcakkhandhā\". = Что такое здесь "
          "пять совокупностей в мире чувственных желаний? … – это называется «пятью совокупностями в мире чувственных "
          "желаний».",
          "Tayo kusalahetū, tayo akusalahetū, tayo abyākatahetū = " + cap(nlist([list(HETU_GROUP.values())[i]
                                                                                 for i in (0, 1, 3)])),
          "Alobho kusalahetu … / Lobho akusalahetu … = " + item_ru("alobho kusalahetu") + " … / "
          + item_ru("lobho akusalahetu") + " …",
          "alobho vipākahetu = " + item_ru("alobho vipākahetu") + " (items joined with «;»)",
          "– ime tayo kusalahetū. = – таковы три благих корня. (ch. 17 «– таковы N X»; pi-1 ^1-1067 «Это три …»)",
          f"Kusalānaṃ vā dhammānaṃ vipākato kiriyābyākatesu vā dhammesu alobho, adoso, amoho = {ROOTS3} {VIPAKATO} "
          f"{KIRIYA} (pi-1 ^1-1068)",
          "Kabaḷīkārāhāro, phassāhāro, manosañcetanāhāro, viññāṇāhāro = " + cap(nlist([AHARA[k] for k in (
              "kabaḷīkārāhāro", "phassāhāro", "manosañcetanāhāro", "viññāṇāhāro")])),
          "[kabaḷiṃkāro āhāro (sī. syā.)] = " + FOOD_VAR2,
          "Cakkhusamphasso … manoviññāṇadhātusamphasso = " + cap(nlist([PH[k] for k in (
              "cakkhu", "sota", "ghāna", "jivhā", "kāya", "manodhātu", "manoviññāṇadhātu")])),
          "Cakkhuviññāṇaṃ … kāyaviññāṇaṃ, manodhātu, manoviññāṇadhātu (satta cittāni) = " + cap(nlist(
              [K1.VINN[k] for k in ("cakkhu", "sota", "ghāna", "jivhā", "kāya")] + [DH["mano"], DH["manoviññāṇa"]])),
          "", "## Rebirth (Dhammadassanavāra)", "",
          "upapattikkhaṇe = " + MOMENT + "; sabbesaṃ = " + ALL + "; kassaci = " + SOME + "; aparāni / aparā = " + OTHER,
          "pātubhavanti / pātubhavati = появляются / появляется",
          "Kāmadhātuyā upapattikkhaṇe kati khandhā pātubhavanti…? = В мире чувственных желаний в момент перерождения "
          "сколько совокупностей появляется…?",
          "Kāmadhātuyā upapattikkhaṇe kassa N X pātubhavanti? = У кого в мире чувственных желаний в момент перерождения "
          "появляются N X?",
          "<beings> upapattikkhaṇe N X pātubhavanti – … = У <beings>, … в момент перерождения появляются N X – …",
          "Kāmadhātuyā upapattikkhaṇe etesaṃ imāni N X pātubhavanti. = У них в мире чувственных желаний в момент "
          "перерождения появляются эти N X.",
          "Kāmadhātuyā upapattikkhaṇe sabbesaṃ katame N X pātubhavanti? … – … sabbesaṃ ime N X pātubhavanti. = Какие N X "
          "появляются в мире чувственных желаний в момент перерождения у всех? … – в мире чувственных желаний в момент "
          "перерождения у всех появляются эти N X.",
          "kassaci / avasesānaṃ sattānaṃ ahetukā pātubhavanti = у некоторых / у остальных существ " + ROOTLESS,
          "ṭhapetvā asaññasattānaṃ devānaṃ = " + EXCEPT_ASANNA,
          "Asaññasattā devā ahetukā anāhārā aphassakā avedanakā asaññakā acetanakā acittakā pātubhavanti = Боги без "
          "восприятия появляются без корней, без питания, без контакта, без чувства, без восприятия, без намерения, "
          "без ума",
          ]
    L += [f"{k} = {v}" for k, v in BEINGS.items()]
    L += ["", "## Planes, gods, lifespans", "",
          "Heṭṭhato X pariyantaṃ karitvā, uparito Y antokaritvā, yaṃ etasmiṃ antare etthāvacarā ettha pariyāpannā = "
          + REALM_FRAME + " (ch. 3)",
          "sammutidevā, upapattidevā, visuddhidevā = условные боги, боги по рождению, боги по чистоте "
          "(upapattidevā per APPROVED.md)",
          "appekacce X sahabyataṃ upapajjanti = " + SOME_REBORN + " X(gen)",
          "X kittakaṃ āyuppamāṇaṃ? = " + HOW_LONG + " X(gen)?; Tesaṃ kittakaṃ āyuppamāṇaṃ? = " + HOW_LONG_THEM,
          "Yāni mānusakāni N vassāni, X eso eko rattindivo = N человеческих лет " + DAY + " X(gen)",
          "Tāya rattiyā tiṃsa rattiyo māso. = " + MONTH,
          "Tena māsena dvādasamāsiyo saṃvaccharo. = " + YEAR,
          "Tena saṃvaccharena dibbāni N vassasatāni X āyuppamāṇaṃ. = N таких божественных лет составляют "
          "продолжительность жизни X(gen).",
          "Manussānaṃ gaṇanāya kittakaṃ hoti? = " + HUMAN_COUNT,
          "N vassakoṭiyo M vassasatasahassāni = the sum in millions / billions (koṭi «миллионы» ×10, termbase "
          "aṭṭhavīsañca koṭiyo = двести восемьдесят миллионов), e.g. Tisso ca vassakoṭiyo saṭṭhi ca "
          "vassasatasahassāni = Тридцать шесть миллионов лет",
          "Paṭhamaṃ jhānaṃ parittaṃ / majjhimaṃ / paṇītaṃ bhāvetvā = развив ограниченное / среднее / высшее первое "
          "медитативное погружение",
          ]
    L += [f"{k} (devānaṃ) = {v}" for k, v in GODS.items()]
    L += ["", "## Question-type sections", "",
          "Pañcannaṃ khandhānaṃ … sattannaṃ cittānaṃ kati X? = Сколько из пяти совокупностей … сколько из семи видов "
          "ума X?",
          "kāmadhātupariyāpanno / na … / pariyāpanno / apariyāpanno = принадлежит (-ат) к миру чувственных желаний / "
          "не принадлежит … / принадлежит к кругам существования / не принадлежит к кругам существования",
          "abhiññeyyo pariññeyyo na pahātabbo na bhāvetabbo na sacchikātabbo = (acc.) следует постичь высшим знанием "
          "и полностью понять, не следует ни устранять, ни развивать, ни осуществлять",
          "siyā pahātabbo / bhāvetabbo / sacchikātabbo = иногда следует устранить / развивать / осуществить; "
          "na X, na Y (with commas) = не следует X, не следует Y",
          "sārammaṇo / anārammaṇo / sārammaṇārammaṇo / anārammaṇārammaṇo = " + " / ".join(x[1] for x in OBJ[::-1]),
          "diṭṭho, suto, muto, viññāto = является увиденным (-ой), услышанным, ощущённым, познанным; na diṭṭho na "
          "suto na muto, viññāto = не является ни увиденным, ни услышанным, ни ощущённым, но является познанным",
          "na vattabbo X-tipi, Y-tipi (no dash, no quotes) = нельзя определить ни как «X», ни как «Y» (ch. 7-9)",
          "", "## Closing", "",
          "Abhiññā dve sārammaṇā, diṭṭhā kusalavedanā; = " + SUMMARY[0],
          "Vipākā ca upādinnā, vitakkaṃ rūpalokiyāti. = " + SUMMARY[1],
          "Vibhaṅgapakaraṇaṃ niṭṭhitaṃ. = " + DONE_LINES[1],
          ]
    return "\n".join(L) + "\n"


def main():
    install()
    check_reuse()
    pali, h = build()
    (S.OUT / PART).write_text(K23.render(pali, h), encoding="utf-8", newline="\n")
    NOTES_PATH.write_text(notes_md(), encoding="utf-8", newline="\n")
    for s in SLIPS + K23.SLIPS + K1.SLIPS + K45.SLIPS:
        print("SLIP:", s)


if __name__ == "__main__":
    main()
