# notes-7-04: Sānusayavāra, paṭiloma (person / place / person and place; niranusaya)

Builder: build_7-04_ru.py (import: `importlib.import_module("build_7-04_ru")`; importing writes nothing). It imports build_7-01_ru, build_7-02_ru, build_7-03_ru and build_sample_ru unchanged; every frame not listed below is theirs.

## New frames [constant / function in brackets]
X-ena niranusayo / niranusayā = не имеет / не имеют скрытой склонности к X (GENITIVE) [7-01 TRANSITIVE + 7-03 NEG_OBJ_CASE, t_pred()]
yo X niranusayo so Y niranusayo? = Кто не имеет скрытой склонности к X, тот не имеет скрытой склонности к Y? [C.Q_WHO with t_pred: 7-01's C.question would put the object in the accusative; question()]
yo yato X niranusayo so tato Y niranusayo? = Кто где не имеет …, тот там не имеет …? [C.Q_WHO_PLACE]
yato X niranusayo tato Y niranusayo? = Где не имеют скрытой склонности к X, там не имеют скрытой склонности к Y? [7-03 Q_YATO, GENERIC_3PL]
yo A ca B ca niranusayo so …? = Кто не имеет ни скрытой склонности к A, ни скрытой склонности к B, тот …? [C.ru_list(case="gen", neg=True)]
… niranusayo so X…pe… Y niranusayo? = … не имеет скрытой склонности к X… скрытой склонности к Y? (series, no «ни») [C.ru_list]
A ca niranusayo B ca niranusayo = не имеет ни скрытой склонности к A, ни скрытой склонности к B; with lists «ни A, ни B, ни C» (verb once, Pāli number; generic «не имеют») [t_both_neg(), C.BOTH_NEG_FRAME; coordinator "Negatives"]
…, no ca B niranusayo (no resumptive) = …, но имеет скрытую склонность к B [7-03 NO_CA_BARE_FRAME with t_pred(neg_extra=True)]
…, no ca so / te tato B niranusayo = …, но он / они там имеет / имеют скрытую склонность к B; list «A, B и C» [C.NO_CA_POS_FRAME]
<places> tato …, no ca tato B niranusayo = <Места>: там не имеют …, но там имеют B [C.ANSWER_INTRO_PLACE]
Person sabbattha A ca niranusayo B ca niranusayo = <Person> везде не имеет ни A, ни B («Архат везде …», «Две личности везде …») [7-02 SABBATTHA after C.PERSON_NOM]
Sānusayavāre paṭilomaṃ. = Отрицательная форма в разделе об имеющих скрытые склонности. [7-03 VARE_FRAME + sample "paccanīkaṃ"]
Sānusayavāro. = Раздел об имеющих скрытые склонности. [C.VARO_CLOSING + sample SECTION_HEADINGS["Sānusayavāro"]]
Proposal for 7-05 … (pajahati / parijānāti paṭiloma): t_both_neg() works for any TRANSITIVE verb (accusative unless NEG_OBJ_CASE says otherwise).

## Reused unchanged
7-01: persons (PERSON_NOM, Эта же личность → она), places (LOCI, LOCI_SEP), resumptives, MULAKA, headings, Да.
7-02: SABBATTHA «везде», final "…pe…." → «…».
7-03: t_pred, Q_YATO, GENERIC_3PL, NEG_OBJ_CASE, NO_CA_BARE_FRAME, VARE_FRAME, RES_T, check_local.

## Source notes (translated as meant; the Pāli file untouched)
^6-7-130 "Sveva puggalo dukkhāya vedanāya ariyāpanne": slip for "apariyāpanne" (every parallel has it) → «в не принадлежащем к кругам существования» [SLIPS_04].
^6-7-122 "… paṭighānusayena niranusayo no ca so tato …": missing comma before "no ca" [SLIPS_04].
^6-7-127 "Arahā sabbattha bhavarāgānusayena niranusayo kāmarāgānusayena ca …": first "ca" missing (parallels ^6-7-128 have it); read as the usual negated pair [MISSING_CA_OK].
^6-7-127 "no ca so tato mānānusayena ca niranusayo": stray "ca" on a single item; same Russian as without it.
^6-7-102, ^6-7-107, ^6-7-113, ^6-7-108, ^6-7-118, ^6-7-119, ^6-7-124, ^6-7-129: spacing before "…pe…" only; final "…pe…." → «…».
