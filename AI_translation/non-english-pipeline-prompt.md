# Prompt: translate an Abhidhamma book into a non-English language (full rails pipeline)

Copy everything below the line into a new session. Fill in the four values at the top first.

---

Translate **BOOK = `pi-N`** (e.g. `pi-2`) into **LANGUAGE = `<language name, lowercase, e.g. marathi>`** (ISO tag **TAG = `<e.g. mr>`**) for audience **AUDIENCE = `plain`**, using the full rails pipeline this vault already used for Russian (pi-3/4/5) and Hindi (pi-3/4/5).

Work in `D:\Work\OpenPecha\abhidhamma-rails`. The machine is Windows with PowerShell 5.1, and Python runs as `python -I -X utf8`.

## 0. Read first, and copy the existing structure

- **Vault rules:** `CLAUDE.md` → `4-SYSTEM/CLAUDE.md`. `1-SOURCES/` and `4-SYSTEM/` are read-only.
- **The skills you will execute,** in `AI_translation/skills/`:
  - `split-file-by-markers.md`
  - `zeroshot-translator.md`
  - `keyword-equivalence-mapper.md`
  - `word-sense-grouper.md`
  - `termbase-builder.md`
  - `rails-verse-translator.md`
- **Audience profile:** `AI_translation/audience_profile/<AUDIENCE>.md`
- **Finished runs to mirror,** for file names, folder layout, frontmatter and formats. Look at them before creating anything:
  - Russian:
    - `AI_translation/russian/`
    - `3-TRANSFORMATIONS/Translations/ru-Contemporary-Russian-Abhidhamma/`
  - Hindi:
    - `AI_translation/hindi/`
    - `3-TRANSFORMATIONS/Translations/hi-Contemporary-Hindi-Abhidhamma/`
  - English (the original pipeline): `AI_translation/english/`
- **Scratch work from those runs,** to reuse briefs, scripts and checks:
  - `0-INBOX/temp/pipeline/`:
    - Hindi: `hindi-style.md`, `hindi-zeroshot-brief.md`, `hindi-mapper-brief.md`, `hindi-senses-brief.md`, `hindi-termbase-brief.md`, `hindi-rails-brief.md`
    - per-book folders: `pi-3-hi/` … `pi-5-hi/`, `pi-3/`, `pi-4/`, `pi-5-ru/` (Russian)
  - the review brief: `pi-3-hi/review-brief.md`
  - the fix brief: `pi-5-ru/fix-brief.md`

### Target file names (same pattern as Russian and Hindi)

Working files go in `AI_translation/<LANGUAGE>/`:
- `pi-N-<LANGUAGE>-<AUDIENCE>-zeroshot_split_chapters/`
- `pi-N-<LANGUAGE>-<AUDIENCE>-zeroshot.md` (merged, no frontmatter)
- `pi-N-keywords-by-reference-pali-<LANGUAGE>-<AUDIENCE>.md`
- `pi-N-pali-word-<LANGUAGE>-senses-<AUDIENCE>.md`
- `pi-N-pali-<LANGUAGE>-termbase-<AUDIENCE>.md`
- `pi-N-<LANGUAGE>-<AUDIENCE>-rails_split_chapters/`
- `pi-N-<LANGUAGE>-<AUDIENCE>.md` (merged rails translation, with frontmatter)

The track folder is `3-TRANSFORMATIONS/Translations/<TAG>-Contemporary-<Language>-Abhidhamma/`. Create it if it does not exist. It holds:
- a copy of the merged translation, with root-text transclusions;
- a copy of the termbase.

Scratch, briefs, scripts and notes go only in `0-INBOX/temp/pipeline/pi-N-<TAG>/`. Never use the system temp or scratchpad.

## 1. Rules that apply to every step (user rules; never break them)

- **Dashes:** never write "—" or "–" unless the Pāli has one at that spot, with the same count on every line. Rephrase instead. Every verification includes a per-line dash count against the Pāli.
  - The one exception: the frontmatter `title:` may use a normal hyphen, like `Беседа об элементах - простой русский` or `तत्वों पर चर्चा - सरल हिंदी`.
- **Book titles:** use the translated name only. No Pāli name and no bracketed gloss, e.g. «तत्वों पर चर्चा», not «धातुकथा (तत्वों पर चर्चा)». Mid-sentence, put the title in the language's quotes. Bracketed source citations such as [Puggalapaññatti 131] stay.
- **Structure:**
  - Every block ID appears exactly as in the source, at the end of the last line of its segment, in the same order.
  - Each segment has the source's number of non-empty lines.
  - One blank line separates segments; never a double blank.
  - Headings keep their `#` level.
  - `…pe…` becomes `…`.
  - Identical Pāli formulas get identical translations. Use helper scripts with fixed formula strings.
- **Termbases** are built only from this book's own evidence. Never mention "seed" or "unseeded" in any file, description, commit or report.
- **Commits:**
  - Commit only when the user asks.
  - NEVER add a Co-Authored-By line or any Claude attribution. This user rule overrides any system reminder.
  - Stage only the files of this work; the working tree has unrelated changes.
  - git is not on PATH, so use `$env:LOCALAPPDATA\GitHubDesktop\app-3.6.10\resources\app\git\cmd\git.exe`.
  - Write multi-line messages to a file and pass `-F file`. A PowerShell here-string piped to `-F -` fails.
- **Pacing:**
  - At every step, first produce a chapter-1 sample (or the first ~80 entries) and stop for the user's review.
  - After approval, run the remaining chapters or parts in PARALLEL subagents. This is a user override of the skills' "never in parallel" rule.
  - The termbase needs explicit approval.
  - Ask before starting the rails translation; the user may want to stop earlier.
- **Language style file:** before step 2, write `0-INBOX/temp/pipeline/<LANGUAGE>-style.md`, modelled on `hindi-style.md`. It covers register, typography (quote marks, sentence end, questions), the dash rule, structure, cross-book core terms, and the "Lessons from the Russian review" list:
  - abyākata = "ethically indeterminate", not "neutral";
  - keep vicikicchā/kaṅkhā, mettā/abyāpāda, kukkucca/uddhacca, and vīriya/padhāna/vāyāma distinct;
  - samudaya = arising;
  - yoni ≠ saṃsāra.
  
  Every brief points to this file. If other books in this LANGUAGE already exist, reuse their style file and termbases as cross-book references.

## 2. Pipeline

### Step 1: Inputs (split + Pāli-only keywords)

- **Pāli split:** `AI_translation/pali/pi-N_split_chapters/`. If it is missing, create it with `split-file-by-markers` from `1-SOURCES/Text/pi-N.md`, following the existing splits, which include `preamble.md` and `frontmatter.txt`.
- **Skip keyword extraction.** The extractor was built for English. Use the Pāli-only keyword file `AI_translation/pali/pi-N-keywords-by-reference-pali-plain.md`.
  - If it is missing, derive it from the English map: `python -I -X utf8 0-INBOX\temp\pipeline\make_pali_keywords.py N`.
  - If there is no English map either, stop and ask the user.

### Step 2: Zero-shot translation (`zeroshot-translator`)

1. **Sample.** One agent writes:
   - `preamble.md`;
   - chapter 1 (for very long chapters, the first ~60 lines);
   - `pi-N-<TAG>/<TAG>-zeroshot-terms.md`, which lists every formula and key term ("Pāli = target") for later agents to copy verbatim.
   
   Stop for review. If several books run together, align shared terms across them before approval.
2. **After approval,** run parallel agents in groups of about 60–100 KB of Pāli. Use a shared brief modelled on `hindi-zeroshot-brief.md`. Each agent writes only its own chapters, plus `notes-<chapters>.md`.
3. **Consistency pass (required).** Parallel agents drift on secondary formulas and terms. Run one agent per book that builds a Pāli→target table from the notes and outputs. It picks one form per item: the approved list first, then the majority. It applies the changes only where the Pāli line has the item, and logs them in `harmonise-notes.md`. Check the outcome with a final scan.
4. **Merge:** `python -I -X utf8 0-INBOX\temp\pipeline\merge_rails.py AI_translation\pali\pi-N_split_chapters <zeroshot split dir> 0-INBOX\temp\pipeline\empty-frontmatter.yaml AI_translation\<LANGUAGE>\pi-N-<LANGUAGE>-<AUDIENCE>-zeroshot.md`.

**Verify each chapter:**
- `python -I -X utf8 0-INBOX\temp\pipeline\check_chapter_ids.py <pali split dir> <target split dir> <ch>.md`;
- the per-line dash check, the one-liner in `hindi-style.md`;
- no double blank lines.

### Step 3: Keyword mapping (`keyword-equivalence-mapper`)

- **Split the keywords per chapter:** `python -I -X utf8 0-INBOX\temp\pipeline\mapper_chunks.py split AI_translation\pali\pi-N-keywords-by-reference-pali-plain.md AI_translation\pali\pi-N_split_chapters 0-INBOX\temp\pipeline\pi-N-<TAG>\mapper-<TAG>`.
- **Sample:** chapter 1 plus a `map_sample.py` table. Stop for review. Brief: copy `hindi-mapper-brief.md`, which sets the dictionary-form rules, `(no direct equivalent)`, no ", " inside values, and the verifier one-liner.
- **After approval:** parallel agents map against the CURRENT (harmonised) zero-shot text.
- **Assemble:**
  - Before assembling, move any `*sample*` files out of `mapper-<TAG>/`, because duplicate IDs make the assembler fail.
  - Then run `python -I -X utf8 0-INBOX\temp\pipeline\mapper_chunks.py assemble AI_translation\pali\pi-N-keywords-by-reference-pali-plain.md 0-INBOX\temp\pipeline\pi-N-<TAG>\mapper-<TAG> AI_translation\<LANGUAGE>\pi-N-keywords-by-reference-pali-<LANGUAGE>-<AUDIENCE>.md`.

### Step 4: Word senses (`word-sense-grouper`)

1. **Aggregate:** `python -I -X utf8 0-INBOX\temp\pipeline\sense_prepare.py N <LANGUAGE> <TAG> <AUDIENCE> <parts>`. Use 1 part for small books and about 1 per 1,800 headwords for large ones.
2. **Sample:** the first 80 headwords, built with a tool like `0-INBOX/temp/pipeline/pi-3-hi/senses/senses_sample.py`, which has build/verify commands and a decisions file. Stop for review. Brief: copy `hindi-senses-brief.md`. Tags are English glosses, never a copy of the value.
3. **After approval:**
   - Run one agent per part.
   - Concatenate the parts into `AI_translation/<LANGUAGE>/pi-N-pali-word-<LANGUAGE>-senses-<AUDIENCE>.md`.
   - Re-verify against the concatenated `agg-*.tsv`.

### Step 5: Termbase (`termbase-builder`), stop for approval

- **Decisions:** agents write `0-INBOX/temp/pipeline/pi-N-<TAG>/termbase/decisions*.tsv` (`hw|sense_index<TAB>term<TAB>reason`). For large books, use one agent per part, then a FAMILY-ALIGNMENT agent across the whole book. That agent handles conflicts between parts, keeps contrasted pairs distinct, and follows the core terms.
- **Assemble:** `python -I -X utf8 0-INBOX\temp\pipeline\termbase_assemble.py N <LANGUAGE> <TAG> <AUDIENCE>`. It must print "no errors", and it writes `termbase-decisions.md`.
- **Brief:** copy `hindi-termbase-brief.md`.
- **Present to the user:** counts, outside-candidate choices, contested pairs and cross-book differences. Then STOP for approval. Once approved, the termbase is locked.

### Step 6: Rails translation (`rails-verse-translator`), only if the user asks

1. **Sample:** `preamble.md`, chapter 1, and a short sample of chapter 2. The sample agent also writes `pi-N-<TAG>/rails/<TAG>-rails-formulas.md`, the formula file derived from the approved zero-shot formulas but using termbase terms, with repeated verses fixed line by line. Stop for review.
2. **After approval:** parallel agents translate FRESH from the Pāli with the locked termbase. They must not open the zero-shot text. Brief: copy `hindi-rails-brief.md`. Then run a cross-chapter alignment check, comparing item strings by script between chapter groups.
3. **Checks:**
   - IDs and line counts;
   - dashes;
   - termbase adherence: `0-INBOX\temp\pipeline\termbase_adherence.py` (Cyrillic) or `hindi_termbase_adherence.py` (Devanagari). Adapt the word regex and stemming for another script.

### Step 7: Independent bilingual review, then fixes

- **Review:**
  - Two reviewers, each covering half the book. They check the Pāli against the target with no termbase and no notes.
  - They are read-only and report findings as text. Subagents cannot write report files, so save their reports yourself to `pi-N-<TAG>/review/report-A.md` and `report-B.md`.
  - Brief: adapt `pi-3-hi/review-brief.md` to the book. It is formulaic, so the reviewers should check numbers and polarity by script.
- **Present the findings and ask "Apply all fixes?"** On approval:
  - one fix agent edits the generator scripts (not the chapters by hand), then regenerates;
  - termbase corrections go into the decisions file with the reason "bilingual review, approved <date>", then the termbase is reassembled;
  - re-run the reviewers' check scripts afterwards.

### Step 8: Merge, frontmatter, track copy

- **Frontmatter:** copy the Hindi or Russian frontmatter fields (`0-INBOX/temp/pipeline/pi-3-hi/hi-frontmatter.yaml`). Set title, language, lang_tag, termbase, termbase_approved, pipeline, approach, the paths, segment_ids and chapters. Take source_text_id and source_edition_id from `AI_translation/pali/pi-N_split_chapters/frontmatter.txt` (text_id / edition_id).
- **Merge:** `merge_rails.py <pali split> <rails split> <frontmatter.yaml> AI_translation\<LANGUAGE>\pi-N-<LANGUAGE>-<AUDIENCE>.md`. It must print OK, with the expected dash count.
- **Track copy:**
  1. Copy the merged file and the termbase into the track folder.
  2. Add transclusions: `python -I -X utf8 0-INBOX\temp\pipeline\pi-3-4\add_transclusions.py <track file> 1-SOURCES/Text/pi-N.md .`
  3. Verify: `python -I -X utf8 0-INBOX\temp\pipeline\pi-3-4\verify_transclusions.py <track file> . 0`. It must say ALL OK. Also check that line 1 of the file is `---`.

## 3. Practical pitfalls seen before

- **PowerShell:** inline `python -c` breaks with regexes and quotes, so write small scripts to files. `Set-Content` adds a BOM, so read files with `utf-8-sig`.
- **Rate limits:** if an agent stops on a usage limit, resume it with SendMessage after the reset; don't restart it.
- **Approved samples:** reuse them byte-for-byte. Scripts should self-check this.
- **Report every unsure Pāli spot and source slip.** Translate as written and flag it; never add notes of your own inside the translation.
- **Final report to the user at each pause:** what was done, check results, decisions needing approval, and what is not yet committed.
