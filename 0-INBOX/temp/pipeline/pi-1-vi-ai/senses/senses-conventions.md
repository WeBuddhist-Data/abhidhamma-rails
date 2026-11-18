# pi-1 Pāli→Vietnamese senses: conventions from the sample (for parts 1–4)

The sample was agg-sample.tsv (the first 120 headwords of part 1). Follow these conventions so all four parts read as one file.
The brief (..\vi-senses-brief.md, with its FORBIDDEN list) and the skill (AI_translation\skills\word-sense-grouper.md) still govern; this file only fixes the choices they leave open. Model: the approved Russian run, ..\..\pi-1-ru\senses\senses-conventions.md and AI_translation\russian\pi-1-pali-word-russian-senses-plain.md. The meanings of the Pāli words are the same in both languages, so the split into senses and the English tags follow the Russian file; only the candidates are Vietnamese.

## 1. Workflow and tool

Files per part K (all in this folder): `decisions-partK.txt` (your hand-written tag table) → `partK-senses.md` (output).

```
python -I -X utf8 senses_tool_vi.py todo   --part K                    # headwords still without a decision line
python -I -X utf8 senses_tool_vi.py ru     <headword> [<headword> ...] # the approved Russian line(s): copy the tags
python -I -X utf8 senses_tool_vi.py words  <headword> [<value>]        # per Vietnamese value, the Pāli compounds it comes from
python -I -X utf8 senses_tool_vi.py show   <headword> [<value>] [<max segs>]  # ids + Pāli/Vietnamese line pairs
python -I -X utf8 senses_tool_vi.py build  --part K                    # builds partK-senses.md, then verifies
python -I -X utf8 senses_tool_vi.py verify --part K
```

Decision lines, one per headword, any order (build writes agg order):
- `hw: {tag}`: one sense; the tool fills in every attested value, most frequent first.
- `hw: {tag1: v1 / v2; tag2: v3}`: explicit split. Every attested value placed; `*` = "all values not listed elsewhere on this line". Values are re-sorted by count inside each sense; senses keep your order (main sense first, as in the Russian line).
- `words hw` is the quickest check before a split: it shows, per value, which Pāli words of those segments contain the stem (e.g. rūpa: hình sắc ← rūpāyatana, rūpārammaṇa, rūpāvacara; cõi hình sắc ← rūpūpapattiyā; vật chất ← rūpasaṅgaha, Rūpakaṇḍa). `show hw value 3` prints the segments themselves.
- An attested value containing " / " is written with " và " in the decisions file (build prints every rewrite; the sample had none).
- Shared candidate: the same Vietnamese string may stand in TWO senses of one headword only when `words`/`show` prove it is attested in both meanings (sample: rūpa «hình sắc», both visible form and the member of «thuộc cõi hình sắc»). Build/verify list every shared candidate; report them.

`verify` fails on: headword list or order differs, duplicate headwords, a missing or unattested value, a tag equal to a value, a tag that is a bare copy of an English hint (case-insensitive), Vietnamese letters in a tag, two senses with the same tag, a candidate containing "/" or "; ", a value listed twice in one sense, non-NFC text, an unparsable line.

## 2. How tags are written

Exactly as the Russian conventions §2: **short English gloss[, distinguishing context] (grammar)**, same grammar labels, same fixed patterns (X-indriyaṃ `the controlling faculty of X (nominative sg.)`, X-balaṃ `the power of X (nominative sg.)`, citta-X `X of the mind (nominative sg.)`, a-/an- `absence of X (nominative sg.)`, X-sahagataṃ `accompanied by X (neuter sg. participle)`, Yo/Yā/Yaṃ `relative pronoun, that which or whatever (… nominative sg.)`, closing-formula pieces).

- **Copy the Russian tag word for word** (`ru <hw>`) whenever the headword exists there with the same meaning. All 120 sample headwords were found there.
- Write a NEW tag only when (a) the headword is missing from the Russian file, or (b) Vietnamese uses ONE value for meanings the Russian split into two (then one combined tag naming both uses, see §3).
- Forbidden in a tag: ": ", "; ", "{", "}", Vietnamese letters. Keep tags under ~20 words.

## 3. One sense or several

Merge into ONE sense (candidates joined by " / ", most frequent first):
- Nominaliser or classifier present or absent: sự hiểu biết rõ ràng / hiểu biết rõ ràng (sampajaññaṃ); nỗ lực / sự nỗ lực (vāyāmo: path factor vs energy list); sự tỉnh thức / tỉnh thức (sati: factor vs inside «năng lực tỉnh thức»); sống / sự sống (jīvita); loại hạn hẹp / hạn hẹp (parittāni). Expected: sự bình thản / bình thản, sự hoài nghi / hoài nghi, loại X / X.
- Tense/aspect word: sinh khởi / đã sinh khởi (uppannaṃ); expected đang sinh khởi, sẽ sinh khởi only if the meaning is still "arisen" (uppādino = "will arise" is its own headword).
- «có» (having) present or absent: niềm tin / có niềm tin (saddhā; «những người có niềm tin»); đối tượng / có đối tượng (ārammaṇaṃ; the «không có đối tượng» of anārammaṇaṃ).
- Synonyms or fuller/shorter forms for one meaning: phần / mục (vāro, section); sống / sự sống / mạng sống (jīvita; mạng sống = «sự mong mỏi mạng sống», jīvitāsā).
- Vietnamese uses ONE word where the Russian has two senses: keep one sense with a combined tag:
  - kāya: thân covers the physical body AND the body sense (kāyāyatana, kāyaviññāṇa «thức qua thân»), also kāyagantha «nút thắt của thân», sakkāyadiṭṭhi. Russian split off осязательный; we cannot.
  - sukhaṃ: hạnh phúc (jhāna factor) / dễ chịu (feeling, mental «trong tâm» AND bodily «nơi thân», 1-445, 1-452) = one sense `happiness, pleasant feeling of mind or body, …`.
  - cittaṃ: tâm also in the colophons «Tâm thứ nhất …», so no separate "type of mind" sense (unlike the Russian вид ума).
  - kāma: dục lạc both in kāmāvacara and in kāmarāga / kāmataṇhā.

SPLIT only for a different meaning or referent, verified with `words` / `show`:
- Dhamma: đối tượng của ý (dhammāyatana, dhammadhātu, dhammārammaṇa, dhammataṇhā) vs hiện tượng (book title) vs Giáo Pháp (dhammamacchariya, dhammapaṭisanthāra).
- rūpa: hình sắc (visible form) vs cõi hình sắc / hình sắc (fine-material sphere; bare «hình sắc» is the member inside «thuộc cõi hình sắc», «cõi» going to avacara) vs vật chất (matter).
- kāya: thân vs thân tinh thần (kāyapassaddhi … kāyujukatā).
- sammā: đúng đắn vs Hoàn Toàn (sammāsambuddha, title line).
- ārabbha: lấy … làm (taking as object) vs liên quan đến (pubbantaṃ / aparantaṃ ārabbha, views about past/future).
- āyatanāni: lĩnh vực nhận biết (sense bases) vs lĩnh vực (abhibhāyatanāni).
- Expected later (decide with `words`/`show`, tags from the Russian file): dukkha khó chịu (painful feeling) vs khó khăn (difficult, of practice) vs sự đau khổ / khổ đau (suffering); sukha dễ dàng (easy, of practice) as its own sense; khandha khối vs āpattikkhandhā; āhāra dưỡng chất vs edible food; magga con đường vs kummagga; hetu gốc rễ vs causes; ṭhiti sự ổn định (concentration list) vs sự tồn tại (life list); sampaggāha (energy vs conceit list); parāmāsa in sīlabbataparāmāsa; cetasika trong tâm / trạng thái trong tâm (mental) vs đồng hành với tâm (mental concomitant); duka bộ đôi (matrix) vs the matter chapter's twofold classification; vuṭṭhāna việc ra khỏi / việc xuất khỏi (one meaning, merge); kiriyā, brahma, mātikā (ma trận, never "outline").
- mano: the Vietnamese map gives ý also inside the citta synonym string, so mano is ONE sense unless a different value turns up (the Russian разум split does not apply).

## 4. Recurring headword families: the sample's senses

Reuse these (wording and order) for every form of the headword; adapt only the grammar label.

| Family | Sense tag (copied from the Russian file unless marked *new*) | Vietnamese |
|---|---|---|
| dhamma | `mind-objects, what the mind as sixth sense knows (compound member, as in dhammāyatana and dhammārammaṇa)` | đối tượng của ý |
| | `phenomena, states, in the book title Dhammasaṅgaṇī (compound member)` | hiện tượng |
| | `the Buddha's teaching, in dhammamacchariya and dhammapaṭisanthāra (compound member)` | Giáo Pháp |
| rūpa | `visible form, the object of the eye (compound member, as in rūpārammaṇa)` | hình sắc |
| | `the fine-material sphere, as in rūpāvacara and rūpūpapatti (compound member)` | hình sắc / cõi hình sắc |
| | `matter, material form (heading and compound member, as in Rūpakaṇḍa)` | vật chất |
| arūpino | `without material form (nominative pl.)` | phi vật chất |
| kāya | *new* `the physical body, or bodily, including the body sense (compound member, as in kāyāyatana, kāyaviññatti and kāyaviññāṇa)` | thân |
| | `the mental body, the group of mental factors (compound member, as in kāyapassaddhi)` | thân tinh thần |
| citta | *new* cittaṃ: `mind, a state of mind, also a numbered type of mind as in 'paṭhamaṃ cittaṃ' (nominative/accusative sg.)`; Citta: `mind, a state of mind (stem and compound member)` | tâm |
| mana / mano | `mind, as stem in manindriya and similar compounds` | ý |
| sukha | *new* `happiness, pleasant feeling of mind or body, as jhāna factor and in the feeling definitions (neuter sg.)` | hạnh phúc / dễ chịu |
| kāma | *new* `the sense sphere, as in kāmāvacara, also sensual desire or pleasure, as in kāmarāga and kāmataṇhā (compound member)` | dục lạc |
| avacara | `belonging to a sphere, or the sphere itself (stem and compound final)`; avacaraṃ `belonging to a sphere, compound final (neuter sg.)`; Kāmāvacara `belonging to the sense sphere (compound member and heading)`; Rūpāvacara `belonging to the fine-material sphere, or that sphere (compound member and heading)` | thuộc cõi (dục lạc / hình sắc) |
| sahagata | `accompanied by, compound final (neuter sg. participle)` | đi kèm (X-sahagata: có X đi kèm) |
| sampayutta | `conjoined with, compound final (neuter sg. participle)` | gắn liền |
| indriya | `controlling faculty, one of the twenty-two (nominative sg.)` | năng lực |
| bala | `power, strength, one of the seven powers (nominative sg.)` | sức mạnh |
| āyatana | `sense bases, the sense fields (nominative pl.)` / `bases, in abhibhāyatanāni 'bases of mastery' (compound final)` | lĩnh vực nhận biết / lĩnh vực |
| ārammaṇa | `object of the mind, what the mind takes up (nominative/accusative sg.)`; ārammaṇāni `kinds of object, in the object-based headings (heading member, nominative pl.)` | đối tượng / có đối tượng; loại đối tượng |
| ārabbha | `taking as object, …` / `concerning, about, in the views 'about the past' and 'about the future' (absolutive)` | lấy … làm / liên quan đến |
| kusala | kusalā `wholesome, said of phenomena (nominative pl.)`; kusalaṃ `wholesome, often standing for the wholesome mind (neuter sg.)` | thiện |
| sammā | `right, correct, rightly, prefixed to path factors (compound member and adverb)` / `perfectly, in sammāsambuddha (title line)` | đúng đắn / Hoàn Toàn |
| jīvita | `life, vitality (compound member, as in jīvitindriya, and nominative)` | sống / sự sống / mạng sống |
| sati | `mindfulness, present awareness (stem and nominative)` | sự tỉnh thức / tỉnh thức (never chánh niệm) |
| vāro | `section, a round of the exposition (heading member)` | phần / mục |
| closing formula | `'arisen immaterial phenomena', the closing 'whatever others' formula (nominative pl.)`; gapped: `'arisen immaterial', the gapped pair …` | hiện tượng phi vật chất … sinh khởi; phi vật chất … sinh khởi |

## 5. Report items

Headword count and the verify line; headwords with >1 sense; senses with >1 candidate; every shared candidate and every " / "→" và " rewrite the build prints; the most consequential splits, the merges forced by a single Vietnamese value, and anything unclear.
