"""Consistency (harmonise) pass for the pi-1 Russian plain zero-shot.

Applies fixed old -> new strings (a few regex patterns, marked rx=True, replacement may be a callable) to the
Russian part files. A rule touches a Russian line ONLY when the aligned Pāli line (non-empty line i <-> non-empty
line i) matches the rule's Pāli pattern, and only in the parts listed for it. Line counts, block IDs, heading
levels, dashes and variant brackets are never touched (asserted per changed line).
Protected (user-approved, never changed): preamble, 1-matika, the first 122 non-empty lines of 2-01.
Backup of the pre-pass files: backup-pre-harmonise/. Log: harmonise-log.tsv (rule, part, line, old, new).
The pass always reads from the backup, so it is idempotent: rerunning it rebuilds the same output.
Strings copied from a winning part (COPY_* constants) are read from the backup at start-up, so they are fixed.

usage: python -I -X utf8 harmonise_ru.py [--dry]
"""
import os, re, sys, collections

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
PDIR = os.path.join(ROOT, r"AI_translation\pali\pi-1_split_chapters")
RDIR = os.path.join(ROOT, r"AI_translation\russian\pi-1-russian-plain-zeroshot_split_chapters")
HERE = os.path.join(ROOT, r"0-INBOX\temp\pipeline\pi-1-ru")
BAK = os.path.join(HERE, "backup-pre-harmonise")
PARTS = ["preamble", "1-matika", "2-01-cittuppadakandam", "2-02-cittuppadakandam", "2-03-cittuppadakandam",
         "2-04-cittuppadakandam", "2-05-cittuppadakandam", "3-01-rupakandam", "3-02-rupakandam", "3-03-rupakandam",
         "4-01-nikkhepakandam", "4-02-nikkhepakandam", "4-03-nikkhepakandam", "5-atthakathakandam"]
PROTECTED_PARTS = {"preamble", "1-matika"}
PROTECTED_2_01 = 122  # first 122 non-empty lines of 2-01 = approved sample
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")

R = []  # (id, pali_regex, old, new, is_regex, parts_prefixes or None)


def rule(rid, pali, old, new, rx=False, parts=None):
    R.append((rid, pali, old, new, rx, parts))


# ------------------------------------------------------------------ backup reader (for COPY constants)
def _bak_segments(part):
    p = [l for l in open(os.path.join(PDIR, part + ".md"), encoding="utf-8-sig").read().splitlines() if l.strip()]
    r = [l for l in open(os.path.join(BAK, part + ".md"), encoding="utf-8").read().splitlines() if l.strip()]
    segs, bp, br = {}, [], []
    for a, b in zip(p, r):
        bp.append(a); br.append(b)
        m = ID.search(a)
        if m:
            segs[m.group(1)] = (bp, br); bp, br = [], []
    return segs


_SEGS = {}


def bak_line(part, sid, i=-1):
    if part not in _SEGS:
        _SEGS[part] = _bak_segments(part)
    return _SEGS[part][sid][1][i]


def between(s, a, b):
    i = s.index(a) + len(a)
    return s[i:s.index(b, i)]


P4_01, P4_02, P4_03, P5 = "4-01-nikkhepakandam", "4-02-nikkhepakandam", "4-03-nikkhepakandam", "5-atthakathakandam"

# =============================================================== 1. jhāna formula and frame (2-01/2-02 wording)
ORD_GEN = {"первого": "первое", "второго": "второе", "третьего": "третье", "четвёртого": "четвёртое", "пятого": "пятое"}
_ORD = "|".join(ORD_GEN)
_ENTER = re.compile(rf"достигает ({_ORD}) медитативного погружения и пребывает в нём")
_RUN_END = re.compile(rf", в это время|…(?= (?:{_ORD}|{'|'.join(ORD_GEN.values())}) медитативн)|; |$")
_ADJ = [("свободном от устремлений", "свободное от устремлений"), ("не имеющем признаков", "не имеющее признаков"),
        ("пустом", "пустое")]


def _enter(s):
    """«достигает N-го погружения и пребывает в нём, в погружении Q» -> «входит в N-е погружение, Q, и пребывает в нём»"""
    out = ""
    while True:
        m = _ENTER.search(s)
        if not m:
            return out + s
        tail = s[m.end():]
        e = _RUN_END.search(tail)
        run = tail[:e.start()]
        if run.startswith(", "):
            run = run[2:]
        assert not run or run.startswith("в "), run
        run = re.sub(r"^в пустом погружении", "пустом", run)
        run = re.sub(r"^в погружении,? ", "", run)
        for a, b in _ADJ:
            run = run.replace(a, b)
        new = f"входит в {ORD_GEN[m.group(1)]} медитативное погружение" + (f", {run}," if run else "") + " и пребывает в нём"
        out += s[:m.start()] + new
        s = tail[e.start():]


def jhana(s):
    for a, b in [("человек развивает ", "человек, развивая "),
                 ("… развивает надмирск", "… развивая надмирск"),
                 (" и, отстранившись от чувственных удовольствий", ", полностью уединившись от чувственных удовольствий"),
                 ("человек, отстранившись от чувственных удовольствий", "человек, полностью уединившись от чувственных удовольствий"),
                 (" и с успокоением направленной мысли и удержания мысли", ", с затиханием направленной мысли и удержания мысли"),
                 (", и с устранением приятного", ", с устранением приятного")]:
        s = s.replace(a, b)
    s = _enter(s)
    s = re.sub(rf"(?<=… )({_ORD}) медитативного погружения", lambda m: ORD_GEN[m.group(1)] + " медитативное погружение", s)
    assert "отстранившись" not in s and "успокоением направленной" not in s and "достигает" not in s, s
    return s


rule("D1-jhana-frame", r"bhāveti|vivicceva kāmehi|vūpasamā|upasampajja", r"^.*$", lambda m: jhana(m.group(0)), rx=True,
     parts=["2-03", "2-05"])

# counting line items (2-01/2-02/2-04: «пятичастное медитативное погружение», «…частный путь»)
rule("D1-count", r"pañcaṅgikaṃ jhānaṃ hoti", "есть медитативное погружение из пяти факторов",
     "есть пятичастное медитативное погружение", parts=["2-03", "2-05"])
rule("D1-count", r"aṭṭhaṅgiko maggo hoti", "есть путь из восьми факторов", "есть восьмичастный путь", parts=["2-03", "2-05"])

# 2. paṭipadā / abhiññā (2-01/2-02)
rule("D2-patipada", r"paṭipad", "с болезненным способом практики", "с трудным способом практики", parts=["2-03", "2-05"])
rule("D2-patipada", r"paṭipad", "с приятным способом практики", "с лёгким способом практики", parts=["2-03", "2-05"])

# 3. vīmaṃsā = пытливость (2-01/2-02), distinct from vicaya = исследование
rule("D3-vimamsa", r"vīmaṃsādhipateyy", "при преобладании исследования", "при преобладании пытливости", parts=["2-03", "2-05"])
rule("D3-vimamsa", r"vīmaṃsādhipateyyaṃ maggaṃ", "в котором преобладает исследование, за исключением исследования",
     "в котором преобладает пытливость, за исключением пытливости", parts=["4-01"])

# 5. asāta = безотрадный (the approved sample has neither form): «ни отрадно, ни безотрадно»
rule("D5-asata", r"nāsātaṃ", "ни отрадно, ни неотрадно", "ни отрадно, ни безотрадно")

# 6. viññatti = внешнее выражение (3-01/3-02/3-03, pi-5)
for a, b in [("телесное сообщение", "телесное внешнее выражение"), ("речевое сообщение", "речевое внешнее выражение")]:
    rule("D6-vinnatti", r"viññatt", a, b, parts=["5-"])
for a, b in [("телесное выражение", "телесное внешнее выражение"), ("речевое выражение", "речевое внешнее выражение")]:
    rule("D6-vinnatti", r"viññatt", a, b, parts=["4-02", "4-03"])

# 7. upacaya = рост (ch3), santati = непрерывность
rule("D7-upacaya", r"rūpassa upacayo", "нарастание материальной формы", "рост материальной формы", parts=["5-"])
rule("D7-upacaya", r"rūpassa upacayo", "накопление материальной формы", "рост материальной формы", parts=["4-02"])

# 8. diṭṭhigata(sampayutta) = (связанный с) приверженностью воззрениям (2-04)
rule("D8-ditthigata", r"diṭṭhigata(?:sampayutt|vippayutt)", "с ложным воззрением", "с приверженностью воззрениям", parts=["5-"])

# 9. patiṭṭhāho = закрепление (as written; 2-04 ^1-381); paṭiggāho keeps «цепкость»
rule("D9-patitthaho", r"gāho patiṭṭhāho", "хватка, цепкость,", "хватка, закрепление,", parts=["4-01", "4-02", "4-03"])

# 10. kammassa katattā = вследствие совершённых действий (ch3, 50 lines), in the 4-01 «которая возникла …» frame
KAT = "вследствие совершённых действий"
rule("D10-katatta", r"kammassa katattā", "вследствие совершённого действия", KAT, parts=["4-01"])
rule("D10-katatta", r"kammassa katattā", "которая возникла не оттого, что было совершено действие",
     f"которая возникла не {KAT}", parts=["4-02"])
rule("D10-katatta", r"kammassa katattā", "которая возникла оттого, что было совершено действие",
     f"которая возникла {KAT}", parts=["4-02"])
rule("D10-katatta", r"kammassa katattā", "которая не является следствием совершённых действий",
     f"которая возникла не {KAT}", parts=["5-"])
rule("D10-katatta", r"kammassa katattā", "которая является следствием совершённых действий",
     f"которая возникла {KAT}", parts=["5-"])

# 12. typo: missing space after «сферы»
rule("D12-typo", r"āyatana", r"сферы(?=[а-яё])", "сферы ", rx=True)

# 13. sārāga beside rāga = пристрастие (4-01); the whole lobha string follows 4-01 (rule B1)
# 14. bahūsu siglum = (во многих изданиях): already uniform (2-02, 4-01); no rule needed.

# =============================================================== 15. other divergences
# B1 lobha string (4-01 wins; 4-02 matches no earlier book where they differ). Exception kept from 4-02 (brief 16):
#    the two senses of rūpataṇhā, which also replace 4-01's «жажда бесформенного».
LOBHA_41 = between(bak_line(P4_01, "1-1141"), "То, что есть ", ", – это называется")
LOBHA_42 = between(bak_line(P4_02, "1-1236"), "То, что есть ", ", – это называется")
rule("B1-lobha", r"rāgo sārāgo", LOBHA_42, LOBHA_41, parts=["4-02"])
rule("B1-lobha-tanha", r"rūpataṇhā arūpataṇhā nirodhataṇhā rūpataṇhā",
     "жажда форм, жажда бесформенного, жажда прекращения, жажда форм,",
     "жажда существования в мире форм, жажда существования в мире без форм, жажда прекращения, жажда видимых форм,",
     parts=["4-01", "4-02"])

# B2 dosa intro and string (4-01; dussanā = проявление злобы as 2-04 and the approved sample's adosa string)
DOSA_41 = between(bak_line(P4_01, "1-1066"), "? ", ", – это называется")
DOSA_42 = between(bak_line(P4_02, "1-1237"), "? ", ", – это называется")
rule("B2-dosa", r"āghāto jāyati", DOSA_42, DOSA_41, parts=["4-02"])
_D42_SEMI = DOSA_42.replace("«Он причиняет мне вред», негодование", "«Он причиняет мне вред»; негодование").replace(
    "«Он причинит мне вред», негодование", "«Он причинит мне вред»; негодование")
_D41_SEMI = DOSA_41.replace("«Он причиняет мне вред» возникает досада, при", "«Он причиняет мне вред» возникает досада; при").replace(
    "«Он причинит мне вред» возникает досада, при", "«Он причинит мне вред» возникает досада; при")
rule("B2-dosa", r"caratīti āghāto jāyati;", _D42_SEMI, _D41_SEMI, parts=["4-02"])

# B3 kaṅkhā string (4-01; vimati = неуверенность as pi-5)
KANKHA_41 = between(bak_line(P4_01, "1-1008"), "То, что есть такое ", ", – это называется")
for prt, sid, a in [("2-04-cittuppadakandam", "1-425", "То, что в это время есть "), (P4_02, "1-1167", "То, что есть такое ")]:
    _old = between(bak_line(prt, sid, 0 if prt.startswith("2-04") else -1), a, ", – ")
    rule("B3-kankha", r"kaṅkhā kaṅkhāyanā", _old, KANKHA_41, parts=[prt[:4]])

# B4 uddhacca string (2-04; avūpasamo = отсутствие затихания, after vūpasama = затихание, decision 1)
rule("B4-uddhacca", r"uddhaccaṃ avūpasamo", "беспокойство ума, неумиротворённость, отвлечение ума, смятение ума",
     "беспокойство ума, отсутствие затихания, отвлечение ума, взбудораженность ума", parts=["4-02"])

# B5 diṭṭhi string (4-01/4-02 = pi-4 ^4-62): diṭṭhivisūkāyika = извращённость воззрений, abhinivesa = приверженность
rule("B5-ditthi", r"diṭṭhivisūkāyikaṃ", "изворотливость воззрений", "извращённость воззрений", parts=["2-04"])
rule("B5-ditthi", r"abhiniveso", r"(хватка, закрепление(?: \[[^\]]*\])?), упрямство,", r"\1, приверженность,", rx=True,
     parts=["2-04"])

# B6 kāma string (4-01, matching its lobha string: sineho = приязнь, mucchā = одурманенность)
rule("B6-kama", r"Yo kāmesu", "чувственная привязанность, чувственный жар, чувственное опьянение",
     "чувственная приязнь, чувственный жар, чувственная одурманенность", parts=["4-02"])
# bhava string: «в отношении видов существования» (4-01)
rule("B6-bhava", r"Yo bhavesu", "То, что в отношении существования есть", "То, что в отношении видов существования есть",
     parts=["4-03"])

# B7 māna string (4-01)
rule("B7-mana", r"Seyyohamasmīti",
     "Самомнение «я лучше», самомнение «я равен», самомнение «я хуже»; то, что есть такое самомнение, мнение о себе, "
     "состояние мнения о себе, возвышение, превознесение, знамя, самовозвеличивание, желание ума выставлять себя напоказ",
     "Самомнение «Я лучше других», самомнение «Я равен другим», самомнение «Я хуже других»; то, что есть такое самомнение, "
     "зазнайство, состояние зазнайства, превознесение, надменность, знамя, возвеличивание себя, желание ума поднять свой стяг",
     parts=["4-02"])

# B8 sakkāyadiṭṭhi body (4-01)
rule("B8-sakkaya", r"assutavā puthujjano",
     "Вот необученный обычный человек, который не видит благородных, не сведущ в учении благородных и не дисциплинирован "
     "в учении благородных, не видит достойных людей, не сведущ в учении достойных людей и не дисциплинирован в учении "
     "достойных людей, рассматривает материальную форму как самость, или самость как обладающую материальной формой, "
     "или материальную форму в самости, или самость в материальной форме.",
     between(bak_line(P4_01, "1-1007"), "? ", " Считает чувство"), parts=["4-02"])
rule("B8-sakkaya", r"assutavā puthujjano",
     "сознание он рассматривает как самость, или самость как обладающую сознанием, или сознание в самости, или самость в сознании.",
     "сознание он считает самостью, или самость обладающей сознанием, или сознание находящимся в самости, или самость "
     "находящейся в сознании.", parts=["4-02"])

# B9 sīlabbata body (4-01)
rule("B9-silabbata", r"sīlena suddhi",
     "Отшельники и брахманы за пределами этого Учения считают: «Очищение достигается обрядами, очищение достигается "
     "обетами, очищение достигается обрядами и обетами»",
     "Отшельники и брахманы вне этого Учения считают: «Чистота достигается обрядами, чистота достигается обетами, "
     "чистота достигается обрядами и обетами»", parts=["4-02"])

# B10 the ten views: sarīra = плоть (4-02 = pi-5), capitals of 4-01
rule("B10-views", r"taṃ jīvaṃ taṃ sarīraṃ|taṃ jīvaṃ taṃ sarīranti", "«Душа и тело одно и то же", "«Душа то же самое, что плоть",
     parts=["4-01"])
rule("B10-views", r"aññaṃ jīvaṃ aññaṃ sarīr", "«Душа одно, а тело другое", "«Душа одно, а плоть другое", parts=["4-01"])
rule("B10-views", r"sassato loko", r"или «(мир|душа)", lambda m: "или «" + m.group(1).capitalize(), rx=True,
     parts=["4-02", "4-03"])

# B11 counted group nouns (4-01): «три вида оков», «десять видов оков» (оковы has no singular)
rule("B11-count", r"[Tt]īṇi saṃyojanāni", "Три оковы", "Три вида оков", parts=["4-02"])
rule("B11-count", r"[Tt]īṇi saṃyojanāni", "Эти три оковы", "Эти три вида оков", parts=["4-02"])
rule("B11-count", r"Dasa saṃyojanāni", "Десять оков", "Десять видов оков", parts=["5-"])
rule("B11-count", r"Dasa kilesavatthūni", "Десять оснований", "Десять основ", parts=["5-"])

# B12 «Те же самые X являются …» (4-01/4-02)
rule("B12-teva", r"^(?:Katame[^?]*\? )?(?:Tāneva|Teyeva|Teva|Sveva) ", r"(?<=\? )Эти же ", "Те же самые ", rx=True,
     parts=["5-"])

# B13 āsava list: diṭṭhāsava = влечение воззрений (4-01)
rule("B13-asava", r"diṭṭhāsav", "влечение к воззрениям", "влечение воззрений", parts=["5-"])
# attavādupādāna = цепляние за учение о самости (4-02; attā = самость, pi-4)
rule("B13-upadana", r"attavādupādān", "учение о «я»", "учение о самости", parts=["5-"])

# B14 Cittaṃ na vattabbaṃ – ch5 frame (36 lines)
for a, b in [("Об уме не следует говорить – ни что он «связан с умом», ни что он «не связан с умом»",
              "Ум нельзя определить – ни как связанный с умом, ни как не связанный с умом"),
             ("Об уме не следует говорить – ни что он «соединён с умом», ни что он «не соединён с умом»",
              "Ум нельзя определить – ни как соединённый с умом, ни как не соединённый с умом")]:
    rule("B14-vattabba", r"Cittaṃ na vattabbaṃ", a, b, parts=["4-02"])

# B15 kabaḷīkāro āhāro = съедаемая пища (ch3, 4-02, pi-5)
rule("B15-kabalikara", r"kabaḷīkār", "пища, съедаемая кусками,", "съедаемая пища", parts=["5-"])

# B16 asekkhā: Upariṭṭhimaṃ arahattaphalaṃ = Высший плод состояния архата (4-01)
rule("B16-asekkha", r"Upariṭṭhimaṃ arahattaphalaṃ", "Высший плод, плод состояния архата", "Высший плод состояния архата",
     parts=["5-"])

# B17 na kāmāvacarā / na rūpāvacarā / na arūpāvacarā lists: 4-02 (mirrors the Pāli commas)
for sid in ["1-1288", "1-1290", "1-1292"]:
    _new = between(bak_line(P4_02, sid), "? ", " – это явления")
    _sid5 = {"1-1288": "1-1602", "1-1290": "1-1604", "1-1292": "1-1606"}[sid]
    _old = between(bak_line(P5, _sid5), "? ", " – это явления")
    rule("B17-na-avacara", r"^Katame dhammā na \w*āvacarā\? \w+āvacarā, \w+āvacarā, apariyāpannā", _old, _new, parts=["5-"])

# B18 sphere lists after a noun: 4-01 («…, к миру форм и к миру без форм»; «…, к миру без форм и не принадлежащие …»)
rule("B18-spheres", r"āvacarā", "к миру форм или к миру без форм, а также не принадлежащие",
     "к миру форм, к миру без форм и не принадлежащие", parts=["4-02", "4-03"])
rule("B18-spheres", r"āvacarā", "к миру форм или к миру без форм", "к миру форм и к миру без форм", parts=["4-02", "4-03"])

# B19 tadekaṭṭhā ca kilesā / taṃsampayutto … / taṃsamuṭṭhānaṃ … (4-01 wording; vacīkamma = речевое действие, pi-5)
rule("B19-tadekattha", r"tadekaṭṭhā ca kilesā", "; пребывающие вместе с ними омрачения,", "; и омрачения, пребывающие вместе с ними,",
     parts=["4-02", "4-03"])
rule("B19-tadekattha", r"tadekaṭṭhā ca kilesā", ", пребывающие вместе с ними омрачения,", ", и омрачения, пребывающие вместе с ними,",
     parts=["4-02", "4-03"])
rule("B19-tadekattha", r"Tadekaṭṭhā ca kilesā", ". Пребывающие вместе с ними омрачения,", ". И омрачения, пребывающие вместе с ними,",
     parts=["4-02", "4-03"])
rule("B19-tadekattha", r"Tadekaṭṭho lobho", "Пребывающие вместе с ними жадность, злоба, заблуждение – это корни,",
     "Жадность, злоба, заблуждение, пребывающие вместе с ними, – это явления, являющиеся корнями,", parts=["4-02", "4-03"])
rule("B19-hetu", r"pahātabbahetū", r"– это корни, устраняемые (видением истины|развитием ума)",
     r"– это явления, являющиеся корнями, устраняемыми \1", rx=True, parts=["4-02", "4-03"])
rule("B19-tamsampayutta", r"taṃsampayutt", r"связанная с (ними|ним|ней) совокупность", r"связанные с \1 совокупность", rx=True,
     parts=["4-02", "4-03"])
rule("B19-vacikamma", r"vacīkamm", "словесное действие", "речевое действие", parts=["4-01"])

# B20 'Tehi dhammehi ye dhammā …' frames (4-01)
T = r"Tehi dhammehi ye dhammā"
for pal, a, b in [
    (T + r" sampayuttā(?!,? te dhamme)", "Явления, связанные с этими явлениями:", "Явления, которые связаны с этими явлениями:"),
    (T + r" vippayuttā(?! sāsavā)", "Явления, не связанные с этими явлениями:", "Явления, которые не связаны с этими явлениями:"),
    (T + r" vippayuttā sāsavā", "Явления, не связанные с этими явлениями: подверженные влечениям",
     "Не связанные с этими явлениями подверженные влечениям"),
    (T + r" sampayuttā,? te dhamme", "Из явлений, связанных с этими явлениями, за исключением этих явлений:",
     "Среди явлений, которые связаны с этими явлениями, за исключением этих явлений,"),
    (T + r" nīvaraṇiyā", "Из явлений, подверженных этим явлениям,", "Среди явлений, которые подвержены этим явлениям,"),
    (T + r" parāmaṭṭhā", "Из явлений, затронутых этими явлениями,", "Среди явлений, которые затронуты этими явлениями,"),
    (T + r" upādāniyā", "Из явлений, служащих объектом цепляния для этих явлений,",
     "Среди явлений, которые служат объектом цепляния для этих явлений,"),
    (T + r" saṃkilesikā", "Из явлений, подверженных омрачению этими явлениями,",
     "Среди явлений, которые подвержены омрачению этими явлениями,"),
    (T + r" saṃkiliṭṭhā", "Из явлений, омрачённых этими явлениями, за исключением этих явлений:",
     "Среди явлений, которые омрачены этими явлениями, за исключением этих явлений,"),
]:
    rule("B20-tehi", pal, a, b, parts=["4-02", "4-03"])

# B22 X-bhūmiyaṃ kāmāvacare rūpāvacare (arūpāvacare) apariyāpanne (4-01 wording)
rule("B22-bhumi", r"bhūmiyaṃ kāmāvacare",
     ", относящемся к миру чувственных желаний, к миру форм, к миру без форм или не принадлежащем к кругам существования",
     " в мире чувственных желаний, в мире форм, в мире без форм и в том, что не принадлежит к кругам существования",
     parts=["4-02", "4-03"])
rule("B22-bhumi", r"bhūmiyaṃ kāmāvacare",
     ", относящемся к миру чувственных желаний, к миру форм или не принадлежащем к кругам существования",
     " в мире чувственных желаний, в мире форм и в том, что не принадлежит к кругам существования",
     parts=["4-02", "4-03"])

# B23 sabbañca rūpaṃ, asaṅkhatā ca dhātu = и вся материальная форма, и необусловленный элемент (4-01)
rule("B23-sabbanca", r"sabbañca rūpaṃ,? asaṅkhatā ca dhātu", "вся материальная форма и необусловленный элемент",
     "и вся материальная форма, и необусловленный элемент", parts=["4-02", "4-03"])

# B24 ye ca dhammā kiriyā neva kusalā nākusalā na ca kammavipākā (4-01)
rule("B24-kiriya", r"ye ca dhammā kiriyā",
     "и те явления, которые являются функциональными, не являются ни благими, ни неблагими, ни результатами действий",
     "и те функциональные явления, которые не являются ни благими, ни неблагими, ни результатами действий", parts=["4-02"])
rule("B24-kiriya", r"ye ca dhammā kiriyā",
     "и те явления, которые являются функциональными, не являются ни благими, ни неблагими и не являются результатами действий",
     "и те функциональные явления, которые не являются ни благими, ни неблагими, ни результатами действий", parts=["3-01"])

# B25 Apariyāpannā maggā ca, maggaphalāni ca, asaṅkhatā ca dhātu (4-01)
rule("B25-magga", r"[Aa]pariyāpannā maggā ca", "Не принадлежащие к кругам существования пути, плоды путей",
     "Пути, не принадлежащие к кругам существования, плоды путей", parts=["4-02", "4-03"])
rule("B25-magga", r"[Aa]pariyāpannā maggā ca", "не принадлежащие к кругам существования пути, плоды путей",
     "пути, не принадлежащие к кругам существования, плоды путей", parts=["4-02", "4-03"])

# B21 ṭhapetvā = кроме (pi-5 termbase; 2-01 … 2-05)
rule("B21-thapetva", r"ṭhapetvā|Ṭhapetvā", "за исключением", "кроме", parts=["4-01", "4-02", "4-03", "5-"])
rule("B21-thapetva", r"ṭhapetvā|Ṭhapetvā", "За исключением", "Кроме", parts=["4-01", "4-02", "4-03", "5-"])


# ------------------------------------------------------------------------------------------------- engine
def dashes(t):
    return t.count("—") + t.count("–")


def main(dry=False):
    log = []
    tot = collections.Counter()
    changed = collections.Counter()
    hit = set()
    blocked = []
    comp = [(rid, re.compile(p), old, new, rx, parts) for rid, p, old, new, rx, parts in R]
    for part in PARTS:
        pl = [l for l in open(os.path.join(PDIR, part + ".md"), encoding="utf-8-sig").read().splitlines() if l.strip()]
        text = open(os.path.join(BAK, part + ".md"), encoding="utf-8").read()
        assert "\r" not in text and not text.startswith("\ufeff"), part
        el = text.split("\n")
        idx = [i for i, l in enumerate(el) if l.strip()]
        assert len(idx) == len(pl), (part, len(idx), len(pl))
        sid_of = {}
        cur = []
        for k, li in enumerate(idx):
            cur.append(k)
            m = ID.search(pl[k])
            if m:
                for kk in cur:
                    sid_of[kk] = m.group(1)
                cur = []
        for k, li in enumerate(idx):
            p, e0 = pl[k], el[li]
            e = e0
            for ri, (rid, pr, old, new, rx, parts) in enumerate(comp):
                if parts and not any(part.startswith(x) for x in parts):
                    continue
                if not pr.search(p):
                    continue
                if rx:
                    e2, n = re.subn(old, new, e)
                    if e2 == e:
                        n = 0
                else:
                    n = e.count(old)
                    e2 = e.replace(old, new)
                if n:
                    hit.add(ri)
                    if part in PROTECTED_PARTS or (part.startswith("2-01") and k < PROTECTED_2_01):
                        blocked.append((rid, part, k))
                        continue
                    log.append((rid, part, sid_of.get(k, "?"), k + 1, e, e2))
                    tot[(rid, part)] += n
                    e = e2
            if e != e0:
                assert dashes(e) == dashes(e0), (part, k, "dash count changed", e)
                assert ID.findall(e) == ID.findall(e0), (part, k, "block id")
                assert re.match(r"#*", e).group(0) == re.match(r"#*", e0).group(0), (part, k, "heading")
                assert re.findall(r"\[[^\]]*\]", e) == re.findall(r"\[[^\]]*\]", e0), (part, k, "brackets")
                assert "—" not in e and ":-" not in e, (part, k)
                el[li] = e
                changed[part] += 1
        if not dry:
            open(os.path.join(RDIR, part + ".md"), "w", encoding="utf-8", newline="\n").write("\n".join(el))
    if not dry:
        with open(os.path.join(HERE, "harmonise-log.tsv"), "w", encoding="utf-8", newline="\n") as f:
            f.write("rule\tpart\tsegment\tline\told\tnew\n")
            for rid, part, sid, ln, old, new in log:
                f.write(f"{rid}\t{part}\t^{sid}\t{ln}\t{old}\t{new}\n")
    per = collections.defaultdict(dict)
    for (rid, part), n in tot.items():
        per[rid][part[:4]] = n
    for rid in sorted(per):
        print(f"{rid:22s} " + ", ".join(f"{p}={n}" for p, n in sorted(per[rid].items())))
    print("lines changed per part:", dict(changed), "total", sum(changed.values()))
    if blocked:
        print("BLOCKED (protected lines a rule would have changed):", blocked)
    for ri, r in enumerate(R):
        if ri not in hit:
            print("NO HIT:", r[0], "|", str(r[2])[:90])


if __name__ == "__main__":
    main(dry="--dry" in sys.argv)
