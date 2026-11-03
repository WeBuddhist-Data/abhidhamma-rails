---
name: map-segments
description: Runs the segment-ID mapping pipeline for the bodhisattvacharyavatara-rails vault -- maps segment_ids in a "to-map" JSON export (any language) to the ids in a language-specific segments registry (e.g. segment_id_mapping/tibetan_segments.json, segment_id_mapping/chinese_segments.json), by matching content against a given source translation markdown, falling back to Claude's own semantic/meaning-based alignment when the to-map file is a paraphrase (e.g. an AI-plain-English rewrite) rather than the same wording. Use when the user asks to run segment mapping, map segments to ids, generate a segment_id mapping, or gives a source-md path, a to-map/segment file path, and a segments-registry path for this pipeline (e.g. "run map-segments on X, Y and Z", "map these segments against the Tibetan translation", "map this English/Chinese/... to-map file").
---

You are running the existing `map_segments.py` pipeline in this vault (the
`bodhisattvacharyavatara-rails` Obsidian vault) against a source translation
markdown, a to-map segment file, and a segments-registry file, all three
named by the user. Do not re-derive or re-implement the matching logic --
the script already handles it. Your job is: locate the vault, locate/
restore the script, work out the right arguments from what the user gave
you, run it, and report the results back in plain language.

## 1. Inputs the user gives you

The user will name, in their prompt, **three paths relative to the vault
root**:

- a **source markdown** file (the translation to match content against),
  e.g. `1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md`
- a **to-map / segment** file (the export that needs ids assigned),
  e.g. `segment_id_mapping/tibetan_to_map.json`
- a **segments registry** file (the id lookup for this run's language --
  e.g. `segment_id_mapping/tibetan_segments.json` or
  `segment_id_mapping/chinese_segments.json`), used as `--segments`

There is **no default or fixed registry file** -- it's per-language/
translation (Tibetan content needs the Tibetan registry, Chinese content
needs the Chinese one, etc.), and guessing or reusing whichever one was
used last would silently produce wrong ids rather than an error. The
script itself enforces this: `--segments` is a required argument with no
default, so a run without it fails fast instead of guessing.

If any of the three is missing or ambiguous from the prompt, ask for it --
don't guess a source-md file when more than one translation exists in
`1-SOURCES/Translations/`, and don't guess which `*_segments.json` registry
applies to which language.

Everything else below is fixed/derived automatically; don't ask the user
about it unless something is actually missing or broken.

## 2. Fixed vault layout this pipeline assumes

- **`segment_id_mapping/skill/scripts/map_segments.py`** -- the script itself.
- **`segment_id_mapping/<lang>_segments.json`** (e.g. `tibetan_segments.json`,
  `chinese_segments.json`) -- the id registry for one language/translation
  (the `reference` -> `id` map). One of these is always given explicitly by
  the user as the third input above and passed as `--segments`; never
  assume or fall back to a particular one.
- **`segment_id_mapping/skill/scripts/<name>_manual_overrides.json`** --
  optional, per-to-map-file overrides: human-confirmed `{"segment_id","reference"}`
  entries (from ambiguous rows a person resolved by hand -- see step 6) or
  a full semantic-alignment mapping you produced yourself (see step 4).
  Name it after the to-map file's stem (the same `<stem>` used for output
  filenames, e.g. `tibetan_manual_overrides.json` for `tibetan_to_map.json`)
  so overrides for different languages/runs never collide. Pass it as
  `--overrides` **only if the file exists** for that to-map file (an
  empty/missing overrides file is normal and not an error). The existing
  `manual_overrides.json` (no stem prefix) is the original Tibetan-run file
  from before this per-stem convention -- treat it as that run's overrides
  file specifically, not a shared/default one.
- **`segment_id_mapping/output/`** -- every `<name>_segment_id_mapping.json` /
  `.report.json` pair this pipeline has ever produced lands here.

If `segment_id_mapping/skill/scripts/map_segments.py` is missing (fresh vault, or it was deleted),
restore it from the copy bundled with this skill at `scripts/map_segments.py`
before doing anything else -- write it to `segment_id_mapping/skill/scripts/map_segments.py` first,
then proceed. Don't touch any `segment_id_mapping/<lang>_segments.json` registry or `segment_id_mapping/skill/scripts/manual_overrides.json`
this way; those are per-vault data, not something this skill ships a copy of.

## 3. Deriving the output filenames

Take the to-map file's basename, strip its extension, and strip a trailing
`_to_map` / ` to be mapped` / `_to_be_mapped` (case-insensitive, treating
spaces and underscores as equivalent) if present -- what's left is the
`<stem>`. Output goes to:

- `segment_id_mapping/output/<stem>_segment_id_mapping.json`
- `segment_id_mapping/output/<stem>_segment_id_mapping.report.json`

Examples already produced in this vault, for reference:
- `segment_id_mapping/tibetan_to_map.json` -> `segment_id_mapping/output/tibetan_segment_id_mapping.json`
- `segment_id_mapping/segments to be mapped.json` -> `segment_id_mapping/output/segment_id_mapping.json`

If a file already exists at the derived output path from a prior run,
overwrite it (that's the expected way to re-run after adding overrides or
fixing the source md) -- but mention in your summary that you overwrote a
prior run's output, in case the user didn't expect that.

## 4. When the content is a paraphrase, not a literal match (semantic matching)

`map_segments.py` only ever does exact and fuzzy (character-similarity)
string matching -- it has no way to recognize that two differently-worded
sentences mean the same thing. That's fine for a to-map export that's the
*same* text with minor drift (typos, respacing). It is not fine for a
to-map file that's an independent paraphrase of the source -- e.g. an
"AI-plain-English" rewrite of a translation, or any case where the wording
is different but the underlying verses are the same. Running the script
as-is against that kind of file will come back essentially 0% matched, exact
and fuzzy alike. That's your signal to switch to semantic matching, done by
you (not the script), in three steps:

1. **Read both files in full** -- the whole to-map file, and the whole
   source markdown parsed the normal way (paragraph blocks ending in
   `^ref`, frontmatter and `![[...]]` transclusion lines skipped, same as
   the script does). Print/list both side by side with indices so you can
   scan them together.

2. **Establish the correspondence.** In this vault, every translation of
   this text (Tibetan, English, Chinese, ...) that follows the standard
   layout shares the exact same `^ref` numbering scheme (chapter-verse,
   e.g. `1-1`, `1-2`, ... `1-a` for a chapter-closing line, `2-0` for a
   chapter heading). So a to-map file that's a straight, in-order
   paraphrase of one of these translations will usually line up
   **positionally** with the source's non-heading blocks (`type != "title"`
   in the `--segments` registry) -- confirm this rather than assume it:
   - Compare the to-map file's first row against the source's first
     non-heading block, and its last row against the source's last
     non-heading block in the range it plausibly covers, by meaning.
   - Compare a few rows at every place a chapter boundary or other
     structural break falls (e.g. right around a `-a` chapter-closing
     block), since that's exactly where a row is most likely to have been
     skipped or an extra one inserted upstream.
   - Count non-heading source blocks in the covered range and compare to
     the to-map row count. An exact match is strong confirmation of clean
     1:1 correspondence; a small mismatch (off by 1 or 2) usually means
     one specific block was dropped from the export (as opposed to
     wholesale reshuffling) -- find it by checking the boundary regions
     from the previous bullet, the same way you'd hunt down a merge/split/
     out-of-order case in the deterministic pipeline, just judging by
     meaning instead of string equality.
   - If the mismatch is large, or spot checks disagree with straight
     positional order, don't force it -- tell the user what you found and
     ask, rather than guessing at a semantic alignment you're not confident
     in.

3. **Encode the result as overrides, then run the normal pipeline.**
   Once you've verified the correspondence (positionally, or however you
   resolved it), write out every `{"segment_id", "reference"}` pair --
   for **all** rows, not just the ones that would otherwise be ambiguous,
   since none of them will string/fuzzy-match at all -- to
   `segment_id_mapping/skill/scripts/<stem>_manual_overrides.json`, then run
   the script exactly as in step 5 with `--overrides` pointing at that
   file. Let the script do the rest (id lookup from the `--segments` registry,
   assembling `content`/`source_content`/`segment_number`, writing
   `<output>.json` and `<report>.json`, and reporting
   `unmatched_source_segments`) -- don't hand-build the output file
   yourself. A source block you deliberately left out (the genuinely
   dropped one from step 2) will correctly show up in
   `unmatched_source_segments` in the report; that's the pipeline
   confirming your finding, not an error to fix.

## 5. Running it

Work out which shell actually has access to the vault's files and can run
Python, then run (from the vault root):

```bash
python3 segment_id_mapping/skill/scripts/map_segments.py \
  --source-md "<source-md path the user gave>" \
  --to-map "<to-map path the user gave>" \
  --segments "<segments-registry path the user gave>" \
  [--overrides "segment_id_mapping/skill/scripts/<stem>_manual_overrides.json"]   # only if that file exists \
  --output "segment_id_mapping/output/<stem>_segment_id_mapping.json" \
  --report "segment_id_mapping/output/<stem>_segment_id_mapping.report.json"
```

- If you have direct shell + file access to the vault already (e.g. a
  device bridge shell mounted at the vault, or the vault is already local
  to your shell), just run it there directly -- no staging needed, and the
  outputs land straight in `segment_id_mapping/output/` on the real vault.
- If you only have the vault's files available in a separate workspace
  (e.g. they were uploaded/staged rather than live-mounted), run the script
  there instead, then write the two output files (and the restored
  `map_segments.py`, if you had to bootstrap it) back into the real vault's
  `segment_id_mapping/output/` (and `segment_id_mapping/skill/scripts/`) afterward.
- Requires only the Python 3 standard library -- no packages to install.
  If `python3` isn't available in whatever shell you're using, try `python`
  before concluding it's missing.

## 6. Reporting back

After it runs, read the console summary (it prints matched/unmatched
counts, and lists unmatched segment_ids and unmatched source references)
and tell the user, in plain language, not a wall of raw JSON:

- how many rows total, how many matched (exact / fuzzy / manual / merged),
  and how many are still unmatched
- if anything is unmatched, name the segment_ids and roughly what's in them
  so the user can decide whether to investigate or add a manual override
- if `unmatched_source_segments` (in the report) includes anything that
  isn't a chapter/section heading, call that out specifically -- it means
  the to-map file is missing real content, not just failing to match some
  it has
- where the two output files landed (the `segment_id_mapping/output/...` paths)

Never guess at an ambiguous match yourself (outside of the deliberate,
verified semantic-matching process in step 4). If the user then confirms a
correct mapping for a still-unmatched row by hand, add
`{"segment_id": "...", "reference": "..."}` to that to-map file's
`segment_id_mapping/skill/scripts/<stem>_manual_overrides.json` (create it
if it doesn't exist yet) and re-run with the same arguments to fold it
in -- this is the normal way to close out the last few rows of any run.
