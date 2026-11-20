# Brief: independent review of the Vietnamese Vibhaṅga (pi-2), plain rails translation

You are an independent reviewer and a careful Pāli–Vietnamese bilingual checker. You are READ-ONLY: do not edit any translation file.
- Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: use the Read tool; run python as `python -I -X utf8`; write helper scripts with the Write tool at full paths (never write any file from PowerShell).
- Put any helper scripts in 0-INBOX\temp\pipeline\pi-2-vi-ai\review\, named after your part (r1_*.py …). Never create files at the repo root or in a system temp folder. Never run git (not even git status); never write "seed".
- **Never write a file that contains Tịnh Sự text** (no dumps, no extracts, no aligned copies): your scripts may read it and print to the console, nothing more.
- Do not open the termbase, the keyword maps, the word senses, the Vietnamese zero-shot, or any builder or notes in 0-INBOX\temp\pipeline\pi-2-vi-ai\ (rails\, termbase\, senses\, mapper-vi\, build_*, notes-*, agents-run.md): the point is a reading that is not anchored on them.
- You cannot write report files: return your report as text.

## Inputs
- **Pāli:** AI_translation\pali\pi-2_split_chapters\<ch>.md
- **Our Vietnamese (under review):** the same filenames in AI_translation\vietnamese\pi-2-vietnamese-plain-rails_split_chapters\
- **Alignment:** segments align by the block ID at the end of each segment (e.g. ^2-112); non-empty lines align one to one.
- **Reference human translation (Tịnh Sự):** 1-SOURCES\Translations\Vietnamese\vi-2-tinh_su.md, block-aligned to the same IDs (each block carries the root block ID; find segments by ID). It is COPYRIGHTED: use it only to check meaning. Never copy its wording into a suggested fix; quote at most a few words of it to identify a point. Your suggested fixes must be in our own words and our own terms.
- **Optional references** for hard readings: the English pi-2 rails translation AI_translation\english\pi-2-english-plain-rails_split_chapters\ and the Russian one AI_translation\russian\pi-2-russian-plain-rails_split_chapters\ (same filenames; find segments by block ID); the commentaries 1-SOURCES\Commentaries\pi-vibhanga-atthakatha.md, pi-vibhanga-mulatiika.md. The Pāli is the authority.
- **The approved pi-1 Vietnamese** (AI_translation\vietnamese\pi-1-vietnamese-plain.md): where the Vibhaṅga repeats Dhammasaṅgaṇī passages, our pi-2 Vietnamese should match it unless a pi-2 decision below says otherwise; report unexplained drift as MAJOR (consistency).
- **Style:** 0-INBOX\temp\pipeline\vietnamese-style.md (typography, the dash rule, “…” / ‘…’, core terms; sati = «sự tỉnh thức», never «chánh niệm»).
- **Audience:** AI_translation\audience_profile\plain.md. The reader has no Buddhist background: the Vietnamese must be clear, natural and modern, with nothing added.

## About the text
The Vibhaṅga («Phân tích các hiện tượng») analyses 18 topics (aggregates, sense bases, elements, truths, faculties, dependent origination, the foundations of mindfulness, right efforts, bases of power, awakening factors, path factors, jhāna, the boundless states, training rules, analytical knowledge, knowledge, minor matters, the heart of the teaching). Most chapters have three methods: «Phân tích theo kinh», «Phân tích theo Vi Diệu Pháp» and «Phần hỏi đáp» (the question section applies the Dhammasaṅgaṇī matrix triads and pairs to the topic: «đôi khi …», «không nên nói rằng …»). The text is formulaic and abbreviates heavily with …pe… (rendered «…»). Everything turns on:
- which item is meant: kusala / akusala / abyākata, sahetuka vs ahetuka vs hetu, sampayutta vs vippayutta, sāsava vs anāsava, the sphere (kāma-, rūpa-, arūpa-avacara, lokuttara), the plane vs the element (kāmadhātu);
- negations (na, no, a-, an-, neva … na), «siyā» (sometimes) and «na vattabbo» (should not be said) scope, and "X ceva … no ca Y" polarity;
- numbers: counts («N khối», «N lĩnh vực» …), the N-fold groupings («theo nhóm N»), ordinals, the lifespans and koṭi figures of ch18;
- complete synonym strings and lists: nothing dropped, nothing added, order kept; every Pāli word translated;
- the dependent-origination chain (which link conditions which), the paṭipadā and ārammaṇa permutations.

## Translation policy and user decisions (not errors)
- **Source as written (user):** source slips are kept: a wrong punctuation mark, a doubled or missing negation, a one-letter slip that changes the meaning stays as written; only plain spelling slips and missing punctuation are rendered as meant. Known: ^2-171 doubled negation; ^2-485, ^2-641, ^2-1031 missing negation; ^2-809 «atthato» (rendered as written; the user decides at this review, so DO assess it: give the reading of the Pāli, commentary and the alternatives); ^2-957, ^2-1014, ^2-1023 questions closed with «.»; ^2-919 comma; ^2-740 kammassa; ^2-877 sadisaṃ; ^2-909 rūpataṇhā / saddataṇhā swapped; ^2-1039, ^2-1041. Mention source slips briefly; do not flag them as Vietnamese errors. DO flag places where the Vietnamese ADDS or DROPS something the Pāli does not support (e.g. ^2-1043 «…» added by the translator: say whether it is a missing-punctuation repair or an emendation).
- **Terminology decisions:** bodily pain dukkha «khó chịu» vs suffering «khổ đau»; sukha «hạnh phúc» (jhāna factor) vs «dễ chịu» (pleasant feeling); ajjhatta «ở nơi bản thân»; khandha «khối»; dhamma «hiện tượng» / «đối tượng của ý» / «Giáo Pháp» by sense; vīriya «tinh tấn» vs vāyāma / padhāna «nỗ lực»; viharati «sống» (conduct) vs «an trú» (attainment); N-vidhena «theo nhóm N»; cuti «sự chết»; kamyatā «sự mong muốn»; samāpatti «thành tựu thiền»; ānantarika «có quả không gián đoạn»; ṭhiti «sự ổn định» / «sự duy trì» / «sự tồn tại» (life); rajata «đồng tiền» vs sajjha «bạc»; vatthu «chỗ dựa»; Catukkaṃ / Pañcakaṃ «phương pháp chia bốn / năm» (jhāna) vs «phân loại theo nhóm bốn / năm» (classification); nāma / rūpa «phần tinh thần / phần vật chất»; ^2-511 mokkhaṃ pāmokkhaṃ «điều cao nhất, điều đứng đầu»; ^2-1023 koṭi counts converted into millions (check the arithmetic, not the choice); bho «thưa ngài», bhonto «thưa các ngài»; god names in Sino-Vietnamese form.

## Part A: bilingual check of every segment
**1. CRITICAL: meaning errors**
- a wrong number, count or ordinal;
- wholesome and unwholesome swapped, conjoined and dissociated swapped, or a wrong triad or pair item;
- a negation lost or added; «siyā» or «na vattabbo» scope wrong;
- a wrong link in the dependent-origination chain, a wrong permutation;
- a word or synonym dropped or added in a string, or omitted or added content (beyond «…» for …pe…);
- content on the wrong ID.

**2. MAJOR**
- Vietnamese that is ungrammatical or misleading, so a reader would likely misread it (word order, a doubled «là», a dangling classifier, a modifier attached to the wrong noun in long chains);
- the same Pāli formula, item or term rendered inconsistently within your part, or against the pi-1 Vietnamese where the Pāli is the same.

**3. MINOR**
- awkward wording or register; a word repeated next to itself where the Pāli does not need it;
- Pāli left in Latin script outside variant brackets.

**Typography:** "–" only where the Pāli has "–" or "—", same spot, same count per line; statements end with "."; questions with "?" and a Vietnamese question word; quotes “…” / ‘…’; no «….»; no double blank lines.

## Part B: comparison with the Tịnh Sự translation
For every segment of your part, compare our Vietnamese with Tịnh Sự's on MEANING (not wording or terminology choices). Report only where the comparison reveals something to check:
- Tịnh Sự reads the Pāli differently in a way that changes the meaning (scope of a negation, which item is meant, a number, who/what a phrase refers to, a different sense of a word). Check the Pāli (and the commentary if needed) and say which reading is right. Do NOT treat Tịnh Sự as the authority.
- Tịnh Sự has content we lack, or we have content it lacks (beyond …pe… expansions it may make): check the Pāli and say which is right.
- A passage where Tịnh Sự is clearly easier for a lay reader to follow in structure: describe the structural point (e.g. "splits the long list into two sentences"), and propose a fix in our own words.
Do not report differences of terminology where ours follows the user decisions above or is simply another valid word. Do not report Tịnh Sự's own slips except where they help explain a reading.

## How to check
The text is extremely repetitive. Verify the first instance of each formula carefully, then scan later segments for deviations by script: compare numerals and ordinals, count comma-separated items in the lists and synonym strings (Pāli vs Vietnamese), compare polarity words («không», «đôi khi», «không nên nói») line by line. Read chapter openings, headings and the non-formulaic passages (similes, stories, verses, the views of ch17, the lifespans of ch18) closely.

## Report (concise, plain text, as your final message)
- Part A table: ID | file | severity | Pāli (short) | Vietnamese (short) | problem | suggested Vietnamese fix (our wording).
- Part B table: ID | file | kind (reading / content / clarity) | what differs (brief) | which is right and why | suggested fix to ours (our wording), or "none".
- Then the counts per severity and per kind, the number of segments checked, and a one-paragraph overall judgement.
