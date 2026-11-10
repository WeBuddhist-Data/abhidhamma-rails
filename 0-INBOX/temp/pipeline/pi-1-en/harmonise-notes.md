# pi-1 English plain zero-shot: consistency (harmonise) pass

Script: harmonise.py (fixed old -> new strings; a few fixed regex patterns, marked rx=True). A rule changes an English
line only when the aligned Pāli line (non-empty line i <-> non-empty line i) matches the rule's Pāli pattern; the
script asserts unchanged dash counts, block IDs and heading levels on every changed line.
Backup of the pre-pass parts: backup-pre-harmonise\. Full per-rule, per-part log: harmonise-log.tsv
(replacements / lines). The pass was run once on the backup state (idempotent rules).
Discovery and final-scan helpers: hz_scan.py (identical Pāli clauses -> English variants), hz_words.py
(word-by-word pairing of synonym strings), hz_probe.py / hz_kwic.py (targeted tallies).

## Decision order
1. Coordinator decisions. 2. Approved term list and samples (1-matika.md, ch2-01-sample.md). 3. Majority, counted
by agent (one vote per builder), then by occurrences. Tie-breaks: where the chapter-2 version (2-04, which follows
the reference builder build_2-01_2-02.py) is involved, the chapter-2 version wins; where only 4-01/4-03 and 4-02
disagree, the 4-01/4-03 version wins (that builder covers two of the three Nikkhepa parts and was already aligned
with chapter 5), unless the approved list decides it (pattern "X of mind" for cittassa X; visuddhi = purification).

## Lines changed per part
2-01: 22 | 2-02: 124 | 2-03: 32 | 2-04: 61 | 2-05: 91 | 3-01: 2 | 3-02: 2 | 3-03: 1 | 4-01: 91 | 4-02: 84 |
4-03: 36 | 5: 71 | 1-matika, preamble: 0. Total 617 lines, 51 rule classes (log ids below).

## Change classes (Pāli | old | new | parts: replacements/lines | reason)

### Coordinator decisions
- A-katame | Katame dhammā kusalā / akusalā / abyākatā? | What states are wholesome / unwholesome / indeterminate? | What are wholesome / unwholesome / indeterminate states? | 2-01 8, 2-02 110, 2-03 26, 2-04 24, 2-05 62, 3-01 1 | matrix frame for the whole book (incl. the approved sample lines ^1-1, ^1-57 …).
- A-ime | ime dhammā kusalā / akusalā / abyākatā | these states are X | these are X states | 2-01 20, 2-02 124, 2-03 30, 2-04 65, 2-05 112, 3-01 1 | same.
- B-thapetva | ṭhapetvā | apart from (2-05), except for / Except for (4-01, 5), leaving X aside / Leaving aside (4-02) | except / Except | 2-05 18/6, 4-01 28/28, 4-02 7/7, 5 72/58 (plus the 4-02 frames under O) | build_2-01_2-02.py: ṭhapetvā = except.
- C-tattha | Tattha | Of these, (4-02) / Among these, (3-01) | Therein, | 4-02 31, 3-01 1 | not defined by the reference builder; majority (Therein 100 lines in 4-01/4-03).
- D-patipada | dukkha- / sukhapaṭipadaṃ | with difficult / easy practice | with painful / pleasant progress | 2-05 132/39 | build_2-01_2-02.py (paṭipadā = mode of progress).
- D-headings (2-05, 14 lines, heading + closing line each) | Suddhikapaṭipadā | The Simple Modes of Practice | Plain Progress (identical Pāli in 2-03) ; Suddhikasuññataṃ | Simple Emptiness | Plain Emptiness ; Suññatapaṭipadā | Emptiness with the Modes of Practice | Progress with Emptiness ; Suddhikaappaṇihitaṃ | Simple Desirelessness | The Plain Desireless ; Appaṇihitapaṭipadā | Desirelessness with the Modes of Practice | Progress with the Desireless ; Chandādhipateyyasuddhikapaṭipadā / -suññatā | Desire as the Dominant Factor: The Simple Modes of Practice / Simple Emptiness | … Plain Progress / Plain Emptiness | suddhika = plain, paṭipadā = progress, appaṇihita = the desireless, as in the 2-03 headings (which follow the reference builder).
- G-mudu | akakkhaḷatā akathinatā | freedom from roughness, freedom from hardness | freedom from hardness, freedom from rigidity | 2-01 2, 2-03 2, 3-02 2, 3-03 1, 4-03 1 | kakkhaḷa = hard throughout. akathinatā had "hardness"; it moves to "rigidity" so the two items stay distinct. Section 3b of en-zeroshot-terms.md changed accordingly (see below).
- P9-suddhi / sīlabbata | sīlabbata | (already "rules and observances" in every part; no "rites and rituals" left) | — | — | checked, no change needed.
- E-kiriya | kiriyā … neva kusalā nākusalā na ca kammavipākā | merely functional | functional | 4-01 5 | majority (2-05, 3-01, 4-02, 5).
- R-kabalikara | kabaḷīkāro āhāro | the nutriment of solid food | edible food | 5 2 | majority (3-01, 3-02, 3-03, 4-02; 153 lines).
- S-hyphen | cakkhu- / sota- / ghāna- / jivhā- / kāyaviññāṇaṃ | Eye consciousness … body consciousness | eye-consciousness … body-consciousness | 5 7/3 | hyphenated in every other part.
- P1 diṭṭhigata (see below), P4 dosa string (see below).
- "outline", "neutral": none present before or after.

### Chapter 2 formulas (2-05 aligned to 2-02 / 2-03 / 2-04)
- E-niyyanika | lokuttaraṃ jhānaṃ (cittaṃ) bhāveti niyyānikaṃ apacayagāmiṃ | absorption (mind) that leads to liberation … | absorption (mind), which leads to liberation … | 2-05 49 | 2-03.
- E-stage-and | … bhūmiyā pattiyā vivicceva / vitakkavicārānaṃ | stage, and, quite secluded | stage, and quite secluded | 2-05 49 | 2-03.
- E-tasseva | Tasseva lokuttarassa kusalassa jhānassa katattā bhāvitattā vipākaṃ | Because that same world-transcending wholesome absorption has been done and developed, as its result one, | As a result of that same world-transcending wholesome absorption that has been done and developed, when one, | 2-05 32 | construction of 2-04 "Tasseva rūpāvacarassa kusalassa kammassa katattā upacitattā vipākaṃ".
- E-sunnata | suññataṃ / animittaṃ / appaṇihitaṃ (qualifying the absorption) | empty / signless / desireless | which is empty / which is signless / which is desireless | 2-05 157/49 | 2-03.
- E-akusalavipaka | akusalassa kammassa katattā upacitattā vipākaṃ X uppannaṃ hoti | because unwholesome action has been done and accumulated, X has arisen as its result | as a result of unwholesome action that has been done and accumulated, X has arisen | 2-05 3 | 2-04 construction.
- E-sasankharena | … sasaṅkhārena | accompanied by joy, associated with knowledge and with prompting (4 forms) | accompanied by joy and associated with knowledge, with prompting | 2-05 4/1 | 2-01 / 2-02 / 2-04.
- E-pathavi | pathavīkasiṇaṃ | using the earth meditation device | using earth as the meditation device | 2-05 2 | build_2-01_2-02.py.
- E-maggangam | maggaṅgaṃ maggapariyāpannaṃ | a factor of the path | a path factor | 2-05 1, 4-01 1 | 2-03 (27 lines).
- E-ruparaga | rūparāgaarūparāga… | lust for the fine-material, lust for the immaterial | lust for fine-material existence, lust for immaterial existence | 2-05 1 | 2-03.
- E-samatikkama | sabbaso rūpasaññānaṃ samatikkamā … ; sabbaso X samatikkamma | with the complete surmounting … with non-attention …; completely surmounting | by completely passing beyond … by not attending …; having completely passed beyond | 2-05 4 | build_2-01_2-02.py.
- E-sukhassa | sukhassa ca pahānā | with the abandoning of happiness | with the abandoning of pleasure | 2-05 4 | build_2-01_2-02.py.

### Chapter 4 / 5 frames
- N-ellipsis | X…pe… Y | X … Y | X… Y | 4-01 80/67, 4-03 41/35, 5 5/5 | the style rule and every other part; only lines whose Pāli has no spaced " …pe…". Left: 4 lines in 2-02 and 1 in 5 where the Pāli itself has " …pe…" (mirrored).
- O-remaining | Te dhamme ṭhapetvā avasesā kusalākusalābyākatā dhammā kāmāvacarā, rūpāvacarā, arūpāvacarā, apariyāpannā | Leaving those states aside, the remaining …: those of the sense sphere, …, and those not included … | Except those states, the remaining …, whether of the sense sphere, of the fine-material sphere, of the immaterial sphere or not included in the spheres of existence | 4-02 10 | 4-01 form (28:28 tie, tie-break).
- O-three-spheres | kāmāvacarā, rūpāvacarā, arūpāvacarā (sāsavā lists) | : those of the sense sphere, of the fine-material sphere and of the immaterial sphere | , whether of the sense sphere, of the fine-material sphere or of the immaterial sphere | 4-02 15 | same.
- O-sasava-start | Sāsavā kusalākusala(byākatā) dhammā | The wholesome, unwholesome and indeterminate states subject to taints | Wholesome, unwholesome and indeterminate states subject to taints | 4-02 7 | 4-01.
- O-dissociated-sasava | Tehi dhammehi ye dhammā vippayuttā sāsavā kusal… | Among the states dissociated from those states, the wholesome … | The states that are dissociated from those states and are wholesome … | 4-02 4 | 4-01.
- O-assoc | Tehi dhammehi ye dhammā sampayuttā / vippayuttā | The states associated / dissociated … | The states that are associated / dissociated … | 4-02 8 | 4-01 (15:15 tie).
- O-assoc-except | Tehi dhammehi ye dhammā sampayuttā, te dhamme ṭhapetvā | Among the states associated with those states, leaving those states aside, | Among the states that are associated with those states, except those states, | 4-02 3 | 4-01.
- O-relation-except | Tehi dhammehi ye dhammā nīvaraṇiyā / upādāniyā / saṃkilesikā / parāmaṭṭhā / saṃkiliṭṭhā, te dhamme ṭhapetvā | Among the states subject to / misapprehended by / defiled by those states, leaving those states aside, | Among the states that, in relation to those states, are subject to hindrances (clinging, defilement) / are misapprehended / are defiled, except those states, | 4-02 5 | 4-01 frame "Tehi dhammehi ye dhammā sāsavā" = "the states that, in relation to those states, are subject to taints".
- O-tadekattha | tadekaṭṭhā / tadekaṭṭho | stand together with them | occur together with them | 4-02 8/6 | 4-01 (8:7).
- O-tamsampayutto | taṃsampayutto … | the aggregate of feeling… the aggregate of consciousness associated with them / with it | the associated aggregate of feeling… aggregate of consciousness | 4-02 13/12 | 4-01 (20 lines).
- O-bhumi-spheres | (Savitakka)bhūmiyaṃ kāmāvacare rūpāvacare (arūpāvacare) apariyāpanne | , in the sense sphere, the fine-material sphere (the immaterial sphere) and what is not included in the spheres of existence, | , whether of the sense sphere, of the fine-material sphere (, of the immaterial sphere) or not included in the spheres of existence, | 4-02 6 | 4-01.
- O-sabbanca | sabbañca rūpaṃ, asaṅkhatā ca dhātu | all material form, and the unconditioned element | all material form and the unconditioned element | 4-01 18 | majority (4-02, 27 lines).
- O-avaseso | Avaseso lobho doso moho | The remaining greed, hate and delusion | The remaining greed, hate, delusion | 4-02 2 | 4-01.
- O-teva / O-sveva | Tāneva / Teva … ; Sveva parāmāso | Those same X are both … ; That same misapprehension is both a misapprehension and misapprehended. | Those same X are states that are both …; That same misapprehension is one of the states that are both misapprehensions and misapprehended. | 4-02 5 | 4-01 + 5.
- O-pahatabbahetu | ime dhammā dassanena / bhāvanāya pahātabbahetū | these are the roots to be abandoned | these are roots to be abandoned | 4-02 2 | 4-01 (tie).
- Q-katatta | (yañca rūpaṃ) kammassa katattā | due to action having been done | due to past action | 4-01 3, 5 6/5 | majority (3-02, 3-03, 4-02; 52 lines).
- M-vattabba | Cittaṃ na vattabbaṃ – cittena sampayuttantipi, cittena vippayuttantipi (saṃsaṭṭhantipi …) | Mind is not to be described – as associated with mind, nor as dissociated from mind. | Mind should not be described – either as "associated with mind" or as "dissociated from mind". | 5 2 | 2:2 tie; 4-02 form chosen because it shows the Pāli quotation (…ti) with quotes, as the rest of the book does.
- J-heṭṭhimāni | Cattāro maggā apariyāpannā, heṭṭhimāni ca tīṇi sāmaññaphalāni | … existence and the three lower fruits | … existence, and the three lower fruits | 5 1 | 4-01; the Pāli has the comma.
- T-tayo-hetu | Tayo kusalahetū, tayo akusalahetū, tayo abyākatahetū | Three wholesome roots, three unwholesome roots, three indeterminate roots. | The three wholesome roots, the three unwholesome roots, the three indeterminate roots. | 5 1 | 4-01.

### Synonym strings (item-level vote of the three agents 2-04, 4-01/4-03, 4-02)
- P1-ditthi | diṭṭhi diṭṭhigataṃ … vipariyāsaggāho | 4-01: holding a view, holding firmly, the ground of sectarian views, grasping things the wrong way round; 4-02: being caught in views, the writhing of views, taking a stand, a sectarian doctrine, inverted grasping; 2-04: a wrong path, a false way | final: view, holding views, the thicket of views, the wilderness of views, the contortion of views, the vacillation of views, the fetter of views, grasping, fixation, adherence, misapprehension, a wrong road, a wrong path, wrongness, a basis for sectarian doctrines, a distorted grasp | 2-04 2, 4-01 28, 4-02 33, 4-03 18 | diṭṭhigata: three different renderings, tie -> chapter-2 "holding views"; vipphandita, kummagga, micchāpatha: 2 of 3; patiṭṭhāho (and the variant reading paṭiggāho in the same slot), titthāyatana, vipariyāsaggāha: tie -> chapter 2.
- P2-moha | aññāṇaṃ adassanaṃ … avijjālaṅgī | 2-04 lack of breakthrough, lack of penetration, confusion; 4-01 non-understanding … failure to perceive directly; 4-02 not understanding … not making it directly evident; 4-02 "lack of knowledge about" | final: lack of knowledge, lack of vision, non-realisation, lack of understanding, lack of awakening, non-penetration, failure to take in, failure to fathom, failure to consider, failure to review, failure to see for oneself, stupidity, foolishness, lack of clear awareness, delusion, deep delusion, utter delusion, ignorance, …; Dukkhe aññāṇaṃ = lack of knowledge of suffering … | 2-04 3, 4-01 3, 4-02 16/4 | item vote; ties -> chapter 2; "of" (4-01) over "about" (4-02).
- P3-kankha | kaṅkhā kaṅkhāyanā … manovilekho | (three versions) | uncertainty, being uncertain, the state of being uncertain, perplexity, doubt, indecision, a forked path, wavering, failure to take a definite stand, hesitation, faltering, failure to fathom, stiffness of mind, mental scratching | 2-04 2, 4-01 2, 4-02 2 | item vote; ties -> chapter 2. apariyogāhanā = failure to fathom in both the moha and kaṅkhā strings.
- P4-dosa | (cittassa āghāto …) doso dussanā … anattamanatā cittassa; Anatthaṃ me acarīti āghāto jāyati … | 4-01 head "annoyance of the mind … malevolence … conflict, opposition, ferocity, … displeasure of the mind"; 4-02 "resentment of mind, repugnance, … wrath …", semicolon frame | final tail = 2-04 string (hate, hating, the state of hating, malice, being malicious, the state of being malicious, hostility, antagonism, fierceness, abusiveness, discontent of mind); head = 4-01 with byāpatti = malice and "of mind": annoyance of mind of this kind there is, resentment, aversion, antagonism, irritation, exasperation, fury, hate, hatred, intense hatred, malice of mind, mental hatred, anger, being angry, the state of being angry; frame = 4-01 ("Annoyance arises at the thought "…", annoyance arises …, or annoyance arises without reason.") | 4-01 3, 4-02 14/8 | coordinator (dosa string to align); tail items 2 of 3 or chapter-2 tie; paṭivirodha = antagonism also in the head.
- P5-lobha | Yo rāgo sārāgo … abhijjhā lobho akusalamūlaṃ | 4-02 version | 4-01 version, with cittassa sārāgo = passion of mind | 4-01 2, 4-02 1 | 2 agents tie -> 4-01/4-03; "of mind" from the approved list.
- P6-mana | Seyyohamasmīti māno … ketukamyatā cittassa | 4-02 version | 4-01 version (Conceit that "I am better" …, loftiness, haughtiness, flag-raising, … the mind's wish to fly its banner) | 4-02 1 | tie -> 4-01.
- P7-views | Sassato lokoti vā … | 4-02: ", or" and "The soul is the same as the body" | 4-01: " or" and "The soul and the body are the same" | 4-02 20/4 | tie -> 4-01.
- P8-natthi | Natthi dinnaṃ … pavedentīti | 4-02 version | 4-03 version (there is no this world, …, there are in the world no ascetics and brahmins who … make them known), variant bracket kept | 4-02 1 | tie -> 4-01/4-03; matches the positive "Atthi dinnaṃ" line of 4-03.
- P9-suddhi | sīlena suddhi, vatena suddhi, sīlabbatena suddhīti | outside this teaching hold that "purity comes through rules …" | outside this Teaching hold that "Purification comes through rules, purification comes through observances, purification comes through rules and observances" | 4-01 3 | approved list visuddhi = purification; "the Teaching" capitalised per the style rules.
- P10-kama | kāmajjhosānaṃ | sensual attachment | sensual holding on | 4-02 2 | tie -> 4-01 (ajjhosāna = holding on in the 4-01 lobha string too).
- P11-puthujjana | ariyadhammassa akovido ariyadhamme avinīto … | is not skilled … and not trained … | is unskilled … and undisciplined … | 4-01 2 | majority (4-02, 3 lines).
- P12-uddhacca | cittassa uddhaccaṃ avūpasamo cetaso vikkhepo bhantattaṃ cittassa | restlessness of mind, unsettledness, distraction of mind, the mind's whirling | restlessness of mind, disquiet, distraction of the mind, agitation of mind | 4-02 2 | tie -> chapter 2 (cetaso = "of the mind" as in the approved "the directing of the mind").

## Sense splits and deliberate differences kept
- sukha: pleasant (feeling), happiness (factor, sukhasahagata), pleasure (bodily sukha, kāyikaṃ sukhaṃ, and the fourth-absorption formula). So Sukhabhūmiyaṃ = "In the plane of pleasant feeling" in the feeling triad (^1-988) but "In the plane of happiness" for sukhasahagatā (^1-1004). Approved list section 4.
- diṭṭhigata: "holding views" as an item of the diṭṭhi string; "wrong view(s)" in diṭṭhigatasampayutta / diṭṭhigatānaṃ pahānāya (mind-class and path formulas). Different function, kept apart.
- sārāga: "lust" in the short 2-04 lobha string and asārāga = non-lust (approved); "passion" in the long lobha string, where rāgo = lust stands right before it.
- rūpataṇhā twice in the long lobha string: craving for fine-material existence / craving for visible forms (different senses, kept, notes-4-02).
- paṭipadā = (mode of) progress; dukkhanirodhagāminī paṭipadā = the way leading to the cessation of suffering (the path of the four truths), kept.
- paṭigha: aversion (paṭighasampayutta, dosa string) vs impact (paṭighasaññā), already apart.
- āhāra = nutriment, but kabaḷīkāro āhāro = edible food (majority; the material-form item lists).
- ārabbha: "on account of" (ch. 3) vs yaṃ yaṃ vā panārabbha "whatever it takes up as its object" (ch. 2), different constructions.
- Remaining spaced " … " in 2-02 (4 lines) and 5 (1 line) mirror a spaced " …pe…" in the Pāli.

## Final scan
Re-extracted after the pass: hz_scan.py (identical Pāli clauses and lines across all parts) -> 0 groups with more than
one English rendering (57 before). hz_words.py (word-by-word string pairing) -> 33 groups left, all checked: alignment
artefacts (different list contexts, frame words absorbed into the first item) or the sense splits above; no real
variant left. Checks: check_chapter_ids.py all OK; dashcheck.py equal lines, 0 mismatches, 0 extra em-dashes for all
14 parts; no CR, no double blank lines, no "outline", "neutral", ":-", "pe…", "apart from", "Of these,",
"leaving", "except for", "states are wholesome/…", "roughness", "rites".

## Changes to en-zeroshot-terms.md
- Section 3 (frames): "Katame dhammā kusalā? = What states are wholesome?" -> "What are wholesome states?", and the two
  "… – these states are wholesome." lines -> "… – these are wholesome states." (coordinator decision on the matrix frame).
- Section 3b: mudutā string "… freedom from roughness, freedom from hardness" -> "… freedom from hardness, freedom from
  rigidity" (coordinator decision kakkhaḷa = hard).
- New section "## 6. Harmonised (consistency pass)" appended with all final forms and the sense splits.

## Not resolved (left for review)
- Strings that occur in one part only (thina, middha, kukkucca, issā, macchariya, the ten-view lines with "only this is
  true …") were not compared; nothing to harmonise against.
- The "na vattabbā" lines of chapter 5 ("these are not to be counted among X, nor among Y") keep their own wording;
  only the two "Cittaṃ na vattabbaṃ" lines were aligned with 4-02.
- Tie-breaks between 4-01/4-03 and 4-02 (ten views, natthi dinnaṃ, māna, lobha) were made by the rule above, not by
  preference of wording; a reviewer may prefer the 4-02 wording in places (e.g. "there is no this world").

## Coordinator fixes after the pass (fix_awkward.py)

- natthi ayaṃ loko…: "there is no this world, there is no other world" → "this world does not exist, the other world does not exist" (2 occurrences; the tie-break wording was not natural English)
- kāmajjhosān…: "sensual holding on" → "holding on to sensual pleasures" (4 occurrences; the tie-break wording was not natural English)
