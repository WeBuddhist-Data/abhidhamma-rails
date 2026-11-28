# notes-7-01: Anusayayamaka frames (family C) and the person / place question shape

Builder: build_7-01_ru.py (import: `importlib.import_module("build_7-01_ru")`; importing writes nothing; `--probe <ch>` prints how far the frames already cover another chapter, writes nothing). Every repeated string comes from the constants named in [brackets].
Source: [pi-N] = approved Russian of that book (asserted in CROSSBOOK_C); [new] = settled here; [proposal] = not in 7-01, offered for 7-02 … 7-11.

## Names [ANUSAYA_TAIL, anusaya(), SATTANUSAYA]
anusaya = скрытая склонность (acc скрытую склонность, gen скрытой склонности, instr скрытой склонностью) [pi-2, pi-4, pi-5]
kāmarāgānusayo = скрытая склонность к чувственной страсти [pi-2, pi-5]
paṭighānusayo = скрытая склонность к неприязни [pi-2, pi-5]
mānānusayo = скрытая склонность к самомнению [pi-2, pi-5]
diṭṭhānusayo = скрытая склонность к воззрениям [pi-2, pi-5]
vicikicchānusayo = скрытая склонность к колебанию [pi-2, pi-5]
bhavarāgānusayo = скрытая склонность к страсти к существованию [pi-2, pi-5]
avijjānusayo = скрытая склонность к неведению [pi-2, pi-5]
Sattānusayā – kāmarāgānusayo, … avijjānusayo. = Семь скрытых склонностей – скрытая склонность к чувственной страсти, …, скрытая склонность к страсти к существованию и скрытая склонность к неведению. [pi-2 16, exact; assert]

## Lists [parse_list(), ru_list()]
A ca B ca C ca (one verb) = A, B и C [new; «и» only where the Pāli has ca]
no ca … A ca B ca (negated list) = ни A, ни B [new; a partial answer says plainly that none of them]
A…pe… B = A… B ; A ca…pe… B ca = A… и B ; a "…pe…" series never takes «ни» (asked in turn) [new]
Plural verb before a list subject: anusenti = залегают [new]

## Verbs [VERB, TRANSITIVE]
anuseti / anusenti = залегает / залегают [pi-5 21 «В болезненном чувстве залегает скрытая склонность к страсти»; assert]
nānuseti / nānusenti = не залегает / не залегают [new]
uppajjati / nuppajjati = возникает / не возникает [sample uppāda = возникновение]
pahīno / pahīnā = устранена / устранены; appahīno, nappahīno = не устранена [pi-5 «у архата страсть устранена»]
pajahati = устраняет (+ acc) [proposal; Pajahanavāro = Раздел об устранении]
parijānāti = полностью понимает (+ acc) [proposal; Pariññāvāro = Раздел о полном понимании]
X-ena sānusayo / niranusayo = имеет / не имеет скрытую склонность к X [proposal; Sānusayavāro = Раздел об имеющих скрытые склонности]

## Persons and places [PERSON_GEN, PERSON_NOM, PERSON_FEM, RES, RES_FEM, LOCI]
Anāgāmissa = у невозвращающегося [pi-5; assert] ; Arahato = у архата [pi-5] ; Puthujjanassa = у обычного человека [pi-5; assert]
Dvinnaṃ / Tiṇṇaṃ / Catunnaṃ puggalānaṃ = у двух / трёх / четырёх личностей [new; puggala = личность]
Tesaññeva puggalānaṃ = у этих же личностей ; Tasseva puggalassa = у этой же личности [new]
tassa / tesaṃ (resumptive) = у него / у них; after «у этой же личности»: у неё [new]
ettha / tattha (after places) = там [new; both resumptive]
tassa tattha / tesaṃ tattha = у него там / у них там [new]
Kāmadhātuyā = в мире чувственных желаний [pi-1, pi-2; assert] ; rūpadhātuyā = в мире форм ; arūpadhātuyā = в мире без форм [pi-2; assert]
dvīsu vedanāsu / tīsu vedanāsu = в двух / трёх видах чувства [new; «видов» as pi-2 «семь видов контакта»]
dukkhāya vedanāya = в болезненном чувстве [pi-1, pi-5]
Sabbasakkāyapariyāpannesu dhammesu = во всех явлениях, входящих в самость [new; sakkāya pi-1 «воззрение о самости», pariyāpanna pi-5 «входит в»]
apariyāpanne = в не принадлежащем к кругам существования [proposal; pi-1 apariyāpanna]
Places in a row stay without a conjunction, as in the Pāli: «в мире форм, в мире без форм».
PERSON_NOM (yo-type, proposal): anāgāmī невозвращающийся, arahā архат, puthujjano обычный человек, tayo puggalā три личности, teva puggalā эти же личности; so / te = он / они.

## Question frames (general shape) [UPPATTI_Q, Q_PERSON, Q_PLACE, Q_PERSON_PLACE, Q_WHO, Q_WHO_PLACE, KHA_PREFIX]
Kattha X anuseti? = Где залегает X? [new]
yassa X anuseti tassa Y anusetīti? = У кого залегает X, у того залегает Y? [new]
yattha X anuseti tattha Y anusetīti? = Где залегает X, там залегает Y? [new; also yato … tato …, proposal]
yassa yattha X anuseti tassa tattha Y anusetīti? = У кого где залегает X, у того там залегает Y? [new]
yo X-aṃ pajahati so Y-aṃ pajahatīti? = Кто устраняет X, тот устраняет Y? [proposal]
yo yato … so tato …? = Кто где …, тот там …? [proposal]
(Kha) … vā pana … = (б) А у кого / А где … [new; as the sample's «А все …»]
-ti before "?" = not rendered [sample]

## Answers [NO, NATTHI, B.AMANTA, ANSWER_INTRO_*, BOTH_FRAME, BOTH_NEG_FRAME, NO_CA_FRAME, NO_CA_POS_FRAME, no_ca(), both_neg()]
Āmantā. = Да. [pi-5] ; No. = Нет. [pi-5; assert] ; Natthi. = Такого нет. [new]
Person X Y anuseti, no ca tassa Z anuseti. = У X залегает Y, но у него не залегает Z. [new]
Places ettha Y anuseti, no ca tattha Z anuseti. = <Места>: там залегает Y, но там не залегает Z. [new; colon instead of a dash]
Person places tassa tattha Y anuseti, no ca tassa tattha Z anuseti. = У X <места>: у него там залегает Y, но у него там не залегает Z. [new]
… Y ca anuseti Z ca anuseti. = … и залегает Y, и залегает Z. (repeated verb kept) [new]
… Y ca anuseti Z ca W ca anusenti. = … и залегает Y, и залегают Z и W. [new]
… Y nānuseti, no ca tassa Z nānuseti. = … не залегает Y, но у него залегает Z. [coordinator; NO_CA_POS_FRAME / no_ca(); "no" negates the verb that follows; never «но не так, что» (NO_CA_NEG_FRAME is deprecated)]
Same for every prepared verb via no_ca(): no ca … nuppajjati = но … возникает; no ca … nappahīno = но … устранена; no ca so … nappajahati = но он устраняет … [coordinator]
… Y ca nānuseti Z ca nānuseti. = … не залегает ни Y, ни Z. [coordinator; BOTH_NEG_FRAME / both_neg(): verb once; plural «не залегают ни Y, ни A, ни B» when a Pāli verb is plural or a list follows; RU_PLURAL]
The positive pair stays «и залегает Y, и залегает Z» [BOTH_FRAME].

## Headings and closings [heading(), MULAKA, VARO_CLOSING, ANUSAYAVARE_FRAME, EXTRA_HEADINGS]
Headings (coordinator decision): the first word, and the first word after a label or a number, is capitalised [heading_case()]: «##### (а) Утвердительная форма по личности», «#### Большой раздел 1. Раздел о скрытых склонностях», «(б) Раздел ответов об элементах»; text from build_sample_ru.SECTION_HEADINGS.
Uppattiṭṭhānavāro. (closing) = Раздел о месте возникновения. [new]
(Ekamūlakaṃ) / (Dukamūlakaṃ) / (Tikamūlakaṃ) / (Catukkamūlakaṃ) / (Pañcakamūlakaṃ) / (Chakkamūlakaṃ) = (На основе одного / двух / трёх / четырёх / пяти / шести) [new]
(Kāmadhātumūlakaṃ) / (Rūpadhātumūlakaṃ) / (Arūpadhātumūlakaṃ) = (На основе мира чувственных желаний / мира форм / мира без форм) [proposal]
Anusayavāre anulomaṃ. / paccanīkaṃ. = Утвердительная / Отрицательная форма в разделе о скрытых склонностях. [new / proposal]
(vitthāretabbaṃ) = (следует развернуть) [pi-5; proposal]
Tadekaṭṭhaṃ pajahati. = Устраняет то, что пребывает вместе с ней. [proposal; tadekaṭṭha pi-1 «пребывающие вместе с ними»]
Uppajjanavāro = Раздел о возникновении [proposal; same Russian as Uppādavāro]
dhātupucchāvāro = раздел вопросов об элементах [proposal; pairs with dhātuvisajjanāvāro]
Kāmadhātuyā cutassa (na) rūpadhātuṃ upapajjantassa = у того, кто, уйдя из мира чувственных желаний, перерождается (не) в мире форм [proposal; cuta pi-4 «уйдя из мира», upapajjati pi-2]
kati anusayā anusenti, kati anusayā nānusenti, kati anusayā bhaṅgā? = сколько скрытых склонностей залегает, сколько скрытых склонностей не залегает, сколько скрытых склонностей разрушено? [proposal]
kassaci satta anusayā anusenti = у некоторых залегают семь скрытых склонностей [proposal; kassaci pi-2] ; anusayā bhaṅgā natthi = разрушенных скрытых склонностей нет [proposal]

## Source slips (rendered as meant)
"kāmārāgānusayo" (Pāli lines 166, block ^6-7-21; 206, block ^6-7-25) = kāmarāgānusayo.
^6-7-35 "anusanti" = anusenti.
^6-7-8 "(Ekamūlakaṃ )" and ^6-7-27 "diṭṭhānusayo …pe…": spacing only.
