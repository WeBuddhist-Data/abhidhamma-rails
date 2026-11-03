# pi-2 English translation — Pecha backend upload

Uploaded 2026-07-30. API base `https://api-aq25662yyq-uc.a.run.app` (production, from
`https://pecha-backend.web.app/config.json`). OpenAPI schema: `GET /v2/schema/openapi` (YAML, not JSON).

## IDs

| what | id |
|---|---|
| source instance (Vibhaṅgapāḷi, pi) | `3HyZUpbWixfrK8H7AuvNJ` |
| source segmentation annotation | `Ik067WBYtqXf5NOgtbPri` (1740 segments) |
| **translation instance (en)** | **`aOI5oGDYWg6XSs5YD4myb`** |
| translation text record | `K0vEdHUX3VTi6wrx7yAae` |
| translation segmentation annotation | `6UMd6RyWzC3k1DdyAkUZb` (1740 segments) |
| alignment annotation (source side) | `g7a3ZKeNbSZbPSm7NsoaA` |
| alignment annotation (target side) | `svDS1bzxyZGqOlueT4vMj` |

## Requests made

1. `POST /v2/instances/3HyZUpbWixfrK8H7AuvNJ/translation` — body `01-translation.json` → 201
2. `POST /v2/annotations/3HyZUpbWixfrK8H7AuvNJ/annotation` — body `02-alignment.json` → 201
   (`instance_id` in the path is the **source**; the target goes in `target_manifestation_id`)

## Metadata sent

- `language` `en`
- `title` `Vibhaṅgapāḷi-AI`
- `author` `{"person_bdrc_id": "P7326"}` — Śākyamuni, the author already on the root text record `l3cscHreTKjoUj14mUb72`
- `copyright` `Public domain` · `license` `CC BY-NC`
- `source` — descriptive string naming the zero-shot plain-audience run

## How the content was segmented

Content is [pi-2-english-plain-zeroshot.md](../english/pi-2-english-plain-zeroshot.md), re-segmented to
match the source instance exactly.

The markdown files carry 1543 blocks; the backend stores 1740 segments. The backend splits some blocks
further and joins multi-line blocks with ` ⤵ ` (U+2935 RIGHT ARROW WITH DOWNWARDS BASE, space either
side). Splitting every backend segment on that marker yields 3427 sub-lines — exactly the line count of
[pi-2.md](../../1-SOURCES/Text/pi-2.md). So the mapping is backend line → Pāli md line → English md line,
re-emitted grouped and ordered the backend's way.

Consequences worth knowing:

- The three summary gāthās the backend hoists above the prose they close sit in the **backend's**
  position here, not the markdown's. That keeps the alignment monotonic, index for index.
- `⤵` in the English is not authored content — it is inserted at exactly the positions where the
  corresponding Pāli segment has one, so both sides break lines identically (1687 in each).
- Paragraph numbers (`768. `) are stripped from content, as the backend does; heading numbers (`1. `)
  are kept and taken from the Pāli heading. Headings keep the source's own `<hN>` level.
- Block `2-768` was the one place the English collapsed two Pāli lines into one; it is split at the
  question mark so line counts agree.

## Verification

`build.py` / `payloads.py` in the session scratchpad assert all of it; 23 checks passed before upload:
counts 1740 across all four annotations, spans ordered and non-overlapping, source alignment spans
byte-identical to `Ik067WBYtqXf5NOgtbPri`, per-segment `⤵` parity, heading indices/levels identical, no
markdown artefacts. After upload: stored content byte-identical to what was sent, stored spans equal to
what was sent, and all 1740 source entries resolve to exactly one target segment with 0 mis-links.
