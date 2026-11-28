# G8 (8-cittayamaka): Russian rails, cittayamaka frames (frame-setter)

Builder: build_rails_G8_ru.py (import with importlib.import_module("build_rails_G8_ru"); importing writes nothing;
`--probe` checks without writing). Functions: pred_ru, both_ru, neither_ru, question, q_bare, q_passed, mind, answer,
translate_line. Tables: VERB, MIND, INTRO, TIME_NP, RESUME, HEAD, FIXED.
Aligned with G2 (build_rails_G2_ru.py): past tense imperfective by gender («возникал»), «но у них» + the flipped verb,
«и является A, и является B», «не являются ни A, ни B», «То, что не является …, не является …?», groups «A, B и C».
Difference: G2 puts the verb before its long khandha subjects; here «ум» stands before the predicate (citta predicates
are «X, но не Y» pairs and copular participles).

## Verbs and participles (termbase)
uppajjati / uppajjittha / uppajjissati = возникает / возникал / возникнет (pl. возникают / возникали / возникнут)
nirujjhati / nirujjhittha / nirujjhissati = прекращается / прекращался / прекратится
uppannaṃ = является возникшим; uppajjamānaṃ = является возникающим
nirujjhamānaṃ = является прекращающимся; niruddhaṃ = является прекратившимся
X na Y (one member negated) = «X, но не Y» (uppajjati na nirujjhati = возникает, но не прекращается)
X ceva Y ca = и X, и Y (verb repeated: и является возникшим, и возникает)
na ceva X na ca Y = ни X, ни Y (ни возникает, ни является возникшим); two participles = не является ни A, ни B
no ca … Y = но … не Y; no ca … na Y = но … Y (coordinator negatives rule)

## Questions
yassa cittaṃ P1 tassa cittaṃ P2? = У кого ум P1, у того ум P2?
yassa vā pana … = А у кого …
yaṃ cittaṃ P1 taṃ cittaṃ P2? = Какой ум P1, тот ум P2?
yassa yaṃ cittaṃ P1 tassa taṃ cittaṃ P2? = У кого какой ум P1, у того тот ум P2?
yassa cittaṃ P1 no ca tassa cittaṃ P0, tassa cittaṃ P2? = У кого ум P1, но у него ум не P0, у того ум P2?
yaṃ cittaṃ P1 no ca taṃ cittaṃ P0, taṃ cittaṃ P2? = Какой ум P1, но этот ум не P0, тот ум P2?
yassa yaṃ … no ca tassa taṃ cittaṃ P0, … = У кого какой ум P1, но у него этот ум не P0, у того тот ум P2?
uppannaṃ uppajjamānaṃ? = То, что является возникшим, является возникающим?
na uppannaṃ na uppajjamānaṃ? = То, что не является возникшим, не является возникающим?
uppajjamānaṃ khaṇaṃ khaṇaṃ vītikkantaṃ atikkantakālaṃ = миновал момент возникновения, этот момент, и время его прошло (APPROVED: the noun stays; aṭṭhakathā «tameva uppādakkhaṇaṃ vītikkantaṃ»)
na nirujjhamānaṃ khaṇaṃ khaṇaṃ vītikkantaṃ atikkantakālaṃ = не миновал момент прекращения, этот момент, и время его не прошло
… tassa cittaṃ? / taṃ cittaṃ? / tassa taṃ cittaṃ? (Atikkantakālavāra) = у того ум таков? / тот ум таков? / у того тот ум таков?
Yassa sarāgaṃ cittaṃ uppajjati… = У кого ум, охваченный страстью, возникает…

## Answers
Āmantā. = Да.; No. = Нет.; Natthi. = Такого нет.; Uppajjittha. = Возникал.; Uppannaṃ. = Является возникшим.
Pacchimacittassa uppādakkhaṇe tesaṃ = В момент возникновения последнего ума у них
Pacchimacittassa bhaṅgakkhaṇe tesaṃ = В момент распада последнего ума у них
Cittassa uppādakkhaṇe / bhaṅgakkhaṇe tesaṃ = В момент возникновения / распада ума у них
Itaresaṃ cittassa uppādakkhaṇe tesaṃ = У остальных в момент возникновения ума
Nirodhasamāpannānaṃ asaññasattānaṃ tesaṃ = У вошедших в медитативное достижение прекращения и у существ без восприятия
Cittassa bhaṅgakkhaṇe nirodhasamāpannānaṃ asaññasattānaṃ tesaṃ = В момент распада ума, у вошедших в медитативное достижение прекращения и у существ без восприятия
Pacchimacittasamaṅgīnaṃ tesaṃ = У обладающих последним умом; Cittasamaṅgīnaṃ = У обладающих умом
Itaresaṃ tesaṃ = У остальных; Itaresaṃ cittasamaṅgīnaṃ = У остальных обладающих умом
no ca tesaṃ cittaṃ = но у них ум; no ca taṃ cittaṃ = но этот ум (after two minds: но эти умы)
no ca tassa taṃ cittaṃ = но у него этот ум (after two minds: но у него эти умы)
Bhaṅgakkhaṇe / Uppādakkhaṇe cittaṃ = Ум в момент распада / возникновения
Atītaṃ / Anāgataṃ / Paccuppannaṃ cittaṃ = Прошлый / Будущий / Настоящий ум
Atītānāgataṃ cittaṃ = Прошлый и будущий ум (singular verb, as the Pāli)
Bhaṅgakkhaṇe anāgatañca cittaṃ = Ум в момент распада и будущий ум (plural verb)
Uppādakkhaṇe anāgatañca cittaṃ = Ум в момент возникновения и будущий ум (plural verb)
Bhaṅgakkhaṇe uppannaṃ, no ca uppajjamānaṃ. = В момент распада оно является возникшим, но не является возникающим.

## Minds (pi-2 list; termbase)
sarāgaṃ / vītarāgaṃ = ум, охваченный страстью / ум, свободный от страсти; sadosaṃ / vītadosaṃ = … злобой / от злобы
samohaṃ / vītamohaṃ = … заблуждением / от заблуждения; saṃkhittaṃ / vikkhittaṃ = сжатый / рассеянный ум
mahaggataṃ / amahaggataṃ = возвышенный / невозвышенный ум; sauttaraṃ / anuttaraṃ = ум, имеющий / не имеющий над собой высшее(го)
samāhitaṃ / asamāhitaṃ = сосредоточенный / несосредоточенный ум; vimuttaṃ / avimuttaṃ = освобождённый / неосвобождённый ум
kusalaṃ / akusalaṃ / abyākataṃ cittaṃ = благой / неблагой / этически неопределённый ум
sukhāya vedanāya sampayuttaṃ = ум, связанный с приятным чувством (pi-1); araṇaṃ = ум, свободный от борьбы
yāva saraṇaaraṇā = вплоть до сопряжённых с борьбой и свободных от борьбы

## Notes and colophon
(Etena upāyena yāva saraṇaaraṇā uddharitabbā.) = (Этим способом их следует излагать вплоть до сопряжённых с борьбой и свободных от борьбы.)
Yassa / yaṃ / yassa yaṃ cittake = в разделе с «у кого ум» / «какой ум» / «у кого какой ум»
Cittayamakaṃ niṭṭhitaṃ. = Парные вопросы об уме завершены.
