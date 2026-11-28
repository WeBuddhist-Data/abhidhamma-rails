# pi-6 Russian zero-shot: coordinator rules (binding for every chapter agent)

The coordinator updates this file while chapter agents run. Re-read it before you build and again before you report.

## User decisions on the sample (2026-11-27)
- Book title «Парные вопросы»; yamaka headings «Парные вопросы о корнях / о совокупностях / о сферах восприятия / об элементах / об истинах / о формирующих факторах / о скрытых склонностях / об уме / о явлениях / о способностях», exactly as in ru-zeroshot-terms.md.
- hetu inside the hetuvāra series = «причина»; mūla = «корень».
- anuloma / paccanīka = «утвердительная / отрицательная форма»; Āmantā = «Да.»; uddeso «Перечень», niddeso «Разъяснение», -nayo «метод», Paṇṇattivāro «Раздел об обозначениях», Pavattivāro «Раздел о протекании». The recurring section headings in ru-zeroshot-terms.md are approved: use them verbatim.
- A relative clause followed by «A ceva B ca» needs a main verb: «X, которые возникают вместе, имеют и A, и B.» (never «X, которые …, и имеют A, и имеют B.»).
- Labels: take them from build_sample_ru (B.LABEL or the constant it exposes); never type them.

## Frame families and who sets them
Wave 1 agents set the frames of a family; every later agent copies them verbatim from that agent's builder (import it) and notes file.
- Family A, paṇṇattivāra (padasodhana, padasodhanamūlacakka, suddha-X, suddha-X-mūlacakka; anuloma / paccanīka; the "X ti? … Y ti?" naming questions): set by 2-01-khandhayamaka (build_2-01_ru.py, notes-2-01.md).
- Family B, pavattivāra (yassa … tassa …, yattha … tattha …, yassa yattha … tassa tattha …; uppajjati / nirujjhati in present, past, future and the mixed tenses; the answer frames naming beings and planes): set by 2-01-khandhayamaka.
- Family C, anusayayamaka (uppattiṭṭhāna, anuseti, sānusaya, pajahati, pariññā, pahīna, uppajjati, dhātu): set by 7-01-anusayayamaka (build_7-01_ru.py, notes-7-01.md).
- Family D, cittayamaka (puggalavāra, dhammavāra, the time sections, uppajjamāna / nirujjhamāna, suttanta / abhidhamma mixtures): set by 8-cittayamaka (build_8_ru.py, notes-8.md).
- Family E, pariññāvāra (parijānāti frames): set by the first agent to finish a chapter containing it (2-02 normally); until then follow the English rails for structure and report your wording.
- Each later yamaka chapter (Khandha 2-02, Āyatana, Dhātu, Sacca, Saṅkhāra, Dhamma, Indriya) imports build_2-01_ru and substitutes its own members (names from pi-1 / pi-2 Russian) into those frames; anusaya chapters import build_7-01_ru.

## Shared frames fixed by the coordinator
(added here as agents report)

### Heading case (coordinator, 2026-11-27)
- In headings, the first word after a label or number is capitalised, as the sample does: «#### (а) Перечень», «(а) Утвердительная форма по личности», «(1) Метод корней». Ordinary sentences are unaffected.

### Negatives (coordinator, 2026-11-27; replaces 7-01's «, но не так, что …»)
- A denied negative verb is said plainly: «…, no ca tesaṃ Y nuppajjati» = «…, но у них возникает Y.»; «…, no ca tassa Y nānuseti» = «…, но у него залегает Y.» (same for прекращается, устраняет, понимает …; 7-02's NO_CA_POS_FRAME). Never «но не так, что».
- Two negated predicates joined by ca … ca: «X ca nuppajjati Y ca nuppajjati» = «не возникает ни X, ни Y» (verb once; plural verb when the Pāli verb is plural or Y is a list: «не залегают ни X, ни A, ни B»). The positive pair «X ca uppajjati Y ca uppajjati» stays «и возникает X, и возникает Y» as 7-01 set it.

### From 2-02 (finished 2026-11-27; build_2-02_ru.py, notes-2-02.md): family E and B additions
- parijānāti «полностью понимает»; na parijānāti «не понимает полностью» (pi-5; never «не полностью понимает», which reads as "partly"); parijānittha «полностью понял / поняли»; parijānissati «полностью поймёт». Anusaya pariññā chapters (7-07, 7-08) take the forms from PJ_RU / pj_pred, not from 7-01's TRANSITIVE + «не ».
- yo … so …? = «Кто …, тот …?»; vā pana «А кто …». Persons: Arahā «архат»; Aggamaggasamaṅgī «обладающий высшим путём»; «Те, кто обретёт путь,»; «Кроме обладающего высшим путём и архата, остальные личности».
- «ye ca Xaṃ upapajjitvā parinibbāyissanti» = «и у тех, кто, переродившись …, достигнет окончательного угасания»; «(yatthakaṃ paripuṇṇaṃ kātabbaṃ)» = «(раздел с «где» следует изложить полностью)»; closings «Раздел о прекращении.», «Раздел о протекании завершён.», «Парные вопросы о совокупностях завершены.».

### Shared phrases (coordinator, from 5-01 and 8; all yamakas)
- pavatte (in the course of existence, against at rebirth) = «в течение жизни»; uppādakkhaṇe / bhaṅgakkhaṇe = «в момент возникновения / распада» (8, pi-5); nirodhasamāpanna «вошедшие в медитативное достижение прекращения» (8); citte vattamāne «когда присутствует … ум» (pi-5).
- yassa cittassa anantarā aggamaggaṃ paṭilabhissanti = «у тех, кто обретёт высший путь сразу после данного ума»; ye caññe maggaṃ paṭilabhissanti = «у других, кто обретёт путь»; āpāyika «существ низших миров».
- Several person / time / place intros are joined in the Pāli order «A, B и C»; «у них» only when no person is named (5-01).

### From 7-01 (finished 2026-11-27; build_7-01_ru.py, load with importlib.import_module("build_7-01_ru"); notes-7-01.md; `--probe <ch>` shows coverage)
- Person / place question shape (every yamaka uses it; 2-01 and 8 align to it): yassa … tassa … = «У кого …, у того …?»; yattha … tattha … = «Где …, там …?»; yassa yattha … tassa tattha … = «У кого где …, у того там …?»; vā pana = «А …» at the start of (б).
- No. = Нет. (pi-5); Natthi. = Такого нет.; Āmantā. = Да.
- Partial answers: «У <person> залегает Y, но у него не залегает Z.»; places «<places>: там залегает Y, но там не залегает Z.» (a colon, never a dash); both-form «и залегает Y, и залегает Z»; lists «A, B и C», negated «ни A, ни B».
- anuseti «залегает» (pi-5); the seven tendencies «скрытая склонность к чувственной страсти / неприязни / самомнению / воззрениям / колебанию / страсти к существованию / неведению» (pi-2, pi-5).
- Planes: в мире чувственных желаний / форм / без форм (pi-2). Persons: у двух / трёх / четырёх личностей, у этих же личностей, у этой же личности.
- From 7-03 (build_7-03_ru.py, notes-7-03.md): yato … tato … (no subject in the Pāli) = indefinite 3rd plural «Где имеют …, там имеют …?» (Q_YATO, GENERIC_3PL, question()); the same shape for the other verbs: «Где устраняют …, там устраняют …?», «Где полностью понимают …, там полностью понимают …?». sānusaya «имеет скрытую склонность к X»; negated иметь takes the genitive (NEG_OBJ_CASE). Person answers «Невозвращающийся имеет Y, но не имеет Z»; place answers «<места>: там имеют Y, но там не имеют Z». t_pred / t_clause / t_answers / tr_line(body, mode) handle any 7-01 transitive verb.
### Person groups (coordinator, from 10-08 / 10-09)
- «Pacchimabhavikānaṃ itthīnaṃ / purisānaṃ upapajjantīnaṃ / upapajjantānaṃ» is one group: «У тех, кто в последний раз перерождается женщиной / мужчиной,».
- «Itaresaṃ <attr> upapajjantānaṃ» = «У остальных, кто перерождается …,» (3-03, 5-01); never «У остальных и у тех, кто …».

- Proposed for 7-02 … 7-11 (in notes-7-01.md): pajahati «устраняет», parijānāti «полностью понимает», pahīna «устранена», sānusaya «имеет …».
