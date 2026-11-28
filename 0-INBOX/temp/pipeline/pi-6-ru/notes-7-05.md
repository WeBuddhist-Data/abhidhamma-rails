# notes-7-05: Pajahanavāra, anuloma (person / place / person and place)

Builder: build_7-05_ru.py (import: `importlib.import_module("build_7-05_ru")`; importing writes nothing). It imports build_7-01_ru, build_7-02_ru, build_7-03_ru, build_7-04_ru, build_2-02_ru and build_sample_ru unchanged; every frame not listed below is theirs.

## New frames [constant / function in brackets]
pajahati = устраняет (+ accusative) [7-01 TRANSITIVE proposal, settled; pi-5 «устраняет возникновение»; assert]
na / no ca … pajahati = не устраняет (accusative kept; 7-03 NEG_OBJ_CASE is for «иметь» only): «но он там не устраняет скрытую склонность к X»; lists «не устраняет ни скрытую склонность к A, ни скрытую склонность к B» [C.no_ca / E.t_pred]
yo X pajahati so Y pajahati? = Кто устраняет X, тот устраняет Y? [C.Q_WHO]; yo yato … so tato …? = Кто где устраняет X, тот там устраняет Y? [C.Q_WHO_PLACE]; (Kha) yo vā pana = (б) А кто …
yato X pajahati tato Y pajahati? = Где устраняют X, там устраняют Y? [7-03 Q_YATO, GENERIC_3PL; pi-5 «устраняют злобу»]
X-ānusayañca Y-ānusayañca (accusative sandhi) = «X и Y» / «X, Y и Z» [preprocess(): "ānusayañca" -> "ānusayaṃ ca" for C.parse_list]
Tadekaṭṭhaṃ pajahati. (object implied) = Устраняет то, что пребывает вместе с устраняемым. [TADEKATTHA_BARE; tadekaṭṭha pi-1 «пребывающие вместе с ними»; number-neutral: the implied object and the antecedent are singular or plural by question (^6-7-138, ^6-7-139), so no «с ней»; replaces 7-01's TADEKATTHA_FRAME proposal]
A pajahati B tadekaṭṭhaṃ pajahati = устраняет A и устраняет B, пребывающую / пребывающие вместе с устраняемой / устраняемыми [TADEKATTHA_PAIR, TADEKATTHA_OBJ, tadekattha(); participle = number of B, «устраняемой(-ыми)» = number of A; «с ней» would be ambiguous after «Эта же личность …: она там …»; «и» joins the two predicates (the Pāli has none)]
Bare "Mānānusayaṃ pajahati." = «Устраняет скрытую склонность к самомнению.» in person sections, «Устраняют …» in the place section (generic subject; 7-03 rule) [p_answers(a, generic_bare); consistency keyed by mode]
Aṭṭhamako = личность восьмой ступени (feminine: so tato = «она там») [pi-5 «Личность восьмой ступени»; assert; PERSON_NOM_05, PERSON_FEM_05]
Aggamaggasamaṅgī = обладающий высшим путём («он там») [2-02 PJ_SUBJ_UNITS, imported]
Sveva puggalo = Эта же личность …: она там … [7-01]
Pajahanavāre anulomaṃ. = Утвердительная форма в разделе об устранении. [PAJAHANAVARE_FRAME; heading «Раздел об устранении» from the sample]

## Prepared for 7-06 (Pajahanavāra paṭiloma; not used in 7-05)
Pajahanavāre paṭilomaṃ. = Отрицательная форма в разделе об устранении.; Pajahanavāro. = Раздел об устранении. [FIXED]
nappajahati = не устраняет (C.TRANSITIVE); pajahanti / nappajahanti = устраняют / не устраняют [TRANSITIVE_05]
Anāgāmimaggasamaṅgī = обладающий путём невозвращения [PERSON_NOM_05; pi-2 / pi-5 «путь невозвращения»; assert]
X ṭhapetvā avasesā puggalā = Кроме X, остальные личности [apart_persons(); 2-01 APART_GROUP, 2-02 PUGGALA_PL], with APART_GEN_05: aggamaggasamaṅgiṃ «обладающего высшим путём» (2-02), anāgāmimaggasamaṅgiṃ «обладающего путём невозвращения», aṭṭhamakaṃ «личности восьмой ступени» (pi-5), dvinnaṃ maggasamaṅgīnaṃ «двух обладающих путём» (pi-2 «обладающего путём»); "Añca Bñca ṭhapetvā" = «Кроме A и B»
apariyāpanne = в не принадлежащем к кругам существования [7-01 LOCI]

## Reused unchanged
7-01: Q_WHO / Q_WHO_PLACE, KHA_PREFIX, ru_list, LOCI (LOCI_SEP), RES / RES_FEM, ANSWER_INTRO_*, BOTH_FRAME, NO_CA_FRAME, MULAKA, heading(), Да. / Нет. / Такого нет.
7-02: final "…pe…." -> «…» (Да…).
7-03: t_pred, Q_YATO, GENERIC_3PL, RES_T, mode_of, check_local.
7-04: t_clause (both-form), question().

## Source notes (translated as written)
^6-7-148 "… avijjānusayaṃ pajahati no ca tato …": comma missing before "no ca" [SLIPS_05].
^6-7-135 "Āmantā …pe….", ^6-7-140 "pajahati …pe….", ^6-7-151 "pajahati …pe….": spacing before …pe… only; final "…pe…." -> «…».
^6-7-164: "(Chakkamūlakaṃ)" ends the last answer line and "Pajahanavāre anulomaṃ." stands on its own line, as in the Pāli.
