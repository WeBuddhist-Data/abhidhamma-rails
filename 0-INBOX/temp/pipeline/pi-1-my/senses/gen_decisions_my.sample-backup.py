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
])

# One Marathi tag, several Burmese values, checked by hand: one sense.
LUMP_OK = {
    'uppannaṃ',          # ဖြစ်ပေါ်လာသော / ဖြစ်ပေါ်သော / ဖြစ်ပေါ်ပြီးသော: tense variants of one verb
    'arūpino dhammā',    # with / without the ellipsis of the closing formula
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
