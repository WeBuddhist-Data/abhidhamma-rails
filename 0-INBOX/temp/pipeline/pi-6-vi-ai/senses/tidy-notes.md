# pi-6 Vietnamese senses: tidy pass notes (2026-11-22)

Brief: ..\vi-senses-tidy-brief.md. Script: tidy_senses_vi.py (`families` finds the differences in code, label stripped; `apply --write` makes the exact replacements of its REPL table and writes tidy-log.tsv; `samplecheck`). Backup of the five decisions files: backup-pre-tidy\. 138 replacements: part 1 11 lines, part 2 21, part 3 45, part 4 43, part 5 18. The 91 sample lines of part 1 are untouched (samplecheck: 91 of 91 identical to sample-senses.md). All five parts VERIFY OK after the rebuild; merged with merge_senses_vi.py (pi-5 copy adapted: 5 parts, pi-6 path).

## Families and the wording chosen

- X-mūlakaṃ closing labels («phần dựa trên …», always bracketed at the end of a segment): `the part based on X, a closing section label (neuter sg.)` (part 5 wording); X = the member tag (the eye base, the world of sense desire, the controlling faculty of the eye …).
- Moment phrases: pacchimacitta = `the final mind` everywhere (parts 3 and 5; part 4 had «last mind»); uppādakkhaṇaṃ / bhaṅgakkhaṇaṃ (-ñca) take the -kkhaṇe gloss: `the moment of arising, the first phase of a mind-moment (accusative sg.)`.
- Samaṅgī persons: `one endowed with X (nominative / accusative sg.)`, `of those endowed with X (genitive pl.)`; Aggamagga- `the highest path, the path of arahantship`; Anāgāmimagga- `the path of non-returning, the third path`; magga- `a path, at the moment of the path` (pi-5 Maggasamaṅgī gloss); maggasamaṅgino is accusative pl. ('dve maggasamaṅgino ṭhapetvā').
- Suddha-X-vāro: `the section on the pure X, the X taken alone, a round of the exposition (heading)`; -mūlacakkavāro (and Padasodhanamūlacakkavāro): `the section on the cycle based on the pure X, a round of the exposition (heading)` (vi «thuần túy»).
- Other X-vāro headings: the conventions pattern `the section on X, a round of the exposition` for every form, labels `(heading)` (-vāro, -vāra), `(locative sg. heading)`, `(accusative sg. heading)`, `(instrumental sg. heading)`. The en tags (Paṇṇattivāro, Pariññāvāro, Pajahanavāro, Puggalavāro, Padasodhanavāro, Atītānāgatavāro) became this pattern too, although senses-conventions.md §4 cited Paṇṇattivāro's en tag as an example: one wording per family. Paṇṇattiuddesavāro / Paṇṇattiniddesavāro follow the sample Uddesavāro / Niddesavāro.
- yatthaka / yassaka labels: part 2 `the section by place / by person and place` (part 3 had «on place … the where-part»).
- Yamaka titles: `title of the chapter on X`, no article (Khandhayamakaṃ, Indriyayamakaṃ lost «the»); cross-references (khandhayamake, dhātuyamakassa …) `title of the chapter on X, in a cross-reference (case)`.
- Past verbs: `having X (past or completed[, negated][, with the question particle -ti])`; pajahittha re-glossed as the act: `having given up a defilement or tendency`.
- Future verbs: pi-5 pattern `will X (3rd sg. / pl. future[, negated][, with the question particle -ti])` instead of the en «(verb, present or future)»: nirujjhissati, parijānissati(-nti), pajahissati(-nti), bhāvessati(-nti), sacchikarissati(-nti), paṭilabhissanti, parinibbāyissanti.
- Participles: nirujjhamāna- `ceasing, in the process of ceasing` (conventions; = uppajjamāna- pattern). uppanna / niruddha were already parallel.
- X-dhātuṃ: Dhammadhātuṃ, cakkhudhātuṃ take the member tag (accusative). kāmadhātuṃ(-yeva) / arūpadhātuṃ: plane tags (`the world of sense desire, the sense sphere`, `the formless world, the immaterial sphere`).
- kāya- / vacī- / cittasaṅkhāro (all forms): `the bodily formation, in-and-out breathing`, `the verbal formation, directed and sustained thought`, `the mental formation, perception and feeling` (^6-6-1).
- Also: khandhe `aggregates, groups of phenomena (accusative pl.)`; puthujjanā `ordinary persons, worldlings (nominative pl.)`; nirodhasaccaṃ + `third of the four noble truths`; paccanīkaokāsā = paccanīkaokāso; parijānātīti label.

## Left as they are (pi-1 … pi-5 approved tags, verbatim for the same headword)

- dhātu nominatives mix `the X element` (organs, mind, mind-consciousness) and `the element of Xs` / `of X-consciousness` (objects, the other consciousnesses): all pi-1 … pi-5 approved; not rewritten to one pattern.
- Sacca members: nirodho `ending` vs nirodhaṃ `cessation, of suffering`; samudayo vs Samudayaṃ; maggo vs Maggaṃ / maggassa `of the way`: each a pi-5 tag for that very headword.
- Accusatives Samādhiṃ, Upekkhaṃ, Saddhaṃ `confidence in the teaching`, Paññaṃ `understanding`, purisānaṃ, vitakkavicārā `applied …` vs vitakkavicāre `directed …`, Arūpe `in the immaterial`, nirujjhanti `(3rd pl. passive)`, unlabelled parijānāti / pajahati / pajahanti / sacchikaronti / nirujjhissanti: pi-1 … pi-5 verbatim.
