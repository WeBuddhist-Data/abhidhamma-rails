# Notes 3-02-ayatanayamaka (Russian zero-shot): Āyatana future / present-past person units

Builder: 0-INBOX\temp\pipeline\pi-6-ru\build_3-02_ru.py (load with importlib.import_module("build_3-02_ru"); importing writes nothing).
Members, AY_CFG, AY_FIXED and tr_line come from build_3-01_ru; families A / B from build_2-01_ru; PERSON_UNITS_2_02, extra_units() and pv_abbr() from build_2-02_ru; the person / place shape from build_7-01_ru.
3-03 … 3-06: `with ay2_units(): …` (or this module's translate_text / tr_line with AY2_CFG) gives the widened person parser; 3-01's output is asserted unchanged under it, and pe_question() is asserted to reproduce 3-01's fixed "…pe…" question lines.

## Family B additions [ay2_person_units, ay2_person_intro, PERSON_UNITS_3_02, REBORN_IN]
Every 2-01 / 2-02 person unit now works with the Āyatana planes (kāmāvacara / rūpāvacara / arūpāvacara) and descriptors:
Ye rūpāvacaraṃ upapajjitvā parinibbāyissanti = тех, кто, переродившись в мире форм, достигнет окончательного угасания [2-01 unit + 3-01 AY_PLANES]
Ye rūpāvacaraṃ arūpāvacaraṃ upapajjitvā parinibbāyissanti = тех, кто, переродившись в мире форм и в мире без форм, достигнет окончательного угасания [new; «и» as 2-01 «перерождается {in1} и {in2}»]
Pacchimabhavikānaṃ ye ca arūpaṃ upapajjitvā parinibbāyissanti = У тех, кто живёт последней жизнью, и у тех, кто, переродившись в мире без форм, достигнет окончательного угасания, [2-01 + 2-02 units]
acakkhukānaṃ kāmāvacaraṃ upapajjantānaṃ = тех, кто перерождается без глаза в мире чувственных желаний; sacakkhukānaṃ kāmāvacaraṃ upapajjantānaṃ = тех, кто перерождается с глазом в мире чувственных желаний [new: 3-01 descriptor, then the plane]
Itaresaṃ sacakkhukānaṃ upapajjantānaṃ = У остальных, кто перерождается с глазом, [2-01 itaresaṃ merge + 3-01 descriptor]
Kāmāvacarā / Rūpāvacarā cavantānaṃ = тех, кто умирает в мире чувственных желаний / в мире форм [2-01 unit]
Rūpāvacarānaṃ arūpāvacarānaṃ = существ мира форм и существ мира без форм [3-01]
Three units: «У A, у B, и у C …» (2-01 joiner): «У тех, кто умирает в существовании с пятью составляющими, у тех, кто перерождается без глаза в мире чувственных желаний, и у существ без восприятия там …»

## Questions with abbreviated lists [pe_question, pe_line]
Yassa X V tassa Y1…pe… Y2… Y3 V-ti? = У кого V X, у того V Y1… Y2… Y3? [3-01 fixed lines, now generic; asserted equal]
Yassa X1…pe… X2… X3 V tassa Y V-ti? = У кого V X1… X2… X3, у того V Y?
Yassa vā pana … = А у кого …; Yassa yattha … tassa tattha … = У кого где …, у того там …
? Uppajjittha. = ? Возникала. (verb agrees with the last named member: сфера → f) [2-01 verb()]

## Fixed lines [AY2_FIXED]
Yassa cakkhāyatanaṃ uppajjissati (tassa manāyatanañca dhammāyatanañca sadisaṃ, ime dve sadisāyeva honti). = У кого возникнет сфера глаза (у того сфера ума и сфера объектов ума одинаковы, эти две в точности одинаковы). [new; sadisa «одинаковы» as 3-01 ekasadisaṃ; -eva «в точности»]
Yattha X V…pe…. = Где V X… [2-02 pv_abbr = 3-01 fixed]

## Source slips
^6-3-75 "rūpāyatanañca ca uppajjittha": doubled "ca" (parallel lines have one); rendered as meant («и возникала …, и возникает …»).
