# Notes 3-05-ayatanayamaka (Russian zero-shot): Āyatana nirodhavāra (end), uppādanirodhavāra (start)

Builder: 0-INBOX\temp\pipeline\pi-6-ru\build_3-05_ru.py (load with importlib.import_module("build_3-05_ru"); importing writes nothing; `--probe [--show]` lists unparsed / all lines, `--dry` prints, `--wide` compares identical Pāli with every other finished chapter). 69 segments, 404 lines.
Everything else comes from build_3-01_ru … build_3-04_ru (members, AY4_CFG, person units incl. «когда они перерождаются / умирают», sa-/a-X-ka with cavantānaṃ, pe_question, abbr_question, the multi-pair splitter, the yatthaka notes), families A / B from build_2-01_ru / build_2-02_ru, the person / place shape from build_7-01_ru. 3-01 … 3-04 are asserted unchanged under the 3-05 unit.
3-06: `with ay5_units(): …` and this module's tr_line / translate_text (AY5_CFG) give everything below.

## Family B additions [PERSON_UNITS_3_05, ay5_units]
Rūpāvacare arūpāvacare parinibbantānaṃ = у тех, кто достигает окончательного угасания в мире форм и в мире без форм [2-01 "{P}e parinibbantānaṃ" + « и {in2}», as "{P}ā {P}ā cavantānaṃ"]

## Abbreviated answers and questions [pe_answer, abbr_stmt, ANS_TAIL_RE]
<persons> tesaṃ…pe… <persons> tesaṃ…pe…. = У …… у …… [intro without its closing comma; later parts lower-case as the Pāli; as 8 «У остальных в момент ……»]
Sabbesaṃ upapajjantānaṃ acakkhukānaṃ cavantānaṃ tesaṃ…pe… sacakkhukānaṃ cavantānaṃ tesaṃ…pe…. = У всех, кто перерождается, и у тех, кто умирает без глаза… у тех, кто умирает с глазом…
<persons> tesaṃ tattha…pe…. = У …, там… (2-01 PV_TAM)
(Kha) yassa vā pana [yattha] X…pe…. = (б) А у кого [где] X… [3-03 abbr_question; no "?" in the Pāli, "…pe…." = «…»]
Yassa [yattha] X na V…pe…. = У кого [где] не V X… [first clause of Q_PERSON / Q_PERSON_PLACE, as 2-02 "Yattha X V…pe…."]
…? No. = …? Нет.; …? No …pe…. = …? Нет…; …? Āmantā …pe…. = …? Да… [7-03, 8]

## Headings, closings, notes [AY5_FIXED]
#### Pavatti 3. uppādanirodhavāro = #### Протекание 3. Раздел о возникновении и прекращении [sample «Протекание 2. …»; = 5-02]
Nirodhavāro. = Раздел о прекращении. [2-02]
(yathā paccuppannātītepi tividhaṃ vitthāritaṃ evaṃ idampi vitthāretabbaṃ). = (как в разделе о настоящем и прошлом развёрнуто тремя способами, так же следует развернуть и это). [new; vitthāritaṃ «развёрнуто», tividhaṃ «тремя способами»]
(yatthakaṃ noti na kātabbaṃ, yatthakaṃ itaresaṃ yatthakānaṃ sadisaṃ kātabbaṃ, yatthakaṃ tīsupi vāresu sadisaṃ). = (раздел с «где» не следует излагать с ответом «Нет», раздел с «где» следует изложить так же, как остальные разделы с «где», раздел с «где» одинаков во всех трёх разделах). [new; yatthakaṃ thrice as in the Pāli]
(Yassakampi yassayatthakampi sadisaṃ). = (И раздел с «у кого», и раздел с «у кого где» одинаковы). [= 5-02 SAME_YY; 5-01 frame]
(Atītā pucchā uppādepi nirodhepi uppādanirodhepi anulomampi paccanīkampi sadisaṃ). = (Вопрос о прошлом в разделе о возникновении, в разделе о прекращении и в разделе о возникновении и прекращении одинаков и в утвердительной, и в отрицательной форме). [3-04 ATITA_NOTE wording; 5-02 has «вопросы о прошлом» / «при возникновении» for the same words: coordinator to align]

## Source points
^6-3-172 "parinibbāntānaṃ": spelling slip, rendered as parinibbantānaṃ.
^6-3-186 "manāyatana…pe…": final ṃ missing, rendered as manāyatanaṃ.
^6-3-195 "manāyatanañca na nirujjhissati, cakkhāyatanañca na nirujjhittha": stray comma kept as written (user rule) = «не прекратится сфера ума, и не прекращалась сфера глаза».
^6-3-194 "Yassa cakkhāyatanaṃ na nirujjhittha…pe…." under the heading paccanīkaokāso (place): "Yassa" where "Yattha" is expected; translated as written «У кого не прекращалась сфера глаза…».
