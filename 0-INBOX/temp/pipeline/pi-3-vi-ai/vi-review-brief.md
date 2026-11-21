# Brief: independent review of the Vietnamese Dhātukathā (pi-3), plain rails translation

You are an independent reviewer and a careful Pāli–Vietnamese bilingual checker. You are READ-ONLY: do not edit any translation file.
- Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: use the Read tool; run python as `python -I -X utf8`; write helper scripts with the Write tool at full paths (never write any file from PowerShell).
- Put any helper scripts in 0-INBOX\temp\pipeline\pi-3-vi-ai\review\, named after your part (r1_*.py …). Never create files at the repo root or in a system temp folder. Never run git (not even git status); never write "seed". No web.
- **Never write a file that contains Tịnh Sự text** (no dumps, no extracts, no aligned copies): your scripts may read it and print to the console, nothing more.
- Do not open the termbase, the keyword maps, the word senses, the Vietnamese zero-shot, or any builder or notes in 0-INBOX\temp\pipeline\pi-3-vi-ai\ (rails\, termbase\, senses\, mapper-vi\, build_*, notes-*, agents-run.md): the point is a reading that is not anchored on them.
- Grep only the specific files named here, never whole folders.
- You cannot write report files: return your report as text.

## Inputs
- **Pāli:** AI_translation\pali\pi-3_split_chapters\<ch>.md
- **Our Vietnamese (under review):** the same filenames in AI_translation\vietnamese\pi-3-vietnamese-plain-rails_split_chapters\
- **Alignment:** segments align by the block ID at the end of each segment (e.g. ^3-112); non-empty lines align one to one.
- **Reference human translation (Tịnh Sự):** 1-SOURCES\Translations\Vietnamese\vi-3-tinh_su.md, block-aligned to the same IDs (find segments by ID). It is COPYRIGHTED: use it only to check meaning. Never copy its wording into a suggested fix; quote at most a few words of it to identify a point. Your suggested fixes must be in our own words and our own terms.
- **Optional references** for hard readings: the English pi-3 rails AI_translation\english\pi-3-english-plain.md and the Russian ones AI_translation\russian\pi-3-russian-plain-rails_split_chapters\<ch>.md (find segments by block ID); the commentaries 1-SOURCES\Commentaries\pi-dhatukatha-atthakatha.md, pi-dhatukatha-mulatiika.md, pi-dhatukatha-anutiika.md. The Pāli is the authority.
- **The approved pi-1 and pi-2 Vietnamese** (AI_translation\vietnamese\pi-1-vietnamese-plain.md, pi-2-vietnamese-plain.md): the Dhātukathā's lists (aggregates, bases, elements, truths, faculties, dependent-origination links) and matrix names should match them unless a decision below says otherwise; report unexplained drift as MAJOR (consistency).
- **Style:** 0-INBOX\temp\pipeline\vietnamese-style.md (typography, dash rule, “…” / ‘…’, core terms; sati = «sự tỉnh thức», never «chánh niệm»).
- **Audience:** AI_translation\audience_profile\plain.md. The reader has no Buddhist background: clear, natural, modern Vietnamese, nothing added.

## About the text
The Dhātukathā («Thảo luận về các yếu tố») asks, for each item (the aggregates, bases, elements, truths, faculties, dependent-origination links, the seven mental factors, and the triads and dyads of the Dhammasaṅgaṇī matrix), in how many aggregates, sense bases and elements it is included (saṅgahita «được gộp vào») or not, and with how many it is associated (sampayutta «gắn liền với») or dissociated. Fourteen methods (chapters 2-15) combine these questions, often with relative clauses ("the states that are included with X by aggregate-inclusion but not by base- or element-inclusion: in how many … are they not included?"). Each method ends with a summary verse (uddāna). Everything turns on:
- the numbers: every count of aggregates, bases and elements; a wrong number is CRITICAL;
- polarity: saṅgahita vs asaṅgahita, sampayutta vs vippayutta, na kehici («by none»), kehici («partly, with some»), Natthi («none»);
- which item is meant (the triad / dyad names, the list members), and that no item is dropped or added in a list or a …pe… run;
- the relative-clause structure: which reference item, which inclusion type (khandha- / āyatana- / dhātu-saṅgahena), which polarity.

## Translation policy and user decisions (not errors)
- **Source as written (user):** source slips are kept; only plain spelling slips and missing punctuation are rendered as meant. Known (assess briefly, do not flag as Vietnamese errors): ^3-112 variant identical to the text; ^3-170 answer covers only araṇā; ^3-189 Cittasahabhūmi (as meant); ^3-213 / ^3-279 / ^3-389 / ^3-495 joined na hetu- compounds (as meant); ^3-269 missing «…» added; ^3-343 variant bracket placement; ^3-357 «..»; ^3-408 association verse in a dissociation chapter; ^3-413 «saṅgahitā te dhammā» without …pe… or question; ^3-447 «Rūpakkhandhā cattāro» (probably Arūpa-; rendered «Bốn khối vật chất» as written: DO assess with the commentary); ^3-453 āsavavippayuttehi (probably āsavasampayuttehi); ^3-487 «ye vippayuttā» without dhammā; ^3-505 cittasaṃsaṭṭhehi repeated. DO flag places where the Vietnamese ADDS or DROPS something the Pāli does not support.
- **Accepted Vietnamese additions (grammar only):** «nhưng» joining mixed na kehici answers; pronouns «nó» / «chúng» / «những hiện tượng ấy» where Vietnamese needs a subject; «thì» before the verb to avoid «được được» / a doubled «gắn liền»; «và» before the last count; «;» between numbered matrix items; ^3-3 «theo ba / bốn cách» for tīhi / catūhi. Report only if one of these misleads.
- **Terminology decisions:** book «Thảo luận về các yếu tố»; methods «Phương pháp thứ nhất … thứ mười bốn»; padaniddeso «Giải thích đề mục về …»; saṅgahita «được gộp vào», sampayutta «gắn liền với»; sabhāga / visabhāga «cùng loại / khác loại»; kehici «một số hiện tượng thuộc …»; Natthi «Không có»; labbhati / labbhare «tìm thấy»; Samucchede «sự phân tích»; nāsaññā «không phải không tri giác» (pi-1); round labels «(Phần xét từng mục một.)» …; sukha «hạnh phúc» (jhāna) / «dễ chịu» (feeling); dukkha «khó chịu» / «khổ đau»; rūpa «vật chất» / «hình sắc»; arūpa «không hình sắc» / «phi vật chất».
- **Lesson from pi-2's review:** predicates or answers that carry no count of their own cover the whole set named in the question; check that the Vietnamese does not narrow or widen the scope.

## Part A: bilingual check of every segment
**1. CRITICAL: meaning errors** — a wrong number or count; included / not included or associated / dissociated swapped; a wrong reference item, inclusion type, triad or dyad item; a negation lost or added; kehici / na kehici confused; an item dropped or added in a list or chain; content on the wrong ID.
**2. MAJOR** — Vietnamese that is ungrammatical or misleading (especially the long relative-clause questions: can a plain reader tell what is included with what?); the same Pāli formula or item rendered inconsistently within your part, across the book, or against pi-1 / pi-2 where the Pāli is the same.
**3. MINOR** — awkward wording or register; repetition; Pāli left in Latin script outside variant brackets.
**Typography:** "–" only where the Pāli has one; statements end with "."; questions with "?" and a Vietnamese question word; quotes “…” / ‘…’; no «….».

## Part B: comparison with the Tịnh Sự translation (meaning only)
For every segment of your part, compare our Vietnamese with Tịnh Sự's on MEANING. Report only where the comparison reveals something to check:
- Tịnh Sự reads the Pāli differently in a way that changes the meaning (a count, a polarity, which item, the relative-clause structure, a verse line). Check the Pāli (and the commentary if needed) and say which reading is right. Tịnh Sự is not the authority.
- Tịnh Sự has content we lack, or we have content it lacks (beyond …pe… expansions): check the Pāli and say which is right.
- A passage where Tịnh Sự is clearly easier for a lay reader to follow in structure: describe the structural point and propose a fix in our own words.
Do not report terminology differences where ours follows the decisions above or is another valid word.

## How to check
The text is extremely repetitive. Verify the first instance of each formula carefully, then check every segment by script: compare every count (Pāli numeral words → Vietnamese numbers, per answer, in order), the polarity words («không được gộp vào», «không gắn liền», «không có … nào», «một số hiện tượng»), and the list items (count …-separated members, Pāli vs Vietnamese). Read the headings, the relative-clause frames and the summary verses closely.

## Report (concise, plain text, as your final message)
- Part A table: ID | file | severity | Pāli (short) | Vietnamese (short) | problem | suggested Vietnamese fix (our wording).
- Part B table: ID | file | kind (reading / content / clarity) | what differs (brief) | which is right and why | suggested fix to ours (our wording), or "none".
- Then the counts per severity and per kind, the number of segments checked, and a one-paragraph overall judgement.
