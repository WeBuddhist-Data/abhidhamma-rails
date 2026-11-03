# map_segments.py

Maps each `segment_id` in a to-map export (e.g. `segments to be mapped.json`,
`tibetan_to_map.json`, `chinese_to_map.json`) to the corresponding `id` in
that language's segments registry (e.g. `tibetan_segments.json`,
`chinese_segments.json`), by matching text content against that language's
translation source markdown.

## Why this exists

- **a to-map file** (e.g. `segments to be mapped.json`, `tibetan_to_map.json`,
  `chinese_to_map.json`) — a list of `{segment_id, content}` rows, in
  translation order. This is the dataset that *needs* IDs assigned.
- **a segments registry** (e.g. `tibetan_segments.json`, `chinese_segments.json`)
  — a list of `{id, type, reference, lines}` rows describing how that
  language's source markdown is segmented into blocks (title, front_matter,
  verse, back_matter), where `reference` is the verse/block number
  (e.g. `"7-58"`) and `id` is the internal ID we want. **One registry per
  language/translation** — there's no single shared file, and none of them
  is a default; the right one for the run at hand is always passed
  explicitly as `--segments`.
- **that language's source markdown** (e.g.
  `1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md` for Tibetan,
  `1-SOURCES/Translations/zh-蔣揚仁欽譯師.md` for Chinese) — the actual
  source text. Every paragraph ends with an Obsidian block ID (`^1-1`,
  `^7-58`, ...) that matches the `reference` field in that language's
  registry.

The script uses the markdown file as the bridge: it finds which block a
to-map row's content corresponds to, reads that block's `^ref`, then looks
up that `ref` in the given `--segments` registry to get the `id`. The
output is a `{"segment_id", ..., "id"}` list (see "Output files" below for
the full shape).

## Folder layout

- **`segment_id_mapping/skill/`** — the map-segments skill: `map-segments.md`, this
  `README.md`, and `scripts/` (`map_segments.py`, and any `manual_overrides.json` /
  `<stem>_manual_overrides.json` files) — everything the script needs to run,
  in one place.
- **`segment_id_mapping/output/`** — every `<output>.json` / `<report>.json` pair the script
  produces, from every run.
- Raw to-map/segments-registry exports (`segments to be mapped.json`,
  `tibetan_segments.json`, `tibetan_to_map.json`, `chinese_segments.json`,
  `chinese_to_map.json`, ...) stay directly under `segment_id_mapping/` —
  they're inputs, not something the script generates.

## How to run it

From the vault root (`bodhisattvacharyavatara-rails/`):

```bash
python3 segment_id_mapping/skill/scripts/map_segments.py --segments "segment_id_mapping/tibetan_segments.json"
```

`--source-md`, `--to-map`, `--output` and `--report` default to the
original Tibetan run's paths, all relative to the vault root:

| Argument      | Default                                                  |
|---------------|-----------------------------------------------------------|
| `--source-md` | `1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md`             |
| `--to-map`    | `segment_id_mapping/segments to be mapped.json`                            |
| `--segments`  | *(none — always required, see below)*                      |
| `--output`    | `segment_id_mapping/output/segment_id_mapping.json`                         |
| `--report`    | `segment_id_mapping/output/segment_id_mapping.report.json`                  |

**`--segments` has no default and must always be passed explicitly.** The
registry is per-language — pointing a Chinese to-map file at the Tibetan
registry (or vice versa) would silently produce wrong or missing ids rather
than an error, so the script refuses to run without `--segments` rather
than guessing which one you mean.

Override any of the others if your files live elsewhere or you want a
different output name — this is the normal way to run it against a new
export, e.g.:

```bash
python3 segment_id_mapping/skill/scripts/map_segments.py \
  --source-md "1-SOURCES/Translations/zh-蔣揚仁欽譯師.md" \
  --to-map "segment_id_mapping/chinese_to_map.json" \
  --segments "segment_id_mapping/chinese_segments.json" \
  --output "segment_id_mapping/output/chinese_segment_id_mapping.json" \
  --report "segment_id_mapping/output/chinese_segment_id_mapping.report.json"
```

`--to-map` can point at either shape of to-map file: a flat
`[{"segment_id", "content"}, ...]` list, or the nested
`{"content": {"sections": [{"segments": [{"segment_id", "content"}, ...]}]}}`
shape some exports use — the script extracts and flattens the nested one
automatically (recursing into any sub-sections too).

If a few rows can't be resolved automatically (see `unmatched` in the
report) and you've manually confirmed the correct verse for one, add it to
that to-map file's overrides file (e.g. `tibetan_manual_overrides.json`,
`chinese_manual_overrides.json` — see "Deriving filenames" via the skill,
or just name it after the to-map file) and pass `--overrides`:

```bash
python3 segment_id_mapping/skill/scripts/map_segments.py \
  --to-map "segment_id_mapping/tibetan_to_map.json" \
  --segments "segment_id_mapping/tibetan_segments.json" \
  --overrides "segment_id_mapping/skill/scripts/manual_overrides.json" \
  --output "segment_id_mapping/output/tibetan_segment_id_mapping.json" \
  --report "segment_id_mapping/output/tibetan_segment_id_mapping.report.json"
```

An overrides file (in `segment_id_mapping/skill/scripts/`) is a list of
`{"segment_id": ..., "reference": ...}` entries (or
`{"segment_id": ..., "id": ...}` if you already know the exact registry
id). These are applied verbatim before any automatic matching runs, so they
can legitimately point at a reference some other segment_id already
claimed (a genuine duplicate verse) — the row is simply removed from the
pool the automatic matcher works through.

Requires only Python 3 standard library — no extra packages to install.

## What it does, step by step

1. **Parse the source markdown.** Splits the file into paragraph blocks
   (separated by blank lines), skipping YAML frontmatter and bare
   transclusion lines (`![[...]]`). Each remaining block that ends in a
   `^ref` block ID becomes one source segment: `(reference, text)`.

2. **Load and de-duplicate the to-map file.** Accepts either the flat
   `[{"segment_id", "content"}, ...]` shape or the nested
   `{"content": {"sections": [{"segments": [...]}]}}` shape (flattened
   automatically). Then de-duplicates by `segment_id`, keeping first
   occurrence order — one export was found to contain the same handful of
   `segment_id`s repeated dozens of times back-to-back (an upstream
   glitch). The script reports how many duplicate rows it dropped.

3. **Match content, in order.** For each row, it normalizes the text —
   stripping the `⤵` line-break marker and all whitespace, so:
   - `དང་།།` (no space) and `དང་། །` (spaced) compare equal, and
   - a `⤵`-joined single-line JSON string compares equal to the markdown's
     real multi-line verse.

   The common case is a plain forward scan: both lists are in the same
   order, so it looks for the next matching source block from where the
   previous match left off. On top of that, four fallbacks handle
   real-world export glitches, tried in order for every row:

   - **exact forward** — the normal case;
   - **source-side merge** — one to-map row is itself the concatenation of
     several *consecutive source* blocks (e.g. a translator's colophon the
     markdown keeps as 3 separate blocks but the export combined into one
     row);
   - **small backward window** — a row that arrived slightly out of order
     upstream (verse N+2 appears in the file before verses N and N+1);
   - **fuzzy match** (similarity ≥ 90%) within a forward window, to
     tolerate small text drift between the two files (a typo fixed in the
     markdown after the JSON was generated).

   If none of those succeed for a single row, it's held in a small buffer
   and merged with the next row(s) — up to 4 — and retried. This is the
   reverse case: the markdown keeps a multi-line verse as one block, but
   the to-map file split that same verse across two rows. All rows in a
   merged group end up pointing at the same `id`.

   Anything still unresolved after all of that is left out of the mapping
   and listed in the report, untouched — the script never guesses.

4. **Look up the `id`.** Once a row is tied to a markdown `reference`, that
   reference is looked up in the given `--segments` registry to get the final `id`.

## Output files

- **`<output>.json`** — the result: a flat list of
  `{"segment_id", "content", "segment_number", "source_content", "reference", "id"}`,
  **one entry per unique `segment_id` in the to-map file, matched or not**,
  **sorted ascending by position in the to-map file**. `content` is the
  to-map row's own text; `segment_number` is included **only when the
  to-map file itself carries a real one** (the nested/sectioned shape) — for
  the flat `{"segment_id","content"}` shape, which has no segment_number at
  all, the key is **omitted entirely** rather than filled in with a
  fabricated or null value (this used to fabricate a positional one; that
  was reverted — a made-up number would look like real data next to the
  segment_id it doesn't actually belong to). Row order in the output file is
  always correct regardless (real segment_number, or to-map file position
  when there isn't one); `source_content` is the markdown block's own text at that
  reference, so the two can be eyeballed side by side; `reference` is the
  markdown verse/block id it matched (e.g. `"7-58"`); `id` is the
  corresponding registry id. A row that couldn't be matched at all,
  or matched a reference missing from the `--segments` registry, still gets a row
  here — with `source_content`, `reference` and `id` all `null` — so this
  file always accounts for every segment_id in the to-map file, not just the
  matched ones.
- **`<report>.json`** — a diagnostic report (this is the file to read when
  you want to know *why* something didn't match, or double-check a fallback
  fired correctly — nothing here is needed to consume the output mapping):
  - `total_rows_in_to_map_file` / `duplicate_rows_dropped` / `unique_segment_ids`
  - `matched` / `matched_exact` / `matched_fuzzy` / `matched_manual`
  - `manual_matches` — rows resolved via `--overrides`
  - `fuzzy_matches` — which rows only matched approximately, with both texts
    shown side by side, worth a quick manual glance
  - `merged_matches` — to-map rows combined to match a single source block
  - `source_merge_matches` — a to-map row matched against several
    *consecutive source* blocks combined (e.g. a 3-block colophon). `reference`
    and `id` here are the **first/anchor block only** (`"b-1"`, not
    `["b-1","b-2","b-3"]`) — same as what actually lands in the output file,
    since downstream only supports a 1:1 mapping, not 1-to-many.
  - `out_of_order_matches` — a row matched behind the current pointer
    (arrived out of sequence upstream)
  - `unmatched` — rows that couldn't be matched at all, in the same shape
    as an `<output>.json` row (segment_id, content, segment_number,
    source_content, reference, id) with `source_content`, `reference` and
    `id` set to `null`, sorted by `segment_number` — each needs manual
    review (see below for what that usually means). **These rows are also
    included in `<output>.json` itself** (with the same nulls) — they're
    repeated here purely for convenience, so you don't have to filter the
    output file to find what still needs attention.
  - `reference_not_in_segments_json` — same null-filled shape (also mirrored
    into `<output>.json`), for a row that matched a markdown block whose
    reference wasn't found in the `--segments` registry (should be empty)
  - `unmatched_source_segments_count` / `unmatched_source_segments` — the
    *reverse* direction: source markdown blocks that no to-map row ever
    claimed at all, as `{"reference", "id", "type", "source_content"}`.
    This is expected for chapter/section headings (`type: "title"`), which
    have no to-map counterpart by design — but any `verse`/`front_matter`/
    `back_matter` reference showing up here means the to-map file is
    missing that content outright (as opposed to `unmatched`, where a
    to-map row exists but couldn't be matched to anything). **This one
    lives in the report only** — it has no `segment_id`, so it has no
    natural row in `<output>.json`.

## Runs so far

- **`segments to be mapped.json`** (344 rows, 134 unique after dropping 210
  duplicate rows): **134/134 matched** (132 exact, 2 fuzzy, 1 merged pair).
- **`tibetan_to_map.json`** (930 rows, all unique): **928/930
  matched** (915 exact, 10 fuzzy, 3 manual, 1 merged pair, 1 source-merge, 2
  out-of-order). Originally 5 rows came back unmatched — genuine data
  issues in that export, not something the script can safely resolve on
  its own:
  - the document's frontmatter `title:` field, which has no counterpart in
    the body text at all — **confirmed by hand as `^0`**, now in
    `manual_overrides.json`;
  - a near-duplicate of a verse from a completely different chapter
    (chapter 4), inserted in the middle of chapter 7's sequence, so its
    rightful verse was already matched earlier — **confirmed by hand as
    `^4-44`** (the same id as its earlier occurrence — a genuine repeated
    verse), also now in `manual_overrides.json`;
  - a real verse (`segment_number` 499) with two extra lines prepended that
    don't appear anywhere in the source file, so the automatic matcher
    couldn't reach it (the source block is only 4 lines, this row is 6) —
    **confirmed by hand as `^7-62`**, also now in `manual_overrides.json`;
  - two rows with no matching text anywhere in the source file at all —
    still unmatched (`segment_number` 564 and 699).

  The 2 still-unmatched rows are listed in `unmatched` in the report, with
  their full content, for a human to decide what to do with them —
  guessing would risk a wrong mapping, which is worse than leaving it
  blank. Add any further confirmations to `manual_overrides.json` and
  re-run with `--overrides` to fold them in.

  `unmatched_source_segments` for this run has 13 entries, all chapter and
  section headings (`^I-0`, `^1-0` ... `^10-0`, `^a-0`, `^b-0`), which never
  have a to-map counterpart by design — every real verse in the source is
  now accounted for.

  **A subtlety worth knowing about, in case you add more overrides later:**
  a manual override can point at a reference some *other* segment_id
  matches automatically and correctly (a genuine duplicate verse, like
  `^4-44` above, which appears twice in the translation). The script
  applies overrides before automatic matching runs, but deliberately marks
  the override's source reference as "consumed" only *after* the automatic
  pass finishes — never during it. An earlier version marked it consumed
  immediately, which caused the automatic pass to skip the reference by
  the time it reached the *other*, legitimately-matching row, incorrectly
  flipping that row to unmatched. Both rows now correctly end up pointing
  at the same `id`.

- **`engish_to_map.json`** (131 rows, all unique, flat `{"segment_id","content"}`
  shape with no `segment_number` — handled the same way as the very first
  run above, positional order preserved) matched against
  `3-TRANSFORMATIONS/Translations/AI_translation/english/bca-english-plain.md`:
  **131/131 matched, all via `--overrides` (0 exact, 0 fuzzy)**. This file is
  an AI-paraphrased "plain English" rewrite, not the same wording as the
  source, so the script's exact/fuzzy string matching found nothing at all —
  every row had to be matched by *meaning* instead, done by reading both
  files and verifying the correspondence (see "Content that won't match
  string-for-string" below), then encoding the full result as
  `{"segment_id","reference"}` overrides in
  `segment_id_mapping/skill/scripts/engish_manual_overrides.json` and
  running the normal pipeline with `--overrides` pointing at it. One
  genuine gap was found this way: `^2-a` ("Thus ends chapter two...") has
  no corresponding to-map row — confirmed both by the exact row-count math
  (131 to-map rows vs. 131 non-heading source blocks in range once `2-a` is
  excluded) and by it correctly appearing in `unmatched_source_segments`.

- **`chinese_to_map.json`** (502 rows, all unique, same flat shape) matched
  against `1-SOURCES/Translations/zh-蔣揚仁欽譯師.md`: **502/502 matched, all
  exact, no overrides needed** — unlike the English run above, this to-map
  file is extracted straight from this same source markdown (a literal
  human translation), so plain string matching worked immediately.
  `unmatched_source_segments` is large for this run (423 of 925 source
  blocks) because this to-map file only covers `^1-1` through `^7-76`
  (chapters 1–7) — the source markdown covers the full ten-chapter text
  plus colophon, so everything from chapter 8 onward (plus every chapter
  heading throughout) is correctly reported as not-yet-covered, not
  missing. Re-running once a fuller export exists will shrink this.

  Note: the first attempt at this run used `tibetan_segments.json` as the
  registry (before `chinese_segments.json` existed as its own file) and
  came back 500/502, flagging `^3-34` and `^7-76` as matched-but-missing
  from the registry. That was simply the wrong registry for this
  language — re-running with the real `chinese_segments.json` resolved
  both immediately. This is exactly why `--segments` has no default: using
  the wrong language's registry doesn't error, it just quietly produces
  gaps that look like genuine data problems.

### Content that won't match string-for-string (semantic matching)

`map_segments.py` only does exact and fuzzy *string* matching — it has no
way to know two differently-worded sentences mean the same thing. That's
enough for a to-map export that's the same text with minor drift (typos,
respacing), but not for a to-map file that's an independent paraphrase of
the source (an "AI-plain-English" rewrite, a different translator's prose,
etc.) — running the script as-is against that kind of file comes back
essentially 0% matched.

When that happens, the fix isn't a script change — it's reading both files
and aligning them by meaning instead, then feeding the *result* through the
same pipeline as a full set of `--overrides` (all rows, not just the
ambiguous ones). In this vault every translation shares the same `^ref`
chapter-verse numbering, so a paraphrase that follows the source in order
usually lines up positionally with the source's non-heading blocks —
confirm this (start, end, every chapter boundary, and a row-count check)
rather than assume it; a small count mismatch is usually one specific
dropped or extra row, findable the same way you'd hunt a merge/split/
out-of-order case, just by meaning instead of string equality. The
`map-segments` skill (see `skill/map-segments.md`, step 4) has the full worked
process — this is what produced the `engish_to_map.json` run above.
