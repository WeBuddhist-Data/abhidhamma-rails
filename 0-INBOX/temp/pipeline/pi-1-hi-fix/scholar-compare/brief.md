# Brief: compare the Hindi pi-1 with the scholar version (Mātikā)

The only scholar version of the Dhammasaṅgaṇī in the vault is an English scholarly translation of the Mātikā. It is `pali-english/en-dhammasangani-ai-auto-scholarly-1.md`, made with the scholarly profile (`pali-english/audience_requirments/skills/audience_scholarly.md`) and the scholarly termbase (`pali-english/audience_requirments/termbase/termbase-pi-1-audience_scholarly.md`). The Hindi is the plain version (`AI_translation/audience_profile/plain.md`).

Task: for each of the 164 Mātikā lines, check whether the Hindi says **the same thing** as the scholar version. Where they differ, decide from the Pāli which is right. This is read-only: change no translation file, and write only your output file.

## Input

`scholar-compare/side-by-side.jsonl`: one line per Mātikā entry (`ref` is the vault's Pāli ID, `en_ref` the English file's ID), with fields `pali`, `english_scholarly` and `hindi`. Read it in parts of about 40 lines.

You may consult:
- the scholarly termbase (to see the intended English sense of a term);
- the vault's commentary `1-SOURCES/Commentaries/pi-dhammasangani-atthakatha.md` (the Mātikā is explained at the start);
- the Hindi termbase `AI_translation/hindi/pi-1-pali-hindi-termbase-plain.md`.

## Verdict per line

| Verdict | When |
|---|---|
| `SAME` | The same meaning, and the same distinctions (wording may differ) |
| `PLAINER` | The same meaning, but the Hindi uses an everyday word or explanation where the scholar version uses the technical term (expected: plain.md). Say which term |
| `DIFFERS-HINDI` | The meaning differs, and the Pāli supports the scholar version: the Hindi needs a fix. Give the fix |
| `DIFFERS-ENGLISH` | The meaning differs, and the Pāli supports the Hindi: the scholar version is the one that is off |
| `DIFFERS-BOTH-OK` | Different readings, both defensible from the Pāli or commentary. Say what each takes |
| `MISSING` / `ADDED` | One side drops or adds something the Pāli has or lacks |

Be strict about meaning and distinctions (for example *sappaccaya* / *saṅkhata*, *sanidassana* / *sappaṭigha*, *upādinna* / *upādāniya*, *āsava* / *sāsava*, *hetu* / *sahetuka*). Don't count register or style differences as differences: that is `PLAINER`.

## Output

`scholar-compare/compare-hi.md`:

1. **Summary:** the count per verdict, and a short answer to "does the Hindi say the same as the scholar version?"
2. **Table, every line:** ref | verdict | Pāli (short) | English scholarly (short) | Hindi (short) | note.
3. **Fixes needed in the Hindi** (only `DIFFERS-HINDI` / `MISSING` / `ADDED` on the Hindi side), each with the Pāli justification.
4. **Points where the scholar version itself is off** (`DIFFERS-ENGLISH`).

At the end, reply with only: the counts per verdict, and every `DIFFERS-HINDI`, `MISSING` or `ADDED` line (one line each), plus the 5 most important `PLAINER` terms.
