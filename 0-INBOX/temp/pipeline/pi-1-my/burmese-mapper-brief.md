# Brief: Pāli→Burmese keyword mapping (pi-1, Dhammasaṅgaṇī «သဘောတရားများကို စုစည်းရေတွက်ခြင်း»)

**Setup.**
- Work in /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails on macOS (zsh). Use the Read/Write tools for files and run Python as `python3 -I -X utf8`; write helper scripts to files, not inline `-c` with regexes.
- Write ONLY your own mapped files and helper scripts inside `0-INBOX/temp/pipeline/pi-1-my/mapper-my/`. Never use the system temp directory. Don't commit. Never use the words for a planted starting value or its negative.
- Source rule: never look up or use any existing Burmese translation, nissaya or web source. Everything comes from the Burmese text of this track.

**Read first.**
- `AI_translation/skills/keyword-equivalence-mapper.md` (the skill you execute).
- `0-INBOX/temp/pipeline/burmese-style.md` (Burmese conventions and approved core terms).
- `0-INBOX/temp/pipeline/pi-1-my/my-zeroshot-terms.md`, `harmonise-table.tsv` and `harmonise-notes.md`: the forms the translation uses. The text is FINAL (consistency pass done): map against the CURRENT chapter files.
- Method model: the pi-1 Marathi mapper `0-INBOX/temp/pipeline/pi-1-mr/mapper-mr/map_all.py` and `map-table.md` (a table T of keyword → target, per-segment overrides CTX, accepted stems, and a built-in verifier), plus the Marathi rules in `0-INBOX/temp/pipeline/pi-1-mr/marathi-mapper-brief.md`. Copy the approach into your own script; do not import it. The Marathi values are not Burmese: never copy them.

**Per chapter <ch>.**
- Keywords: `mapper-my/<ch>.keywords.md`, `[id] kw1, kw2, ...` (Pāli).
- Burmese (CURRENT text): `AI_translation/burmese/pi-1-burmese-plain-zeroshot_split_chapters/<ch>.md`. Segments end with ^id.
- Pāli source, for context: `AI_translation/pali/pi-1_split_chapters/<ch>.md`.
- Output: `mapper-my/<ch>.mapped.md`. Same lines, same order, the same keywords in the same order, each written `pali=ဗမာ`.
- Hard cases: the English mapping `AI_translation/english/pi-1-keywords-by-reference-pali-english-plain.md` and the Marathi `AI_translation/marathi/pi-1-keywords-by-reference-pali-marathi-plain.md` show how fragments and multiword keywords were handled; the Burmese itself must come from the Burmese translation.

**Rules.**
- Find, in THAT segment's Burmese, the word or phrase that carries the keyword's meaning.
- Give it in DICTIONARY form, Burmese style (propose and document the exact rules in your table file; the user reviews them with this sample):
  - Nouns without case particles and postpositions (၏, ကို, ၌, တွင်, နှင့်, မှ, ဖြင့်, အား, သို့, သည်, က …) and without plural markers (များ, တို့) for a bare keyword: dhammā = သဘောတရား. A keyword with a numeral keeps the count the text uses. A genitive that is part of the term stays (e.g. «X၏ စွမ်းရည်»).
  - Adjectival / participial keywords: the attributive phrase as the text builds it, ending in «သော» (sampayuttā = «…နှင့် ယှဉ်တွဲသော» with its object if the keyword includes it), without the head noun သဘောတရား.
  - Verbs: one fixed dictionary form, e.g. verb + «သည်» (uppajjati = ဖြစ်ပေါ်သည်); decide and document.
  - Drop sentence-final material (။, ဖြစ်ကြသည်, ဖြစ်သည်) unless it is the keyword's meaning.
- Discontinuous keywords join the parts with « … ».
- Context decides the sense (rūpa as matter = ရုပ်, as visible object = အဆင်းအရောင်; bahiddhā «in others» vs «outside»; paṭigha aversion vs impact), as harmonise-notes.md records.
- Fragments that lost a negative prefix map to the positive part.
- Keep keywords exactly as given (multiword, capitalised, odd fragments). Never add, drop, merge or reorder them. The keyword files may repeat keywords: every repeat gets the same value.
- No direct equivalent in that segment (only inside a Pāli variant bracket, or a particle with no Burmese word): `kw=(no direct equivalent)`.
- Identical formulaic segments get identical mappings. A table plus per-segment overrides is the expected method, after you have actually read the segment types.
- No ", " inside a Burmese value (use « / » only for genuine alternatives). Burmese «၊» inside a value is also not allowed.

**Verify each chapter (all must pass).**
1. Keyword preservation, which must print `bad []`:
```
python3 -I -X utf8 -c "import pathlib;d=pathlib.Path('0-INBOX/temp/pipeline/pi-1-my/mapper-my');ch='CH';a=[l.split('] ',1) for l in (d/f'{ch}.keywords.md').read_text(encoding='utf-8').splitlines()];b=[l.split('] ',1) for l in (d/f'{ch}.mapped.md').read_text(encoding='utf-8').splitlines()];assert [x[0] for x in a]==[x[0] for x in b];bad=[i for (i,x),(_,y) in zip(a,b) if [k.strip() for k in x.split(', ')]!=[k.split('=',1)[0] for k in y.split(', ')]];print(ch,'lines',len(a),'bad',bad)"
```
2. Presence: every space-separated chunk of every value occurs in that segment's Burmese (allowing only for the particles your dictionary-form rules strip). Your script runs this; list and justify every exception.
3. No ", " and no «၊» inside any value.

**Approved sample (user, 2026-11-17): binding for all later chapters.**
- The dictionary-form rules in `mapper-my/map-table.md` (rules 1–11) and the values in `preamble.mapped.md` / `1-matika.mapped.md` are approved. The same keyword in the same kind of segment keeps the sample's value; Mātikā items quoted in later chapters keep the 1-matika values.
- Parallel agents: do NOT edit `map_all.py`, `map-table.md` or the sample outputs. Write your own `mapper-my/map_<your chapters>.py`, copying (not importing, if importing would run it) the sample's tables, compose rules, context functions and verifier; register only your chapters; write `mapper-my/map-table-<your chapters>.md` with any NEW rule or value (each new rule explained).
- `show_seg.py` is a read-only helper you may use.

**Final report (short):** per chapter the line count, the verifier results and the number of (no direct equivalent); the dictionary-form rules you chose (for the user's review); mappings that are genuinely unclear.
