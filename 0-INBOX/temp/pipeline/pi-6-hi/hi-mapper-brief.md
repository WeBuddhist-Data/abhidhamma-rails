# Brief: Pāli→Hindi keyword mapping for pi-6 (Yamaka)

**Setup.**
- Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write tools for files, PowerShell for commands, `python -I -X utf8`, helper scripts written to files (inline `python -c` with regexes breaks in PowerShell).
- Write ONLY your own mapped files, plus helper scripts named after your files, inside 0-INBOX\temp\pipeline\pi-6-hi\mapper-hi\. Never create files at the repo root. Do not touch 1-SOURCES\ or 4-SYSTEM\, do not edit the translation, and do not run git. Never write "seed" or "unseeded".

**Read first.**
- AI_translation\skills\keyword-equivalence-mapper.md (the skill you execute).
- 0-INBOX\temp\pipeline\hindi-style.md (Hindi conventions, core terms).
- **Binding conventions from the approved maps:** 0-INBOX\temp\pipeline\pi-1-hi\mapper-hi\hi-map-conventions.md (dhammā = singular परिघटना; compounds and members; fragments; particles) and 0-INBOX\temp\pipeline\pi-2-hi\mapper-hi\hi-map-conventions-pi2.md, plus their table modules (pi-1-hi\mapper-hi\map_common_hi.py, pi-2-hi\mapper-hi\map_sample_hi.py: import read-only; extend tables in YOUR OWN script).
- **Finished Hindi maps:** AI_translation\hindi\pi-1-keywords-by-reference-pali-hindi-plain.md and pi-2-keywords-by-reference-pali-hindi-plain.md. The same Pāli keyword in the same Hindi context gets the same value (grep them).
- **pi-6 conventions (once the sample is approved):** 0-INBOX\temp\pipeline\pi-6-hi\mapper-hi\hi-map-conventions-pi6.md and the sample's table module map_sample_hi.py in the same folder (import read-only).

**Per file <f>:**
- **Keywords (Pāli):** 0-INBOX\temp\pipeline\pi-6-hi\mapper-hi\<f>.keywords.md, `[id] kw1, kw2, …`.
- **Hindi translation:** AI_translation\hindi\pi-6-hindi-plain-zeroshot_split_chapters\<f>.md (segments end with ^id). It is final (user-approved sample, harmonised).
- **Pāli source, for context:** AI_translation\pali\pi-6_split_chapters\<f>.md.
- **Very helpful:** the Hindi was generated from the Pāli by builder scripts with fixed phrase tables: 0-INBOX\temp\pipeline\pi-6-hi\build_*_hi.py (+ common modules), build_sample_hi.py, hi-zeroshot-terms.md, notes-*.md, and harmonise-log.tsv / harmonise-notes.md (the consistency pass changed strings after the builders ran; the TRANSLATION FILE is the truth). The English map of the same book (AI_translation\english\pi-6-keywords-by-reference-pali-english-plain.md) shows how each Pāli keyword was read.
- **Output:** mapper-hi\<f>.mapped.md. Same lines, same order, the same Pāli keywords in the same order, each written `pāli=हिंदी`.

**Rules (as approved for the Hindi pi-1/2/3/4/5 maps).**
- **Find the Hindi in that segment.** For each keyword, the word or phrase in THAT segment's Hindi that carries its meaning.
- **Dictionary form:** nouns in the direct case (singular, or plural if the concept is plural: परिघटनाओं → परिघटना); adjectives/participles masculine direct singular unless the concept is plural; verbs as infinitive (-ना) or the participle the text uses (उत्पन्न होना, समाप्त होना); strip postpositions and case markers (को, से, में, का/की/के, ने) unless part of the term.
- **Compounds and fragments:** keywords include whole compounds and their members. Map each to the Hindi part that renders it. A fragment that lost a negative prefix maps to the positive part.
- **Keep keywords exactly as given** (multiword, capitalised, odd forms alike). Never add, drop, merge or reorder them.
- **No direct equivalent:** if there is none in that segment, write `kw=(no direct equivalent)`.
- **Compare each segment for real.** Identical formulaic segments get identical mappings. A helper script with a mapping table plus per-segment overrides is fine (and recommended for this very repetitive book), but only after you have actually read the segments; every Hindi value must actually occur (as written or in a regular inflected form) in that segment's Hindi: check it with a script and list exceptions with reasons.
- **No ", " inside a Hindi value** (it is the separator). Drop the comma or use " / ".
- Core: dhamma=परिघटना; kusala=हितकर; akusala=हानिकर; abyākata=नैतिक रूप से अनिर्धारित; khandha=समूह; mātikā=मूल सूची.
- pi-6 specifics: bare words in the word-checking pairs keep their bare Hindi (rūpaṃ=रूप, saṅkhārā=रचनाएँ) while the khandha/āyatana/dhātu/indriya names get the full term; hetu=हेतु, mūla=मूल.

**Verify each file** (replace F). It must print `bad []`:
```
python -I -X utf8 -c "import pathlib;d=pathlib.Path('0-INBOX/temp/pipeline/pi-6-hi/mapper-hi');ch='F';a=[l.split('] ',1) for l in (d/f'{ch}.keywords.md').read_text(encoding='utf-8').splitlines()];b=[l.split('] ',1) for l in (d/f'{ch}.mapped.md').read_text(encoding='utf-8').splitlines()];assert [x[0] for x in a]==[x[0] for x in b];bad=[i for i,(x,y) in enumerate(zip(a,b)) if len(x)>1 and [k.strip() for k in x[1].split(', ')]!=[k.split('=',1)[0] for k in y[1].split(', ')]];print(ch,'lines',len(a),'bad',bad)"
```
(Lines with only an ID and a heading keyword still have one keyword; lines without keywords, if any, must stay as they are.) Plus your presence check (every Hindi value found in that segment's Hindi, exceptions listed).

**Final report (short):** per file the line count, verifier result, number of (no direct equivalent), presence-check result, and genuinely unclear mappings.
