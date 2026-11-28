# pi-6 (Yamaka) Pāli→Russian senses: conventions from the sample (for parts 1–2)

The sample was agg-sample.tsv (123 headwords: the first 110 rows of part 1 plus every multi-value row of the book, 14 of them). Follow these conventions so both parts read as one file.
The brief (..\ru-senses-brief.md) and the skill (AI_translation\skills\word-sense-grouper.md) govern; this file fixes the choices they leave open. Base: ..\..\pi-1-ru\senses\senses-conventions.md and ..\..\pi-2-ru\senses\senses-conventions.md. Everything there still holds; this file repeats the essentials and records what pi-6 adds. Why a headword has the values it has: ..\mapper-ru\ru-map-conventions-pi6.md and ..\mapper-ru\notes-map-G*.md.

## 1. Workflow and tool

Files per part K (all in this folder): `decisions-partK.txt` (your hand-written tag table) → `partK-senses.md` (output).

```
python -I -X utf8 -B senses_tool_ru.py todo   --part K        # headwords still without a decision line
python -I -X utf8 -B senses_tool_ru.py prior  --part K        # each todo headword: agg row + approved pi-1 … pi-5 Russian
                                                              # senses lines + the pi-6 English senses line (start here)
python -I -X utf8 -B senses_tool_ru.py prior  <hw> [<hw> ...] # same for named headwords
python -I -X utf8 -B senses_tool_ru.py show   <hw> [<value>] [<max segs>] [<width>]   # ids + Pāli/Russian lines
python -I -X utf8 -B senses_tool_ru.py build  --part K        # builds partK-senses.md, then verifies
python -I -X utf8 -B senses_tool_ru.py verify --part K
python -I -X utf8 -B senses_tool_ru.py reuse  --part K        # lines reusing a pi-1 … pi-5 tag verbatim (for the report)
python -I -X utf8 -B senses_tool_ru.py sample                 # = build --part sample
```

- Always pass a value and a width to `show` from PowerShell (`show dukkhaṃ боль 2 200`): PowerShell 5.1 drops an empty "" argument, so `show hw "" 2` does not work; give a real value instead.
- Decision lines, one per headword, any order (build writes agg order): `hw: {tag}` = one sense, every attested value filled in, most frequent first; `hw: {tag1: v1 / v2; tag2: v3 / *}` = explicit split, every attested value placed exactly once, `*` = all values not listed elsewhere on the line. Senses keep your order (main sense first); values are re-sorted by count inside a sense.
- An attested value containing " / " is written with " и " (the build lists every rewrite; the sample had none).
- `verify` fails on: headword list or order differs, duplicates, a missing/extra value, a tag equal to a value, a tag that is a bare copy of an English hint, Cyrillic in a tag, two senses with the same tag, a candidate containing "/" or "; ", an unparsable line.

## 2. Tags

Pattern: **short English gloss[, distinguishing context] (grammar)**, as in pi-1/pi-2.

- **Earlier books first.** 286 of pi-6's 1,126 headwords have a line in a pi-1 … pi-5 Russian senses file (29 in the sample). Where pi-6 has the same Russian value in the same sense, copy the tag verbatim (sample: 18 of the 29; pi-1/pi-2 wording preferred over pi-3/4/5 where several books have the line). Change only the grammar label or the example context when the earlier one does not fit pi-6 (pi-2 arahato «in the knowledge chapter» → pi-6 «as a person in the questions and answers»); write a new tag when the earlier value differs (pi-1/2 kusalahetū «благие корни» vs pi-6 «благие причины»; pi-5 nāmā «звать»; pi-3 Ekamūlakaṃ «по одному»).
- pi-6 English senses are a hint for wording and polysemy, not binding; never copy their bare value ("root-of-roots", "section", "outline") as the tag.
- Context in every sense of a split headword: the chapter («in the chapter on truths», «in the chapter on faculties», «in the chapter on elements»), the phrase («in 'rūpadhātuṃ upapajjantassa'»), or the line (homage line).
- Grammar labels: the pi-1/pi-2 set, plus pi-6 particles spelled out in the label: `quoted with -ti`, `with ca 'and'`, `with ceva 'both … and'`; `(locative phrase)` for the moment keys; `(colophon)` for the closing labels («… niṭṭhito»); `(neuter nominative pl.)` for -āni.
- Forbidden in a tag: ": ", "; ", "{", "}", Cyrillic, a bare English hint. Keep tags under ~20 words.

## 3. One sense or several

Merge (one sense, candidates " / "):
- grammatical variants and construction variants of one meaning: возникающий / возникновение and прекращающийся / прекращение (uppajjamānaṃ / nirujjhamānaṃ: the participle; in the past-time questions «uppajjamānaṃ khaṇaṃ … vītikkantaṃ» the same participle qualifies khaṇaṃ and the Russian nominalises it inside «миновал момент возникновения»; same meaning, as pi-2 uppajjitvā после возникновения / возникновение);
- жить последней жизнью / в последний раз (Pacchimabhavikānaṃ: one referent, those in their final existence; «в последний раз» is the map's rendering only before upapajjantānaṃ / upapajjantīnaṃ, «кто в последний раз перерождается»; as the pi-1 relative-pronoun rule, the Russian choice follows the construction, not a meaning change);
- two phrasings of one abbreviation note: так же как в разделе с «у кого» / такой же как раздел с «у кого» (yassakasadisaṃ);
- gapped phrases with their plain form: момент распада ума / момент распада … ума (the gap holds «этого» for the unlisted tassa, G9 citta_moment rule); существование с пятью составляющими / существование … с пятью составляющими (^6-5-30 «с четырьмя составляющими и с пятью составляющими»). A gapped value is one candidate, kept as written;
- tense values: one headword = one Pāli form = one sense, even where the map value is the infinitive of another tense form (uppajjittha = возникать, like uppajjati); the denied-negative value of a nuppajj- form (positive «возникать» where the Russian says «но у них возникает Y») is a candidate of the same sense, not a new one.

Split (checked with `show`):
- **rūpaṃ**: материальная форма (matter, «Kusalasamuṭṭhānaṃ rūpaṃ») vs форма (the bare word of the term-analysis questions of the khandha, āyatana and dhātu chapters, «rūpaṃ rūpakkhandho?», «Rūpadhātuṃ ṭhapetvā avasesaṃ rūpaṃ», wider than matter: piyarūpa). Matter first.
- **arahato**: Достойный (homage line, every chapter's «Namo tassa …») vs архат (the person in the anusaya and other answers). pi-2 split and order.
- **Rūpadhātu-**: мир форм (fine-material world, a plane of rebirth, anusaya chapter) vs элемент видимых форм (one of the eighteen elements, dhātu chapter). pi-2 dhātu split (элемент vs мир).
- **dukkha-**: страдание (the truth, saccayamaka) vs боль (the faculty dukkhindriya, indriyayamaka; notes-map-G10a). Suffering first for every form of the family (dukkhaṃ, dukkhanti, Dukkhañca), whichever is more frequent in the form.
- **upapajjissati**: переродиться (will be reborn, ^6-10-309, kept as written) vs возникнуть (^6-3-212 source slip for uppajjissati, rendered as meant «не возникнет сфера носа»). The slip sense is named as a slip in its tag.
- Later (expected, decide with `show`): sukhaṃ удовольствие (faculty) vs счастье; arūpa мир без форм (plane) vs нематериальный (notes-map-G2: not covered by the frame); hetu причина (Hetuvārādi) vs корень (ahetuka / sahetuka); cittassa ум vs вид ума if a numbered class turns up; dhātu элемент vs мир (kāmadhātu, arūpadhātu, as Rūpadhātuṃ).

## 4. Recurring headword families: the tags of the sample (and of the families still to come)

Reuse these senses (wording and order) whenever the same Russian value turns up under any form of the headword; adapt only the grammar label and the particle note.

| Family | Sense tag | Russian |
|---|---|---|
| kusala / akusala / abyākata | `wholesome, said of phenomena (nominative pl.)` (pi-1); neuter `wholesome, the wholesome as a substantive (neuter sg.)`; same for `unwholesome`, `ethically indeterminate, neither wholesome nor unwholesome` | благой / неблагой / этически неопределённый |
| X dhammā | `wholesome phenomena (nominative pl.)` (pi-1); `ethically indeterminate phenomena`; Nāmā `mental, of the mind side as opposed to matter, in 'nāmā dhammā' (nominative pl.)` | благие явления, умственный |
| X-mūla(ā/āni) | `wholesome roots (nominative pl.)` (pi-1/2); Mūlāni `roots, the root conditions (nominative pl.)` (pi-1); Mūlaṃ `root, a root condition (nominative sg.)` | благие корни, корни, корень |
| X-mūlamūla- | `wholesome roots of roots, in the root-of-roots method (nominative pl.)` | благие корни корней |
| X-mūlena | `with a wholesome root, the root that states share (instrumental sg.)` | благой корень |
| X-mūlaka- / X-mūlamūlaka- | `based on a wholesome root[ of roots], in the based-on-a-root[-of-roots] method (…)` | основанный на благом корне [корней] |
| ekamūla- / aññamaññamūla- | `having a common root, sharing one root with another state (…)` / `having a mutual root, each being a root of the other (…)` | имеющий общий / взаимный корень |
| ekamūlamūla- / aññamaññamūlamūla- | `having a common / mutual root of roots, in the root-of-roots method (…)` | … корень корней |
| ekamūlaka- / aññamaññamūlaka- (+ -mūlaka-) | `based on a common / mutual root[ of roots], in the based-on-a-root[-of-roots] method (…)` | основанный на общем / взаимном корне [корней] |
| root-compound grammar | -ā `(nominative pl.)`, -aṃ `(neuter sg.)`, -āni `(neuter nominative pl.)`, -āti `quoted with -ti (nominative pl.)`, -añceva `with ceva 'both … and' (neuter sg.)`; the Russian value is the same for all forms (map §2) | |
| Hetuvārādi verse | `cause, the second of the ten names for a root in the Hetuvārādi verse (nominative sg.)`; nidāna third, sambhava fourth, pabhava fifth, samuṭṭhāna/āhāra/ārammaṇa sixth to eighth, paccaya ninth (pi-5 `support, conditioning factor`), samudaya tenth | причина, источник, начало, исток, … условие, возникновение |
| X-hetū … X-samudayā | `wholesome causes, the hetu member of the ten-name series (nominative pl.)` (… sources / origins / springs / producers / nutriment / objects / conditions / originations) | благие причины … благие возникновения |
| headings | X-yamakaṃ `the pairs on X, title of the X chapter (heading and colophon)`; Yamakapāḷi `the canonical text of the Yamaka, full title of the book of pairs (title line)`; -vāro `the section on X (heading)`; -nayo `the method of X, Nth questioning method (heading member)`; uddeso `statement, the opening enumeration of a section (heading)` (pi-1); niddeso `exposition, detailed explanation (heading member)` (pi-1); colophons `the section of the statement, closing label of the opening enumeration (colophon)` | парные вопросы о X, раздел о X, метод X, перечень, разъяснение |
| headings to come | anulomaṃ / paccanīkaṃ `the positive / negative form of the questions (heading member)`; paṇṇattivāro `the section on designations (heading)`; pavattivāro `the section on occurrence (heading)`; pariññāvāro `the section on full understanding (heading)`; -uppādavāro / -nirodhavāro `the section on arising / ceasing (heading)` | утвердительная / отрицательная форма, раздел об обозначениях … |
| tense (to come) | uppajjati `arises, comes into being (3rd sg. present)`; uppajjittha `arose, came into being (3rd sg. aorist)`; uppajjissati `will arise, will come into being (3rd sg. future)`; nirujjhati / -ittha / -issati `ceases / ceased / will cease (…)`; nuppajj- `does not arise / did not arise / will not arise (…, negated)`; uppanna `arisen, come into being`; niruddha `ceased, stopped`; uppajjamāna / nirujjhamāna as in the sample | возникать, возникнуть, прекращаться, прекратиться, не возникать … |
| persons (to come) | upapajjantānaṃ `of those being reborn (genitive pl. present participle)`; cavantānaṃ `of those passing away (genitive pl. present participle)`; parinibbantānaṃ `of those attaining final extinction (genitive pl. present participle)`; Pacchimabhavikānaṃ as in the sample; Itaresaṃ `of the others, the remaining persons (genitive pl.)`; arahato / Arahā as in the sample | перерождаться, умирать, достигать окончательного угасания … |
| planes (to come) | Pañcavokāre `in the five-constituent existence, the plane of beings with all five aggregates (locative sg.)` (-aṃ accusative, -ā nominative); -ānaṃ `of the beings of the five-constituent existence (genitive pl.)`; catu- / eka-vokāra likewise (four / one constituent); Arūpe `in the formless world, the immaterial plane (locative sg.)`; Asaññasatta- `the beings without perception, the non-percipient plane (…)`; Suddhāvāsa- `the Pure Abodes (…)` / -ānaṃ `of the beings of the Pure Abodes (genitive pl.)` | существование с пятью составляющими, существа с …, мир без форм, существа без восприятия, Чистые обители |
| moments | cittassa uppādakkhaṇe / bhaṅgakkhaṇe `at the moment of the mind's arising / dissolution, the arising / break-up instant of a consciousness (locative phrase)`; X-sampayutta- / X-vippayuttacittassa … `at the arising moment of a mind conjoined / not conjoined with X (locative phrase)`; pacchimacittassa … `… of the last mind (locative phrase)`; uppādakkhaṇe alone `at the moment of arising (locative)` | момент возникновения / распада ума (… ума) |
| answers (to come) | Āmantā `yes, the affirmative answer (particle)`; No `no, the negative answer (particle)`; Natthi `there is no such case, the answer 'none' (verb as answer)` | да, нет, такого нет |
| rūpa / dukkha / arahato / Rūpadhātu | the split tags of the sample (sample-senses.md lines 71, 111, 116–119) | |

## 5. Report items

Headword count and the verify line; headwords with >1 sense; senses with >1 candidate; the `reuse` line; any " / "→" и " rewrite; the most consequential splits and synonym clashes; any source slip that produced its own sense.
