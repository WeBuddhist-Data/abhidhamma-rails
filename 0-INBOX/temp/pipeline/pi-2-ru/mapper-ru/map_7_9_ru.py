"""Build the Pāli->Russian keyword maps for pi-2 (Vibhaṅga) chapters 7-satipatthanavibhango,
8-sammappadhanavibhango and 9-iddhipadavibhango.

usage: python -I -X utf8 map_7_9_ru.py [PART ...]           (writes <part>.mapped.md and verifies; default: all three,
                                                            in book order)
       python -I -X utf8 map_7_9_ru.py --dump PART [--miss]  (prints every keyword=value with a presence flag;
                                                            --miss: only the flagged ones; no writing)

Resolution order per keyword: OVERRIDES[bid][kw]  ->  context rules (resolve())  ->  T (this file: map_6_ru.T + the
chapter 7-9 additions)  ->  pi-1 CH2 / MATRIX.
Conventions: ru-map-conventions-pi2.md (+ the pi-1 file), notes-map-2-3.md, notes-map-4-5.md, notes-map-6.md; new
decisions: notes-map-7-9.md.
"""
import pathlib
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import map_6_ru as M6  # noqa: E402  (read-only: its table T, EXC)
import map_4_5_ru as M45  # noqa: E402  (read-only: _DUKA, CHOICES)
from map_common_pi2_ru import (GAP, NDE, build_part, hetuko_value, lc, present,  # noqa: E402,F401
                               read_keywords, read_pali, read_russian, value, verify)

PARTS = ["7-satipatthanavibhango", "8-sammappadhanavibhango", "9-iddhipadavibhango"]

# ---------------------------------------------------------------------------- table
T = dict(M6.T)
assert not any(v.startswith("классификация") for v in T.values())

T.update({
    # ================================================================ ch. 7 Satipaṭṭhāna
    # ---- headings / frame
    "satipaṭṭhāna": "основа осознанности", "paṭṭhāna": "основа",
    "satipaṭṭhānavibhaṅgo": "разбор основ осознанности",
    "satipaṭṭhānā": "основы осознанности", "paṭṭhānā": "основы",
    "satipaṭṭhānaṃ": "основа осознанности", "paṭṭhānaṃ": "основа",
    "satipaṭṭhānānaṃ": "основы осознанности", "paṭṭhānānaṃ": "основы",
    "ānupassanā": "созерцание", "anupassanā": "созерцание", "ānupassanāniddeso": "разъяснение созерцания",
    "kāyānupassanā": "созерцание тела", "kāyānupassanāniddeso": "разъяснение созерцания тела",
    "vedanānupassanā": "созерцание чувств", "vedanānupassanāniddeso": "разъяснение созерцания чувств",
    "cittānupassanā": "созерцание ума", "cittānupassanāniddeso": "разъяснение созерцания ума",
    "dhammānupassanā": "созерцание явлений", "dhammānupassanāniddeso": "разъяснение созерцания явлений",
    # ---- «пребывает во внутреннем теле, созерцая тело …» (ch. 4 2-205 pattern)
    "anupassī": "созерцающий", "vedanānupassī": "созерцающий чувства", "cittānupassī": "созерцающий ум",
    "dhammānupassī": "созерцающий явления",
    "vedanānupassī viharati": "пребывать" + GAP + "созерцающий чувства",
    "cittānupassī viharati": "пребывать" + GAP + "созерцающий ум",
    "dhammānupassī viharati": "пребывать" + GAP + "созерцающий явления",
    "vedanāsu vedanānupassī": "в чувствах созерцающий чувства",
    "ajjhattaṃ kāye": "внутреннее тело", "bahiddhā kāye": "внешнее тело",
    "ajjhattabahiddhā kāye": "внутреннее и внешнее тело",
    "ajjhattaṃ vedanāsu": "внутренние чувства", "bahiddhā vedanāsu": "внешние чувства",
    "ajjhattabahiddhā vedanāsu": "внутренние и внешние чувства",
    "citte": "ум", "ajjhattaṃ citte": "внутренний ум", "bahiddhā citte": "внешний ум",
    "ajjhattabahiddhā citte": "внутренний и внешний ум",
    "bahiddhā dhammesu": "внешние явления", "ajjhattaṃ": "внутренний",
    "loke": "мир", "abhijjhādomanassaṃ": "алчность и уныние", "abhijjhādomanassa": "алчность и уныние",
    "loke abhijjhādomanassaṃ": "алчность и уныние в отношении мира",
    "loke abhijjhādomanassa": "алчность и уныние в отношении мира",
    # ---- the body (2-356): «рассматривает … от подошв ног вверх и от кончиков волос на голове вниз, ограниченное
    # кожей и полное разного рода нечистот»
    "talā": "подошва", "kesamatthakā": "кончики волос на голове", "matthakā": "кончик",
    "pariyantaṃ": "ограниченный", "pakārassa": "род", "asucino": "нечистота", "paccavekkhati": "рассматривать",
    "kāye kesā": "тело" + GAP + "волосы на голове", "atthissa": "его" + GAP + "есть", "mutta": "моча",
    # ---- «Этот признак он практикует, развивает, многократно повторяет, чётко устанавливает …»
    "āsevati": "практиковать", "āsevitvā": "практиковать", "bhāvetvā": "развить",
    "bahulīkaroti": "многократно повторять", "bahulīkaritvā": "многократно повторить",
    "vavatthapeti": "устанавливать", "vavatthapetvā": "установить",
    "taṃ nimittaṃ āsevati": "этот признак" + GAP + "практиковать",
    "taṃ nimittaṃ āsevitvā": "практиковать этот признак",
    "upasaṃharati": "направлять", "cittaṃ upasaṃharati": "направлять ум",
    # ---- definitions (2-357 … 2-361, 2-368 … 2-372)
    "upeto": "обладать", "samupeto": "вполне обладать", "upāgato": "снабжённый", "samupāgato": "вполне снабжённый",
    "upapanno": "обеспеченный", "sampanno": "оснащённый", "samannāgato": "наделённый",
    "iriyati": "принимать положения тела", "pāleti": "оберегать себя", "yapeti": "поддерживать себя",
    "yāpeti": "продлевать существование", "carati": "действовать", "viharatīti": "пребывать",
    "ātāpo": "ревностность", "vīriyārambho": "приложение усердия",
    # ---- loko / abhijjhā / domanassa (2-362 …): «устранены, полностью устранены, успокоены, усмирены,
    # умиротворены, угасли, полностью угасли, прекращены, полностью прекращены, иссушены, полностью иссушены,
    # сведены на нет»
    "kāyo": "тело", "vinītā": "устранённый", "paṭivinītā": "полностью устранённый", "santā": "успокоенный",
    "samitā": "усмирённый", "vūpasantā": "умиротворённый", "atthaṅgatā": "угаснуть",
    "abbhatthaṅgatā": "полностью угаснуть", "appitā": "прекращённый", "byappitā": "полностью прекращённый",
    "sositā": "иссушённый", "visositā": "полностью иссушённый", "byantīkatā": "сведённый на нет",
    # ---- feelings (2-363)
    "vedayamāno": "испытывать", "vedayāmī": "испытывать", "vedayatī": "испытывать", "pajānāti": "понимать",
    "sāmisaṃ": "плотский", "nirāmisaṃ": "неплотский",
    "sukhaṃ vedanaṃ": "приятное чувство", "dukkhaṃ vedanaṃ": "болезненное чувство",
    "sāmisaṃ sukhaṃ": "плотский приятный", "sāmisaṃ sukhaṃ vedanaṃ": "плотское приятное чувство",
    "nirāmisaṃ sukhaṃ": "неплотский приятный", "nirāmisaṃ sukhaṃ vedanaṃ": "неплотское приятное чувство",
    "sāmisaṃ dukkhaṃ": "плотский болезненный", "sāmisaṃ dukkhaṃ vedanaṃ": "плотское болезненное чувство",
    "nirāmisaṃ dukkhaṃ": "неплотский болезненный",
    "nirāmisaṃ dukkhaṃ vedanaṃ": "неплотское болезненное чувство",
    "vedanāsu cittaṃ": "ум" + GAP + "чувства",
    # ---- mind (2-365): «когда ум охвачен страстью …»
    "rāgaṃ": "страсть", "dosaṃ": "злоба", "mohaṃ": "заблуждение",
    "sarāgaṃ vā cittaṃ": "ум охваченный страстью", "vītarāgaṃ vā cittaṃ": "ум свободный от страсти",
    "sadosaṃ vā cittaṃ": "ум охваченный злобой", "vītadosaṃ vā cittaṃ": "ум свободный от злобы",
    "samohaṃ vā cittaṃ": "ум охваченный заблуждением", "vītamohaṃ vā cittaṃ": "ум свободный от заблуждения",
    "saṃkhittaṃ": "сжатый", "saṃkhittaṃ vā cittaṃ": "ум сжатый",
    "vikkhittaṃ": "рассеянный", "vikkhittaṃ vā cittaṃ": "ум рассеянный",
    "mahaggataṃ vā cittaṃ": "ум возвышенный",
    "amahaggataṃ": "невозвышенный", "amahaggataṃ vā cittaṃ": "ум невозвышенный",
    "sauttaraṃ": "имеющий над собой высшее", "sauttaraṃ vā cittaṃ": "ум имеющий над собой высшее",
    "anuttaraṃ": "не имеющий над собой высшего", "anuttaraṃ vā cittaṃ": "ум не имеющий над собой высшего",
    "samāhitaṃ": "сосредоточенный", "samāhitaṃ vā cittaṃ": "ум сосредоточенный",
    "asamāhitaṃ": "несосредоточенный", "asamāhitaṃ vā cittaṃ": "ум несосредоточенный",
    "vimuttaṃ": "освобождённый", "vimuttaṃ vā cittaṃ": "ум освобождённый",
    "avimuttaṃ": "неосвобождённый", "avimuttaṃ vā cittaṃ": "ум неосвобождённый",
    # ---- mental objects (2-367): «когда внутри него есть чувственное желание … понимает и то, как происходит
    # возникновение невозникшего …»
    "santaṃ": "есть", "kāmacchandaṃ": "чувственное желание", "byāpādaṃ": "недоброжелательность",
    "thinamiddhaṃ": "вялость и сонливость", "thina": "вялость", "middhaṃ": "сонливость",
    "uddhaccakukkuccaṃ": "беспокойство и угрызения", "uddhacca": "беспокойство", "kukkuccaṃ": "угрызения",
    "vicikicchaṃ": "колебание",
    "uppādo": "возникновение", "anuppādo": "не" + GAP + "возникновение",
    "uppannassa": "возникший", "anuppannassa": "невозникший", "pahīnassa": "устранённый",
    "uppannassa kāmacchandassa": "возникшее чувственное желание",
    "anuppannassa kāmacchandassa": "невозникшее чувственное желание",
    "pahīnassa kāmacchandassa": "устранённое чувственное желание",
    "uppannāya vicikicchāya": "возникшее колебание", "anuppannāya vicikicchāya": "невозникшее колебание",
    "pahīnāya vicikicchāya": "устранённое колебание",
    "uppannassa satisambojjhaṅgassa": "возникший фактор пробуждения осознанности",
    "anuppannassa satisambojjhaṅgassa": "невозникший фактор пробуждения осознанности",
    "kāmacchandassa uppādo": "возникновение" + GAP + "чувственного желания",
    "vicikicchāya uppādo": "возникновение" + GAP + "колебания",
    "anuppannāya vicikicchāya uppādo": "возникновение невозникшего колебания",
    "satisambojjhaṅgassa uppādo": "возникновение" + GAP + "фактора пробуждения осознанности",
    "upekkhāsambojjhaṅgassa uppādo": "возникновение" + GAP + "фактора пробуждения невозмутимости",
    "satisambojjhaṅgassa bhāvanāya pāripūrī":
        "завершённость развития" + GAP + "фактора пробуждения осознанности",
    "pāripūrī": "завершённость",
    "sambojjhaṅgaṃ": "фактор пробуждения", "satisambojjhaṅgaṃ": "фактор пробуждения осознанности",
    "dhammavicayasambojjhaṅgaṃ": "фактор пробуждения исследования явлений",
    "vīriyasambojjhaṅgaṃ": "фактор пробуждения усердия", "pītisambojjhaṅgaṃ": "фактор пробуждения восторга",
    "passaddhisambojjhaṅgaṃ": "фактор пробуждения безмятежности",
    "samādhisambojjhaṅgaṃ": "фактор пробуждения сосредоточения",
    "upekkhāsambojjhaṅgaṃ": "фактор пробуждения невозмутимости",
    "vicaya": "исследование", "dhammavicaya": "исследование явлений", "passaddhi": "безмятежность",
    # ---- pañhāpucchaka (2-388, 2-389)
    "apacayagāmino": "ведущий к убыванию", "aniyatā": "непредопределённый",
    "bahiddhārammaṇā": "имеющий внешний объект", "appamāṇārammaṇā": "имеющий безмерный объект",
    # ================================================================ ch. 8 Sammappadhāna
    "padhāna": "усилие", "sammappadhānavibhaṅgo": "разбор правильных усилий",
    "sammappadhānā": "правильные усилия", "padhānā": "усилия",
    "sammappadhānaṃ": "правильное усилие", "padhānaṃ": "усилие",
    "sammappadhānānaṃ": "правильные усилия", "padhānānaṃ": "усилия",
    # «ради невозникновения невозникших дурных неблагих явлений порождает желание, прилагает усилие, пробуждает
    # усердие, напрягает ум, прилагает старания» (pi-1 ^1-1377, ch. 4 2-205)
    "anuppannānaṃ": "невозникший", "cittaṃ paggaṇhāti": "напрягать ум", "vīriyaṃ ārabhati": "пробуждать усердие",
    "padahatīti": "прилагать старания", "paggaṇhātīti": "напрягать", "cittaṃ paggaṇhātīti": "напрягать ум",
    "janetīti": "порождать", "chandaṃ janetīti": "порождать желание", "ārabhatīti": "пробуждать",
    "vīriyaṃ ārabhatīti": "пробуждать усердие", "vāyamatīti": "прилагать усилие",
    # «Три неблагих корня – жадность, злоба, заблуждение. И омрачения, пребывающие вместе с ними. Связанные с ними …;
    # порождённые ими телесное действие, речевое действие и умственное действие» (pi-1 ^1-985 / ^1-986)
    "akusalamūlāni": "неблагие корни", "lobho": "жадность", "doso": "злоба", "ekaṭṭhā": "пребывающий вместе",
    "sampayutto": "связанный", "samuṭṭhānaṃ": "порождённый", "kāyakammaṃ": "телесное действие",
    "vacīkammaṃ": "речевое действие", "manokammaṃ": "умственное действие",
    # «То, что есть желание, проявление желания, желание действовать, благое стремление к Учению … Это желание он
    # порождает, полностью порождает, поднимает, полностью поднимает, вызывает, полностью вызывает»
    "chando": "желание", "chandikatā": "проявление желания", "kattu": "действовать", "kamyatā": "желание",
    "kusalo": "благой", "kusalo dhammacchando": "благое стремление к Учению",
    "imaṃ chandaṃ janeti": "это желание" + GAP + "порождать", "sañjaneti": "полностью порождать",
    "uṭṭhapeti": "поднимать", "samuṭṭhapeti": "полностью поднимать", "nibbatteti": "вызывать",
    "abhinibbatteti": "полностью вызывать",
    # «Это усердие он пробуждает, полностью пробуждает, практикует, развивает, многократно повторяет»
    "imaṃ vīriyaṃ ārabhati": "это усердие" + GAP + "пробуждать", "samārabhati": "полностью пробуждать",
    # «Этот ум он напрягает, полностью напрягает, поддерживает, всячески поддерживает»
    "imaṃ cittaṃ paggaṇhāti": "этот ум" + GAP + "напрягать", "sampaggaṇhāti": "полностью напрягать",
    "upatthambheti": "поддерживать", "paccupatthambheti": "всячески поддерживать",
    # «То, что есть сохранение, есть неутрата; … есть умножение; … есть обширность; … есть развитие; … есть
    # завершённость» (2-406, 2-420)
    "asammoso": "неутрата", "bhiyyobhāvo": "умножение", "vepullaṃ": "обширность",
    # ================================================================ ch. 9 Iddhipāda
    "iddhi": "сверхспособность", "pāda": "основа", "iddhipāda": "основа сверхспособностей",
    "iddhipādo": "основа сверхспособностей", "iddhipādaṃ": "основа сверхспособностей",
    "iddhipādā": "основы сверхспособностей", "pādā": "основы",
    "iddhipādānaṃ": "основы сверхспособностей", "pādānaṃ": "основы",
    "chandiddhipādo": "желание как основа сверхспособностей",
    "vīriyiddhipādo": "усердие как основа сверхспособностей",
    "cittiddhipādo": "ум как основа сверхспособностей",
    "vīmaṃsiddhipādo": "пытливость как основа сверхспособностей",
    # «развивает основу сверхспособностей, наделённую сосредоточением через желание и формирующим фактором усилия»
    "iddhipādaṃ bhāveti": "развивать основу сверхспособностей",
    "iddhipādaṃ bhāvetī": "развивать основу сверхспособностей",
    "samannāgataṃ": "наделённый", "samannāgataṃ iddhipādaṃ": "основа сверхспособностей наделённая",
    "samādhipadhānasaṅkhārasamannāgataṃ": "наделённый сосредоточением" + GAP + "и формирующим фактором усилия",
    "samādhipadhānasaṅkhārasamannāgato": "наделённый сосредоточением" + GAP + "и формирующим фактором усилия",
    "chanda": "желание", "vīmaṃsā": "пытливость", "vīmaṃsaṃ": "пытливость", "citta": "ум",
    "chandasamādhi": "сосредоточение через желание", "vīriyasamādhi": "сосредоточение через усердие",
    "cittasamādhi": "сосредоточение через ум", "vīmaṃsāsamādhi": "сосредоточение через пытливость",
    "padhānasaṅkhāra": "формирующий фактор усилия", "padhānasaṅkhāro": "формирующий фактор усилия",
    "padhānasaṅkhārā": "формирующие факторы усилия", "saṅkhāro": "формирующий фактор",
    # «Если монах, сделав желание главенствующим, обретает сосредоточение, обретает однонаправленность ума …
    # Всё вместе, собранное воедино и обобщённое, получает название «…»»
    "adhipatiṃ": "главенствующий", "labhati": "обретать", "samādhiṃ": "сосредоточение",
    "labhati samādhiṃ": "обретать сосредоточение", "ekaggataṃ": "однонаправленность",
    "cittassekaggataṃ": "однонаправленность ума", "ekajjhaṃ": "вместе",
    "abhisaññahitvā": "собранный воедино", "saṅkhyaṃ": "название", "gacchati": "получать",
    "saṅkhyaṃ gacchati": "получать название", "tveva": NDE,
    # the vīriya / samādhi strings (pi-1 ^1-13 / ^1-15, ch. 5 2-220)
    "dhuratā": "несение бремени", "avisāhaṭa": "нерассеянность", "asithila": "неослабевающий",
    "ussoḷhī": "упорство", "ṭhiti": "устойчивость",
    # «То, что у этих явлений есть сверхспособность, успех, преуспевание, полное преуспевание, обретение, получение,
    # достижение, полное достижение, касание, непосредственное постижение, вхождение»
    "samiddhi": "успех", "ijjhanā": "преуспевание", "samijjhanā": "полное преуспевание", "lābho": "обретение",
    "paṭilābho": "получение", "patti": "достижение", "sampatti": "полное достижение", "phusanā": "касание",
    "sacchikiriyā": "непосредственное постижение", "upasampadā": "вхождение",
    "viññāṇakhandho": "совокупность сознания", "paggāho": "напряжение сил",
    # Duka 2-465: «Пытливость как основа сверхспособностей является корнем … ум как основа сверхспособностей не
    # сопутствует уму … ни как «не соединённый с умом» … относится к внутреннему»
    "na hetu": "не являющийся корнем", "acetasiko": "не сопутствующий уму", "visaṃsaṭṭho": "не соединённый",
    "ajjhattiko": "относящийся к внутреннему", "sahabhū": "сосуществующий",
})

# ---------------------------------------------------------------------------- per-segment overrides
# Pañhāpucchaka: the chapter 7-9 Tika (2-388 …) has only finite verbs («не устраняются», «сопровождаются»), so it
# takes the Duka values (as 2-153 / 2-188 / 2-224); uppannā = возникший («являются возникшими», as 2-152).
_PANHA = dict(M45._DUKA)
_PANHA.update({"uppannā": "возникший", "citta": "ум"})
# vedanā strings (2-363): «приятное / болезненное чувство»
_FEEL = {"sukhaṃ": "приятный", "dukkhaṃ": "болезненный"}
# vattati / carati in «Он принимает положения тела, живёт, оберегает себя, поддерживает себя, продлевает
# существование, действует, пребывает» (Pāli order Iriyati vattati pāleti yapeti yāpeti carati viharati)
_VIHARATI = {"vattati": "жить", "carati": "действовать"}
# «чувственное желание»: kāma = чувственный (as ch. 4 kāmataṇhā)
OVERRIDES = {
    "2-356": {"pāda": "нога"},   # pādatalā «от подошв ног» (ch. 9 pāda of iddhipāda = основа)
    "2-358": dict(_VIHARATI), "2-369": dict(_VIHARATI),
    "2-363": dict(_FEEL),
    "2-367": {"ajjhattaṃ": "внутри", "kāma": "чувственный", "chandaṃ": "желание"},
    "2-388": dict(_PANHA), "2-389": dict(_PANHA),
    # ch. 8: dhamma (dhammacchando «стремление к Учению») = Учение; ṭhiti = сохранение (2-406, 2-420)
    "2-406": {"ṭhiti": "сохранение"}, "2-420": {"ṭhiti": "сохранение"},
    "2-429": dict(_PANHA), "2-430": dict(_PANHA),
}
OVERRIDES.update({"2-464": dict(_PANHA), "2-465": {**_PANHA, "hetu": "корень", "cittaṃ": "ум"}})
# dhamma of dhammacchando «благое стремление к Учению» = Учение
for _b in ("2-392", "2-398", "2-410", "2-421", "2-433", "2-446", "2-458"):
    OVERRIDES.setdefault(_b, {})["dhamma"] = "Учение"

CHOICES = dict(M45.CHOICES)

EXC = {**M6.EXC,
       "atthaṅgatā": "угаснуть ~ угасли (past stem without -ну-)",
       "abbhatthaṅgatā": "полностью угаснуть ~ полностью угасли (past stem without -ну-)",
       "vītarāgaṃ vā cittaṃ": "ум свободный от страсти ~ ум свободен от страсти (short form, fleeting е)",
       "vītadosaṃ vā cittaṃ": "ум свободный от злобы ~ ум свободен от злобы (short form, fleeting е)",
       "vītamohaṃ vā cittaṃ": "ум свободный от заблуждения ~ ум свободен от заблуждения (short form, fleeting е)"}
# per-segment presence exceptions: {(bid, kw): reason}
EXC_SEG = {}
for _b in ("2-355", "2-363"):
    EXC_SEG[(_b, "vedanāsu vedanānupassī")] = ("в чувствах созерцающий чувства ~ «во внутренних / внешних чувствах, "
                                               "созерцая чувства» (the ajjhattaṃ / bahiddhā adjective stands "
                                               "between «во» and «чувствах»), = 2-374")


def resolver_for(part):
    ru, pi = read_russian(part), read_pali(part)

    def resolve(bid, kw, kws):
        k = lc(kw)
        text = ru.get(bid, "")
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        if k in ov:
            return ov[k]
        if kw == "hetuko":
            return hetuko_value(pi.get(bid, ""))
        if k == "saṅkhāra":   # stem of padhānasaṅkhāra(-samannāgata) «формирующим фактором усилия» (sg.), else
            return ("формирующий фактор" if "padhānasaṅkhāra" in {lc(x) for x in kws}   # saṅkhārakkhandho
                    else "формирующие факторы")
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
