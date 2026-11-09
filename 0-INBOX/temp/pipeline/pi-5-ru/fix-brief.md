# Brief: apply the review fixes to the Russian Kathāvatthu (pi-5)

Work in D:\Work\OpenPecha\abhidhamma-rails (Windows; Read/Edit/Write tools for files, PowerShell for commands; python as `python -I -X utf8`). Other agents fix other chapters in parallel: edit ONLY your own chapter files in AI_translation\russian\pi-5-russian-plain-rails_split_chapters\. Helper scripts (if any) only in 0-INBOX\temp\pipeline\pi-5-ru\review\, named fix_<part>_*.py.

The user approved ALL fixes below.

## Inputs
- Pāli (authority): AI_translation\pali\pi-5_split_chapters\<ch>.md (same filenames). Segments align by the block ID at the end of each segment.
- Your review report (the to-do list): named in your task. Each row gives ID, problem and a suggested fix. Verify each row against the Pāli before changing anything; if a suggestion is wrong, do the right thing and say so in your report.
- Book-wide termbase changes: 0-INBOX\temp\pipeline\pi-5-ru\fix-termbase-changes.md (pali | previous Russian | new Russian). These apply in EVERY chapter, not only where a reviewer flagged them. Search your chapters for every previous Russian form (all inflections) and, where the Pāli at that spot is the listed term (or a compound / inflection of it), replace it with the new term, inflected to fit the sentence. Do not change a Russian word where the Pāli is a different term (e.g. «нейтральн-» for something other than abyākata; «усилие» for padhāna / vāyāma / sammappadhāna, which stays).
- The updated locked termbase: AI_translation\russian\pi-5-pali-russian-termbase-plain.md.
- Sentence formulas (unchanged): 0-INBOX\temp\pipeline\pi-5-ru\ru-rails-formulas.md.

## Book-wide decisions (apply wherever the Pāli has the term)
- abyākata = «этически неопределённый» (inflect: «этически неопределённое чувство», «этически неопределённые явления»). kiriyābyākata = «этически неопределённый функциональный» (add the noun if the Pāli implies one: «… функциональным явлением»); vipākābyākata = «этически неопределённый, являющийся результатом действий» (comma allowed in running text). EXCEPTION: the Buddha's undeclared questions (^5-708, "sassato loko"ti … abyākatametaṃ and similar) = «это оставлено без ответа».
- abyāpāda = «отсутствие недоброжелательности»; mettā = «доброжелательность» (all forms, incl. mettāya).
- vicikicchā = «колебание» (vicikicchānusaya «скрытая склонность к колебанию», saṃyojana «оковы колебания», nīvaraṇa «помеха колебания», pariyuṭṭhāna «одержимость колебанием»); kaṅkhā stays «сомнение».
- kappa = «эпоха» everywhere (kappasatāni «сотни эпох», kappasahassāni «тысячи эпох», «сорок две тысячи эпох» …).
- vīriya / vīriyindriya = «усердие» / «способность усердия» everywhere.
- yoni = «способ рождения» (saññāyoni «способ рождения с восприятием»); saṃsāra = «круговорот перерождений» (saññāsaṃsāra «круговорот перерождений с восприятием»).
- arahatta = «состояние архата» (arahattamagga «путь к состоянию архата», arahattaphala «плод состояния архата», arahattā parihāyati «утрачивает состояние архата»); never «архатство».
- āsavakkhaya / āsavānaṃ khaya = «уничтожение влечений»; never «истощение» for khaya of the āsavas.
- kukkucca = «угрызения»; uddhacca stays «беспокойство».
- samudaya = «возникновение» (dukkhasamudaya «возникновение страдания»).
- saṇṭhāti = «длиться / продолжаться» (5-654: «Эпоха длится …»; 5-906: make it clear the question is whether the earth etc. lasts only one mind-moment).
- voharati = «высказываться» (bhaṇati stays «говорить»).
- nerayika = «обитатель ада»; virāgadhamma = «подверженный увяданию»; cakkavattisatta = «будущий вселенский правитель»; santo (sappurisā) = «добрые»; dukkhassantakiriyā = «конец страдания»; ānisaṃsa = «преимущество»; parinipphanna = «полностью сформированный» / aparinipphanna «не полностью сформированный»; saṅkapparāga = «страстное помышление».

## Rules (unchanged)
- Block IDs exact at the end of the last line of each segment; each segment keeps the source's number of non-empty lines; one blank line between segments; no double blank lines.
- DASH RULE (user): "–" only where the Pāli has "–"/"—", same spot, same count on every line. Never add a dash in a fix (rephrase instead).
- Questions without «ли»; quotes «…» / „…“; "…pe…" = «…».
- Identical Pāli formulas → identical Russian. When you align a formula, align ALL its occurrences in your chapters.
- Do not touch anything a report marks INFO or advisory unless your task says so.

## Verify each edited chapter (all must pass)
python -I 0-INBOX\temp\pipeline\check_chapter_ids.py AI_translation\pali\pi-5_split_chapters AI_translation\russian\pi-5-russian-plain-rails_split_chapters <ch>.md
python -I -X utf8 -c "import sys;f=lambda p:[l for l in open(p,encoding='utf-8').read().splitlines() if l.strip()];c=lambda t:t.count('—')+t.count('–');a,b=f(sys.argv[1]),f(sys.argv[2]);bad=[i for i,(x,y) in enumerate(zip(a,b)) if c(x)!=c(y)];print('lines',len(a),len(b),'dash-line mismatches',len(bad),bad[:5])" AI_translation\pali\pi-5_split_chapters\<ch>.md AI_translation\russian\pi-5-russian-plain-rails_split_chapters\<ch>.md
Then grep your chapters once more for the previous Russian forms in fix-termbase-changes.md and for «архатств», «истощени», «мировых период», «лоно», «нейтральн», «миролюбив», «останавлива», «положени» to confirm none is left where the Pāli has the changed term.

## Final report (short)
Per chapter: checks passed + number of segments changed. Report rows applied / adjusted / skipped (with reason). Any spot where you were unsure.
