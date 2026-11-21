# Brief: Vietnamese zero-shot of pi-3 (Dhātukathā), ONE chapter

Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write tools for files (write scripts with the Write tool at their full paths, never via a shell redirect), PowerShell for commands, `python -I -X utf8`. Write ONLY your own chapter file in the output folder, plus `build_<N>_vi.py` and `notes-<N>.md` (N = your chapter number) inside 0-INBOX\temp\pipeline\pi-3-vi-ai\. Never create files at the repo root or in a system temp folder. Do not touch 1-SOURCES\ or 4-SYSTEM\, do not edit any other file (other agents' chapters, builders and notes, the sample, the terms file), never run git (not even git status), never write "seed" or "unseeded" in any file. No web access. You cannot write report files for me: return your report as text.

The user approved the sample (preamble, 1-uddeso, 2-pathamanayo) on 2026-11-20, with the book title «Thảo luận về các yếu tố». **Three agents work at the same time, one chapter each.** You cannot see the other agents' work, so use the sample and the SHARED FRAMES below exactly; a later harmonise pass reconciles anything else.

## FORBIDDEN (copyrighted reference translation)
Never open, grep or search: 1-SOURCES\Translations\Vietnamese\ (any file), 0-INBOX\raw-data\vi-*, 0-INBOX\temp\pipeline\pi-1-vi\, pi-2-vi\, pi-3-4-vi\, pi-5-vi\, pi-6-vi\, pi-7-vi\, pi-1-th-vi\, vi-tools\. No web lookups. No folder-wide searches over 0-INBOX\temp\pipeline\, 1-SOURCES\ or AI_translation\: Grep only the specific files named here.

## Read first (binding)
- 0-INBOX\temp\pipeline\vietnamese-style.md: style, DASH RULE, “…” / ‘…’, core terms, verify commands.
- 0-INBOX\temp\pipeline\pi-3-vi-ai\vi-zeroshot-terms.md (READ-ONLY): book title, all chapter and sub-section headings (the padaniddeso headings and closing lines), the list-member names, counts, frames and terms. Copy them verbatim.
- The approved sample and its builder (READ-ONLY; import, do not edit): AI_translation\vietnamese\pi-3-vietnamese-plain-zeroshot_split_chapters\1-uddeso.md, 2-pathamanayo.md, built by 0-INBOX\temp\pipeline\pi-3-vi-ai\build_sample_vi.py (`sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-3-vi-ai"); import build_sample_vi as B`). Importing writes nothing. Its constants give every list member (aggregates, bases, elements, truths, faculties, dependent-origination links, the triad/dyad names from pi-1), the counts in Vietnamese words and the saṅgaha question/answer frames. pi-3-vi-ai\lookup_vi.py prints the pi-1 / pi-2 Vietnamese line for a Pāli search.
- Cross-book Vietnamese (user-approved, reviewed): pi-1 and pi-2 rails (AI_translation\vietnamese\pi-1-vietnamese-plain-rails_split_chapters\, pi-2-vietnamese-plain-rails_split_chapters\), termbases (AI_translation\vietnamese\pi-1-pali-vietnamese-termbase-plain.md, pi-2-pali-vietnamese-termbase-plain.md) and the user's decisions (0-INBOX\temp\pipeline\pi-1-vi-ai\termbase\APPROVED.md, pi-2-vi-ai\termbase\APPROVED.md). Any list item not in the sample builder: take it from there.
- AI_translation\skills\zeroshot-translator.md and AI_translation\audience_profile\plain.md.
- Cross-check of meaning and structure only (translate FROM THE PĀLI): AI_translation\english\pi-3-english-plain.md and AI_translation\russian\pi-3-russian-plain-rails_split_chapters\<ch>.md (find segments by block ID); 0-INBOX\temp\pipeline\pi-3\ru-zeroshot-terms.md, ru-rails-formulas.md.

## SHARED FRAMES (coordinator; all parallel agents use these exactly)
- Relative clause, instrumental of relation: "Xena / Xāya ye dhammā …" = «Đối với X, những hiện tượng nào …». In a chain "Aena ye dhammā… Bena ye dhammā… Cena ye dhammā [predicate]" = «Đối với A, những hiện tượng nào… đối với B, những hiện tượng nào… đối với C, những hiện tượng nào [predicate]» (first «Đối» capitalised only at sentence start).
- Inclusion modifiers: khandhasaṅgahena saṅgahitā / asaṅgahitā = «được gộp vào / không được gộp vào theo cách gộp vào khối»; āyatanasaṅgahena … = «… theo cách gộp vào lĩnh vực nhận biết»; dhātusaṅgahena … = «… theo cách gộp vào yếu tố». Joined with commas in the Pāli order: «được gộp vào theo cách gộp vào khối, không được gộp vào theo cách gộp vào lĩnh vực nhận biết, không được gộp vào theo cách gộp vào yếu tố».
- Association in a relative clause: "Xena ye dhammā sampayuttā / vippayuttā" = «Đối với X, những hiện tượng nào gắn liền với nó / không gắn liền với nó».
- Second relative: "tehi dhammehi ye dhammā …" = «đối với những hiện tượng ấy, những hiện tượng nào …» (with sampayuttā / vippayuttā: «gắn liền với chúng / không gắn liền với chúng»).
- Main clause: ", te dhammā katihi khandhehi katihāyatanehi katihi dhātūhi asaṅgahitā?" = «, thì những hiện tượng đó không được gộp vào bao nhiêu khối, bao nhiêu lĩnh vực nhận biết, bao nhiêu yếu tố?»; with saṅgahitā «được gộp vào bao nhiêu …?»; with sampayuttā «gắn liền với bao nhiêu khối, bao nhiêu lĩnh vực nhận biết, bao nhiêu yếu tố?»; with vippayuttā «không gắn liền với bao nhiêu …?».
- Answer: "Te dhammā catūhi khandhehi … asaṅgahitā." = «Những hiện tượng đó không được gộp vào bốn khối, …». The …pe… shortened answers ("…pe… te dhammā …") = «… những hiện tượng đó …».
- Direct association question: "X katihi khandhehi katihāyatanehi katihi dhātūhi sampayuttoti? Natthi." = «X gắn liền với bao nhiêu khối, bao nhiêu lĩnh vực nhận biết, bao nhiêu yếu tố? Không có.»; "Katihi vippayutto?" = «Không gắn liền với bao nhiêu?»; "Katihi sampayutto?" = «Gắn liền với bao nhiêu?».
- "ekenāyatanena ekāya dhātuyā kehici vippayutto / sampayutto" = «không gắn liền / gắn liền với một số hiện tượng trong một lĩnh vực nhận biết, một yếu tố» (counts vary; «một số hiện tượng trong» stands for kehici). A ";" before it stays ";".
- Anything else that recurs and is new: settle it once for your chapter, write it in notes-<N>.md ("Pāli = tiếng Việt", one per line), and list it in your report.

## Source and output
- Source: AI_translation\pali\pi-3_split_chapters\<ch>.md
- Output: AI_translation\vietnamese\pi-3-vietnamese-plain-zeroshot_split_chapters\<ch>.md (same filename; the folder exists).
- The chapters are very repetitive. Generate yours with a builder script with fixed formula strings (pi-3-vi-ai\build_<N>_vi.py, importing build_sample_vi), so every repeat is byte-identical. The builder must assert that every string it takes from pi-1 / pi-2 still occurs in those rails files.

## Rules
- Identical Pāli = identical Vietnamese, within your chapter, with the sample and with pi-1 / pi-2 Vietnamese.
- Core: dhamma = hiện tượng; khandha = khối; āyatana = lĩnh vực nhận biết; dhātu = yếu tố; saṅgahita = được gộp vào; sampayutta = gắn liền với; rūpa = vật chất (visible form = hình sắc); saṅkhāra (aggregate) = tạo tác; vedanā = cảm giác; saññā = tri giác; viññāṇa = thức; sati = sự tỉnh thức (never «chánh niệm»).
- No notes or commentary of your own inside the translation. Variant brackets "[khác chính tả (Sī., Syā.): <Pāli>]" for spelling-only variants, "[dị bản (…): <Pāli>]" otherwise. "…pe…" → "…" (never «….»). (Ka)/(Kha)/(Ga) → (a)/(b)/(c). Digits stay.
- No "—" or "–" unless the Pāli has one at that spot (same count per line); no ":-". Questions end with "?" and use a Vietnamese question word. Avoid a doubled «là».
- Translate the Pāli as written (user rule): no emendations; only plain spelling slips and missing punctuation may be rendered as meant. Report suspected slips (wrong counts included: keep the count as written).

## Verify your chapter (all must pass before you report)
- `python -I -X utf8 0-INBOX\temp\pipeline\check_chapter_ids.py AI_translation\pali\pi-3_split_chapters AI_translation\vietnamese\pi-3-vietnamese-plain-zeroshot_split_chapters <ch>.md` prints OK.
- `python -I -X utf8 0-INBOX\temp\pipeline\dashcheck.py <pali ch> <vietnamese ch>`: equal line counts, 0 dash mismatches, 0 extra em-dashes.
- `python -I -X utf8 0-INBOX\temp\pipeline\pi-1-vi-ai\verify_rails_vi.py <pali ch> <vietnamese ch>` prints OK.
- The builder's pi-1 / pi-2 asserts pass.

## Final report (short, as text, under 300 words)
- Checks passed, segment count.
- Key new terms/formulas (also in your notes file) and what you reused from the sample / pi-1 / pi-2.
- Pāli you were unsure about or that looks like a source slip (translated as written).
