# Harmonise pass, pi-1 Russian plain zero-shot: notes

Script: harmonise_ru.py (reads backup-pre-harmonise\, rerunnable, --dry). Log: harmonise-log.tsv (one row per rule per changed line: rule, part, segment, line, old, new). Divergence scans: divergences-pre.md (before, `find_divergences_ru.py --bak`), divergences.md (after). Helpers: ru_common.py, probe_ru.py, show_seg_ru.py.
347 lines changed (2-01 3, 2-02 8, 2-03 27, 2-04 15, 2-05 55, 3-01 1, 4-01 43, 4-02 96, 4-03 1, 5 98). preamble, 1-matika, 3-02, 3-03 untouched; the first 122 non-empty lines of 2-01 unchanged.

## Decisions applied (rule id = harmonise_ru.py)
- D1 jhāna frame = 2-01/2-02: «человек, развивая …, полностью уединившись от чувственных удовольствий / с затиханием направленной мысли и удержания мысли … входит в N-е медитативное погружение, <qualifiers>, и пребывает в нём»; «с устранением приятного» without «и»; later ordinals in the accusative. Lokuttara-only wording kept (надмирское …, ведущее к освобождению …, ступени, «(благое)/(результат)»); the qualifiers become neuter accusative: пустое, свободное от устремлений, не имеющее признаков. D1-count: pañcaṅgika jhāna / aṭṭhaṅgika magga = «пятичастное медитативное погружение» / «восьмичастный путь» (2-01/2-04).
- D2 paṭipadā «с трудным / лёгким способом практики». D3 vīmaṃsā «пытливость» (also 4-01 ^1-1040).
- D5 asāta: the approved sample has neither form, so «безотрадный»; nāsātaṃ = «ни отрадно, ни безотрадно».
- D6 viññatti «внешнее выражение»; D7 upacaya «рост» (also 4-02 «накопление»); D8 diṭṭhigata(sampayutta) «приверженность воззрениям» (ch5); D9 patiṭṭhāho «закрепление» (4-01, 4-02; paṭiggāho keeps «цепкость»: 4-01 ^1-1007/1009/1105/1122).
- D10 kammassa katattā «вследствие совершённых действий» (ch3, 50 lines), frame «которая возникла (не) вследствие совершённых действий» (4-01, 4-02, ch5).
- D12 «сферы» + space (2-02, 8 lines). 13: sārāga «пристрастие» (4-01). 14: «(во многих изданиях)» was already uniform.
- 15 (B rules): 4-01 wins over 4-02/4-03 for the lobha, dosa, kaṅkhā, kāma, bhava, māna, sakkāyadiṭṭhi, sīlabbata bodies, the Tehi-dhammehi frames, sphere lists («и», not «или / а также»), bhūmi frames, tadekaṭṭha / taṃsampayutta, «и вся материальная форма, и необусловленный элемент», «Пути, не принадлежащие …», «это явления, являющиеся корнями …», «Три вида оков». 4-02 wins where it matches an earlier book: vacīkamma «речевое действие» (pi-5), sarīra «плоть» in the ten views (pi-5; capitals of 4-01 kept), and its two senses of rūpataṇhā («жажда существования в мире форм», «жажда видимых форм», now also in 4-01). Other choices: kaṅkhā string = 4-01 (vimati «неуверенность», pi-5); uddhacca string = 2-04 (avūpasamo «отсутствие затихания», after decision 1); diṭṭhi string items = 4-01/4-02/pi-4 (извращённость воззрений, приверженность); ṭhapetvā «кроме» everywhere (pi-5, 2-0x; 125 replacements, one per ṭhapetvā); ch5 «Те же самые», «Десять видов оков», «Десять основ», «влечение воззрений», «учение о самости», «съедаемая пища», «Высший плод состояния архата»; na vattabba = ch5 frame «… нельзя определить – ни как …» (36 lines vs 2); na kāmāvacarā lists = 4-02 (mirror the Pāli commas).

## Left on purpose
- bhūmi: «ступень» (paṭhamāya bhūmiyā pattiyā, path stage), «уровень» (X-bhūmiyaṃ), «мир» (catūsu bhūmīsu): three senses.
- kakkhaḷa: «твёрдое» (earth element, ch3 = pi-5) vs akakkhaḷatā «отсутствие грубости» (approved sample).
- parāmāsa «искажение» (matrix) vs sīlabbataparāmāsa «приверженность обрядам и обетам» (pi-5); diṭṭhiparāmāsa «искажение в виде воззрений».
- cittuppāda: only ch5 (73 lines), always «вид(ы) ума»; the terms file has «возникновение ума» (heading «Раздел о возникновении ума», approved). User to confirm.
- divergences.md (a4) 8 groups: item-alignment artefacts where the Pāli differs (nibbāna vs asaṅkhatā dhātu, different list lengths).

## Builder constants that need the same change (do not rebuild without them)
- build_2-03_ru.py: J1, J5, DEV_JHANA, DEV_TWENTY («развивает» → «развивая»), CL/ALL4/IN_J/EMPTY/DESIRELESS assembly (qualifiers before «и пребывает в нём»), PP (lines 288-291), ADHI (295), SANGAHA_ITEMS (228-229).
- build_2-05_ru.py: WHEN, VIV (136), VUP (137), VIPAKA_OPEN, ENTER/path_chunk, IN_J, EMPTY, ATTR1 (180), PATIPADA (168-171), SUKHA_PAHANA, kiriya openers in EXACT.
- build_2-01_2-02_ru.py: 133 (неотрадно), 366/368 (сферыб…). build_2-04_ru.py: 112 (неотрадно), 121-122 (изворотливость, упрямство), 139 (kaṅkhā string).
- build_3-01_ru.py: 175 (kiriyā frame).
- build_4-01_ru.py: 84 (словесное), 98-100 (совершённого действия), 214 (жажда форм / бесформенного), 268 (patiṭṭhāho only), 274 (тело), 472 (исследование), every «за исключением».
- build_4-02_4-03_ru.py: 56, 62, 64, 66, 69, 72, 73, 77, 214, 216, 229 (dosa), 238, 246, 272, 292-294, 304-305 (lobha), 340, 357-358, 369, 405, 411, 529, 532, 538, 554, 557, 568, 627, 641, 645.
- build_5_ru.py: 41-49, 150-162, 176-177, 201-202, 241-262, 343, 382-426, 455-456, 462-489, 511, 536, 562, 579-580, 596, 605, 615-641 (Эти же, Десять оков/оснований, к воззрениям, о «я», сообщение, нарастание, съедаемая кусками, ложным воззрением, за исключением).
