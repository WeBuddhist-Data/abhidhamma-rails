# Parser — Root Text

Takes a linted source file and produces API-ready JSON payloads for the edition, TOC, and alignment.

## What it does

Runs these functions from the source `.md` and its lint JSON:

1. **extract_text_input** — strips null/empty fields from the lint JSON and writes a clean `text.json`, named after the source file
2. **build_edition** — extracts content from the source `.md`, builds a segmented edition with character-level spans, writes `edition.json`
3. **build_toc** — builds a nested table of contents from the source headings, writes `toc.json`
4. **build_alignment** — for `translation` and `commentary` files only, extracts segment-to-segment alignment from Obsidian transclusion links (`![[...#^ref]]`), writes `alignment.json`

## Output

```
output/
  <stem>/                          # one folder per source file
    <stem>.text.json        # clean text_input payload (named after the source file)
    <stem>.edition.json     # edition content + segmentation
    <stem>.toc.json         # nested TOC with character spans
    <stem>.alignment.json   # source↔target segment alignments (translations/commentaries only)
```

## Alignment

Transclusion links in the source file (`![[root_text_path#^ref]]`) define which root text segment each translation/commentary segment corresponds to.

- `source_segment_reference` — segment in the translation or commentary
- `target_segment_reference` — segment in the root text

For root texts and their translations, alignment is 1-to-1.

## Requirements

```
pip install PyYAML pyewts
```

Requires Python 3.8+.

## How to run

Run from the project root (`abhidhamma-rails/`):

```bash
python3 4-SYSTEM\scripts\parser-root-text\parser.py "1-SOURCES\Text\pi-1.md" "4-SYSTEM\scripts\linter-root-text\output\pi-1.lint.json"
```

## Notes

- Run the linter first — the parser reads `translation_of` and other resolved fields from the lint JSON
- Author/translator contributions without a resolvable id are dropped with a warning; missing contributions are allowed
- Missing `alt_titles` is allowed (warning only)
- Blocks without a reference marker (`^ref`) are skipped with a warning
- Header refs may have any depth (`^n-n-n-…`); content refs (verse / top / front / back) max `^n-n-n` (3 parts)
- Pure transclusion blocks (`![[...]]` only) are silently skipped — they are used for alignment, not content
- Tibetan TOC titles in Wylie are auto-converted to Unicode
- `metadata.source` comes from `source`, or `source_url` as an alias; `metadata.type` from `edition_type`, defaulting to `critical`
- Cleaned before parsing (the source file is never modified): `<small>…</small>` tags are dropped and the gloss text kept; non-breaking spaces become ordinary spaces
- A line of zero-width characters only counts as blank, so it does not split a block. The block is kept whole and a warning says its parts may each need their own block ID
- Headings deeper than level 6 (7 or more `#`) have `**` stripped from the TOC title, since Obsidian renders only six levels and people bold those to look like headings. Bold on levels 1–6 is left alone
- Transclusions written one after another form a single group, even when a blank line separates them. Anything else between them starts a new group
- Headings are TOC-only: they add no segment and no text to the edition `content` (no segment has type `title`). A TOC section spans from its heading's position in `content` to the next heading of the same or higher level (else the end of `content`); a heading followed directly by such a heading gets an empty span
- Alignment: headings take no alignment, and pending transclusions are dropped at a heading. Transclusions that target a heading in the `root_text` file are skipped (one warning lists them)
