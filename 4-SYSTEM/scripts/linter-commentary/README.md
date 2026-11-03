# Linter — Commentary

Validates vault commentary files (`.md`) and produces a structured JSON payload ready for the API.

Forked from `linter-root-text`. Content segments are treated as **paragraphs** (not verses). The distinguishing field is **`commentary_of`**, resolved from the linked root text.

## What it does

1. Reads the YAML frontmatter from the commentary `.md` file
2. Requires `file_type: commentary` and `root_text`
3. Validates required fields (`title`, `language`, `license`, `category_id`, `source`/`source_url`, etc.). Author is optional for now — missing ones produce a warning
4. Reads the author from the frontmatter. A person without `[bdrc:ID]` or `[op:ID]` is skipped with a warning — no API name lookups
5. Uses `title` and `alt_titles` from the YAML frontmatter as-is (no BDRC work search)
6. Auto-resolves **`commentary_of`** from the root text's `text_id` (via `root_text` path)
7. Copies `category_id` from the root text when missing
8. Patches the source file in place for fields that can be auto-resolved (`lang_tag`, `language`, `commentary_of`, `category_id`), never overwriting an existing value, and renames a `source_url` field to `source`
9. Validates edition segmentation refs and TOC heading structure
10. Writes output to `output/<stem>.lint.json` on success, or `output/<stem>.lint.errors.json` on failure

## Output

```
output/
  <stem>.lint.json          # on success — contains text_input payload
  <stem>.lint.errors.json   # on failure — contains errors and notes
```

The `text_input` block in the output is what gets submitted to the API to create a text. It includes `commentary_of` when the root text has a `text_id`.

## Files

| File | Role |
|------|------|
| `lint_text_input.py` | Entry point — reads source file, runs validation, writes output |
| `build.py` | Builds the `text_input` payload from validated data |
| `validate.py` | Field-level validation rules (commentary-specific) |
| `lookup.py` | Person lookups via API / BDRC — no longer used by anything |
| `constants.py` | API endpoints, allowed values, field lists |
| `languages.py` | Auto-generated language code/name mappings |
| `requirements.txt` | Python dependencies |

## Requirements

```
pip install -r requirements.txt
```

Requires Python 3.8+.

## How to run

Run from the project root (`abhidhamma-rails/`):

```bash
python3 4-SYSTEM\scripts\linter-commentary\lint_text_input.py "1-SOURCES\Commentaries\pi-dhammasangani-atthakatha.md"
```

Then parse:

```bash
python3 4-SYSTEM\scripts\parser-commentary\parser.py "1-SOURCES\Commentaries\pi-dhammasangani-atthakatha.md" "4-SYSTEM\scripts\linter-commentary\output\pi-dhammasangani-atthakatha.lint.json"
```

## Source file format

See `4-SYSTEM/Templates/FILE_YAML_PROPERTIES.md` §3 (Commentary).

Minimum linkage:

```yaml
file_type: commentary
root_text: 1-SOURCES/Text/pi-1.md
# commentary_of: <auto-filled from root text_id>
# category_id: <copied from root if missing>
```

## Notes

- Set `text_id` on the root text first — otherwise `commentary_of` cannot be resolved (WARN, not ERROR)
- Accepts `source` or `source_url` for the edition URL (tipitaka.org exports use `source_url`); `source_url` is renamed to `source` in the frontmatter, and the payload always uses `source`
- Contributors are read from the frontmatter only — there are no name lookups against the API. A person needs `[bdrc:ID]` or `[op:ID]` after their name; without one they are skipped with a warning naming the role and the person. `rails`, or a bare `[op:ID]` with no name, counts as an AI contributor
- The API base is one constant in `constants.py` (`https://library.webuddhist.com/v2/`) and can be overridden with the `VAULT_API_BASE` environment variable. Languages come from `/v2/languages` (fetched once at start, with a saved copy used when the network is unavailable)
- Tibetan titles in Wylie are auto-converted to Unicode in the output
- `title` and `alt_titles` are keyed with the plain language code (`lang_tag`, or the resolved `language` if `lang_tag` is not set), e.g. `sa`, `pi`, and kept in whatever script they are written in. Script-suffixed keys of a known language (`sa-x-iast`, `pi-x-iast`) are reduced to the base code
- Pali (`pi`) title/alt text must be Roman script: any non-Latin letter is an ERROR (dict entries with a `pi…` key are checked too)
- Header refs may have any depth (`^n-n-n-…`); content refs max `^n-n-n` (3 parts)
- Pure transclusion blocks (`![[...]]` only) are skipped during segmentation validation — they are for alignment
- After the text, edition, and TOC are created in the API, save the returned IDs back as `text_id`, `edition_id`, and `toc_id`
