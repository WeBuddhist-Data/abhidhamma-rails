---
name: daily-tipitaka-day
description: Compose one or more Daily Tipitaka per-language day files (day-NNN.md) end-to-end. First gathers the Pāli source verses, the section summary, and the practice notes for each requested day into a per-day assets scratchpad in 0-INBOX/, stops if any asset is missing, then writes the seven-step day file using the plan template and per-language requirements. Use whenever Evan asks to create or fill in day-NNN files in any Daily Tipitaka language track (e.g. "draft days 12–17 in en").
---

# daily-tipitaka-day

This skill produces a **complete Daily Tipitaka day file** — frontmatter, the seven-step session, and the app notification — for one day at a time, in batches as requested. Without this skill, drafting a day file from scratch is slow and unreliable because the agent has to hunt for the right Pāli verses, the right section summary, and the right practice notes across three different files in `1-SOURCES/` and `2-RAILS/`. This skill makes that lookup deterministic: it writes a per-day **assets scratchpad** to `0-INBOX/daily-tipitaka/` first, halts if anything is missing, and only then composes the day file from those assets plus the template and the plan requirements.

**Why the day file's §4 and §6 are abbreviated (first verse + last verse only).** The WeBuddhist app pulls the full verse text for a day's range from its own verse library at render time. The day file's job is *not* to reproduce all the verses — it is to give the plan-importer enough to (a) confirm the range and (b) find the first and last verses in the app library so the right range can be selected. The full text of every verse in the range lives only in the **assets scratchpad** in `0-INBOX/`, because the scratchpad is what §1 and §5 are written from. The day file's §4 and §6 print only the *first* and *last* verses of the range, each with its verse number (and, in §6, its block ID). This is a hard constraint, not a stylistic preference — the app's daily-session screen is calibrated for ~5 minutes of reading, of which most of the time is the verses themselves, leaving little room for the orientation prose around them.

**A verse block can span several lines, and its block ID sits on the LAST one.** This is the single most common source of silently-wrong day files, so read it carefully. In `1-SOURCES/Text/pi-*.md`, one numbered verse often runs over several lines — the number appears only on the **first** line, and the `^<book>-<verse>` anchor only on the **last**. Verse `^2-15`, for example, is three lines:

```
15. Tattha katamā saññā atītā? … ayaṃ vuccati saññā atītā.
Tattha katamā saññā anāgatā? … ayaṃ vuccati saññā anāgatā.
Tattha katamā saññā paccuppannā? … ayaṃ vuccati saññā paccuppannā. ^2-15
```

If you locate a verse by grepping for its anchor and take *that line* as the verse, you get only the tail — here, "What is present perception?" — so the day file appears to start in the middle of a sentence, with the past- and future-perception clauses silently dropped. Some blocks are long: `^2-33` is thirteen lines, `^2-34` is ten. Truncation is invisible unless you test for it, which is why the completion checks below do so explicitly.

**To resolve a verse, find the line carrying its anchor, then walk backwards to the verse's true opening** — stop at a blank line, at a heading, or at the previous line that itself ends in an anchor. The line you stop *after* is the opening line, and it normally begins with the printed verse number. Every consumer follows this rule: the assets scratchpad's range must begin at the first verse's opening line, not at its anchor line, and the day file's §4/§6 entries must begin there too. The same applies to the translation file, which mirrors the source's line structure.

**Length discipline on §1 and §5.** The casual-Buddhist audience this plan serves is calibrated for ~5-minute sessions on a phone. §1 (Today's Chanting Guide) and §5 (Pāli Word of the Day) are the two prose sections that compete with the verses for that budget, so both are kept short. See Phase 2 step 3 and step 6 for the per-section caps. The plan's outcome statement — *"come away each day ready to do a little less harm, a little more good, and know your mind a little better than before"* — is the yardstick: every paragraph in §1 and §5 should be earning its place against that, not against academic completeness.

**Plain-English discipline on §1 and §5.** The audience is international, with English as a second or third language for a large share of readers. The audience profile sets the target at 8th-grade reading level — concretely, **Flesch-Kincaid grade ≤ 9** for both §1 and §5, with average sentence length ~12–15 words. This is not a stylistic preference; it is the floor below which the readership the plan was built for can actually use it. **Pāli technical terms are welcome and expected — but every Pāli term gets a short plain-English gloss on first use in the section.** What is *not* welcome: academic register ("canonical formula", "the text foregrounds"), figurative English idioms that don't translate ("step off the map", "lets the rubber meet the road"), internal-architecture references ("the practice rail describes…" — the reader doesn't know what a rail is and shouldn't have to), or chains of multisyllable English where a short word would do (*"meditative absorption" → "deep focus", "sensual pleasures" → "sense desires", "dissociated from knowledge" → "without wisdom"*). The Phase 2 completion check measures this; if §1 or §5 lands above grade 9, rewrite — don't just trim, simplify.

A correct output is a day file that (1) cites only `2-RAILS/` (never `1-SOURCES/` directly), (2) matches the section/verse range declared for that day in `<lang>/schedule.md`, (3) carries the *first* and *last* Pāli verses of the range with their block IDs preserved in §6 (not the whole range), (4) respects the §1 and §5 length caps, and (5) respects the template's character caps for the app notification (Title ≤ 40, Body ≤ 120, Button ≤ 15).

---

## Inputs

The skill needs both inputs before it starts. If either is missing, ask the human contributor — do not guess.

| Input | Description | Example |
|---|---|---|
| `day-range` | One or more day numbers in the plan. Accepts `N`, `N-M` (inclusive range), or comma list `N,M,P`. | `7-11`, `12`, `15,17,19` |
| `language-tag` | The target language track. Must already exist as a folder under `3-TRANSFORMATIONS/Plans/Daily-Tipitaka/`. | `en`, `pi`, `bo`, `zh`, `hi` |

Required files the skill reads (must already exist — if missing, stop and report):

- `3-TRANSFORMATIONS/Plans/Daily-Tipitaka/<lang>/schedule.md` — maps each day to its section name and verse range.
- `3-TRANSFORMATIONS/Plans/Daily-Tipitaka/<lang>/requirements.md` — the per-language style contract.
- `3-TRANSFORMATIONS/Plans/Daily-Tipitaka/<lang>/days/_template/day-template.md` — the day file template.
- The Pāli source text for the book the day's verses come from (e.g. `1-SOURCES/Text/pi-1.md` for Book I, `pi-2.md` for Book II, `pi-3.md` for Book III). Schedule.md identifies which book.
- `2-RAILS/Sections/<book>-summaries.md` — the per-TOC-node summaries (e.g. `pi-1-summaries.md`).
- `2-RAILS/Sections/<book>-practice.md` — the per-TOC-node practice notes (e.g. `pi-1-practice.md`).

## Output

Two files per day in the range:

1. **Assets scratchpad** — `0-INBOX/daily-tipitaka/day-NNN-assets.md` (per-day; overwrite if it exists)
2. **Day file** — `3-TRANSFORMATIONS/Plans/Daily-Tipitaka/<lang>/days/day-NNN.md` (overwrite only if the existing file is still in unfilled template state — see Rules §3)

`NNN` is the three-digit zero-padded day number (e.g. `day-007`, `day-150`).

---

## Output file format

### Assets scratchpad (`0-INBOX/daily-tipitaka/day-NNN-assets.md`)

This is the working file the skill writes during Phase 1 and consumes during Phase 2. It is the single source of truth for what the day file will contain — if it's wrong, fix it here before generating the day file.

```markdown
---
day: <N>
language: <lang>
plan: <plan-number-from-schedule>
section: <section-name-from-schedule, e.g. "1. Cittuppādakaṇḍaṃ">
verses: <verse-range-from-schedule, e.g. "1–26">
book_source: <full path, e.g. 1-SOURCES/Text/pi-1.md>
summary_rail: <full path, e.g. 2-RAILS/Sections/pi-1-summaries.md>
practice_rail: <full path, e.g. 2-RAILS/Sections/pi-1-practice.md>
subsections:
  - <subsection heading text, e.g. "Padabhājanī">
  # If the day's verse range straddles two or more subsections, list each one in source order.
  # If part of the range falls outside any deeper subsection (e.g. between two ##### blocks), record the parent #### heading text instead and add a note in the relevant content section.
status: assets-gathered
---

# Day <N> — Assets

## Schedule entry

| Day | Date | Section | Verses |
|---|---|---|---|
| day-NNN | <date from schedule> | <section> | <verse-range> |

## Pāli source verses

<Verbatim copy of the Pāli verses from <book_source>, including their block IDs (^1-N). Preserve every heading at any level (`###`, `####`, `#####`, `######`) that falls inside the verse range or sits immediately above the first verse — chapter and section headings carry orientation context, do not strip them. Do NOT paraphrase, translate, or reformat.>

## Section summary (from `<summary_rail>`)

<Verbatim copy of the relevant section-summary block, including its TOC anchor (^toc-N-N-N) and the commentary back-citations beneath it.>

## Practice notes (from `<practice_rail>`)

<Verbatim copy of the relevant practice block, including its TOC anchor and back-citations.>

## English translation (if a translation file exists)

<If `3-TRANSFORMATIONS/Translations/<lang>-…/<book>-…-ai.md` exists for the target language, copy the verses in the day's range here verbatim. Otherwise note "No translation file found — Reading for Meaning will be drafted from the section summary + practice + commentary back-citations." This is the only acceptable source of English prose for §4 of the day file; the skill does not translate from raw Pāli on its own.>
```

### Day file (`3-TRANSFORMATIONS/Plans/Daily-Tipitaka/<lang>/days/day-NNN.md`)

```markdown
---
day: <N>
language: <lang>
plan: <plan-number>
passage: "<Section-name>, <Subsection chain if any> — vv. <range>"
status: draft
sources:
  - 2-RAILS/Sections/<book>-summaries.md
  - 2-RAILS/Sections/<book>-practice.md
---

# Day <N> — <Thematic title drawn from the section summary>

## 1. Today's Chanting Guide

<**Hard cap: ~2 short paragraphs (max ~180 words total) plus the closing question.** Plain language. One sentence that locates the passage in the larger map (drawn from the section summary), then one short paragraph naming what the day's verses actually walk through and why it matters for a casual practitioner. Skip exhaustive structural commentary — that belongs in the rails, not here. Closes with: "Today's question to carry into the chant: *…*">

## 2. Homage

![[../../assets/liturgy/vandana.md]]

## 3. Intention

![[../../assets/liturgy/intention.md]]

## 4. Reading for Meaning

**Verses <A>–<B>.** *(Full text rendered in the WeBuddhist app from the verse library; the first and last verses of the range are printed below so the plan-importer can find the right entries.)*

**v. <A>.** <First verse of the range in the target language, taken verbatim from the assets file's "English translation" section, **beginning at the verse's opening line**. If the verse spans several lines, print its opening line, then ` *(…)* `, then its closing line — see "multi-line verses" below.>

…

**v. <B>.** <Last verse of the range in the target language, same rule.>

*Source: [[2-RAILS/Sections/<book>-summaries.md]], [[2-RAILS/Sections/<book>-practice.md]]*

## 5. Pāli Word of the Day

### <TERM> — <Gloss>

**Pronunciation:** <syllabified guide, one line>

**In today's passage:** <2–4 sentences: what the word does in this specific day's verses, drawn from the practice rail and section summary.>

**Why it matters:** <2–4 sentences: how the word changes how the practitioner sees their own mind, drawn from the practice rail. End on something a casual reader can carry into the day — less harm, more good, knowing their mind a little better.>

**Hard cap on §5: ~140 words total across pronunciation + the two paragraphs.** Do not add a separate "Literal sense" or "Etymology" paragraph — fold any literal-sense note into "In today's passage" if it earns its place.

## 6. Chanting in Pāli

**Verses <A>–<B>.** *(Full Pāli text rendered in the WeBuddhist app from the verse library; the first and last verses of the range are printed below — with their block IDs — so the plan-importer can find the right entries.)*

<If the verse range opens inside a named subsection of the source text, name it on one line before the first verse — e.g. `Section: Suññatavāro → Rūpāvacarakusalaṃ → Catukkanayo`. If the range straddles one or more new headings, name those too. Do **not** print full heading blocks; the plan-importer needs orientation, not the full TOC.>

**<A>.** <First Pāli verse of the range, verbatim from the assets file, **beginning at the verse's opening line**, formatted for chanting (clause-level line breaks, closing formula in bold). Block ID preserved at the end: `^<book>-<A>`.>

…

**<B>.** <Last Pāli verse of the range, same rule. Block ID preserved at the end: `^<book>-<B>`.>

### Multi-line verses in §4 and §6

A verse that spans several lines is printed as **opening line + ` *(…)* ` + closing line**, on one paragraph, with the block ID last (§6). For example:

```
**33.** Tattha katamo rūpakkhandho? Ekavidhena rūpakkhandho – … Evaṃ ekavidhena rūpakkhandho. *(…)* Ayaṃ vuccati rūpakkhandho. ^2-33
```

Both ends are needed, for two different reasons. The **opening** line is the verse's real beginning — without it the entry reads as a fragment. The **closing** line is what makes the entry identifiable: in the Abhidhamma's repeating formulas, several consecutive verses open identically (`^2-40`, `^2-41` and `^2-57` all begin "Ekavidhena vedanākkhandho – phassasampayutto."), so an opening-only entry can leave a day's first and last verses looking like the same verse. The closing line also carries the anchor.

Do **not** print the intervening lines: `*(…)*` marks their omission, and the app renders the full text from its own verse library. Keep `*(…)*` distinct from the standalone `…` line that separates the range's first verse from its last — one marks elision *within* a verse, the other elision *between* verses.

## 7. Aspiration

![[../../assets/liturgy/aspiration.md]]

## 8. App Notification

**Title:** <≤ 40 chars, e.g. "Day N — <Thematic title>">
**Body:** <≤ 120 chars, one-sentence hook>
**Button:** <optional, ≤ 15 chars, e.g. "Begin">
```

---

## Rules

1. **Phase order is fixed: assets first, day file second.** Never write the day file before its assets scratchpad exists and is complete. The assets scratchpad is the single source of truth for what goes into the day file.
2. **Stop on missing assets — do not invent content.** Halt the entire batch and report the gap to the human contributor if any of the following is true for any day in the range. "Missing" covers both shapes:
   - **Shape A — not found at all.** The Pāli source for a verse in the range cannot be located by block ID; or the source text file itself doesn't exist; or the summary/practice rail file doesn't exist; or no heading matching the day's subsection text appears in the rail.
   - **Shape B — found but empty.** The heading exists in the rail but the content beneath it is empty, is only a TOC back-link, or contains scaffold-only markers (e.g. `[[#^toc-…|↑↑↑]]` with no narrative paragraphs underneath).
   In both shapes, do not write a partial assets file and do not move on to the next day in the batch. Report which day, which asset, and which shape so the human contributor can fix the rail or the schedule.
3. **Do not overwrite a filled day file.** If `<lang>/days/day-NNN.md` already exists and contains anything beyond the unfilled template, stop and ask. "Unfilled template" means the file matches `day-template.md` line-for-line except for the frontmatter `day:` and `language:` values.
4. **Citation chain stays in 2-RAILS/.** The day file's `sources:` frontmatter and §4 source line cite only `2-RAILS/` paths. Never cite `1-SOURCES/` from the day file. The assets scratchpad may quote `1-SOURCES/` verbatim because it lives in `0-INBOX/` and is not cited from anywhere downstream.
5. **Day file's §4 and §6 print first verse + last verse only.** Not the whole range. The WeBuddhist app pulls the full verses from its own library at render time; the day file's job is to give the plan-importer enough to find the right range. The two verses are taken verbatim from the assets file (§6 from the Pāli source section, §4 from the English translation section). Both block IDs (`^<book>-<first>` and `^<book>-<last>`) are preserved at the end of their verses in §6.
6. **Every verse begins at its opening line, never at its anchor line.** A verse's `^<book>-<verse>` anchor sits on its *last* line; the printed verse number sits on its first. Resolve a verse by finding the anchor and walking backwards to the opening (stop at a blank line, a heading, or a previous anchor line). This applies to the assets scratchpad's range start and to both §4 and §6 entries. Multi-line verses render as `opening *(…)* closing` — see "Multi-line verses in §4 and §6" above. Never let an entry begin mid-verse; that is a silent corruption a reader notices immediately and a checker will not, unless it tests for it.
7. **Assets scratchpad always carries the full verse range.** This is the source of truth §1 and §5 are written from. The "first verse + last verse only" rule applies to the *day file*, never to the assets file.
8. **§1 length cap: ~180 words.** Two short paragraphs maximum, plus the closing question. If the draft exceeds the cap, cut — do not add a third paragraph and trim the first two.
9. **§5 length cap: ~140 words.** Pronunciation line + "In today's passage" (2–4 sentences) + "Why it matters" (2–4 sentences). No separate "Literal sense" paragraph; fold any literal-sense note into "In today's passage" if it pays its way.
10. **App notification character caps are hard limits.** Title ≤ 40 characters. Body ≤ 120 characters. Button (if present) ≤ 15 characters. Re-count after writing; if any cap is exceeded, tighten the wording before reporting completion.
11. **English Reading for Meaning content sources only from the assets file.** If the assets file has an "English translation" section drawn from a translation track file, §4 uses the first and last verses from it verbatim. If no translation file exists, §4 falls back to a *one-line* gloss of the first and last verses drawn from the section summary — never a fresh translation from Pāli.
12. **Frontmatter `sources:` lists every rail the day file draws from.** At minimum: the summaries rail and the practice rail. Add the verse-rails path if `2-RAILS/Verses/<ref>.md` files exist for any verse in the day's range.
13. **One assets file per day, never one per batch.** Even if days share a section, each day gets its own `0-INBOX/daily-tipitaka/day-NNN-assets.md`.
14. **Do not modify any file in `1-SOURCES/` or `2-RAILS/`.** This skill writes only to `0-INBOX/daily-tipitaka/`, `3-TRANSFORMATIONS/Plans/Daily-Tipitaka/<lang>/days/`, and `3-TRANSFORMATIONS/Plans/Daily-Tipitaka/<lang>/termbase.md` (append-only — see Rule 17).
15. **One translation track per language, across every book.** §4 for a given language always comes from the same track folder (for English, `3-TRANSFORMATIONS/Translations/en-Contemporary-English-Abhidhamma/`), with one output file per book — `en-dhammasangani-ai.md`, `en-vibhanga-ai.md`, and so on. A reader is on one continuous journey; a mid-journey change of track would change register and terminology and read as a break in voice. If a translation arrives labelled for some other audience (a filename or frontmatter field saying "plain", "simple", "accessible"), **do not create a new track for it** — check it against the existing track's `requirements.md` first. That contract already specifies a 7th–8th grade reading level and short sentences, so an "accessible" label usually describes what the track already is. Report the arrival and file it as the book's output in the existing track.
16. **When §1/§5 and §4 word the same concept differently, do not "fix" §1.** §1 and §5 use the locked rendering from `<lang>/termbase.md`; §4 is verbatim from the translation. If the translation diverges from a locked row, both sides are individually correct and the mismatch belongs to the *translation*. Record it (in the translation's `known_issues` frontmatter and as a note in the plan termbase) and leave §1/§5 alone — changing them would break consistency with every earlier day that used the locked term.
17. **Termbase is the cross-day consistency lock; treat it as authoritative and append-only.** Every Pāli technical term that appears in §1 or §5 of a day file is looked up against `<lang>/termbase.md` first (see Phase 2 step 3). Locked renderings are used verbatim; new terms grow the file via Phase 2 step 10. The skill **never** modifies or removes an existing locked row — only the human contributor does that, because every change cascades through every published day. The termbase is how today's day-012 stays consistent with tomorrow's day-013 and with day-007 written last week; without it, the same Pāli word ends up rendered three different ways across the journey.

---

## Starting a new book, or a new section of one

The plan crosses book boundaries (Book I ends at day-077; Book II runs 078–178; Book III 179–200), and it is normal for a requested batch to be the first to need a source, a rail, or a translation that nobody has produced yet. Check these **before** Phase 1, because a missing rail halts the batch under Rule 2 and it is better to discover that in one lookup than five.

| Prerequisite | Path | If missing |
|---|---|---|
| Root text | `1-SOURCES/Text/pi-<book>.md` | **Hard stop.** Only the human contributor can add canonical text. Report precisely which book and which verse range is unavailable. Do not translate or reconstruct verses from a commentary or an audio transcript. |
| Commentary | `1-SOURCES/Commentaries/pi-<book>-atthakatha.md` (also `-mulatiika`, `-anutiika`) | **Hard stop for rail-building.** The rails are grounded in commentary; without it, do not write rail prose. |
| Summaries rail | `2-RAILS/Sections/pi-<book>-summaries.md` | Buildable. Grounded in the aṭṭhakathā layer. |
| Practice rail | `2-RAILS/Sections/pi-<book>-practice.md` | Buildable — use the `practice-summaries` skill, which owns the format (Pāli prose weaving the three pillars, TOC block with `^toc-N` anchors, `[[#^toc-N\|↑↑↑]]` backlink under each heading, commentary back-citations beneath each entry). |
| Translation | the language's single track, one file per book (see Rule 15) | Not a hard stop — Rule 11 allows a one-line gloss fallback — but say so plainly in the run report, because a whole plan cannot ship on glosses. **Do not substitute draft-grade material to close the gap** — see below. |

**Never substitute draft-grade material for a missing asset.** A vault under active development accumulates intermediates that *look* like the thing you need: zeroshot or first-pass translations, scaffolded termbases, partial rails, audience profiles someone stubbed out. Reaching for one to unblock a batch is the wrong trade. A missing day is recoverable — someone builds it next week. A published day drafted from draft-grade material has to be found and redone, and if the draft used different terminology, it breaks voice for every reader who reaches that point in the journey.

Two tells that material is not ready:

- **The pipeline says so.** Check the producing skill's own description. A path documented as "no termbase", "first draft", "quick or exploratory", "fast path" is not the deliverable, however complete its coverage looks. Coverage is not grade.
- **It disagrees with what is already published.** Spot-check two or three recurring terms against the day files already shipped. If a candidate source says "aggregate of material form" where published days say "aggregate of form", adopting it changes vocabulary mid-journey.

When you find only draft-grade material, halt the batch and report precisely: which asset is missing, what draft exists, why it does not qualify, and what would have to be produced. That report is more useful than a day file that has to be withdrawn.

Two things to check when a rail already exists but is new to you:

- **Rails are often partial.** A rail file covering Book II may cover only its first vibhaṅga. Confirm the day's specific subsections resolve, not merely that the file exists — this is Rule 2's "Shape B", a heading present with nothing under it.
- **Match the rail's own structure to the commentary's, not to the root text's.** Where the commentary treats several sibling nodes under one shared method, give them one combined entry rather than several stubs; a TOC entry whose body would be empty is worse than no entry. Every TOC line must resolve to a non-empty body, and every body heading must appear in the TOC.

Ground rail prose only in what the commentary actually says, and cite the specific anchors used (`[[1-SOURCES/Commentaries/pi-<book>-atthakatha.md#^<book>-N]]`). Rail prose written this way still needs a native Pāli reviewer before the days built on it are published — say so in the run report.

---

## Procedure

### Phase 0 — Resolve inputs

The goal of Phase 0 is to turn each requested day number into a concrete lookup plan: *which range of verses to fetch, from which source file, with which rail files alongside it.* Nothing is read from the source text yet — that's Phase 1.

1. Parse `day-range` into a sorted list of day numbers (e.g. `7-11` → `[7, 8, 9, 10, 11]`).
2. Confirm `3-TRANSFORMATIONS/Plans/Daily-Tipitaka/<language-tag>/` exists. If not, stop and report.
3. **Get the verse range for each day from `<lang>/schedule.md`.** This is the schedule's primary job — it owns the day → verse-range mapping. Open `<lang>/schedule.md`, find the row for each requested day in the "Day-by-Day Calendar" tables, and record from that row: the date, the plan number (from the surrounding `### Plan N — Days A–B …` heading), the section name, and the verse range (the rightmost column, e.g. `1–26`). If a day is not in the schedule, stop and report.
4. **Resolve the verse range to a source file and a block-ID range.** Schedule rows are grouped by book: Plans 1–5 = Book I (Dhammasaṅgaṇī), Plans 6–23 = Book II (Vibhaṅga), Plans 24–27 = Book III (Dhātukathā). Map the book to its files:

   | Book | Source text | Summaries rail | Practice rail | Block-ID prefix |
   |---|---|---|---|---|
   | I | `1-SOURCES/Text/pi-1.md` | `2-RAILS/Sections/pi-1-summaries.md` | `2-RAILS/Sections/pi-1-practice.md` | `^1-` |
   | II | `1-SOURCES/Text/pi-2.md` | `2-RAILS/Sections/pi-2-summaries.md` | `2-RAILS/Sections/pi-2-practice.md` | `^2-` |
   | III | `1-SOURCES/Text/pi-3.md` | `2-RAILS/Sections/pi-3-summaries.md` | `2-RAILS/Sections/pi-3-practice.md` | `^3-` |

   The block IDs in these source files follow the Bible-style scheme `^<book>-<verse>` (declared in each file's `verse_id_format: book-verse` frontmatter — see `4-SYSTEM/Guidelines/abhidhamma-annex.md`). So for day-007 in Book I with range `1–26`, the lookup target is "every block from `^1-1` through `^1-26` in `1-SOURCES/Text/pi-1.md`."

The per-language `requirements.md` and `day-template.md` are not read in Phase 0 — they are read in Phase 2 at the moment of composition, so a Phase 1 halt doesn't waste a read.

#### Worked example — day-007

Phase 0 turns the schedule row into a lookup plan; Phase 1 executes the lookups. For day-007:

| What | Value | Where the skill finds it |
|---|---|---|
| Day number | 7 | Input |
| Schedule row | `\| day-007 \| 20 May (Thu) \| 1. Cittuppādakaṇḍaṃ \| 1–26 \|` | `<lang>/schedule.md` |
| Plan heading above the row | `### Plan 2 — Days 7–37 · Consciousness (20 May–19 Jun)` | `<lang>/schedule.md` |
| Book | Book I | Plans 1–5 = Book I (lookup table above) |
| Source text file | `1-SOURCES/Text/pi-1.md` | Lookup table above |
| Block-ID range | `^1-1` through `^1-26` (26 blocks) | Source text file |
| Subsection containing the range | `Padabhājanī` | `##### Padabhājanī ^1-1-1-1-0` heading just before `^1-1` in the source text |
| Summary rail | `2-RAILS/Sections/pi-1-summaries.md` | Lookup table above |
| Summary block to copy | `#### Padabhājanī` (lines 313–322) | Summary rail, matched by subsection text |
| Practice rail | `2-RAILS/Sections/pi-1-practice.md` | Lookup table above |
| Practice block to copy | `### Padabhājanī` (lines 110–120) | Practice rail, matched by subsection text |

### Phase 1 — Gather assets (one per day)

The goal of Phase 1 is to copy the actual verse text (and the matching summary + practice blocks) out of the source files and into a per-day scratchpad in `0-INBOX/`. By the end of Phase 1 every day's scratchpad is self-contained — Phase 2 never needs to touch `1-SOURCES/` or `2-RAILS/` again.

For each day `N` in the range:

1. Create the directory `0-INBOX/daily-tipitaka/` if it does not exist.
2. **Copy the Pāli verses for the day's range.** Open the source text file resolved in Phase 0 step 4. Find every block whose ID is in the day's range — i.e. for a range of `A–B` with block-ID prefix `^P-`, every block from `^P-A` to `^P-B` inclusive.

   **Get the start boundary right.** Locate the line carrying `^P-A`, then walk backwards to that verse's opening line (stop at a blank line, a heading, or a previous anchor line) and begin the copy there. Copying from the anchor line instead drops the earlier lines of a multi-line first verse, so the scratchpad — and every §1/§5 paragraph written from it — silently starts mid-verse. The end boundary needs no such care: the anchor sits on the verse's last line, so copying up to and including it captures the whole final verse.

   Copy each block verbatim, in source order, preserving **every heading at any level** (`###`, `####`, `#####`, `######` — any that appear inside the range or immediately above the first verse). Chapter (`###`) and section (`####`) headings carry orientation the chanter needs, even though they may seem "too high level"; do not strip them. Do not paraphrase, translate, or reformat.

   *Examples:*
   - *Day-007: scans `1-SOURCES/Text/pi-1.md` and copies the blocks ending in `^1-1`, `^1-2`, … `^1-26` — 26 blocks in total, including the `##### Padabhājanī ^1-1-1-1-0` heading just before `^1-1`.*
   - *Day-012 (verses 151–163): the range straddles the closing definition-blocks of the 5th–8th kāmāvacaramahākusalacittāni (following the `##### Suññatavāro` pattern established at v145) and opens the new `#### Rūpāvacarakusalaṃ` section with its `##### Catukkanayo` subsection — both the closing `Dutiyabhāṇavāro` marker at the end of v159 and the new `####` and `#####` headings between v159 and v160 must be preserved in the assets file.*
3. **Identify the subsection(s) the day's verse range falls inside.** The schedule.md row only names the top-level section (e.g. `1. Cittuppādakaṇḍaṃ`); the summary and practice rails are organized by *subsection* (Padabhājanī, Koṭṭhāsavāro, Suññatavāro). So the skill has to derive the subsection from the source text:

   1. While scanning the source text in step 2, track the most recent `##### …` heading above each verse. That heading is the subsection.
   2. Record the *text* of every distinct subsection heading the day's range falls under — usually one, occasionally two if the range straddles a boundary.
   3. The heading text alone is the lookup key for steps 4 and 5. Heading text is identical across the source text, the summary rail, and the practice rail — only the heading level and anchor format differ. (For day-007 the recorded subsection is `Padabhājanī`. For day-011 the range `121–150` straddles `Suññatavāro` (verses 121–145) and the un-headed Cittas 2–5 block (146–150) — record `Suññatavāro` and note in the assets file that 146–150 sit under the parent `Kāmāvacarakusalaṃ` rather than under any deeper subsection.)

4. **Copy the matching section summary from the summary rail.** Open the summaries rail resolved in Phase 0 step 4 (e.g. `2-RAILS/Sections/pi-1-summaries.md`). For each subsection text recorded in step 3, find a heading whose text matches — **match by text, not by heading level**. The heading level varies depending on how deeply the subsection sits in the TOC (in `pi-1-summaries.md`, chapter-level sections like `Kāmāvacarakusalaṃ` sit at `###` while deeper subsections like `Padabhājanī` sit at `####`). Copy: the heading line, the `[[#^toc-…|↑↑↑]]` back-link, the paragraph(s) beneath, and the commentary back-citation lines, up to (but not including) the **next heading at the same level or shallower**. If the same heading text appears more than once in the rail (rare — `Catasso paṭipadā (Rūpāvacara)` is the only known case in Book I), disambiguate by walking up the heading hierarchy to find the one whose parent heading matches the top-level section named in the schedule row.

   *Example: for day-007 the skill looks for `Padabhājanī` in `2-RAILS/Sections/pi-1-summaries.md`. It finds `#### Padabhājanī` at line 313 and copies down to just before the next `####` heading (`#### Koṭṭhāsavāro` at line 323).*
5. **Copy the matching practice notes from the practice rail.** Open the practice rail resolved in Phase 0 step 4 (e.g. `2-RAILS/Sections/pi-1-practice.md`). Same procedure as step 4 — **match by heading text, not by level**. The practice rail's heading levels run one level shallower than the summary rail (in `pi-1-practice.md`, chapter-level sections like `Kāmāvacarakusalaṃ` sit at `##` and deeper subsections like `Padabhājanī` sit at `###`), but the heading *text* is identical across both rails and the source text. Copy from the matching heading down to the next heading at the same level or shallower, or the next `---` divider if the rail uses dividers between entries.

   *Example: for day-007 the skill looks for `Padabhājanī` in `2-RAILS/Sections/pi-1-practice.md`. It finds `### Padabhājanī` at line 110 and copies down to just before `### Koṭṭhāsavāro` at line 121.*
6. **Copy the English translation if a translation track exists.** Check `3-TRANSFORMATIONS/Translations/<lang>-*/…-ai.md` (any `<lang>-*` track folder, e.g. `en-Contemporary-English-Abhidhamma/en-dhammasangani-ai.md`). If found, locate the same block-ID range as in step 2 and copy those verses. If not, record the note specified in the assets-file format above.
7. **If any of steps 2, 4, or 5 fail to find content, halt the entire batch.** Report which day's which asset is missing (verses, summary, or practice) and stop. Do not write a partial assets file and do not move on to the next day. A missing translation file (step 6) is not a halt condition — the assets file records the note and Phase 2 falls back to paraphrasing from the summary + practice.
8. Write `0-INBOX/daily-tipitaka/day-NNN-assets.md` using the format in the *Output file format* section above. Three-digit zero-pad the day number (e.g. day 7 → `day-007-assets.md`).

#### Phase 1 completion check (gate)

After Phase 1 has run for every day in the batch, verify *all* of the following before moving on. **If any check fails, stop. Do not start Phase 2.** Report the gap to the human contributor.

- [ ] One assets file exists at `0-INBOX/daily-tipitaka/day-NNN-assets.md` for every day in the requested range.
- [ ] Every assets file's frontmatter has a non-empty `section`, `verses`, `book_source`, `summary_rail`, and `practice_rail`.
- [ ] Every assets file's "Pāli source verses" section contains the same number of distinct block IDs as the day's verse range. (For range `A–B` with prefix `^P-`, the section should contain `B − A + 1` blocks from `^P-A` to `^P-B`.)
- [ ] **Every assets file's verse range begins at the first verse's opening line.** The first non-heading line of the "Pāli source verses" section should begin with the printed verse number `A.` — if it begins mid-sentence, the multi-line start boundary was mishandled (see Phase 1 step 2). Check the "English translation" section the same way.
- [ ] Every assets file's "Section summary" section is non-empty and contains the matching `#### <subsection-text>` heading from the summary rail.
- [ ] Every assets file's "Practice notes" section is non-empty and contains the matching `### <subsection-text>` heading from the practice rail.
- [ ] No day was silently skipped because of a missing asset — every halt was reported.

If every check passes, report the list of assets files written and proceed to Phase 2. If you want to inspect or edit the assets files before composition, this is the natural pause point.

### Phase 2 — Compose the day file (one per day)

Read these files once at the start of Phase 2 (before the per-day loop). They are the same for every day in the batch:

- `<lang>/days/_template/day-template.md` — the seven-step day file shape and the liturgy transclude lines.
- `<lang>/requirements.md` — the per-language plan style contract (register, format conventions, tone) that governs how §1, §4, §5, and §8 are written. **Important:** at the bottom of this file there is a pointer to a *translation track requirements file* — for English the pointer reads `../Translations/en-Contemporary-English-Abhidhamma/requirements.md`. Follow that pointer and read the translation track requirements too. It is the file that actually governs how Pāli renders into the target language (handling of repeated formulas, treatment of compound terms, sentence length, transliteration policy) — without it, §4 (Reading for Meaning) will drift in style from the rest of the translation track.
- `3-TRANSFORMATIONS/Translations/<lang>-<TrackName>/requirements.md` — the per-language translation track style contract, located via the pointer above. The track-name suffix varies (e.g. `en-Contemporary-English-Abhidhamma`); use the path the plan requirements names, do not guess. If the plan requirements does not point to a translation track requirements file for this language (e.g. for a newly-scaffolded language with no translation track yet), record that gap in the run report and proceed using the plan requirements alone — do not invent translation conventions.
- **`<lang>/termbase.md`** — the plan-level cross-day term lock. The growing single-source-of-truth for the English (or per-language) rendering of every recurring Abhidhamma Pāli term. **Without this file, every day's §1 and §5 risk drifting from the §4 rendering and from previous days' renderings.** The skill MUST consult it before composing any prose section (§1, §5) and MUST follow the locked rendering for every term it lists. See Phase 2 step 3 below for the lookup procedure and Phase 2 step 10 for the "grow the database" mechanism.
- **`3-TRANSFORMATIONS/Translations/<lang>-<TrackName>/termbase.md`** — the per-track Pāli→English term lock used by the translation that produced the §4 verses. The plan termbase above is the canonical authority for the prose sections (§1, §5), but this file is the fallback when a term isn't yet in the plan termbase: look here for the BB-curated rendering before inventing one. Many entries here are still `TODO`; if both this file and the plan termbase have no rendering, see Phase 2 step 10.
- **`2-RAILS/Bilingual-Glossaries/pi-<lang>.md`** — the consolidated bilingual glossary. Read on demand when neither termbase has the term being looked up.

Then for each day `N` in the range (only after every assets file in the batch is written):

1. Read `0-INBOX/daily-tipitaka/day-NNN-assets.md`.
2. Check whether `<lang>/days/day-NNN.md` exists and whether it is in unfilled-template state. If it is filled, stop for that day and report — do not overwrite.
3. Compose §1 (Today's Chanting Guide). **Hard cap ~180 words** (two short paragraphs + closing question). One short paragraph that says where the passage sits in the larger map (drawn from the section summary). One short paragraph that says what the day's verses walk through, in plain language. End with the closing line: "Today's question to carry into the chant: *…*" Write for a casual practitioner with five minutes — the test is whether they could read it before reaching the verses and still feel oriented, not whether it covers every structural feature of the passage. Cut, don't expand.

   **Term-lock lookup (do this before drafting §1).** Make a short list of the Pāli technical terms you intend to use in §1 (e.g. *kāmāvacara*, *rūpāvacara*, *jhāna*, *kusala*, *citta*). For each one, in this order of authority:
   1. **Check `<lang>/termbase.md`** (the plan termbase). If the term has a row with a non-`TODO` rendering, use that rendering verbatim in §1.
   2. **Otherwise check `3-TRANSFORMATIONS/Translations/<lang>-<TrackName>/termbase.md`** (the translation track termbase). If found, use that rendering AND append a new row to the plan termbase so the lock propagates (see Phase 2 step 10).
   3. **Otherwise scan today's drafted §4 verses** for the English wording the translation file used for that term, and use that wording. Append a row to the plan termbase.
   4. **Otherwise consult `2-RAILS/Bilingual-Glossaries/pi-<lang>.md`** (the consolidated glossary) and use the rendering there. Append a row to the plan termbase.
   5. **Last resort:** if no rendering is found anywhere, render the term with the skill's best plain-English gloss AND append a candidate row to the plan termbase with `status: candidate` and a note in the run report that the next reviewer should confirm.
   The point: every term in §1 traces to a locked rendering, and the act of using a new term *grows* the termbase. Never invent a rendering on the fly without recording it back.

   **Plain-English checklist for §1.** Aim for Flesch-Kincaid grade ≤ 9 (8th-grade reading level — see the audience profile). Concretely: average sentence length 12–15 words; common words over multi-syllable Latinate ones; Pāli terms are welcome but each gets a short plain-English gloss the first time it appears (the locked rendering goes first, the plain-English gloss follows in parentheses if the locked term reads academic — e.g. *"the *Rūpāvacarakusalaṃ* — wholesome consciousness of the fine-material sphere (the mind in deep meditation)"*); no figurative English idioms ("step off the map", "the rubber meets the road"); no internal-architecture references ("the summary rail says…" — the reader doesn't know what a rail is). After drafting, re-read §1 imagining a non-native English reader in Kolkata, Nagpur, or Sankisa (see persona vignettes in `<lang>/audience.md`). If a sentence would stop them, shorten it or swap a simpler word — but do not swap the *locked term itself*; only the surrounding wording or the parenthetical gloss.
4. §2, §3, §7: copy the liturgy-transclude lines from the template unchanged.
5. Compose §4 (Reading for Meaning) using **only the first and last verses** of the day's range, in this shape:
   - One header line: `**Verses A–B.** *(Full text rendered in the WeBuddhist app from the verse library; the first and last verses of the range are printed below so the plan-importer can find the right entries.)*`
   - Then `**v. A.** <first verse, verbatim from the assets file's "English translation" section>`
   - Then a separator line containing only `…`
   - Then `**v. B.** <last verse, verbatim from the assets file's "English translation" section>`
   - Then `*Source: [[2-RAILS/Sections/<book>-summaries.md]], [[2-RAILS/Sections/<book>-practice.md]]*`
   Do not paraphrase the verses; take them verbatim from the assets file (Rule §10). The translation track requirements file is what governs the wording of the assets-file translation, not this skill — by the time §4 is being composed, those decisions are already baked into the assets text.
6. Compose §5 (Pāli Word of the Day). **Hard cap ~140 words.** Pick a term named in the practice rail block as central to today's passage. Three parts in this order:
   - `### <TERM> — <short plain-English gloss, e.g. "Deep Meditation Focus" not "Meditative Absorption">`
   - `**Pronunciation:** <syllabified guide, one line, plain-language phonetics — e.g. "The 'jh' is like a soft 'j'." Avoid IPA-style notation.>`
   - `**In today's passage:** <2–4 sentences on what the word does in the day's verses, drawn from the practice rail and section summary. Fold any literal-sense note in here if it earns its place. If a second Pāli term is needed, gloss it in parentheses the first time.>`
   - `**Why it matters:** <2–4 sentences on how the word changes how the practitioner sees their own mind, drawn from the practice rail — translated out of rail vocabulary into plain English. End on something a casual reader can carry — less harm, more good, knowing their mind a little better.>`
   No separate "Literal sense" or "Etymology" paragraph. Re-count words after writing; cut if over cap.

   **Term-lock lookup for §5.** Same procedure as §1 (Phase 2 step 3 above). The headword of §5 — the Pāli word being foregrounded — is itself a candidate for the plan termbase. **Before composing §5, run the term-lock lookup on the headword.** If it has a locked rendering in `<lang>/termbase.md`, the §5 heading must use that rendering (e.g. *"JHĀNA — Meditative Absorption"* not *"JHĀNA — Deep Meditation Focus"* if the locked rendering is "meditative absorption"). The plain-English gloss can follow in parentheses or in the "In today's passage" paragraph. Any *other* Pāli term mentioned in §5 (e.g. *cetasika*, the names of the five hindrances) also runs through the lookup before being used.

   **Plain-English checklist for §5.** Same target as §1: Flesch-Kincaid grade ≤ 9, average sentence length 12–15 words, common words over multi-syllable Latinate ones. **No internal-architecture references** ("the practice rail describes…", "the section summary foregrounds…") — readers don't know what the rails are and shouldn't have to. Translate rail concepts into reader-facing language instead ("the teaching says…", "in practice this is…"). Pāli technical terms are welcome; the locked rendering goes first, then a plain-English gloss in parentheses if needed.
7. Compose §6 (Chanting in Pāli) using **only the first and last Pāli verses** of the day's range, in this shape:
   - One header line: `**Verses A–B.** *(Full Pāli text rendered in the WeBuddhist app from the verse library; the first and last verses of the range are printed below — with their block IDs — so the plan-importer can find the right entries.)*`
   - If the verse range opens inside a named subsection of the source text, name it on one orientation line before the first verse — e.g. `**Section:** Suññatavāro → Rūpāvacarakusalaṃ → Catukkanayo`. If the range straddles new headings, name them too. Do **not** print full heading blocks; the plan-importer needs orientation, not the full TOC.
   - Then `**A.** <first Pāli verse, verbatim from the assets file, formatted for chanting (clause-level line breaks, closing formula in bold). Block ID `^<book>-<A>` at the end.>`
   - Then a separator line containing only `…`
   - Then `**B.** <last Pāli verse, same shape, ending with block ID `^<book>-<B>`.>`
8. Compose §8 (App Notification): thematic Title (≤ 40 chars), one-sentence Body hook (≤ 120 chars), optional Button (≤ 15 chars, default `Begin`). Re-count characters after writing — if any cap is exceeded, tighten before moving on.
9. Write the day file at `<lang>/days/day-NNN.md`. Frontmatter populated per the format above. `status: draft` always — the human contributor flips it to `partial` or `complete` after review.
10. **Grow the plan termbase.** For each Pāli term that was used in §1 or §5 of any day in this batch and was *not* already in `<lang>/termbase.md` with a non-`TODO` rendering at the start of the run, append a new row to `<lang>/termbase.md` recording the rendering that was used. Each new row has:
    - `Pāli` — the term lemma (e.g. `kāmāvacara`, not `kāmāvacaraṃ`).
    - `English (Contemporary)` (or the per-language column) — the rendering used in the day file's §1 or §5. Italicised per the existing rows' convention.
    - `Tibetan` / `Chinese` / `Hindi` — leave blank if this run is for a language those columns don't apply to.
    - `Bilingual Glossary / Sense` — the path to the consolidated bilingual glossary entry if one exists (`2-RAILS/Bilingual-Glossaries/pi-<lang>.md`), or a local-wiki page if one exists.
    - `Status` — `draft` if the rendering came from a non-`TODO` row in the translation track termbase or from a published §4 verse; `candidate` if the skill had to invent the rendering (last-resort case 5 above) and needs reviewer confirmation.
    Keep rows alphabetical by Pāli (the existing file's convention). **Never modify or downgrade an existing locked row** — if the skill thinks a locked rendering is wrong for the casual register, flag it in the run report and leave the row untouched. Only the human contributor changes locked rows, because every change requires re-reading every day that used the old rendering.
11. Report the new termbase rows added by this run alongside the day file paths, so the human contributor can confirm them in the same review pass.

#### Phase 2 completion check

After Phase 2 has run for every day in the batch:

- [ ] One day file exists at `3-TRANSFORMATIONS/Plans/Daily-Tipitaka/<lang>/days/day-NNN.md` for every day whose Phase 1 assets file was complete.
- [ ] No pre-existing filled day file was overwritten — any conflict was reported instead.
- [ ] Every day file's `sources:` frontmatter lists at least the summaries rail and the practice rail.
- [ ] Every day file's §4 (Reading for Meaning) contains **exactly two** verse-numbered entries: the first verse of the range (`**v. A.**`) and the last (`**v. B.**`), separated by a `…` divider line. No other verses.
- [ ] Every day file's §6 (Chanting in Pāli) contains **exactly two** distinct block IDs: `^<book>-A` (on the first verse) and `^<book>-B` (on the last verse), separated by a `…` divider line. No other block IDs.
- [ ] **Both boundary verses in §4 and §6 begin at their verse's opening line.** For each of the four entries (§4 first/last, §6 first/last), resolve the verse in its source file, walk back to its opening line, and confirm the day file's entry starts with that same text. An entry that starts mid-verse is the failure mode this check exists for — it is invisible to every other check here. A bash test:
  ```bash
  # Substitute DAY, BOOK (1/2/3), A and B; run from the vault root.
  python3 -c "
  import re
  DAY,P,A,B='078','2',1,15
  SRC=f'1-SOURCES/Text/pi-{P}.md'
  def opening(path,n):
      L=open(path,encoding='utf-8').read().split('\n')
      ei=[i for i,l in enumerate(L) if re.search(rf'\^{P}-{n}\s*\$',l)][0]
      si=ei; j=ei-1
      while j>=0:
          s=L[j].strip()
          if s=='' or re.search(r'\^[\w\-]+\s*\$',L[j]) or re.match(r'^#{1,6}\s',L[j]): break
          si=j; j-=1
      first=re.sub(rf'\s*\^{P}-\d+\s*\$','',L[si]).strip()
      return re.sub(rf'^{n}\.\s*','',first)
  t=open(f'3-TRANSFORMATIONS/Plans/Daily-Tipitaka/en/days/day-{DAY}.md',encoding='utf-8').read()
  s6=re.search(r'## 6\..*?(?=\n## 7)',t,re.S).group(0)
  for n in (A,B):
      op=opening(SRC,n)
      ok=bool(re.search(rf'\*\*{n}\.\*\* '+re.escape(op[:55]),s6))
      print(f'  §6 v{n}: {\"OK\" if ok else \"STARTS MID-VERSE\"}')
  "
  ```
- [ ] **The first and last verse entries are distinguishable from each other.** In the Abhidhamma's repeating formulas consecutive verses often open with identical wording, so if a day's two entries read the same, the closing line is missing from one or both (see "Multi-line verses in §4 and §6"). A reader must be able to tell the range's start from its end.
- [ ] §1 word count ≤ ~180 words (re-count after writing). Cut if over.
- [ ] §5 word count ≤ ~140 words (re-count after writing). Cut if over.
- [ ] Every Pāli technical term appearing in §1 or §5 has a corresponding row in `<lang>/termbase.md` (either pre-existing or newly appended in Phase 2 step 10), and the English rendering used in §1/§5 matches that row's locked rendering verbatim. **Spot-check at least three terms per day** by grepping the term in §1/§5 against the termbase row.
- [ ] §1 and §5 each measure at **Flesch-Kincaid grade ≤ 9** (8th-grade reading level — the audience profile's target). If above, rewrite — don't just trim, simplify. Pāli terms are fine when glossed plainly; what pushes the grade up is academic register, long Latinate words where a short Anglo-Saxon one would do, and 25+-word sentences. A quick measurement check in bash:
  ```bash
  # Run from any folder; substitute the day file path:
  python3 -c "
  import re, sys
  txt = open('PATH/TO/day-NNN.md').read()
  for n, label in [(1, '§1'), (5, '§5')]:
      m = re.search(rf'## {n}\.[^\n]+\n(.*?)(?=\n## |\Z)', txt, re.S)
      if not m: continue
      s = re.sub(r'\*+([^*]+)\*+', r'\1', m.group(1))
      s = re.sub(r'###?\s+[^\n]+', '', s)
      sents = [x for x in re.split(r'[.!?]+', s) if x.strip()]
      words = re.findall(r'[A-Za-zĀāĪīŪūṅñṭḍṇṃḷ-]+', s)
      def syl(w):
          w = re.sub(r'[āīūṅñṭḍṇṃḷṛṣśḥ]', 'a', w.lower())
          c = 0; pv = False
          for ch in w:
              v = ch in 'aeiouy'
              if v and not pv: c += 1
              pv = v
          if w.endswith('e') and c > 1: c -= 1
          return max(1, c)
      asl = len(words)/len(sents); asw = sum(syl(w) for w in words)/len(words)
      print(f'{label}: FK grade {0.39*asl + 11.8*asw - 15.59:.1f}  ease {206.835 - 1.015*asl - 84.6*asw:.1f}  ({len(words)} words, {len(sents)} sentences)')
  "
  ```
- [ ] Every day file's §8 app notification has: Title ≤ 40 chars, Body ≤ 120 chars, Button (if present) ≤ 15 chars. Re-count after writing.

Report the day numbers written, the assets file paths, the day file paths, and any verification warnings.

---

## Completion check

This skill has two internal gates. A run is complete only when both pass.

**Phase 0 + Phase 1 (assets):**

- [ ] `day-range` and `language-tag` both supplied; language folder exists
- [ ] Schedule row located for every day in the range
- [ ] Phase 1 completion check passes for every day — assets file written and verified (see *Phase 1 completion check (gate)* above)
- [ ] No day silently skipped; every halt reported

**Phase 2 (day files):**

- [ ] Phase 2 completion check passes for every day (see *Phase 2 completion check* above) — day file written, no overwrites, citations clean, block IDs preserved, notification character caps respected
- [ ] Final report names every assets file path, every day file path, and any verification warnings
