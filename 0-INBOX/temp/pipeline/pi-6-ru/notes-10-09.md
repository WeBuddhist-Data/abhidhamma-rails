# Notes 10-09-indriyayamaka (Russian zero-shot): (5) Paccuppannānāgatavāro, anuloma (puggalo, okāso, puggalokāsā)

Builder: 0-INBOX\temp\pipeline\pi-6-ru\build_10-09_ru.py (load with importlib.import_module("build_10-09_ru"); importing writes nothing; `--probe` prints every line). 22 segments, 271 lines.
Shape = 3-03 (Āyatana, same section): "yassa X uppajjati tassa Y uppajjissatīti?" = «У кого возникает X, у того возникнет Y?»; both-form «и возникает X, и возникнет Y»; persons-and-places «там и возникает X, и возникнет Y».
Reused: members, headings, mūlaka tails (build_10-01_ru); attributes, moment(), chain_question(), place line driver (build_10-02_ru); in_units, moments(), pv_norm, S1_RE / S2_RE, desc_clause (build_10-03_ru); the 10-05 / 10-07 future units (build_10-07_ru.MY_UNITS); the 2-01 plane units on the Āyatana planes; 3-03 _YE2 («переродившись в мире форм и в мире без форм»); build_5-01_ru.pv_intro joining («, когда они перерождаются», «в момент возникновения этого ума», «у них»).
10-10 / 10-11: now_fut_units(intro), now_fut_intro(intro, tattha), pv_sentence(s, subj) (handles na / no ca / neither frames), question(q, subj), tr_line(text, subj), NOW_FUT_UNITS, GENDER_UNITS, LAST_REBORN_DESC.
Checks: frame asserts against 3-03 / 5-01 intros; every segment build_10-07_ru (226) / build_10-03_ru (214) parses is byte-identical, except their unmerged groups (below); 196 lines identical with build_10-08_ru.tr_line (in progress); the only Pāli lines shared with finished chapters are the 3 headings (identical).

## Frames
ye ca purisā / yā ca itthiyo upekkhāya (somanassena) upapajjitvā parinibbāyissanti = тех мужчин / женщин, которые, переродившись с невозмутимостью (с радостью), достигнут окончательного угасания [NEW: 10-05 «тех мужчин, которые, …, достигнут» + 2-01 «переродившись {in}» + 10-02 attribute]
yā ca itthiyo rūpāvacaraṃ arūpāvacaraṃ upapajjitvā parinibbāyissanti = тех женщин, которые, переродившись в мире форм и в мире без форм, достигнут окончательного угасания [NEW: same + 3-03 two planes]
Pacchimabhavikānaṃ itthīnaṃ upapajjantīnaṃ / purisānaṃ upapajjantānaṃ = У тех, кто в последний раз перерождается женщиной / мужчиной, [NEW combination: 2-01 «тех, кто в последний раз перерождается {in}» + 10-02 «женщиной»; one group, not «у тех, кто живёт последней жизнью, и у тех, кто перерождается женщиной»]
Itaresaṃ / Itarāsaṃ <attr> upapajjantānaṃ = У остальных, кто перерождается <attr>, [3-03, 5-01 merge; build_10-03 / 10-07 parsers would give «У остальных и у тех, кто …»]
<attr> kāmāvacaraṃ upapajjantānaṃ = тех, кто перерождается без глаза / не женщиной в мире чувственных желаний [3-03]
… tesaṃ (tāsaṃ) upapajjantānaṃ after a "ye / yā" clause = «, когда они перерождаются» [3-03, 5-01]
Pacchimacittassa uppādakkhaṇe yassa cittassa anantarā upekkhāsampayuttapacchimacittaṃ uppajjissati tassa cittassa uppādakkhaṇe = В момент возникновения последнего ума и у тех, у кого сразу после данного ума возникнет последний ум, связанный с невозмутимостью, в момент возникновения этого ума [10-05 unit + 5-01 / 9-01 «в момент возникновения этого ума»]
Somanassasampayuttapacchimacittassa uppādakkhaṇe = В момент возникновения последнего ума, связанного с радостью, [10-02 moment()]
(Sadisaṃ ) = (Так же) [NEW; "the same" as the itthindriya pair above; English rails "(The same.)"]

## Source points
- ^6-10-369 "(Kha) yassa vā pana somanassindriyaṃ uppajjissati, tassa …": stray comma (kept as written; the Russian frame has its comma in that place anyway, so the line reads like its parallels).
- ^6-10-376 "Sacakkhukānaṃ upapajjantānaṃ tesaṃ tattha manindriyaṃ uppajjissati cakkhundriyañca uppajjati": the first "ca" is missing (parallels: manindriyañca); kept as written, «там возникнет способность ума и возникает способность глаза» (no «и …, и …»).
- ^6-10-366 "(Sadisaṃ )": stray space before ")" (spacing only): «(Так же)».
