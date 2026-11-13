# pi-6 Hindi plain zero-shot (Yamaka): harmonise pass

Script: harmonise_hi.py (reads backup-pre-harmonise\, writes the 44 files; --dry; log harmonise-log.tsv, B9 skips in harmonise-skipped.txt).
Finder: find_divergences_hi.py (divergences.md = before, --bak; divergences-after.md = after), with who_scan6.py (a4) and paren_scan6.py (a5).
Helpers: hz6_common.py, kwic6.py, show6.py, diff6.py, organ_forms6.py, who_join_survey6.py, agree_check6.py, sample_lines6.py, post_checks6.py, verify_harmonise.ps1.
Protected: preamble.md, 1-mulayamaka non-empty lines 1-122, 2-01-khandhayamaka non-empty lines 1-27, 219-248, 518-547 (located with sample_lines6.py; 0 changed).

The builders were NOT rerun. A rebuild drops this pass unless the builder constants below get the same change.

## Decisions (brief step 2) and the builder constant that needs the same change

| Rule | Decision | Why | Builder change needed |
|---|---|---|---|
| I1-organs, I1-organ-order | sa-X-ka = «X वाले», a-X-ka = «X से रहित», several joined « और » (mixed «आँख वाले और कान से रहित», both «आँख वाले और कान वाले»); modifier before the place («आँख से रहित इंद्रिय-सुखों के लोक में जन्म लेने वालों में») | terms file sahetuka/ahetuka = «मूल वाला / मूल से रहित» (level 1) gives «वाले / से रहित»; build_10a_hi MODS (Indriya, 400+ lines) already uses it with « और » for every modifier pair | build_3_hi descriptor table and DESC_BUT «{A} पर {B}» (3-0x); build_2_hi lines 237/243 «{s}-रहित», «{s1} वाले लेकिन {s2}-रहित» (used by build_4_hi); build_3_hi place-before-modifier order |
| I2-sota | «दिव्य कान और तृष्णा की धारा, कान हैं» | 3-01 = 10-01; plain Hindi, the approved sample adds no Devanāgarī gloss | build_4_hi line 69 «तृष्णा का प्रवाह» → «तृष्णा की धारा»; drop K.B_OVERRIDE["Dibbasotaṃ taṇhāsotaṃ"] = «“कान” (सोत)» (line 74) |
| I3-catupanca | «चार या पाँच समूहों वाले अस्तित्व» in every case form (… में / … से / … के प्राणियों में / … में जन्म लेने वालों में) | build_2_hi (Khandha, the builder the Khandha-type chapters follow), line 177; also matches 10-08 … 10-11 «या» for the accusative places | build_5_hi CATUPANCA (line 114); build_10a_hi lines 337/339; build_10b_hi place list joined «या»; common_6_9_hi (realm-name joining); build_3_hi (catuvokārānaṃ pañcavokārānaṃ as two chunks) |
| I4-natthi | «ऐसा कोई नहीं है।» also in 7-01 … 7-11 | same context everywhere (a question with no case to answer); build_2_hi, 174 of 322 | build_7a_hi SHORT["Natthi"] (line 69) |
| (item 5) | no change: agreement differs only by subject (agree_check6.py: 0 subject/verb mismatches) | | |
| B1-cavanta-abl | X-ā cavantānaṃ = «X से मरने वालों में» | build_2_hi; 3-0x had «X में मरने वालों में» | build_3_hi (ablative realm + cavantānaṃ) |
| B2-pacchimabhavika | Pacchimabhavikānaṃ X upapajjantānaṃ = one group «X में अंतिम जन्म लेने वालों में» (itthīnaṃ: «अंतिम जन्म लेने वाली स्त्रियों में») | build_2_hi; 10-09 … 10-11 split it into two groups | build_10b_hi my_who (pacchimabhavikānaṃ + following upapajjantānaṃ chunk) |
| B3-tesam-cavanta | «…पाएँगे, उनमें से जन्म लेने / मरने वालों में» | build_2_hi, 3-0x, 5-0x | build_10b_hi RESUM (lines 99-100); common_6_9_hi line 147 |
| B4-dutiye | «शुद्ध निवास लोक के प्राणियों में दूसरे मन के चलते समय» | 5-0x, 9-0x (Pāli order, more lines) | build_10a_hi SUDDHAVASA_DUTIYE (line 301) |
| B5-sabbesam-cittassa | «सभी के मन के … होने के क्षण में» | 6-0x, 9-0x (128 lines) over «सबमें» (10, 70) and «सभी में» (5, 7) | build_10a_hi SABBESAM (line 299, with cittassa); build_5_hi sabbesaṃ + moment |
| B6-anantara | «जिनमें इस मन के ठीक बाद X उत्पन्न होगा, उनमें» | 6-0x (45 lines) over 10-12 (7) | build_10a_hi ANANTARA (line 312) |
| B7-rupa-arupa-beings | rūpāvacarānaṃ arūpāvacarānaṃ = «सूक्ष्म भौतिक लोक के प्राणियों में और अभौतिक लोक के प्राणियों में» | 3-0x = build_2_hi chunk rule (every chunk keeps «में») | common_6_9_hi realm-run (line ~219) |
| B8-chunk-me | every being/place chunk keeps «में» («A के प्राणियों में और B के प्राणियों में») | build_2_hi, 3-0x | build_10a_hi.join (the 2026-11-12 plain-noun rule) |
| B9-chunk-join | the last chunk is joined with « और »: «A में और B में», «A में, B में और C में»; a mid-chain «, और जो» loses its «और» | build_2_hi, 3-0x, 10-0x | build_5_hi who() (", " joins; used by build_8_hi); common_6_9_hi chunk joining |
| B10-yo-vyakti | pariññā / pajahana / bhāvanā questions «(क) जो व्यक्ति …, क्या वह …?», past «जिस व्यक्ति ने …, क्या उसने …?» | identical frame; no sample/terms form, the builders tie (build_2_hi vs build_7a_hi), no pi-1/pi-2 form; occurrences: Anusaya ~620 question lines vs ~165 | build_2_hi, build_3_hi PARI_REL (line 333), build_4_hi, build_5_hi, common_6_9_hi, build_10b_hi (yo-question frames) |
| B11-raso | bare raso = «स्वाद» (also «अर्थ का स्वाद, शिक्षा का स्वाद और मुक्ति का स्वाद») | 3-01: the bare word = the noun of the compound (rasāyatana / rasadhātu = «स्वाद का …») | build_4_hi line 40 "raso"; line 71 Attharaso |
| N-notes, N-yassaka | yassaka / yatthaka / yassayatthaka = «व्यक्ति वाला भाग / स्थान वाला भाग / व्यक्ति और स्थान वाला भाग»; sadisaṃ = «समान»; vitthāretabbaṃ = «… का (इसी प्रकार) विस्तार करना चाहिए»; vibhajitabbaṃ / vibhatta = «… का विभाजन करना चाहिए / किया गया है»; cakkaṃ bandhitabbaṃ = «चक्र पूरा करना चाहिए»; saṃkhittaṃ = «संक्षिप्त किया गया है»; anulomampi paccanīkampi = «सकारात्मक भी और नकारात्मक भी»; asammohantena = «बिना भ्रम के» | build_2_hi («स्थान वाला भाग», «विभाजन») and the build_2/build_4 family; «खंड» stays for vāra (incl. «व्यक्ति और स्थान वाले खंड» = puggalokāsavāra inside two 5-01 variant brackets) | build_3_hi notes (lines 535-581); build_5_hi YASSAKA/YATTHAKA/YASSAYATTHAKA (69-71) and notes (559-596); common_6_9_hi notes (60-78); build_7b_hi VITTHARETABBAM (215, 366); build_10b_hi SADISAM (524) |

## Left on purpose
- Agreement of the short answers (Uppajjittha. = «उत्पन्न हुआ था / हुई थी / हुई थीं» …): the subject differs (brief item 5); divergences-after (a3) lists exactly these 4 groups.
- 6-01 line 170: «ध्यान की पहली अवस्था में, इंद्रिय-सुखों के लोक, सूक्ष्म भौतिक लोक और अभौतिक लोक में» (a chunk followed by a place list; unclear where «और» belongs), and the note in 5-02 line 309 that quotes a Pāli chain with its own commas: B9 skipped both.
- B9 never rejoins a chain that has «…» inside the chain itself; abbreviated answers («… वहाँ दुःख का सत्य…») are rejoined up to «वहाँ».
- 5-02 «सर्वोच्च मार्ग के उत्पन्न होने के क्षण में और जो …, और जो दूसरे लोग …, उनमें» (yassa … ye caññe … tesaṃ): two relatives share one correlative, so the inner «, और जो» stays.
- notes-*.md were not edited; divergences-after (c) still shows their pre-pass «Pāli = Hindi» lines. The table above says which form now holds.

## Checks after the pass
check_chapter_ids OK, verify_hi OK, dashcheck 0 mismatches for all 44 files (verify_harmonise.ps1); protected lines 0 changed; raw line counts and heading lines unchanged; «—», «:-», «धर्म», «seed», Latin letters outside [..]: 0 (post_checks6.py).
divergences-after.md: (a1) 0, (a2) 0, (a3) 4 (agreement only), (a4) WHO 0 (81 before), (a5) notes 0 (2 before).
