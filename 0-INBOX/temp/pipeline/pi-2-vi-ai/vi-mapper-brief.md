# Brief: Pāli→Vietnamese keyword mapping for pi-2 (Vibhaṅga), remaining parts

Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write/Edit tools for files (write scripts with the Write tool at their full paths; never write files from PowerShell), PowerShell for commands, `python -I -X utf8`. Agents map the parts ONE AT A TIME, in book order; earlier parts are finished. Write ONLY your own mapped files, plus helper scripts and notes named after your parts, inside 0-INBOX\temp\pipeline\pi-2-vi-ai\mapper-vi\. Never create files at the repo root or in a system temp folder. Do not touch 1-SOURCES\ or 4-SYSTEM\, do not edit the translation, do not edit earlier agents' files, never run git (not even git status), never write "seed". You cannot write report files for me: return your report as text.

## FORBIDDEN (copyrighted reference translation)
Never open, grep or search: 1-SOURCES\Translations\Vietnamese\ (any file), 0-INBOX\raw-data\vi-*, 0-INBOX\temp\pipeline\pi-1-vi\, pi-2-vi\, pi-3-4-vi\, pi-5-vi\, pi-6-vi\, pi-7-vi\, pi-1-th-vi\, vi-tools\. No folder-wide searches over 0-INBOX\temp\pipeline\, 1-SOURCES\ or AI_translation\ (search only the specific files named here).

## Read first (binding)
- AI_translation\skills\keyword-equivalence-mapper.md (the skill you execute).
- 0-INBOX\temp\pipeline\vietnamese-style.md (Vietnamese conventions, core terms, sati = «sự tỉnh thức»).
- **Conventions (user-approved):**
  - pi-1: 0-INBOX\temp\pipeline\pi-1-vi-ai\mapper-vi\vi-map-conventions.md (READ-ONLY): value form (frame words «các» / «những», existential «có», predicate «là» dropped; nominalisers kept as the text has them), discontinuous values with " … ", compounds and members, fragments that lost a negative prefix = the positive Vietnamese word, `(no direct equivalent)` only as defined there, Yo/Yā/Yaṃ, matrix items, factor names, synonym strings, question frames.
  - pi-2 additions, approved with the sample on 2026-11-18: mapper-vi\vi-map-conventions-pi2.md (READ-ONLY): N-vidhena «theo nhóm N»; the X-niyo family «đối tượng của X» …; vuccati X «được gọi là X»; Yaṃ kiñci «bất cứ … nào»; X ceva X-sampayutto «vừa là X vừa gắn liền với X»; siyā «đôi khi»; paccayā «do … làm điều kiện»; saha «cùng»; Vibhaṅga = the whole title.
- **Tooling (READ-ONLY):** mapper-vi\map_common_vi.py (pi-2 paths; reuses pi-1's present() and tables; build_part(), verify()) and mapper-vi\map_sample_vi.py. Import them (`sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-vi-ai\mapper-vi")`). Extend tables in YOUR OWN script (`map_<parts>_vi.py`), never in the shared files. Earlier agents' map scripts can be imported the same way; importing must not rewrite their outputs (or any pi-1 output).
- The approved maps (preamble / 1-khandhavibhango .mapped.md) and the mapped files and notes-map-*.md of earlier pi-2 parts: the same Pāli keyword in the same Vietnamese context gets the same value.
- The pi-1 Vietnamese keyword map AI_translation\vietnamese\pi-1-keywords-by-reference-pali-vietnamese-plain.md (grep, don't read whole): where a pi-2 segment repeats pi-1 Pāli with the same Vietnamese (matrix items, mind-state definitions, synonym strings, jhāna formulas), the same keyword gets the same value. mapper-vi\pi1_lookup_vi.py helps.
- Cross-check of how each Pāli keyword was read (meaning only, not Vietnamese wording): the Russian pi-2 map 0-INBOX\temp\pipeline\pi-2-ru\mapper-ru\<part>.mapped.md and its notes-map-*.md; the English pi-2 map AI_translation\english\pi-2-keywords-by-reference-pali-english-plain.md (grep, don't read whole).

## Per part
- Keywords (Pāli): mapper-vi\<part>.keywords.md, `[id] kw1, kw2, …`.
- Vietnamese translation: AI_translation\vietnamese\pi-2-vietnamese-plain-zeroshot_split_chapters\<part>.md (segments end with ^id). It is final for this step (harmonised); do not edit it.
- Pāli source, for context: AI_translation\pali\pi-2_split_chapters\<part>.md.
- Very helpful: the Vietnamese was generated from the Pāli by builder scripts with fixed phrase tables: 0-INBOX\temp\pipeline\pi-2-vi-ai\build_ch1_sample_vi.py, build_1_vi.py, build_2-3_vi.py, build_4-5_vi.py, build_6_vi.py, build_7-9_vi.py, build_10-12_vi.py, build_13-15_vi.py, build_16_vi.py, build_17_vi.py, build_18_vi.py, with notes-<chapters>.md and vi-zeroshot-terms.md. The harmonise pass changed some strings afterwards (pi-2-vi-ai\harmonise-log.tsv lists every old → new: e.g. rajataṃ «đồng tiền», āghātavatthu «chỗ dựa», nāma/rūpa «phần vật chất», ^2-171 the doubled negation, counted questions «… là những gì?»); the TRANSLATION FILE is the truth.
- Output: mapper-vi\<part>.mapped.md: the same lines, in the same order, with the same Pāli keywords in the same order, each `pāli=tiếng Việt`. Write it with `build_part()`.
- New recurring decisions go in mapper-vi\notes-map-<your parts>.md, one "pāli = tiếng Việt (context)" per line.

## Rules (user-approved)
- For each keyword, the word or phrase in THAT segment's Vietnamese that carries its meaning, copied as it stands there, in the value form of the conventions.
- Keep keywords exactly as given (multiword, capitalised, odd forms). Never add, drop, merge or reorder.
- `(no direct equivalent)` only as defined in the pi-1 conventions (particle with no Vietnamese word, word only inside a variant bracket kept in Pāli, fragment whose positive part is not a Vietnamese word, keyword with no word of its own in the Vietnamese).
- Compare each segment for real; the same Pāli word may map differently by context (e.g. kāmadhātu «yếu tố dục lạc» in ch3 vs «cõi dục lạc» in ch18; sukha «hạnh phúc» as jhāna factor vs «dễ chịu» as feeling; viharati «sống» vs «an trú»); identical formulaic segments get identical mappings. A table plus per-segment overrides is fine, but only after reading the segments.
- Where the Vietnamese renders a source slip as written (the chapter notes list them; e.g. ^2-171, ^2-485, ^2-641, ^2-809 atthato, ^2-1031), map to what the Vietnamese says.
- No ", " inside a value (drop the comma, or " / " for alternatives).
- Core: dhamma = hiện tượng (the Teaching = Giáo Pháp); kusala = thiện; akusala = bất thiện; abyākata = không xác định về mặt đạo đức; khandha = khối; rūpa (matter) = vật chất; vedanā = cảm giác; saññā = tri giác; saṅkhāra = tạo tác; viññāṇa = thức; vitakka = sự hướng tâm; vicāra = sự duy trì tâm; sati = sự tỉnh thức; mātikā = ma trận.

## Verify each part; it must print `bad []` and 0 presence misses
`python -I -X utf8 0-INBOX\temp\pipeline\pi-2-vi-ai\mapper-vi\check_parts_vi.py <part> [<part> …]` (structure: same IDs, same keywords in the same order; plus verify(): every Vietnamese value found in that segment's Vietnamese). List any exception with its reason. Also hash the earlier mapped files (pi-1 and pi-2) before and after your run: they must be unchanged.

## Final report (short, as text, under 350 words)
Per part: line count, verifier result, number of (no direct equivalent), presence-check result. New conventions you needed (also in your notes file). Genuinely unclear mappings.
