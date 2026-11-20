# Brief: RAILS Vietnamese translation, plain audience, pi-2 (Vibhaṅga): SAMPLE

## Setup
- Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write/Edit tools for files (write scripts with the Write tool at full paths; never write any file from PowerShell, not even a temporary list), PowerShell for commands, `python -I -X utf8`.
- Write ONLY the outputs listed below plus helper scripts in 0-INBOX\temp\pipeline\pi-2-vi-ai\rails\. Never create files at the repo root or in a system temp folder. Do not touch 1-SOURCES\ or 4-SYSTEM\, do not edit any pi-1 file, never run git (not even git status), never write "seed" or "unseeded". You cannot write report files for me: return your report as text.
- This sample is what the user reviews before the rest of the book is translated. It sets every sentence formula the later agents will copy.

## FORBIDDEN
- The copyrighted reference translation: never open, grep or search 1-SOURCES\Translations\Vietnamese\ (any file), 0-INBOX\raw-data\vi-*, 0-INBOX\temp\pipeline\pi-1-vi\, pi-2-vi\, pi-3-4-vi\, pi-5-vi\, pi-6-vi\, pi-7-vi\, pi-1-th-vi\, vi-tools\. No web lookups of Vietnamese Abhidhamma translations.
- The Vietnamese zero-shot of THIS book (translate FRESH from the Pāli): AI_translation\vietnamese\pi-2-vietnamese-plain-zeroshot_split_chapters\, pi-2-vietnamese-plain-zeroshot.md, the zero-shot builders and notes in pi-2-vi-ai\ (build_*_vi.py, notes-*.md, ch1-sample.md, vi-zeroshot-terms.md, harmonise files, backup-pre-harmonise\, divergences*.md), and the Vietnamese side of the keyword maps (pi-2-vi-ai\mapper-vi\*.mapped.md, the assembled pi-2-keywords-by-reference-pali-vietnamese-plain.md).
- No folder-wide searches over 0-INBOX\temp\pipeline\, 1-SOURCES\ or AI_translation\.

## Read first
- AI_translation\skills\rails-verse-translator.md. Follow it.
- 0-INBOX\temp\pipeline\vietnamese-style.md: register, typography (“…” / ‘…’), the strict DASH RULE, structure, review lessons, core terms (sati = «sự tỉnh thức», never «chánh niệm»).
- **The approved Vietnamese pi-1 rails** (user-approved and reviewed; the Vibhaṅga repeats the Dhammasaṅgaṇī word for word in its Abhidhamma and question sections): AI_translation\vietnamese\pi-1-vietnamese-plain.md and pi-1-vietnamese-plain-rails_split_chapters\ (1-matika.md has every triad and pair name; 3-0x-rupakandam.md the matter lists), 0-INBOX\temp\pipeline\pi-1-vi-ai\rails\vi-rails-formulas.md and build_rails_sample_vi.py (constants; importing writes nothing). Where pi-2 has the same Pāli as pi-1, reuse the pi-1 Vietnamese unless the pi-2 termbase decides otherwise for that word; report each such difference. Find matches by grepping the Pāli in AI_translation\pali\pi-1_split_chapters\ and reading the same non-empty line in the pi-1 Vietnamese rails file.
- For how the Vibhaṅga sample is structured (meaning and layout only, never wording): the approved Russian pi-2 rails sample, 0-INBOX\temp\pipeline\pi-2-ru\rails\ru-rails-formulas.md and build_rails_sample_ru.py with its output AI_translation\russian\pi-2-russian-plain-rails_split_chapters\1-khandhavibhango.md; the English pi-2 rails AI_translation\english\pi-2-english-plain-rails_split_chapters\ (grep by block ID) for meaning.
- Where any model disagrees with the pi-2 Vietnamese termbase, the termbase wins.

## Inputs
- **Source:** AI_translation\pali\pi-2_split_chapters\<ch>.md
- **Locked termbase (authoritative, user-approved 2026-11-19):** AI_translation\vietnamese\pi-2-pali-vietnamese-termbase-plain.md, `pali: {english tag: tiếng Việt; …}`, plus 0-INBOX\temp\pipeline\pi-2-vi-ai\termbase\APPROVED.md (the user's decisions: cross-book terms aligned to pi-1; ṭhiti three senses; ^2-511 mokkhaṃ to be rendered as 'chief'; koṭi in millions) and the pi-1 decisions in 0-INBOX\temp\pipeline\pi-1-vi-ai\termbase\APPROVED.md.
  - Look up each Pāli word; pick the sense by its tag. Compounds and phrases often have their own entries; a compound without an entry is built from its members' entries.
  - Terms are in citation form: a noun term keeps its nominaliser where it stands as a noun; inside a compound phrase or as a modifier use the bare word; add or drop «các» / «những», «có», «là», tense words and classifiers as Vietnamese grammar needs. Never swap in a synonym.
  - If no sense fits, use the closest sibling entry and REPORT it.
- **Approved book frame (user, 2026-11-18; copy verbatim):** `# Abhidhammapiṭake` = «# Tạng Vi Diệu Pháp»; `## Vibhaṅgapāḷi` = «## Phân tích các hiện tượng». Chapter headings (### level): Khandhavibhaṅgo «Phân tích các khối»; Āyatanavibhaṅgo «Phân tích các lĩnh vực nhận biết»; Dhātuvibhaṅgo «Phân tích các yếu tố»; Saccavibhaṅgo «Phân tích các sự thật»; Indriyavibhaṅgo «Phân tích các năng lực»; Paṭiccasamuppādavibhaṅgo «Phân tích sự sinh khởi tùy thuộc vào điều kiện»; Satipaṭṭhānavibhaṅgo «Phân tích sự thiết lập tỉnh thức»; Sammappadhānavibhaṅgo «Phân tích các nỗ lực đúng đắn»; Iddhipādavibhaṅgo «Phân tích các nền tảng thần thông»; Bojjhaṅgavibhaṅgo «Phân tích các chi phần giác ngộ»; Maggaṅgavibhaṅgo «Phân tích các chi phần của con đường»; Jhānavibhaṅgo «Phân tích các tầng thiền»; Appamaññāvibhaṅgo «Phân tích các trạng thái không thể đo lường»; Sikkhāpadavibhaṅgo «Phân tích các điều tu học»; Paṭisambhidāvibhaṅgo «Phân tích các loại hiểu biết thông suốt»; Ñāṇavibhaṅgo «Phân tích các loại hiểu biết»; Khuddakavatthuvibhaṅgo «Phân tích các chủ đề nhỏ»; Dhammahadayavibhaṅgo «Phân tích cốt lõi của các hiện tượng». Section headings (#### level): Suttantabhājanīyaṃ «Phân tích theo kinh»; Abhidhammabhājanīyaṃ «Phân tích theo Vi Diệu Pháp»; Pañhāpucchakaṃ «Phần hỏi đáp» (the closing line repeats the heading with «.»). Counted questions end «… là những gì?». N-vidhena = «theo nhóm N» (e.g. «theo nhóm mười»), without «phân loại».
- **Audience:** AI_translation\audience_profile\plain.md

## What to produce
1. AI_translation\vietnamese\pi-2-vietnamese-plain-rails_split_chapters\preamble.md (source preamble.md; create the folder).
2. 0-INBOX\temp\pipeline\pi-2-vi-ai\rails\sample-1\1-sample.md: chapter 1 from its start through the line before `##### Vedanākkhandho ^2-1-2-2-0` (the first 77 non-empty Pāli lines; the Pāli slice is 0-INBOX\temp\pipeline\pi-2-vi-ai\ch1-sample-pali.md, a Pāli file you may read), with the same blank lines.
3. 0-INBOX\temp\pipeline\pi-2-vi-ai\rails\vi-rails-formulas.md: every recurring sentence formula and fixed string of the sample (the aggregate definition «Yaṃ kiñci rūpaṃ atītānāgatapaccuppannaṃ …», the past/future/present, internal/external, gross/subtle, inferior/superior, far/near definitions, the closing «ayaṃ vuccati …», the N-vidhena classification lines, the book frame, the 18 chapter headings, the section headings) as "Pāli = tiếng Việt", one per line. It becomes binding for the later agents. Mark each string taken unchanged from the pi-1 Vietnamese rails with "(pi-1)".
4. 0-INBOX\temp\pipeline\pi-2-vi-ai\rails\build_rails_sample_vi.py: builds 1–2 from fixed formula strings (Python constants the later agents can import; importing must not rewrite outputs: guard with `if __name__ == "__main__":`).

## Rules
- **Block IDs:** exact, at the end of the last line of each segment, in the same order.
- **Headings:** keep their #-level.
- **Segments:** each has the source's number of non-empty lines. One blank line between segments; no double blank lines.
- **DASH RULE (user):** "–" only where the Pāli has "–" or "—", same spot, same count on every line. Never add one; no ":-".
- **Punctuation:** "…pe…" becomes "…" (never «….»). Statements end with ".". Questions end with "?" and use a Vietnamese question word (gì, nào …). Quotes “…” / ‘…’.
- **Brackets:** "[khác chính tả (Sī.): …]" for spelling-only variants, "[dị bản (…): …]" otherwise; (Ka)/(Kha)/(Ga) → (a)/(b)/(c). Translate editorial notes. Follow the pi-1 Vietnamese rails for the exact bracket wording.
- **Translate the Pāli as written** (user rule): no emendations; only plain spelling slips may be rendered as meant. Report suspected slips.
- **Formulas:** identical Pāli gets identical Vietnamese, within the sample and with the pi-1 Vietnamese rails.
- **Readability for a plain reader:** the long lists and -pe- runs must read as natural Vietnamese sentences. Never leave a term sitting ungrammatically; recast a sentence where a literal string reads badly, while keeping every term. Avoid a doubled «là».

## Verify (all must pass)
```
python -I -X utf8 0-INBOX\temp\pipeline\check_chapter_ids.py AI_translation\pali\pi-2_split_chapters AI_translation\vietnamese\pi-2-vietnamese-plain-rails_split_chapters preamble.md
python -I -X utf8 0-INBOX\temp\pipeline\dashcheck.py <pali> <vietnamese>     (preamble, and pi-2-vi-ai\ch1-sample-pali.md vs rails\sample-1\1-sample.md)
python -I -X utf8 0-INBOX\temp\pipeline\pi-1-vi-ai\verify_rails_vi.py <pali> <vietnamese> [<pali> <vietnamese> …]     (the same two pairs)
```
Then termbase adherence: copy the sample with the Write tool into a scratch folder under pi-2-vi-ai\rails\ (e.g. rails\adh-sample\) named 1-khandhavibhango.md, together with preamble.md, and run
```
python -I -X utf8 0-INBOX\temp\pipeline\termbase_adherence_vi.py AI_translation\pali\pi-2-keywords-by-reference-pali-plain.md AI_translation\vietnamese\pi-2-pali-vietnamese-termbase-plain.md <that scratch folder>
```
Read the misses with judgement (gapped phrases, the nominaliser and classifiers cause false misses) and fix the genuine ones.

## Report (under 450 words, as text)
- Checks passed; segment counts; adherence results.
- 10–15 key formulas as "Pāli = tiếng Việt" (the aggregate definition, past/future/present, internal/external, gross/subtle, far/near, a classification line, the closing line, the section headings).
- Strings reused from the pi-1 Vietnamese rails and any place where the pi-2 termbase made you differ from pi-1.
- Termbase misfits (term, segment, why it does not fit, what you wrote) and terms the termbase lacks.
- Unsure Pāli or source slips.
