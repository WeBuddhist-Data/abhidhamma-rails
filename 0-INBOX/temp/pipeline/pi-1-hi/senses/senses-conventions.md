# pi-1 Pāli→Hindi senses: conventions from part 1 (for parts 2–6)

Part 1 (agg-part1.tsv, 415 headwords) was the sample. Follow these conventions so all six parts read as one file.
The brief (..\hi-senses-brief.md) and the skill (AI_translation\skills\word-sense-grouper.md) still govern; this file only fixes the choices they leave open.

## 1. Workflow and tool

Files per part K (all in this folder): `decisions-partK.txt` (your hand-written tag table) → `partK-senses.md` (output).

```
python -I -X utf8 senses_tool_pi1.py todo   agg-partK.tsv decisions-partK.txt      # headwords still without a line
python -I -X utf8 senses_tool_pi1.py show   <headword> [<hindi value>] [<max segs>] # ids + Pāli/Hindi lines in context
python -I -X utf8 senses_tool_pi1.py build  agg-partK.tsv decisions-partK.txt partK-senses.md   # builds, then verifies
python -I -X utf8 senses_tool_pi1.py verify agg-partK.tsv partK-senses.md
```

Decision lines, one per headword, in any order (build writes agg order):
- `hw: {tag}`: one sense; the tool fills in every attested value, most frequent first.
- `hw: {tag1: v1 / v2; tag2: v3}`: explicit split. Every attested value must be placed exactly once; `*` means "all values not listed elsewhere on this line". Values are re-sorted by count inside each sense; senses keep your order (put the main sense first).
- `show` with a value prints only the line pairs whose Hindi contains it (for gapped values, the part before " … "). Use `show hw value 0` to list ids only. Check every value that looks like a different meaning before you decide to split or merge.

`verify` fails on: headword list or order differs, duplicates, a missing/extra value, a tag that equals a value, a tag that is a bare copy of an English hint (case-insensitive), Devanagari in a tag, two senses with the same tag, a candidate with "/" or "; ".

## 2. How tags are written

Pattern: **short English gloss[, distinguishing context] (grammar)**. Same style as the approved pi-4/pi-5 files.

- Gloss: describe the meaning, do not just repeat the en≈ hint. If the hint is "power of concentration", write "the power of concentration (nominative sg.)"; if it is "rigidity", write "rigidity, stiffness (nominative sg.)". A paraphrase or added synonym is better than an article.
- Context: add it only where it identifies the use: "in kāyagantha 'bodily tie'", "in the restraint passage", "in the concentration list", "as in rūpāvacara and rūpūpapatti". Mandatory in every sense of a split headword.
- Grammar in parentheses, from this fixed set:
  `(nominative sg.)`, `(nominative pl.)`, `(accusative sg.)`, `(nominative/accusative sg.)`, `(genitive sg.)`, `(genitive pl.)`, `(instrumental)`, `(locative)`, `(neuter sg.)`, `(feminine sg.)`, `(masculine sg.)`, `(neuter sg. participle)`, `(nominative pl. participle)`, `(feminine or pl. participle)`, `(absolutive)`, `(3rd sg. present)`, `(stem and nominative)`, `(compound member)`, `(compound final)`, `(heading)`, `(heading member)`, `(numeral)`, `(neuter sg. adjective)`.
  Headwords that are stems taken from compounds (Dhamma, kāya, rūpa, mana, Citta, Kusala …) get `(compound member)` or `(stem and compound member)`. Headword pieces of a chapter or section title get `(heading)` / `(heading member)`.
- Forbidden inside a tag: ": ", "; ", "{", "}", Devanagari. Keep tags under ~15 words.

### Fixed tag patterns for recurring shapes (reuse them verbatim)

| Shape | Tag pattern | Example |
|---|---|---|
| X-indriyaṃ | `the controlling faculty of X (nominative sg.)` | saddhindriyaṃ |
| X-balaṃ | `the power of X (nominative sg.)` | satibalaṃ |
| citta-X / cittassa X | `X of the mind (nominative sg.)` | cittalahutā: `lightness of the mind (nominative sg.)` |
| X-kkhandho / -khandhaṃ / -khandhassa | `the aggregate of X (nominative sg.)` / `(accusative sg.)` / `of the aggregate of X (genitive sg.)` | vedanākkhandhassa |
| samaye X (phrase "उस समय … X") | `'at that time there is X', the definition formula` | samaye phasso |
| a-/an- negatives (alobho, adoso, akakkhaḷatā …) | `absence of X (nominative sg.)` | amoho: `absence of delusion` |
| -itattaṃ | `the state of having X-ed (neuter sg.)` or `the state of being X (neuter sg.)` | sañjānitattaṃ, passambhitattaṃ |
| -anā action nouns | `X-ing, act of … (nominative sg.)` | sañjānanā: `perceiving, act of recognising` |
| paññā-X metaphors | `wisdom as a X (nominative sg.)`; the bare X: `X, wisdom as a …` | paññāsatthaṃ: `wisdom as a sword`; satthaṃ: `sword, wisdom as a blade` |
| X-sahagata(ṃ/ā) | `accompanied by X (neuter sg.)` / `(feminine or pl.)` | upekkhāsahagataṃ |
| Yo / Yā / Yaṃ / ye | `relative pronoun, that which (masculine/feminine/neuter nominative sg.)`; `those which (masculine nominative pl.)` | |
| X-dhātu (mano-, manoviññāṇa-, dhamma-) | `the X element (…)` / `the element of X (…)` | manodhātu: `the mind element` |
| X-āyatanaṃ | `the X sense base (nominative sg.)` / `the sense base of X` | manāyatanaṃ, dhammāyatanaṃ |
| X-avacara(ṃ) | `belonging to the X sphere (…)` | Rūpāvacara, Kāmāvacara |
| …-arūpino dhammā closing formula | `'arisen immaterial phenomena', the closing 'whatever others' formula (nominative pl.)` | |

## 3. One sense or several

Merge into ONE sense (candidates separated by " / "):
- Grammatical variants of one Hindi lemma: मन का विषय / मन के विषय; के साथ होना / के साथ होने वाला / के साथ (sahagata); उत्पन्न / उत्पन्न हो चुका / उत्पन्न होकर (uppanna).
- A noun and its derived adjective for the SAME meaning: शरीर / शारीरिक (kāya, physical body), मन / मानस / मानसिक (mano), सुख / सुखद (sukha), शून्य / शून्यता (suññata), इच्छा-रहित / इच्छाओं का अभाव (appaṇihita), मूल / मूल वाला (hetuka).
- Gapped and ungapped forms: प्रगति का ढंग / प्रगति का … ढंग; मन की चेतना का तत्व / मन की चेतना का … तत्व.
- Synonyms or fuller/shorter forms: क्लेश / मन के क्लेश; सूची / मूल सूची (Mātikā); दृष्टि / ग़लत दृष्टि (diṭṭhi); इंद्रिय-चेतना / चेतना (viññāṇāni); हितकर / हितकर मन (kusalaṃ); बार-बार स्मरण / स्मरण (anussati); इरादा / इरादा करना (sañcetanā); उत्पन्न / भली-भाँति उत्पन्न (samuppannā, where it only avoids repeating उत्पन्न in a synonym list); सूक्ष्म भौतिक / सूक्ष्म भौतिक लोक and अभौतिक / अभौतिक लोक (the sphere, adjective or noun).

SPLIT only for a different meaning or a different grammatical role that changes the meaning, verified with `show`:
- noun vs bahuvrīhi "having X": ārammaṇaṃ विषय vs विषय वाला (parittārammaṇaṃ).
- technical vs ordinary use: khandha समूह vs पुंज (dukkhakkhandha) vs श्रेणी (āpattikkhandha); āhāra आहार vs भोजन (kabaḷīkāra āhāra); magga मार्ग vs कुमार्ग (kummaggo); kiriyā "functional" vs करना (akiriyā); āloka आलोक (wisdom) vs प्रकाश (visible light).
- list-dependent meanings: ṭhiti स्थिरता (concentration list) vs टिके रहना (life-faculty list); sampaggāha दृढ़ता से उठाए रखना (energy list) vs स्वयं को ऊपर उठाना (conceit list).
- noun vs adjective with a different referent: saddhā श्रद्धा (faith) vs श्रद्धावान (persons having faith); cetasika मानसिक / मानसिक भाव (mental, as opposed to bodily) vs मन का सहचर (mental concomitant, acetasika).

## 4. Recurring headword families: the tags used in part 1

Reuse these senses (wording and order) whenever the same Hindi value turns up under any form of the headword. Adapt only the grammar label.

| Family | Sense tag (part 1) | Hindi |
|---|---|---|
| dhamma | `mind-objects, what the mind as sixth sense knows (compound member, as in dhammārammaṇa)` | मन के विषय / मन का विषय |
| | `phenomena, in the book title Dhammasaṅgaṇī` (in later parts: `phenomena, states (nominative pl.)`) | परिघटना |
| | `the Buddha's teaching, in dhammamacchariya and dhammapaṭisanthāra` | शिक्षा |
| rūpa | `visible form, the object of the eye (compound member, as in rūpārammaṇa)` | दृश्य रूप |
| | `the fine-material sphere, as in rūpāvacara and rūpūpapatti (compound member)` | सूक्ष्म भौतिक / सूक्ष्म भौतिक लोक |
| | `matter, material form (heading and compound member, as in Rūpakaṇḍa)` | भौतिक रूप |
| arūpa | `the immaterial sphere (compound member, as in arūpāvacara and arūpūpapatti)` | अभौतिक / अभौतिक लोक |
| arūpino | `without material form (nominative pl.)` | अभौतिक |
| kāya | `the physical body, or bodily (compound member, as in kāyaviññāṇa and kāyakamma)` | शरीर / शारीरिक |
| | `the mental body, the group of mental factors (in kāyapassaddhi and similar)` | मानसिक काया |
| | `body, in kāyagantha 'bodily tie' (compound member)` | काया |
| citta | `mind, a state or type of mind (nominative/accusative sg.)`; stem: `mind, consciousness (stem and compound member)`; `of the mind (genitive sg.)` | मन |
| mano / mana | `mind, the thinking faculty, also adjectival 'mental' in compounds`; mana: `mind, as stem in manindriya and similar compounds` | मन / मानस / मानसिक |
| mānasaṃ | `mentality, mental activity as a synonym of mind (neuter sg.)` | मानसिक क्रिया |
| cetasika | `mental, of the mind as opposed to the body (neuter sg. adjective)` | मानसिक / मानसिक भाव |
| | `a mental concomitant, in acetasikaṃ (noun)` | मन का सहचर |
| sahagata | `accompanied by, compound final (neuter sg. participle)` / `(feminine or pl. participle)` | के साथ होना / के साथ होने वाला / के साथ |
| sampayutta / vippayutta | `conjoined with, compound final (neuter sg. participle)` / `dissociated from (neuter sg. participle)` | जुड़ा / अलग |
| indriya | `controlling faculty, one of the twenty-two (nominative sg.)` | क्षमता |
| | `sense faculty to be guarded, in the restraint passage (cakkhundriya)` | इंद्रिय |
| āyatana | `sense bases, the sense fields (nominative pl.)` | इंद्रिय-क्षेत्र |
| | `bases, in abhibhāyatanāni 'bases of mastery' (compound final)` | आधार |
| ārammaṇa | `object of the mind, what the mind takes up (noun, nominative/accusative sg.)` | विषय |
| | `having such-and-such an object, as in parittārammaṇaṃ (compound final)` | विषय वाला |
| khandha | `aggregate, group of phenomena (nominative sg.)` | समूह |
| | `of a mass, in dukkhakkhandhassa 'of the whole mass of suffering'` | पुंज |
| | `classes of offences, in āpattikkhandhā (compound final)` | श्रेणी |
| āhāra | `nutriment, a sustaining condition of mind (contact, volition, consciousness)` | आहार |
| | `edible food, in kabaḷīkāro āhāro` | भोजन |
| magga | `the path, as a set of factors (nominative sg.)` / `the path (stem and heading)` | मार्ग |
| | `road, in kummaggo 'wrong road', a synonym of wrong view` | कुमार्ग |
| hetu | `roots, the wholesome and unwholesome root conditions (stem and heading)`; `roots, root conditions (nominative pl.)` | मूल |
| hetuka | `having roots, rooted (compound final)` | मूल / मूल वाला |
| kusala / akusala | `wholesome (stem and heading)`, `wholesome, said of phenomena (nominative pl.)`, `wholesome, often standing for the wholesome mind (neuter sg.)`; akusala likewise with `unwholesome` | हितकर / हानिकर |
| abyākata | `neither wholesome nor unwholesome, morally indeterminate (heading and stem)`; `neither wholesome nor unwholesome (neuter sg.)` | नैतिक रूप से अनिर्धारित |
| vipāka | `resultant, born as the result of action (compound member)` | कर्म के फल रूपी / कर्म-फल रूपी |
| kiriyā | `merely functional, producing no result (stem and compound member)` | केवल क्रिया रूपी / क्रिया रूपी / क्रिया |
| | `doing, in akiriyā 'not doing' (noun)` | करना |
| avacara | `belonging to a sphere, compound final (stem)`; kāmāvacara: `belonging to the sense sphere`; rūpāvacara: `belonging to the fine-material sphere`; arūpāvacara: `belonging to the immaterial sphere` | लोक से संबंधित … |
| kāma | `sensual pleasure, the sense sphere (compound member, as in kāmāvacara)` | इंद्रिय-सुख |
| sammā | `right, correct, prefixed to path factors (compound member)` | सही |
| | `perfectly, in sammāsambuddha (title line)` | पूर्ण रूप से |
| diṭṭhi | `view, opinion, often wrong view (stem and nominative)` | दृष्टि / ग़लत दृष्टि |
| ṭhiti | `stability, steadiness of mind (in the concentration list)` | स्थिरता |
| | `persistence, lasting of life (in the life-faculty list)` | टिके रहना |
| sukha | `pleasure, happiness, or pleasant (neuter sg.)`; sukhā: `pleasant, agreeable, of feeling or of speech (feminine adjective)` | सुख / सुखद |
| vedanā / saññā / saṅkhāra / viññāṇa | `feeling, the affective tone of experience`; `perception, recognition`; `mental formations, volitional activities`; `consciousness` | अनुभूति / पहचान / मानसिक रचनाएँ / चेतना |
| dhātu | `element, irreducible constituent (stem and compound final)` | तत्व |
| jhāna | `meditative absorption (nominative/accusative sg.)` | ध्यान |
| upekkhā | `equanimity, neutral feeling (nominative and stem)` | समभाव |
| brahma | `divine, sublime, in brahmavihāra (compound member)` | ब्रह्म |
| | `the Brahmā world, in brahmaloka (compound member)` | ब्रह्मलोक |
| Mātikā | `the matrix, the book's list of topics (heading)` (never "outline") | सूची / मूल सूची |

Expected later (not in part 1, decide with `show`): saṅkhāra as "prompting" in sasaṅkhārika (प्रेरणा) is a separate sense from मानसिक रचनाएँ; hetu as "cause" (कारण), if attested, separate from मूल; rūpa in the matter chapter is mostly भौतिक रूप, but keep दृश्य रूप (visible object) apart.

## 5. Report items

Report: headword count and the verify line; headwords with >1 sense; senses with >1 candidate; any " / "→" और " rewrite the build prints (part 1 had none); the most consequential splits and synonym clashes.
