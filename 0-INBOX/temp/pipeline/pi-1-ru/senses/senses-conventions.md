# pi-1 Pāli→Russian senses: conventions from the sample (for parts 1–4)

The sample was agg-sample.tsv (120 headwords: the first 90 of part 1 plus 30 multi-value ones). Follow these conventions so all parts read as one file.
The brief (..\ru-senses-brief.md) and the skill (AI_translation\skills\word-sense-grouper.md) still govern; this file only fixes the choices they leave open. Modelled on ..\ref\hi_senses-conventions.md (the Hindi pi-1 run); where the two agree, the Russian file reuses the Hindi tag wording.

## 1. Workflow and tool

Files per part K (all in this folder): `decisions-partK.txt` (your hand-written tag table) → `partK-senses.md` (output).

```
python -I -X utf8 senses_tool_ru.py todo   --part K                  # headwords still without a decision line
python -I -X utf8 senses_tool_ru.py show   <headword> [<russian value>] [<max segs>]   # ids + Pāli/Russian lines
python -I -X utf8 senses_tool_ru.py build  --part K                  # builds partK-senses.md, then verifies
python -I -X utf8 senses_tool_ru.py verify --part K
```

Decision lines, one per headword, any order (build writes agg order):
- `hw: {tag}`: one sense; the tool fills in every attested value, most frequent first.
- `hw: {tag1: v1 / v2; tag2: v3}`: explicit split. Every attested value placed exactly once; `*` = "all values not listed elsewhere on this line". Values are re-sorted by count inside each sense; senses keep your order (main sense first).
- `show hw value 0` lists ids only; `show hw value 3` prints the first 3 segments' Pāli/Russian line pairs containing the value. Check every value that looks like a different meaning before you split or merge.
- An attested value containing " / " must be written with " и " in the decisions file (the build prints every such rewrite; the sample had none).

`verify` fails on: headword list or order differs, duplicates, a missing/extra value, a tag equal to a value, a tag that is a bare copy of an English hint (case-insensitive), Cyrillic in a tag, two senses with the same tag, a candidate containing "/" or "; ", an unparsable line.

## 2. How tags are written

Pattern: **short English gloss[, distinguishing context] (grammar)**, as in the approved pi-4/pi-5 Russian files.

- Gloss: describe the meaning; do not repeat the en≈ hint. Hint "power of concentration" → `the power of concentration (nominative sg.)`; hint "calm" → `calming of the mind, serenity (nominative sg.)`.
- Context: only where it identifies the use, and in every sense of a split headword: "in kummaggo 'crooked road'", "in the life-faculty list", "as in rūpāvacara and rūpūpapatti".
- Grammar labels (same set as Hindi): `(nominative sg.)`, `(nominative pl.)`, `(nominative/accusative sg.)`, `(accusative sg.)`, `(genitive sg.)`, `(instrumental)`, `(locative)`, `(neuter sg.)`, `(neuter sg. participle)`, `(nominative pl. participle)`, `(neuter sg. adjective)`, `(absolutive)`, `(stem and nominative)`, `(compound member)`, `(compound final)`, `(stem and compound member)`, `(heading)`, `(heading member)`, `(title line)`, `(noun)`, `(adverb and adjective)`.
- Forbidden in a tag: ": ", "; ", "{", "}", Cyrillic. Keep tags under ~15 words.

### Fixed tag patterns (reuse verbatim)

| Shape | Tag pattern | Example |
|---|---|---|
| X-indriyaṃ | `the controlling faculty of X (nominative sg.)` | saddhindriyaṃ |
| X-balaṃ | `the power of X (nominative sg.)` | satibalaṃ |
| citta-X / cittassa X | `X of the mind (nominative sg.)` | cittalahutā: `lightness of the mind (nominative sg.)` |
| bare X of the same list | `X, synonym (nominative sg.)` | lahutā: `lightness, buoyancy (nominative sg.)` |
| a-/an- negatives | `absence of X (nominative sg.)` | amoho: `absence of delusion (nominative sg.)` |
| X-sahagataṃ | `accompanied by X (neuter sg. participle)` | upekkhāsahagataṃ |
| Yo / Yā / Yaṃ | `relative pronoun, that which or whatever (masculine / feminine / neuter nominative sg.)` | |
| X-avacara(ṃ) | `belonging to the X sphere (…)` | kāmāvacaraṃ |
| closing formula pieces | `'arisen immaterial phenomena', the closing 'whatever others' formula (nominative pl.)`; gapped pieces: `'…', the gapped pair of the closing formula` | samuppannā arūpino |

## 3. One sense or several

Merge into ONE sense (candidates separated by " / "):
- Grammatical variants of one Russian lemma: возникать / возникший / возникнуть (uppannaṃ); сопровождаемый / сопровождаться (sahagataṃ); сводка / сводки; корни / корень (hetuka); виды ума / виды … ума.
- Noun and its derived adjective or adverb for the SAME meaning: тело / телесный (kāya, physical body); ум / умственный (mano); жизненный / жизнь (jīvita); пустой / пустота (Suññataṃ); правильный / правильно (sammā); внутри себя / внутренний (ajjhattaṃ); душевный / душевное состояние (cetasikaṃ, mental as opposed to bodily).
- Sphere adjective and sphere noun: мир форм / форма (rūpa; "форма" in the map is the genitive inside «миру форм»); относящийся к миру / мир (avacara); мир форм / относящийся к миру форм (Rūpāvacara); без форм / мир без форм (Arūpa).
- Synonyms or fuller/shorter forms: благой ум / благой (kusalaṃ); результат / результат действий (vipāka); проявление намерения / намерение (sañcetanā); возникший / полностью возникший (samuppannā, where полностью only avoids repeating возникший in a synonym list); прямота / прямизна (ujukatā, both in the uprightness synonym list); функциональный … ум / функциональный … умственный.
- The relative pronoun: то что / любой / то самое / который are one sense (Yo, Yaṃ). The Russian choice follows the construction (definition, "любой другой" in the matter chapter, emphatic "yo eva so"), not a meaning change.

SPLIT only for a different meaning or a different referent, verified with `show`:
- citta: ум (a mind, state of mind) vs вид ума (a numbered class of consciousness, "Paṭhamaṃ cittaṃ"). Unlike Hindi, kept apart because the Russian count-noun use needs its own rendering.
- technical vs ordinary use: khandha совокупности vs классы (āpattikkhandhā); āhāra питание (the three nutriments) vs пища (kabaḷīkāra āhāra, edible food); magga путь vs дорога (kummaggo); kiriyā функциональный vs делание (akiriyā); hetu корни vs причины (ṭhānakusalatā); āyatana сферы восприятия vs сферы (abhibhāyatana); brahma божественный (brahmavihāra) vs Брахма (brahmaloka).
- list-dependent meanings: ṭhiti устойчивость (concentration list) vs сохранение (life-faculty list); sampaggāha крепкое удержание (energy list) vs возвеличивание себя (conceit list).
- noun vs adjective with a different referent: cetasika душевный (mental, as opposed to bodily) vs сопутствующий уму (mental concomitant, acetasikaṃ).
- the mano rule of the brief: ум / умственный vs разум (разум only in the citta synonym string "cittaṃ mano mānasaṃ … mano", where it avoids a second ум).
- fixed compound: parāmāsa искажение vs приверженность (only in sīlabbataparāmāsa).
- use of ārabbha: имеющий объектом (taking a sense object) vs в отношении (views about the past/future).
- matrix vs matter chapter: duka пары (dyads of the matrix) vs классификация по два (Rūpakaṇḍa's twofold classification).

## 4. Recurring headword families: the tags of the sample

Reuse these senses (wording and order) whenever the same Russian value turns up under any form of the headword; adapt only the grammar label.

| Family | Sense tag (sample) | Russian |
|---|---|---|
| dhamma | `mind-objects, what the mind as sixth sense knows (compound member, as in dhammāyatana and dhammārammaṇa)` | объекты ума / объект ума |
| | `phenomena, states, in the book title Dhammasaṅgaṇī (compound member)` (elsewhere: `phenomena, states (nominative pl.)`) | явление / явления |
| | `the Buddha's teaching, in dhammamacchariya and dhammapaṭisanthāra (compound member)` | Учение |
| rūpa | `visible form, the object of the eye (compound member, as in rūpārammaṇa)` | видимая форма |
| | `the fine-material sphere, as in rūpāvacara and rūpūpapatti (compound member)` | мир форм / форма |
| | `matter, material form (heading and compound member, as in Rūpakaṇḍa)` | материальная форма |
| arūpa | `the immaterial sphere, or immaterial (compound member, as in arūpāvacara and arūpūpapatti)` | без форм / мир без форм |
| arūpino | `without material form (nominative pl.)` | нематериальный |
| kāya | `the physical body, or bodily (compound member, as in kāyaviññeyya and kāyaviññatti)` | тело / телесный |
| | `the mental body, the group of mental factors (compound member, as in kāyapassaddhi)` | умственное тело |
| | `touch as the body sense, in kāyaviññāṇa 'tactile consciousness' (compound member)` | осязательный |
| citta | `mind, a state of mind (nominative/accusative sg.)` | ум |
| | `a type of mind, the numbered class in 'paṭhamaṃ cittaṃ' (nominative sg.)`; pl.: `types of mind, the classes of consciousness (nominative pl.)` | вид ума / виды ума |
| mano / mana | `mind, the thinking faculty, also adjectival 'mental' (compound member, as in manodhātu and manosañcetanā)` | ум / умственный |
| | `intellect, a synonym of mind in the definition of citta (nominative sg.)` | разум |
| | mana: `mind, as stem in manindriya and similar compounds` | ум |
| cetasika | `mental, of the mind as opposed to the body (neuter sg. adjective)` | душевный / душевное состояние |
| | `a mental concomitant, in acetasikaṃ (noun)` | сопутствующий уму |
| sahagata | `accompanied by, compound final (neuter sg. participle)` | сопровождаемый / сопровождаться |
| sampayutta | `conjoined with, compound final (neuter sg. participle)` | связанный |
| indriya | `controlling faculty, one of the twenty-two (nominative sg.)` | способность |
| bala | `power, strength, one of the seven powers (nominative sg.)` | сила |
| āyatana | `sense bases, the sense fields (nominative pl.)` | сферы восприятия |
| | `bases, in abhibhāyatanāni 'bases of mastery' (compound final)` | сферы |
| ārammaṇa | `object of the mind, what the mind takes up (nominative/accusative sg.)` | объект |
| ārabbha | `taking as object, of a mind arising on a sense object (absolutive)` | имеющий объектом |
| | `concerning, about, in the views 'about the past' and 'about the future' (absolutive)` | в отношении |
| khandha | `aggregates, groups of phenomena (nominative pl.)` | совокупности |
| | `classes of offences, in āpattikkhandhā (compound final)` | классы |
| āhāra | `nutriment, a sustaining condition (contact, volition, consciousness) (nominative sg.)` | питание |
| | `edible food, in kabaḷīkāro āhāro (nominative sg.)` | пища |
| magga | `the path, as a set of factors (nominative sg.)` | путь |
| | `road, in kummaggo 'crooked road', a synonym of wrong view` | дорога |
| hetu | `roots, the root conditions (nominative pl.)` | корни |
| | `causes, in the definition of skill in what is possible (nominative pl.)` | причины |
| hetuka | `having roots, rooted, in sahetuka and ahetuka (compound final)` | корни / корень |
| kusala | `wholesome, said of phenomena (nominative pl.)`; `wholesome, often standing for the wholesome mind (neuter sg.)` | благой / благой ум |
| vipāka | `result of action, resultant (compound member)` | результат / результат действий |
| kiriyā | `merely functional, producing no result (stem and compound member)` | функциональный |
| | `doing, in akiriyā 'not doing' (noun)` | делание |
| avacara | `belonging to a sphere, or the sphere itself (stem and compound final)`; kāmāvacara: `belonging to the sense sphere`; Rūpāvacara: `belonging to the fine-material sphere, or that sphere` | относящийся к миру … / мир … |
| kāma | `the sense sphere, as in kāmāvacara (compound member)` | чувственные желания |
| | `sensual desire or pleasure, in kāmarāga, kāmāsava and kāmataṇhā (compound member)` | чувственные удовольствия / чувственный |
| sammā | `right, correct, rightly, prefixed to path factors (compound member and adverb)` | правильный / правильно |
| | `perfectly, in sammāsambuddha (title line)` | полностью |
| sukha | `happiness, pleasant feeling of mind, as jhāna factor and in adukkhamasukha (neuter sg.)` | счастье / приятный |
| | `bodily pleasure, in kāyikaṃ sukhaṃ and sukhindriya (neuter sg.)` | удовольствие |
| jīvita | `life, vitality (compound member, as in jīvitindriya, and nominative)` | жизненный / жизнь |
| ṭhiti | `stability, steadiness of mind (in the concentration list)` | устойчивость |
| | `persistence, lasting of life (in the life-faculty list)` | сохранение |
| sampaggāha | `firm upholding of the mind (in the energy list)` | крепкое удержание |
| | `self-exaltation (in the conceit list)` | возвеличивание себя |
| parāmāsa | `misapprehension, wrong grasping by views (stem and heading member)` | искажение |
| | `adherence, in sīlabbataparāmāsa 'adherence to rules and vows' (compound final)` | приверженность |
| brahma | `divine, sublime, in brahmavihāra (compound member)` | божественный |
| | `the Brahmā world, in brahmaloka (compound member)` | Брахма |
| duka | `pairs, the dyads of the matrix (heading member)` | пары |
| | `classification by twos, the section of the matter chapter (heading)` | классификация по два |
| Nikkhepa | `summary, the concise exposition of the matrix (heading member, as in Nikkhepakaṇḍa)` | сводка / сводки |
| diṭṭhi | `view, opinion, right or wrong (stem and nominative)` | воззрение |
| ajjhatta | `internally, within oneself (adverb and adjective)` | внутри себя / внутренний |

Expected later (decide with `show`): saṅkhāra as "prompting" in sasaṅkhārika vs the aggregate (формирующие факторы); mātikā (the matrix, never "outline"); kāya in kāyagantha; khandha in dukkhakkhandha; āloka (wisdom) vs light; hetu as cause elsewhere; vuṭṭhāna избавление (from offences) vs выход (from attainments), as named in the brief.

## 5. Report items

Report: headword count and the verify line; headwords with >1 sense; senses with >1 candidate; any " / "→" и " rewrite the build prints; the most consequential splits and synonym clashes.
