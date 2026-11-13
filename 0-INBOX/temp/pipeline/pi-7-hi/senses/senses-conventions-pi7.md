# pi-7 (Paṭṭhāna) Pāli→Hindi senses: conventions beyond pi-1 / pi-6 (for parts 1 to 4)

Settled on the sample (`agg-sample.tsv`: the first 90 headwords of part 1 plus 30 of its multi-value headwords; `decisions-sample.txt` → `sample-senses.md`, VERIFY OK, 120 lines, 142 senses, 21 headwords with >1 sense) and a survey of the 132 multi-value headwords of `agg-all.tsv`.
Still binding: the brief (`..\hi-senses-brief.md`), the skill (`AI_translation\skills\word-sense-grouper.md`), `..\..\pi-1-hi\senses\senses-conventions.md` (tag style, grammar labels, merge/split rules, family table) and `..\..\pi-6-hi\senses\senses-conventions-pi6.md` (inflection families, verb tenses, realms, headings). The Hindi values are explained in `..\mapper-hi\hi-map-conventions-pi7.md` and `..\mapper-hi\map-reports.md`.

## 1. Workflow

```
python -I -B -X utf8 senses_tool_pi7.py todo   agg-partK.tsv decisions-partK.txt
python -I -B -X utf8 senses_tool_pi7.py show   <headword> "<hindi value>" [<max segs>]
python -I -B -X utf8 senses_tool_pi7.py build  agg-partK.tsv decisions-partK.txt partK-senses.md
python -I -B -X utf8 senses_tool_pi7.py verify agg-partK.tsv partK-senses.md
```
- `show` prints whole Pañhāvāra segments (very long lines). `sample_ctx.py` in this folder prints short windows instead: `python -I -B -X utf8 sample_ctx.py <hw> "<value>" <n> [<hw> "<value>" <n> …]` (value `-` = all occurrences). `sample_grep.py agg-partK.tsv [hw …]` prints the pi-1..pi-6 senses lines of each headword (case-insensitive). Both write nothing.
- Decision lines use the agg headword exactly, capital first letter included (`Natthi`, `Anulomaṃ`).
- Part 1 copies the 120 decision lines of `decisions-sample.txt` verbatim for the sample headwords. Any part that contains a sample headword in another case form reuses its tag shape.
- Column 2 (en≈) is a back-mapped hint and is often wrong (dhammānaṃ «condition», Nissaya «non-disappearance», Natthi «contiguity»). Tag from the Hindi and the segment.
- One attested value = one sense, always.
- verify rejects a tag equal to a hint (case-insensitive). So never write a bare «root condition» or «Negative Method»: add the role (`root condition, as a named condition (nominative)`).

## 2. Tag style

Pattern (pi-1): `short English gloss[, context or role] (grammar)`. Grammar labels as pi-1/pi-6, plus these pi-7 ones: `(stem)`, `(heading)`, `(heading member)`, `(locative, heading)`, `(heading and nominative)`, `(negative ablative)`, `(negative noun)`, `(nominative, verbal)`, `(nominative, label)`, `(gerundive)`, `(absolutive)`, `(postposition)`, `(compound)`.
English vocabulary for the 24 conditions (fixed, use exactly): root, object, predominance, proximity (anantara), contiguity (samanantara), co-arising, mutuality, support, strong-support, pre-arising, post-arising, repetition, kamma, result (vipāka; say «result condition, kamma-result …» where helpful), nutriment, faculty, jhāna, path, association, dissociation, presence, absence (natthi), disappearance (vigata), non-disappearance (avigata). Always «condition», never «relation». Phenomena = «phenomena, states»; abyākata = «neither wholesome nor unwholesome» / «indeterminate» (never «neutral»).

## 3. The condition-name families (fixed tag shapes; change only X and the grammar)

| Pāli shape | Tag | Hindi | Sample |
|---|---|---|---|
| Xpaccayo (list, heading, definition) | `X condition, as a named condition (nominative)` | X-कारण | hetupaccayo, Ārammaṇapaccayo |
| Xpaccayoti | `X condition, with quotative -ti, opening its definition (nominative)` | X-कारण | Hetupaccayoti |
| Xpaccayena | `X condition, in 'is a condition by way of X' (instrumental)` | X-कारण | hetupaccayena |
| Xpaccayā (positive) | `X condition, by which a state arises[, also in headings] (ablative)` | X-कारण | vigatapaccayā |
| bare stem X / X-paccaya member in lists and headings | `X condition, bare stem in lists and headings (stem)` | X-कारण | Anantara, Jhāna, Nissaya |
| count locative hetuyā, ārammaṇe, adhipatiyā, … | `in the X condition, the count locative (locative)` | X-कारण | (parts) |
| naXpaccayo (only «का अभाव») | `absence of the X condition, as a named negative condition (nominative)` | X-कारण का अभाव | nahetupaccayo, Nakammapaccayo |
| naXpaccayā | SPLIT by role: `without the X condition, in the negative chains (negative ablative)` + `absence of the X condition, in headings (negative noun)` | X-कारण के बिना / X-कारण का अभाव | naadhipatipaccayā, naārammaṇapaccayā |
| bare negative stem naX / noX | SPLIT by role: `absence of the X condition, bare negative stem in headings (stem)` + `without the X condition, bare negative stem in a chain of negatives (stem)` | का अभाव / के बिना | Naanantara, Napacchājāta, Naadhipati, Nonatthi |
| negative count locative nahetuyā, nakamme, … | `in the absence of the X condition, the negative count locative (locative)` | X-कारण का अभाव | (parts) |
| X-paccayasadisaṃ / naX-sadisaṃ / X-paccayādi | `like the X condition, …` / `like the absence of the X condition, …` / `the X condition and the rest, …` | … के समान / … आदि | (parts) |

With a single value, keep only the matching role tag (nahetupaccayo has no «के बिना», so one sense). The role words «negative ablative» / «negative noun» must appear in the two tags whenever a headword carries both values, so the termbase can see the split.

## 4. Condition name vs plain word (SPLIT, condition sense first unless the plain sense is more frequent)

| Headword | Senses (tag → Hindi) |
|---|---|
| Natthi / natthi | `absence condition, bare stem in lists and headings (stem)` → अनुपस्थिति-कारण; `there is not, is absent, in the editorial notes (3rd sg. present)` → नहीं / नहीं है / नहीं होना / न … है (agent drift, ONE sense) |
| Atthi / atthi | `presence condition, bare stem …` → उपस्थिति-कारण; `there is, is found, in the editorial notes (3rd sg. present)` → है |
| adhipati | `predominance condition, bare stem or separate word in lists and headings (stem)` → प्रधानता-कारण; `predominance, the predominant factor itself, in notes and answers (nominative)` → प्रधानता. Item compounds «<item> प्रधानता» (akusalādhipati) take the second shape. |
| āhāra forms | `nutriment condition, …` → आहार-कारण; `nutriment, the label or the sustaining factor (…)` → आहार; `edible food, physical food (…)` → भोजन (pi-1 split). Check āhāraṃ with `show`. |
| vipāka forms | `resultant, born as the result of action (<grammar>)` → कर्म-फल रूपी / कर्म के फल रूपी (ONE sense: two spellings of one adjective); `result condition, named in the count notes (…)` → कर्म-फल-कारण; `the kamma-result itself, rendered as a noun (…)` / `the kamma-result, resultant consciousness as a noun (nominative sg.)` → कर्म-फल. Applies to vipākaṃ, vipāko, vipākassa, vipāke. |
| Sahajāta / sahajātaṃ / purejāta / pacchājāta stems and labels | `X condition, bare stem in lists and headings (stem)` → X-कारण; `X as a label, in the section name …-vāra and the X subtype (heading member)` or `(nominative, label)` → सह-उत्पत्ति / पूर्व-उत्पत्ति / पश्चात्-उत्पत्ति (सह-उत्पन्न goes with the label). The Sahajātavāra FRAME «साथ जन्म लेकर» is a third sense: `born together with, the Sahajātavāra frame (absolutive-like participle)`. |
| pacchājātā | `post-arisen, arising later, said of mind and its concomitants (nominative pl.)` → बाद में उत्पन्न; `post-arising, the label of the post-arising kind and its questions (nominative, label)` → पश्चात्-उत्पत्ति |
| anantarā | `immediately after, with nothing in between (postposition)` → ठीक बाद (pi-6 wording); `the proximity conditions, in an editorial note (nominative pl.)` → निकटता-कारण |
| Upanissaya | `strong-support condition, bare stem …` → प्रबल आश्रय-कारण; `relying strongly on, variant spelling of the absolutive upanissāya (absolutive)` → प्रबल आश्रय से |
| Ārammaṇādhipati (and other X-adhipati subtypes) | `object-predominance, the object kind of predominance (nominative)` → विषय रूपी प्रधानता; `object and predominance conditions together, in the combination counts (compound)` → विषय-कारण प्रधानता-कारण (also fused hetādhipati «मूल-कारण प्रधानता-कारण») |
| paccayā | `because of, with X as condition, in the Paccayavāra frame (ablative)` → के कारण; `conditions, as a noun or a detached compound member (nominative pl.)` → कारण |
| paccayo | one sense: `is a condition, the predicate of the Pañhāvāra and definition formula (nominative, verbal)` → कारण होना |

## 5. Methods, sections, series, counts, items (all `(heading)` unless used in a sentence)

| Shape | Tag | Hindi |
|---|---|---|
| anuloma (all forms) | SPLIT: `the positive method, counting with the conditions present (heading and nominative)` → सकारात्मक क्रम; `conformity, the conformity moment before change-of-lineage (nominative sg.)` → अनुरूपता | |
| paccanīya / anulomapaccanīya / paccanīyānuloma | `the negative method, counting with the conditions absent`; `the positive-negative method …, present then absent`; `the negative-positive method …, absent then present` | |
| Paccaya-X / Dhamma-X | add `by conditions` / `by phenomena` (Dhammānulome `in the positive method by phenomena, division of the book (locative, heading)`) | कारणों का X / परिघटनाओं का X |
| X-vāro | `the X section, …` (Vibhaṅgavāro `the analysis section, where each answer is set out`; Saṅkhyāvāro `the counting section, the number of answers per condition`; Paccayavāro `the section on conditions, 'with X as condition'`); members of «Sahajāta-paccaya-nissaya-saṃsaṭṭha-sampayuttavāro» → `… in the section name …vāra (heading member)` | X का खंड |
| saṃsaṭṭha in that heading | ONE sense: `conjoined, intermixed, in the section name Saṃsaṭṭhavāra (heading member)` → घुला-मिला / घुले-मिले होने / घुला-मिला होना | |
| N-ka count headings (Tikaṃ, Catukkaṃ, … Tevīsakaṃ) | `<N>s, combinations of <N> conditions in the counts (heading)` (Tikaṃ `threes, combinations of three conditions in the counts`); NOT the pi-2 «triads» sense | N कारणों का मेल |
| X-dukaṃ in the counts | `pairs with the X condition, combinations in the counts (heading)`; naX-dukaṃ `pairs with absence of the X condition, in the negative counts (heading)` | X-कारण (के अभाव) के साथ दो कारणों का मेल |
| dyad / triad names | `the X dyad, <n>th dyad of the matrix (heading)` / `the X triad, …`; «matrix», never «outline». Fuller/shorter Hindi forms of one name are ONE sense (Lokiyadukaṃ «लौकिक परिघटनाओं वाला / लौकिक वाला …», dassanattikaṃ, Cittasampayuttadukaṃ, lokiyadukasadisaṃ). | X वाला दो/तीन का वर्गीकरण |
| Hetudukaṃ (both) | SPLIT: `the root dyad, first dyad of the matrix (heading)` + `pairs with the root condition, combinations in the counts (heading)` | |
| series | Ekamūlakaṃ `the one-condition series, counts that start from a single condition`; X-mūlakaṃ `the series starting from the X condition`; naX-mūlakaṃ `the series starting from absence of the X condition` | … शृंखला |
| X-padaṃ | `the X item, heading of the series that starts from it`; Abyākatapadaṃ `the indeterminate item, neither wholesome nor unwholesome` | X पद |
| Suddhaṃ / Gaṇanā | `the conditions taken singly, the single-condition count`; `the count, the reckoning of answers (heading and nominative sg.)` | |
| Paṭṭhānapāḷi / X-paṭṭhānaṃ | `the Book of Conditional Relations, title of the whole book`; `the Conditional Relations of the triads, first division of the book` | कारण-संबंध |

## 6. MERGE (one sense, candidates by count): synonyms, drift, variants

- Translator drift between parallel agents (brief): natthi (above), jappeti «पालना / करना» `fosters, indulges in, in mānaṃ jappeti 'is conceited' (3rd sg. present)` (pi-2 «nurses, fosters»), gaṇhāti «ग्रहण करना / पकड़ना / अपनाना» `grasps, adopts, in diṭṭhiṃ gaṇhāti (3rd sg. present)`, pāṇaṃ «प्राणी / जीव», Pāṇātipāto, adinnaṃ, ādiyati, samphaṃ, nillopaṃ, ekāgārikaṃ, paripanthe, tiṭṭhati («घात लगाना / खड़ा होना», in paripanthe tiṭṭhati), gāmaghātaṃ, nigamaghātaṃ, jīvitā / voropeti (in jīvitā voropeti), paritāpeti, pariyiṭṭhimūlakaṃ, sutaṃ, Paripuṇṇaṃ / paripuṇṇā «पूरा / पूर्ण / परिपूर्ण», Bhavaṅgaṃ «जीवन-धारा / भवांग», pavattipaṭisandhi (four wordings), niyatamicchādiṭṭhiyā, ruhiruppādakammassa, vaṇṇasampadaṃ, paṭighātatthāya, sajjhāyamaggena, ninnānākaraṇaṃ, āmasanaṃ, avasesā, itare «अन्य / बाकी», ekāyeva, ekasadisā, Ghaṭane «संयोजन / मेल», labbhati «मिलना / लागू होना» (`is found, is obtainable, applies here`), the paṭisambhidā and ṭhānāṭhāna knowledges (dhammappaṭisambhidāya «शिक्षा / परिघटनाओं का …» is one knowledge: merge and report it), suddhake «अकेला कारण / शुद्ध पद» (same instruction, merge and report).
- Instruction gerundives: kātabba (all forms) «बनाना / करना / तैयार करना / शामिल करना / लेना / जोड़ना चाहिए» = ONE sense `should be done, is to be worked out or included (gerundive)`; vibhajitabba «विश्लेषण / विभाजन करना / अलग-अलग दिखाना चाहिए» `should be analysed, set out separately (gerundive)`; gaṇetabba «गिनना / करना चाहिए» `should be counted, is to be reckoned (gerundive)`; vitthāretabba, niyāmetabbaṃ, uddharitabbā, and the participles anumajjantena, vibhajantena, gaṇitā / gaṇitaṃ, paccavekkhitvā.
- Grammatical variants and gapped forms: sampayuttakānaṃ «जुड़ा हुआ / जुड़ा»; kusalākusalaṃ «हितकर और हानिकर / हितकर या हानिकर» `wholesome or unwholesome, said of kamma or of a mind (neuter sg.)`; uppannaṃ, anuppannaṃ (incl. «अब तक उत्पन्न न हुआ»); upapatticittassa; kiriyaṃ / kiriyassa «केवल क्रिया रूपी / … मन»; arūpe «अभौतिक लोक / अभौतिक»; the vipākābyākata- and vipākamano(viññāṇa)dhātu- families (कर्म-फल रूपी ~ कर्म के फल रूपी, gapped ~ ungapped); kaṭattārūpaṃ; pahātabbahetukādhipati; anulomamātikā «… मूल सूची / … सूची» (`the matrix of the positive method`); garukārammaṇā; Ajjhattikā.
- Closing-pair pronoun forms are the SAME sense as the full form (pi-1 Sāsavā precedent): Sāsavaṃ / sāsavo «मन के मैलों का विषय बनने वाला / उनका विषय बनने वाला», Anāsava-, Saññojaniya-, Ganthaniya-, Nīvaraṇiya-, Parāmaṭṭhaṃ «उसका …», Upādāniya-, naanāsavo, Nasāsavañca, naaganthaniyo. Tag with pi-2 wording (sāsavo `subject to the taints, a possible object of the taints (masculine sg.)`).
- Negation placement only: nocittasahabhū / nocittasahabhuṃ «मन के साथ-साथ न होने वाला / मन के साथ-साथ होने वाला न होने वाला» = one sense. pahātabbahetukaṃ / -o «छोड़े जाने वाले मूलों वाला / छोड़े जाने वाले मूल» = one sense (shorter form inside a longer phrase; confirm with `show`).

## 7. SPLIT also (beyond §4)

- katvā: `having made, in garuṃ katvā 'having given weight to' (absolutive)` → देकर; `having performed, in uposathakammaṃ katvā 'having kept the observance day' (absolutive)` → पालन करके / करके.
- karoti: `performs, observes, in uposathakammaṃ karoti (3rd sg. present)` → पालन करना; `commits, carries out, in gāmaghātaṃ and nigamaghātaṃ karoti (3rd sg. present)` → करना / डालना.
- rūpaṃ (and other rūpa forms with both values): `matter, material form (…)` → भौतिक रूप; `visible form, the object of the eye (…)` → दृश्य रूप.
- nabhāvanāya / Nadassanena: split by FRAME (the Hindi moves the negation), tags: `neither by …, in the triad 'neither by seeing nor by development' (instrumental)` → न सत्य-दर्शन / न मानसिक अभ्यास; `not by …, in the dyad 'not to be abandoned by …' (instrumental)` → … से न / … … न; `by … with negated roots, in the -hetuka items 'without roots to be abandoned by …' (instrumental)` → … … रहित / … … से रहित. Seeing = सत्य-दर्शन («by seeing the truths»), development = मानसिक अभ्यास («by mental development»).
- saṅkhāre: `mental formations, volitional activities (accusative pl.)` (pi-1/2) → मानसिक रचनाएँ / मानसिक रचना vs `conditioned phenomena, formations seen as impermanent, in 'saṅkhāre aniccato vipassati' (accusative pl.)` → निर्मित परिघटना; confirm with `show` before splitting.
- sahajātaṃ and similar frame words: any value that is a different FRAME (Sahajātavāra «साथ जन्म लेकर», Sampayuttavāra «जुड़कर», Nissayavāra «आश्रय से») is its own sense, tagged with the frame name.

## 8. Report items

Headword count and the verify line; headwords with >1 sense; senses with >1 candidate; any " / "→" और " rewrite the build prints (the sample had none); the most consequential splits and drift merges.
