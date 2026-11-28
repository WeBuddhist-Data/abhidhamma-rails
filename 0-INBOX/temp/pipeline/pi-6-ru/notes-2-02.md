# Notes 2-02-khandhayamaka (Russian zero-shot): family E (pariññāvāra) frames + family B additions

Builder: 0-INBOX\temp\pipeline\pi-6-ru\build_2-02_ru.py (load with importlib.import_module("build_2-02_ru"); importing writes nothing).
Families A and B are imported from build_2-01_ru (KH_CFG extended to KH2_CFG); the person / place shape and Q_WHO from build_7-01_ru.
Later chapters with a pariññāvāra add "pj_obj" (accusative member names) to their config and call pj_line(text, cfg), or translate_text(src, cfg) of this module.

## Family E: pariññāvāra (PJ_FORMS, PJ_RU, pj_pred, pj_question, pj_subject, pj_sentence, pj_line)
parijānāti = полностью понимает; parijānanti = полностью понимают [pi-5 «полностью понимает страдание»; assert]
na parijānāti = не понимает полностью; na parijānanti = не понимают полностью [pi-5 «не понимает полностью страдание»; assert; never «не полностью …» (reads as "partly")]
parijānittha = полностью понял / полностью поняли (perfective: aṭṭhakathā "niṭṭhitapariññākicco", the task is finished); na parijānittha = не понял полностью / не поняли полностью [new]
parijānissati / parijānissanti = полностью поймёт / полностью поймут; na … = не поймёт полностью / не поймут полностью [new]
Russian number follows the subject (parijānittha does not show it); verb before the object; object in the accusative (совокупность acc = nom).
(Ka) yo X parijānāti so Y parijānātīti? = (а) Кто полностью понимает X, тот полностью понимает Y? [C.Q_WHO]
(Kha) yo vā pana Y parijānāti so X parijānātīti? = (б) А кто полностью понимает Y, тот полностью понимает X? [C.KHA_PREFIX]
… na parijānāti so … na parijānātīti? = Кто не понимает полностью X, тот не понимает полностью Y?
Answers: Āmantā. = Да.; No. = Нет. [7-01, pi-5]
<Subj> X na parijānāti, no ca Y na parijānittha. = <Subj> не понимает полностью X, но полностью понял Y. [PJ_NO_CA_FRAME «, но {pred}»; coordinator "Negatives"; no pronoun: the Pāli has none]
<Subj> Xñca na parijānanti Yñca na parijānittha. (different tenses) = <Subj> не понимают полностью X и не поняли полностью Y. [PJ_NEG_MIXED_FRAME = 2-01 PV_NEG_MIXED_FRAME]
<Subj> Xñca na V Yñca na V. (same Russian verb) = <Subj> не V ни X, ни Y. [PJ_NEITHER_FRAME = 2-01 PV_NEITHER_FRAME; not in 2-02, prepared]
<Subj> Xñca V1 Yñca V2. = <Subj> и V1 X, и V2 Y. [PJ_BOTH_FRAME = 7-01 BOTH_FRAME; not in 2-02, prepared]
Persons (PJ_SUBJ_UNITS, nominative):
Arahā = архат [pi-5; assert]
Aggamaggasamaṅgī = обладающий высшим путём [maggasamaṅgī pi-1/pi-2 «обладающий путём»; agga = высший; aṭṭhakathā: arahattamaggaṭṭha]
Ye maggaṃ paṭilabhissanti te = Те, кто обретёт путь, [paṭilabhati pi-5 «обретает»]
(Arahā / Aggamaggasamaṅgī) ye ca puthujjanā maggaṃ na paṭilabhissanti te = (Архат / Обладающий высшим путём) и те обычные люди, которые не обретут путь, [pi-4 «а также те обычные люди, которые»; puthujjana pi-4/pi-5]
Aggamaggasamaṅgiñca arahantañca ṭhapetvā avasesā puggalā = Кроме обладающего высшим путём и архата, остальные личности [2-01 APART_GROUP; puggala = личность pi-5]
Pariññāvāro. (closing) = Раздел о полном понимании. [C.VARO_CLOSING; heading from the sample]

## Family B additions (pavattivāra)
ye ca Xaṃ upapajjitvā parinibbāyissanti = и у тех, кто, переродившись {в X}, достигнет окончательного угасания, [2-01 unit wording; "ca" = the «и» of the person list]
ye ca Xaṃ upapajjitvā parinibbāyissanti tesaṃ cavantānaṃ = и у тех, кто, переродившись {в X}, достигнет окончательного угасания, когда они умирают, [new; cavati = умирать (2-01)]
(PERSON_UNITS_2_02; extra_units() adds them to build_2-01_ru only inside the block; 2-01's output is asserted unchanged)
Yattha X V…pe…. = Где V X… [PV_ABBR_RE; first clause of C.Q_PLACE]
Yattha X na V (yatthakaṃ paripuṇṇaṃ kātabbaṃ). = Где не V X (раздел с «где» следует изложить полностью). [new]
… V…pe…. (end of an answer) = … V… [style rule]
(Yathā uppādavāre paccuppannātītaṃ vibhattaṃ tathā idha vibhajitabbaṃ). = (Как в разделе о возникновении разобран раздел о настоящем и прошлом, так же следует разбирать и здесь). [pi-2 1 «(Как разобрано в разделе о материальной форме, так же следует разбирать и здесь.)»; assert]
Nirodhavāro. = Раздел о прекращении.; Uppādanirodhavāro. = Раздел о возникновении и прекращении. [C.VARO_CLOSING]
Pavattivāro niṭṭhito. = Раздел о протекании завершён. [PAVATTIVARO, head of the approved "Pavattivāro 1. uppādavāro"]
Khandhayamakapāḷi niṭṭhitā. = Парные вопросы о совокупностях завершены. [B.YAMAKA_CLOSING_FRAME]
"? No." in the pavattivāra = «? Нет.» [C.NO]

## Source slips (rendered as meant; SLIPS in the builder)
^6-2-185 "vadanākkhandho" = vedanākkhandho (spelling).
^6-2-134 "… saññākkhandho ca nirujjhissati vedanākkhandho nirujjhati": second "ca" missing; rendered as the parallel lines («и прекратится …, и прекращается …»).
^6-2-163 "… rūpakkhandho nuppajjati vedanākkhandho ca na nirujjhati": first "ca" missing (^6-2-159 has it); the Russian «не возникает X и не прекращается Y» is the same either way.
^6-2-151 stray comma in "rūpakkhandho ca na nirujjhittha, vedanākkhandho ca …": dropped.
