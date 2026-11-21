# Brief: RAILS Vietnamese translation, plain audience, pi-3 (Dhātukathā): SAMPLE

## Setup
- Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write/Edit tools for files (write scripts with the Write tool at full paths; never write any file from PowerShell, not even a temporary list), PowerShell for commands, `python -I -X utf8`.
- Write ONLY the outputs listed below plus helper scripts in 0-INBOX\temp\pipeline\pi-3-vi-ai\rails\. Never create files at the repo root or in a system temp folder. Do not touch 1-SOURCES\ or 4-SYSTEM\, do not edit any pi-1 / pi-2 file, never run git (not even git status), never write "seed" or "unseeded". No web. You cannot write report files for me: return your report as text.
- This sample (preamble, 1-uddeso, 2-pathamanayo) is what the user reviews before the rest of the book is translated (three agents at a time, one chapter each). It sets every sentence formula the later agents will copy.

## FORBIDDEN
- The copyrighted reference translation: never open, grep or search 1-SOURCES\Translations\Vietnamese\ (any file), 0-INBOX\raw-data\vi-*, 0-INBOX\temp\pipeline\pi-1-vi\, pi-2-vi\, pi-3-4-vi\, pi-5-vi\, pi-6-vi\, pi-7-vi\, pi-1-th-vi\, vi-tools\.
- The Vietnamese zero-shot of THIS book (translate FRESH from the Pāli): AI_translation\vietnamese\pi-3-vietnamese-plain-zeroshot_split_chapters\, pi-3-vietnamese-plain-zeroshot.md, and everything zero-shot in pi-3-vi-ai\ (build_*_vi.py, notes-*.md, vi-zeroshot-*.md, harmonise*, backup-pre-harmonise\, divergences*.md, find_divergences_vi.py, vi_common.py, probe_*.py, lookup_vi.py, merge_zeroshot_vi.py); and the Vietnamese side of the keyword maps (pi-3-vi-ai\mapper-vi\*.mapped.md, map_*_vi.py, notes-map-*.md, vi-map-conventions-pi3.md, crosscheck-values.tsv, and AI_translation\vietnamese\pi-3-keywords-by-reference-pali-vietnamese-plain.md).
- No folder-wide searches over 0-INBOX\temp\pipeline\, 1-SOURCES\ or AI_translation\: Grep only the specific files named here.

## Read first
- AI_translation\skills\rails-verse-translator.md. Follow it.
- 0-INBOX\temp\pipeline\vietnamese-style.md: register, typography (“…” / ‘…’), the strict DASH RULE, structure, review lessons, core terms (sati = «sự tỉnh thức», never «chánh niệm»).
- **The approved Vietnamese pi-1 and pi-2 rails** (user-approved and reviewed): AI_translation\vietnamese\pi-1-vietnamese-plain-rails_split_chapters\ (1-matika.md has every triad and dyad name), AI_translation\vietnamese\pi-2-vietnamese-plain-rails_split_chapters\ (the lists: aggregates, bases, elements, truths, faculties, dependent origination, satipaṭṭhāna …), their formula files 0-INBOX\temp\pipeline\pi-1-vi-ai\rails\vi-rails-formulas.md and 0-INBOX\temp\pipeline\pi-2-vi-ai\rails\vi-rails-formulas.md, and pi-2-vi-ai\rails\build_rails_sample_vi.py (constants; importing writes nothing). Where pi-3 has the same Pāli as pi-1 / pi-2, reuse their Vietnamese unless the pi-3 termbase decides otherwise for that word; report each such difference. Find matches by grepping the Pāli in AI_translation\pali\pi-1_split_chapters\ or pi-2_split_chapters\ and reading the same non-empty line in the Vietnamese rails file.
- For meaning and layout only (never wording): the Russian pi-3 rails AI_translation\russian\pi-3-russian-plain-rails_split_chapters\<ch>.md and 0-INBOX\temp\pipeline\pi-3\ru-rails-formulas.md; the English pi-3 rails AI_translation\english\pi-3-english-plain.md (grep by block ID).
- Where any model disagrees with the pi-3 Vietnamese termbase, the termbase wins.

## Inputs
- **Source:** AI_translation\pali\pi-3_split_chapters\<ch>.md
- **Locked termbase (authoritative, user-approved 2026-11-20):** AI_translation\vietnamese\pi-3-pali-vietnamese-termbase-plain.md, `pali: {english tag: tiếng Việt; …}`, plus 0-INBOX\temp\pipeline\pi-3-vi-ai\termbase\APPROVED.md (the user's decisions: nāsaññā «không phải không tri giác» (pi-1); labbhati «tìm thấy»; Samucchede written «sự phân tích»; the kāma / āyatana artefact uses the separate terms; ^3-447 as written) and the pi-1 / pi-2 decisions in 0-INBOX\temp\pipeline\pi-1-vi-ai\termbase\APPROVED.md and pi-2-vi-ai\termbase\APPROVED.md.
  - Look up each Pāli word; pick the sense by its tag. Compounds and phrases often have their own entries; a compound without an entry is built from its members' entries.
  - Terms are in citation form: a noun keeps its nominaliser where it stands as a noun; inside a compound phrase or as a modifier use the bare word; add or drop «các» / «những», «có», «là», «điều», «với», tense words and classifiers as Vietnamese grammar needs. Never swap in a synonym.
  - If no sense fits, use the closest sibling entry and REPORT it.
- **Approved book frame and headings (user, 2026-11-20; copy verbatim):**
  - `# Abhidhammapiṭake` = «# Tạng Vi Diệu Pháp»; `## Dhātukathāpāḷi` = «## Thảo luận về các yếu tố»; colophon «Bộ “Thảo luận về các yếu tố” đã hoàn tất.»; the book names in ^3-5: dhammasaṅgaṇī «“Liệt kê các hiện tượng”», dhātukathā «“Thảo luận về các yếu tố”».
  - Chapters (###): Uddeso «Phần nêu đề mục»; Paṭhamanayo … Cuddasamanayo «Phương pháp thứ nhất / thứ hai / thứ ba / thứ tư / thứ năm / thứ sáu / thứ bảy / thứ tám / thứ chín / thứ mười / thứ mười một / thứ mười hai / thứ mười ba / thứ mười bốn».
  - Ch1 sections (####): Nayamātikā «Ma trận các phương pháp»; Abbhantaramātikā «Ma trận bên trong»; Nayamukhamātikā «Ma trận lối vào các phương pháp»; Lakkhaṇamātikā «Ma trận các đặc tính»; Bāhiramātikā «Ma trận bên ngoài».
  - X-padaniddeso (####) = «Giải thích đề mục về X»; its closing line «Giải thích đề mục về X, phần thứ nhất.» (dutiyo … cuddasamo = phần thứ hai … phần thứ mười bốn). The 14 method names X: saṅgahāsaṅgaha «sự gộp vào và sự không gộp vào»; saṅgahitena asaṅgahitaṃ «điều không được gộp vào dựa trên điều được gộp vào» (and the other 12 in the same pattern: asaṅgahitena saṅgahitaṃ «điều được gộp vào dựa trên điều không được gộp vào», saṅgahitena saṅgahitaṃ, asaṅgahitena asaṅgahitaṃ; sampayogavippayoga «sự gắn liền và sự không gắn liền»; sampayuttena vippayuttaṃ «điều không gắn liền dựa trên điều gắn liền», vippayuttena sampayuttaṃ, sampayuttena sampayuttaṃ, vippayuttena vippayuttaṃ; saṅgahitena sampayuttaṃ vippayuttaṃ «điều gắn liền và điều không gắn liền dựa trên điều được gộp vào», sampayuttena saṅgahitaṃ asaṅgahitaṃ «điều được gộp vào và điều không được gộp vào dựa trên điều gắn liền», asaṅgahitena sampayuttaṃ vippayuttaṃ, vippayuttena saṅgahitaṃ asaṅgahitaṃ).
  - ##### sub-headings: Khandho «Các khối»; Āyatanaṃ «Các lĩnh vực nhận biết»; Dhātu «Các yếu tố»; Saccaṃ «Các sự thật»; Indriyaṃ «Các năng lực»; Paṭiccasamuppādādi «Sự sinh khởi tùy thuộc vào điều kiện và các mục khác»; Khandhādi «Các khối và các mục khác»; Saccādi «Các sự thật và các mục khác»; Phassādisattakaṃ «Nhóm bảy mục bắt đầu bằng sự tiếp xúc»; Tikaṃ «Bộ ba»; Dukaṃ «Bộ đôi».
  - Round labels: (Ekamūlakaṃ.) «(Phần xét từng mục một.)», (Dukamūlakaṃ.) «(Phần xét từng nhóm hai.)», (Tikamūlakaṃ.) «(Phần xét từng nhóm ba.)», (Catukkamūlakaṃ.) «(Phần xét từng nhóm bốn.)», (Pañcakaṃ.) «(Phần xét cả năm.)».
- **Audience:** AI_translation\audience_profile\plain.md

## What to produce
1. AI_translation\vietnamese\pi-3-vietnamese-plain-rails_split_chapters\preamble.md, 1-uddeso.md, 2-pathamanayo.md (create the folder).
2. 0-INBOX\temp\pipeline\pi-3-vi-ai\rails\vi-rails-formulas.md: every recurring sentence formula and fixed string of the sample (the katihi … saṅgahito? / asaṅgahito? question and answer, the counts, the na kehici frames, the asaṅkhataṃ khandhato ṭhapetvā clause, the list members, the round labels, headings) as "Pāli = tiếng Việt", one per line. ALSO propose, marked "(proposed for ch3-15)", the frames the later chapters need, built from the termbase: "Xena ye dhammā khandhasaṅgahena saṅgahitā …, te dhammā katihi … ?", "tehi dhammehi ye dhammā …", "X katihi … sampayutto? Natthi.", "kehici vippayutto" (read those Pāli chapters for their shape; Pāli files are allowed). It becomes binding for the later agents. Mark each string taken unchanged from pi-1 / pi-2 rails with "(pi-1)" / "(pi-2)".
3. 0-INBOX\temp\pipeline\pi-3-vi-ai\rails\build_rails_sample_vi.py: builds 1 from fixed formula strings (Python constants the later agents can import; importing must not rewrite outputs: guard with `if __name__ == "__main__":`). It asserts at build time that every (pi-1) / (pi-2) string still occurs in those rails files.

## Rules
- **Block IDs:** exact, at the end of the last line of each segment, in the same order.
- **Headings:** keep their #-level.
- **Segments:** each has the source's number of non-empty lines. One blank line between segments; no double blank lines.
- **DASH RULE (user):** "–" only where the Pāli has "–" or "—", same spot, same count on every line. Never add one; no ":-".
- **Punctuation:** "…pe…" becomes "…" (never «….»). Statements end with ".". Questions end with "?" and use a Vietnamese question word. Quotes “…” / ‘…’. Missing spaces after "(7)" etc. may be rendered as meant.
- **Brackets:** "[khác chính tả (Sī.): …]" for spelling-only variants, "[dị bản (…): …]" otherwise; follow the pi-1 / pi-2 Vietnamese rails for the exact bracket wording.
- **Translate the Pāli as written** (user rule): no emendations, add nothing that is not in the Pāli; only plain spelling slips may be rendered as meant. Report suspected slips.
- **Formulas:** identical Pāli gets identical Vietnamese, within the sample and with the pi-1 / pi-2 Vietnamese rails.
- **Readability for a plain reader:** the long lists and -pe- runs must read as natural Vietnamese sentences; recast where a literal string reads badly, keeping every term. Avoid a doubled «là» or «được được».

## Verify (all must pass)
```
python -I -X utf8 0-INBOX\temp\pipeline\check_chapter_ids.py AI_translation\pali\pi-3_split_chapters AI_translation\vietnamese\pi-3-vietnamese-plain-rails_split_chapters <file>.md
python -I -X utf8 0-INBOX\temp\pipeline\dashcheck.py <pali> <vietnamese>
python -I -X utf8 0-INBOX\temp\pipeline\pi-1-vi-ai\verify_rails_vi.py <pali> <vietnamese>
```
for preamble.md, 1-uddeso.md, 2-pathamanayo.md. Then termbase adherence:
```
python -I -X utf8 0-INBOX\temp\pipeline\termbase_adherence_vi.py AI_translation\pali\pi-3-keywords-by-reference-pali-plain.md AI_translation\vietnamese\pi-3-pali-vietnamese-termbase-plain.md AI_translation\vietnamese\pi-3-vietnamese-plain-rails_split_chapters
```
Read the misses with judgement (gapped phrases, nominalisers, the āyatanehi + numeral artefacts cause false misses) and fix the genuine ones.

## Report (under 450 words, as text)
- Checks passed; segment counts; adherence results.
- 10-15 key formulas as "Pāli = tiếng Việt", and the proposed frames for ch3-15.
- Strings reused from pi-1 / pi-2 rails and any place where the pi-3 termbase made you differ.
- Termbase misfits (term, segment, why it does not fit, what you wrote) and terms the termbase lacks.
- Unsure Pāli or source slips.
