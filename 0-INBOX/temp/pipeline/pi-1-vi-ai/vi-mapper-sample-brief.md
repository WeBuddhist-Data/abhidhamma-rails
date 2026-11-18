# Brief: Pāli→Vietnamese keyword mapping, pi-1 (Dhammasaṅgaṇī): SAMPLE

Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write tools for files (write scripts with the Write tool, never via a shell redirect), PowerShell for commands, `python -I -X utf8`. Write ONLY inside 0-INBOX\temp\pipeline\pi-1-vi-ai\mapper-vi\. Never create files at the repo root or in a system temp folder. Do not touch 1-SOURCES\ or 4-SYSTEM\, do not edit the translation, never run git (not even git status), never write "seed". You cannot write report files for me: return your report as text.

This sample (preamble, 1-matika, 2-01) is what the user reviews before the remaining parts are mapped (one agent at a time). It sets the conventions the later agents copy.

## FORBIDDEN (copyrighted reference translation)
Never open, grep or search: 1-SOURCES\Translations\Vietnamese\vi-*.md, 0-INBOX\raw-data\vi-*, 0-INBOX\temp\pipeline\pi-1-vi\, pi-2-vi\, pi-3-4-vi\, pi-5-vi\, pi-6-vi\, pi-7-vi\, pi-1-th-vi\, vi-tools\. No folder-wide searches over 0-INBOX\temp\pipeline\, 1-SOURCES\ or AI_translation\.

## Read first
- AI_translation\skills\keyword-equivalence-mapper.md (the skill you execute).
- 0-INBOX\temp\pipeline\vietnamese-style.md (Vietnamese conventions, approved core terms, sati = «sự tỉnh thức»).
- The Russian map of this same book, the closest model of how pi-1 was handled (conventions for dhammā, samaye, compounds, fragments, particles, matrix item names, (no direct equivalent)): 0-INBOX\temp\pipeline\pi-1-ru\mapper-ru\ru-map-conventions.md, map_common_ru.py, map_sample_ru.py, 1-matika.mapped.md, 2-01-cittuppadakandam.mapped.md (read 30–40 lines of each mapped file). The Hindi equivalents: 0-INBOX\temp\pipeline\pi-1-ru\ref\hi-map-conventions.md, hi_map_common_hi.py. The English map AI_translation\english\pi-1-keywords-by-reference-pali-english-plain.md shows how each Pāli keyword was read.

## Per part (preamble, 1-matika, 2-01-cittuppadakandam)
- Keywords (Pāli): 0-INBOX\temp\pipeline\pi-1-vi-ai\mapper-vi\<part>.keywords.md, `[id] kw1, kw2, …`.
- Vietnamese translation: AI_translation\vietnamese\pi-1-vietnamese-plain-zeroshot_split_chapters\<part>.md (segments end with ^id). It is final (approved and harmonised); do not edit it.
- Pāli source, for context: AI_translation\pali\pi-1_split_chapters\<part>.md.
- Very helpful: the Vietnamese was generated from the Pāli by builder scripts with fixed phrase tables: 0-INBOX\temp\pipeline\pi-1-vi-ai\build_matika_vi.py, build_ch2_01_sample_vi.py, build_2-01_2-02_vi.py, vi-zeroshot-terms.md, vi-core-terms.md, notes-*.md. The consistency pass changed some strings afterwards (harmonise-log.tsv); the TRANSLATION FILE is the truth.
- Output: mapper-vi\<part>.mapped.md: the same lines, in the same order, with the same Pāli keywords in the same order, each written `pāli=tiếng Việt`.

## Also write (for the later agents)
- mapper-vi\vi-map-conventions.md: the conventions you settled, modelled on the Russian conventions file.
- mapper-vi\map_common_vi.py: shared tables (core terms, factor names, matrix items) and a presence check (every Vietnamese value found as written in that segment's Vietnamese, NFC, case-insensitive at the start of a sentence). Later agents will import it.
- mapper-vi\map_sample_vi.py: your mapping table plus per-segment overrides for the three parts.

## Rules (user-approved for the earlier maps, adapted to Vietnamese)
- **Find the Vietnamese in that segment.** For each keyword, the word or phrase in THAT segment's Vietnamese that carries its meaning, copied as it stands there.
- **Dictionary form (Vietnamese has no inflection):** give the phrase as the text writes it, but drop words that belong to the frame and not to the keyword: plural markers («các», «những»), the existential «có» of the counting lines, «là» of the predicate, sentence-initial capitals, punctuation. Keep nominalisers that are part of the term («sự tiếp xúc», «niềm tin», «lòng từ ái», «trạng thái …») exactly as the text uses them. Record the rule you settle for each of these in the conventions file.
- **Compounds and fragments:** keywords include whole compounds and their members (e.g. `cittamudutā`, `mudutā`, `citta`). Map each to the Vietnamese part that renders it (cittamudutā=sự mềm mại của tâm, mudutā=sự mềm mại, citta=tâm). A fragment that lost a negative prefix maps to the positive part.
- **Keep keywords exactly as given** (multiword, capitalised, odd forms). Never add, drop, merge or reorder.
- **No direct equivalent:** if there is none in that segment (the word appears only inside a variant bracket kept in Pāli, a particle has no Vietnamese word, or the keyword's own Vietnamese is absent), write `kw=(no direct equivalent)`.
- **Compare each segment for real.** The same Pāli word may map differently by context. Identical formulaic segments get identical mappings. A table plus per-segment overrides is fine, but only after you have read the segments; check presence by script and list exceptions with reasons.
- **No ", " inside a Vietnamese value** (it is the separator). Drop the comma or use " / ".

## Verify each part (replace PART); it must print `bad []`
```
python -I -X utf8 -c "import pathlib;d=pathlib.Path('0-INBOX/temp/pipeline/pi-1-vi-ai/mapper-vi');ch='PART';a=[l.split('] ',1) for l in (d/f'{ch}.keywords.md').read_text(encoding='utf-8').splitlines()];b=[l.split('] ',1) for l in (d/f'{ch}.mapped.md').read_text(encoding='utf-8').splitlines()];assert [x[0] for x in a]==[x[0] for x in b];bad=[i for (i,x),(_,y) in zip(a,b) if [k.strip() for k in x.split(', ')]!=[k.split('=',1)[0] for k in y.split(', ')]];print(ch,'lines',len(a),'bad',bad)"
```
(If PowerShell mangles the one-liner, put the same code in mapper-vi\verify_map_vi.py taking the part as an argument.) Plus your presence check (every Vietnamese value found in that segment's Vietnamese; exceptions listed with reasons).

## Report (under 400 words, as text)
Per part: line count, verifier result, number of (no direct equivalent), presence-check result. The main conventions you settled. 10–15 example mappings for review (a factor name, a compound and its members, a synonym-string word, a matrix item, a particle). Genuinely unclear mappings.
