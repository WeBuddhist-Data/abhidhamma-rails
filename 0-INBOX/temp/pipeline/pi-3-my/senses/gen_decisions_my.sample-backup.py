"""Write the Pāli→Burmese pi-3 decisions file for senses_my.py (brief: pi-3-my/burmese-senses-brief.md).
Adapted from pi-2-my/senses/gen_decisions_my.py (same MANUAL / LUMP_OK mechanism).

usage: python -I -X utf8 gen_decisions_my.py <agg.tsv> <decisions.txt>

For every headword of agg.tsv that has Burmese values (NDE-only headwords are skipped):
  1. a hand decision in MANUAL below wins;
  2. otherwise the approved Burmese senses are BINDING, pi-2 first, then pi-1 (each looked up exact, else the
     one case-insensitive match: the aggregation keeps the first spelling seen). The reference is pi-2's line
     if pi-2 has the headword, else pi-1's. Every pi-3 value that the reference lists goes under the reference's
     sense with its English tag, in the reference's sense order (a sense with no pi-3 value is left out).
     A pi-3 value the reference does not list:
       - pi-2 is the reference and pi-1 lists the value: pi-1's sense (tag) is added after pi-2's (REVIEW);
       - the reference has one sense: the value joins it (REVIEW unless the headword is in LUMP_OK);
       - the reference has several senses: UNRESOLVED (write MANUAL);
  3. otherwise, if the Marathi pi-3 senses file gives the headword ONE English tag, the line is that tag + every
     attested Burmese value (one sense; several values -> REVIEW unless LUMP_OK);
  4. otherwise (several Marathi senses, or no Marathi line) the headword is UNRESOLVED: write MANUAL.
Only the ENGLISH tags are read from the Marathi file; its Marathi values are dropped on parsing and never written.
A MANUAL entry for a pi-2 / pi-1 headword must keep the binding split: every value the binding senses list (pi-2's
sense for it, else pi-1's) sits under a sense whose tag starts with that binding tag (an appended «, the same value
also naming …» is allowed) unless the headword is in TAG_CHANGED (logged reason); and a MANUAL sense that holds
only values the binding senses do not list, with a tag that starts with none of the binding tags, is a NEW sense
and the headword must be in NEW_SENSE (logged reason, e.g. saṅgaha = inclusion).
The script fails (exit 1) while anything is UNRESOLVED, a MANUAL value is not attested, a MANUAL entry omits an
attested value, a MANUAL entry breaks a binding sense, or a new sense is not logged in NEW_SENSE.
"""
import pathlib
import re
import sys
from collections import OrderedDict

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
MY2_SENSES = ROOT / 'AI_translation/burmese/pi-2-pali-word-burmese-senses-plain.md'
MY1_SENSES = ROOT / 'AI_translation/burmese/pi-1-pali-word-burmese-senses-plain.md'
MR_SENSES = ROOT / 'AI_translation/marathi/pi-3-pali-word-marathi-senses-plain.md'
VAL_RE = re.compile(r'^(.*)=(\d+)\[[^\]]*\]$')
NONLATIN = re.compile(r'[ऀ-ॿက-႟]')

# Hand decisions: headword -> [(English tag, [Burmese values])]. Values must be attested.
# Binding senses first (pi-2, else pi-1 order and tag), then the senses new in pi-3.
MANUAL = OrderedDict([
    # ---- sample: the Dhātukathā's methods, a genuinely new sense (the pi-2 / pi-1 value is not attested);
    #      tag: 'inclusion' / 'dissociation' + the Marathi pi-3 tag, as asaṅgaho / asaṅgaha (Marathi tags) ----
    ('vippayogo', [
        ('dissociation, the method of non-conjunction, in sampayogo vippayogo (nominative noun)',
         ['ကင်းကွာခြင်း']),
    ]),
    ('saṅgaho', [
        ('inclusion, the method of comprising within a category, in saṅgaho asaṅgaho (nominative noun)',
         ['အကျုံးဝင်ခြင်း']),
    ]),
    ('saṅgaha', [
        ('inclusion, comprising, as heading compound member (Saṅgahāsaṅgahapadaniddeso)', ['အကျုံးဝင်ခြင်း']),
    ]),
    # ---- sample: new in pi-3, the Marathi tag adjusted to the Burmese evidence ----
    ('bhāga', [
        # Marathi 'class or portion': the Burmese «သဘော» (sabhāgo «တူညီသော သဘော», visabhāgo «ကွဲပြားသော သဘော»,
        # ^3-4) is kind, nature; 'portion' has no Burmese evidence
        ('class, kind, in sabhāga and visabhāga (compound final)', ['သဘော']),
    ]),
])

# Binding headwords whose MANUAL entry deliberately departs from a binding tag (headword: reason).
TAG_CHANGED = {}

# Binding headwords whose MANUAL entry adds a sense with values the binding senses do not list (headword: reason).
NEW_SENSE = {
    'vippayogo': "pi-2 «ကွေကွင်းရခြင်း» is separation from the loved (not attested in pi-3); pi-3 «ကင်းကွာခြင်း» "
                 "is the method of dissociation (approved mapper sample)",
    'saṅgaho': "pi-1 «စုစည်းခြင်း» is the compendium, grouping into kinds (Rūpasaṅgaho, not attested in pi-3); "
               "pi-3 «အကျုံးဝင်ခြင်း» is inclusion (approved mapper sample)",
    'saṅgaha': "pi-2 «အကျဉ်းချုပ်» is summary (Saṅgahavāra, not attested in pi-3); pi-3 «အကျုံးဝင်ခြင်း» is "
               "inclusion (approved mapper sample)",
}

# Several Burmese values under one sense, or a value the binding sense does not list, checked by hand
# (variants or synonyms of one meaning, or the pi-3 text's own word for the binding meaning).
LUMP_OK = {
    # ---- sample ----
    'nayo',    # «ခွဲနည်း» (pi-3 text, mapper M8) = pi-1's 'method of analysis' «နည်း»: the same meaning, one sense
    'bodhi',   # «ဗောဇ္ဈင်» (bojjhaṅga as one Burmese word, mapper) = pi-2's 'enlightenment, in bojjhaṅga': one sense
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
    my2 = read_senses(MY2_SENSES, True)
    my1 = read_senses(MY1_SENSES, True)
    mr = read_senses(MR_SENSES, False)
    out, unresolved, review, errs = [], [], [], []
    stats = OrderedDict((k, 0) for k in (
        'manual', 'p2_same', 'p2_subset', 'p2_plus_p1', 'p2_lump', 'p1_same', 'p1_subset', 'p1_lump', 'mr',
        'case_only'))
    for hw, vals in rows.items():
        if not vals:
            continue
        k2, k1 = lookup(my2, hw), lookup(my1, hw)
        p2 = my2.get(k2) if k2 else None
        p1 = my1.get(k1) if k1 else None
        if (k2 and k2 != hw) or (not p2 and k1 and k1 != hw):
            stats['case_only'] += 1
        p2_of = {v: t for t, vs in (p2 or []) for v in vs}
        p1_of = {v: t for t, vs in (p1 or []) for v in vs}
        bind_of = dict(p1_of)
        bind_of.update(p2_of)                                     # pi-2 first where both list a value
        bind_tags = [t for t, _ in (p2 or [])] + [t for t, _ in (p1 or [])]
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
            if (p2 or p1) and hw not in TAG_CHANGED:
                for t, vs in senses:
                    for v in vs:
                        if v in bind_of and not t.startswith(bind_of[v]):
                            errs.append(f'{hw}: {v!r} leaves its binding sense {bind_of[v]!r}')
            if p2 or p1:
                for t, vs in senses:
                    if all(v not in bind_of for v in vs) and not any(t.startswith(b) for b in bind_tags) \
                            and hw not in NEW_SENSE:
                        errs.append(f'{hw}: new sense {t!r} not logged in NEW_SENSE')
        elif p2 or p1:
            ref, ref_of, src = (p2, p2_of, 'p2') if p2 else (p1, p1_of, 'p1')
            new = [v for v in vals if v not in ref_of]
            if not new:
                senses = [(t, [v for v in vs if v in vals]) for t, vs in ref]
                senses = [(t, vs) for t, vs in senses if vs]
                full = len(senses) == len(ref) and len(vals) == len(ref_of)
                stats[f'{src}_{"same" if full else "subset"}'] += 1
            elif src == 'p2' and all(v in p1_of for v in new):
                senses = [(t, [v for v in vs if v in vals]) for t, vs in p2]
                senses = [(t, vs) for t, vs in senses if vs]
                for v in new:
                    t1 = p1_of[v]
                    hit = [s for s in senses if s[0] == t1]
                    if hit:
                        hit[0][1].append(v)
                    else:
                        senses.append((t1, [v]))
                stats['p2_plus_p1'] += 1
                if hw not in LUMP_OK:
                    review.append((hw, 'pi-2 senses + pi-1 sense for ' + ' / '.join(new), list(vals)))
            elif len(ref) == 1:
                senses = [(ref[0][0], list(vals))]
                stats[f'{src}_lump'] += 1
                if hw not in LUMP_OK:
                    review.append((hw, f'{"pi-2" if src == "p2" else "pi-1"} one sense, new values '
                                   + ' / '.join(new), list(vals)))
            else:
                unresolved.append((hw, f'{"pi-2" if src == "p2" else "pi-1"} senses '
                                   + str([t for t, _ in ref]), list(vals)))
                continue
        else:
            k3 = lookup(mr, hw)
            tags = mr.get(k3) if k3 else None
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
    unused = [h for h in list(MANUAL) + list(LUMP_OK) if h not in rows]
    if unused:
        print(f'note: MANUAL / LUMP_OK entries not in this input (fine for a part run): {unused}')
    with open(outp, 'w', encoding='utf-8', newline='\n') as f:
        f.write(f'# Pāli→Burmese pi-3 sense decisions, written by gen_decisions_my.py from {pathlib.Path(aggp).name}\n')
        f.write('# English tags: pi-2 then pi-1 Burmese senses (binding), else Marathi pi-3 senses (tags only), '
                'or MANUAL;\n')
        f.write('# values: pi-3 Burmese keyword map only.\n')
        f.write('\n'.join(out) + '\n')
    print(f'wrote {len(out)} decision lines -> {outp}')
    print('  ' + ' | '.join(f'{k} {v}' for k, v in stats.items()))
    if review:
        print(f'REVIEW ({len(review)}): check, then add to LUMP_OK or MANUAL:')
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
