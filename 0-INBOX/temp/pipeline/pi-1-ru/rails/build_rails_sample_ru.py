"""Builder for the Russian rails SAMPLE of pi-1 (Dhammasaṅgaṇī, plain audience).

Writes (only when run as a script):
  AI_translation/russian/pi-1-russian-plain-rails_split_chapters/preamble.md
  AI_translation/russian/pi-1-russian-plain-rails_split_chapters/1-matika.md
  0-INBOX/temp/pipeline/pi-1-ru/rails/sample-2-01/2-01-sample.md
  0-INBOX/temp/pipeline/pi-1-ru/rails/ru-rails-formulas.md

All Russian comes from the fixed strings below, so identical Pāli gives byte-identical Russian.
Every term follows the locked termbase AI_translation/russian/pi-1-pali-russian-termbase-plain.md.
Later chapter builders may import the constants (MATRIX, FACTORS, S_*, frame functions);
importing writes nothing.

usage: python -I -X utf8 build_rails_sample_ru.py
"""
import pathlib
import re

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
PALI = ROOT / "AI_translation" / "pali" / "pi-1_split_chapters"
OUT = ROOT / "AI_translation" / "russian" / "pi-1-russian-plain-rails_split_chapters"
PIPE = ROOT / "0-INBOX" / "temp" / "pipeline" / "pi-1-ru"
RAILS = PIPE / "rails"
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")


def cap(s):
    return s[0].upper() + s[1:]


def low(s):
    return s[0].lower() + s[1:]


# ================================================================== labels, variants
LAB = ["(а)", "(б)", "(в)"]          # (Ka) (Kha) (Ga)


def spell(sig, word):
    """Spelling-only variant: [vi (sī. syā.)] -> [вариант написания (Sī., Syā.): vi]."""
    return f"[вариант написания ({sig}): {word}]"


def reading(sig, word):
    """Variant with a different word or wording."""
    return f"[вариант чтения ({sig}): {word}]"


# ================================================================== text frame and headings
HOMAGE = "Почтение Благословенному, Достойному, Полностью Пробуждённому Будде"
H_PITAKA = "В корзине Абхидхаммы"
H_BOOK = "Перечисление явлений"
H_MATIKA = "Матрица"
TIKA = "Матрица троек"
DUKA = "Матрица пар"
ABHI_DUKA = "Матрица пар Абхидхаммы"
SUTTA_DUKA = "Матрица пар из наставлений"
MATIKA_DONE = "Матрица завершена"
CUULANTARA = "Малые промежуточные пары"
MAHANTARA = "Большие промежуточные пары"
PITTHI = "Заключительные пары"

CH_HEADINGS = {   # chapters 2-5 (### level)
    "Cittuppādakaṇḍaṃ": "Раздел о возникновении ума",
    "Rūpakaṇḍaṃ": "Раздел о материальной форме",
    "Nikkhepakaṇḍaṃ": "Раздел сводки",
    "Aṭṭhakathākaṇḍaṃ": "Раздел разъяснений",
}
H_KAMA_KUSALA = "Благой ум, относящийся к миру чувственных желаний"   # Kāmāvacarakusalaṃ
H_PADABHAJANI = "Разбор по словам"                                    # Padabhājanī / Padabhājanīyaṃ.
BHANAVARA_1 = "Первый раздел для чтения вслух"                        # Paṭhamabhāṇavāro.

# ================================================================== matrix
# Each item: (pali name as used after «Katame dhammā», russian name in lower case, variant or "")
# Matrix line = "(а) " + cap(name) + variant + "."; question = «Что такое name?»; answer = «это name.»
PH = "явления"


def q_form(name):
    return f"Что такое {name}?"


def a_form(name):
    return f"это {name}."


TRIADS = {
    "1-M1-1": [("kusalā", "благие явления", ""), ("akusalā", "неблагие явления", ""),
               ("abyākatā", "этически неопределённые явления", "")],
    "1-M1-2": [("sukhāya vedanāya sampayuttā", "явления, связанные с приятным чувством", ""),
               ("dukkhāya vedanāya sampayuttā", "явления, связанные с болезненным чувством", ""),
               ("adukkhamasukhāya vedanāya sampayuttā",
                "явления, связанные с чувством, которое ни болезненно, ни приятно", "")],
    "1-M1-3": [("vipākā", "явления, являющиеся результатом действий", ""),
               ("vipākadhammadhammā", "явления, способные приносить результаты", ""),
               ("nevavipākanavipākadhammadhammā",
                "явления, не являющиеся результатом действий и не способные приносить результаты", "")],
    "1-M1-4": [("upādiṇṇupādāniyā", "явления, охваченные цеплянием и служащие его объектом",
                spell("Syā.", "upādinnupādāniyā")),
               ("anupādiṇṇupādāniyā", "явления, не охваченные цеплянием, но служащие его объектом", ""),
               ("anupādiṇṇaanupādāniyā", "явления, не охваченные цеплянием и не служащие его объектом",
                spell("Syā.", "anupādinnānupādāniyā"))],
    "1-M1-5": [("saṃkiliṭṭhasaṃkilesikā", "явления, омрачённые и подверженные омрачению", ""),
               ("asaṃkiliṭṭhasaṃkilesikā", "явления, неомрачённые, но подверженные омрачению", ""),
               ("asaṃkiliṭṭhaasaṃkilesikā", "явления, неомрачённые и не подверженные омрачению",
                spell("Syā.", "asaṃkiliṭṭhāsaṃkilesikā"))],
    "1-M1-6": [("savitakkasavicārā", "явления с направленной мыслью и удержанием мысли", ""),
               ("avitakkavicāramattā", "явления без направленной мысли, только с удержанием мысли", ""),
               ("avitakkaavicārā", "явления без направленной мысли и без удержания мысли",
                spell("Syā.", "avitakkāvicārā"))],
    "1-M1-7": [("pītisahagatā", "явления, сопровождаемые восторгом", ""),
               ("sukhasahagatā", "явления, сопровождаемые счастьем", ""),
               ("upekkhāsahagatā", "явления, сопровождаемые невозмутимостью", "")],
    "1-M1-8": [("dassanena pahātabbā", "явления, устраняемые видением истины", ""),
               ("bhāvanāya pahātabbā", "явления, устраняемые развитием ума", ""),
               ("neva dassanena na bhāvanāya pahātabbā",
                "явления, не устраняемые ни видением истины, ни развитием ума", "")],
    "1-M1-9": [("dassanena pahātabbahetukā", "явления, чьи корни устраняются видением истины", ""),
               ("bhāvanāya pahātabbahetukā", "явления, чьи корни устраняются развитием ума", ""),
               ("neva dassanena na bhāvanāya pahātabbahetukā",
                "явления, чьи корни не устраняются ни видением истины, ни развитием ума", "")],
    "1-M1-10": [("ācayagāmino", "явления, ведущие к накоплению", ""),
                ("apacayagāmino", "явления, ведущие к убыванию", ""),
                ("nevācayagāmināpacayagāmino", "явления, не ведущие ни к накоплению, ни к убыванию",
                 spell("Syā.", "nevācayagāmino nāpacayagāmino"))],
    "1-M1-11": [("sekkhā", "явления, относящиеся к обучающимся", ""),
                ("asekkhā", "явления, относящиеся к завершившим обучение", ""),
                ("nevasekkhanāsekkhā", "явления, не относящиеся ни к обучающимся, ни к завершившим обучение",
                 spell("Sī., Syā.", "nevasekkhānāsekkhā"))],
    "1-M1-12": [("parittā", "ограниченные явления", ""), ("mahaggatā", "возвышенные явления", ""),
                ("appamāṇā", "безмерные явления", "")],
    "1-M1-13": [("parittārammaṇā", "явления с ограниченным объектом", ""),
                ("mahaggatārammaṇā", "явления с возвышенным объектом", ""),
                ("appamāṇārammaṇā", "явления с безмерным объектом", "")],
    "1-M1-14": [("hīnā", "низшие явления", ""), ("majjhimā", "средние явления", ""),
                ("paṇītā", "высшие явления", "")],
    "1-M1-15": [("micchattaniyatā", "явления, предопределённо ведущие к ложному", ""),
                ("sammattaniyatā", "явления, предопределённо ведущие к правильному", ""),
                ("aniyatā", "непредопределённые явления", "")],
    "1-M1-16": [("maggārammaṇā", "явления, имеющие объектом путь", ""),
                ("maggahetukā", "явления, имеющие корнем путь", ""),
                ("maggādhipatino", "явления, находящиеся под главенством пути", "")],
    "1-M1-17": [("uppannā", "возникшие явления", ""), ("anuppannā", "невозникшие явления", ""),
                ("uppādino", "явления, которым предстоит возникнуть", "")],
    "1-M1-18": [("atītā", "прошлые явления", ""), ("anāgatā", "будущие явления", ""),
                ("paccuppannā", "настоящие явления", "")],
    "1-M1-19": [("atītārammaṇā", "явления с прошлым объектом", ""),
                ("anāgatārammaṇā", "явления с будущим объектом", ""),
                ("paccuppannārammaṇā", "явления с настоящим объектом", "")],
    "1-M1-20": [("ajjhattā", "внутренние явления", ""), ("bahiddhā", "внешние явления", ""),
                ("ajjhattabahiddhā", "внутренние и внешние явления", "")],
    "1-M1-21": [("ajjhattārammaṇā", "явления с внутренним объектом", ""),
                ("bahiddhārammaṇā", "явления с внешним объектом", ""),
                ("ajjhattabahiddhārammaṇā", "явления с внутренним и внешним объектом", "")],
    "1-M1-22": [("sanidassanasappaṭighā", "видимые и способные к соударению явления", ""),
                ("anidassanasappaṭighā", "невидимые, но способные к соударению явления", ""),
                ("anidassanaappaṭighā", "невидимые и не способные к соударению явления",
                 spell("Syā.", "anidassanāppaṭighā"))],
}

# ---- the clusters (gocchaka) share one shape; Russian pieces per cluster
# pali: nom, neg ("no"/"na"), prone, notprone, d6 head (the «X kho pana» word)
# ru: is_ / isnot (являющиеся X / не являющиеся X), prone / notprone, assoc / dissoc,
#     d6_gen (genitive of the «kho pana» head), d6_nom, heading
CLUSTERS = {
    "hetu": dict(
        sids=["1-M2-1", "1-M2-2", "1-M2-3", "1-M2-4", "1-M2-5", "1-M2-6"],
        p_nom="hetū", p_neg="na", p_prone="sahetukā", p_notprone="ahetukā",
        p_assoc="hetusampayuttā", p_dissoc="hetuvippayuttā", p_d6="na hetū",
        is_="являющиеся корнями", isnot="не являющиеся корнями",
        prone="имеющие корни", notprone="не имеющие корней",
        assoc="связанные с корнями", dissoc="не связанные с корнями",
        d6_gen="не являющихся корнями", d6_nom="не являющиеся корнями",
        heading="Группа корней", p_heading="Hetugocchakaṃ"),
    "asava": dict(
        sids=["1-M2-14", "1-M2-15", "1-M2-16", "1-M2-17", "1-M2-18", "1-M2-19"],
        p_nom="āsavā", p_neg="no", p_prone="sāsavā", p_notprone="anāsavā",
        p_assoc="āsavasampayuttā", p_dissoc="āsavavippayuttā", p_d6="āsavavippayuttā",
        is_="являющиеся влечениями", isnot="не являющиеся влечениями",
        prone="подверженные влечениям", notprone="свободные от влечений",
        assoc="связанные с влечениями", dissoc="не связанные с влечениями",
        d6_gen="не связанных с влечениями", d6_nom="не связанные с влечениями",
        heading="Группа влечений", p_heading="Āsavagocchakaṃ"),
    "samyojana": dict(
        sids=["1-M2-20", "1-M2-21", "1-M2-22", "1-M2-23", "1-M2-24", "1-M2-25"],
        p_nom="saṃyojanā", p_neg="no", p_prone="saṃyojaniyā", p_notprone="asaṃyojaniyā",
        p_assoc="saṃyojanasampayuttā", p_dissoc="saṃyojanavippayuttā", p_d6="saṃyojanavippayuttā",
        is_="являющиеся оковами", isnot="не являющиеся оковами",
        prone="подверженные оковам", notprone="не подверженные оковам",
        assoc="связанные с оковами", dissoc="не связанные с оковами",
        d6_gen="не связанных с оковами", d6_nom="не связанные с оковами",
        heading="Группа оков", p_heading="Saṃyojanagocchakaṃ"),
    "gantha": dict(
        sids=["1-M2-26", "1-M2-27", "1-M2-28", "1-M2-29", "1-M2-30", "1-M2-31"],
        p_nom="ganthā", p_neg="no", p_prone="ganthaniyā", p_notprone="aganthaniyā",
        p_assoc="ganthasampayuttā", p_dissoc="ganthavippayuttā", p_d6="ganthavippayuttā",
        is_="являющиеся узами", isnot="не являющиеся узами",
        prone="подверженные узам", notprone="не подверженные узам",
        assoc="связанные с узами", dissoc="не связанные с узами",
        d6_gen="не связанных с узами", d6_nom="не связанные с узами",
        heading="Группа уз", p_heading="Ganthagocchakaṃ"),
    "ogha": dict(
        sids=["1-M2-32", "1-M2-33", "1-M2-34", "1-M2-35", "1-M2-36", "1-M2-37"],
        p_nom="oghā", p_neg="no", p_prone="oghaniyā", p_notprone="anoghaniyā",
        p_assoc="oghasampayuttā", p_dissoc="oghavippayuttā", p_d6="oghavippayuttā",
        is_="являющиеся потоками", isnot="не являющиеся потоками",
        prone="подверженные потокам", notprone="не подверженные потокам",
        assoc="связанные с потоками", dissoc="не связанные с потоками",
        d6_gen="не связанных с потоками", d6_nom="не связанные с потоками",
        heading="Группа потоков", p_heading="Oghagocchakaṃ"),
    "yoga": dict(
        sids=["1-M2-38", "1-M2-39", "1-M2-40", "1-M2-41", "1-M2-42", "1-M2-43"],
        p_nom="yogā", p_neg="no", p_prone="yoganiyā", p_notprone="ayoganiyā",
        p_assoc="yogasampayuttā", p_dissoc="yogavippayuttā", p_d6="yogavippayuttā",
        is_="являющиеся ярмами", isnot="не являющиеся ярмами",
        prone="подверженные ярмам", notprone="не подверженные ярмам",
        assoc="связанные с ярмами", dissoc="не связанные с ярмами",
        d6_gen="не связанных с ярмами", d6_nom="не связанные с ярмами",
        heading="Группа ярм", p_heading="Yogagocchakaṃ"),
    "nivarana": dict(
        sids=["1-M2-44", "1-M2-45", "1-M2-46", "1-M2-47", "1-M2-48", "1-M2-49"],
        p_nom="nīvaraṇā", p_neg="no", p_prone="nīvaraṇiyā", p_notprone="anīvaraṇiyā",
        p_assoc="nīvaraṇasampayuttā", p_dissoc="nīvaraṇavippayuttā", p_d6="nīvaraṇavippayuttā",
        is_="являющиеся помехами", isnot="не являющиеся помехами",
        prone="подверженные помехам", notprone="не подверженные помехам",
        assoc="связанные с помехами", dissoc="не связанные с помехами",
        d6_gen="не связанных с помехами", d6_nom="не связанные с помехами",
        heading="Группа помех", p_heading="Nīvaraṇagocchakaṃ"),
    "paramasa": dict(   # no «ceva … sampayuttā» pair: 5 segments
        sids=["1-M2-50", "1-M2-51", "1-M2-52", "1-M2-53", None, "1-M2-54"],
        p_nom="parāmāsā", p_neg="no", p_prone="parāmaṭṭhā", p_notprone="aparāmaṭṭhā",
        p_assoc="parāmāsasampayuttā", p_dissoc="parāmāsavippayuttā", p_d6="parāmāsavippayuttā",
        is_="являющиеся искажениями", isnot="не являющиеся искажениями",
        prone="затронутые искажениями", notprone="не затронутые искажениями",
        assoc="связанные с искажениями", dissoc="не связанные с искажениями",
        d6_gen="не связанных с искажениями", d6_nom="не связанные с искажениями",
        heading="Группа искажений", p_heading="Parāmāsagocchakaṃ"),
    "upadana": dict(
        sids=["1-M2-69", "1-M2-70", "1-M2-71", "1-M2-72", "1-M2-73", "1-M2-74"],
        p_nom="upādānā", p_neg="no", p_prone="upādāniyā", p_notprone="anupādāniyā",
        p_assoc="upādānasampayuttā", p_dissoc="upādānavippayuttā", p_d6="upādānavippayuttā",
        is_="являющиеся цепляниями", isnot="не являющиеся цепляниями",
        prone="служащие объектом цепляния", notprone="не служащие объектом цепляния",
        assoc="связанные с цепляниями", dissoc="не связанные с цепляниями",
        d6_gen="не связанных с цепляниями", d6_nom="не связанные с цепляниями",
        heading="Группа цепляний", p_heading="Upādānagocchakaṃ"),
}

# pair items: sid -> [(pali name, ru name, variant), (…)] ; special lines in MATRIX_LINES
PAIRS = {}
MATRIX_LINES = {}       # sid -> full list of Russian lines (without the block id)
EXTRA_NAMES = []        # (pali, ru) names used only in chapter frames (the «kho pana» pairs)


def cluster(c):
    s = c["sids"]
    PAIRS[s[0]] = [(c["p_nom"], f"{PH}, {c['is_']}", ""),
                   (f"{c['p_neg']} {c['p_nom']}", f"{PH}, {c['isnot']}", "")]
    PAIRS[s[1]] = [(c["p_prone"], f"{PH}, {c['prone']}", ""),
                   (c["p_notprone"], f"{PH}, {c['notprone']}", "")]
    PAIRS[s[2]] = [(c["p_assoc"], f"{PH}, {c['assoc']}", ""),
                   (c["p_dissoc"], f"{PH}, {c['dissoc']}", "")]
    PAIRS[s[3]] = [(f"{c['p_nom']} ceva {c['p_prone']} ca", f"{PH}, {c['is_']} и {c['prone']}", ""),
                   (f"{c['p_prone']} ceva {c['p_neg']} ca {c['p_nom']}",
                    f"{PH}, {c['prone']}, но {c['isnot']}", "")]
    if s[4]:
        PAIRS[s[4]] = [(f"{c['p_nom']} ceva {c['p_assoc']} ca", f"{PH}, {c['is_']} и {c['assoc']}", ""),
                       (f"{c['p_assoc']} ceva {c['p_neg']} ca {c['p_nom']}",
                        f"{PH}, {c['assoc']}, но {c['isnot']}", "")]
    MATRIX_LINES[s[5]] = [f"{LAB[0]} Среди явлений, {c['d6_gen']}, есть и {c['prone']}.",
                          f"{LAB[1]} Есть и {c['notprone']}.",
                          f"{c['heading']}."]
    EXTRA_NAMES.append((f"{c['p_d6']} {c['p_prone']}", f"{PH}, {c['d6_nom']}, но {c['prone']}"))
    EXTRA_NAMES.append((f"{c['p_d6']} {c['p_notprone']}", f"{PH}, {c['d6_nom']} и {c['notprone']}"))


for _c in CLUSTERS.values():
    cluster(_c)

PAIRS.update({
    # Cūḷantaradukaṃ
    "1-M2-7": [("sappaccayā", "явления, имеющие условия", ""), ("appaccayā", "явления, не имеющие условий", "")],
    "1-M2-8": [("saṅkhatā", "обусловленные явления", ""), ("asaṅkhatā", "необусловленные явления", "")],
    "1-M2-9": [("sanidassanā", "видимые явления", ""), ("anidassanā", "невидимые явления", "")],
    "1-M2-10": [("sappaṭighā", "явления, способные к соударению", ""),
                ("appaṭighā", "явления, не способные к соударению", "")],
    "1-M2-11": [("rūpino", "материальные явления", ""), ("arūpino", "нематериальные явления", "")],
    "1-M2-12": [("lokiyā", "мирские явления", ""), ("lokuttarā", "надмирские явления", "")],
    "1-M2-13": [("kenaci viññeyyā", "явления, познаваемые тем или иным видом сознания", ""),
                ("kenaci na viññeyyā", "явления, не познаваемые тем или иным видом сознания", "")],
    # Mahantaradukaṃ
    "1-M2-55": [("sārammaṇā", "явления, имеющие объект", ""), ("anārammaṇā", "явления, не имеющие объекта", "")],
    "1-M2-56": [("cittā", "явления, являющиеся умом", ""), ("no cittā", "явления, не являющиеся умом", "")],
    "1-M2-57": [("cetasikā", "явления, сопутствующие уму", ""), ("acetasikā", "явления, не сопутствующие уму", "")],
    "1-M2-58": [("cittasampayuttā", "явления, связанные с умом", ""),
                ("cittavippayuttā", "явления, не связанные с умом", "")],
    "1-M2-59": [("cittasaṃsaṭṭhā", "явления, соединённые с умом", ""),
                ("cittavisaṃsaṭṭhā", "явления, не соединённые с умом", "")],
    "1-M2-60": [("cittasamuṭṭhānā", "явления, порождённые умом", ""),
                ("no cittasamuṭṭhānā", "явления, не порождённые умом", "")],
    "1-M2-61": [("cittasahabhuno", "явления, сосуществующие с умом", ""),
                ("no cittasahabhuno", "явления, не сосуществующие с умом", "")],
    "1-M2-62": [("cittānuparivattino", "явления, следующие за умом", ""),
                ("no cittānuparivattino", "явления, не следующие за умом", "")],
    "1-M2-63": [("cittasaṃsaṭṭhasamuṭṭhānā", "явления, соединённые с умом и порождённые им", ""),
                ("no cittasaṃsaṭṭhasamuṭṭhānā", "явления, не являющиеся соединёнными с умом и порождёнными им", "")],
    "1-M2-64": [("cittasaṃsaṭṭhasamuṭṭhānasahabhuno",
                 "явления, соединённые с умом, порождённые им и сосуществующие с ним", ""),
                ("no cittasaṃsaṭṭhasamuṭṭhānasahabhuno",
                 "явления, не являющиеся соединёнными с умом, порождёнными им и сосуществующими с ним", "")],
    "1-M2-65": [("cittasaṃsaṭṭhasamuṭṭhānānuparivattino",
                 "явления, соединённые с умом, порождённые им и следующие за ним", ""),
                ("no cittasaṃsaṭṭhasamuṭṭhānānuparivattino",
                 "явления, не являющиеся соединёнными с умом, порождёнными им и следующими за ним", "")],
    "1-M2-66": [("ajjhattikā", "явления, относящиеся к внутреннему", ""),
                ("bāhirā", "явления, относящиеся к внешнему", "")],
    "1-M2-67": [("upādā", "производные явления", ""), ("no upādā", "непроизводные явления", "")],
    "1-M2-68": [("upādiṇṇā", "явления, охваченные цеплянием", spell("Sī., Syā.", "upādinnā")),
                ("anupādiṇṇā", "явления, не охваченные цеплянием", "")],
    # Kilesagocchakaṃ
    "1-M2-75": [("kilesā", "явления, являющиеся омрачениями", ""),
                ("no kilesā", "явления, не являющиеся омрачениями", "")],
    "1-M2-76": [("saṃkilesikā", "явления, подверженные омрачению", ""),
                ("asaṃkilesikā", "явления, не подверженные омрачению", "")],
    "1-M2-77": [("saṃkiliṭṭhā", "омрачённые явления", ""), ("asaṃkiliṭṭhā", "неомрачённые явления", "")],
    "1-M2-78": [("kilesasampayuttā", "явления, связанные с омрачениями", ""),
                ("kilesavippayuttā", "явления, не связанные с омрачениями", "")],
    "1-M2-79": [("kilesā ceva saṃkilesikā ca", "явления, являющиеся омрачениями и подверженные омрачению", ""),
                ("saṃkilesikā ceva no ca kilesā", "явления, подверженные омрачению, но не являющиеся омрачениями", "")],
    "1-M2-80": [("kilesā ceva saṃkiliṭṭhā ca", "явления, являющиеся омрачениями и омрачённые", ""),
                ("saṃkiliṭṭhā ceva no ca kilesā", "явления, омрачённые, но не являющиеся омрачениями", "")],
    "1-M2-81": [("kilesā ceva kilesasampayuttā ca", "явления, являющиеся омрачениями и связанные с омрачениями", ""),
                ("kilesasampayuttā ceva no ca kilesā",
                 "явления, связанные с омрачениями, но не являющиеся омрачениями", "")],
    # Piṭṭhidukaṃ
    "1-M2-83": [("dassanena pahātabbā", "явления, устраняемые видением истины", ""),
                ("na dassanena pahātabbā", "явления, не устраняемые видением истины", "")],
    "1-M2-84": [("bhāvanāya pahātabbā", "явления, устраняемые развитием ума", ""),
                ("na bhāvanāya pahātabbā", "явления, не устраняемые развитием ума", "")],
    "1-M2-85": [("dassanena pahātabbahetukā", "явления, чьи корни устраняются видением истины", ""),
                ("na dassanena pahātabbahetukā", "явления, чьи корни не устраняются видением истины", "")],
    "1-M2-86": [("bhāvanāya pahātabbahetukā", "явления, чьи корни устраняются развитием ума", ""),
                ("na bhāvanāya pahātabbahetukā", "явления, чьи корни не устраняются развитием ума", "")],
    "1-M2-87": [("savitakkā", "явления с направленной мыслью", ""), ("avitakkā", "явления без направленной мысли", "")],
    "1-M2-88": [("savicārā", "явления с удержанием мысли", ""), ("avicārā", "явления без удержания мысли", "")],
    "1-M2-89": [("sappītikā", "явления с восторгом", ""), ("appītikā", "явления без восторга", "")],
    "1-M2-90": [("pītisahagatā", "явления, сопровождаемые восторгом", ""),
                ("na pītisahagatā", "явления, не сопровождаемые восторгом", "")],
    "1-M2-91": [("sukhasahagatā", "явления, сопровождаемые счастьем", ""),
                ("na sukhasahagatā", "явления, не сопровождаемые счастьем", "")],
    "1-M2-92": [("upekkhāsahagatā", "явления, сопровождаемые невозмутимостью", ""),
                ("na upekkhāsahagatā", "явления, не сопровождаемые невозмутимостью", "")],
    "1-M2-93": [("kāmāvacarā", "явления, относящиеся к миру чувственных желаний", ""),
                ("na kāmāvacarā", "явления, не относящиеся к миру чувственных желаний", "")],
    "1-M2-94": [("rūpāvacarā", "явления, относящиеся к миру форм", ""),
                ("na rūpāvacarā", "явления, не относящиеся к миру форм", "")],
    "1-M2-95": [("arūpāvacarā", "явления, относящиеся к миру без форм", ""),
                ("na arūpāvacarā", "явления, не относящиеся к миру без форм", "")],
    "1-M2-96": [("pariyāpannā", "явления, принадлежащие к кругам существования", ""),
                ("apariyāpannā", "явления, не принадлежащие к кругам существования", "")],
    "1-M2-97": [("niyyānikā", "явления, ведущие к освобождению", ""),
                ("aniyyānikā", "явления, не ведущие к освобождению", "")],
    "1-M2-98": [("niyatā", "предопределённые явления", ""), ("aniyatā", "непредопределённые явления", "")],
    "1-M2-99": [("sauttarā", "явления, над которыми есть высшее", ""),
                ("anuttarā", "явления, над которыми нет высшего", "")],
    "1-M2-100": [("saraṇā", "явления, сопряжённые с борьбой", ""), ("araṇā", "явления, свободные от борьбы", "")],
    # Suttantikadukamātikā: the «dhammā» pairs
    "1-M2-101": [("vijjābhāgino", "явления, причастные к истинному знанию", ""),
                 ("avijjābhāgino", "явления, причастные к неведению", "")],
    "1-M2-102": [("vijjūpamā", "явления, подобные молнии", ""), ("vajirūpamā", "явления, подобные алмазу", "")],
    "1-M2-103": [("bālā", "явления, свойственные глупцам", ""), ("paṇḍitā", "явления, свойственные мудрым", "")],
    "1-M2-104": [("kaṇhā", "тёмные явления", ""), ("sukkā", "светлые явления", "")],
    "1-M2-105": [("tapanīyā", "явления, причиняющие мучения", ""),
                 ("atapanīyā", "явления, не причиняющие мучений", "")],
    "1-M2-106": [("adhivacanā", "явления, являющиеся наименованиями", ""),
                 ("adhivacanapathā", "явления, являющиеся путями наименования", "")],
    "1-M2-107": [("nirutti", "явления, являющиеся выражениями", ""),
                 ("niruttipathā", "явления, являющиеся путями выражения", "")],
    "1-M2-108": [("paññatti", "явления, являющиеся обозначениями", ""),
                 ("paññattipathā", "явления, являющиеся путями обозначения", "")],
})

# Suttanta pairs without «dhammā»: sid -> ((pali a, ru a), (pali b, ru b)); line = "(а) Ru."
SUTTA_ITEMS = {
    "1-M2-109": (("nāmañca", "Умственное"), ("rūpañca", "Материальная форма")),
    "1-M2-110": (("avijjā ca", "Неведение"), ("bhavataṇhā ca", "Жажда существования")),
    "1-M2-111": (("bhavadiṭṭhi ca", "Воззрение о существовании"), ("vibhavadiṭṭhi ca", "Воззрение о несуществовании")),
    "1-M2-112": (("sassatadiṭṭhi ca", "Воззрение о вечности"), ("ucchedadiṭṭhi ca", "Воззрение об уничтожении")),
    "1-M2-113": (("antavā diṭṭhi ca", "Воззрение о конечности"), ("anantavā diṭṭhi ca", "Воззрение о бесконечности")),
    "1-M2-114": (("pubbantānudiṭṭhi ca", "Воззрение о прошлом"), ("aparantānudiṭṭhi ca", "Воззрение о будущем")),
    "1-M2-115": (("ahirikañca", "Бессовестность"), ("anottappañca", "Отсутствие страха перед дурным")),
    "1-M2-116": (("hirī ca", "Совестливость"), ("ottappañca", "Страх перед дурным")),
    "1-M2-117": (("dovacassatā ca", "Неспособность принимать наставления"),
                 ("pāpamittatā ca", "Дружба с дурными людьми")),
    "1-M2-118": (("sovacassatā ca", "Готовность принимать наставления"),
                 ("kalyāṇamittatā ca", "Дружба с добрыми людьми")),
    "1-M2-119": (("āpattikusalatā ca", "Умение разбираться в проступках"),
                 ("āpattivuṭṭhānakusalatā ca", "Умение разбираться в избавлении от проступков")),
    "1-M2-120": (("samāpattikusalatā ca", "Умение разбираться в медитативных достижениях"),
                 ("samāpattivuṭṭhānakusalatā ca", "Умение разбираться в выходе из медитативных достижений")),
    "1-M2-121": (("dhātukusalatā ca", "Умение разбираться в элементах"),
                 ("manasikārakusalatā ca", "Умение разбираться во внимании")),
    "1-M2-122": (("āyatanakusalatā ca", "Умение разбираться в сферах восприятия"),
                 ("paṭiccasamuppādakusalatā ca", "Умение разбираться в возникновении в зависимости от условий")),
    "1-M2-123": (("ṭhānakusalatā ca", "Умение разбираться в возможном"),
                 ("aṭṭhānakusalatā ca", "Умение разбираться в невозможном")),
    "1-M2-124": (("ajjavo ca", "Прямодушие"), ("maddavo ca", "Мягкость")),
    "1-M2-125": (("khanti ca", "Терпение"), ("soraccañca", "Кротость")),
    "1-M2-126": (("sākhalyañca", "Приветливость"),
                 ("paṭisanthāro ca", "Радушие " + spell("Ka.", "paṭisandhāro ca"))),
    "1-M2-127": (("indriyesu aguttadvāratā ca", "Неохранение врат чувств"),
                 ("bhojane amattaññutā ca", "Незнание меры в еде")),
    "1-M2-128": (("indriyesu guttadvāratā ca", "Охранение врат чувств"),
                 ("bhojane mattaññutā ca", "Знание меры в еде")),
    "1-M2-129": (("muṭṭhasaccañca", "Утрата осознанности"), ("asampajaññañca", "Отсутствие ясного понимания")),
    "1-M2-130": (("sati ca", "Осознанность"), ("sampajaññañca", "Ясное понимание")),
    "1-M2-131": (("paṭisaṅkhānabalañca", "Сила размышления"), ("bhāvanābalañca", "Сила развития ума")),
    "1-M2-132": (("samatho ca", "Успокоение"), ("vipassanā ca", "Прозрение")),
    "1-M2-133": (("samathanimittañca", "Признак успокоения"), ("paggāhanimittañca", "Признак напряжения сил")),
    "1-M2-134": (("paggāho ca", "Напряжение сил"), ("avikkhepo ca", "Отсутствие отвлечения")),
    "1-M2-135": (("sīlavipatti ca", "Испорченность нравственности"), ("diṭṭhivipatti ca", "Испорченность воззрения")),
    "1-M2-136": (("sīlasampadā ca", "Безупречность нравственности"), ("diṭṭhisampadā ca", "Безупречность воззрения")),
    "1-M2-137": (("sīlavisuddhi ca", "Чистота нравственности"), ("diṭṭhivisuddhi ca", "Чистота воззрения")),
    "1-M2-138": (("diṭṭhivisuddhi kho pana", "Чистота воззрения"),
                 ("yathādiṭṭhissa ca padhānaṃ", "И усилие того, кто следует своему воззрению")),
    "1-M2-139": (("saṃvego ca saṃvejaniyesu ṭhānesu", "Потрясённость в обстоятельствах, которые должны потрясать"),
                 ("saṃviggassa ca yoniso padhānaṃ", "И вдумчивое усилие того, кто потрясён")),
    "1-M2-140": (("asantuṭṭhitā ca kusalesu dhammesu", "Отсутствие довольства благими явлениями"),
                 ("appaṭivānitā ca padhānasmiṃ", "И непреклонность в усилии")),
    "1-M2-141": (("vijjā ca", "Истинное знание"), ("vimutti ca", "Освобождение")),
    "1-M2-142": (("khaye ñāṇaṃ", "Знание об уничтожении"), ("anuppāde ñāṇanti", "Знание о невозникновении")),
}

# closing lines appended after the item lines
CLOSINGS = {
    "1-M1-22": [f"{TIKA}."],
    "1-M2-13": [f"{CUULANTARA}."],
    "1-M2-68": [f"{MAHANTARA}."],
    "1-M2-82": None,   # kho pana pair, built below
    "1-M2-100": [f"{PITTHI}.", f"{ABHI_DUKA}."],
    "1-M2-142": [f"{SUTTA_DUKA} {reading('Syā.', 'suttantamātikā')}.", f"{MATIKA_DONE}."],
}
MATRIX_LINES["1-M2-82"] = [f"{LAB[0]} Среди явлений, не связанных с омрачениями, есть и подверженные омрачению.",
                           f"{LAB[1]} Есть и не подверженные омрачению.",
                           "Группа омрачений."]
EXTRA_NAMES += [("kilesavippayuttā saṃkilesikā", "явления, не связанные с омрачениями, но подверженные омрачению"),
                ("kilesavippayuttā asaṃkilesikā", "явления, не связанные с омрачениями и не подверженные омрачению")]

MATRIX_HEADINGS = {
    "1-M-0": f"### {H_MATIKA}",
    "1-M-1-0": f"#### {TIKA}",
    "1-M-2-0": f"#### {DUKA}",
    "1-M-2-1-0": f"##### {CLUSTERS['hetu']['heading']}",
    "1-M-2-2-0": f"##### {CUULANTARA}",
    "1-M-2-3-0": f"##### {CLUSTERS['asava']['heading']}",
    "1-M-2-4-0": f"##### {CLUSTERS['samyojana']['heading']}",
    "1-M-2-5-0": f"##### {CLUSTERS['gantha']['heading']}",
    "1-M-2-6-0": f"##### {CLUSTERS['ogha']['heading']}",
    "1-M-2-7-0": f"##### {CLUSTERS['yoga']['heading']}",
    "1-M-2-8-0": f"##### {CLUSTERS['nivarana']['heading']}",
    "1-M-2-9-0": f"##### {CLUSTERS['paramasa']['heading']}",
    "1-M-2-10-0": f"##### {MAHANTARA}",
    "1-M-2-11-0": f"##### {CLUSTERS['upadana']['heading']}",
    "1-M-2-12-0": "##### Группа омрачений",
    "1-M-2-13-0": f"##### {PITTHI}",
    "1-M-2-14-0": f"##### {SUTTA_DUKA}",
}


def matrix():
    m = dict((k, [v]) for k, v in MATRIX_HEADINGS.items())
    for sid, items in list(TRIADS.items()) + list(PAIRS.items()):
        lines = [f"{LAB[i]} {cap(ru)}{(' ' + var) if var else ''}." for i, (_, ru, var) in enumerate(items)]
        lines += CLOSINGS.get(sid) or []
        m[sid] = lines
    for sid, ((_, a), (_, b)) in SUTTA_ITEMS.items():
        m[sid] = [f"{LAB[0]} {a}.", f"{LAB[1]} {b}."] + (CLOSINGS.get(sid) or [])
    m.update(MATRIX_LINES)
    return m


# ================================================================== chapter 2 frames
TS = "в это время"                       # tasmiṃ samaye
OPEN_1 = ("В то время, когда возникает благой ум, относящийся к миру чувственных желаний, "
          "сопровождаемый радостью, связанный со знанием, имеющий объектом видимую форму, или звук, "
          "или запах, или вкус, или осязаемое, или объект ума, или что бы то ни было,")
# Yasmiṃ samaye kāmāvacaraṃ kusalaṃ cittaṃ uppannaṃ hoti somanassasahagataṃ ñāṇasampayuttaṃ
# rūpārammaṇaṃ vā … dhammārammaṇaṃ vā yaṃ yaṃ vā panārabbha,
OTHERS = ("какие бы другие нематериальные явления, возникшие в зависимости от условий, "
          "ни были в это время")
# ye vā pana tasmiṃ samaye aññepi atthi paṭiccasamuppannā arūpino dhammā
KUSALA_NAME = TRIADS["1-M1-1"][0][1]     # благие явления
Q_KUSALA = q_form(KUSALA_NAME)           # Katame dhammā kusalā?
A_KUSALA = a_form(KUSALA_NAME)           # ime dhammā kusalā.
CLOSE_OTHERS = f"Или же {OTHERS}, – {A_KUSALA}"   # Ye vā pana … dhammā – ime dhammā kusalā.

# the factor list of ^1-1, in order: (pali, russian nominative, variant)
FACTORS = [
    ("phasso", "контакт", ""), ("vedanā", "чувство", ""), ("saññā", "восприятие", ""),
    ("cetanā", "намерение", ""), ("cittaṃ", "ум", ""), ("vitakko", "направленная мысль", ""),
    ("vicāro", "удержание мысли", ""), ("pīti", "восторг", ""), ("sukhaṃ", "счастье", ""),
    ("cittassekaggatā", "однонаправленность ума", ""), ("saddhindriyaṃ", "способность веры", ""),
    ("vīriyindriyaṃ", "способность усердия", spell("Sī., Syā.", "viriyindriyaṃ")),
    ("satindriyaṃ", "способность осознанности", ""), ("samādhindriyaṃ", "способность сосредоточения", ""),
    ("paññindriyaṃ", "способность мудрости", ""), ("manindriyaṃ", "способность ума", ""),
    ("somanassindriyaṃ", "способность радости", ""), ("jīvitindriyaṃ", "жизненная способность", ""),
    ("sammādiṭṭhi", "правильное воззрение", ""), ("sammāsaṅkappo", "правильный помысел", ""),
    ("sammāvāyāmo", "правильное усилие", ""), ("sammāsati", "правильная осознанность", ""),
    ("sammāsamādhi", "правильное сосредоточение", ""), ("saddhābalaṃ", "сила веры", ""),
    ("vīriyabalaṃ", "сила усердия", spell("Sī., Syā.", "viriyabalaṃ")),
    ("satibalaṃ", "сила осознанности", ""), ("samādhibalaṃ", "сила сосредоточения", ""),
    ("paññābalaṃ", "сила мудрости", ""), ("hiribalaṃ", "сила совестливости", ""),
    ("ottappabalaṃ", "сила страха перед дурным", ""), ("alobho", "отсутствие жадности", ""),
    ("adoso", "отсутствие злобы", ""), ("amoho", "отсутствие заблуждения", ""),
    ("anabhijjhā", "отсутствие алчности", ""), ("abyāpādo", "отсутствие недоброжелательности", ""),
    ("sammādiṭṭhi", "правильное воззрение", ""), ("hirī", "совестливость", ""),
    ("ottappaṃ", "страх перед дурным", ""),
    ("kāyapassaddhi", "безмятежность умственного тела", spell("Syā.", "kāyappassaddhi")),
    ("cittapassaddhi", "безмятежность ума", spell("Syā.", "cittappassaddhi")),
    ("kāyalahutā", "лёгкость умственного тела", ""), ("cittalahutā", "лёгкость ума", ""),
    ("kāyamudutā", "мягкость умственного тела", ""), ("cittamudutā", "мягкость ума", ""),
    ("kāyakammaññatā", "работоспособность умственного тела", ""),
    ("cittakammaññatā", "работоспособность ума", ""),
    ("kāyapāguññatā", "натренированность умственного тела", ""),
    ("cittapāguññatā", "натренированность ума", ""),
    ("kāyujukatā", "прямота умственного тела", spell("Sī., Ka.", "kāyujjukatā")),
    ("cittujukatā", "прямота ума", spell("Sī., Ka.", "cittujjukatā")),
    ("sati", "осознанность", ""), ("sampajaññaṃ", "ясное понимание", ""), ("samatho", "успокоение", ""),
    ("vipassanā", "прозрение", ""), ("paggāho", "напряжение сил", ""), ("avikkhepo", "отсутствие отвлечения", ""),
]
FN = {p: r for p, r, _ in FACTORS}       # factor name lookup


def factor_list():
    """tasmiṃ samaye phasso hoti, vedanā hoti, … avikkhepo hoti"""
    parts = [f"есть {r}{(' ' + v) if v else ''}" for _, r, v in FACTORS]
    return f"{TS} " + ", ".join(parts)


SEG_1_1 = f"{Q_KUSALA} {OPEN_1} {factor_list()}; или же {OTHERS}, – {A_KUSALA}"

# ---- fixed synonym strings (S): what follows «Yo/Yā/Yaṃ tasmiṃ samaye» up to the dash
TAJJA = "рождённ{} контактом соответствующего элемента умственного сознания"   # tajjāmanoviññāṇadhātusamphassaj-
S_PHASSA = "контакт, касание, соприкосновение, состояние соприкосновения"
S_SUKHA = ("душевная отрада, душевное счастье, рождённое контактом ума отрадное приятное переживание, "
           "рождённое контактом ума отрадное приятное чувство")
S_VEDANA = TAJJA.format("ая") + " " + S_SUKHA
S_SANNA = TAJJA.format("ое") + " восприятие, узнавание, состояние узнавания"
S_CETANA = (TAJJA.format("ое") + " намерение, проявление намерения, состояние намеренности "
            + reading("Syā.", "sañcetayitattaṃ"))
S_CITTA = ("ум, разум, умственная деятельность, сердце, чистота, разум, сфера ума, способность ума, "
           "сознание, совокупность сознания, соответствующий элемент умственного сознания")
S_VITAKKA = ("мышление, направленная мысль, помысел, прикрепление мысли, усиленное прикрепление мысли, "
             "направление ума на объект, правильный помысел")
S_VICARA = ("движение мысли, удержание мысли, последовательное удержание мысли, пристальное удержание мысли, "
            "непрерывная связь ума с объектом, неотрывное наблюдение за объектом")
S_PITI = ("восторг, ликование, веселье, оживление, весёлость, бурная весёлость, удовлетворённость, "
          "воодушевление, довольство ума")
S_SAMADHI = ("устойчивость ума, собранность, стабильность, отсутствие рассеяния, отсутствие отвлечения, "
             "нерассеянность ума, успокоение, способность сосредоточения, сила сосредоточения, "
             "правильное сосредоточение")
S_SADDHA = "вера, доверие, уверенность, глубокая убеждённость, вера, способность веры, сила веры"


def s_viriya(var=False):
    a = " " + spell("Sī., Syā.", "viriyārambho") if var else ""
    b = " " + spell("Sī.", "ussoḷhi") if var else ""
    return (f"душевное приложение усердия{a}, порыв, напор, старание, усилие, рвение, упорство{b}, "
            "стойкость, твёрдость, неослабевающий напор, неотступное желание, неотступное несение бремени, "
            "крепкое удержание бремени, усердие, способность усердия, сила усердия, правильное усилие")


S_VIRIYA = s_viriya()
S_VIRIYA_VAR = s_viriya(True)            # ^1-13 only
S_SATI = ("осознанность, припоминание, воспоминание, осознанность, способность помнить, "
          "способность удерживать в памяти, отсутствие поверхностности, отсутствие забывчивости, "
          "осознанность, способность осознанности, сила осознанности, правильная осознанность")
S_PANNA = ("мудрость, понимание, исследование, тщательное исследование, исследование явлений, различение, "
           "распознавание, точное распознавание, учёность, умелость, тонкость, ясность суждения, размышление, "
           "проверка, широта ума, разумность, руководящая сила, прозрение, ясное понимание, стрекало, "
           "мудрость, способность мудрости, сила мудрости, меч мудрости, башня мудрости, свет мудрости, "
           "сияние мудрости, светоч мудрости, сокровище мудрости, отсутствие заблуждения, "
           "исследование явлений, правильное воззрение")
S_JIVITA = ("срок жизни, сохранение, поддержание, продление, движение " + spell("Sī.", "irīyanā")
            + ", течение, сбережение, жизнь, жизненная способность")
S_ALOBHA = ("отсутствие жадности, отсутствие проявления жадности, отсутствие состояния жадности, "
            "отсутствие пристрастия, отсутствие проявления страсти, отсутствие состояния страсти, "
            "отсутствие алчности, отсутствие жадности как благой корень")


def s_adosa(var=False):
    v = " " + reading("Syā.", "adūsanā adūsitattaṃ") if var else ""
    return (f"отсутствие злобы, отсутствие проявления злобы, отсутствие состояния злобы{v}, "
            "отсутствие недоброжелательности, отсутствие неприязни, отсутствие злобы как благой корень")


S_ADOSA = s_adosa()
S_ADOSA_VAR = s_adosa(True)              # ^1-33 only
S_AMOHA = S_PANNA + ", отсутствие заблуждения как благой корень"
HIRI_BODY = ("То, что в это время стыдятся того, чего следует стыдиться, "
             "стыдятся допускать в себе дурные неблагие явления")
OTTAPPA_BODY = ("То, что в это время боятся того, чего следует бояться, "
                "боятся допускать в себе дурные неблагие явления")
KAYA_GEN = "у совокупности чувств, совокупности восприятия и совокупности формирующих факторов"
CITTA_GEN = "у совокупности сознания"


def s_passaddhi(var=False):
    v = (lambda w: " " + spell("Sī., Syā.", w)) if var else (lambda w: "")
    return (f"безмятежность, полная безмятежность{v('paṭippassaddhi')}, утихание, "
            f"полное утихание{v('paṭippassambhanā')}, состояние полного утихания{v('paṭippassambhitattaṃ')}")


S_PASSADDHI = s_passaddhi()
S_PASSADDHI_VAR = s_passaddhi(True)      # ^1-40 only
S_LAHUTA = "лёгкость, быстрота перемен, отсутствие медлительности, отсутствие скованности"
S_MUDUTA = "мягкость, гибкость, отсутствие грубости, отсутствие жёсткости"
S_KAMMANNATA = "работоспособность, состояние работоспособности, свойство работоспособности"
S_PAGUNATA = "натренированность, состояние натренированности, свойство натренированности"
S_UJUKATA = "прямизна, прямота, отсутствие кривизны, отсутствие изогнутости, отсутствие извилистости"


def body(s, gen=None):
    """Yo/Yā/Yaṃ tasmiṃ samaye [X-khandhassa] S"""
    return f"То, что {TS} {gen + ' ' if gen else ''}есть {s}"


def definition(factor, bod):
    """Katamo tasmiṃ samaye F hoti? <body> – ayaṃ/idaṃ tasmiṃ samaye F hoti."""
    f = FN[factor]
    return f"Что такое {f} {TS}? {bod}, – это {f} {TS}."


def kaya(s):
    return body(s, KAYA_GEN)


def citta(s):
    return body(s, CITTA_GEN)


SAMPLE_DEFS = [   # (sid, factor, body)
    ("1-2", "phasso", body(S_PHASSA)),
    ("1-3", "vedanā", body(S_VEDANA)),
    ("1-4", "saññā", body(S_SANNA)),
    ("1-5", "cetanā", body(S_CETANA)),
    ("1-6", "cittaṃ", body(S_CITTA)),
    ("1-7", "vitakko", body(S_VITAKKA)),
    ("1-8", "vicāro", body(S_VICARA)),
    ("1-9", "pīti", body(S_PITI)),
    ("1-10", "sukhaṃ", body(S_SUKHA)),
    ("1-11", "cittassekaggatā", body(S_SAMADHI)),
    ("1-12", "saddhindriyaṃ", body(S_SADDHA)),
    ("1-13", "vīriyindriyaṃ", body(S_VIRIYA_VAR)),
    ("1-14", "satindriyaṃ", body(S_SATI)),
    ("1-15", "samādhindriyaṃ", body(S_SAMADHI)),
    ("1-16", "paññindriyaṃ", body(S_PANNA)),
    ("1-17", "manindriyaṃ", body(S_CITTA)),
    ("1-18", "somanassindriyaṃ", body(S_SUKHA)),
    ("1-19", "jīvitindriyaṃ", f"То, что у этих нематериальных явлений есть {S_JIVITA}"),
    ("1-20", "sammādiṭṭhi", body(S_PANNA)),
    ("1-21", "sammāsaṅkappo", body(S_VITAKKA)),
    ("1-22", "sammāvāyāmo", body(S_VIRIYA)),
    ("1-23", "sammāsati", body(S_SATI)),
    ("1-24", "sammāsamādhi", body(S_SAMADHI)),
    ("1-25", "saddhābalaṃ", body(S_SADDHA)),
    ("1-26", "vīriyabalaṃ", body(S_VIRIYA)),
    ("1-27", "satibalaṃ", body(S_SATI)),
    ("1-28", "samādhibalaṃ", body(S_SAMADHI)),
    ("1-29", "paññābalaṃ", body(S_PANNA)),
    ("1-30", "hiribalaṃ", HIRI_BODY),
    ("1-31", "ottappabalaṃ", OTTAPPA_BODY),
    ("1-32", "alobho", body(S_ALOBHA)),
    ("1-33", "adoso", body(S_ADOSA_VAR)),   # Pāli ends «hoti?»: kept as written (user 2026-11-14), see seg()
    ("1-34", "amoho", body(S_AMOHA)),
    ("1-35", "anabhijjhā", body(S_ALOBHA)),
    ("1-36", "abyāpādo", body(S_ADOSA)),
    ("1-37", "sammādiṭṭhi", body(S_PANNA)),
    ("1-38", "hirī", HIRI_BODY),
    ("1-39", "ottappaṃ", OTTAPPA_BODY),
    ("1-40", "kāyapassaddhi", kaya(S_PASSADDHI_VAR)),
    ("1-41", "cittapassaddhi", citta(S_PASSADDHI)),
    ("1-42", "kāyalahutā", kaya(S_LAHUTA)),
    ("1-43", "cittalahutā", citta(S_LAHUTA)),
    ("1-44", "kāyamudutā", kaya(S_MUDUTA)),
    ("1-45", "cittamudutā", citta(S_MUDUTA)),
    ("1-46", "kāyakammaññatā", kaya(S_KAMMANNATA)),
    ("1-47", "cittakammaññatā", citta(S_KAMMANNATA)),
    ("1-48", "kāyapāguññatā", kaya(S_PAGUNATA)),
    ("1-49", "cittapāguññatā", citta(S_PAGUNATA)),
    ("1-50", "kāyujukatā", kaya(S_UJUKATA)),
    ("1-51", "cittujukatā", citta(S_UJUKATA)),
    ("1-52", "sati", body(S_SATI)),
    ("1-53", "sampajaññaṃ", body(S_PANNA)),
    ("1-54", "samatho", body(S_SAMADHI)),
    ("1-55", "vipassanā", body(S_PANNA)),
    ("1-56", "paggāho", body(S_VIRIYA)),
]


def sample():
    s = {
        "1-1-0": [f"### {CH_HEADINGS['Cittuppādakaṇḍaṃ']}"],
        "1-1-1-0": [f"#### {H_KAMA_KUSALA}"],
        "1-1-1-1-0": [f"##### {H_PADABHAJANI}"],
        "1-1": [SEG_1_1],
    }
    for sid, f, b in SAMPLE_DEFS:
        s[sid] = [definition(f, b)]
    # user 2026-11-14: translate the source as written; the Pāli of ^1-33 ends «adoso hoti?»
    s["1-33"] = [s["1-33"][0][:-1] + "?"]
    s["1-57"] = [definition("avikkhepo", body(S_SAMADHI)), CLOSE_OTHERS,
                 f"{H_PADABHAJANI}.", f"{BHANAVARA_1}."]
    return s


PREAMBLE = {"T-1": [HOMAGE], "0": [f"# {H_PITAKA}"], "1-0": [f"## {H_BOOK}"]}


# ================================================================== output
def segments(path):
    out, buf = [], []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        buf.append(line)
        m = ID.search(line)
        if m:
            out.append((m.group(1), buf))
            buf = []
    assert not buf, f"lines without id in {path}"
    return out


def emit(pali_path, ru, target):
    segs = segments(pali_path)
    ids = [i for i, _ in segs]
    assert set(ids) == set(ru), (sorted(set(ids) - set(ru))[:10], sorted(set(ru) - set(ids))[:10])
    blocks = []
    for sid, plines in segs:
        rlines = list(ru[sid])
        assert len(plines) == len(rlines), (sid, len(plines), len(rlines))
        for a, b in zip(plines, rlines):
            assert len(a) - len(a.lstrip("#")) == len(b) - len(b.lstrip("#")), sid
            assert a.count("–") + a.count("—") == b.count("–") + b.count("—"), ("dash", sid)
        rlines[-1] = f"{rlines[-1]} ^{sid}"
        blocks.append("\n".join(rlines))
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text("\n\n".join(blocks) + "\n", encoding="utf-8", newline="\n")
    print("wrote", target, len(blocks), "segments")


def formulas():
    L = ["# pi-1 Dhammasaṅgaṇī: Russian rails sentence formulas (binding for chapter agents)", "",
         "Format: Pāli = Russian, one per line. Generated by build_rails_sample_ru.py; import its constants "
         "rather than retyping. Termbase: AI_translation/russian/pi-1-pali-russian-termbase-plain.md.", "",
         "## Text frame and headings", "",
         f"Namo tassa bhagavato arahato sammāsambuddhassa = {HOMAGE}",
         f"# Abhidhammapiṭake = # {H_PITAKA}",
         f"## Dhammasaṅgaṇīpāḷi = ## {H_BOOK} (mid-sentence: «{H_BOOK}»)",
         f"### Mātikā = ### {H_MATIKA}",
         f"#### Tikamātikā = #### {TIKA}",
         f"Tikamātikā. (closing line) = {TIKA}.",
         f"#### Dukamātikā = #### {DUKA}",
         f"Abhidhammadukamātikā. (closing line) = {ABHI_DUKA}.",
         f"##### Suttantikadukamātikā = ##### {SUTTA_DUKA}",
         f"Suttantikadukamātikā [suttantamātikā (syā.)]. = {SUTTA_DUKA} {reading('Syā.', 'suttantamātikā')}.",
         f"Mātikā niṭṭhitā. = {MATIKA_DONE}.",
         f"##### Cūḷantaradukaṃ / Cūḷantaradukaṃ. = ##### {CUULANTARA} / {CUULANTARA}.",
         f"##### Mahantaradukaṃ / Mahantaradukaṃ. = ##### {MAHANTARA} / {MAHANTARA}.",
         f"##### Piṭṭhidukaṃ / Piṭṭhidukaṃ. = ##### {PITTHI} / {PITTHI}.",
         ]
    for c in CLUSTERS.values():
        L.append(f"##### {c['p_heading']} / {c['p_heading']}. = ##### {c['heading']} / {c['heading']}.")
    L.append("##### Kilesagocchakaṃ / Kilesagocchakaṃ. = ##### Группа омрачений / Группа омрачений.")
    for p, r in CH_HEADINGS.items():
        L.append(f"### {p} = ### {r}")
    L += [f"#### Kāmāvacarakusalaṃ = #### {H_KAMA_KUSALA}",
          f"##### Padabhājanī = ##### {H_PADABHAJANI}",
          f"Padabhājanīyaṃ. (closing line) = {H_PADABHAJANI}.",
          f"Paṭhamabhāṇavāro. = {BHANAVARA_1}.",
          "", "## Line labels, variants, punctuation", "",
          "(Ka) / (Kha) / (Ga) = (а) / (б) / (в)",
          "[word (sī. syā.)] spelling only = [вариант написания (Sī., Syā.): word] (sigla capitalised, comma-separated)",
          "[word (syā.)] different word or wording = [вариант чтения (Syā.): word]",
          "…pe… = … (same spot)",
          "– (Pāli dash) = – (same spot, same count; never add one). Before it the Russian clause closes with a comma: «…, – это …»",
          "Statements end with «.», questions with «?», never «ли».",
          "X ceva … Y ca (both) = X и Y;  X ceva … na/no ca Y (but not) = X, но не Y",
          "X kho pana dhammā Y-pi. / Z-pi. (matrix) = (а) Среди явлений, X(gen.), есть и Y. / (б) Есть и Z.",
          "vipāka/vipākā as a class of phenomena = являющиеся результатом действий",
          "kāya- in kāyapassaddhi etc. = умственное тело (gen. умственного тела)",
          "", "## Question and answer frames", "",
          "Katame dhammā X? = Что такое X? (X = matrix name below, in lower case, without its variant bracket)",
          "– ime dhammā X. = – это X.",
          f"Katame dhammā kusalā? = {Q_KUSALA}",
          f"– ime dhammā kusalā. = – {A_KUSALA}",
          f"Yasmiṃ samaye kāmāvacaraṃ kusalaṃ cittaṃ uppannaṃ hoti somanassasahagataṃ ñāṇasampayuttaṃ "
          f"rūpārammaṇaṃ vā saddārammaṇaṃ vā gandhārammaṇaṃ vā rasārammaṇaṃ vā phoṭṭhabbārammaṇaṃ vā "
          f"dhammārammaṇaṃ vā yaṃ yaṃ vā panārabbha, = {OPEN_1}",
          "Yasmiṃ samaye … cittaṃ uppannaṃ hoti = В то время, когда возникает … ум",
          f"tasmiṃ samaye = {TS}",
          f"tasmiṃ samaye F hoti, G hoti, … = {TS} есть F, есть G, … (nominative; «есть» before every factor)",
          f"ye vā pana tasmiṃ samaye aññepi atthi paṭiccasamuppannā arūpino dhammā = или же {OTHERS}",
          f"; ye vā pana … – ime dhammā kusalā. (end of ^1-1) = ; или же {OTHERS}, – {A_KUSALA}",
          f"Ye vā pana … – ime dhammā kusalā. (own line, ^1-57) = {CLOSE_OTHERS}",
          "", "## Definition formulas (chapter 2)", "",
          f"Katamo/Katamā/Katamaṃ tasmiṃ samaye F hoti? = Что такое F {TS}?",
          f"Yo/Yā/Yaṃ tasmiṃ samaye S – = То, что {TS} есть S, –",
          f"ayaṃ/idaṃ tasmiṃ samaye F hoti. = это F {TS}.",
          f"Yā tasmiṃ samaye vedanākkhandhassa saññākkhandhassa saṅkhārakkhandhassa S – = То, что {TS} {KAYA_GEN} есть S, –",
          f"Yā tasmiṃ samaye viññāṇakkhandhassa S – = То, что {TS} {CITTA_GEN} есть S, –",
          "Yo tesaṃ arūpīnaṃ dhammānaṃ S – = То, что у этих нематериальных явлений есть S, –",
          f"Yaṃ tasmiṃ samaye hirīyati hiriyitabbena hirīyati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā – = {HIRI_BODY}, –",
          f"Yaṃ tasmiṃ samaye ottappati ottappitabbena ottappati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā – = {OTTAPPA_BODY}, –",
          "alobho/adoso/amoho kusalamūlaṃ = отсутствие жадности/злобы/заблуждения как благой корень",
          f"Example ^1-2 = {definition('phasso', body(S_PHASSA))}",
          "", "## Factor names (nominative, ^1-1 order)", ""]
    seen = set()
    for p, r, v in FACTORS:
        if p in seen:
            continue
        seen.add(p)
        L.append(f"{p} = {r}" + (f"  (^1-1 variant: {v})" if v else ""))
    L += ["", "## Fixed synonym strings", "",
          f"phasso phusanā saṃphusanā saṃphusitattaṃ = {S_PHASSA}",
          f"tajjāmanoviññāṇadhātusamphassajaṃ cetasikaṃ sātaṃ cetasikaṃ sukhaṃ cetosamphassajaṃ sātaṃ sukhaṃ vedayitaṃ cetosamphassajā sātā sukhā vedanā = {S_VEDANA}",
          f"cetasikaṃ sātaṃ cetasikaṃ sukhaṃ cetosamphassajaṃ sātaṃ sukhaṃ vedayitaṃ cetosamphassajā sātā sukhā vedanā = {S_SUKHA}",
          f"tajjāmanoviññāṇadhātusamphassajā saññā sañjānanā sañjānitattaṃ = {S_SANNA}",
          f"tajjāmanoviññāṇadhātusamphassajā cetanā sañcetanā cetayitattaṃ [sañcetayitattaṃ (syā.)] = {S_CETANA}",
          f"cittaṃ mano mānasaṃ hadayaṃ paṇḍaraṃ mano manāyatanaṃ manindriyaṃ viññāṇaṃ viññāṇakkhandho tajjāmanoviññāṇadhātu = {S_CITTA}",
          "mano inside this citta string = разум (termbase sense «intellect»); elsewhere mano = ум",
          f"takko vitakko saṅkappo appanā byappanā cetaso abhiniropanā sammāsaṅkappo = {S_VITAKKA}",
          f"cāro vicāro anuvicāro upavicāro cittassa anusandhānatā anupekkhanatā = {S_VICARA}",
          f"pīti pāmojjaṃ āmodanā pamodanā hāso pahāso vitti odagyaṃ attamanatā cittassa = {S_PITI}",
          f"cittassa ṭhiti saṇṭhiti avaṭṭhiti avisāhāro avikkhepo avisāhaṭamānasatā samatho samādhindriyaṃ samādhibalaṃ sammāsamādhi = {S_SAMADHI}",
          f"saddhā saddahanā okappanā abhippasādo saddhā saddhindriyaṃ saddhābalaṃ = {S_SADDHA}",
          f"cetasiko vīriyārambho nikkamo parakkamo uyyāmo vāyāmo ussāho ussoḷhī thāmo dhiti asithilaparakkamatā anikkhittachandatā anikkhittadhuratā dhurasampaggāho vīriyaṃ vīriyindriyaṃ vīriyabalaṃ sammāvāyāmo = {S_VIRIYA}",
          f"(^1-13 with variants) = {S_VIRIYA_VAR}",
          f"sati anussati paṭissati sati saraṇatā dhāraṇatā apilāpanatā asammussanatā sati satindriyaṃ satibalaṃ sammāsati = {S_SATI}",
          f"paññā pajānanā vicayo pavicayo dhammavicayo sallakkhaṇā upalakkhaṇā paccupalakkhaṇā paṇḍiccaṃ kosallaṃ nepuññaṃ vebhabyā cintā upaparikkhā bhūrī medhā pariṇāyikā vipassanā sampajaññaṃ patodo paññā paññindriyaṃ paññābalaṃ paññāsatthaṃ paññāpāsādo paññāāloko paññāobhāso paññāpajjoto paññāratanaṃ amoho dhammavicayo sammādiṭṭhi = {S_PANNA}",
          f"… sammādiṭṭhi amoho kusalamūlaṃ (the amoho definition) = {S_AMOHA}",
          f"āyu ṭhiti yapanā yāpanā iriyanā [irīyanā (sī.)] vattanā pālanā jīvitaṃ jīvitindriyaṃ = {S_JIVITA}",
          f"alobho alubbhanā alubbhitattaṃ asārāgo asārajjanā asārajjitattaṃ anabhijjhā alobho kusalamūlaṃ = {S_ALOBHA}",
          f"adoso adussanā adussitattaṃ abyāpādo abyāpajjo adoso kusalamūlaṃ = {S_ADOSA}",
          f"(^1-33 with variant) = {S_ADOSA_VAR}",
          f"passaddhi paṭipassaddhi passambhanā paṭipassambhanā paṭipassambhitattaṃ = {S_PASSADDHI}",
          f"(^1-40 with variants) = {S_PASSADDHI_VAR}",
          f"lahutā lahupariṇāmatā adandhanatā avitthanatā = {S_LAHUTA}",
          f"mudutā maddavatā akakkhaḷatā akathinatā = {S_MUDUTA}",
          f"kammaññatā kammaññattaṃ kammaññabhāvo = {S_KAMMANNATA}",
          f"paguṇatā paguṇattaṃ paguṇabhāvo = {S_PAGUNATA}",
          f"ujutā ujukatā ajimhatā avaṅkatā akuṭilatā = {S_UJUKATA}",
          "", "## Matrix names with question and answer forms", "",
          "Matrix line = (а)/(б)/(в) + name with capital letter + variant + «.»", ""]
    for sid, items in list(TRIADS.items()) + list(PAIRS.items()):
        for p, r, var in items:
            dh = "dhammā " + p if "ceva" in p else p + " dhammā"
            if "ceva" in p:     # matrix word order: X ceva dhammā Y ca
                x, rest = p.split(" ceva ", 1)
                dh = f"{x} ceva dhammā {rest}"
            L.append(f"{dh} [{sid}] = {cap(r)}" + (f" {var}" if var else ""))
            L.append(f"Katame dhammā {p}? = {q_form(r)}")
            L.append(f"ime dhammā {p}. = {a_form(r)}")
    L += ["", "### Names used only in later chapters (the «kho pana» pairs)", ""]
    for p, r in EXTRA_NAMES:
        L.append(f"Katame dhammā {p}? = {q_form(r)}")
        L.append(f"ime dhammā {p}. = {a_form(r)}")
    L += ["", "### Suttanta items without «dhammā»", ""]
    for sid, ((pa, ra), (pb, rb)) in SUTTA_ITEMS.items():
        L.append(f"{pa} [{sid}] = {ra}")
        L.append(f"{pb} [{sid}] = {rb}")
    L += ["", "### «kho pana» matrix lines", ""]
    for sid in sorted(MATRIX_LINES, key=lambda s: int(s.split("-")[-1])):
        L.append(f"[{sid}] = " + " / ".join(MATRIX_LINES[sid]))
    return "\n".join(L) + "\n"


def main():
    emit(PALI / "preamble.md", PREAMBLE, OUT / "preamble.md")
    emit(PALI / "1-matika.md", matrix(), OUT / "1-matika.md")
    emit(PIPE / "ref" / "ch2-01-pali-1-122.md", sample(), RAILS / "sample-2-01" / "2-01-sample.md")
    (RAILS / "ru-rails-formulas.md").write_text(formulas(), encoding="utf-8", newline="\n")
    print("wrote", RAILS / "ru-rails-formulas.md")


if __name__ == "__main__":
    main()
