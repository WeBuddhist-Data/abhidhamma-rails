# Brief: Pāli→Hindi keyword mapping for pi-2 (Vibhaṅga)

**Setup.**
- Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write tools for files, PowerShell for commands, `python -I -X utf8`, helper scripts written to files (inline `python -c` with regexes breaks in PowerShell).
- Write ONLY your own mapped files, plus helper scripts named after your chapters, inside 0-INBOX\temp\pipeline\pi-2-hi\mapper-hi\. Do not touch 1-SOURCES\ or 4-SYSTEM\, do not edit the translation, and do not run git.

**Read first.**
- AI_translation\skills\keyword-equivalence-mapper.md (the skill you execute).
- 0-INBOX\temp\pipeline\hindi-style.md (Hindi conventions, core terms).
- **pi-1 conventions (user-approved, binding here too):** 0-INBOX\temp\pipeline\pi-1-hi\mapper-hi\hi-map-conventions.md (dhammā = singular परिघटना; samaye X = «उस समय … X»; compounds and members; fragments; particles; matrix item names) and the shared tables in 0-INBOX\temp\pipeline\pi-1-hi\mapper-hi\map_common_hi.py (import it read-only; extend tables in YOUR OWN script).
- **The finished pi-1 Hindi map:** AI_translation\hindi\pi-1-keywords-by-reference-pali-hindi-plain.md. pi-2 reuses pi-1's Hindi wording for identical Pāli, so the same Pāli keyword in the same Hindi context gets the same value as in pi-1 (grep it).
- Format: AI_translation\hindi\pi-4-keywords-by-reference-pali-hindi-plain.md (30–40 lines).

**Per chapter <ch>:**
- **Keywords (Pāli):** 0-INBOX\temp\pipeline\pi-2-hi\mapper-hi\<ch>.keywords.md, `[id] kw1, kw2, …`.
- **Hindi translation:** AI_translation\hindi\pi-2-hindi-plain-zeroshot_split_chapters\<ch>.md (segments end with ^id). It is final (user-approved sample, harmonised).
- **Pāli source, for context:** AI_translation\pali\pi-2_split_chapters\<ch>.md.
- **Very helpful:** the Hindi was generated from the Pāli by builder scripts with fixed phrase tables: 0-INBOX\temp\pipeline\pi-2-hi\build_*_hi.py (+ their helper modules), hi-zeroshot-terms.md, notes-*.md, harmonise-log.tsv / harmonise-notes.md (the consistency pass changed some strings after the builders ran; the TRANSLATION FILE is the truth). The English map of the same book (AI_translation\english\pi-2-keywords-by-reference-pali-english-plain.md) shows how each Pāli keyword was read.
- **Output:** mapper-hi\<ch>.mapped.md. Same lines, same order, the same Pāli keywords in the same order, each written `pāli=हिंदी` (as in the pi-1/pi-4 Hindi maps).

**Rules (as approved for the Hindi pi-1/3/4/5 maps).**
- **Find the Hindi in that segment.** For each keyword, the word or phrase in THAT segment's Hindi that carries its meaning.
- **Dictionary form:** nouns in the direct case (singular, or plural if the concept is plural: परिघटनाओं → परिघटना); adjectives/participles masculine direct singular (जुड़ा, अलग) unless the concept is plural; verbs as infinitive (-ना) or the participle the text uses; strip postpositions and case markers (को, से, में, का/की/के, ने) unless part of the term.
- **Compounds and fragments:** keywords include whole compounds and their members. Map each to the Hindi part that renders it. A fragment that lost a negative prefix maps to the positive part.
- **Keep keywords exactly as given** (multiword, capitalised, odd forms alike). Never add, drop, merge or reorder them.
- **No direct equivalent:** if there is none in that segment, write `kw=(no direct equivalent)`.
- **Compare each segment for real.** Identical formulaic segments get identical mappings. A helper script with a mapping table plus per-segment overrides is fine (and recommended), but only after you have actually read the segments; every Hindi value must actually occur (as written or in a regular inflected form) in that segment's Hindi: check it with a script and list exceptions with reasons.
- **No ", " inside a Hindi value** (it is the separator). Drop the comma or use " / ".
- Core: dhamma=परिघटना; kusala=हितकर; akusala=हानिकर; abyākata=नैतिक रूप से अनिर्धारित; mātikā=मूल सूची; khandha=समूह.

**Verify each chapter** (replace CH). It must print `bad []`:
```
python -I -X utf8 -c "import pathlib;d=pathlib.Path('0-INBOX/temp/pipeline/pi-2-hi/mapper-hi');ch='CH';a=[l.split('] ',1) for l in (d/f'{ch}.keywords.md').read_text(encoding='utf-8').splitlines()];b=[l.split('] ',1) for l in (d/f'{ch}.mapped.md').read_text(encoding='utf-8').splitlines()];assert [x[0] for x in a]==[x[0] for x in b];bad=[i for (i,x),(_,y) in zip(a,b) if [k.strip() for k in x.split(', ')]!=[k.split('=',1)[0] for k in y.split(', ')]];print(ch,'lines',len(a),'bad',bad)"
```
Plus your presence check (every Hindi value found in that segment's Hindi, exceptions listed).

**Final report (short):** per chapter the line count, verifier result, number of (no direct equivalent), presence-check result, and genuinely unclear mappings.
