# Linter — Root Text

Validates vault source files (`.md`) and produces a structured JSON payload ready for the API.

## What it does

1. Reads the YAML frontmatter from the source `.md` file
2. Validates required fields (`title`, `language`, `license`, `category_id`, `source`, `edition_type`, etc.). Author/translator are optional for now — missing ones produce a warning
3. Reads author/translator from the frontmatter. A person without `[bdrc:ID]` or `[op:ID]` is skipped with a warning — no API name lookups
4. Uses `title` and `alt_titles` from the YAML frontmatter as-is (no BDRC work search)
5. For translation files, auto-resolves `translation_of` from the root text's `text_id`
6. For commentary files, auto-resolves `commentary_of` from the root text's `text_id`
7. Patches the source file in place for fields that can be auto-resolved (`lang_tag`, `language`, `translation_of`, `category_id`), never overwriting an existing value, and renames a `source_url` field to `source`
8. Writes output to `output/<stem>.lint.json` on success, or `output/<stem>.lint.errors.json` on failure

## Output

```
output/
  <stem>.lint.json          # on success — contains text_input payload
  <stem>.lint.errors.json   # on failure — contains errors and notes
```

The `text_input` block in the output is what gets submitted to the API to create a text.

## Files

| File | Role |
|------|------|
| `lint_text_input.py` | Entry point — reads source file, runs validation, writes output |
| `build.py` | Builds the `text_input` payload from validated data |
| `validate.py` | Field-level validation rules |
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
python3 4-SYSTEM\scripts\linter-root-text\lint_text_input.py "1-SOURCES\Text\pi-1.md"
```

## Source file format

See `4-SYSTEM/Templates/FILE_YAML_PROPERTIES.md` for the required YAML properties for each file type (`root-text`, `translation`, `commentary`).

## Notes

- Tibetan titles in Wylie romanization (e.g. `kun dpal spyod 'jug`) are auto-converted to Unicode in the output
- `title` must be set in the YAML. `alt_titles` is optional for now (warning if missing). Neither is looked up from BDRC
- `alt_titles` are variants in the **same language** as the file (`lang_tag`). Use a string or a list of strings; each is keyed with the file's language code for the API:

  ```yaml
  lang_tag: sa
  title: bodhisattvacaryāvatāra
  alt_titles:
    - Bodhi(sattva)caryāvatāra
    - bodhicaryāvatāra
  ```

  → `title: {"sa": "bodhisattvacaryāvatāra"}`, `language: "sa"` (Sanskrit may be IAST or Devanagari)
- `title` and `alt_titles` are keyed with the plain language code (`lang_tag`, or the resolved `language` if `lang_tag` is not set), e.g. `sa`, `pi`, and kept in whatever script they are written in. Script-suffixed keys of a known language (`sa-x-iast`, `pi-x-iast`) are reduced to the base code
- Pali (`pi`) title/alt text must be Roman script: any non-Latin letter is an ERROR (dict entries with a `pi…` key are checked too)
- Contributors are read from the frontmatter only — there are no name lookups against the API. A person needs `[bdrc:ID]` or `[op:ID]` after their name; without one they are skipped with a warning naming the role and the person. `rails`, or a bare `[op:ID]` with no name, counts as an AI contributor
- The API base is one constant in `constants.py` (`https://library.webuddhist.com/v2/`) and can be overridden with the `VAULT_API_BASE` environment variable. Languages come from `/v2/languages` (fetched once at start, with a saved copy used when the network is unavailable)
- Accepts `source` or `source_url` for the edition URL; `source_url` is renamed to `source` in the frontmatter, and the payload always uses `source`
- If `bdrc_work_id` (or `bdrc`) is set in the YAML, it is passed through to the API payload as `bdrc`; it is never resolved by title search
- Header refs may have any depth (`^n-n-n-…`); content refs (verse / top / front / back) max `^n-n-n` (3 parts)
- The source file title is never overwritten by the linter
- After the text, edition, and TOC are created in the API, save the returned IDs back to the source file as `text_id`, `edition_id`, and `toc_id`
