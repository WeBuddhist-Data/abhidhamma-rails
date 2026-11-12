# Brief: consistency (harmonise) pass, pi-2 Hindi plain zero-shot

Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write tools for files, PowerShell for commands, `python -I -X utf8`, helper scripts written to files. Write only in AI_translation\hindi\pi-2-hindi-plain-zeroshot_split_chapters\ (the 19 files) and 0-INBOX\temp\pipeline\pi-2-hi\. Do not touch 1-SOURCES\ or 4-SYSTEM\, do not run git.

## Situation
Nine agents translated the 18 chapters of the Vibhaṅga in parallel from one term list (pi-2-hi\hi-zeroshot-terms.md), each with builder scripts (pi-2-hi\build_*_hi.py plus shared helper modules) and a notes file (pi-2-hi\notes-*.md). preamble.md and the first 77 non-empty lines of 1-khandhavibhango.md (= pi-2-hi\ch1-sample.md) are user-approved and must stay unchanged. The book reuses pi-1 Hindi (AI_translation\hindi\pi-1-hindi-plain-rails_split_chapters\, final and reviewed) wherever the Pāli matches.
Where the same Pāli occurs in different chapters, the Hindi must now be identical.

## Method (as the pi-1 pass)
Model: 0-INBOX\temp\pipeline\pi-1-hi\harmonise_hi.py and find_divergences_hi.py (read them; adapt paths and chapter list). Write pi-2-hi\harmonise_hi.py that applies fixed old → new strings to the Hindi chapter files, where a rule only touches a Hindi line whose aligned Pāli line (non-empty line i ↔ non-empty line i) matches the rule's Pāli pattern. Back up the pre-pass files to pi-2-hi\backup-pre-harmonise\ first, log every rule to pi-2-hi\harmonise-log.tsv (rule, chapter, replacements, lines). Line counts, IDs, heading levels and dashes must not change. Support --dry.
Do NOT rebuild with the builders (that would drop the pass); edit the outputs with the script. Note in pi-2-hi\harmonise-notes.md which builder constant would need the same change.

## Step 1: find divergences systematically
Write pi-2-hi\find_divergences_hi.py:
- (a) Whole segments: group segments across all chapters by their Pāli text (normalised: strip the ^id, variant brackets, collapse spaces); where the Pāli is identical but the Hindi differs, list them.
- (b) Lines and recurring phrases: the same for identical Pāli LINES and for frequent formula phrases (synonym strings, definitions, frames, headings).
Write the result to pi-2-hi\divergences.md. Also read every notes-*.md and compare their "Pāli = Hindi" lines: the same Pāli with different Hindi across notes is a divergence even if the lines are not identical.

## Step 2: decisions
Known divergences reported by the agents (decide each with the rule in item 8):
1. The Suttanta definitions of jāti, jarā, maraṇa, soka, parideva, dukkha, domanassa, upāyāsa (and the byasana / appiyehi sampayoga / piyehi vippayoga / yampicchaṃ strings) occur in ch4 (Sacca) and ch6 (Paṭiccasamuppāda): one wording.
2. dukkhanirodhagāminī paṭipadā: ch4 uses «… मार्ग» (pi-5); check every chapter and use one form.
3. Pañhāpucchaka (question-and-answer) predicates: chapters differ in how the predicate agrees (masculine plural to the implied subject, «ये …», «सभी क्षमताएँ …», or pi-1's «… परिघटनाएँ हैं»). Within one chapter the subject noun decides gender/number; but the SAME frame (siyā …, na vattabbā …, kenaci viññeyyā …) must have the same shape everywhere. Pick one shape per frame and apply it.
4. Niddesa headings: «व्याख्या» (ch9, ch16, ch17, pi-4) vs «… का विवरण» (ch6). One form.
5. Mātikā section headings: «एकल वर्गीकरण की मूल सूची» (ch16) vs «एकल प्रकारों की मूल सूची» (ch17), and the matching «दो-दो …», «तीन-तीन …» forms; also «Ekakaṃ / Dukaṃ / Tikaṃ / Catukkaṃ / Pañcakaṃ» headings («तीन-तीन के वर्गीकरण», «चार-चार / पाँच-पाँच की विधि» …). One scheme.
6. The upekkhā synonym string: ch12 «समभाव, समभाव रखना, उदासीन भाव से देखना, मन का संतुलन» vs ch5/7/10/11 «समभाव, समभाव रखना, तटस्थ भाव से देखना, मन की तटस्थता». Use pi-1's wording if pi-1 has this string; otherwise the majority.
7. akaniṭṭha: «अकनिष्ठ देवताओं» (pi-1 ^1-1287 ff.) vs «सबसे ऊँचे अकनिष्ठ देवताओं» (ch18 elsewhere). One form (prefer pi-1).
8. For every other divergence of identical Pāli: the approved sample and terms file win, then pi-1 Hindi (rails), then pi-3/4/5 Hindi, then the chapter with more occurrences. Renderings that differ because the Pāli differs, and source slips translated as written, stay.
9. Do not change the approved sample, preamble, or chapter/section headings fixed in the terms file.

## Step 3: apply and verify
Run harmonise_hi.py. Then run find_divergences_hi.py again: segment-level divergences (a) must be 0 except where the Pāli differs only inside variant brackets or the text was rightly kept as written (list those). For every chapter:
- `python -I 0-INBOX\temp\pipeline\check_chapter_ids.py AI_translation\pali\pi-2_split_chapters AI_translation\hindi\pi-2-hindi-plain-zeroshot_split_chapters` (all OK)
- `python -I -X utf8 0-INBOX\temp\pipeline\pi-1-hi\verify_hi.py <pali> <hindi>` (OK)
- preamble.md and the first 77 non-empty lines of 1-khandhavibhango.md unchanged vs backup.
Also grep the whole set for: «—», «:-», «धर्म», «seed», Latin letters outside [..] brackets.

## Final report (short)
Rules applied (count per rule and chapter), the choices you made under 1–8 with reasons, divergences left on purpose, check results, and anything that needs the user's eye.
