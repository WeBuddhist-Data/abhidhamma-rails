# Brief: RAILS Vietnamese translation, plain audience, pi-5 (Kathāvatthu): SAMPLE

## Setup
- Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write/Edit tools for files (write scripts with the Write tool at full paths under D:\Work\OpenPecha\abhidhamma-rails; never write any file from PowerShell), PowerShell for commands, `python -I -X utf8 -B` (-B: no __pycache__). LF line endings.
- Write ONLY the outputs listed below plus helper scripts in 0-INBOX\temp\pipeline\pi-5-vi-ai\rails\. Never create files at the repo root, outside the repo or in a system temp folder. Do not touch 1-SOURCES\ or 4-SYSTEM\, do not edit any pi-1 … pi-4 file, never run git (not even git status), never write "seed" or "unseeded". No web. You cannot write report files for me: return your report as text.
- This sample (preamble, 1-puggalakatha: 430 lines) is what the user reviews before the rest of the book is translated (three agents at a time, one chapter each). It sets every debate formula the later agents will copy.

## FORBIDDEN
- The copyrighted reference translation: never open, grep or search 1-SOURCES\Translations\Vietnamese\ (any file), 0-INBOX\raw-data\vi-*, 0-INBOX\temp\pipeline\pi-1-vi\, pi-2-vi\, pi-3-4-vi\, pi-5-vi\, pi-6-vi\, pi-7-vi\, pi-1-th-vi\, vi-tools\.
- The Vietnamese zero-shot of THIS book (translate FRESH from the Pāli): AI_translation\vietnamese\pi-5-vietnamese-plain-zeroshot_split_chapters\, pi-5-vietnamese-plain-zeroshot.md, and everything zero-shot in pi-5-vi-ai\ (build_*_vi.py, notes-*.md, vi-zeroshot-*.md, coordinator-rules.md, harmonise*, backup-pre-harmonise\, divergences*.md, find_divergences_vi.py, vi_common.py, probe_*.py, builder_hits_vi.py, find_pi1234_rails_vi.py, fix_crlf_vi.py, merge_zeroshot_vi.py); the Vietnamese side of the keyword maps (pi-5-vi-ai\mapper-vi\ except *.keywords.md; AI_translation\vietnamese\pi-5-keywords-by-reference-pali-vietnamese-plain.md); the senses files' example values are fine to read only through the termbase.
- No folder-wide searches over 0-INBOX\temp\pipeline\, 1-SOURCES\ or AI_translation\: Grep only the specific files named here.

## Read first
- AI_translation\skills\rails-verse-translator.md. Follow it.
- 0-INBOX\temp\pipeline\vietnamese-style.md: register, typography (“…” outer / ‘…’ inner; this book nests quotes often), the strict DASH RULE, structure, review lessons, core terms (sati = «sự tỉnh thức», never «chánh niệm»).
- **The approved Vietnamese pi-1 … pi-4 rails** (user-approved and reviewed): AI_translation\vietnamese\pi-1-… … pi-4-vietnamese-plain-rails_split_chapters\ (the lists: aggregates, bases, elements, faculties, path factors, person types, jhāna, path / fruit phrases, the sutta passages they quote), and their formula files 0-INBOX\temp\pipeline\pi-N-vi-ai\rails\vi-rails-formulas.md (N = 1 … 4). Where pi-5 has the same Pāli as pi-1 … pi-4, reuse their Vietnamese unless the pi-5 termbase decides otherwise; report each difference. Find matches by grepping the Pāli in AI_translation\pali\pi-N_split_chapters\<file>.md and reading the same non-empty line in the Vietnamese rails file (0-INBOX\temp\pipeline\pi-4-vi-ai\rails\find_pi123_rails_vi.py shows a lookup method; write a copy covering pi-1 … pi-4 in pi-5-vi-ai\rails\, e.g. find_pi1234r_vi.py).
- For meaning and layout only (never wording): the Russian pi-5 rails AI_translation\russian\pi-5-russian-plain-rails_split_chapters\<ch>.md and 0-INBOX\temp\pipeline\pi-5-ru\ru-rails-formulas.md; the English pi-5 rails AI_translation\english\pi-5-english-plain.md (grep by block ID); the commentary 1-SOURCES\Commentaries\pi-kathavatthu-atthakatha.md (Pāli; allowed) for hard readings.
- Where any model disagrees with the pi-5 Vietnamese termbase, the termbase wins.

## Inputs
- **Source:** AI_translation\pali\pi-5_split_chapters\<ch>.md
- **Locked termbase (authoritative, user-approved 2026-11-21):** AI_translation\vietnamese\pi-5-pali-vietnamese-termbase-plain.md, `pali: {english tag: tiếng Việt; …}`, plus 0-INBOX\temp\pipeline\pi-5-vi-ai\termbase\APPROVED.md (the user's decisions: saṃvara «sự thu thúc»; adhipati «yếu tố chủ đạo»; hetupaccaya «điều kiện gốc rễ»; aggo «bậc hàng đầu»; (a)kusala kāya- / vacī- / manokamma «nghiệp (bất) thiện bằng thân / lời nói / ý»; feelings sukha / dukkha «dễ chịu» / «khó chịu» (kāyika / cetasika dukkha «nơi thân» / «trong tâm»), «khổ đau» / «hạnh phúc» for suffering in general and happiness; niyata «cố định»; tiṭṭheyya / tiṭṭhanti «kéo dài», tiṭṭhati «duy trì», atthi «tồn tại»; «một bậc A-la-hán» without «một» where the Pāli has no numeral; names Sê-ni-gia, Sô-ma, Diêm-ma, Tu-bạt-đà-la) and the pi-1 … pi-4 decisions in their termbase\APPROVED.md.
  - Look up each Pāli word; pick the sense by its tag. A compound without an entry is built from its members' entries.
  - Terms are in citation form: a noun keeps its nominaliser where it stands as a noun; inside a phrase or as a modifier use the bare word; add or drop «các» / «những», «có», «là», «điều», tense words and classifiers as Vietnamese grammar needs. Never swap in a synonym.
  - If no sense fits, use the closest sibling entry and REPORT it.
- **Approved book frame, headings and debate formulas (user, 2026-11-21; copy verbatim):**
  - Homage «Kính lễ Đức Thế Tôn, bậc A-la-hán, bậc Tự Giác Ngộ Hoàn Toàn»; `# Abhidhammapiṭake` «# Tạng Vi Diệu Pháp»; `## Kathāvatthupāḷi` «## Các vấn đề tranh luận»; <X>kathā «Bàn về <X>» (Puggalakathā «Bàn về người»); <X>kathā niṭṭhitā «Phần bàn về <X> đã hoàn tất.»; N-vaggo «Chương thứ N»; (Saṃkhittaṃ) «(Tóm lược)»; (Ka) / (Kha) / (Ga) «(a) / (b) / (c)».
  - Chapter 1 headings: Suddhasaccikaṭṭho «Thực tại chân thật thuần túy»; okāsa- / kāla- / avayavasaccikaṭṭho «Thực tại chân thật xét theo nơi chốn / thời gian / các bộ phận»; Anulomapaccanīkaṃ «Chiều thuận và chiều nghịch»; Paccanīkānulomaṃ «Chiều nghịch và chiều thuận»; Suddhikasaṃsandanaṃ «Sự đối chiếu thuần túy»; Opammasaṃsandanaṃ «Sự đối chiếu bằng phép so sánh»; Catukkanayasaṃsandanaṃ «Sự đối chiếu theo phương pháp bốn cách»; Lakkhaṇayuttikathā «Bàn về lập luận dựa trên đặc tính»; Vacanasodhanaṃ «Sự làm sáng tỏ từ ngữ»; X-anuyogo «Chất vấn về X» (Paññatta- «sự định danh», Gati- «cõi tái sinh», Upādāpaññatta- «sự định danh phụ thuộc», Purisakāra- «việc làm của con người», Abhiññā- «các loại hiểu biết trực tiếp», Ñātakānuyogādi «người thân và các mục khác», Paṭivedha- «sự thấu triệt», Saṅgha- «Tăng đoàn», Saccikaṭṭhasabhāga- «những gì cùng bản chất với thực tại chân thật»). A closing label = the heading + ".".
  - Thesis and answers: "X"ti? «Có phải X không?»; Āmantā. «Đúng vậy.»; Āmantā? «Đúng vậy?» (as written); Na hevaṃ vattabbe. «Không nên nói như vậy.»; Vattabbaṃ. «Nên nói.»; …pe… «…» (never «.…» / «….»).
  - Questions and quotes: Nanu Xti? «Chẳng phải X sao?»; Nanu vuttaṃ bhagavatā – "…" «Chẳng phải Đức Thế Tôn đã nói thế này sao – “…”»; Vuttaṃ bhagavatā – "…" «Đức Thế Tôn đã nói – “…”»; Na vattabbaṃ – "X"ti? «Có phải không nên nói – “X” không?»; Attheva suttantoti? «Có bài kinh như vậy thật không?»; Tena hi Xti. «Vậy thì X.»; Xti katvā tena ca kāraṇena Yti? «Có phải vì cho rằng X, và vì lý do ấy, Y không?»; Xti, Yti? «Có phải nếu X …, thì Y … không?»; "X"ti vattabbo «nên gọi là “X”»; Aññaṃ X añño Y «X là khác, Y là khác».
  - Rebuttal pentad: Ājānāhi niggahaṃ / paṭikammaṃ. «Hãy thừa nhận sự bác bỏ. / sự phản bác.»; Hañci P, tena vata re vattabbe – "Q"ti. «Nếu P, thì này bạn, chắc chắn nên nói – “Q”.»; No ce pana vattabbe – "Q"ti, no ca vata re vattabbe – "P"ti. «Còn nếu không nên nói – “Q”, thì này bạn, chắc chắn không nên nói – “P”.»; Yaṃ tattha vadesi – "vattabbe kho – ‘P’, no ca vattabbe – ‘Q’"ti micchā. «Điều bạn nói ở đây là sai – “nên nói – ‘P’, nhưng không nên nói – ‘Q’”.» (repair the Pāli's garbled close "’ as ’”); …ti idaṃ te micchā. «Điều bạn nói ở đây là sai lầm của bạn – “…”.»; section labels Anulomapañcakaṃ. «Nhóm năm phần theo chiều thuận.», Paccanīkapañcakaṃ. «… theo chiều nghịch.», Paṭikamma- / Niggaha- / Upanayana- / Niggamanacatukkaṃ. «Nhóm bốn phần về sự phản bác / sự bác bỏ / sự áp dụng / sự kết luận.»; Paṭhamo … niggaho. «Sự bác bỏ thứ nhất. …».
  - Speaker notes in square brackets translated inside the brackets: [iminā lakkhaṇena sakavādīpucchā / paravādīpucchā dassitā] «[với dấu hiệu này, câu hỏi của người theo học thuyết của chúng ta / khác được trình bày]». Variant brackets «[khác chính tả (Sī., Syā.): X]» for spelling-only variants, «[dị bản (…): X]» otherwise; «[cần tham khảo Phụ chú giải]» for [ṭīkā oloketabbā].
  - Core terms: saccikaṭṭha «thực tại chân thật», paramattha «thực tại tối hậu», saccikaṭṭhaparamatthena «như một thực tại chân thật và tối hậu», upalabbhati «được tìm thấy», sakavādī «người theo học thuyết của chúng ta», paravādī «người theo học thuyết khác», puggala «người», re «này bạn».
  - These are the approved formulas, not wording to vary: the rails translation recasts only where the termbase says otherwise; report every place where you depart from them and why.
- **Audience:** AI_translation\audience_profile\plain.md

## What to produce
1. AI_translation\vietnamese\pi-5-vietnamese-plain-rails_split_chapters\preamble.md, 1-puggalakatha.md (create the folder).
2. 0-INBOX\temp\pipeline\pi-5-vi-ai\rails\vi-rails-formulas.md: every recurring frame and fixed string of the sample ("Pāli = tiếng Việt", one per line), which chapters 2-31 must use verbatim. Mark each string taken unchanged from pi-1 … pi-4 rails with "(pi-1)" … "(pi-4)".
3. 0-INBOX\temp\pipeline\pi-5-vi-ai\rails\build_rails_sample_vi.py: builds 1 from fixed strings exposed as constants (the frames, the pentad sentences with their slots, the section labels, the speaker notes, headings, closers, the quote-order repair) that later agents import; importing must not rewrite outputs (`if __name__ == "__main__":`). It asserts at build time that every (pi-N) string still occurs in those rails files, and offers per-line dash / quote / NFC checks.

## Rules
- **Block IDs:** exact, at the end of the last line of each segment, in the same order. **Headings:** keep their #-level. **Segments:** the source's number of non-empty lines; one blank line between segments.
- **DASH RULE (user):** "–" only where the Pāli has "–", same spot, same count on every line. Never add one; no ":-".
- **Punctuation:** statements end with "."; questions with "?" and a Vietnamese question word; keep the Pāli's own punctuation where it differs and report it. Quotes “…” / ‘…’ as the Pāli nests them.
- **Translate the Pāli as written** (user rule): no emendations, add nothing that is not in the Pāli, drop nothing that is (a repeated word stays); never merge sentences; only plain spelling slips and missing punctuation may be rendered as meant. Report suspected slips.
- **Formulas:** identical Pāli gets identical Vietnamese, within the sample and with the pi-1 … pi-4 Vietnamese rails.
- **Readability for a plain reader:** natural Vietnamese; recast where a literal string reads badly, keeping every term. Avoid a doubled «là».

## Verify (all must pass)
For preamble.md and 1-puggalakatha.md:
```
python -I -X utf8 -B 0-INBOX\temp\pipeline\check_chapter_ids.py AI_translation\pali\pi-5_split_chapters AI_translation\vietnamese\pi-5-vietnamese-plain-rails_split_chapters <file>.md
python -I -X utf8 -B 0-INBOX\temp\pipeline\dashcheck.py <pali> <vietnamese>
python -I -X utf8 -B 0-INBOX\temp\pipeline\pi-1-vi-ai\verify_rails_vi.py <pali> <vietnamese>
```
Then termbase adherence:
```
python -I -X utf8 -B 0-INBOX\temp\pipeline\termbase_adherence_vi.py AI_translation\pali\pi-5-keywords-by-reference-pali-plain.md AI_translation\vietnamese\pi-5-pali-vietnamese-termbase-plain.md AI_translation\vietnamese\pi-5-vietnamese-plain-rails_split_chapters
```
Read the misses with judgement and fix the genuine ones.

## Report (under 450 words, as text)
- Checks passed; segment counts; adherence results.
- 10-15 key formulas as "Pāli = tiếng Việt".
- Strings reused from pi-1 … pi-4 rails and any place where the pi-5 termbase made you differ (from those rails or from the approved formulas above).
- Termbase misfits (term, segment, why, what you wrote) and terms the termbase lacks.
- Unsure Pāli or source slips.
