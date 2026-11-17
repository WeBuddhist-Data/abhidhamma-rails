# Brief: RAILS Russian translation, plain audience, pi-2 (Vibhaṅga): SAMPLE

## Setup
- Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write tools for files (write scripts with the Write tool, never via a shell redirect), PowerShell for commands, `python -I -X utf8`.
- Write ONLY the outputs listed below plus helper scripts in 0-INBOX\temp\pipeline\pi-2-ru\rails\. Never create files at the repo root or in a system temp folder. Do not touch 1-SOURCES\ or 4-SYSTEM\, do not edit any pi-1 file, do not run git, never write "seed" or "unseeded". You cannot write report files for me: return your report as text.
- This sample is what the user reviews before the rest of the book is translated. It sets every sentence formula the later agents will copy.

## Read first
- AI_translation\skills\rails-verse-translator.md. Follow it.
- 0-INBOX\temp\pipeline\russian-style.md: register, typography («…»/„…“, no «ли»), the strict DASH RULE, structure.
- Translate FRESH from the Pāli, consulting the locked termbase term by term.
- Do NOT open the Russian pi-2 zero-shot (AI_translation\russian\pi-2-russian-plain-zeroshot_split_chapters\, pi-2-russian-plain-zeroshot.md), the zero-shot builders and notes in pi-2-ru\ (build_*_ru.py and notes-*.md in the pi-2-ru folder itself, ch1-sample.md, harmonise files) or the Russian side of the keyword maps (pi-2-ru\mapper-ru\*.mapped.md, pi-2-keywords-by-reference-pali-russian-plain.md).
- You MAY open (they are not the zero-shot): pi-2-ru\ru-zeroshot-terms.md only for the book title and the 18 chapter headings the user approved (book title «Подробный разбор»; keep those headings), and pi-2-ru\termbase\APPROVED.md.
- Models of house style and shared passages:
  - **The approved Russian pi-1 rails** (the Vibhaṅga repeats the Dhammasaṅgaṇī word for word in its Abhidhamma and question sections): AI_translation\russian\pi-1-russian-plain.md and pi-1-russian-plain-rails_split_chapters\, especially 1-matika.md (every triad and pair name), and 0-INBOX\temp\pipeline\pi-1-ru\rails\ru-rails-formulas.md with build_rails_sample_ru.py (constants; importing writes nothing). Where pi-2 has the same Pāli as pi-1, reuse the pi-1 Russian unless the pi-2 termbase decides otherwise for that word; report each such difference.
  - The finished Russian rails of other books (AI_translation\russian\pi-3-russian-plain.md, pi-4-…, pi-5-…).
  - For how the Vibhaṅga sample is structured: the Hindi pi-2 rails sample builder, formulas and brief, restored to 0-INBOX\temp\pipeline\pi-2-ru\ref\ (hi_rails_build_rails_sample.py, hi_rails_hi-rails-formulas.md, hi_hi-rails-brief.md; hi_rails_build_rails_1.py is the Hindi rest of chapter 1).
  - Where any model disagrees with the pi-2 Russian termbase, the termbase wins.

## Inputs
- **Source:** AI_translation\pali\pi-2_split_chapters\<ch>.md
- **Locked termbase (authoritative, user-approved 2026-11-17):** AI_translation\russian\pi-2-pali-russian-termbase-plain.md, `pali: {english tag: русский; …}`, plus 0-INBOX\temp\pipeline\pi-2-ru\termbase\APPROVED.md (the user's fix: ajjhattaṃ / bahiddhā «внутренний» / «внешний»; and its "For the rails step" notes: rūpataṇhā has two meanings, «жажда видимых форм» in the sense-object lists and «жажда мира форм» for the fine-material sphere; upapattidevā; the dictionary-form infinitives).
  - Look up each Pāli word; pick the sense by its tag. Compounds and phrases often have their own entries; a compound without an entry is built from its members' entries.
  - Inflect grammatically (case, number, gender, verb agreement, short/long adjective), but never swap in a synonym. Terms are in dictionary form.
  - If no sense fits, use the closest sibling entry and REPORT it.
- **Approved earlier decisions (user):** N-vidhena = «на два вида», «по одному», «на десять видов» … WITHOUT «классификация» (dasavidhena rūpakkhandho = «совокупность материальной формы на десять видов»); niyaka = «закреплённый» (pi-1).
- **Audience:** AI_translation\audience_profile\plain.md

## What to produce
1. AI_translation\russian\pi-2-russian-plain-rails_split_chapters\preamble.md (source preamble.md). The folder exists and is empty.
2. 0-INBOX\temp\pipeline\pi-2-ru\rails\sample-1\1-sample.md: chapter 1 from its start through ^2-33 (the first 77 non-empty Pāli lines; the Pāli slice is 0-INBOX\temp\pipeline\pi-2-ru\ch1-sample-pali.md, the same slice the Hindi sample used).
3. 0-INBOX\temp\pipeline\pi-2-ru\rails\ru-rails-formulas.md: every recurring sentence formula and fixed string of the sample (the aggregate definition «Yaṃ kiñci rūpaṃ atītānāgatapaccuppannaṃ …», the past/future/present, internal/external, gross/subtle, inferior/superior, far/near definitions, the closing «ayaṃ vuccati …», the N-vidhena classification lines, the chapter headings of all 18 chapters, the section headings Suttantabhājanīyaṃ / Abhidhammabhājanīyaṃ / Pañhāpucchakaṃ) as "Pāli = Russian", one per line. It becomes binding for the later agents. Mark each string taken unchanged from pi-1 with "(pi-1)".
4. 0-INBOX\temp\pipeline\pi-2-ru\rails\build_rails_sample_ru.py: builds 1-2 from fixed formula strings (Python constants the later agents can import; importing must not rewrite outputs: guard with `if __name__ == "__main__":`).

## Rules
- **Block IDs:** exact, at the end of the last line of each segment, in the same order.
- **Headings:** keep their #-level.
- **Segments:** each has the source's number of non-empty lines. One blank line between segments; no double blank lines.
- **DASH RULE (user):** "–" only where the Pāli has "–" or "—", same spot, same count on every line. Never add one; no ":-".
- **Punctuation:** "…pe…" becomes "…". Statements end with ".". Questions end with "?", never with «ли». Quotes «…» / „…“.
- **Brackets:** «[вариант написания (Sī.): …]» for spelling-only variants, «[вариант чтения (…): …]» otherwise; (Ka)/(Kha)/(Ga) → (а)/(б)/(в). Translate editorial notes. Follow the pi-1 Russian rails for the exact bracket wording.
- **Translate the Pāli as written** (user rule): no emendations; only plain spelling slips may be rendered as meant. Report suspected slips.
- **Formulas:** identical Pāli gets identical Russian.
- **Readability for a plain reader:** the long lists and -pe- runs must read as Russian sentences. Never leave a term sitting ungrammatically; recast a sentence where a literal string reads badly, while keeping every term.

## Verify (all must pass)
```
python -I -X utf8 0-INBOX\temp\pipeline\dashcheck.py AI_translation\pali\pi-2_split_chapters\preamble.md AI_translation\russian\pi-2-russian-plain-rails_split_chapters\preamble.md
python -I -X utf8 0-INBOX\temp\pipeline\dashcheck.py 0-INBOX\temp\pipeline\pi-2-ru\ch1-sample-pali.md 0-INBOX\temp\pipeline\pi-2-ru\rails\sample-1\1-sample.md
python -I -X utf8 0-INBOX\temp\pipeline\pi-1-ru\verify_ru.py 0-INBOX\temp\pipeline\pi-2-ru\ch1-sample-pali.md 0-INBOX\temp\pipeline\pi-2-ru\rails\sample-1\1-sample.md
```
plus a check that the block IDs of 1-sample.md and preamble.md equal those of their Pāli, in order, with the same non-empty line count per segment; no «ли», no Latin outside variant brackets, no double blank lines, no CR, no em dash. Then termbase adherence: copy the sample into a scratch folder under pi-2-ru\rails\ named 1-khandhavibhango.md (with preamble.md) and run
```
python -I -X utf8 0-INBOX\temp\pipeline\termbase_adherence.py AI_translation\pali\pi-2-keywords-by-reference-pali-plain.md AI_translation\russian\pi-2-pali-russian-termbase-plain.md <that scratch folder>
```
Read the misses with judgement (inflection and split phrases cause false misses) and fix the genuine ones.

## Report (under 450 words, as text)
- Checks passed; segment counts; adherence results.
- 10–15 key formulas as "Pāli = Russian" (the aggregate definition, past/future/present, internal/external, gross/subtle, far/near, a classification line, the closing line, the section headings).
- Strings reused from pi-1 and any place where the pi-2 termbase made you differ from pi-1.
- Termbase misfits (term, segment, why it does not fit, what you wrote) and terms the termbase lacks.
- Unsure Pāli or source slips.
