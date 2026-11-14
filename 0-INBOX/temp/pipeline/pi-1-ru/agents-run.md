# pi-1 Russian plain: agent log (started 2026-11-14)

Inputs: AI_translation\pali\pi-1_split_chapters (13 parts + preamble); style 0-INBOX\temp\pipeline\russian-style.md (new, from pi-3/4/5 and the pi-5 review); reference builders from the English and Hindi pi-1 runs restored from git (08b7ff3~1) into ref\.

## Zero-shot sample (ru-zeroshot-sample-brief.md)
Sample agent: a828abc9da19283e5 (preamble, 1-matika, 2-01 lines 1-122 = ^1-1-0 … ^1-57, ru-zeroshot-terms.md). Approved 2026-11-14 with the ^1-M1-9 fix («явления, чьи корни устраняются …»; applied in build_matika_ru.py, terms rebuilt). Term choices approved: mātikā «матрица», vicāra «удержание мысли», saṅkhāra «формирующие факторы», dosa «злоба», asaṅkhata «необусловленное», paṭiccasamuppāda «возникновение в зависимости от условий».

## Zero-shot parallel (ru-zeroshot-brief.md; refs in ref\ restored from git)
agent id | parts
---|---
a3921d6f8bb08e7e1 | 2-01 (after sample), 2-02
a5cd52a028e9b71e3 | 2-03
a87321931ef30e485 | 2-04
af2593478c3a24e8b | 2-05
a046d9df6b9036b41 | 3-01
ab510b068cdb66cdb | 3-02, 3-03
aebdb721ac1893e34 | 4-01
a7d092baae079aae3 | 4-02, 4-03
a9d089d2a3e6ce4b9 | 5

Reports:
- 2-03 done (96 seg, checks OK). Frames shared with 2-01/2-02 chosen independently: harmonise to 2-01/2-02 wording. Choices: sammappadhāna «правильное усилие» (= sammāvāyāma Russian), abhiññā «высшее знание», paṭipadā «болезненный / приятный способ практики». Slips: ^1-364 comma for dash; ^1-314 amoho line shorter; ^1-337/^1-363 «благие явления….».
- 3-01 done (29 seg, checks OK). Terms shared with 3-02/3-03 (upacaya «рост», santati «непрерывность», viññatti «внешнее выражение», kabaḷīkāra āhāra «съедаемая пища») need aligning. Slips: ^1-584 vs ^1-594 item split; punctuation at ^1-591/592/586; ^1-U1 odd ID kept.
- 2-01 (164 seg) + 2-02 (143 seg) done, checks OK. Reference wording for the 2-0x frames. Conflicts with 2-03 to harmonise: paṭipadā «с трудным / лёгким способом практики» (2-03 «болезненный / приятный»); vīmaṃsā «пытливость» vs 2-03 adhipateyya «исследования»; sasaṅkhārena «с побуждением»; «и пребывает в нём» moved to chain end (word-order departure). Slips: ^1-135 «?»; ^1-150/189 commas; ^1-167/180/182/202 dash; ^1-270 vīmaṃsādhipateyya missing.
- 2-05 done (99 seg, checks OK); copied 2-03 lokuttara wording. Disagreements across 2-0x for harmonise: vivicceva kāmehi (2-03 «отстранившись от чувственных удовольствий» / 2-02 «полностью уединившись от …» / 2-04 «… от чувственных желаний»); vūpasamā «успокоение» vs «затихание» (samatha = успокоение!); upasampajja «достигает» vs «входит в»; subject «человек развивает» vs 2-04 plural; ṭhapetvā «кроме» vs «за исключением»; vīmaṃsā = vicaya clash; 2-02 typo «сферыбесконечного». Slips: ^1-528, ^1-553 split word + aññindriya/aññātāvindriya, ^1-576 double answer.
- 3-02 (151 seg) + 3-03 (250 seg) done, checks OK; aligned to 3-01 wording. Open: kakkhaḷa «твёрдый» vs mudutā string akakkhaḷatā «отсутствие грубости» (oḷārika = грубый); viññatti «внешнее выражение» close to nirutti «выражение»; mano «ум» (ch3) vs «разум» (citta string). Slips: ^1-750/765/773/788/895/939 punctuation; ^1-850 dhoso; ^1-597/609 case; ^1-596/606 gāmopeso; ^1-636 dash.
- 2-04 done (149 seg, checks OK); follows 2-01/2-02 wording for shared jhāna phrases (vivicceva «полностью уединившись», vūpasamā «затихание», «с устранением приятного»). Open: asāta «ни неотрадно» (2-01 upekkhā string) vs «безотрадный» (2-05 dukkha string) — compatible? check; micchā- = ложный; ahirika «бессовестность». Slips: ^1-377 «?», ^1-473 «.», ^1-381 patiṭṭhāho, ^1-433 mental string for eye feeling, ^1-501–504 no upekkhāsahagata.
- 5 done (249 seg, checks OK). Conflicts: viññatti «сообщение» (ch3 «внешнее выражение»); upacaya «нарастание» (ch3 «рост»); diṭṭhigata «ложное воззрение» (2-04 «приверженность воззрениям»); ṭhapetvā «за исключением» (2-0x «кроме»); cittuppāda «вид ума» (terms file «возникновение ума»; matches heading «Двенадцать видов неблагого ума»); bhūmi «мир». Slips: ^1-1389 cut-off item, ^1-1478 «.», ^1-1387 comma, ^1-1501/1502 abridged.
- 4-01 done (179 seg, checks OK). Conflicts: patiṭṭhāho «цепкость» (as meant) vs 2-04 «закрепление» (as written) → user rule: as written unless a spelling slip; check Hindi/English; kammassa katattā «вследствие совершённого действия» vs 3-0x «вследствие совершённых действий»; sīlabbataparāmāsa «приверженность обрядам и обетам» vs parāmāsa «искажение». Slips: ^1-1022 question form, visarga «ः» at ^1-1106/1123/1128/1143/1144, ^1-1130… sāsavā in fetter groups.
- 4-02 (155 seg) + 4-03 (82 seg) done, checks OK.

All 14 files re-checked by me 2026-11-14: check_chapter_ids OK, dashcheck 0 mismatches, verify_ru OK, 2-01 starts with the sample. Stray empty root file build_2-01_2-02_ru.py removed.

## Harmonise (harmonise-brief.md)
Agent: afbc6adeb6907e57f. Decisions in the brief: 2-01/2-02 jhāna wording wins; vīmaṃsā «пытливость»; viññatti «внешнее выражение»; upacaya «рост»; diṭṭhigata «приверженность воззрениям»; patiṭṭhāho «закрепление» (as written); cittuppāda «вид ума» (to show the user).
Done: 347 lines changed, segment divergences 17 → 0, all checks OK, sample/matrix/preamble unchanged. Agent choices: asāta «безотрадный»; kammassa katattā «вследствие совершённых действий»; sārāga «пристрастие»; ṭhapetvā «кроме» everywhere. Builders now stale (harmonise-notes.md lists constants).
Merged: AI_translation\russian\pi-1-russian-plain-zeroshot.md (1,930 segments, 1,497 dashes, OK). Open for the user: cittuppāda in ch5 «вид ума» vs terms file «возникновение ума». User 2026-11-14: keep «вид ума» in ch5 (ch2 heading stays «возникновение ума").

## Keyword map (ru-mapper-sample-brief.md)
split_keywords_ru.py → mapper-ru\<part>.keywords.md (1,916 lines, 14 files). Hindi models restored to ref\ (hi-map-conventions.md, hi_map_common_hi.py, hi_1-matika/2-01 .mapped.md).
Sample agent: af43fa7848f338ab1 (preamble, 1-matika, 2-01; writes ru-map-conventions.md, map_common_ru.py, map_sample_ru.py). Approved 2026-11-14 with the fix: non-word positive parts and keywords with no own Russian word = (no direct equivalent) (nikkhitta, santuṭṭhitā, ṭhānesu; fix_sample_map_ru.py, 9 replacements; rule added to ru-map-conventions.md).
Parallel (ru-mapper-brief.md):
agent id | parts
---|---
a32c6d6497faea475 | 2-02, 2-03
a4ea9111936653b22 | 2-04
a461ec2ae9298a2f3 | 2-05, 3-01
adcab9081ad1e020a | 3-02, 3-03
a2f631cef87f8dde6 | 4-01
ab38defdca56cfe46 | 4-02, 4-03
ac1cbe454723455fc | 5

Reports:
- 2-04 done (149 lines, bad [], 4 NDE nikkhitta, 0 presence misses). Open: dvedhā/patho both «распутье» (1-425); sahagataṃ = «с» (1-501..504; maybe NDE); ānañcāyatana «сфера бесконечного» (partial); sukhaṃ 1-449 счастье vs answer «телесное удовольствие».
- 2-02 (143, bad [], 46 presence "misses" = inflection limits: говорить/огонь/видеть) + 2-03 (96, bad [], 32 NDE: caya 26, nikkhitta 4, avasesa 2) done. sahagataṃ = «с» at 1-273..276 too. Fixed the shared CH2/MATRIX tables in map_common_ru.py (nikkhitta, santuṭṭhitā, ṭhānesu → NDE) so later parts inherit the user rule.
- 3-02 (151) + 3-03 (244) done, bad [], 0 NDE; 34 presence misses = inflection (verbs as infinitive, ветер/огонь/рот/тарелки). Open: vidhena = «по» (bare preposition, like sahagataṃ = «с»); Duka = «классификация по два» in ch3 headings (matrix «пары»).
- 2-05 (99, bad [], 51 NDE: caya 49, avasesa, nikkhitta) + 3-01 (21, bad [], 4 inflection misses) done. Same open points: vidhena/sahagataṃ bare prepositions; ānañcāyatana partial; cross-check lokuttara values vs 2-03.
- 5 done (249, bad [], 2 NDE: caya, sekkhā; 1 inflection miss). Open: two clause-shaped values with finite verbs (hetū ekato uppajjanti; dhammā kenaci viññeyyā); uppāda = вид (ch5).
- 4-01 done (179, bad [], 6 NDE: caya, sekkhā, patho/gāho; 21 inflection misses). Inconsistent with 2-04: patho NDE here vs «распутье» in 2-04 → align. Ito = «это» (dictionary form «этот»).
- 4-02 (155, 2 NDE) + 4-03 (82, 19 NDE) done, bad [], presence misses = inflection.

Coordinator: crosscheck_map_ru.py (structure, bare function words, identical-segment conflicts, multi-value list) + cleanup_map_ru.py (171 changes, cleanup-log.tsv): sahagataṃ «с» and vidhena «по» → NDE; patho/gāho NDE; X ceva X-niyā pairs → ch5 participle form; hetukā «имеющий корни»; one wording for upasampajja viharati, vivicca(eva), paṭipadaṃ dandha/khippa, asaṅkhatā ca dhātu; Ito «этот». After: 0 identical-segment conflicts; only na = «не» left as a bare word.
Assembled: AI_translation\russian\pi-1-keywords-by-reference-pali-russian-plain.md (1,916 lines, 32,533 pairs, 158 NDE).

## Word senses (ru-senses-brief.md)
senses_prepare_ru.py 4 (adapted from Hindi senses_prepare_pi1.py) → 2,479 headwords (135 multi-value; 10 NDE-only omitted), agg-part1..4.tsv (620/620/620/619). agg-sample.tsv = first 90 of part1 + 30 more multi-value (42 multi in sample).
Sample agent: a7c5fb2791964bc26 (sample-senses.md, senses-conventions.md, senses_tool_ru.py). Done: 120 headwords, 145 senses, 22 multi-sense, 28 multi-candidate; VERIFY OK (re-run by me). Splits: rūpa ×3, kāya ×3, dhamma ×3, mano, citta (ум / вид ума), sukha, kāma, ārabbha, parāmāsa, Duka. Approved 2026-11-14.
User (temporary): run the rest ONE AT A TIME, not in parallel.
Part 1: a08f03a6ea4a09eb8 done (620 hw, 652 senses, 27 multi-sense, 38 multi-candidate; VERIFY OK re-run). New splits: dukkha ×3, sukha ×3, bahiddhā (вовне / вне), eva (полностью / несомненно, one occurrence), āhāraṃ.
Part 2: ab03197c6013abeb6 done (620 hw, 630 senses, 10 multi-sense, 35 multi-candidate; VERIFY OK re-run). Note for termbase: abhiniveso приверженность / убеждённость (clash with sīlabbataparāmāsa «приверженность»).
Part 3: a20cce42bcfce54c0 done (620 hw, 625 senses, 5 multi-sense, 28 multi-candidate; VERIFY OK re-run). Splits: sineho, sīla, dhamme, niyatā, sacca.
Part 4: a2f21e1f61c47bc9a done (619 hw, 621 senses, 2 multi-sense, 5 multi-candidate; VERIFY OK re-run).
Merged (senses\merge_senses_ru.py, adapted from Hindi): AI_translation\russian\pi-1-pali-word-russian-senses-plain.md — 2,479 headwords, 2,528 senses; all 4 parts verify; order = agg-all; no dashes/"outline" in tags.

## Termbase (ru-termbase-brief.md; termbase\tb_tool_ru.py adapted from Hindi tb_tool_pi1.py)
106 multi-candidate senses. Builder: a60d034b9916b5382 (decisions.tsv; runs termbase_assemble.py 1 russian ru plain). Needs the user's explicit approval afterwards.
Built: AI_translation\russian\pi-1-pali-russian-termbase-plain.md (2,479 hw, 2,528 senses; 106 multi decided, 3 aligned, 0 outside; assembler no errors, re-run by me). 19 cross-book differences (crossbook-out.txt). Proposed fixes for the user: ujutā «прямизна» (clash with ujukatā «прямота»); asārāgo «отсутствие пристрастия» (sārāgo family); Suññataṃ «пустой»; ajjhattaṃ / bahiddhā (adverb) «внутри себя» / «вовне».
APPROVED 2026-11-14 with the 4 fixes (termbase\APPROVED.md; apply_user_fixes.py → decisions.tsv + decisions-user.tsv; reassembled: no errors). Locked.

## Rails translation (ru-rails-sample-brief.md)
Sample agent: aa9e80b750557d69a (preamble, 1-matika, 2-01 through ^1-57 in rails\sample-2-01\, ru-rails-formulas.md, build_rails_sample_ru.py). Hindi pi-1 rails sample builder + formulas restored to ref\ as structural models.
Done: preamble 3, 1-matika 181, 2-01 sample 60 segments; all checks OK (re-run by me); adherence sample 0/1,041 misses, matrix 13/580 (all inflection). Question frame «Что такое X?». Open for the user: ^1-33 «?» rendered as a statement (emendation; rule says as written).
APPROVED 2026-11-14 with the fix: ^1-33 keeps «?» (build_rails_sample_ru.py, rebuilt; checks OK).
User: remaining chapters ONE AT A TIME, in book order (ru-rails-brief.md):
- 2-01 (rest) + 2-02: a2d94047e0359d0b3 done (164 + 143 seg; checks OK re-run; adherence 4/5,845 false misses). Misfits: paṭighasaññā «восприятия соударения»; satimā «осознанный»; arūpa saññāsahagata «в сопровождении восприятия сферы …»; bhāveti subject «кто-либо». Commas added at ^1-150/165/189 (punctuation); ^1-135 «?» kept.
- 2-03: a718ffc9fe35e6322 done (96 seg; checks OK re-run; 2-01/2-02 rebuild byte-identical with its tables; adherence 13/2,363, 12 false). Misfit: micchā «неправильный» in micchāājīvā (from the termbase's own gapped entry); maggapariyāpannaṃ «входящий в путь»; anavasesa «без остатка». ^1-364 comma kept as written.
- 2-04: a43dcd88522424ea7 done (149 seg; checks OK re-run; earlier chapters rebuild byte-identical; adherence 3/3,173 false). Misfits for review: titthāyatana «сфера сектантских учений» (pi-4 «прибежище …»); cetasikaṃ asātaṃ «душевная безотрадность»; sukhaṃ bodily «удовольствие» under sukhasahagataṃ «сопровождаемое счастьем» (^1-443); vipākaṃ «в качестве его результата»; byāpatti = byāpādo «недоброжелательность» twice (^1-418/419); dukkhaṃ «боль» for mental pain. Slips kept: ^1-377 «?», ^1-473 «.».
- 2-05: ab356a07d5d3a98da done (99 seg; checks OK re-run; 2-01..2-04 rebuild byte-identical; adherence 1/3,083 false). Misfits: vipāko standalone «результат действий»; aññātāvīnaṃ «обладающих окончательным знанием»; suññatā heading «пустое»; dukkhasahagataṃ «сопровождаемое болью»; labels «X (благой ум)» / «X (результат действий)». For the user: ^1-528 missing full stop rendered «.» + capital (zero-shot used «;»).
- 3-01: a0102ce8afa1d1454 done (29 seg; checks OK; adherence 18/505, inflection/finite verbs). Misfits: vatthu «основа»; dūre/santike «вдали/вблизи»; dhammāyatanapariyāpanna «принадлежит к сфере объектов ума»; Rūpavibhatti = rūpasaṅgaho «классификация материальной формы»; -meva «несомненно» ×40+.
- COORDINATOR FIX 2026-11-14: the approved matrix had three «ни … ни» items without «не» (1-M1-8 (в), 1-M1-9 (в), 1-M1-11 (в)) and 3-01 inherited them. Fixed in build_rails_sample_ru.py and build_rails_3-01_ru.py («не устраняемые ни …», «чьи корни не устраняются ни …», «не относящиеся ни …»; 3-01 «не устраняется ни …», «не относится ни …»); rebuilt matrix, sample, formulas, 3-01; 2-01..2-05 unchanged (hashes equal). To tell the user.
- 3-02 + 3-03: a399ef468745b0f9c done (151 + 250 seg; checks OK re-run; adherence 56/5,896 false). Gaps filled: telaṃ «растительное масло», itthi-/purisa- lists adjectival «женская внешность…», -gataṃ «считающееся …», vacībhedo «членораздельная речь». Slips kept: ^1-750 «.», ^1-765/773/788 «?», ^1-895/939 run-on.
  FOR REVIEW PASS: «X, – это» after a bare noun or list (no clause to close), e.g. «Сфера видимых форм, – это …»: 205 lines book-wide so far; Russian punctuation wants «X – это» there (comma only after a participial/subordinate clause).
- 4-01: a9e9195474e249445 done (179 seg; checks OK re-run; adherence 32/3,080, 1 real: vipākato with kusalānaṃ dhammānaṃ «в виде результатов благих явлений»). Uses «X – это» after bare nouns (0 bare «, – это»); earlier chapters to be aligned in the review sweep. Gaps filled (table in notes-4-01.md): samuppannā «полностью возникшие» vs uppannā; bhūtā «ставшие»; atthaṃ carati «приносит пользу»; saṅgha «Община»; Tattha katamo X «Что такое здесь X?». Slips kept: visarga «ः» → «;», patiṭṭhāho, Sāsavā in fetter groups, ^1-1014 no «?».
- 4-02 + 4-03: a245165e2c1c3a4fa done (155 + 82 seg; checks OK re-run; adherence 41/3,619 mostly false). For review: Natthi split «ничего не значит» (gifts, parents …) vs «нет» (fruit of deeds, beings, ascetics), as pi-4; vipāko «результат»; nāmaṃ «имя» (naming list); paccayā «условия»; hotīti «так происходит возникновение»; pair frame kept «X по отношению к Y является …». Slips kept: ^1-1310 «?», ^1-1301 colon, ^1-1285/1286 order.
- 5: a8c5f086feb9cbbaa done (249 seg; adherence 21/3,226 false). Choices: bhūmīsu «четырёх миров»; «кроме …, – это» comma kept (closes the кроме phrase; sample ^1-62 does it); sabbeva «все без исключения»; pakaraṇa «Книга». For the user: ^1-1389 clipped «ya vedanāya sampayuttātipi» rendered as the full matrix item (as meant).

Book-wide checks 2026-11-14 (all 14 files): check_chapter_ids OK, dashcheck 0 mismatches, verify_ru OK, 2-01 starts with the sample, no «ли»/em dash/«:-»/seed/CR; adherence 202/32,411 (0.6%, mostly inflection). find_divergences_rails_ru.py: 113 identical-Pāli groups, 0 diverging. fix_bare_comma_ru.py: 205 lines in 3-02/3-03 «X, – это» -> «X – это» (log fix-bare-comma-log.tsv; rerun after any rebuild of the 3-02/3-03 builder).
Next: independent bilingual review (step 7), then fixes, merge, frontmatter, track copy.

## Review (review-brief.md; findings saved by me to review\findings-rN.md)
User: reviewers ONE AT A TIME. r1 preamble/1-matika/2-01/2-02: a96c6637b4999162f done (0 crit, 0 major, 6 minor; findings-r1.md: 1 APPLY, 2 ASK, 3 REJECT) → r2 2-03..2-05: a603e74d01718e0a9 done (0 crit, 1 major ^1-443, 7 minor; findings-r2.md: 6 APPLY, 2 REJECT) → r3 ch3: a1dcf5a864bcfbf75 done (0 crit, 4 major = -gataṃ agreement ×9 seg, 10 minor; findings-r3.md: 8 APPLY, 3 REJECT, 3 ASK) → r4 ch4+5: ad4dff6a18537062a done (0 crit, 0 major, 6 minor; findings-r4.md: 4 APPLY, 1 ASK).
All 4 reviews in: 0 critical, 5 major (^1-443; -gataṃ agreement), minor polish. Questions put to the user: APPLY list; sārāga family; asantuṭṭhitā; headings (bhāṇavāra, «на N видов», Rūpavibhatti, bhūmi).
User 2026-11-14: Apply all; sārāga family all «пристрастия»; asantuṭṭhitā «Ненасытность»; wording left to me ("whichever you think best") → I chose all four (часть для чтения вслух, на N видов, Разбор материальной формы, четырёх уровней). Termbase: decisions-review.tsv, reassembled no errors; APPROVED.md updated.
Fix agent: a7c2b40f19c2c9b7d done (apply_review_fixes_ru.py, backup-pre-fixes\, fixes-log.tsv: 368 lines changed; Ekakaṃ kept «по одному»; builders-stale.md; run order builder → rails\fix_bare_comma_ru.py → apply_review_fixes_ru.py with refreshed backup). My re-check: all 14 OK, 0 divergences, no «считающееся»/«ли»/em dash/seed.

## Merge and track copy (2026-11-14)
ru-frontmatter.yaml → AI_translation\russian\pi-1-russian-plain.md (merge_rails.py OK; 1,930 segments; 1,497 dashes). Track copy + termbase in 3-TRANSFORMATIONS\Translations\ru-Contemporary-Russian-Abhidhamma\; add_transclusions 1,782, verify ALL OK, line 1 = ---. Not committed (needs the user's ask).
- then 2-03, 2-04, 2-05, 3-01, 3-02+3-03, 4-01, 4-02+4-03, 5
