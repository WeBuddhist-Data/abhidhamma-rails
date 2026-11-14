# Russian plain translations: shared style rules (pi-1 onward)

Written 2026-11-14 for pi-1, from the approved Russian pi-3, pi-4 and pi-5 work and the pi-5 bilingual review (0-INBOX\temp\pipeline\pi-5-ru\fix-brief.md). Every Russian brief points here.

Audience: AI_translation\audience_profile\plain.md. Readers have little or no Buddhist background. Write clear, modern, natural Russian. Minor clarification through wording is OK, but add nothing that is absent from the source. Priority: understanding > accuracy > readability > consistency.

## Language and vocabulary
- Modern standard Russian in a plain register. Prefer common words; avoid Church-Slavonic or archaic phrasing and needless loanwords.
- **Technical terms:** translate the concept into understandable Russian. No bare transliterations of opaque Pāli terms (khandha, āyatana, dhātu …). Established Russian Buddhist words stay: Будда, Благословенный, архат, нирвана, монах.
- **Book titles:** the Russian name only, no Pāli name and no bracketed gloss: «Беседа об элементах», «Описание типов людей», «Предметы обсуждения». Mid-sentence, put the title in «…». Citation brackets such as [Пуггалапаннятти 131] stay as references. Frontmatter `title:` uses a normal hyphen: `Беседа об элементах - простой русский`.
- Natural Russian grammar, case government and agreement. Keep the chosen word for a term consistent.

## Typography
- Statements end with ".". Questions end with "?". **No «ли»** in questions (user rule from pi-3): «Во сколько совокупностей включена?», not «Включена ли …?». Use intonation or a question word instead.
- Quotes: «…» outer, „…“ nested.
- **DASH RULE (user, strict):** "–" or "—" appears ONLY where the Pāli has "–" or "—", at the same spot and with the same count on every line. Russian normally writes a dash for a missing copula («X — это Y») or before a summarising word; here that is forbidden. Rephrase: «X является Y», «X: Y», a comma, or a reordered sentence. No ":-".
- "…pe…" becomes "…" at the same spot.
- **Digits:** where the Pāli has digits, e.g. "(1)", keep them. Numbers written as Pāli words become Russian words.
- **Variant brackets:** keep the sigla and the variant's Pāli, translate the label:
  - «[вариант чтения (Sī., Syā.): …]» when a word differs;
  - «[вариант написания (Syā.): …]» for spelling-only differences.
- Translate editorial notes in square brackets.

## Structure (hard rules)
- Every block ID stays exactly as in the source, at the end of the last line of its segment, in the same order.
- Headings keep their #-level.
- Each segment has exactly the source's number of non-empty lines, one blank line between segments, no double blank lines, no CR characters.
- Identical Pāli formulas get identical Russian. Use a builder script with fixed formula strings.
- Translate FROM THE PĀLI. The English and Hindi zero-shots and their builders are a cross-check of meaning and structure only.
- Translate the Pāli as written: no emendations of apparent slips; only plain spelling slips may be rendered as meant. Report suspected slips.
- Never write "seed" or "unseeded".

## Cross-book core terms (approved in pi-3/4/5; the pi-5 review decisions win)

### Text frame
- Namo tassa bhagavato arahato sammāsambuddhassa = Почтение Благословенному, Достойному, Полностью Пробуждённому Будде
- Abhidhammapiṭake = В корзине Абхидхаммы

### Core Abhidhamma terms
- dhamma (phenomenon) = явление; dhamma (the Teaching) = Учение.
- khandha = совокупность; āyatana = сфера восприятия; dhātu = элемент; sacca = истина; indriya = способность.
- rūpa (matter) = материальная форма; rūpa (visible object) = видимая форма.
- citta = ум; cetasika = сопутствующее уму; viññāṇa = сознание.
- vedanā = чувство; saññā = восприятие; cetanā = намерение; phassa = контакт; manasikāra = внимание; adhimokkha = решимость.
- saddhā = вера; vīriya = усердие (vīriyindriya = способность усердия); sati = осознанность; samādhi = сосредоточение; paññā = мудрость.
- jhāna = медитативное погружение.
- vitakka = направленная мысль.
- pīti = восторг; sukha = счастье; upekkhā = невозмутимость.
- kusala / akusala = благой / неблагой.
- **abyākata = этически неопределённый** (never «нейтральный»). vipākābyākata = «этически неопределённый, являющийся результатом действий»; kiriyābyākata = «этически неопределённый функциональный».
- hetu (root) = корень; āsava = влечение; saṃyojana = оковы; gantha = узы; ogha = поток; yoga = ярмо; nīvaraṇa = помеха; parāmāsa = искажение; upādāna = цепляние; kilesa = омрачение.
- lobha = жадность; moha = заблуждение; avijjā = неведение; taṇhā = жажда; diṭṭhi = воззрение; māna = самомнение; thina / middha = вялость / сонливость; hiri / ottappa = совестливость / страх перед дурным.
- lokiya / lokuttara = мирской / надмирский.

### Path, beings and attainments
- ariya = благородный; magga / phala = путь / плод.
- sotāpanna = вошедший в поток; arahant = архат; arahatta = состояние архата (never «архатство»).
- nibbāna = нирвана; bhagavā = Благословенный; bhikkhu = монах; puggala = личность (pi-4 descriptions of persons: человек).
- kappa = эпоха.

### Lessons from the Russian bilingual review (binding)
- Keep these pairs distinct, one word each, never swapped:
  - vicikicchā = колебание vs kaṅkhā = сомнение;
  - mettā = доброжелательность vs abyāpāda = отсутствие недоброжелательности;
  - kukkucca = угрызения vs uddhacca = беспокойство;
  - vīriya = усердие vs padhāna / vāyāma = усилие.
- samudaya = возникновение. yoni = способ рождения, distinct from saṃsāra = круговорот перерождений.
- āsavānaṃ khaya = уничтожение влечений (never «истощение»).

### Terms the earlier books rendered differently (pick ONE for pi-1 and report it)
Default to the pi-5 form unless the Dhammasaṅgaṇī context needs otherwise:
- saṅkhāra (aggregate): pi-3 «умственные формации», pi-5 «формирующие факторы»; in dependent origination pi-3 «формации».
- vicāra: pi-3 «обдумывание», pi-5 «удержание мысли».
- dosa: pi-4 «ненависть», pi-5 «злоба».
- asaṅkhata: pi-3 «несотворённое», pi-5 «необусловленное».
- paṭiccasamuppāda: pi-3 «взаимозависимое возникновение», pi-5 «возникновение в зависимости от условий».
- mātikā: pi-3 «перечень». English now says "matrix" (user rule for English); Hindi «मूल सूची». Propose a Russian form.

## Verify (must pass)
```
python -I -X utf8 0-INBOX\temp\pipeline\check_chapter_ids.py <pali_split_dir> <russian_split_dir> <ch>.md
python -I -X utf8 0-INBOX\temp\pipeline\dashcheck.py <pali_file> <russian_file>
```
check_chapter_ids prints OK; dashcheck shows equal line counts and 0 dash mismatches. For a partial sample, compare against the same Pāli lines (write them to a scratch file first). Also grep for «—», «ли» in questions, Latin words outside variant brackets, double blank lines.
