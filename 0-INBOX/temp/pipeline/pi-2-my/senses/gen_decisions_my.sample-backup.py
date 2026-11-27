"""Write the Pāli→Burmese pi-2 decisions file for senses_my.py (brief: pi-2-my/burmese-senses-brief.md).
Adapted from pi-1-my/senses/gen_decisions_my.py (same MANUAL / LUMP_OK mechanism).

usage: python -I -X utf8 gen_decisions_my.py <agg.tsv> <decisions.txt>

For every headword of agg.tsv that has Burmese values (NDE-only headwords are skipped):
  1. a hand decision in MANUAL below wins;
  2. otherwise, if the approved pi-1 Burmese senses file has the headword (exact, else the one
     case-insensitive match: the aggregation keeps the first spelling seen), its senses are BINDING:
     every pi-2 value that pi-1 lists goes under pi-1's sense with pi-1's English tag, in pi-1's
     sense order (a pi-1 sense with no pi-2 value is left out). A pi-2 value that pi-1 does not list
     is REVIEW (pi-1 has one sense: add the headword to LUMP_OK if the value is a variant / synonym
     of that sense, else MANUAL) or UNRESOLVED (pi-1 has several senses: MANUAL);
  3. otherwise, if the Marathi pi-2 senses file gives the headword ONE English tag, the line is that
     tag + every attested Burmese value (one sense; several values -> REVIEW unless LUMP_OK);
  4. otherwise (several Marathi senses, or no Marathi line) the headword is UNRESOLVED: write MANUAL.
Only the ENGLISH tags are read from the Marathi file; its Marathi values are dropped on parsing and
never written. A MANUAL entry for a pi-1 headword must keep pi-1's split: every value pi-1 lists sits
under a sense whose tag starts with pi-1's tag for it (an appended «, the same value also naming …»
is allowed) unless the headword is in P1_TAG_CHANGED (logged reason).
The script fails (exit 1) while anything is UNRESOLVED, a MANUAL value is not attested, a MANUAL entry
omits an attested value, or a MANUAL entry breaks a pi-1 sense.
"""
import pathlib
import re
import sys
from collections import OrderedDict

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
MY1_SENSES = ROOT / 'AI_translation/burmese/pi-1-pali-word-burmese-senses-plain.md'
MR_SENSES = ROOT / 'AI_translation/marathi/pi-2-pali-word-marathi-senses-plain.md'
VAL_RE = re.compile(r'^(.*)=(\d+)\[[^\]]*\]$')
NONLATIN = re.compile(r'[ऀ-ॿက-႟]')

# Hand decisions: headword -> [(English tag, [Burmese values])]. Values must be attested.
# pi-1 senses first (pi-1 order, pi-1 tag), then the senses new in pi-2.
MANUAL = OrderedDict([
    # ---- sample: pi-1 senses, a value pi-1 lacks placed in its pi-1 sense ----
    ('rūpa', [
        ('the fine-material sphere, as in rūpāvacara and rūpūpapatti (compound member), rūpa in '
         'rūpasaññā of the immaterial-jhāna formula being given under matter',
         ['သိမ်မွေ့သော ရုပ်']),
        ('visible form, the object of the eye (compound member, as in rūpārammaṇa)', ['အဆင်းအရောင်']),
        ('matter, material form (heading and compound member, as in Rūpakaṇḍa and rūpakkhandha), also '
         'the material side of nāmarūpa (in nāmarūpapaccayā)',
         ['ရုပ်', 'ရုပ်ပိုင်း']),
    ]),
    # ---- sample: pi-1 senses + a genuinely new pi-2 meaning ----
    ('rūpaṃ', [
        ('matter, material form (nominative/accusative sg.), also the material side of nāmarūpa',
         ['ရုပ်', 'ရုပ်ပိုင်း']),
        ('visible form, the object of the eye, in the restraint passage (accusative sg.)',
         ['အဆင်းအရောင်']),
        ("of such a nature, in piyarūpaṃ sātarūpaṃ 'what is dear and pleasing' (compound final)",
         ['သဘော ရှိသော', 'သဘော']),
    ]),
    ('Āyatana', [
        ('sense bases, the sense fields (compound member)', ['အာရုံခံ နယ်ပယ်']),
        ('sphere, in the names of the immaterial attainments such as ākāsānañcāyatana (compound final)',
         ['နယ်ပယ်']),
    ]),
    ('āyatanaṃ', [
        ('sense base, the sense field (nominative/accusative sg.)', ['အာရုံခံ နယ်ပယ်']),
        ('sphere, in the names of the immaterial attainments such as ākāsānañcāyatanaṃ (compound final)',
         ['နယ်ပယ်']),
    ]),
    ('Dhātu', [
        ('element, irreducible constituent (stem and compound final)', ['ဓာတ်']),
        ('realm, plane of existence, in kāmadhātu, rūpadhātu and arūpadhātu (compound final)', ['ဘုံ']),
    ]),
    ('Magga', [
        ('the path (stem and heading)', ['မဂ်']),
        ("way, road, in kummagga 'wrong way' (compound member)", ['လမ်း']),
    ]),
    ('āhāro', [
        ('nutriment, a sustaining condition of mind (contact, volition, consciousness), also edible '
         'food as nutriment, in kabaḷīkāro āhāro and the four nutriments',
         ['အာဟာရ']),
        ("food, what is eaten, in evamāhāro 'having such food' of the past-lives formula (compound final)",
         ['အစာ']),
    ]),
    ('Tattha', [
        ('therein, in that connection, opening a definition (locative)', ['ထိုတို့အနက်']),
        ("in that, in the case just described, in 'yā tattha paññā' 'the understanding therein' (locative)",
         ['ထို၌']),
    ]),
    ('ajjhattaṃ', [
        ("internally, within oneself, as in 'ajjhattaṃ arūpasaññī' and 'ajjhattaṃ sampasādanaṃ' (adverb)",
         ['မိမိ၌', 'မိမိ၏ အတွင်း၌ ဖြစ်သော']),
        ("internal, one's own as opposed to others' (internal and external pair)", ['မိမိ၌ ရှိသော']),
    ]),
    ('Dukkha', [
        ("painful, hard, as in dukkhapaṭipadā 'painful practice' (compound member)", ['ခက်ခဲသော']),
        ('pain, painful feeling or painful to the touch (compound member, as in dukkhasahagata and '
         'dukkhasamphassa)',
         ['နာကျင်သော', 'နာကျင်မှု', 'ကိုယ်ဆင်းရဲခြင်း']),
        ('suffering, the whole of what is unsatisfactory, in dukkhamūla and dukkhakkhandha (compound '
         'member)',
         ['ဒုက္ခ']),
        ("misery, affliction in the everyday sense, in dukkhadhammena phuṭṭhassa 'touched by some "
         "painful thing' and sukhadukkha 'pleasure and pain' of the views (compound member)",
         ['ဆင်းရဲ']),
    ]),
    # ---- sample: one pi-1 sense, the same value also carrying a second meaning in pi-2 ----
    ('saṅkhāra', [
        ('mental formations, volitional activities (compound member, in saṅkhārakkhandha), the same '
         'value also naming the formation of striving, in padhānasaṅkhāra of the bases of power',
         ['ပြုပြင်ဖန်တီးမှု']),
    ]),
    ('upādāya', [
        ('derived from, depending on the great elements, as in upādāya rūpaṃ (absolutive), the same '
         "value also naming 'with reference to', in ajjhattikassa upādāya and 'hetū paccayā upādāya'",
         ['မှီ၍']),
    ]),
])

# pi-1 headwords whose MANUAL entry deliberately departs from a pi-1 tag (headword: reason).
P1_TAG_CHANGED = {}

# Several Burmese values under one sense, checked by hand (variants or synonyms of one meaning).
LUMP_OK = {
    # ---- sample ----
    'jātaṃ',   # time list «မွေးဖွားပြီးသော» (born) / sahajātaṃ «ဖြစ်ပေါ်သော» (co-arisen): one meaning, come to be
}


def parse_line(line):
    """'hw: {t: a / b; t2: c}' -> (hw, [(t, [a, b]), (t2, [c])])."""
    i = line.find(': {')
    if i < 0 or not line.endswith('}'):
        return None, None
    hw, body = line[:i], line[i + 3:-1]
    senses = []
    for s in body.split('; '):
        if ': ' not in s:
            return hw, None
        t, v = s.rsplit(': ', 1)
        senses.append((t.strip(), [x.strip() for x in v.split(' / ')]))
    return hw, senses


def read_senses(path, keep_values):
    d = {}
    for line in path.read_text(encoding='utf-8-sig').splitlines():
        line = line.strip()
        if not line:
            continue
        hw, s = parse_line(line)
        if hw is None or s is None:
            sys.exit(f'cannot parse senses line in {path.name}: {line[:80]!r}')
        d[hw] = s if keep_values else [t for t, _ in s]   # Marathi: values dropped here
    return d


def lookup(d, hw):
    if hw in d:
        return hw
    m = [k for k in d if k.lower() == hw.lower()]
    return m[0] if len(m) == 1 else None


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
    my1 = read_senses(MY1_SENSES, True)
    mr = read_senses(MR_SENSES, False)
    out, unresolved, review, errs = [], [], [], []
    stats = {'manual': 0, 'p1_same': 0, 'p1_subset': 0, 'p1_lump': 0, 'mr': 0, 'p1_case': 0}
    for hw, vals in rows.items():
        if not vals:
            continue
        k1 = lookup(my1, hw)
        p1 = my1.get(k1) if k1 else None
        if k1 and k1 != hw:
            stats['p1_case'] += 1
        p1_of = {v: t for t, vs in (p1 or []) for v in vs}
        if hw in MANUAL:
            stats['manual'] += 1
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
            if p1 and hw not in P1_TAG_CHANGED:
                for t, vs in senses:
                    for v in vs:
                        if v in p1_of and not t.startswith(p1_of[v]):
                            errs.append(f'{hw}: {v!r} leaves its pi-1 sense {p1_of[v]!r}')
        elif p1:
            new = [v for v in vals if v not in p1_of]
            if not new:
                senses = [(t, [v for v in vs if v in vals]) for t, vs in p1]
                senses = [(t, vs) for t, vs in senses if vs]
                stats['p1_same' if len(senses) == len(p1) and len(vals) == len(p1_of) else 'p1_subset'] += 1
            elif len(p1) == 1 and hw in LUMP_OK:
                senses = [(p1[0][0], list(vals))]
                stats['p1_lump'] += 1
            elif len(p1) == 1:
                senses = [(p1[0][0], list(vals))]
                review.append((hw, 'pi-1 one sense, new values ' + ' / '.join(new), list(vals)))
                stats['p1_lump'] += 1
            else:
                unresolved.append((hw, 'pi-1 senses ' + str([t for t, _ in p1]), list(vals)))
                continue
        else:
            k2 = lookup(mr, hw)
            tags = mr.get(k2) if k2 else None
            if tags and len(tags) == 1:
                senses = [(tags[0], list(vals))]
                stats['mr'] += 1
                if len(vals) > 1 and hw not in LUMP_OK:
                    review.append((hw, 'one Marathi tag', list(vals)))
            else:
                unresolved.append((hw, f'Marathi tags={tags}', list(vals)))
                continue
        for tag, _ in senses:
            if NONLATIN.search(tag) or '; ' in tag or not tag:
                errs.append(f'{hw}: bad tag {tag!r}')
        out.append(hw + ': {' + '; '.join(t + ': ' + ' / '.join(vs) for t, vs in senses) + '}')
    unused = [h for h in MANUAL if h not in rows]
    if unused:
        print(f'note: MANUAL entries not in this input (fine for a part run): {unused}')
    with open(outp, 'w', encoding='utf-8', newline='\n') as f:
        f.write(f'# Pāli→Burmese pi-2 sense decisions, written by gen_decisions_my.py from {pathlib.Path(aggp).name}\n')
        f.write('# English tags: pi-1 Burmese senses (binding), else Marathi pi-2 senses (tags only), or MANUAL;\n')
        f.write('# values: pi-2 Burmese keyword map only.\n')
        f.write('\n'.join(out) + '\n')
    print(f'wrote {len(out)} decision lines -> {outp}')
    print(f'  MANUAL {stats["manual"]} | pi-1 senses unchanged {stats["p1_same"]} | pi-1 senses, subset '
          f'attested {stats["p1_subset"]} | pi-1 one sense + new values {stats["p1_lump"]} | Marathi tag '
          f'{stats["mr"]} | pi-1 matched by case only {stats["p1_case"]}')
    if review:
        print(f'REVIEW ({len(review)}): several Burmese values lumped into one sense; check, then add to '
              f'LUMP_OK or MANUAL:')
        for hw, why, vs in review:
            print(f'  {hw} [{why}]: {" / ".join(vs)}')
    if unresolved:
        print(f'UNRESOLVED ({len(unresolved)}): write MANUAL:')
        for hw, why, vs in unresolved:
            print(f'  {hw}\t{why}\tburmese={vs}')
    if errs:
        print(f'ERRORS ({len(errs)}):')
        for e in errs:
            print('  ' + e)
    return 1 if (unresolved or errs) else 0


if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    sys.exit(main(*sys.argv[1:]))
