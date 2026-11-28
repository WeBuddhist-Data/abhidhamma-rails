"""Russian plain zero-shot of pi-6 (Yamaka): SAMPLE builder (preamble + 1-mulayamaka.md).

Run:    python -I -X utf8 -B 0-INBOX\\temp\\pipeline\\pi-6-ru\\build_sample_ru.py
Import: from build_sample_ru import *   (importing never writes any file; only __main__ builds)

Other chapter agents copy the fixed formula strings below verbatim:
  - book frame (NAMO, ABHIDHAMMAPITAKE, BOOK_TITLE, YAMAKA_TITLES, closings),
  - labels (LETTERS: (Ka) (Kha) ... -> (а) (б) ...),
  - section-heading words (UDDESO, NIDDESO, VARO, NAYA, SECTION_HEADINGS),
  - pair-question frames (KA_FRAME*, KHA_FRAME*),
  - answers (AMANTA) and partial-answer frames (TINEVA_FRAME, AVASESA_NA_FRAME, AHETUKA_FRAME,
    SAMUTTHANA_FRAME, MULANI_FRAME),
  - the per-line checks (check_pair) and the cross-book assert (check_crossbook).
"""
import pathlib
import re
import sys
import unicodedata

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
PALI_DIR = ROOT / "AI_translation" / "pali" / "pi-6_split_chapters"
OUT_DIR = ROOT / "AI_translation" / "russian" / "pi-6-russian-plain-zeroshot_split_chapters"
RAILS = {b: ROOT / "AI_translation" / "russian" / f"pi-{b}-russian-plain-rails_split_chapters" for b in "12345"}

# ---------------------------------------------------------------------------------------------
# Labels. (Ka) (Kha) ... follow the Pāli alphabet; Russian letters in alphabet order without
# ё, й, ъ, ы, ь (as in pi-2: (Ṅa) = (д), (Ca) = (е), (Cha) = (ж), (Ja) = (з)).
# ---------------------------------------------------------------------------------------------
PALI_LETTERS = ["Ka", "Kha", "Ga", "Gha", "Ṅa", "Ca", "Cha", "Ja", "Jha", "Ña", "Ṭa", "Ṭha", "Ḍa",
                "Ḍha", "Ṇa", "Ta", "Tha", "Da", "Dha", "Na", "Pa", "Pha", "Ba", "Bha", "Ma", "Ya",
                "Ra", "La"]
RU_LETTERS = list("абвгдежзиклмнопрстуфхцчшщэюя")
LETTERS = dict(zip(PALI_LETTERS, RU_LETTERS))

# ---------------------------------------------------------------------------------------------
# Book frame
# ---------------------------------------------------------------------------------------------
NAMO = "Почтение Благословенному, Достойному, Полностью Пробуждённому Будде"   # pi-1..5
ABHIDHAMMAPITAKE = "В корзине Абхидхаммы"                                      # pi-1..5
BOOK_TITLE = "Парные вопросы"                                                  # Yamakapāḷi (user-approved)

YAMAKA_TITLES = {                      # ### headings of the ten yamakas (user-approved)
    "Mūlayamakaṃ": "Парные вопросы о корнях",
    "Khandhayamakaṃ": "Парные вопросы о совокупностях",
    "Āyatanayamakaṃ": "Парные вопросы о сферах восприятия",
    "Dhātuyamakaṃ": "Парные вопросы об элементах",
    "Saccayamakaṃ": "Парные вопросы об истинах",
    "Saṅkhārayamakaṃ": "Парные вопросы о формирующих факторах",
    "Anusayayamakaṃ": "Парные вопросы о скрытых склонностях",
    "Cittayamakaṃ": "Парные вопросы об уме",
    "Dhammayamakaṃ": "Парные вопросы о явлениях",
    "Indriyayamakaṃ": "Парные вопросы о способностях",
}
# Mūlayamakapāḷi niṭṭhitā. = Парные вопросы о корнях завершены. (any "<X>yamaka(pāḷi) niṭṭhitā/ṃ")
YAMAKA_CLOSING_FRAME = "{title} завершены."

# Section-heading words
UDDESO = "Перечень"          # uddeso (pi-1 Uddeso = Перечень)
NIDDESO = "Разъяснение"      # niddeso (pi-1/pi-2)
VARO = "Раздел"              # -vāro (pi-1/pi-2: Раздел …)
NAYO = "метод"               # -nayo (pi-1 Catukkanayo = Четверичный метод)
NITTHITO = "завершён"        # (masc.) niṭṭhito; niṭṭhitā (pl. titles) = завершены
UDDESAVARO_NITTHITO = "Раздел перечня завершён."
NIDDESAVARO_NITTHITO = "Раздел разъяснения завершён."

NAYA = {   # the four methods of the Mūlayamaka
    "mūlanayo": "метод корней",
    "mūlamūlanayo": "метод корней корней",
    "mūlakanayo": "метод основания на корне",
    "mūlamūlakanayo": "метод основания на корне корней",
}

# Recurring section headings of the book (proposals; text after any (N)/(Ka) label).
SECTION_HEADINGS = {
    "Mūlavāro": "Раздел о корнях",
    "Hetuvārādi": "Раздел о причинах и другие",
    "Mūlavārauddeso.": "Перечень раздела о корнях.",
    "Mūlavāraniddeso.": "Разъяснение раздела о корнях.",
    "uddeso": UDDESO,
    "niddeso": NIDDESO,
    "Paṇṇattivāro": "Раздел об обозначениях",
    "Paṇṇattivāraniddesa": "Разъяснение раздела об обозначениях",
    "Padasodhanavāro": "Раздел уточнения слов",
    "Padasodhanamūlacakkavāro": "Круговой раздел на основе уточнения слов",
    "Suddhakhandhavāro": "Раздел о совокупностях как таковых",
    "Suddhakhandhamūlacakkavāro": "Круговой раздел на основе совокупностей как таковых",
    "Suddhindriyamūlacakkavāro": "Круговой раздел на основе способностей как таковых",
    "anulomaṃ": "утвердительная форма",
    "paccanīkaṃ": "отрицательная форма",
    "anulomapuggalo": "утвердительная форма по личности",
    "anulomaokāso": "утвердительная форма по месту",
    "anulomapuggalokāsā": "утвердительная форма по личности и месту",
    "paccanīkapuggalo": "отрицательная форма по личности",
    "paccanīkaokāso": "отрицательная форма по месту",
    "paccanīkapuggalokāsā": "отрицательная форма по личности и месту",
    "paṭilomapuggalo": "отрицательная форма по личности",
    "paṭilomaokāso": "отрицательная форма по месту",
    "paṭilomapuggalokāsā": "отрицательная форма по личности и месту",
    "Pavattivāro 1. uppādavāro": "Раздел о протекании 1. раздел о возникновении",
    "Pavatti 2. nirodhavāro": "Протекание 2. раздел о прекращении",
    "Paccuppannavāro": "Раздел о настоящем",
    "Atītavāro": "Раздел о прошлом",
    "Anāgatavāro": "Раздел о будущем",
    "Paccuppannātītavāro": "Раздел о настоящем и прошлом",
    "Paccuppannānāgatavāro": "Раздел о настоящем и будущем",
    "Atītānāgatavāro": "Раздел о прошлом и будущем",
    "Uppattiṭṭhānavāro": "Раздел о месте возникновения",
    "Mahāvāro 1. anusayavāro": "Большой раздел 1. раздел о скрытых склонностях",
    "Anusayavāra": "Раздел о скрытых склонностях",
    "Sānusayavāro": "Раздел об имеющих скрытые склонности",
    "Sānusayavāra": "Раздел об имеющих скрытые склонности",
    "Pajahanavāro": "Раздел об устранении",
    "Pajahanavāra": "Раздел об устранении",
    "Pariññāvāro": "Раздел о полном понимании",
    "Pahīnavāro": "Раздел об устранённом",
    "dhātuvisajjanāvāro": "раздел ответов об элементах",
    "Suddhacittasāmaññaṃ": "Ум вообще",
    "Suddhacittasāmañña": "Ум вообще",
    "Puggalavāro": "Раздел о личности",
    "Dhammavāro": "Раздел о явлениях",
    "Puggaladhammavāro": "Раздел о личности и явлениях",
    "Uppādanirodhakālasambhedavāro": "Раздел о смешении времени возникновения и прекращения",
    "Uppāduppannavāro": "Раздел о возникновении и возникшем",
    "Nirodhuppannavāro": "Раздел о прекращении и возникшем",
    "Uppādavāro": "Раздел о возникновении",
    "Nirodhavāro": "Раздел о прекращении",
    "Uppādanirodhavāro": "Раздел о возникновении и прекращении",
    "Uppajjamāna-nanirodhavāro": "Раздел о возникающем и непрекращающемся",
    "Uppajjamānananirodhavāro": "Раздел о возникающем и непрекращающемся",
    "Uppajjamānuppannavāro": "Раздел о возникающем и возникшем",
    "Nirujjhamānuppannavāro": "Раздел о прекращающемся и возникшем",
    "Uppannuppādavāro": "Раздел о возникшем и возникновении",
    "Uppannuppajjamānavāro": "Раздел о возникшем и возникающем",
    "Niruddhanirujjhamānavāro": "Раздел о прекратившемся и прекращающемся",
    "Atikkantakālavāro": "Раздел о прошедшем времени",
    "Suttantacittamissakaviseso": "Особенность ума из наставлений в смешении",
    "Abhidhammacittamissakaviseso": "Особенность ума из Абхидхаммы в смешении",
}

# ---------------------------------------------------------------------------------------------
# Adjective slots for the four Mūlayamaka bases (kusala / akusala / abyākata / nāma)
# ---------------------------------------------------------------------------------------------
def _adj(stem, hard="ый"):
    """stem without ending: благ / неблаг / этически неопределённ / умственн."""
    o = "о" if hard == "ой" else "ы"
    return {
        "m_nom": stem + hard,             # благой корень
        "m_gen": stem + "ого",            # благого корня
        "m_prep": stem + "ом",            # на благом корне
        "m_instr": stem + ("им" if hard == "ой" else "ым"),   # с благим корнем
        "n_nom": stem + "ое",             # благое
        "n_instr": stem + ("им" if hard == "ой" else "ым"),   # порождённая благим
        "f_instr": stem + ("ой" if hard == "ой" else "ой"),   # не является благой
        "nom_pl": stem + ("ие" if hard == "ой" else "ые"),    # благие явления
        "gen_pl": stem + ("их" if hard == "ой" else "ых"),    # три благих корня
        "dat_pl": stem + ("им" if hard == "ой" else "ым"),    # к благим явлениям
        "instr_pl": stem + ("ими" if hard == "ой" else "ыми"),  # благими корнями
        "_o": o,
    }


ADJ = {
    "kusala": _adj("благ", "ой"),
    "akusala": _adj("неблаг", "ой"),
    "abyākata": _adj("этически неопределённ"),
    "nāma": _adj("умственн"),
}
PALI_PL = {"kusalā": "kusala", "akusalā": "akusala", "abyākatā": "abyākata", "nāmā": "nāma"}
PALI_SG = {"kusalaṃ": "kusala", "akusalaṃ": "akusala", "abyākataṃ": "abyākata", "nāmaṃ": "nāma"}
NUM = {"Tīṇ": ("три", "корня"), "Nav": ("девять", "корней")}   # Tīṇeva / Naveva
METHOD = {"mūl": 1, "mūlamūl": 2, "mūlak": 3, "mūlamūlak": 4}   # stems before the case ending

# ---------------------------------------------------------------------------------------------
# Fixed formula strings with slots
# ---------------------------------------------------------------------------------------------
AMANTA = "Да."                                                    # Āmantā. (pi-5)
# (Ka) ye keci X dhammā, sabbe te Y?   /   (Ka) ye keci Z dhammā, sabbe te Y?  (Z = predicate phrase)
KA_FRAME = "Все {x_nom_pl} явления {pred_pl}?"
KA_FRAME_PHRASE = "Все явления, {subj_part_pl}, {pred_pl}?"
# (Kha) ye vā pana Y, sabbe te dhammā X?
KHA_FRAME_NOUN = "А все {y_nom_pl} относятся к {x_dat_pl} явлениям?"          # Y a noun (roots)
KHA_FRAME_PHRASE = "А всё, что {y_sg}, относится к {x_dat_pl} явлениям?"     # Y a predicate
# answers
TINEVA_FRAME = "Есть только {num} {x_gen_pl} {root}{tail}."                  # Tīṇeva kusalamūlāni.
AVASESA_NA_FRAME = "Остальные {x_nom_pl} явления {neg_pred_pl}."              # Avasesā kusalā dhammā na kusalamūlā.
AHETUKA_FRAME = "{X_n_nom}, не имеющее корней, {neg_pred_sg}. {X_n_nom}, имеющее корни, {pred_sg}."
SAMUTTHANA_FRAME = ("Материальная форма, порождённая {x_n_instr}, {pred_sg_f}, но не является {x_f_instr}. "
                    "{X_n_nom} и {pred_sg}, и является {x_n_instr}.")
# "… ekamūlāni ceva aññamaññamūlāni ca": the verb stands once, before «и … , и …» (user fix 2026-11-27):
# «Благие корни, которые возникают вместе, имеют и общий корень, и взаимный корень.»
# «… основаны и на общем корне, и на взаимном корне.»
MULANI_FRAME = ("{X_nom_pl} корни, которые возникают вместе, {verb_pl} и {eka_obj}, и {anna_obj}. "
                "Остальные явления, возникшие вместе с {x_m_instr} корнем, {x_eka_pl}, но {neg_anna_pl}.")

# Hetuvāra series (Mūlaṃ hetu nidānañca …): Pāli stem, Russian noun, Russian instrumental (plural
# except питание), whether the adjective takes the neuter singular instrumental.
HETU_SERIES = [
    ("hetu", "причина", "причинами", False),
    ("nidāna", "источник", "источниками", False),
    ("sambhava", "начало", "началами", False),
    ("pabhava", "исток", "истоками", False),
    ("samuṭṭhāna", "порождающий фактор", "порождающими факторами", False),
    ("āhāra", "питание", "питанием", True),
    ("ārammaṇa", "объект", "объектами", False),
    ("paccaya", "условие", "условиями", False),
    ("samudaya", "возникновение", "возникновениями", False),
]
UDDANA_1 = "Корень, причина и источник, начало вместе с истоком;"
UDDANA_2 = "Порождающий фактор, питание, объект{var}, условие вместе с возникновением."
HETU_TINEVA = "Есть только три благие причины"   # Tayo eva kusalahetū


def cap(s):
    return s[0].upper() + s[1:]


def series(x, sep="… "):
    a = ADJ[x]
    return sep.join(f"{a['n_instr'] if sg else a['instr_pl']} {ins}" for _, _, ins, sg in HETU_SERIES)


# ---------------------------------------------------------------------------------------------
# Predicates of the four methods. kind: base / eka / anna. x=None: the bare form (no base word).
# forms: pl, sg (neuter), sg_f, part_pl, neg_pl, neg_sg
# ---------------------------------------------------------------------------------------------
def pred(x, kind, m, form):
    t = " корней" if m in (2, 4) else ""
    a = ADJ[x] if x else None
    if kind == "base" and m in (1, 2):           # kusalamūlā / kusalamūlamūlā: nouns
        noun = f"{a['instr_pl']} корнями{t}"
        return {"pl": f"являются {noun}", "neg_pl": f"не являются {noun}"}[form]
    if m in (1, 2):                               # имеют общий / взаимный … корень (корней)
        adj_acc, adj_gen = {"eka": ("общий", "общего"), "anna": ("взаимный", "взаимного")}[kind]
        acc = f"{adj_acc} {a['m_nom'] + ' ' if a else ''}корень{t}"
        gen = f"{adj_gen} {a['m_gen'] + ' ' if a else ''}корня{t}"
        return {"pl": f"имеют {acc}", "sg": f"имеет {acc}", "sg_f": f"имеет {acc}",
                "part_pl": f"имеющие {acc}", "neg_pl": f"не имеют {gen}", "neg_sg": f"не имеет {gen}"}[form]
    pre = {"base": "", "eka": "общем ", "anna": "взаимном "}[kind]   # m in (3, 4): основан(ы) на …
    loc = f"на {pre}{a['m_prep'] + ' ' if a else ''}корне{t}"
    return {"pl": f"основаны {loc}", "sg": f"основано {loc}", "sg_f": f"основана {loc}",
            "part_pl": f"основанные {loc}", "neg_pl": f"не основаны {loc}", "neg_sg": f"не основано {loc}"}[form]


XS = r"(akusala|kusala|abyākata|nāma)"
SUF = r"(mūlamūlak|mūlamūl|mūlak|mūl)"


def parse_pl(s):
    m = re.fullmatch(XS + r"mūlena (eka|aññamañña)" + SUF + "ā", s)
    if m:
        return m.group(1), ("eka" if m.group(2) == "eka" else "anna"), METHOD[m.group(3)]
    m = re.fullmatch(XS + SUF + "ā", s)
    if m:
        return m.group(1), "base", METHOD[m.group(2)]
    raise ValueError(f"plural predicate not parsed: {s!r}")


def parse_sg(s):
    """-> (x, kind, m, neg) for 'kusalamūlena (na) ekamūlaṃ' / '(na) kusalamūlakaṃ'."""
    m = re.fullmatch(XS + r"mūlena (na )?(eka|aññamañña)" + SUF + "aṃ", s)
    if m:
        return m.group(1), ("eka" if m.group(3) == "eka" else "anna"), METHOD[m.group(4)], bool(m.group(2))
    m = re.fullmatch(r"(na )?" + XS + SUF + "aṃ", s)
    if m:
        return m.group(2), "base", METHOD[m.group(3)], bool(m.group(1))
    raise ValueError(f"singular predicate not parsed: {s!r}")


def ka(subj, p):
    x, kind, m = parse_pl(p)
    if subj in PALI_PL:
        return KA_FRAME.format(x_nom_pl=ADJ[PALI_PL[subj]]["nom_pl"], pred_pl=pred(x, kind, m, "pl"))
    sx, skind, sm = parse_pl(subj)
    return KA_FRAME_PHRASE.format(subj_part_pl=pred(sx, skind, sm, "part_pl"), pred_pl=pred(x, kind, m, "pl"))


def kha(subj, adj):
    x, kind, m = parse_pl(subj)
    dat = ADJ[PALI_PL[adj]]["dat_pl"]
    if kind == "base" and m in (1, 2):
        t = " корней" if m == 2 else ""
        return KHA_FRAME_NOUN.format(y_nom_pl=f"{ADJ[x]['nom_pl']} корни{t}", x_dat_pl=dat)
    return KHA_FRAME_PHRASE.format(y_sg=pred(x, kind, m, "sg"), x_dat_pl=dat)


def answer(s):
    s = s.strip()
    if s == "Āmantā.":
        return AMANTA
    m = re.fullmatch(r"(Tīṇ|Nav)eva " + XS + SUF + r"āni\. Avasesā (akusalā|kusalā|abyākatā|nāmā) dhammā na "
                     + XS + SUF + r"ā\.", s)
    if m:
        num, root = NUM[m.group(1)]
        x, mm = m.group(2), METHOD[m.group(3)]
        assert PALI_PL[m.group(4)] == x == m.group(5) and METHOD[m.group(6)] == mm, s
        a = ADJ[x]
        return (TINEVA_FRAME.format(num=num, x_gen_pl=a["gen_pl"], root=root, tail=" корней" if mm == 2 else "")
                + " " + AVASESA_NA_FRAME.format(x_nom_pl=a["nom_pl"], neg_pred_pl=pred(x, "base", mm, "neg_pl")))
    m = re.fullmatch(r"Ahetukaṃ (\w+) (.+?)\. Sahetukaṃ (\w+) (.+?)\.", s)
    if m:
        x = PALI_SG[m.group(1)]
        assert PALI_SG[m.group(3)] == x, s
        x1, k1, m1, n1 = parse_sg(m.group(2))
        x2, k2, m2, n2 = parse_sg(m.group(4))
        assert x1 == x2 == x and (k1, m1) == (k2, m2) and n1 and not n2, s
        return AHETUKA_FRAME.format(X_n_nom=cap(ADJ[x]["n_nom"]), neg_pred_sg=pred(x, k1, m1, "neg_sg"),
                                    pred_sg=pred(x, k1, m1, "sg"))
    low = re.sub(r"(^|\. )(\w)", lambda mo: mo.group(1) + mo.group(2).lower(), s)   # sentence capitals
    m = re.fullmatch(XS + r"samuṭṭhānaṃ rūpaṃ (.+?),? na (\w+)\. (\w+) (.+?)ñceva (\w+)ñca\.", low)
    if m:
        x = m.group(1)
        assert PALI_SG[m.group(3)] == x == PALI_SG[m.group(4)] and m.group(6) + "ṃ" == m.group(3), s
        x1, k1, m1, n1 = parse_sg(m.group(2))
        x2, k2, m2, n2 = parse_sg(m.group(5) + "ṃ")
        assert x1 == x2 == x and (k1, m1) == (k2, m2) and not n1 and not n2, s
        a = ADJ[x]
        return SAMUTTHANA_FRAME.format(x_n_instr=a["n_instr"], pred_sg_f=pred(x, k1, m1, "sg_f"),
                                       x_f_instr=a["f_instr"], X_n_nom=cap(a["n_nom"]),
                                       pred_sg=pred(x, k1, m1, "sg"))
    m = re.fullmatch(r"Mūlāni yāni ekato uppajjanti " + XS + r"mūlāni eka" + SUF + r"āni ceva aññamañña" + SUF
                     + r"āni ca\. Avasesā " + XS + r"mūlasahajātā dhammā " + XS + r"mūlena eka" + SUF
                     + r"ā,? na ca aññamañña" + SUF + r"ā\.", s)
    if m:
        x = m.group(1)
        ms = {METHOD[m.group(i)] for i in (2, 3, 6, 7)}
        assert x == m.group(4) == m.group(5) and len(ms) == 1, s
        mm = ms.pop()
        a = ADJ[x]
        verb, eka_obj = pred(None, "eka", mm, "pl").split(" ", 1)
        verb2, anna_obj = pred(None, "anna", mm, "pl").split(" ", 1)
        assert verb == verb2, s
        return MULANI_FRAME.format(X_nom_pl=cap(a["nom_pl"]), verb_pl=verb, eka_obj=eka_obj,
                                   anna_obj=anna_obj, x_m_instr=a["m_instr"],
                                   x_eka_pl=pred(x, "eka", mm, "pl"), neg_anna_pl=pred(None, "anna", mm, "neg_pl"))
    raise ValueError(f"answer not parsed: {s!r}")


# ---------------------------------------------------------------------------------------------
# Fixed lines of the sample (exact Pāli line text without the block ID -> Russian)
# ---------------------------------------------------------------------------------------------
VAR_KA = " [вариант чтения (Ka.): samuṭṭhānāhārārammaṇaṃ]"
FIXED = {
    "Namo tassa bhagavato arahato sammāsambuddhassa": NAMO,
    "# Abhidhammapiṭake": "# " + ABHIDHAMMAPITAKE,
    "## Yamakapāḷi": "## " + BOOK_TITLE,
    "### Mūlayamakaṃ": "### " + YAMAKA_TITLES["Mūlayamakaṃ"],
    "#### (Ka) uddeso": f"#### ({LETTERS['Ka']}) {UDDESO}",
    "##### (Kha) niddeso": f"##### ({LETTERS['Kha']}) {NIDDESO}",
    "#### Mūlavāro": "#### " + SECTION_HEADINGS["Mūlavāro"],
    "#### Kusalā dhammā": "#### " + cap(ADJ["kusala"]["nom_pl"]) + " явления",
    "#### 2-10. Hetuvārādi": "#### 2-10. " + SECTION_HEADINGS["Hetuvārādi"],
    "Mūlavārauddeso.": SECTION_HEADINGS["Mūlavārauddeso."],
    "Mūlavāraniddeso.": SECTION_HEADINGS["Mūlavāraniddeso."],
    "Uddesavāro niṭṭhito.": UDDESAVARO_NITTHITO,
    "Niddesavāro niṭṭhito.": NIDDESAVARO_NITTHITO,
    "Mūlayamakapāḷi niṭṭhitā.": YAMAKA_CLOSING_FRAME.format(title=YAMAKA_TITLES["Mūlayamakaṃ"]),
    "Mūlaṃ hetu nidānañca, sambhavo pabhavena ca;": UDDANA_1,
    "Samuṭṭhānāhārārammaṇā [samuṭṭhānāhārārammaṇaṃ (ka.)], paccayo samudayena cāti.": UDDANA_2.format(var=VAR_KA),
    "Samuṭṭhānāhārārammaṇā, paccayo samudayena cāti.": UDDANA_2.format(var=""),
    # hetuvāra lines ("…pe…" -> "…"; final "…pe…." / "…." -> "…")
    ("Ye keci kusalā dhammā, sabbe te kusalahetū…pe… kusalanidānā…pe… kusalasambhavā…pe… kusalappabhavā…pe… "
     "kusalasamuṭṭhānā…pe… kusalāhārā…pe… kusalārammaṇā…pe… kusalapaccayā…pe… kusalasamudayā…pe…."):
        f"Все {ADJ['kusala']['nom_pl']} явления являются {series('kusala')}…",
    "Ye keci kusalā dhammā, sabbe te kusalahetūti…?":
        f"Все {ADJ['kusala']['nom_pl']} явления являются {ADJ['kusala']['instr_pl']} причинами…?",
    ("Tayo eva kusalahetū, avasesā kusalā dhammā na kusalahetū…pe… kusalanidānā… kusalasambhavā… kusalappabhavā… "
     "kusalasamuṭṭhānā… kusalāhārā… kusalārammaṇā… kusalapaccayā… kusalasamudayā…."):
        f"{HETU_TINEVA}, остальные {ADJ['kusala']['nom_pl']} явления не являются {series('kusala')}…",
    ("Ye keci akusalā dhammā… ye keci abyākatā dhammā… ye keci nāmā dhammā, sabbe te nāmahetū ti… nāmanidānā… "
     "nāmasambhavā… nāmappabhavā… nāmasamuṭṭhānā… nāmāhārā… nāmārammaṇā… nāmapaccayā… nāmasamudayā…."):
        (f"Все {ADJ['akusala']['nom_pl']} явления… все {ADJ['abyākata']['nom_pl']} явления… "
         f"все {ADJ['nāma']['nom_pl']} явления являются {series('nāma')}…"),
}

NAYA_HEAD = re.compile(r"(#+) (?:(Kusalā|Akusalā|Abyākatā|Nāmā) dhammā )?\((\d+)\) (\w+)")
KA_RE = re.compile(r"\(Ka\) ye keci (.+?) dhammā, sabbe te (.+?)(?:ti)?\?(.*)")
KHA_RE = re.compile(r"\(Kha\) ye vā pana (.+?), sabbe te dhammā (akusalā|kusalā|abyākatā|nāmā)(?:ti)?\?(.*)")
ID_RE = re.compile(r"^(.*?)( \^[0-9A-Za-z-]+)?$")


def tr(text):
    """Translate one Pāli line (block ID already removed)."""
    if not text.strip():
        return ""
    if text in FIXED:
        return FIXED[text]
    m = NAYA_HEAD.fullmatch(text)
    if m:
        naya = NAYA[m.group(4).lower()]
        if m.group(2):
            x = PALI_PL[m.group(2).lower()]
            return f"{m.group(1)} {cap(ADJ[x]['nom_pl'])} явления ({m.group(3)}) {naya}"
        return f"{m.group(1)} ({m.group(3)}) {cap(naya)}"
    m = KA_RE.fullmatch(text)
    if m:
        out = f"({LETTERS['Ka']}) " + ka(m.group(1), m.group(2))
        return out + (" " + answer(m.group(3)) if m.group(3).strip() else "")
    m = KHA_RE.fullmatch(text)
    if m:
        out = f"({LETTERS['Kha']}) " + kha(m.group(1), m.group(2))
        return out + (" " + answer(m.group(3)) if m.group(3).strip() else "")
    return answer(text)


def translate_file(src_text):
    out = []
    for line in src_text.split("\n"):
        body, bid = ID_RE.match(line).groups()
        out.append(tr(body) + (bid or ""))
    return "\n".join(out)


# ---------------------------------------------------------------------------------------------
# Checks
# ---------------------------------------------------------------------------------------------
DASHES = ("–", "—")
ID_ANY = re.compile(r"\^[0-9A-Za-z-]+\s*$")


def check_pair(pali, ru, name=""):
    """Per-line checks of a Russian file against its Pāli source (both full texts)."""
    errs = []
    pl, rl = pali.split("\n"), ru.split("\n")
    if len(pl) != len(rl):
        errs.append(f"line count {len(pl)} vs {len(rl)}")
    if "\r" in ru:
        errs.append("CR found")
    if "\n\n\n" in ru:
        errs.append("double blank line")
    if not unicodedata.is_normalized("NFC", ru):
        errs.append("not NFC")
    for i, (p, r) in enumerate(zip(pl, rl), 1):
        if bool(p.strip()) != bool(r.strip()):
            errs.append(f"{i}: blank/non-blank mismatch")
        pid, rid = ID_ANY.search(p), ID_ANY.search(r)
        if (pid and pid.group(0).strip()) != (rid and rid.group(0).strip()):
            errs.append(f"{i}: block ID differs")
        for d in DASHES:
            if p.count(d) != r.count(d):
                errs.append(f"{i}: dash {d!r} count {p.count(d)} vs {r.count(d)}")
        if ":-" in r:
            errs.append(f"{i}: ':-'")
        if "…." in r:
            errs.append(f"{i}: '….'")
        if '"' in r or "'" in r:
            errs.append(f"{i}: straight quote")
        if r.count("«") != r.count("»") or r.count("„") != r.count("“"):
            errs.append(f"{i}: unbalanced quotes")
        if re.search(r"(?<![А-Яа-яЁё])ли(?![А-Яа-яЁё])", r):
            errs.append(f"{i}: «ли»")
        if "  " in r or r != r.strip():
            errs.append(f"{i}: extra spaces")
        body = ID_ANY.sub("", re.sub(r"\[[^\]]*\]", "", r))
        if re.search(r"[A-Za-zÀ-ɏḀ-ỿ]", body):
            errs.append(f"{i}: Latin outside brackets")
        if p.startswith("#") != r.startswith("#") or (p.startswith("#") and p.split(" ")[0] != r.split(" ")[0]):
            errs.append(f"{i}: heading level differs")
    if errs:
        raise AssertionError(f"{name}: " + "; ".join(errs[:20]))
    return True


# Strings this builder takes from the approved pi-1 … pi-5 Russian rails (book, exact string).
CROSSBOOK = [
    ("5", NAMO), ("1", NAMO), ("5", "# " + ABHIDHAMMAPITAKE), ("1", "# " + ABHIDHAMMAPITAKE),
    ("1", "(а) Благие явления."), ("1", "(б) Неблагие явления."), ("1", "(в) Этически неопределённые явления."),
    ("1", "как благой корень"), ("1", "Явления, имеющие корни."), ("1", "Явления, не имеющие корней."),
    ("1", "(а) Умственное."), ("1", "порождённая умом"), ("1", "материальная форма"),
    ("1", "#### Перечень"), ("1", "##### Разъяснение"), ("2", "##### Разъяснение"),
    ("1", "##### Четверичный метод"), ("2", "##### Раздел о явлениях"), ("2", "##### Раздел о причине"),
    ("1", "### Матрица"), ("2", "завершён."), ("1", "завершена."), ("5", "? Да."),
    ("1", "Остальные"), ("1", "объект"), ("1", "питание"), ("1", "источник"), ("2", "условию"),
    ("1", "возникают вместе"), ("1", "возникшее вместе"), ("1", "возникновение"),
    ("1", "совокупность"), ("1", "сферы восприятия"), ("1", "элемент"), ("2", "истина"),
    ("5", "формирующие факторы"), ("1", "скрытая склонность"), ("1", "способность"), ("5", "Личность"),
]


def check_crossbook():
    cache = {}
    missing = []
    for b, s in CROSSBOOK:
        if b not in cache:
            cache[b] = "\n".join(p.read_text(encoding="utf-8") for p in sorted(RAILS[b].glob("*.md")))
        if s not in cache[b]:
            missing.append((b, s))
    if missing:
        raise AssertionError(f"cross-book strings not found in the pi-1..5 rails: {missing}")
    return True


SAMPLE_FILES = ["preamble.md", "1-mulayamaka.md"]


def main():
    check_crossbook()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    seen = {}
    for name in SAMPLE_FILES:
        src = (PALI_DIR / name).read_text(encoding="utf-8")
        ru = unicodedata.normalize("NFC", translate_file(src))
        for p, r in zip(src.split("\n"), ru.split("\n")):   # identical Pāli -> identical Russian
            pb, rb = ID_ANY.sub("", p).strip(), ID_ANY.sub("", r).strip()
            if pb in seen:
                assert seen[pb] == rb, f"inconsistent: {pb!r}"
            seen[pb] = rb
        check_pair(src, ru, name)
        with open(OUT_DIR / name, "w", encoding="utf-8", newline="\n") as f:
            f.write(ru)
        print("written", OUT_DIR / name, "lines", len(ru.split("\n")))
    print("cross-book asserts OK; per-line checks OK")


if __name__ == "__main__":
    main()
