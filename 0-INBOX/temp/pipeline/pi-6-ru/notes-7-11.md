# notes-7-11: (Kha) Dhātuvisajjanāvāra; Anusayayamaka close

Builder: build_7-11_ru.py (import: `importlib.import_module("build_7-11_ru")`; importing writes nothing; `--dry` prints the lines). It imports build_7-10_ru (dhatu_who, planes_ru, DHATU_SRC_RU / DHATU_DST_RU, DHATU_BHANGA_NATTHI10, MULAKA10, MULAKA_TAIL_RE) and through it 7-01 … 7-09 and build_sample_ru, all unchanged. Builder checks: all cross-book asserts of 7-01 … 7-10 plus its own, consistency with the finished anusaya chapters and the sample (the Namo line is shared), per-line counts.

## Frames [constant in brackets]
Kāmadhātuyā cutassa kāmadhātuṃ upapajjantassa = у того, кто, умерев в мире чувственных желаний, перерождается в мире чувственных желаний [7-10 dhatu_who]
anusayā bhaṅgā natthi = скрытых склонностей, подлежащих разделению, нет [7-10 DHATU_BHANGA_NATTHI10, coordinator]
kassaci N anusayā anusenti = в некоторых случаях залегают N [new; KASSACI_FRAME. pi-2 has kassaci «у некоторых», but after the generic singular «У того, кто …» a plural «у некоторых» does not agree; English rails "in some cases"]
satta anusayā = семь скрытых склонностей [pi-2 17-khuddakavatthuvibhango; assert]
pañca anusayā = пять скрытых склонностей [new; NUM_RU]
tayo anusayā = три скрытые склонности [new; NUM_RU]
anusenti = залегают [7-01 «залегает», plural with the numerals]
satteva anusayā anusenti = залегают ровно семь скрытых склонностей [new; SATTEVA; aṭṭhakathā ^6-155 "sattevāti niyametvā vuttaṃ"]
X cutassa (no upapajjantassa) = у того, кто умер X [new; DHATU_CUTA_ONLY]
Y upapatti nāma natthi = перерождения Y не бывает [new; NO_UPAPATTI; Y by planes_ru: «в мире форм», «не в мире чувственных желаний и не в мире без форм»]
heṭṭhā upapajjamāno kāmadhātuṃyeva upapajjati = перерождаясь ниже, он перерождается только в мире чувственных желаний [new; HETTHA]
…, satteva anusayā anusenti (after HETTHA) = …, у него залегают ровно семь скрытых склонностей [new; HIS + SATTEVA]
(Nakāmadhātumūlakaṃ) … (Nakāmanarūpadhātumūlakaṃ) = (На основе не мира …) [7-10 MULAKA10]
(Kha) dhātuvisajjanāvāro = (б) Раздел ответов об элементах [sample SECTION_HEADINGS via 7-09 heading9]
Dhātuvisajjavāro. = Раздел ответов об элементах. [FIXED11]
Anusayayamakaṃ niṭṭhitaṃ. = Парные вопросы о скрытых склонностях завершены. [sample YAMAKA_CLOSING_FRAME]
Namo tassa bhagavato arahato sammāsambuddhassa = Почтение Благословенному, Достойному, Полностью Пробуждённому Будде [sample NAMO]

## Source notes (translated as written; the Pāli file untouched)
Line 35 "rūpadhātuyā upapattināma natthi": joined spelling of "upapatti nāma" (lines 11, 13, 37); rendered as meant.
Line 38 "Dhātuvisajjavāro.": short spelling of the heading's "dhātuvisajjanāvāro"; rendered as the heading.
The Pāli commas of the "upapatti nāma natthi, heṭṭhā …, satteva …" sentences are kept (comma splices in the Russian too).
