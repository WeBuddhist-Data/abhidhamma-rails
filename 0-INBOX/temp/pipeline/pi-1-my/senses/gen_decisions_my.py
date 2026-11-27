"""Write the Pāli→Burmese decisions file for senses_my.py (brief: pi-1-my/burmese-senses-brief.md).

usage: python -I -X utf8 gen_decisions_my.py <agg.tsv> <decisions.txt>

For every headword of agg.tsv that has Burmese values (NDE-only headwords are skipped):
  1. a hand decision in MANUAL below wins (tag wording from the Marathi pi-1 senses where the
     same headword and sense recur, values = Burmese only);
  2. otherwise, if the Marathi pi-1 senses file gives the headword ONE English tag, the line is
     that tag + every attested Burmese value (one sense);
  3. otherwise (Marathi has several senses) the headword is UNRESOLVED: write a MANUAL entry.
Only the ENGLISH tags are read from the Marathi file; its Marathi values are dropped on parsing
and never written. Headwords with one Marathi tag but several Burmese values are printed as
REVIEW unless listed in LUMP_OK (checked by hand: grammatical variants or synonyms of one sense).
The script fails (exit 1) while anything is UNRESOLVED, a MANUAL value is not attested, or a
MANUAL entry omits an attested value.
"""
import pathlib
import re
import sys
from collections import OrderedDict

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
MR_SENSES = ROOT / 'AI_translation/marathi/pi-1-pali-word-marathi-senses-plain.md'
VAL_RE = re.compile(r'^(.*)=(\d+)\[[^\]]*\]$')
NONLATIN = re.compile(r'[ऀ-ॿက-႟]')

# Hand decisions: headword -> [(English tag, [Burmese values])]. Values must be attested.
MANUAL = OrderedDict([
    ('Dhamma', [
        ('phenomena, states (as in the book title Dhammasaṅgaṇī), the same value also naming '
         'mind-objects, what the mind as sixth sense knows (as in dhammāyatana)',
         ['သဘောတရား']),
        ("the Buddha's teaching, in dhammamacchariya and dhammapaṭisanthāra", ['တရား']),
    ]),
    ('kāya', [
        ('the physical body, or bodily (compound member, as in kāyaviññāṇa and kāyakamma)',
         ['ကိုယ်']),
        ('the mental body, the group of mental factors (in kāyapassaddhi and similar)',
         ['စိတ်၏ အဖော်တို့']),
    ]),
    ('paṭicca', [
        ('dependent on conditions, first member of paṭiccasamuppanna, and of paṭiccasamuppāda '
         '(dependent origination) in the Mātikā and its definition',
         ['အကြောင်းတို့ကို မှီ၍', 'အကြောင်းအကျိုး ဆက်စပ်']),
    ]),
    ('indriyaṃ', [
        ('controlling faculty, one of the twenty-two (nominative sg.), the same value also naming '
         'the sense faculty to be guarded in the restraint passage (cakkhundriya)',
         ['စွမ်းရည်']),
    ]),
    ('saddhā', [
        ('faith, confidence (nominative sg.), also as an adjective, having faith (of persons, in '
         'the good-friendship definition)',
         ['ယုံကြည်မှု', 'ယုံကြည်မှု ရှိသော']),
    ]),
    ('rūpa', [
        ('the fine-material sphere, as in rūpāvacara and rūpūpapatti (compound member), rūpa in '
         'rūpasaññā of the immaterial-jhāna formula being given under matter',
         ['သိမ်မွေ့သော ရုပ်']),
        ('visible form, the object of the eye (compound member, as in rūpārammaṇa)',
         ['အဆင်းအရောင်']),
        ('matter, material form (heading and compound member, as in Rūpakaṇḍa and rūpakkhandha)',
         ['ရုပ်']),
    ]),
    ('sammā', [
        ('right, correct, prefixed to path factors (compound member), also the adverb rightly '
         '(sammāpaṭipannā)',
         ['မှန်ကန်သော', 'မှန်ကန်စွာ']),
        ('perfectly, in sammāsambuddha (title line)', ['အပြည့်အဝ']),
    ]),
    # ---- full run (part1): UNRESOLVED headwords (several Marathi senses) ----
    ('āyatanāni', [
        ('sense bases, the sense fields (nominative pl.)', ['အာရုံခံ နယ်ပယ်']),
        ("bases, in abhibhāyatanāni 'bases of mastery' (compound final)", ['နယ်ပယ်']),
    ]),
    ('brahma', [
        ('divine, sublime, in brahmavihāra (compound member)', ['ဗြဟ္မစိုရ်']),
        ('the Brahmā world, in brahmaloka (compound member)', ['ဗြဟ္မာ့']),
    ]),
    ('kiriyā', [
        ('merely functional, producing no result (stem and compound member)', ['ပြုရုံမျှသာ ဖြစ်သော']),
        ("doing, in akiriyā 'not doing' (noun)", ['ပြုခြင်း']),
    ]),
    ('ṭhiti', [
        ('stability, steadiness of mind (in the concentration list), the same value also naming '
         'persistence, the lasting of life (in the life-faculty list)',
         ['တည်တံ့ခြင်း']),
    ]),
    ('sampaggāho', [
        ('upholding, keeping the mind exerted (in the energy list)', ['ခိုင်မြဲစွာ ထမ်းဆောင်ခြင်း']),
        ('self-exaltation, holding oneself high (in the conceit list)', ['အလွန် မြှင့်တင်ခြင်း']),
    ]),
    ('khandhā', [
        ('aggregates, groups of phenomena (nominative pl.)', ['အစုအဝေး']),
        ('classes of offences, in āpattikkhandhā (compound final)', ['အစု']),
    ]),
    ('dukkha', [
        ("painful, hard, as in dukkhapaṭipadā 'painful practice' (compound member)", ['ခက်ခဲသော']),
        ('pain, painful feeling or painful to the touch (compound member, as in dukkhasahagata '
         'and dukkhasamphassa)',
         ['နာကျင်သော', 'နာကျင်မှု']),
        ('suffering, the whole of what is unsatisfactory, in dukkhamūla and dukkhakkhandha '
         '(compound member)',
         ['ဒုက္ခ']),
    ]),
    ('bahiddhā', [
        ('externally, of forms seen outside oneself, in the bases of mastery (adverb)', ['ပြင်ပ၌']),
        ("external, belonging to others, in 'ajjhattaṃ vā bahiddhā vā' and the internal and "
         "external triad (adverb)",
         ['သူတစ်ပါး၌']),
        ("outside, in 'ito bahiddhā' 'outside this teaching' (adverb)", ['အပြင်ဘက်']),
    ]),
    ('thambhitattaṃ', [
        ('stiffening of the mind, mental paralysis, in the doubt list (neuter sg.)',
         ['တောင့်တင်းနေသော အဖြစ်']),
        ('distension, the stiffened state of matter, in the air element definition (neuter sg.)',
         ['တောင့်တင်းထားသော အဖြစ်']),
    ]),
    ('rūpaṃ', [
        ('matter, material form (nominative/accusative sg.), also the material side of nāmarūpa',
         ['ရုပ်', 'ရုပ်ပိုင်း']),
        ('visible form, the object of the eye, in the restraint passage (accusative sg.)',
         ['အဆင်းအရောင်']),
    ]),
    ('vaṇṇa', [
        ('colour, hue, as in vaṇṇanibhā (compound member)', ['အရောင်']),
        ('praise, reputation, in vaṇṇamacchariya (compound member)', ['ဂုဏ်သတင်း']),
    ]),
    ('khandha', [
        ('stem, trunk of a plant, in khandharaso (compound member)', ['ပင်စည်']),
        ('aggregate, group of phenomena, in khandhadhātuāyatanā (compound member)', ['အစုအဝေး']),
    ]),
    ('kāyassa', [
        ('the physical body, or bodily (genitive sg., as in kāyassa thambhanā and imassa kāyassa '
         'ṭhitiyā)',
         ['ကိုယ်', 'ကိုယ်ခန္ဓာ']),
        ('the mental body, the group of mental factors (genitive sg., in kāyassa akallatā, the '
         'definition of torpor)',
         ['စိတ်၏ အဖော်']),
    ]),
    ('bhedo', [
        ("breaking forth, in vacībhedo 'utterance of speech' (nominative sg.)", ['ကွဲထွက်ခြင်း']),
        ('breaking up, dissolution, in the impermanence list (nominative sg.)', ['ကွဲခြင်း']),
    ]),
    ('sīla', [
        ("precepts and rites, in sīlabbata 'adherence to rites and rituals' (compound member), the "
         "same value also naming virtue, moral conduct (in sīlasaṃvara, sīlavipatti and sīlavisuddhi)",
         ['သီလ']),
    ]),
    ('dhammassa', [
        ("the Buddha's teaching, in 'unskilled in the teaching of the noble ones' (genitive sg.)",
         ['တရား']),
    ]),
    ('dhamme', [
        ("the Buddha's teaching, in 'doubts about the Teacher, the teaching, the training' (locative)",
         ['တရားတော်']),
        ('phenomena, states, in dhamme ārabbha (accusative pl.)', ['သဘောတရား']),
    ]),
    ('vuṭṭhāna', [
        ('emerging, from an offence in āpattivuṭṭhāna (rehabilitation) and from a meditative '
         'attainment in samāpattivuṭṭhāna (compound member)',
         ['ထမြောက်ရာ']),
    ]),
    ('vuṭṭhānakusalatā', [
        ('skill in emerging, from offences in āpattivuṭṭhānakusalatā and from attainments in '
         'samāpattivuṭṭhānakusalatā',
         ['ထမြောက်ရာ၌ ကျွမ်းကျင်ခြင်း']),
    ]),
    # ---- full run (part1): REVIEW headwords split for a genuinely different meaning ----
    ('vāro', [
        ('portion for recitation, in bhāṇavāra (heading)', ['အပိုင်း']),
        ('round of the exposition, in koṭṭhāsavāra and suññatavāra (heading)', ['ဖော်ပြချက်']),
    ]),
    ('Chanda', [
        ('desire to act, zeal as dominant factor (compound member)', ['ဆန္ဒ']),
        ('sensual desire, the wanting in kāmacchanda, the first hindrance (compound member)',
         ['လိုလားမှု']),
    ]),
    ('cetasikaṃ', [
        ('mental, of the mind as opposed to the body (neuter sg. adjective)', ['စိတ်ပိုင်းဆိုင်ရာ']),
        ('a mental factor, what accompanies the mind, in the cetasika dyad (acetasikaṃ, neuter sg.)',
         ['စိတ်၏ အဖော်']),
    ]),
    ('maggo', [
        ('the path, as a set of factors (nominative sg.)', ['မဂ်']),
        ("way, road, in kummaggo 'wrong way' (compound final, nominative sg.)", ['လမ်း']),
    ]),
    ('maggaṃ', [
        ("way, the means to rebirth, in rūpūpapattiyā maggaṃ 'the way to rebirth in the "
         "fine-material sphere' (accusative sg.)",
         ['လမ်း']),
        ('the supramundane path, as a set of factors (accusative sg.)', ['မဂ်']),
    ]),
    ('hetū', [
        ('roots, root conditions (nominative pl.)', ['အမြစ်']),
        ("causes, conditions, in 'hetū paccayā' of the skill-in-the-possible passage (nominative pl.)",
         ['အကြောင်း']),
    ]),
    ('kāyena', [
        ('with the physical body, through the body (instrumental)', ['ကိုယ်']),
        ('with the mental body, the group of mental factors, in the third-jhāna formula '
         '(instrumental)',
         ['စိတ်၏ အဖော်တို့']),
    ]),
    ('sukha', [
        ("easy, as in sukhapaṭipadā 'easy practice' (compound member)", ['လွယ်ကူသော']),
        ('pleasure, happiness, or pleasant (compound member, as in sukhasahagata, sukhavihāra and '
         'sukhasamphassa)',
         ['သာယာမှု', 'သာယာစွာ', 'သာယာသော']),
    ]),
    ('āhāraṃ', [
        ('nutriment, a sustaining condition of mind (contact, volition, consciousness), in '
         'lokuttaraṃ āhāraṃ (accusative sg.)',
         ['အာဟာရ']),
        ('food, what is eaten, in the moderation-in-eating passage (accusative sg.)', ['အစာ']),
    ]),
    ('phala', [
        ('fruit, of plants in the smell and taste lists (compound member)', ['အသီး']),
        ('fruition of the path, in phalasamaṅgī (compound member)', ['ဖိုလ်']),
    ]),
    ('sineho', [
        ('affection, fond attachment, in the greed list and in kāmasineha (nominative sg.)',
         ['ချစ်ခင်မှု', 'ချစ်ခင်ခြင်း']),
        ('cohesion, moisture or fluidity, in the water-element definition (nominative sg.)',
         ['စေးကပ်မှု']),
    ]),
    ('phalaṃ', [
        ('fruit, the result of good and bad deeds, in the wrong-view and right-view formulas '
         '(nominative sg.)',
         ['အသီးအပွင့်']),
        ('fruition attainment, the fruit of the path, in arahattaphalaṃ (nominative sg.)', ['ဖိုလ်']),
    ]),
    ('niyatā', [
        ('fixed in destiny, with a certain outcome (nominative pl. participle)', ['ကျိန်းသေသော']),
        ("individual, restricted to oneself, in 'ajjhattaṃ paccattaṃ niyatā' (nominative pl. "
         "participle)",
         ['သီးသန့် ဖြစ်သော']),
    ]),
    ('sacca', [
        ('truth, what is true, as in idaṃsaccābhinivesa (compound member)', ['အမှန်']),
        ("the truths, in saccānulomikañāṇa 'knowledge in conformity with the truths' "
         "(compound member)",
         ['သစ္စာ']),
    ]),
    # ---- full run (part1): REVIEW headwords kept as one sense, tag widened to cover the values ----
    ('gāho', [
        ('grasp, seizing, a holding on to a view (nominative sg.), also taking up a position, in '
         "anekaṃsaggāho 'not taking one side' (doubt list)",
         ['စွဲကိုင်ခြင်း', 'ယူနိုင်ခြင်း']),
    ]),
    ('sekkhā', [
        ('in training, belonging to the learner stage (nominative pl.), also the training itself '
         'as the positive part of asekkhā',
         ['ကျင့်ကြံဆဲသူ၏', 'ကျင့်ကြံမှု']),
    ]),
    ('vibhava', [
        ('non-existence, annihilation, in vibhavataṇhā and vibhavadiṭṭhi (compound member)',
         ['ဘဝ ပြတ်စဲခြင်း', 'ဘဝ ပျောက်ကွယ်သည်']),
    ]),
    ('kusalato', [
        ('from among the wholesome minds, or as wholesome, in the planes-of-arising lists (ablative)',
         ['ကုသိုလ်စိတ်', 'ကုသိုလ်']),
    ]),
    ('kiriyato', [
        ('from among the functional minds, or as functional, in the planes-of-arising lists '
         '(ablative)',
         ['ပြုရုံမျှသာ ဖြစ်သော စိတ်', 'ပြုရုံမျှသာ']),
    ]),
    ('vipākato', [
        ('as resultant, under the heading of results of action, or from among the resultant minds '
         '(ablative)',
         ['အကျိုး ဖြစ်သော စိတ်', 'ကံ၏ အကျိုး', 'အကျိုး']),
    ]),
    ('vipākato ca kiriyato', [
        ('from among, or as, the resultant and the functional minds',
         ['ကံ၏ အကျိုးအဖြစ်လည်းကောင်း ပြုရုံမျှသာအဖြစ်လည်းကောင်း',
          'အကျိုး ဖြစ်သော စိတ်အနက်လည်းကောင်း ပြုရုံမျှသာ ဖြစ်သော စိတ်အနက်လည်းကောင်း']),
    ]),
])

# One Marathi tag, several Burmese values, checked by hand: one sense.
LUMP_OK = {
    'uppannaṃ',          # ဖြစ်ပေါ်လာသော / ဖြစ်ပေါ်သော / ဖြစ်ပေါ်ပြီးသော: tense variants of one verb
    'arūpino dhammā',    # with / without the ellipsis of the closing formula
    # ---- full run (part1), checked by hand: one sense ----
    # adjective vs the noun supplying စိတ် (kinds of mind), or the bare stem (5 rule 15 / 18)
    'kusalaṃ', 'akusalaṃ', 'kusalesu',
    # adjective «…သော» vs noun «…ခြင်း / …မှု» of the same verb (headings, neva sātaṃ nāsātaṃ)
    'Suññata', 'Suññataṃ', 'Appaṇihitaṃ', 'sātaṃ', 'asātaṃ', 'anussati',
    # «…မှု» / «…ခြင်း» of one verb, or causative of the same verb
    'domanassa', 'nandī', 'mucchā', 'santuṭṭhitā', 'samāpatti', 'uppādāya', 'Saṃvego',
    # tense / aspect variants (arisen / not-yet lists), with or without ကောင်းစွာ for sam-
    'samuppannā', 'uppannā', 'jātā', 'abhinibbattā', 'samuṭṭhitā', 'nibbattā', 'pātubhūtā',
    'sañjātā', 'uṭṭhitā',
    # continuous vs « … » where a heading or list inserts a word
    'vipākamanoviññāṇadhātu', 'vipākā manoviññāṇadhātu', 'Kiriyāmano', 'Kiriyā mano',
    'rūpaṃ sappaṭighaṃ', 'rūpaṃ appaṭighaṃ',
    # numerals counted with ပါး vs bare
    'Dasa', 'Ekādasa',
    # the text's own wording differs for the same Pāli (same meaning)
    'kammassa katattā', 'akusalābyākatā', 'abyākatahetū', 'akusalahetū', 'kusalahetū',
    'vatthūni', 'rūpañca nibbānañca', 'rūpañca', 'kamyatā',
    # synonyms for one meaning (the termbase step picks one)
    'Yo', 'sukhā', 'ākāsa', 'eva', 'patho', 'ñāṇaṃ', 'indriyānaṃ', 'para',
}


def parse_tags(line):
    """'hw: {t: v; t2: v2}' -> (hw, [t, t2]); the values are discarded."""
    i = line.find(': {')
    if i < 0 or not line.endswith('}'):
        return None, None
    hw, body = line[:i], line[i + 3:-1]
    tags = []
    for s in body.split('; '):
        if ': ' not in s:
            return hw, None
        tags.append(s.rsplit(': ', 1)[0].strip())
    return hw, tags


def read_mr_tags():
    tags = {}
    for line in MR_SENSES.read_text(encoding='utf-8-sig').splitlines():
        line = line.strip()
        if not line:
            continue
        hw, t = parse_tags(line)
        if hw is None or t is None:
            sys.exit(f'cannot parse Marathi senses line: {line[:80]!r}')
        tags[hw] = t
    return tags


def read_agg(path):
    rows = OrderedDict()
    for n, line in enumerate(open(path, encoding='utf-8-sig'), 1):
        line = line.rstrip('\n').rstrip('\r')
        if not line.strip():
            continue
        cols = line.split('\t')
        if len(cols) != 4:
            sys.exit(f'agg line {n}: expected 4 columns')
        vals = OrderedDict()
        for item in [x.strip() for x in cols[2].split(' | ') if x.strip()]:
            m = VAL_RE.match(item)
            if not m:
                sys.exit(f'agg line {n}: cannot parse {item!r}')
            vals[m.group(1)] = vals.get(m.group(1), 0) + int(m.group(2))
        rows[cols[0]] = vals
    return rows


def main(aggp, outp):
    rows = read_agg(aggp)
    mr = read_mr_tags()
    out, unresolved, review, errs = [], [], [], []
    for hw, vals in rows.items():
        if not vals:
            continue
        if hw in MANUAL:
            senses = MANUAL[hw]
            given = [v for _, vs in senses for v in vs]
            for v in given:
                if v not in vals:
                    errs.append(f'{hw}: MANUAL value not attested: {v!r}')
            for v in vals:
                if v not in given:
                    errs.append(f'{hw}: attested value missing from MANUAL: {v!r}')
            if len(given) != len(set(given)):
                errs.append(f'{hw}: a value is under two senses')
        elif hw in mr and len(mr[hw]) == 1:
            senses = [(mr[hw][0], list(vals))]
            if len(vals) > 1 and hw not in LUMP_OK:
                review.append((hw, list(vals)))
        else:
            unresolved.append((hw, mr.get(hw), list(vals)))
            continue
        for tag, _ in senses:
            if NONLATIN.search(tag) or '; ' in tag or not tag:
                errs.append(f'{hw}: bad tag {tag!r}')
        out.append(hw + ': {' + '; '.join(t + ': ' + ' / '.join(vs) for t, vs in senses) + '}')
    unused = [h for h in MANUAL if h not in rows]
    if unused:
        print(f'note: MANUAL entries not in this input (fine for a part run): {unused}')
    with open(outp, 'w', encoding='utf-8', newline='\n') as f:
        f.write(f'# Pāli→Burmese pi-1 sense decisions, written by gen_decisions_my.py from {pathlib.Path(aggp).name}\n')
        f.write('# English tags: Marathi pi-1 senses (tags only) or MANUAL; values: Burmese keyword map only.\n')
        f.write('\n'.join(out) + '\n')
    print(f'wrote {len(out)} decision lines -> {outp} (MANUAL used: '
          f'{sum(h in rows for h in MANUAL)})')
    if review:
        print(f'REVIEW ({len(review)}): one Marathi tag, several Burmese values; check, then add to '
              f'LUMP_OK or MANUAL:')
        for hw, vs in review:
            print(f'  {hw}: {" / ".join(vs)}')
    if unresolved:
        print(f'UNRESOLVED ({len(unresolved)}): several Marathi senses or no Marathi line; write MANUAL:')
        for hw, t, vs in unresolved:
            print(f'  {hw}\ttags={t}\tburmese={vs}')
    if errs:
        print(f'ERRORS ({len(errs)}):')
        for e in errs:
            print('  ' + e)
    return 1 if (unresolved or errs) else 0


if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    sys.exit(main(*sys.argv[1:]))
