# notes-7-07: Pariññāvāra (anuloma person / place / person and place; paṭiloma person / place)

Builder: build_7-07_ru.py (import: `importlib.import_module("build_7-07_ru")`; importing writes nothing). It imports build_7-01_ru … build_7-06_ru, build_2-02_ru and build_sample_ru unchanged; every frame not listed below is theirs.
For 7-08 (paṭilomapuggalokāsā, closing lines): tr_line(body, mode) / translate_file(src) already parse "sabbattha", "Anāgāmimaggasamaṅgiṃ ṭhapetvā …", person + places + "so tato", "Pariññāvāre paṭilomaṃ.", "Pariññāvāro." (FIXED). Reuse: PJ_VERBS, pj_t_pred(), pj_both_neg(), pj_clause(), question7(), answers7(), check_local7(), check_consistency7().

## New frames [constant / function in brackets]
parijānāti / parijānanti = полностью понимает / полностью понимают (+ accusative) [2-02 PJ_RU via P.pj_pred; pi-5; assert]
na parijānāti / na parijānanti = не понимает полностью / не понимают полностью (accusative kept, as 7-05 / 7-06 «устраняет») [2-02 PJ_RU; never «не полностью …»; check_local7 asserts]
yo X parijānāti so Y parijānāti? = Кто полностью понимает X, тот полностью понимает Y? ; negated = Кто не понимает полностью X, тот не понимает полностью Y? [C.Q_WHO, question7()]
yo yato … so tato …? = Кто где полностью понимает X, тот там полностью понимает Y? [C.Q_WHO_PLACE]
yato X parijānāti tato Y parijānāti? = Где полностью понимают X, там полностью понимают Y? ; negated «Где не понимают полностью X, там не понимают полностью Y?» [7-03 Q_YATO, generic 3rd plural]
yo A ca B ca na parijānāti so …? = Кто не понимает полностью ни A, ни B, тот …? [C.ru_list(neg=True)]
A ca na parijānāti B ca na parijānāti = не понимает полностью ни A, ни B (verb once; number of the Pāli verb; generic «не понимают полностью») [pj_both_neg(), C.BOTH_NEG_FRAME; coordinator "Negatives"]
…, no ca so [tato] B na parijānāti = …, но он / она [там] полностью понимает B ; …, no ca [so] tato B parijānāti = …, но [он] там не понимает полностью B [C.NO_CA_POS_FRAME / NO_CA_FRAME]
X ṭhapetvā avasesā puggalā … na parijānanti = Кроме X, остальные личности не понимают полностью ни … [7-05 apart_persons()]
Tadekaṭṭhaṃ parijānāti. = Полностью понимает то, что пребывает вместе с полностью понимаемым. [TADEKATTHA_BARE_07; 7-05 TADEKATTHA_BARE with the pariññā verb and participle; asserted parallel]
A parijānāti B tadekaṭṭhaṃ parijānāti = полностью понимает A и полностью понимает B, пребывающую / пребывающие вместе с полностью понимаемой / полностью понимаемыми [7-05 TADEKATTHA_PAIR / TADEKATTHA_OBJ / TADEKATTHA_PART; PJ_PASSIVE_WITH]
A parijānāti, B tadekaṭṭhaṃ parijānāti (Pāli comma) = полностью понимает A, полностью понимает B, пребывающую вместе с полностью понимаемой [TADEKATTHA_PAIR_COMMA "{p1}, {p2}"; the comma kept, no «и» added]
A ca parijānāti B ca tadekaṭṭhaṃ parijānāti = и полностью понимает A, и полностью понимает B, пребывающую вместе с полностью понимаемой [C.BOTH_FRAME]
Bare "Mānānusayaṃ parijānāti." (person sections) = Полностью понимает скрытую склонность к самомнению. [7-05 rule: generic «Полностью понимают» only in a place section]
Pariññāvāre anulomaṃ. = Утвердительная форма в разделе о полном понимании. [PARINNAVARE_FRAME; heading from the sample]
Prepared for 7-08: Pariññāvāre paṭilomaṃ. = Отрицательная форма в разделе о полном понимании.; Pariññāvāro. = Раздел о полном понимании. [FIXED; = 2-02 closing]
Heading "#### Pariññāvāra" = «#### Раздел о полном понимании» (same as Pariññāvāro, as the sample's Pajahanavāra / Sānusayavāra) [HEADING_ALIAS]

## Source notes (translated as written; the Pāli file untouched)
^6-7-243 "(Ka) yato paṭighānusayaṃ na parijānāti tato mānānusayaṃ parijānātīti?": the second "na" is missing (every parallel and the answer are negative); a word, not a spelling slip, so rendered as written: «Где не понимают полностью …, там полностью понимают скрытую склонность к самомнению?».
^6-7-220, -221, -222, -224: "…vicikicchānusayaṃ parijānāti, X tadekaṭṭhaṃ parijānāti" has a comma (7-05's parallels have none); the comma is kept.
^6-7-201, -206, -212, -217, -223, -228, -234, -239, -245, -250: spacing before "…pe…" only; final "…pe…." → «…».
