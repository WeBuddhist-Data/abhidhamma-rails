# Brief: RAILS Vietnamese translation, plain audience, pi-6 (Yamaka): SAMPLE

## Setup
- Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write/Edit tools for files (write scripts with the Write tool at full paths under D:\Work\OpenPecha\abhidhamma-rails; never write any file from PowerShell), PowerShell for commands, `python -I -X utf8 -B` (-B: no __pycache__). LF line endings.
- Write ONLY the outputs listed below plus helper scripts in 0-INBOX\temp\pipeline\pi-6-vi-ai\rails\ (create the folder). Never create files at the repo root (not even an empty one), outside the repo or in a system temp folder. Do not touch 1-SOURCES\ or 4-SYSTEM\, do not edit any pi-1 … pi-5 file, never run git (not even git status), never write "seed" or "unseeded". No web. You cannot write report files for me: return your report as text.
- This sample (preamble, 1-mulayamaka: 305 lines) is what the user reviews before the rest of the book is translated (five agents at a time, one chapter each). It sets every pair-question formula the later agents will copy.

## FORBIDDEN
- The copyrighted reference translation: never open, grep or search 1-SOURCES\Translations\Vietnamese\ (any file), 0-INBOX\raw-data\vi-*, 0-INBOX\temp\pipeline\pi-1-vi\, pi-2-vi\, pi-3-4-vi\, pi-5-vi\, pi-6-vi\, pi-7-vi\, pi-1-th-vi\, vi-tools\.
- The Vietnamese zero-shot of THIS book (translate FRESH from the Pāli): AI_translation\vietnamese\pi-6-vietnamese-plain-zeroshot_split_chapters\, pi-6-vietnamese-plain-zeroshot.md, and everything in 0-INBOX\temp\pipeline\pi-6-vi-ai\ outside termbase\ and rails\ (build_*_vi.py, notes-*.md, vi-zeroshot-*.md, zeroshot-coordinator-rules.md, harmonise*, backup-pre-harmonise\, divergences*.md, find_divergences_vi.py, vi_common.py, probe_*.py, list_headings_vi.py, merge_zeroshot_vi.py, split_keywords_vi.py, senses_prepare_vi.py, senses\, the other briefs). One exception: you may copy 0-INBOX\temp\pipeline\pi-6-vi-ai\find_pi12345r_vi.py (a lookup that reads only the pi-1 … pi-5 Pāli and Vietnamese RAILS) into rails\ and use the copy.
- The Vietnamese side of the keyword map: 0-INBOX\temp\pipeline\pi-6-vi-ai\mapper-vi\ (all of it except the *.keywords.md files) and AI_translation\vietnamese\pi-6-keywords-by-reference-pali-vietnamese-plain.md. The senses file's values reach you only through the termbase.
- No folder-wide searches over 0-INBOX\temp\pipeline\, 1-SOURCES\ or AI_translation\: Grep only the specific files named here.

## Read first
- AI_translation\skills\rails-verse-translator.md. Follow it.
- 0-INBOX\temp\pipeline\vietnamese-style.md: register, typography (“…” outer / ‘…’ inner), the strict DASH RULE, structure, review lessons, core terms (sati = «sự tỉnh thức», never «chánh niệm»).
- **The approved Vietnamese pi-1 … pi-5 rails** (user-approved and reviewed): AI_translation\vietnamese\pi-N-vietnamese-plain-rails_split_chapters\ (N = 1 … 5) and their formula files 0-INBOX\temp\pipeline\pi-N-vi-ai\rails\vi-rails-formulas.md. Where pi-6 has the same Pāli as pi-1 … pi-5, reuse their Vietnamese unless the pi-6 termbase decides otherwise; report each difference. Find matches with the find_pi12345r_vi.py copy (it greps the Pāli in AI_translation\pali\pi-N_split_chapters\ and prints the same non-empty line of the Vietnamese rails).
- For meaning and layout only (never wording): the English pi-6 rails AI_translation\english\pi-6-english-plain-rails_split_chapters\1-mulayamaka.md (there is no Russian pi-6); the commentary 1-SOURCES\Commentaries\pi-yamaka-atthakatha.md (Pāli; allowed; grep it, don't read it whole) for hard readings.
- Where any model disagrees with the pi-6 Vietnamese termbase, the termbase wins.

## Inputs
- **Source:** AI_translation\pali\pi-6_split_chapters\preamble.md, 1-mulayamaka.md.
- **Locked termbase (authoritative, user-approved 2026-11-22):** AI_translation\vietnamese\pi-6-pali-vietnamese-termbase-plain.md, `pali: {english tag: tiếng Việt; …}`, plus 0-INBOX\temp\pipeline\pi-6-vi-ai\termbase\APPROVED.md (the user's decisions; decision 4 lists text-level changes, mostly for later chapters) and the pi-1 … pi-5 decisions in their termbase\APPROVED.md.
  - Look up each Pāli word; pick the sense by its tag. A compound without an entry is built from its members' entries.
  - Terms are in citation form: a noun keeps its nominaliser where it stands as a noun; inside a phrase or as a modifier use the bare word; add or drop «các» / «những», «có», «là», «điều», tense words and classifiers as Vietnamese grammar needs. Never swap in a synonym.
  - If no sense fits, use the closest sibling entry and REPORT it.
- **Approved book frame, headings and formulas (user, 2026-11-22; copy verbatim):**
  - Homage «Kính lễ Đức Thế Tôn, bậc A-la-hán, bậc Tự Giác Ngộ Hoàn Toàn»; `# Abhidhammapiṭake` «# Tạng Vi Diệu Pháp»; `## Yamakapāḷi` «## Các cặp câu hỏi». Book closer Yamakapakaraṇaṃ niṭṭhitaṃ. «Bộ “Các cặp câu hỏi” đã hoàn tất.»; <X>yamakapāḷi niṭṭhitā. «Phần <yamaka title, lowercase> đã hoàn tất.» (Mūlayamakapāḷi niṭṭhitā. «Phần các cặp câu hỏi về gốc rễ đã hoàn tất.»); niṭṭhito / niṭṭhitā «đã hoàn tất».
  - Yamaka titles «Các cặp câu hỏi về …»: Mūla- «gốc rễ», Khandha- «các khối», Āyatana- «các lĩnh vực nhận biết», Dhātu- «các yếu tố», Sacca- «các sự thật», Saṅkhāra- «các tạo tác», Anusaya- «các khuynh hướng tiềm ẩn», Citta- «tâm», Dhamma- «các hiện tượng», Indriya- «các năng lực».
  - Labels (Ka) (Kha) (Ga) (Gha) (Ṅa) (Ca) (Cha) (Ja) = (a) (b) (c) (d) (đ) (e) (g) (h) (Vietnamese alphabet order; never f / j / w / z: verify_rails_vi rejects them).
  - Chapter 1 headings: uddeso «Phần nêu đề mục»; niddeso «Phần giải thích»; <X>vāro «Mục về <X>» (Mūlavāro «Mục về gốc rễ»; Hetuvārādi «Mục về nguyên nhân và các mục khác»); Uddesavāro / Niddesavāro «Mục nêu đề mục» / «Mục giải thích» (+ niṭṭhito «… đã hoàn tất.»); Mūlavārauddeso. «Phần nêu đề mục của mục về gốc rễ.»; Mūlavāraniddeso. «Phần giải thích của mục về gốc rễ.»; <X>nayo «Phương pháp về <X>»: Mūlanayo «… gốc rễ», Mūlamūlanayo «… cội rễ», Mūlakanayo «… sự bắt nguồn từ gốc rễ», Mūlamūlakanayo «… sự bắt nguồn từ cội rễ» (a lowercase method word as written stays lowercase).
  - Recurring headings of the later chapters (put them in the formulas file as approved; do not invent others): (Ka) anulomaṃ / (Kha) paccanīkaṃ «(a) Chiều thuận / (b) Chiều nghịch»; paṭiloma «chiều ngược» (kept apart from paccanīka); Paṇṇattivāro «Mục về sự định danh»; Padasodhanavāro «Mục về sự làm sáng tỏ thuật ngữ»; Padasodhanamūlacakkavāro «Mục về vòng luân chuyển dựa trên sự làm sáng tỏ thuật ngữ»; Suddha<X>vāro «Mục về các <X> thuần túy»; Pavattivāro «Mục về sự diễn tiến»; uppādavāro «mục về sự sinh khởi»; nirodhavāro «mục về sự chấm dứt»; Pariññāvāro «Mục về sự hiểu biết trọn vẹn»; Paccuppanna- / Atīta- / Anāgatavāro «Mục về hiện tại / quá khứ / tương lai»; anulomapuggalo / anulomaokāso / anulomapuggalokāsā «Chiều thuận theo người / theo nơi chốn / theo người và nơi chốn» (paccanīka- «Chiều nghịch …»); Pajahanavāro «Mục về sự dứt bỏ»; Pahīnavāro «Mục về những gì đã được dứt bỏ»; dhātupucchāvāro «Mục hỏi theo các cõi», dhātuvisajjanāvāro «Mục trả lời theo các cõi».
  - Pair questions: (Ka) Ye keci X dhammā, sabbe te Y(ti)? «(a) Bất cứ hiện tượng nào X, có phải tất cả chúng đều Y không?»; (Kha) Ye vā pana Y, sabbe te dhammā X(ti)? «(b) Còn bất cứ gì Y, có phải tất cả các hiện tượng ấy đều X không?»; a question cut by …pe… keeps its shape and ends «…» (add «không?» only where the Pāli has "?"). X slot: kusalā «là thiện», akusalā «là bất thiện», abyākatā «không xác định về mặt đạo đức», nāmā «thuộc phần tinh thần».
  - Answers: Āmantā. «Đúng vậy.»; Tīṇeva Xmūlāni. «Chỉ có ba gốc rễ X.»; Naveva nāmamūlāni. «Chỉ có chín gốc rễ thuộc phần tinh thần.»; Avasesā X dhammā na Y. «Các hiện tượng X còn lại không phải là Y.»; Xsamuṭṭhānaṃ rūpaṃ … «Vật chất do <X> sinh ra thì …, nhưng …»; «vừa A vừa B» for A ceva B ca; Ahetukaṃ / Sahetukaṃ X «X mà không có gốc rễ / mà có gốc rễ»; ekato uppajjanti «cùng sinh khởi»; sahajāta «cùng sinh»; …pe… «…» (never «.…» / «….»).
  - The four methods: mūla «gốc rễ», mūlamūla «cội rễ», -mūlaka «bắt nguồn từ gốc rễ», -mūlamūlaka «bắt nguồn từ cội rễ»; eka- «có cùng một …» / «bắt nguồn từ cùng một …» (eka = the same, not the number: aṭṭhakathā); aññamañña- «làm gốc rễ cho nhau / làm cội rễ cho nhau / bắt nguồn từ gốc rễ của nhau / bắt nguồn từ cội rễ của nhau»; Xmūlena «xét theo gốc rễ X»; kusala- / akusala- / abyākata- / nāmamūla «gốc rễ thiện / bất thiện / không xác định về mặt đạo đức / thuộc phần tinh thần».
  - The ten-term hetuvāra series: mūla, hetu, nidāna, sambhava, pabhava, samuṭṭhāna, āhāra, ārammaṇa, paccaya, samudaya = «gốc rễ, nguyên nhân, căn nguyên, sự hình thành, sự khởi nguồn, nguồn gốc, dưỡng chất, đối tượng, điều kiện, sự phát sinh» (hetu in this series «nguyên nhân»; elsewhere sahetuka / ahetuka «có / không có gốc rễ»); compounds noun + adjective (kusalahetū «nguyên nhân thiện», nāmārammaṇā «đối tượng thuộc phần tinh thần»); verse: Mūlaṃ hetu nidānañca, sambhavo pabhavena ca; «Gốc rễ, nguyên nhân và căn nguyên, sự hình thành cùng với sự khởi nguồn;» / Samuṭṭhānāhārārammaṇā, paccayo samudayena cāti. «Nguồn gốc, dưỡng chất, đối tượng, điều kiện cùng với sự phát sinh.».
  - Variant brackets as in pi-1 … pi-5: «[dị bản (Ka.): X]» (form variant), «[khác chính tả (…): X]» for spelling-only variants.
  - These are approved formulas, not wording to vary: recast only where the termbase says otherwise; report every place where you depart from them and why.
- **Audience:** AI_translation\audience_profile\plain.md

## What to produce
1. AI_translation\vietnamese\pi-6-vietnamese-plain-rails_split_chapters\preamble.md, 1-mulayamaka.md (create the folder).
2. 0-INBOX\temp\pipeline\pi-6-vi-ai\rails\vi-rails-formulas.md: every recurring frame and fixed string of the sample, plus the approved later-chapter headings above ("Pāli = tiếng Việt", one per line), which chapters 2-01 … 10-13 must use verbatim. Mark each string taken unchanged from pi-1 … pi-5 rails with "(pi-1)" … "(pi-5)".
3. 0-INBOX\temp\pipeline\pi-6-vi-ai\rails\build_rails_sample_vi.py: builds preamble and 1 from fixed strings exposed as constants and slot helpers (LABEL, headings, closers, the pair-question frames with X / Y slots, the answer frames, the four-method terms, the hetuvāra series) that later agents import; importing must not rewrite outputs (`if __name__ == "__main__":`). It asserts at build time that every (pi-N) string still occurs in those rails files, and offers per-line dash / quote / NFC checks.

## Rules
- **Block IDs:** exact, at the end of the last line of each segment, in the same order. **Headings:** keep their #-level. **Segments:** the source's number of non-empty lines; one blank line between segments.
- **DASH RULE (user):** "–" only where the Pāli has "–", same spot, same count on every line. Never add one; no ":-".
- **Punctuation:** statements end with "."; questions with "?" and a Vietnamese question word; keep the Pāli's own punctuation where it differs and report it.
- **Translate the Pāli as written** (user rule): no emendations, add nothing that is not in the Pāli, drop nothing that is (a repeated word stays); never merge sentences; only plain spelling slips and missing punctuation may be rendered as meant. Report suspected slips.
- **Formulas:** identical Pāli gets identical Vietnamese, within the sample and with the pi-1 … pi-5 Vietnamese rails.
- **Distinct pairs:** mūla «gốc rễ» vs mūlamūla «cội rễ»; hetu «nguyên nhân» (series) vs «gốc rễ» (sahetuka / ahetuka); plus the pi-1 … pi-5 pairs.
- **Readability for a plain reader:** natural Vietnamese; recast where a literal string reads badly, keeping every term. Avoid a doubled «là».

## Verify (all must pass)
For preamble.md and 1-mulayamaka.md:
```
python -I -X utf8 -B 0-INBOX\temp\pipeline\check_chapter_ids.py AI_translation\pali\pi-6_split_chapters AI_translation\vietnamese\pi-6-vietnamese-plain-rails_split_chapters <file>.md
python -I -X utf8 -B 0-INBOX\temp\pipeline\dashcheck.py <pali> <vietnamese>
python -I -X utf8 -B 0-INBOX\temp\pipeline\pi-1-vi-ai\verify_rails_vi.py <pali> <vietnamese>
```
Then termbase adherence:
```
python -I -X utf8 -B 0-INBOX\temp\pipeline\termbase_adherence_vi.py AI_translation\pali\pi-6-keywords-by-reference-pali-plain.md AI_translation\vietnamese\pi-6-pali-vietnamese-termbase-plain.md AI_translation\vietnamese\pi-6-vietnamese-plain-rails_split_chapters
```
Read the misses with judgement and fix the genuine ones.

## Report (under 450 words, as text)
- Checks passed; segment counts; adherence results.
- 10-15 key formulas as "Pāli = tiếng Việt".
- Strings reused from pi-1 … pi-5 rails and any place where the pi-6 termbase made you differ (from those rails or from the approved formulas above).
- Termbase misfits (term, segment, why, what you wrote) and terms the termbase lacks.
- Unsure Pāli or source slips.
