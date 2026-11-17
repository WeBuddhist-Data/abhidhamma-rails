# Brief: RAILS Russian translation, plain audience, pi-2 (Vibhaṅga): remaining chapters

## Setup
- Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write tools for files (write scripts with the Write tool, never via a shell redirect), PowerShell for commands, `python -I -X utf8`.
- Write ONLY your own chapter files, plus helper scripts and notes named after your chapters in 0-INBOX\temp\pipeline\pi-2-ru\rails\. Never create files at the repo root or in a system temp folder. Do not touch 1-SOURCES\ or 4-SYSTEM\, do not edit other agents' files or any pi-1 file, do not run git, never write "seed" or "unseeded". You cannot write report files for me: return your report as text.

## Read first
- AI_translation\skills\rails-verse-translator.md. Follow it.
- 0-INBOX\temp\pipeline\russian-style.md: register, typography («…»/„…“, no «ли»), the strict DASH RULE, structure. The book is «Подробный разбор».
- Translate FRESH from the Pāli, consulting the locked termbase term by term.
- Do NOT open the Russian pi-2 zero-shot (AI_translation\russian\pi-2-russian-plain-zeroshot_split_chapters\, pi-2-russian-plain-zeroshot.md), the zero-shot builders and notes in the pi-2-ru folder itself (build_*_ru.py, notes-*.md, ch1-sample.md, harmonise files) or the Russian side of the keyword maps (pi-2-ru\mapper-ru\*.mapped.md, pi-2-keywords-by-reference-pali-russian-plain.md). You MAY open pi-2-ru\ru-zeroshot-terms.md for the approved book title and chapter headings only.
- Models of house style and shared passages:
  - **The approved Russian pi-1 rails** (the Vibhaṅga's Abhidhamma and question sections repeat the Dhammasaṅgaṇī word for word): AI_translation\russian\pi-1-russian-plain-rails_split_chapters\ (1-matika.md has every triad and pair name), 0-INBOX\temp\pipeline\pi-1-ru\rails\ru-rails-formulas.md and its builders (build_rails_*_ru.py, constants; import them, never edit them). Where pi-2 has the same Pāli as pi-1, reuse the pi-1 Russian unless the pi-2 termbase or a pi-2 user decision says otherwise; report each such difference.
  - The finished Russian rails of other books (AI_translation\russian\pi-3-russian-plain.md, pi-4-…, pi-5-…).
  - For how a Vibhaṅga chapter is structured: the Hindi pi-2 rails builders. ref\hi_rails_build_rails_1.py is restored; for the other chapters restore what you need yourself into 0-INBOX\temp\pipeline\pi-2-ru\ref\ with
    `Start-Process -FilePath "$env:LOCALAPPDATA\GitHubDesktop\app-3.6.10\resources\app\git\cmd\git.exe" -ArgumentList @("show","08b7ff3~1:0-INBOX/temp/pipeline/pi-2-hi/rails/build_rails_<N>.py") -RedirectStandardOutput "<abs path>\ref\hi_rails_build_rails_<N>.py" -NoNewWindow -Wait`
    (this read-only `git show` is the only git command allowed).
  - Where any model disagrees with the pi-2 Russian termbase, the termbase wins.

## Inputs
- **Source:** AI_translation\pali\pi-2_split_chapters\<ch>.md
- **Locked termbase (authoritative, user-approved 2026-11-17):** AI_translation\russian\pi-2-pali-russian-termbase-plain.md, `pali: {english tag: русский; …}`, plus 0-INBOX\temp\pipeline\pi-2-ru\termbase\APPROVED.md (ajjhattaṃ / bahiddhā «внутренний» / «внешний»; its "For the rails step" notes: rūpataṇhā «жажда видимых форм» in the sense-object lists vs «жажда мира форм» for the fine-material sphere; sukhaṃ bodily pleasure in 2-594; upapattidevā; the text's own forms for muṭṭhassatī / appassuto).
  - Look up each Pāli word; pick the sense by its tag. Compounds and phrases often have their own entries; a compound without an entry is built from its members' entries.
  - Inflect grammatically (case, number, gender, verb agreement, short/long adjective), but never swap in a synonym.
  - If no sense fits, use the closest sibling entry and REPORT it.
- **The approved sample (user-approved 2026-11-17): the model for everything.**
  - AI_translation\russian\pi-2-russian-plain-rails_split_chapters\preamble.md (done; do not rewrite it).
  - 0-INBOX\temp\pipeline\pi-2-ru\rails\sample-1\1-sample.md: chapter 1 through ^2-33.
  - 0-INBOX\temp\pipeline\pi-2-ru\rails\ru-rails-formulas.md (READ-ONLY): every string in it is binding; copy it verbatim (the 18 chapter headings, the section headings, the aggregate definition frames, the N-vidhena lines «… на N видов» without «классификация»). 0-INBOX\temp\pipeline\pi-2-ru\rails\build_rails_sample_ru.py holds the same strings as Python constants: import it (`sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-ru\rails"); import build_rails_sample_ru as S`) instead of retyping them. Never edit it; importing writes nothing.
  - Terms the termbase lacks, as built in the sample (reuse them): dūre «вдали», santike «вблизи», āsanne «рядом», anāsanne «не рядом», upakaṭṭhe «поблизости», anupakaṭṭhe «не поблизости», avidūre «недалеко», asantike «не вблизи», samuppannaṃ «полностью возникший», anavaññātaṃ «не презренный», hīnasammataṃ / paṇītasammataṃ «признанный низшим / высшим», bhūtaṃ «ставший», viññāṇā (pl.) «виды сознания»; vuccanti «это называется». Tattha in questions = «здесь».
  - Source slips are translated as written (user).
- **Audience:** AI_translation\audience_profile\plain.md
- **Helper:** a builder script with fixed formula strings guarantees identical Russian for identical Pāli. The Vibhaṅga is extremely repetitive (the three methods of each chapter, the question sections, the -pe- runs): build your chapters with one (build_rails_<chapters>_ru.py).
- Any NEW recurring formula goes in rails\notes-<chapters>.md ("Pāli = Russian", one per line), not in the formulas file.
- **The chapter groups run ONE AT A TIME (user), in book order.** Before you start, read the finished earlier groups' rails builders and notes (0-INBOX\temp\pipeline\pi-2-ru\rails\build_rails_*_ru.py, rails\notes-*.md) and their output chapters: the same Pāli must get the same Russian, so import or copy their strings (never edit their files). Where your chapter repeats a passage an earlier rails chapter (pi-2 or pi-1) already has, reuse that Russian exactly.

## Output
AI_translation\russian\pi-2-russian-plain-rails_split_chapters\<ch>.md (the folder exists). 1-khandhavibhango.md only: its first 77 non-empty Pāli lines (^2-1-0 … ^2-33) are the approved sample; reuse sample-1\1-sample.md byte-for-byte as the start of the file and continue from the next segment.

## Rules
- **Block IDs:** exact, at the end of the last line of each segment, in the same order (including any odd IDs such as ^2-U…).
- **Headings:** keep their #-level.
- **Segments:** each has the source's number of non-empty lines; one blank line between segments; no double blank lines.
- **DASH RULE (user):** "–" only where the Pāli has "–" or "—", same spot, same count on every line. Never add one; no ":-".
- **Punctuation:** "…pe…" becomes "…". Statements end with ".". Questions end with "?", never with «ли». Quotes «…» / „…“.
- **Brackets:** «[вариант написания (Sī.): …]» for spelling-only variants, «[вариант чтения (…): …]» otherwise; (Ka)/(Kha)/(Ga) → (а)/(б)/(в). Translate editorial notes.
- **Translate the Pāli as written** (user rule): no emendations; only plain spelling slips may be rendered as meant. Report suspected slips.
- **Formulas:** identical Pāli gets identical Russian; where two segments differ only by a variant bracket or a numeral, the Russian differs only there.
- **Readability for a plain reader:** the long lists and -pe- runs must read as Russian sentences; recast where a literal string reads badly, keeping every term.

## Verify each chapter (all must pass)
```
python -I -X utf8 0-INBOX\temp\pipeline\check_chapter_ids.py AI_translation\pali\pi-2_split_chapters AI_translation\russian\pi-2-russian-plain-rails_split_chapters <ch>.md
python -I -X utf8 0-INBOX\temp\pipeline\dashcheck.py AI_translation\pali\pi-2_split_chapters\<ch>.md AI_translation\russian\pi-2-russian-plain-rails_split_chapters\<ch>.md
python -I -X utf8 0-INBOX\temp\pipeline\pi-1-ru\verify_ru.py AI_translation\pali\pi-2_split_chapters\<ch>.md AI_translation\russian\pi-2-russian-plain-rails_split_chapters\<ch>.md
```
Also: no «ли», no Latin outside variant brackets, no double blank lines, no CR, no em dash; 1-khandhavibhango starts with the sample byte-for-byte. Then termbase adherence (checks the segments present in the folder):
```
python -I -X utf8 0-INBOX\temp\pipeline\termbase_adherence.py AI_translation\pali\pi-2-keywords-by-reference-pali-plain.md AI_translation\russian\pi-2-pali-russian-termbase-plain.md AI_translation\russian\pi-2-russian-plain-rails_split_chapters
```
Fix genuine misses in your chapters; inflection and split phrases cause false misses, so read them with judgement.

## Final report (short, as text)
- Per chapter: checks passed, segment count, adherence result for your chapters.
- New formulas (also in your notes file).
- Strings reused from pi-1 and any place where the pi-2 termbase made you differ from pi-1.
- Termbase misfits (term, segment, why it does not fit, what you wrote).
- Unsure Pāli or source slips.
