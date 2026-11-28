# notes-rails-G7: Anusayayamaka frames (7-01 … 7-11; frame-setter for the anusaya frames)

Format: Pāli = Russian, one per line. Builder: build_rails_G7_ru.py (import with importlib.import_module("build_rails_G7_ru");
importing writes nothing). Functions: np_ru, vp, body_ru, neither, answer, question, na_vattabbo, dhatu, heading, fixed,
translate_line. Tables: ANU, HEAD, VRU, VP, OBJ_CASE, PERSON, EXCEPT, PLACE_RU, REL_RU, CORR_RU, LABELS, VARA, SUBHEAD.
notes_G7_examples.py prints the example lines below from the builder.
Aligned with G2 (build_rails_G2_ru.py; main() cross-checks Нет. / Такого нет. / Архат / Обладающий высшим путём /
полностью понимает / не понимает полностью / Кроме / «у кого где … у того там»): question shapes, «но у него / у них» +
the flipped verb, «и V X, и V Y», «не V ни X, ни Y», and G2's rule that after a place intro the resumptive ettha / tattha /
tato is not rendered and after a person + place intro the pronoun is not rendered while tattha / tato = «там».

## Terms (termbase; pi-2 / pi-5)

anuseti / anusenti = залегает / залегают (pi-5; APPROVED); nānuseti = не залегает
kāmarāgānusayo … avijjānusayo = скрытая склонность к чувственной страсти / к неприязни / к самомнению / к воззрениям / к колебанию / к страсти к существованию / к неведению
X ca Y ca (one verb) = скрытые склонности к X и к Y (head noun once, plural verb); X…pe… Y = скрытая склонность к X… к Y
sānusayo / niranusayo = имеет / не имеет (+ gen. after negation); pajahati = устраняет; parijānāti = полностью понимает; na parijānāti = не понимает полностью (G2)
pahīno / appahīno = устранена / не устранена (pl. устранены); uppajjati = возникает
tadekaṭṭhaṃ (pi-2 «пребывающий вместе с ним») = пребывающую вместе с ней (с ними when the first tendency is a list)
puggala = личность; Anāgāmī невозвращающийся; Arahā архат; Puthujjano обычный человек; Aṭṭhamako личность восьмой ступени;
  Anāgāmimaggasamaṅgī обладающий путём невозвращения; Aggamaggasamaṅgī обладающий высшим путём
places: Kāmadhātuyā dvīsu / tīsu vedanāsu = в мире чувственных желаний в двух / трёх видах чувства; Dukkhāya vedanāya = в болезненном чувстве;
  Rūpadhātuyā / Arūpadhātuyā = в мире форм / в мире без форм; Apariyāpanne = в том, что не принадлежит к кругам существования;
  Sabbasakkāyapariyāpannesu dhammesu = во всех явлениях, принадлежащих к самости; sabbattha (with a negated verb) = нигде
several places = «A, B и C» (Pāli order); a place ending in a clause (apariyāpanne, sakkāyapariyāpannesu) takes a closing comma

## Questions

Kattha kāmarāgānusayo anuseti? = Где залегает скрытая склонность к чувственной страсти?
(Ka) yassa kāmarāgānusayo anuseti tassa paṭighānusayo anusetīti? Āmantā. = (а) У кого залегает скрытая склонность к чувственной страсти, у того залегает скрытая склонность к неприязни? Да.
(Kha) yassa vā pana paṭighānusayo anuseti tassa kāmarāgānusayo anusetīti? No. = (б) А у кого залегает скрытая склонность к неприязни, у того залегает скрытая склонность к чувственной страсти? Нет.
(Ka) yattha kāmarāgānusayo ca paṭighānusayo ca anusenti tattha mānānusayo anusetīti? Natthi. = (а) Где залегают скрытые склонности к чувственной страсти и к неприязни, там залегает скрытая склонность к самомнению? Такого нет.
(Kha) yassa vā pana yattha mānānusayo anuseti tassa tattha kāmarāgānusayo anusetīti? = (б) А у кого где залегает скрытая склонность к самомнению, у того там залегает скрытая склонность к чувственной страсти?
Yassa paṭighānusayo anuseti tassa diṭṭhānusayo…pe… vicikicchānusayo anusetīti? = У кого залегает скрытая склонность к неприязни, у того залегает скрытая склонность к воззрениям… к колебанию?
(Ka) yo kāmarāgānusayena sānusayo so paṭighānusayena sānusayoti? Āmantā. = (а) Кто имеет скрытую склонность к чувственной страсти, тот имеет скрытую склонность к неприязни? Да.
(Ka) yato kāmarāgānusayena sānusayo tato paṭighānusayena sānusayoti? No. = (а) Где имеют скрытую склонность к чувственной страсти, там имеют скрытую склонность к неприязни? Нет.
(Ka) yo yato kāmarāgānusayena sānusayo so tato mānānusayena sānusayoti? Āmantā. = (а) Кто где имеет скрытую склонность к чувственной страсти, тот там имеет скрытую склонность к самомнению? Да.
(Ka) yo kāmarāgānusayaṃ pajahati so mānānusayaṃ pajahatīti? = (а) Кто устраняет скрытую склонность к чувственной страсти, тот устраняет скрытую склонность к самомнению?
(Ka) yo kāmarāgānusayaṃ parijānāti so paṭighānusayaṃ parijānātīti? = (а) Кто полностью понимает скрытую склонность к чувственной страсти, тот полностью понимает скрытую склонность к неприязни?
(Ka) yassa kāmarāgānusayo pahīno tassa paṭighānusayo pahīnoti? = (а) У кого устранена скрытая склонность к чувственной страсти, у того устранена скрытая склонность к неприязни?
yassa / yattha / yassa yattha / yo / yato / yo yato = у кого / где / у кого где / кто / где / кто где; tassa / tattha / tassa tattha / so / tato / so tato = у того / там / у того там / тот / там / тот там
yato … tato … (no subject in the Pāli) and every subjectless verb in the okāsa sections = indefinite 3rd pl. («Где имеют / устраняют / полностью понимают …»)
(Kha) yattha vā pana…pe…? = (б) А где…?

## Answers

Āmantā. = Да.; No. = Нет.; Natthi. = Такого нет.; Āmantā …pe…. = Да…
Anāgāmissa mānānusayo anuseti, no ca tassa kāmarāgānusayo anuseti. = У невозвращающегося залегает скрытая склонность к самомнению, но у него не залегает скрытая склонность к чувственной страсти.
Tiṇṇaṃ puggalānaṃ mānānusayo ca anuseti kāmarāgānusayo ca anuseti. = У трёх личностей и залегает скрытая склонность к самомнению, и залегает скрытая склонность к чувственной страсти.
Anāgāmissa avijjānusayo ca mānānusayo ca anusenti, no ca tassa kāmarāgānusayo ca paṭighānusayo ca anusenti. = У невозвращающегося залегают скрытые склонности к неведению и к самомнению, но у него не залегают скрытые склонности к чувственной страсти и к неприязни.
Anāgāmissa kāmarāgānusayo nānuseti, no ca tassa mānānusayo nānuseti. = У невозвращающегося не залегает скрытая склонность к чувственной страсти, но у него залегает скрытая склонность к самомнению.
Arahato kāmarāgānusayo ca nānuseti mānānusayo ca nānuseti. = У архата не залегает ни скрытая склонность к чувственной страсти, ни к самомнению.
Dvinnaṃ puggalānaṃ vicikicchānusayo nānuseti, no ca tesaṃ kāmarāgānusayo ca paṭighānusayo ca nānusenti. = У двух личностей не залегает скрытая склонность к колебанию, но у них залегают скрытые склонности к чувственной страсти и к неприязни.
Arahato sabbattha kāmarāgānusayo ca nānuseti paṭighānusayo ca nānuseti. = У архата нигде не залегает ни скрытая склонность к чувственной страсти, ни к неприязни.
Dvinnaṃ puggalānaṃ sabbattha…pe…. = У двух личностей нигде…
Kāmadhātuyā dvīsu vedanāsu ettha kāmarāgānusayo anuseti. = В мире чувственных желаний в двух видах чувства залегает скрытая склонность к чувственной страсти.
Sabbasakkāyapariyāpannesu dhammesu ettha diṭṭhānusayo anuseti. = Во всех явлениях, принадлежащих к самости, залегает скрытая склонность к воззрениям.
Rūpadhātuyā arūpadhātuyā ettha mānānusayo anuseti, no ca tattha kāmarāgānusayo anuseti. = В мире форм и в мире без форм залегает скрытая склонность к самомнению, но там не залегает скрытая склонность к чувственной страсти.
Kāmadhātuyā dvīsu vedanāsu ettha mānānusayo ca anuseti kāmarāgānusayo ca anuseti. = В мире чувственных желаний в двух видах чувства и залегает скрытая склонность к самомнению, и залегает скрытая склонность к чувственной страсти.
Anāgāmissa kāmadhātuyā dvīsu vedanāsu rūpadhātuyā arūpadhātuyā tassa tattha mānānusayo anuseti, no ca tassa tattha kāmarāgānusayo anuseti. = У невозвращающегося в мире чувственных желаний в двух видах чувства, в мире форм и в мире без форм там залегает скрытая склонность к самомнению, но у него там не залегает скрытая склонность к чувственной страсти.
Tesaññeva puggalānaṃ kāmadhātuyā dvīsu vedanāsu tesaṃ tattha mānānusayo ca anuseti kāmarāgānusayo ca anuseti. = У этих же личностей в мире чувственных желаний в двух видах чувства там и залегает скрытая склонность к самомнению, и залегает скрытая склонность к чувственной страсти.
Tesaññeva puggalānaṃ rūpadhātuyā arūpadhātuyā apariyāpanne tesaṃ tattha vicikicchānusayo ca nānuseti kāmarāgānusayo ca paṭighānusayo ca nānusenti. = У этих же личностей в мире форм, в мире без форм и в том, что не принадлежит к кругам существования, там не залегают ни скрытая склонность к колебанию, ни к чувственной страсти, ни к неприязни.
Anāgāmī mānānusayena sānusayo, no ca kāmarāgānusayena sānusayo. = Невозвращающийся имеет скрытую склонность к самомнению, но не имеет скрытой склонности к чувственной страсти.
Tayo puggalā mānānusayena ca sānusayā kāmarāgānusayena ca sānusayā. = Три личности и имеют скрытую склонность к самомнению, и имеют скрытую склонность к чувственной страсти.
Rūpadhātuyā arūpadhātuyā tato mānānusayena sānusayo, no ca tato kāmarāgānusayena sānusayo. = В мире форм и в мире без форм имеют скрытую склонность к самомнению, но там не имеют скрытой склонности к чувственной страсти.
Anāgāmī kāmadhātuyā dvīsu vedanāsu rūpadhātuyā arūpadhātuyā so tato mānānusayena sānusayo, no ca so tato kāmarāgānusayena sānusayo. = Невозвращающийся в мире чувственных желаний в двух видах чувства, в мире форм и в мире без форм там имеет скрытую склонность к самомнению, но он там не имеет скрытой склонности к чувственной страсти.
Arahā sabbattha kāmarāgānusayena ca niranusayo paṭighānusayena ca niranusayo. = Архат нигде не имеет ни скрытой склонности к чувственной страсти, ни к неприязни.
Mānānusayena sānusayo. = Имеет скрытую склонность к самомнению. (okāsa sections: Имеют …)
Tadekaṭṭhaṃ pajahati. = Устраняет ту, что пребывает вместе с ней. («те, что пребывают» when the asked tendencies are a list; «с ними» when the first half is a list; okāsa: Устраняют …)
Tadekaṭṭhaṃ parijānāti. = Полностью понимает ту, что пребывает вместе с ней.
Sveva puggalo kāmadhātuyā dvīsu vedanāsu so tato vicikicchānusayaṃ pajahati kāmarāgānusayaṃ tadekaṭṭhaṃ pajahati. = Эта же личность в мире чувственных желаний в двух видах чувства там устраняет скрытую склонность к колебанию, устраняет скрытую склонность к чувственной страсти, пребывающую вместе с ней.
Aggamaggasamaṅgī kāmarāgānusayaṃ nappajahati, no ca so mānānusayaṃ nappajahati. = Обладающий высшим путём не устраняет скрытую склонность к чувственной страсти, но он устраняет скрытую склонность к самомнению.
Dvinnaṃ maggasamaṅgīnaṃ ṭhapetvā avasesā puggalā kāmarāgānusayañca nappajahanti mānānusayañca nappajahanti. = Кроме двух обладающих путём, остальные личности не устраняют ни скрытой склонности к чувственной страсти, ни к самомнению.
Aggamaggasamaṅgiñca aṭṭhamakañca ṭhapetvā avasesā puggalā sabbattha … = Кроме обладающего высшим путём и личности восьмой ступени, остальные личности нигде …
Anāgāmimaggasamaṅgiñca aṭṭhamakañca / Dvinnaṃ maggasamaṅgīnañca aṭṭhamakañca / Aggamaggasamaṅgiṃ / Anāgāmimaggasamaṅgiṃ ṭhapetvā avasesā puggalā = Кроме обладающего путём невозвращения и личности восьмой ступени / двух обладающих путём и личности восьмой ступени / обладающего высшим путём / обладающего путём невозвращения, остальные личности
Anāgāmimaggasamaṅgī kāmarāgānusayaṃ na parijānāti, no ca so mānānusayaṃ na parijānāti. = Обладающий путём невозвращения не понимает полностью скрытую склонность к чувственной страсти, но он полностью понимает скрытую склонность к самомнению.
Anāgāmissa kāmarāgānusayo pahīno, no ca tassa mānānusayo pahīno. = У невозвращающегося устранена скрытая склонность к чувственной страсти, но у него не устранена скрытая склонность к самомнению.
Rūpadhātuyā arūpadhātuyā ettha mānānusayo pahīno; kāmarāgānusayo na vattabbo "pahīno"ti vā "appahīno"ti vā. = В мире форм и в мире без форм устранена скрытая склонность к самомнению; о скрытой склонности к чувственной страсти не следует говорить ни «устранена», ни «не устранена».
X ca Y ca na vattabbā "pahīnā"ti vā "appahīnā"ti vā = о скрытых склонностях к X и к Y не следует говорить ни «устранены», ни «не устранены»
Na vattabbo "pahīno"ti vā "appahīno"ti vā. = Не следует говорить ни «устранена», ни «не устранена».
… (vitthāretabbaṃ). = … (следует развернуть).; (Vitthāretabbaṃ). = (Следует развернуть). (pi-5 vitthāretabbaṃ «следует развернуть»)
persons (gen.): Anāgāmissa / Arahato / Puthujjanassa / Dvinnaṃ / Tiṇṇaṃ / Catunnaṃ puggalānaṃ / Tesaññeva puggalānaṃ / Tasseva puggalassa = У невозвращающегося / У архата / У обычного человека / У двух / трёх / четырёх личностей / У этих же личностей / У этой же личности
persons (nom.): Anāgāmī / Arahā / Puthujjano / Dve / Tayo / Cattāro puggalā / Teva puggalā / Sveva puggalo / Aṭṭhamako = Невозвращающийся / Архат / Обычный человек / Две / Три / Четыре личности / Эти же личности / Эта же личность / Личность восьмой ступени
no ca tassa / tesaṃ / so / te / tattha / tato (+ tattha / tato) = но у него (у неё) / у них / он (она) / они / там (+ там); verb flipped (coordinator)

## Dhātu sections (user: «мирах»)

Kāmadhātuyā cutassa kāmadhātuṃ upapajjantassa kati anusayā anusenti, kati anusayā nānusenti, kati anusayā bhaṅgā? = У того, кто, умерев в мире чувственных желаний, перерождается в мире чувственных желаний, сколько скрытых склонностей залегает, сколько скрытых склонностей не залегает, сколько скрытых склонностей подлежит разделению?
Na kāmadhātuyā na rūpadhātuyā cutassa na kāmadhātuṃ na arūpadhātuṃ upapajjantassa … = У того, кто, умерев не в мире чувственных желаний и не в мире форм, перерождается не в мире чувственных желаний и не в мире без форм, …
kassaci satta anusayā anusenti, kassaci pañca anusayā anusenti, kassaci tayo anusayā anusenti = в одних случаях залегают семь скрытых склонностей, в других случаях залегают пять скрытых склонностей, в третьих случаях залегают три скрытые склонности
satteva anusayā anusenti = залегают именно семь скрытых склонностей
anusayā bhaṅgā natthi = скрытых склонностей, подлежащих разделению, нет (termbase bhaṅgā «подлежать разделению»; aṭṭhakathā «vibhajitabbā»)
Arūpadhātuyā cutassa rūpadhātuyā upapatti nāma natthi, heṭṭhā upapajjamāno kāmadhātuṃyeva upapajjati, satteva anusayā anusenti = У того, кто умер в мире без форм, перерождения в мире форм вообще нет, перерождаясь ниже, он перерождается только в мире чувственных желаний, залегают именно семь скрытых склонностей

## Headings, closings, labels

### Anusayayamakaṃ = ### Парные вопросы о скрытых склонностях
Sattānusayā – kāmarāgānusayo, … = Семь скрытых склонностей – скрытая склонность к чувственной страсти, …, скрытая склонность к неведению.
#### Uppattiṭṭhānavāro = #### Раздел о месте возникновения
#### Mahāvāro 1. anusayavāro = #### Большой раздел 1. Раздел о скрытых склонностях
#### Anusayavāra = #### Раздел о скрытых склонностях
#### Sānusayavāro / Sānusayavāra = #### Раздел об имеющих скрытые склонности
#### Pajahanavāro / Pajahanavāra = #### Раздел об устранении
#### Pariññāvāro / Pariññāvāra = #### Раздел о полном понимании
#### Pahīnavāro / Pahīnavāra = #### Раздел об устранённом
##### Uppajjanavāro = ##### Раздел о возникновении (new: not in ru-zeroshot-terms; = Uppādavāro)
##### (Ka) anulomapuggalo / (Kha) anulomaokāso / (Ga) anulomapuggalokāsā = ##### (а) Утвердительная форма по личности / (б) … по месту / (в) … по личности и месту
##### (Gha) paṭilomapuggalo / (Ṅa) paṭilomaokāso / (Ca) paṭilomapuggalokāsā = ##### (г) Отрицательная форма по личности / (д) … по месту / (е) … по личности и месту
##### (Ka) dhātupucchāvāro = ##### (а) Раздел вопросов о мирах (user)
##### (Kha) dhātuvisajjanāvāro = ##### (б) Раздел ответов о мирах (user)
Uppattiṭṭhānavāro. = Раздел о месте возникновения.; Anusayavāro. / Sānusayavāro. / … = Раздел о … .
Anusayavāre anulomaṃ. = Утвердительная форма в разделе о скрытых склонностях.; Pahīnavāre paṭilomaṃ. = Отрицательная форма в разделе об устранённом.
Dhātupucchāvāro. = Раздел вопросов о мирах.; Dhātuvisajjavāro. = Раздел ответов о мирах.
Anusayayamakaṃ niṭṭhitaṃ. = Парные вопросы о скрытых склонностях завершены.
(Ekamūlakaṃ) / (Dukamūlakaṃ) / (Tika-) / (Catukka-) / (Pañcaka-) / (Chakkamūlakaṃ) = (На основе одной) / (На основе двух) / (… трёх) / (… четырёх) / (… пяти) / (На основе шести)
(Kāmadhātumūlakaṃ) / (Nakāmanarūpadhātumūlakaṃ) = (На основе мира чувственных желаний) / (На основе не мира чувственных желаний и не мира форм) (termbase)
[pahīno (sī. ka.) anusayavārena pana na sameti] = [вариант чтения (Sī., Ka.): pahīno; но с разделом о скрытых склонностях это не согласуется] (placed after the Russian verb)
