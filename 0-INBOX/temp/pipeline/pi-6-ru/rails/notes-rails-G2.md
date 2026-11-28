# notes-rails-G2: Khandhayamaka frames (paṇṇatti, pavatti, pariññā)

Format: Pāli = Russian, one per line. Builder: build_rails_G2_ru.py (import with importlib; importing writes
nothing). Later groups register their nouns with G2.register_term(...) and call G2.translate_line(...), or use
the frame functions directly: pn_question_line, pn_answer, pv_question, partial, pair, person_answer,
place_answer, intro, short_answer, pv_fragment, pr_question_line, pr_answer, heading, colophon, var_br.
X / Y = any registered noun (nom / acc / gen / ins / gender); verbs agree with their noun.
New planes / persons: add to PL_ACC / PL_LOC / PL_ABL / BEINGS, then set G2.GROUP_RULES = None (rebuilt on
the next call); or append (regex, fn) pairs to G2.GROUP_RULES after G2.intro_groups('') has built it.
New pariññā-type verbs: TVERB; new subjects: PERSONS (pariññā), SUBJ (paṇṇatti).

## Paṇṇatti (naming) frames

(Ka) rūpaṃ rūpakkhandho? = (а) Форма является совокупностью материальной формы?
(Kha) rūpakkhandho rūpaṃ? = (б) Совокупность материальной формы является формой?
(Ka) saṅkhārā saṅkhārakkhandho? = (а) Формирующие факторы являются совокупностью формирующих факторов?
(Kha) khandhā vedanākkhandho? = (б) Совокупности являются совокупностью чувств?
(Ka) rūpaṃ khandho? = (а) Форма является совокупностью?
(Kha) khandhā rūpaṃ? = (б) Совокупности являются формой?
(Ka) na rūpaṃ na rūpakkhandho? = (а) То, что не является формой, не является совокупностью материальной формы?
(Kha) na khandhā na vedanākkhandho? = (б) То, что не является совокупностями, не является совокупностью чувств?
(Ka) na saṅkhārā na khandho? = (а) То, что не является формирующими факторами, не является совокупностью?
(Ka) rūpaṃ rūpakkhandhoti? = (а) Форма является совокупностью материальной формы?
Piyarūpaṃ sātarūpaṃ rūpaṃ, na rūpakkhandho. = Привлекательная форма, отрадная форма является формой, но не является совокупностью материальной формы.
Rūpakkhandho rūpañceva rūpakkhandho ca. = Совокупность материальной формы и является формой, и является совокупностью материальной формы.
Diṭṭhisaññā saññā, na saññākkhandho. = Восприятие-воззрение является восприятием, но не является совокупностью восприятия.
Saññākkhandho saññā ceva saññākkhandho ca. = Совокупность восприятия и является восприятием, и является совокупностью восприятия.
Saṅkhārakkhandhaṃ ṭhapetvā avasesā saṅkhārā, na saṅkhārakkhandho. = Кроме совокупности формирующих факторов, остальные являются формирующими факторами, но не являются совокупностью формирующих факторов.
Piyarūpaṃ sātarūpaṃ na rūpakkhandho, rūpaṃ. = Привлекательная форма, отрадная форма не является совокупностью материальной формы, но является формой.
Rūpañca rūpakkhandhañca ṭhapetvā avasesā na ceva rūpaṃ na ca rūpakkhandho. = Кроме формы и совокупности материальной формы, остальные не являются ни формой, ни совокупностью материальной формы.
Saṅkhārakkhandhaṃ ṭhapetvā avasesā na saṅkhārakkhandho, saṅkhārā. = Кроме совокупности формирующих факторов, остальные не являются совокупностью формирующих факторов, но являются формирующими факторами.
Vedanākkhandho khandho ceva vedanākkhandho ca. = Совокупность чувств и является совокупностью, и является совокупностью чувств.
Avasesā khandhā na vedanākkhandho. = Остальные совокупности не являются совокупностью чувств.
Rūpaṃ ṭhapetvā avasesā khandhā na rūpaṃ, khandhā. = Кроме формы, остальные совокупности не являются формой, но являются совокупностями.
Rūpañca khandhe ca ṭhapetvā avasesā na ceva rūpaṃ na ca khandhā. = Кроме формы и совокупностей, остальные не являются ни формой, ни совокупностями.
X Y? = X является Y? (Y instrumental; plural X: являются); na X na Y? = То, что не является X, не является Y?
S B, na C. = S является B, но не является C.;  S na C, B. = S не является C, но является B.
A B ceva C ca. = A и является B, и является C. (user rule: no relative clause -> «и …, и …» with the verb twice)
X ṭhapetvā avasesā = Кроме X(gen), остальные (pl.);  X-ñca Y-ñca ṭhapetvā avasesā na ceva A na ca B = Кроме X и Y, остальные не являются ни A, ни B.
piyarūpaṃ sātarūpaṃ = привлекательная форма, отрадная форма (piya / sāta as pi-2 «привлекательно и отрадно»; rūpa = форма: termbase bare-word sense)

## Pavatti frames: questions

(Ka) yassa rūpakkhandho uppajjati tassa vedanākkhandho uppajjatīti? = (а) У кого возникает совокупность материальной формы, у того возникает совокупность чувств?
(Kha) yassa vā pana vedanākkhandho uppajjati tassa rūpakkhandho uppajjatīti? = (б) А у кого возникает совокупность чувств, у того возникает совокупность материальной формы?
(Ka) yattha rūpakkhandho uppajjati tattha vedanākkhandho uppajjatīti? = (а) Где возникает совокупность материальной формы, там возникает совокупность чувств?
(Kha) yattha vā pana vedanākkhandho uppajjati tattha rūpakkhandho uppajjatīti? = (б) А где возникает совокупность чувств, там возникает совокупность материальной формы?
(Ka) yassa yattha rūpakkhandho uppajjati tassa tattha vedanākkhandho uppajjatīti? = (а) У кого где возникает совокупность материальной формы, у того там возникает совокупность чувств?
(Kha) yassa vā pana yattha vedanākkhandho uppajjati tassa tattha rūpakkhandho uppajjatīti? = (б) А у кого где возникает совокупность чувств, у того там возникает совокупность материальной формы?
(Ka) yassa rūpakkhandho nuppajjati tassa vedanākkhandho nuppajjatīti? = (а) У кого не возникает совокупность материальной формы, у того не возникает совокупность чувств?
(Ka) yassa rūpakkhandho uppajjittha tassa vedanākkhandho uppajjitthāti? = (а) У кого возникала совокупность материальной формы, у того возникала совокупность чувств?
(Ka) yassa rūpakkhandho nuppajjittha tassa vedanākkhandho nuppajjitthāti? = (а) У кого не возникала совокупность материальной формы, у того не возникала совокупность чувств?
(Ka) yassa rūpakkhandho uppajjissati tassa vedanākkhandho uppajjissatīti? = (а) У кого возникнет совокупность материальной формы, у того возникнет совокупность чувств?
(Ka) yassa rūpakkhandho nuppajjissati tassa vedanākkhandho nuppajjissatīti? = (а) У кого не возникнет совокупность материальной формы, у того не возникнет совокупность чувств?
(Ka) yassa rūpakkhandho nirujjhati tassa vedanākkhandho nirujjhatīti? = (а) У кого прекращается совокупность материальной формы, у того прекращается совокупность чувств?
(Ka) yassa rūpakkhandho na nirujjhati tassa vedanākkhandho na nirujjhatīti? = (а) У кого не прекращается совокупность материальной формы, у того не прекращается совокупность чувств?
(Ka) yassa rūpakkhandho nirujjhittha tassa vedanākkhandho nirujjhitthāti? = (а) У кого прекращалась совокупность материальной формы, у того прекращалась совокупность чувств?
(Ka) yassa rūpakkhandho na nirujjhittha tassa vedanākkhandho na nirujjhitthāti? = (а) У кого не прекращалась совокупность материальной формы, у того не прекращалась совокупность чувств?
(Ka) yassa rūpakkhandho nirujjhissati tassa vedanākkhandho nirujjhissatīti? = (а) У кого прекратится совокупность материальной формы, у того прекратится совокупность чувств?
(Ka) yassa rūpakkhandho na nirujjhissati tassa vedanākkhandho na nirujjhissatīti? = (а) У кого не прекратится совокупность материальной формы, у того не прекратится совокупность чувств?
(Ka) yassa rūpakkhandho uppajjati tassa vedanākkhandho uppajjitthāti? = (а) У кого возникает совокупность материальной формы, у того возникала совокупность чувств?
(Ka) yassa rūpakkhandho uppajjati tassa vedanākkhandho uppajjissatīti? = (а) У кого возникает совокупность материальной формы, у того возникнет совокупность чувств?
(Ka) yassa rūpakkhandho uppajjittha tassa vedanākkhandho uppajjissatīti? = (а) У кого возникала совокупность материальной формы, у того возникнет совокупность чувств?
(Ka) yassa rūpakkhandho uppajjati tassa vedanākkhandho nirujjhatīti? = (а) У кого возникает совокупность материальной формы, у того прекращается совокупность чувств?
(Ka) yassa rūpakkhandho nuppajjati tassa vedanākkhandho na nirujjhatīti? = (а) У кого не возникает совокупность материальной формы, у того не прекращается совокупность чувств?
(Ka) yassa rūpakkhandho nuppajjittha tassa vedanākkhandho na nirujjhissatīti? = (а) У кого не возникала совокупность материальной формы, у того не прекратится совокупность чувств?
verbs (termbase; by the gender of their noun): uppajjati возникает / возникают; uppajjittha возникал(а, о, и);
  uppajjissati возникнет / возникнут; nirujjhati прекращается; nirujjhittha прекращался(ась, ось, ись);
  nirujjhissati прекратится; nuppajjati / na nirujjhati … = не + the same form

## Pavatti frames: answers

Āmantā. = Да.
No. = Нет.
Natthi. = Такого нет.
Uppajjati. / Uppajjittha. / Uppajjissati. / Nirujjhati. / Nirujjhittha. / Nirujjhissati. = Возникает. / Возникала. / Возникнет. / Прекращается. / Прекращалась. / Прекратится. (gender of the question's 2nd noun)
Asaññasattaṃ upapajjantānaṃ tesaṃ rūpakkhandho uppajjati, no ca tesaṃ vedanākkhandho uppajjati. = У тех, кто перерождается среди существ без восприятия, возникает совокупность материальной формы, но у них не возникает совокупность чувств.
Pañcavokāraṃ upapajjantānaṃ tesaṃ rūpakkhandho ca uppajjati vedanākkhandho ca uppajjati. = У тех, кто перерождается в существовании с пятью составляющими, и возникает совокупность материальной формы, и возникает совокупность чувств.
Arūpaṃ upapajjantānaṃ tesaṃ rūpakkhandho nuppajjati, no ca tesaṃ vedanākkhandho nuppajjati. = У тех, кто перерождается в мире без форм, не возникает совокупность материальной формы, но у них возникает совокупность чувств.
Sabbesaṃ cavantānaṃ tesaṃ rūpakkhandho ca nuppajjati vedanākkhandho ca nuppajjati. = У всех, кто умирает, не возникает ни совокупность материальной формы, ни совокупность чувств.
Asaññasatte tattha rūpakkhandho uppajjati, no ca tattha vedanākkhandho uppajjati. = Среди существ без восприятия возникает совокупность материальной формы, но там не возникает совокупность чувств.
Pañcavokāre tattha rūpakkhandho ca uppajjati vedanākkhandho ca uppajjati. = В существовании с пятью составляющими и возникает совокупность материальной формы, и возникает совокупность чувств.
Asaññasattaṃ upapajjantānaṃ tesaṃ tattha rūpakkhandho uppajjati, no ca tesaṃ tattha vedanākkhandho uppajjati. = У тех, кто перерождается среди существ без восприятия, там возникает совокупность материальной формы, но у них там не возникает совокупность чувств.
Asaññasattānaṃ tesaṃ tattha rūpakkhandho uppajjittha, no ca tesaṃ tattha vedanākkhandho uppajjittha. = У существ без восприятия там возникала совокупность материальной формы, но у них там не возникала совокупность чувств.
Suddhāvāsānaṃ tesaṃ tattha rūpakkhandho ca nuppajjittha vedanākkhandho ca nuppajjittha. = У существ Чистых обителей там не возникала ни совокупность материальной формы, ни совокупность чувств.
Ye arūpaṃ upapajjitvā parinibbāyissanti tesaṃ vedanākkhandho uppajjissati, no ca tesaṃ rūpakkhandho uppajjissati. = У тех, кто, переродившись в мире без форм, достигнет окончательного угасания, возникнет совокупность чувств, но у них не возникнет совокупность материальной формы.
Itaresaṃ tesaṃ vedanākkhandho ca uppajjissati rūpakkhandho ca uppajjissati. = У остальных и возникнет совокупность чувств, и возникнет совокупность материальной формы.
Pacchimabhavikānaṃ tesaṃ rūpakkhandho ca nuppajjissati vedanākkhandho ca nuppajjissati. = У тех, кто живёт последней жизнью, не возникнет ни совокупность материальной формы, ни совокупность чувств.
Sabbesaṃ cavantānaṃ arūpaṃ upapajjantānaṃ tesaṃ vedanākkhandho uppajjittha, no ca tesaṃ rūpakkhandho uppajjati. = У всех, кто умирает, и у тех, кто перерождается в мире без форм, возникала совокупность чувств, но у них не возникает совокупность материальной формы.
Itaresaṃ pañcavokāraṃ upapajjantānaṃ tesaṃ tattha rūpakkhandho ca uppajjati vedanākkhandho ca uppajjittha. = У остальных, кто перерождается в существовании с пятью составляющими, там и возникает совокупность материальной формы, и возникала совокупность чувств.
Pañcavokārā cavantānaṃ arūpānaṃ tesaṃ tattha vedanākkhandho uppajjittha, no ca tesaṃ tattha rūpakkhandho uppajjati. = У тех, кто умирает в существовании с пятью составляющими, и у существ мира без форм там возникала совокупность чувств, но у них там не возникает совокупность материальной формы.
Catuvokāraṃ pañcavokāraṃ upapajjantānaṃ tesaṃ saññākkhandho ca uppajjittha vedanākkhandho ca uppajjati. = У тех, кто перерождается в существовании с четырьмя составляющими и в существовании с пятью составляющими, и возникала совокупность восприятия, и возникает совокупность чувств.
Suddhāvāse parinibbantānaṃ asaññasattā cavantānaṃ tesaṃ tattha rūpakkhandho ca nuppajjati vedanākkhandho ca nuppajjittha. = У тех, кто достигает окончательного угасания в Чистых обителях, и у тех, кто умирает среди существ без восприятия, там и не возникает совокупность материальной формы, и не возникала совокупность чувств.
Pacchimabhavikānaṃ pañcavokāraṃ upapajjantānaṃ tesaṃ rūpakkhandho uppajjati, no ca tesaṃ vedanākkhandho uppajjissati. = У тех, кто в последний раз перерождается в существовании с пятью составляющими, возникает совокупность материальной формы, но у них не возникнет совокупность чувств.
Pañcavokāre parinibbantānaṃ arūpe pacchimabhavikānaṃ asaññasattā cavantānaṃ tesaṃ tattha rūpakkhandho ca nuppajjati vedanākkhandho ca nuppajjissati. = У тех, кто достигает окончательного угасания в существовании с пятью составляющими, у тех, кто живёт последней жизнью в мире без форм, и у тех, кто умирает среди существ без восприятия, там и не возникает совокупность материальной формы, и не возникнет совокупность чувств.
Itaresaṃ catuvokārānaṃ pañcavokārānaṃ tesaṃ tattha vedanākkhandho ca uppajjittha saññākkhandho ca uppajjissati. = У остальных существ с четырьмя составляющими и существ с пятью составляющими там и возникала совокупность чувств, и возникнет совокупность восприятия.
Pacchimabhavikānaṃ arūpaṃ upapajjantānaṃ ye ca arūpaṃ upapajjitvā parinibbāyissanti tesaṃ cavantānaṃ tesaṃ vedanākkhandho nirujjhissati, no ca tesaṃ rūpakkhandho nirujjhissati. = У тех, кто в последний раз перерождается в мире без форм, и у тех умирающих, кто, переродившись в мире без форм, достигнет окончательного угасания, прекратится совокупность чувств, но у них не прекратится совокупность материальной формы.
Catuvokārā pañcavokārā cavantānaṃ tesaṃ rūpakkhandho nuppajjati, no ca tesaṃ vedanākkhandho na nirujjhati. = У тех, кто умирает в существовании с четырьмя составляющими и в существовании с пятью составляющими, не возникает совокупность материальной формы, но у них прекращается совокупность чувств.
Arūpaṃ upapajjantānaṃ asaññasattā cavantānaṃ tesaṃ rūpakkhandho ca nuppajjati vedanākkhandho ca na nirujjhati. = У тех, кто перерождается в мире без форм, и у тех, кто умирает среди существ без восприятия, и не возникает совокупность материальной формы, и не прекращается совокупность чувств.
no ca tesaṃ (tattha) Y V = но у них (там) не V Y; no ca tesaṃ Y na V / nuppajjati = но у них V Y (coordinator)
X ca V Y ca V (positive) = и V X, и V Y; X ca na V Y ca na V (same verb) = не V ни X, ни Y (coordinator);
  different verbs / tenses: и V1 X, и V2 Y (each with its own «не» where negated)
person intro + tesaṃ: the resumptive tesaṃ is not rendered; place + tattha: the resumptive tattha is not
  rendered; tesaṃ tattha after a person intro = «… там»; several groups joined «A, B и C» (Pāli order)
person groups: sabbesaṃ cavantānaṃ / upapajjantānaṃ = у всех, кто умирает / перерождается;
  X-aṃ upapajjantānaṃ = у тех, кто перерождается в X; X-ā cavantānaṃ = у тех, кто умирает в X;
  pacchimabhavikānaṃ (X-aṃ) upapajjantānaṃ = у тех, кто в последний раз перерождается (в X) (APPROVED);
  (X-e) pacchimabhavikānaṃ = у тех, кто живёт последней жизнью (в X); (X-e) parinibbantānaṃ = у тех, кто
  достигает окончательного угасания (в X); X-ānaṃ = у существ X; itaresaṃ = у остальных; itaresaṃ X-aṃ
  upapajjantānaṃ = у остальных, кто перерождается в X (APPROVED); itaresaṃ X-ānaṃ = у остальных существ X;
  ye X-aṃ upapajjitvā parinibbāyissanti = у тех, кто, переродившись в X, достигнет окончательного угасания;
  ye ca X-aṃ upapajjitvā parinibbāyissanti tesaṃ cavantānaṃ = у тех умирающих, кто, переродившись в X, …
planes (termbase): pañcavokāra в существовании с пятью составляющими / существ с пятью составляющими;
  catuvokāra … с четырьмя составляющими; arūpa в мире без форм / существ мира без форм; asaññasatta
  среди существ без восприятия / существ без восприятия; suddhāvāsa в Чистых обителях / существ Чистых обителей
Yattha rūpakkhandho nirujjhati…pe…. = Где прекращается совокупность материальной формы…
Yattha rūpakkhandho na nirujjhati (yatthakaṃ paripuṇṇaṃ kātabbaṃ). = Где не прекращается совокупность материальной формы (раздел с «где» следует изложить полностью).
(Yathā uppādavāre paccuppannātītaṃ vibhattaṃ tathā idha vibhajitabbaṃ). = (Как в разделе о возникновении разобрано настоящее и прошлое, так и здесь следует разобрать.)

## Pariññā frames

(Ka) yo rūpakkhandhaṃ parijānāti so vedanākkhandhaṃ parijānātīti? = (а) Кто полностью понимает совокупность материальной формы, тот полностью понимает совокупность чувств?
(Kha) yo vā pana vedanākkhandhaṃ parijānāti so rūpakkhandhaṃ parijānātīti? = (б) А кто полностью понимает совокупность чувств, тот полностью понимает совокупность материальной формы?
(Ka) yo rūpakkhandhaṃ na parijānāti so vedanākkhandhaṃ na parijānātīti? = (а) Кто не понимает полностью совокупность материальной формы, тот не понимает полностью совокупность чувств?
(Ka) yo rūpakkhandhaṃ parijānittha so vedanākkhandhaṃ parijānitthāti? = (а) Кто полностью понял совокупность материальной формы, тот полностью понял совокупность чувств?
(Ka) yo rūpakkhandhaṃ parijānissati so vedanākkhandhaṃ parijānissatīti? = (а) Кто полностью поймёт совокупность материальной формы, тот полностью поймёт совокупность чувств?
(Ka) yo rūpakkhandhaṃ na parijānāti so vedanākkhandhaṃ na parijānitthāti? = (а) Кто не понимает полностью совокупность материальной формы, тот не понял полностью совокупность чувств?
Arahā rūpakkhandhaṃ na parijānāti, no ca vedanākkhandhaṃ na parijānittha. = Архат не понимает полностью совокупность материальной формы, но полностью понял совокупность чувств.
Aggamaggasamaṅgiñca arahantañca ṭhapetvā avasesā puggalā rūpakkhandhañca na parijānanti vedanākkhandhañca na parijānittha. = Кроме обладающего высшим путём и архата, остальные личности и не понимают полностью совокупность материальной формы, и не поняли полностью совокупность чувств.
Ye maggaṃ paṭilabhissanti te rūpakkhandhaṃ na parijānanti, no ca vedanākkhandhaṃ na parijānissanti. = Те, кто обретёт путь, не понимают полностью совокупность материальной формы, но полностью поймут совокупность чувств.
Arahā ye ca puthujjanā maggaṃ na paṭilabhissanti te rūpakkhandhañca na parijānanti vedanākkhandhañca na parijānissanti. = Архат и те обычные люди, которые не обретут путь, и не понимают полностью совокупность материальной формы, и не поймут полностью совокупность чувств.
Aggamaggasamaṅgī vedanākkhandhaṃ na parijānittha, no ca rūpakkhandhaṃ na parijānāti. = Обладающий высшим путём не понял полностью совокупность чувств, но полностью понимает совокупность материальной формы.
parijānāti полностью понимает / понимают; parijānittha полностью понял / поняли; parijānissati полностью поймёт /
  поймут; na … = не понимает полностью / не понял полностью / не поймёт полностью (never «полностью не …»);
  same negated verb on both objects: не V полностью ни X, ни Y

## Headings and closing labels

#### Paṇṇattivāro = #### Раздел об обозначениях
##### (Ka) uddeso = ##### (а) Перечень
#### Padasodhanavāro = #### Раздел уточнения слов
##### (Ka) anulomaṃ = ##### (а) Утвердительная форма
##### (Kha) paccanīkaṃ = ##### (б) Отрицательная форма
#### Padasodhanamūlacakkavāro = #### Круговой раздел на основе уточнения слов
#### Suddhakhandhavāro = #### Раздел о совокупностях как таковых
#### Suddhakhandhamūlacakkavāro = #### Круговой раздел на основе совокупностей как таковых
##### (Kha) niddeso = ##### (б) Разъяснение
#### Paṇṇattivāraniddesa = #### Разъяснение раздела об обозначениях
#### Pavattivāro 1. uppādavāro = #### Раздел о протекании 1. Раздел о возникновении
#### (1) Paccuppannavāro = #### (1) Раздел о настоящем
##### (Ka) anulomapuggalo = ##### (а) Утвердительная форма по личности
##### (Kha) anulomaokāso = ##### (б) Утвердительная форма по месту
##### (Ga) anulomapuggalokāsā = ##### (в) Утвердительная форма по личности и месту
##### (Gha) paccanīkapuggalo = ##### (г) Отрицательная форма по личности
##### (Ṅa) paccanīkaokāso = ##### (д) Отрицательная форма по месту
##### (Ca) paccanīkapuggalokāsā = ##### (е) Отрицательная форма по личности и месту
#### (2) Atītavāro = #### (2) Раздел о прошлом
#### (3) Anāgatavāro = #### (3) Раздел о будущем
#### (4) Paccuppannātītavāro = #### (4) Раздел о настоящем и прошлом
#### (5) Paccuppannānāgatavāro = #### (5) Раздел о настоящем и будущем
#### (6) Atītānāgatavāro = #### (6) Раздел о прошлом и будущем
#### Pavatti 2. nirodhavāro = #### Протекание 2. Раздел о прекращении
#### Uppādanirodhavāro = #### Раздел о возникновении и прекращении
#### Pariññāvāro = #### Раздел о полном понимании
#### Paccuppannavāro = #### Раздел о настоящем
Paṇṇattiuddesavāro. = Раздел перечня обозначений.
Paṇṇattiniddesavāro. = Раздел разъяснения обозначений.
Uppādavāro niṭṭhito. = Раздел о возникновении завершён.
Nirodhavāro. = Раздел о прекращении.
Uppādanirodhavāro. = Раздел о возникновении и прекращении.
Pavattivāro niṭṭhito. = Раздел о протекании завершён.
Pariññāvāro. = Раздел о полном понимании.
Khandhayamakapāḷi niṭṭhitā. = Парные вопросы о совокупностях завершены.
Pañcakkhandhā – rūpakkhandho, … = Пять совокупностей – совокупность материальной формы, совокупность чувств, совокупность восприятия, совокупность формирующих факторов, совокупность сознания.
variants: [X (syā.)] = [вариант чтения (Syā.): X]; (sī. syā.) = (Sī., Syā.); evamuparipi = «; так же и далее»
