# Brief: Pāli→Hindi keyword mapping for pi-1 (Dhammasaṅgaṇī)

**Setup.**
- Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write tools for files, PowerShell for commands, `python -I -X utf8`, helper scripts written to files (inline `python -c` with regexes breaks in PowerShell).
- Write ONLY your own mapped files, plus helper scripts named after your parts, inside 0-INBOX\temp\pipeline\pi-1-hi\mapper-hi\. Do not touch 1-SOURCES\ or 4-SYSTEM\, do not edit the translation, and do not run git.

**Read first.**
- AI_translation\skills\keyword-equivalence-mapper.md (the skill you execute).
- 0-INBOX\temp\pipeline\hindi-style.md (Hindi conventions, core terms).
- The approved format and conventions: AI_translation\hindi\pi-4-keywords-by-reference-pali-hindi-plain.md and pi-5-…-plain.md (the same step for earlier Hindi books; look at 30–40 lines, and grep them for terms you meet).

**The user approved the sample (preamble, 1-matika, 2-01).** Binding for all other parts:
- mapper-hi\hi-map-conventions.md (READ-ONLY): the settled conventions (dhammā = singular परिघटना; samaye X = «उस समय … X»; compounds and members; fragments; particles; matrix item names). Follow it exactly.
- mapper-hi\map_common_hi.py (READ-ONLY): shared tables and the presence check; import it (`sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-hi\mapper-hi")`). Extend its tables in YOUR OWN script, not in the shared file.
- The approved sample maps (preamble/1-matika/2-01 .mapped.md): the same Pāli keyword in the same Hindi context gets the same value.
- New recurring decisions go in mapper-hi\notes-map-<your parts>.md, one "pāli = हिंदी (context)" per line.

**Per part <part>:**
- **Keywords (Pāli):** 0-INBOX\temp\pipeline\pi-1-hi\mapper-hi\<part>.keywords.md, `[id] kw1, kw2, …`.
- **Hindi translation:** AI_translation\hindi\pi-1-hindi-plain-zeroshot_split_chapters\<part>.md (segments end with ^id). It is final (user-approved, harmonised).
- **Pāli source, for context:** AI_translation\pali\pi-1_split_chapters\<part>.md.
- **Very helpful:** the Hindi was generated from the Pāli by builder scripts with fixed phrase tables: 0-INBOX\temp\pipeline\pi-1-hi\build_*_hi.py, hi-zeroshot-terms.md, notes-*.md, harmonise-log.tsv / harmonise-notes-hi.md (the consistency pass changed some strings after the builders ran; the TRANSLATION FILE is the truth). The tables show exactly which Pāli produced which Hindi phrase. The English map of the same book (AI_translation\english\pi-1-keywords-by-reference-pali-english-plain.md) shows how each Pāli keyword was read.
- **Output:** mapper-hi\<part>.mapped.md. Same lines, same order, the same Pāli keywords in the same order, each written `pāli=हिंदी` (as in the pi-4/pi-5 Hindi maps).

**Rules (as approved for the Hindi pi-3/4/5 maps).**
- **Find the Hindi in that segment.** For each keyword, the word or phrase in THAT segment's Hindi that carries its meaning.
- **Dictionary form:** nouns in the direct case (singular, or plural if the concept is plural: परिघटनाओं → परिघटना); adjectives/participles masculine direct singular (जुड़ा, अलग) unless the concept is plural; verbs as infinitive (-ना) or the participle the text uses; strip postpositions and case markers (को, से, में, का/की/के, ने) unless part of the term (e.g. «इंद्रिय-सुखों के लोक से संबंधित» is one term for kāmāvacara).
- **Compounds and fragments:** keywords include whole compounds and their members (e.g. `cittamudutā`, `mudutā`, `citta`). Map each to the Hindi part that renders it (cittamudutā=मन की मृदुता, mudutā=मृदुता, citta=मन). A fragment that lost a negative prefix maps to the positive part. The user prefers whole compounds to cut non-word fragments; if a keyword is a stem/fragment, still map it to the Hindi for that meaning.
- **Keep keywords exactly as given** (multiword, capitalised, odd forms alike). Never add, drop, merge or reorder them.
- **No direct equivalent:** if there is none in that segment (e.g. the word appears only inside a variant bracket kept in Pāli, or a particle has no Hindi word), write `kw=(no direct equivalent)`.
- **Compare each segment for real.** The same Pāli word may map differently by context. Identical formulaic segments get identical mappings. A helper script with a mapping table plus per-segment overrides is fine (and recommended for these formulaic chapters), but only after you have actually read the segments; every Hindi value must actually occur (as written or in a regular inflected form) in that segment's Hindi: check it with a script and list exceptions with reasons.
- **No ", " inside a Hindi value** (it is the separator). Drop the comma or use " / ".
- Core: dhamma=परिघटना; kusala=हितकर; akusala=हानिकर; abyākata=नैतिक रूप से अनिर्धारित; mātikā=मूल सूची.

**Verify each part** (replace PART). It must print `bad []`:
```
python -I -X utf8 -c "import pathlib;d=pathlib.Path('0-INBOX/temp/pipeline/pi-1-hi/mapper-hi');ch='PART';a=[l.split('] ',1) for l in (d/f'{ch}.keywords.md').read_text(encoding='utf-8').splitlines()];b=[l.split('] ',1) for l in (d/f'{ch}.mapped.md').read_text(encoding='utf-8').splitlines()];assert [x[0] for x in a]==[x[0] for x in b];bad=[i for (i,x),(_,y) in zip(a,b) if [k.strip() for k in x.split(', ')]!=[k.split('=',1)[0] for k in y.split(', ')]];print(ch,'lines',len(a),'bad',bad)"
```
Plus your presence check (every Hindi value found in that segment's Hindi, exceptions listed).

**Final report (short):** per part the line count, verifier result, number of (no direct equivalent), presence-check result, and genuinely unclear mappings.
