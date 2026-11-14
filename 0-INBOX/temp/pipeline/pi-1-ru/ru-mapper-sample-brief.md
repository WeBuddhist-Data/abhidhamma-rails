# Brief: Pāli→Russian keyword mapping, pi-1 (Dhammasaṅgaṇī): SAMPLE

Work in D:\Work\OpenPecha\abhidhamma-rails. Windows: Read/Write tools for files (write scripts with the Write tool, never via a shell redirect), PowerShell for commands, `python -I -X utf8`. Write ONLY inside 0-INBOX\temp\pipeline\pi-1-ru\mapper-ru\. Never create files at the repo root or in a system temp folder. Do not touch 1-SOURCES\ or 4-SYSTEM\, do not edit the translation, do not run git, never write "seed". You cannot write report files for me: return your report as text.

This sample (preamble, 1-matika, 2-01) is what the user reviews before the remaining parts are mapped in parallel. It sets the conventions the later agents copy.

## Read first
- AI_translation\skills\keyword-equivalence-mapper.md (the skill you execute).
- 0-INBOX\temp\pipeline\russian-style.md (Russian conventions, core terms).
- Approved Russian maps of earlier books (format and dictionary-form conventions; read 30–40 lines, grep for terms you meet): AI_translation\russian\pi-3/pi-4/pi-5-keywords-by-reference-pali-russian-plain.md, and the pi-5 brief 0-INBOX\temp\pipeline\pi-5-ru\mapper-brief.md (its rules are user-approved and binding here too).
- The Hindi map of this same book, as a model of how pi-1 was handled (conventions for dhammā, samaye, compounds, fragments, particles, matrix item names): 0-INBOX\temp\pipeline\pi-1-ru\ref\hi-map-conventions.md, ref\hi_map_common_hi.py, ref\hi_1-matika.mapped.md, ref\hi_2-01-cittuppadakandam.mapped.md. The English map AI_translation\english\pi-1-keywords-by-reference-pali-english-plain.md shows how each Pāli keyword was read.

## Per part (preamble, 1-matika, 2-01-cittuppadakandam)
- Keywords (Pāli): 0-INBOX\temp\pipeline\pi-1-ru\mapper-ru\<part>.keywords.md, `[id] kw1, kw2, …`.
- Russian translation: AI_translation\russian\pi-1-russian-plain-zeroshot_split_chapters\<part>.md (segments end with ^id). It is final (approved and harmonised); do not edit it.
- Pāli source, for context: AI_translation\pali\pi-1_split_chapters\<part>.md.
- Very helpful: the Russian was generated from the Pāli by builder scripts with fixed phrase tables: 0-INBOX\temp\pipeline\pi-1-ru\build_matika_ru.py, build_ch2_01_sample_ru.py, build_2-01_2-02_ru.py, ru-zeroshot-terms.md, notes-*.md. The consistency pass changed some strings afterwards (harmonise-log.tsv); the TRANSLATION FILE is the truth.
- Output: mapper-ru\<part>.mapped.md: the same lines, in the same order, with the same Pāli keywords in the same order, each written `pāli=русский`.

## Also write (for the parallel agents)
- mapper-ru\ru-map-conventions.md: the conventions you settled (dhammā; samaye X = «в это время … X»; compounds and their members; fragments; particles; matrix item names; dictionary forms), modelled on the Hindi conventions file.
- mapper-ru\map_common_ru.py: shared tables (core terms, factor names, matrix items) and a presence check (every Russian value found in that segment's Russian, as written or in a regular inflected form), modelled on hi_map_common_hi.py. Later agents will import it.
- mapper-ru\map_sample_ru.py: your mapping table plus per-segment overrides for the three parts.

## Rules (user-approved for the Russian pi-3/4/5 maps)
- **Find the Russian in that segment.** For each keyword, the word or phrase in THAT segment's Russian that carries its meaning.
- **Dictionary form:** nouns nominative (plural kept if the concept is plural); adjectives/participles nominative masculine singular unless the concept is plural; verbs infinitive or the participle the text uses. Do not copy case-inflected forms.
- **Compounds and fragments:** keywords include whole compounds and their members (e.g. `cittamudutā`, `mudutā`, `citta`). Map each to the Russian part that renders it (cittamudutā=мягкость ума, mudutā=мягкость, citta=ум). A fragment that lost a negative prefix maps to the positive part.
- **Keep keywords exactly as given** (multiword, capitalised, odd forms). Never add, drop, merge or reorder.
- **No direct equivalent:** if there is none in that segment (the word appears only inside a variant bracket kept in Pāli, or a particle has no Russian word), write `kw=(no direct equivalent)`.
- **Compare each segment for real.** The same Pāli word may map differently by context. Identical formulaic segments get identical mappings. A table plus per-segment overrides is fine, but only after you have read the segments; check presence by script and list exceptions with reasons.
- **No ", " inside a Russian value** (it is the separator). Drop the comma or use " / ".
- Core (approved): dhamma = явление; kusala = благой; akusala = неблагой; abyākata = этически неопределённый; mātikā = матрица; vicāra = удержание мысли; saṅkhāra (aggregate) = формирующие факторы; dosa = злоба; asaṅkhata = необусловленное; cittuppāda = вид ума (ch5) / возникновение ума (ch2 heading).

## Verify each part (replace PART); it must print `bad []`
```
python -I -X utf8 -c "import pathlib;d=pathlib.Path('0-INBOX/temp/pipeline/pi-1-ru/mapper-ru');ch='PART';a=[l.split('] ',1) for l in (d/f'{ch}.keywords.md').read_text(encoding='utf-8').splitlines()];b=[l.split('] ',1) for l in (d/f'{ch}.mapped.md').read_text(encoding='utf-8').splitlines()];assert [x[0] for x in a]==[x[0] for x in b];bad=[i for (i,x),(_,y) in zip(a,b) if [k.strip() for k in x.split(', ')]!=[k.split('=',1)[0] for k in y.split(', ')]];print(ch,'lines',len(a),'bad',bad)"
```
Plus your presence check (every Russian value found in that segment's Russian; exceptions listed with reasons).

## Report (under 400 words, as text)
Per part: line count, verifier result, number of (no direct equivalent), presence-check result. The main conventions you settled. 10–15 example mappings for review (a factor name, a compound and its members, a synonym-string word, a matrix item, a particle). Genuinely unclear mappings.
