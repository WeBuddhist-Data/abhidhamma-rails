# pi-2 Russian zero-shot: harmonise pass notes (2026-11-15)

Scripts (all in this folder): ru_common.py, find_divergences_ru.py (divergences-pre.md = backup, divergences.md = after),
harmonise_ru.py (reads backup-pre-harmonise\, writes the 19 part files, log harmonise-log.tsv), check_viriya_ru.py,
find_bare_comma.py, probe_harm.py, probe_none.py. The builders were NOT rerun or edited: rerunning one would undo the
pass for its chapters; rerun harmonise_ru.py after any rebuild, or change the builder constants below.

## Rules applied (44 lines, 46 replacements)
- D1-viriya, ch5 ^2-220: «…, сила усердия, правильное усилие, – это» -> «…, сила усердия, – это» (Pāli has no
  sammāvāyāmo). check_viriya_ru.py: all 37 vīriya strings now match their own Pāli line item by item
  (ch9 ^2-433 maggariyāpannaṃ = spelling slip rendered as meant).
- D2-kamesu, ch14 (5 lines): «неподобающего поведения в чувственных удовольствиях» -> «неправильного …».
  «неподобающее поведение» remains only for anācāra (ch12 ^2-512 ff.), a different Pāli word.
- D3-gods, ch18 ^2-1020 (3): «богов Аканиттха» -> «высочайших богов»; «богов, рождённых в сфере …» -> «богов, достигших сферы …».
- D4-rajata, ch3 ^2-173: second «серебро» (rajataṃ) -> «монеты». Vibhaṅga aṭṭhakathā: «Sajjhūti rajataṃ» (sajjhu =
  silver metal, keeps «серебро»), «Rajatanti kahāpaṇo» (rajata in this list = coin). pi-1 has no such list; its
  jātarūparajata «золото и серебро» (pi-2 ch2 ^2-162) stays.
- D6-comma, ch3 ^2-184 (non-empty line 49): «… это элемент осязаемого, – это» -> «… – это» (the only «X, – это» after a stretch
  without a comma; same test as pi-1-ru\rails\fix_bare_comma_ru.py).
- D7-thapetva, ch16 (2): «за исключением» -> «кроме» (pi-1, pi-5; pi-2 elsewhere).
- D7-kilesavatthu, ch16 ^2-819: «бессовестность и отсутствие …» -> «бессовестность, отсутствие …» (pi-1, ch17 ^2-966).
- D7-niddesa, ch16 (20): niddesa headings and closings = pi-1 Rūpakaṇḍa (identical Pāli, same structure
  «Ekavidhena X … Ekakaniddeso … Ekakaṃ.»): «Разъяснение классификации по одному / на два вида … на десять видов»,
  closings «Классификация по одному. … Классификация на десять видов.»; ch17 (11): «#### Объяснение X» ->
  «#### Разъяснение X» (niddesa = «разъяснение», pi-1, ch6, ch7, ch16).

## Left on purpose (find_divergences_ru.py "Left on purpose", 37 groups; (a) and (b) otherwise 0)
- Ekakaṃ. … Dasakaṃ.: ch16 «Классификация …» (classification, pi-1 Rūpakaṇḍa); ch17 «Единицы. … Десятки.» (groups
  of listed items, as pi-1 4-01/5 «Тройки.»); ch12 Catukkaṃ./Pañcakaṃ. «Четверичный / Пятеричный метод» (jhāna method).
  Question-section headings ##### Tikaṃ / Dukaṃ «Тройки» / «Пары» (matrix triads/dyads) vs pi-1 Rūpakaṇḍa
  «Классификация на три / два вида».
- saṅkhārapaccayā viññāṇaṃ: plural «формирующими факторами» in the Suttanta section (^2-227), singular elsewhere (notes-6).
- Tattha katamaṃ dukkhaṃ?: «боль» for bodily pain in the soka … upāyāsa list (^2-196, ^2-239), «страдание» elsewhere (notes-4-5).
- Question-section predicates (siyā lokuttarā, siyā anāgatā …, atthi akusalaṃ, kenaci na viññeyyā): number/gender
  agreement with different subjects.
- Scanner artifacts: ch1 ^2-33 item boundaries (approved sample); ṭhiti in the vīriya string vs cittassa ṭhiti.
- dhamme ñāṇaṃ: «знание Учения» (ch16 catukka ^2-796, path knowledge) vs «знание явлений» (paṭisambhidā, ch15 ^2-718,
  ch16 ^2-800): two meanings, kept.
- veramaṇī «воздержание» (precept names, ch14) vs «уклонение» (abstention list, ch4/11); saṅgati «встреча» (ch4) vs
  «сочетание» (ch6); slips kept as written per the notes files.

## Cross-book differences (for the user)
- Akaniṭṭha / formless gods: pi-1 ^1-1289, ^1-1291 «богов Аканиттха», «богов, рождённых в сфере бесконечного
  пространства / ни восприятия, ни невосприятия»; pi-2 now «высочайших богов», «богов, достигших сферы …» throughout
  (ch18 ^2-1020 … ^2-1028, = pi-5). pi-1 unchanged.
- Ekakaṃ.-type closings: pi-1 uses «Классификация …» only in the Rūpakaṇḍa; pi-2 ch17 keeps the counted nouns.

## Builder constants that would need the same change (not edited)
- build_4_5_ru.py: the ch5 ^2-220 vīriyindriya string (drop «, правильное усилие»).
- build_13_15_ru.py line 197: "kāmesumicchācārā": «неподобающего поведения …» -> «неправильного поведения …».
- build_18_ru.py lines 933-938, 947: RUPA_WORLD «богов Аканиттха» (also the variant .replace), ARUPA_WORLD «рождённых в сфере».
- build_2_3_ru.py line 298: «коралл, серебро, золото» -> «коралл, монеты, золото»; the ch3 phoṭṭhabbadhātu line («элемент осязаемого, – это»).
- build_16_ru.py: CLOSE_GROUP (line 50), heading f-string line 1399, line 832 «За исключением», line 877 «за исключением»,
  the ^2-819 kilesavatthu list («и отсутствие»).
- build_17_ru.py lines 322-327: «#### Объяснение …» -> «#### Разъяснение …».
