# Skills Catalog

This file catalogues every skill used in the abhidhamma-rails vault, grouped by workflow phase. Each entry names the skill, states its purpose, describes its inputs and outputs, and points to the SKILL.md that operationalises it. For the phase a skill belongs to and the failure mode it addresses, see the **Translation workflow** section of the [vault README](../../README.md).

Skills that already exist are marked **[exists]**. Skills that are planned but not yet written are marked **[planned]**.

The translation pipeline reads top-to-bottom: source ingestion populates `1-SOURCES/`, the rails-building skills turn those sources into `2-RAILS/` context (Sections / Verses / Local-Wiki / Bilingual Glossaries), the translation skills consume those rails to produce `3-TRANSFORMATIONS/Translations/<track-name>/`, and the QA skill checks the output back against the rails.

---

## Source ingestion skills

These skills bring raw material into `1-SOURCES/` in a consistent, citation-ready format.

### `epub-to-markdown` **[exists]**
Converts EPUB files (commentaries, reference texts) into formatted Obsidian markdown with block IDs, headings, and frontmatter.
→ [`epub-to-markdown/SKILL.md`](epub-to-markdown/SKILL.md)

### `json-to-source-text` **[exists]**
Converts tipitaka.org JSON exports of root texts into formatted source-text markdown files.
→ [`json-to-source-text/SKILL.md`](json-to-source-text/SKILL.md)

### `json-to-commentary` **[exists]**
Converts tipitaka.org JSON exports of Pali commentaries (aṭṭhakathā) into formatted commentary markdown files.
→ [`json-to-commentary/SKILL.md`](json-to-commentary/SKILL.md)

### `format-root-text` **[exists]**
Normalises an existing root-text file: heading structure, block IDs, verse formatting.
→ [`format-root-text/SKILL.md`](format-root-text/SKILL.md)

### `format-commentary` **[exists]**
Normalises an existing commentary file: OCR cleanup, heading structure, paragraph granularity, block IDs.
→ [`format-commentary/SKILL.md`](format-commentary/SKILL.md)

### `add-toc` **[exists]**
Inserts or regenerates a table of contents in a source or rails file.
→ [`add-toc/SKILL.md`](add-toc/SKILL.md)

---

## Rails-building skills (context preparation for translation)

These skills populate `2-RAILS/` with the structured context that translation and QA skills consume.

### `section-summary-raw` **[exists]**
**Purpose:** Generate a summary of one table-of-contents node in the original language, drawn from a single commentary.
**Inputs:** Commentary file(s) in `1-SOURCES/`, the TOC node to summarise.
**Outputs:** One summary file per commentary under `2-RAILS/Sections/Raw/<commentary-name>/<node-id>.md`.
**Rules:** Use only the terminology the commentary itself uses. No translation. No paraphrase beyond compression. Every claim cites a block ID from the source file.
→ [`section-summary-raw/SKILL.md`](section-summary-raw/SKILL.md)

### `section-summary-combined` **[exists]**
**Purpose:** Combine the per-commentary raw summaries for one TOC node and add an English translation of the combined summary.
**Inputs:** All raw summary files for the target node under `2-RAILS/Sections/Raw/`.
**Outputs:** One combined file at `2-RAILS/Sections/<node-id>.md` containing the original-language synthesis and an English translation.
**Rules:** Use only the terminology the commentary itself uses. No translation. No paraphrase beyond compression. Every claim cites a block ID from the source file.
→ [`section-summary-combined/SKILL.md`](4-SYSTEM/Skills/section-summary-raw/section-summary-combined/SKILL.md)

### `atthakatha-summaries` **[exists]**
**Purpose:** Create structured Pāli-language introductory summaries for each TOC node in a root text, drawn strictly from the Aṭṭhakathā. Produces or extends the consolidated summaries file at `2-RAILS/Sections/<text-name>-summaries.md`, with a full TOC block, hierarchical block IDs, back-links, summary paragraphs, and block-level citations.
**Inputs:** Root text in `1-SOURCES/Text/`; corresponding Aṭṭhakathā in `1-SOURCES/Commentaries/`; existing summaries file (if any) at `2-RAILS/Sections/<text-name>-summaries.md`.
**Outputs:** Updated `2-RAILS/Sections/<text-name>-summaries.md` with new or extended TOC entries and Pāli summary paragraphs, each citing at least one block ID from the source commentary.
**Rules:** Summaries written in Pāli using the commentary's own vocabulary. No English. No parametric knowledge. Every paragraph cites a specific block ID.
→ [`atthakatha-summaries/SKILL.md`](atthakatha-summaries/SKILL.md)

### `practice-summaries` **[exists]**
**Purpose:** Extract practical information from commentaries to provide guidance on doing less harm, doing more good, and cultivating the mind based on the root text.
**Inputs:** Commentary file(s) in `1-SOURCES/`, Root text TOC.
**Outputs:** One practice-oriented summary file at `2-RAILS/Sections/<text name>-practice.md`.
**Rules:** Grounded strictly in traditional commentary. Structured around three pillars: (1) Doing Less Harm, (2) Doing More Good, (3) Cultivating the Mind. Use technical Pāli terms with diacritics.
→ [`practice-summaries/SKILL.md`](practice-summaries/SKILL.md)

### `verse-context` **[exists]**
**Purpose:** Build the verse-level context file for one verse.
**Inputs:** Root-text verse (from `1-SOURCES/`), all commentary passages that discuss it (via block transclusions from `1-SOURCES/`).
**Outputs:** One file at `2-RAILS/Verses/<verse-id>.md` containing: (1) transclusions of commentary passages, (2) a synthesis of the commentators' interpretations in the original language, (3) a disambiguated restatement of the verse in the original language precise enough to exclude any mistranslation.
→ [`verse-context/SKILL.md`](verse-context/SKILL.md)

### `local-wiki-article` **[exists]**
**Purpose:** Create or update a Local-Wiki article for one key term.
**Inputs:** Commentary passages that explain or define the term (via block citations from `1-SOURCES/`).
**Outputs:** One file at `2-RAILS/Local-Wiki/<term>.md` containing: cited commentary explanations in the original language, and a short contextual definition drafted from those citations (also in the original language).
→ [`local-wiki-article/SKILL.md`](local-wiki-article/SKILL.md)

### `interlinear-gloss` **[exists]**
**Purpose:** For one root text + one translation, build a word-by-word gloss file at `2-RAILS/Bilingual-Glossaries/Raw/<source>-<target>-gloss.md` pairing them verse by verse. Each verse is rendered as the translation followed by a ```gloss``` block containing a vertical list of Pāli-to-target pairs. This format supports long compounds and bracketed semantic expansions (the "neither" rule). Token-level alignment lives here so every downstream bilingual glossary step reads from one place. Untranslated sections are handled via a bracketed fallback from the Rhys Davids (`en-rd`) translation.
**Inputs:** `1-SOURCES/Text/<root-text>.md`, one translation under `1-SOURCES/Translations/<Language>/`.
**Outputs:** One gloss file per translation under `2-RAILS/Bilingual-Glossaries/Raw/<source-lang>-<target-lang-tag>-gloss.md`.
**Helper:** `scripts/scaffold_gloss.py` aligns blocks by `^block-id`, populates the translation and a vertical `gloss` block with Pāli tokens and `--` placeholders, and re-runs idempotently (preserves filled lines by matching Pāli tokens). `--validate` checks for missing glosses.
→ [`interlinear-gloss/SKILL.md`](interlinear-gloss/SKILL.md)

### `glossary-extract-raw` **[exists]**
**Purpose:** Extract every source-language keyword and the rendering(s) it receives, from one interlinear gloss file, into a raw per-source bilingual glossary.
**Inputs:** One gloss file at `2-RAILS/Bilingual-Glossaries/Raw/<source>-<target>-gloss.md`.
**Outputs:** One bilingual glossary file at `2-RAILS/Bilingual-Glossaries/Raw/<source>-<target>.md` with a table mapping source lemma → rendering used in that translation.
**Helper:** `scripts/extract_pairs.py` walks every ``gloss`` block, supports both legacy horizontal and new vertical formats, and emits a CSV of `(source_token, source_lemma, target_rendering, block_id)` rows ready for tallying.
→ [`glossary-extract-raw/SKILL.md`](glossary-extract-raw/SKILL.md)

### `glossary-combine` **[exists]**
**Purpose:** Merge all raw bilingual glossary files for one language pair into a single consolidated bilingual glossary.
**Inputs:** All relevant files under `2-RAILS/Bilingual-Glossaries/Raw/`.
**Outputs:** One consolidated bilingual glossary at `2-RAILS/Bilingual-Glossaries/<lang-pair>.md` showing every attested rendering side by side.
**Helper:** `scripts/combine_glossaries.py` merges raw rendering tables by keyword, sums frequencies across sources, normalises case-only duplicates, and writes the consolidated file with Local-Wiki links auto-populated where articles exist.
→ [`glossary-combine/SKILL.md`](glossary-combine/SKILL.md)

### `glossary-select` **[exists]**
**Purpose:** Build the prescriptive per-track termbase for one track by selecting the preferred rendering for each term from the consolidated bilingual glossary, guided by the track's `requirements.md`. If no existing rendering is satisfactory, derive one from the Local-Wiki article for that term and feed the new rendering back into the consolidated bilingual glossary.
**Inputs:** `2-RAILS/Bilingual-Glossaries/<lang-pair>.md`, `3-TRANSFORMATIONS/Translations/<track-name>/requirements.md`, Local-Wiki articles as needed.
**Outputs:** `3-TRANSFORMATIONS/Translations/<track-name>/termbase.md` — the prescriptive termbase, scoped to keywords that appear in the text being translated; plus updates to the consolidated bilingual glossary for any new derived renderings.
→ [`glossary-select/SKILL.md`](glossary-select/SKILL.md)

### `pali-keyword-extraction` **[exists]**
**Purpose:** Extract domain-specific English keywords from a translation file using TF-IDF (Pass 1 only). Produces a ranked keyword list — unigrams and compound phrases — for independent review or use as input to `pali-biterm-extraction`.
**Inputs:** An English translation markdown file with Obsidian block IDs; an output path.
**Outputs:** A ranked keyword list at the output path, one keyword per line with TF-IDF score.
→ [`pali-keyword-extraction/SKILL.md`](pali-keyword-extraction/SKILL.md)

### `pali-biterm-extraction` **[exists]**
**Purpose:** For a block-aligned Pāli source file and an English translation file, extract every attested English rendering for each Pāli token's morphological family. Writes one file per term to `bilingual-glossary/` in the benchmark format: senses, per-sense English frequency tables, and declensions with example phrases. The script (Pass 2) produces a flat draft; Claude applies semantic grouping to produce the final file.
**Inputs:** A Pāli source markdown file and a matching English translation file (both with Obsidian block IDs); a focus term (root form); output directory (`bilingual-glossary/`).
**Outputs:** `bilingual-glossary/{term}-draft.md` (flat draft from script) → `bilingual-glossary/{term}.md` (final benchmark format after Claude's semantic grouping). Also supports YAML mode (`--format yaml`) for the `glossary-combine` pipeline.
→ [`pali-biterm-extraction/SKILL.md`](pali-biterm-extraction/SKILL.md)

### `glossary-contested` **[exists]**
**Purpose:** Scan the consolidated bilingual glossary and identify terms with genuine rendering variation, ranked by contestedness score.
**Inputs:** Consolidated bilingual glossary at `2-RAILS/Bilingual-Glossaries/<pair>.md`.
**Outputs:** Ranked contested-terms report at `0-INBOX/<pair>-contested.md` (moved to `2-RAILS/Bilingual-Glossaries/<pair>-contested.md` after review).
→ [`glossary-contested/SKILL.md`](glossary-contested/SKILL.md)

---

## Translation requirements skills

### `requirements-author` **[planned]**
**Purpose:** Author or audit a track's `requirements.md` so it contains everything the `translate-section` skill needs to behave consistently across the whole text.
**Inputs:** The track folder `3-TRANSFORMATIONS/Translations/<track-name>/`; the per-track termbase (if it exists yet); samples of any prior translation in the same target language.
**Outputs:** A complete `3-TRANSFORMATIONS/Translations/<track-name>/requirements.md`, written in the target language, covering: target audience and register; bilingual glossary reference path; preferred rendering for structurally significant terms; style constraints (sentence length, paragraph length, treatment of verse vs. prose, list handling, transliteration vs. translation policy, footnote vs. inline glossing); cultural-adaptation rules; and the source-rail dependencies the translator must consult.
**Audit mode:** Given an existing `requirements.md`, report which of the above sections are missing or under-specified before any translation begins.
→ `requirements-author/SKILL.md` *(to be written)*

---

## Translation skills

### `translate-section` **[planned]**
**Purpose:** Translate a small batch of TOC nodes into the target language.
**Inputs:**
- `3-TRANSFORMATIONS/Translations/<track-name>/requirements.md`
- `3-TRANSFORMATIONS/Translations/<track-name>/termbase.md`
- `2-RAILS/Sections/<node-id>.md` for each node in the batch
- `2-RAILS/Verses/<verse-id>.md` for each verse in the batch
- `2-RAILS/Local-Wiki/<term>.md` for any term in the batch not adequately covered by the bilingual glossary
**Outputs:** Updated translation file(s) in `3-TRANSFORMATIONS/Translations/<track-name>/`. The frontmatter of each translation file lists the rail files it was generated from.
**Rules:** Translate small batches only — one or a few TOC nodes at a time. Every keyword rendering must match the per-track termbase. Introduce no new rendering without first adding it to the per-track termbase and feeding it back into the consolidated bilingual glossary under `2-RAILS/Bilingual-Glossaries/`. Translate from the disambiguated Pali in the verse-context file, not from the raw root text.
→ `translate-section/SKILL.md` *(to be written)*

### `zero-shot-translate` **[exists]**
**Purpose:** Translate Pāḷi source blocks to the target language using the track’s bilingual glossary as a hard termbase constraint.
**Inputs:** Track folder (with `bilingual glossary.md` and `requirements.md`), Pāḷi source file, block range.
**Outputs:** Translation file at `3-TRANSFORMATIONS/Translations/<track>/` with matching block IDs.
→ [`zero-shot-translate/SKILL.md`](zero-shot-translate/SKILL.md)

---

## Translation QA skills

### `translation-qa` **[planned]**
**Purpose:** Review a translated section against the MQM translation error taxonomy, the track requirements, and the source rails.
**Inputs:**
- The translated section(s) in `3-TRANSFORMATIONS/Translations/<track-name>/`
- `3-TRANSFORMATIONS/Translations/<track-name>/requirements.md`
- `3-TRANSFORMATIONS/Translations/<track-name>/termbase.md`
- Relevant `2-RAILS/Sections/`, `2-RAILS/Verses/`, and `2-RAILS/Local-Wiki/` files
**Outputs:** Appended entries in `3-TRANSFORMATIONS/Translations/<track-name>/qa-report.md`. Each entry records: the segment, MQM error category (accuracy, fluency, terminology, style, locale convention, …), severity (critical / major / minor), and a suggested correction.
**Completion criterion:** A section is marked `status: complete` only when no critical or major MQM errors remain open in the QA report.
→ `translation-qa/SKILL.md` *(to be written)*

### `style-consistency-check` **[planned]**
**Purpose:** Catch the third failure mode — style drift over long texts — that section-by-section QA tends to miss. Scans across many already-translated sections of one track and flags creeping changes in register, sentence length, verse formatting, list handling, term gloss style, and similar style-level patterns.
**Inputs:** All translated files in `3-TRANSFORMATIONS/Translations/<track-name>/`; `requirements.md`; the per-track termbase.
**Outputs:** A style-drift section appended to `qa-report.md`, with span references back to the offending passages.
→ `style-consistency-check/SKILL.md` *(to be written)*

---

## Plan skills

Skills that compose calendar-driven study/practice arcs under `3-TRANSFORMATIONS/Plans/`. They draw from the same rails as the translation skills, but produce per-session day files rather than continuous translations.

### `daily-tipitaka-day` **[exists]**
**Purpose:** Compose one or more Daily Tipitaka per-language day files end-to-end — gather assets first, halt on missing assets, then write the seven-step day file.
**Inputs:** A day-range (e.g. `7-11`) and a language-tag (e.g. `en`); the plan's `schedule.md`, `requirements.md`, and day template; the relevant book under `1-SOURCES/Text/`; the matching `2-RAILS/Sections/<book>-summaries.md` and `<book>-practice.md`.
**Outputs:** Per-day assets scratchpads at `0-INBOX/daily-tipitaka/day-NNN-assets.md` and per-day published files at `3-TRANSFORMATIONS/Plans/Daily-Tipitaka/<lang>/days/day-NNN.md`.
→ [`daily-tipitaka-day/SKILL.md`](daily-tipitaka-day/SKILL.md)

---

## Utility skills

### `source-property-extractor` **[exists]**
Extracts structured metadata (author, date, edition, language, publisher) from a source file and writes it to the frontmatter.
→ [`source-property-extractor/SKILL.md`](source-property-extractor/SKILL.md)

### `property-creator` **[exists]**
Creates or updates Obsidian frontmatter properties on a file.
→ [`property-creator/SKILL.md`](property-creator/SKILL.md)

### `structural-outline-ingest` **[exists]**
Ingests a structural outline (TOC) into a source or rails file.
→ [`structural-outline-ingest/SKILL.md`](structural-outline-ingest/SKILL.md)

---

## System skills

These skills operate on the vault's own structure — creating new skills, maintaining registrations, and auditing integrity. They are meta-level tools for contributors, not pipeline steps.

### `create-skill` **[exists]**
**Purpose:** Scaffold a new skill completely and correctly in a single pass — creates the SKILL.md, registers it in SKILLS-CATALOG.md, creates the slash command file, and optionally adds it to the CLAUDE.md quick-reference table.
**Inputs:** Skill name, purpose sentence, catalog section, inputs/outputs description, and whether it belongs in the CLAUDE.md §12 table.
**Outputs:** `4-SYSTEM/Skills/<skill-name>/SKILL.md`, a new catalog entry, `.claude/commands/<skill-name>.md`, and optionally a new §12 table row in `4-SYSTEM/CLAUDE.md`.
→ [`create-skill/SKILL.md`](create-skill/SKILL.md)
