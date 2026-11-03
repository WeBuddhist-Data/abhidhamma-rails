# Parser — Commentary

Takes a linted commentary file and produces API-ready JSON payloads for the edition, TOC, and root-text alignment.

Forked from `parser-root-text`. Content segments default to **`paragraph`** (not verse). Always emits `alignment.json` from Obsidian transclusions to the root text.

## What it does

Runs these functions from the commentary `.md` and its lint JSON:

1. **extract_text_input** — strips null/empty fields from the lint JSON and writes a clean `text.json`, named after the source file (includes `commentary_of` when present)
2. **build_edition** — extracts content, builds a segmented edition with character-level spans (`type: paragraph` for body), writes `edition.json`
3. **build_toc** — builds a nested table of contents from the source headings, writes `toc.json`
4. **build_alignment** — extracts segment-to-segment alignment from Obsidian transclusion links (`![[...#^ref]]`), writes `alignment.json`

## Output

```
output/
  <stem>/                          # one folder per source file
    <stem>.text.json        # clean text_input payload (with commentary_of, named after the source file)
    <stem>.edition.json     # edition content + segmentation (paragraph default)
    <stem>.toc.json         # nested TOC with character spans
    <stem>.alignment.json   # commentary↔root-text segment alignments
```

## Alignment / transclusion

Transclusion links in the commentary (`![[1-SOURCES/Text/pi-1.md#^1-585]]`) define which root-text segment each commentary segment corresponds to.

- `source_segment_reference` — segment in the commentary
- `target_segment_reference` — segment in the root text

A transclusion or consecutive group of transclusions opens an alignment scope.
Every following commentary paragraph aligns to that root-text block or group
until the scope ends. A scope ends at either:

- the next transclusion group, or
- any heading — commentary after a heading must carry its own transclusion to
  be aligned

Headings themselves are never aligned. Transclusions that target a heading in the
`root_text` file are skipped (headings are not segments); one warning lists them. Alignment may be many-to-one (several
commentary paragraphs gloss one root verse) or many-to-many (several
paragraphs discuss a transcluded verse group).

## Requirements

```
pip install PyYAML pyewts
```

Requires Python 3.8+.

## How to run

Run from the project root (`abhidhamma-rails/`):

```bash
python3 4-SYSTEM\scripts\parser-commentary\parser.py "1-SOURCES\Commentaries\pi-dhammasangani-atthakatha.md" "4-SYSTEM\scripts\linter-commentary\output\pi-dhammasangani-atthakatha.lint.json"
```

## Notes

- Run the linter first — the parser reads `commentary_of` and other resolved fields from the lint JSON
- Author contributions without a resolvable id are dropped with a warning; missing contributions are allowed
- Missing `alt_titles` is allowed (warning only)
- Blocks without a reference marker (`^ref`) are skipped with a warning
- Header refs may have any depth; content refs max `^n-n-n` (3 parts)
- Pure transclusion blocks (`![[...]]` only) are silently skipped from edition content — they feed alignment only
- Tibetan TOC titles in Wylie are auto-converted to Unicode
- Cleaned before parsing (the source file is never modified): `<small>…</small>` tags are dropped and the gloss text kept; non-breaking spaces become ordinary spaces
- A line of zero-width characters only counts as blank, so it does not split a block. The block is kept whole and a warning says its parts may each need their own block ID
- Headings deeper than level 6 (7 or more `#`) have `**` stripped from the TOC title, since Obsidian renders only six levels and people bold those to look like headings. Bold on levels 1–6 is left alone
- Transclusions written one after another form a single group, even when a blank line separates them. Anything else between them starts a new group
- Headings are TOC-only: they add no segment and no text to the edition `content` (no segment has type `title`). A TOC section spans from its heading's position in `content` to the next heading of the same or higher level (else the end of `content`); a heading followed directly by such a heading gets an empty span
