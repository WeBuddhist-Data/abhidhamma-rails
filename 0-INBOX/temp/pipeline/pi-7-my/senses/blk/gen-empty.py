"""Write the Pāli→Burmese pi-7 decisions file for senses_my.py (brief: pi-7-my/burmese-senses-brief.md).
Adapted from pi-6-my/senses/gen_decisions_my.py (same engine and MANUAL / LUMP_OK / TAG_CHANGED / NEW_SENSE / MR_ADJUST
mechanism); the binding chain is now pi-6, then pi-5, pi-4, pi-3, pi-2, pi-1; the tags for headwords new in pi-7 come
from the Marathi pi-7 senses (tags only).

usage: python -I -X utf8 gen_decisions_my.py <agg.tsv> <decisions.txt>

For every headword of agg.tsv that has Burmese values (NDE-only headwords are skipped):
  1. a hand decision in MANUAL below wins;
  2. otherwise the approved Burmese senses are BINDING, pi-6 first, then pi-5, pi-4, pi-3, pi-2, pi-1 (each looked up
     exact, else the one case-insensitive match: the aggregation keeps the first spelling seen). The reference is the
     line of the first of pi-6 / pi-5 / pi-4 / pi-3 / pi-2 / pi-1 that has the headword. Every pi-7 value that the
     reference lists goes under the reference's sense with its English tag, in the reference's sense order (a sense
     with no pi-7 value is left out). A pi-7 value the reference does not list:
       - a later binding file lists it: that file's sense (tag) is added after the reference's, or the value joins the
         reference sense with the same tag (REVIEW);
       - otherwise, the reference has one sense: the value joins it (REVIEW unless the headword is in LUMP_OK);
       - otherwise (the reference has several senses): UNRESOLVED (write MANUAL);
  3. otherwise, if the Marathi pi-7 senses file gives the headword ONE English tag, the line is that tag + every
     attested Burmese value (one sense; several values -> REVIEW unless LUMP_OK); where that Marathi tag does not
     describe the headword the Burmese values show (e.g. the tag of a compound member, or a positive tag on a negated
     form), MR_ADJUST gives the adjusted English tag with its logged reason (only for such headwords);
  4. otherwise (several Marathi senses, or no Marathi line) the headword is UNRESOLVED: write MANUAL.
Only the ENGLISH tags are read from the Marathi file; its Marathi values are dropped on parsing and never written.
A MANUAL entry for a pi-6 / pi-5 / pi-4 / pi-3 / pi-2 / pi-1 headword must keep the binding split: every value the
binding senses list (pi-6's sense for it, else pi-5's, pi-4's, pi-3's, pi-2's, pi-1's) sits under a sense whose tag
starts with that binding tag (an appended «, …» is allowed) unless the headword is in TAG_CHANGED (logged reason); and a
MANUAL sense that holds only values the binding senses do not list, with a tag that starts with none of the binding
tags, is a NEW sense and the headword must be in NEW_SENSE (logged reason).
The script fails (exit 1) while anything is UNRESOLVED, a MANUAL value is not attested, a MANUAL entry omits an
attested value, a MANUAL entry breaks a binding sense, or a new sense is not logged in NEW_SENSE.
"""
import pathlib
import re
import sys
from collections import OrderedDict

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
BIND_FILES = OrderedDict([
    ('p6', ROOT / 'AI_translation/burmese/pi-6-pali-word-burmese-senses-plain.md'),
    ('p5', ROOT / 'AI_translation/burmese/pi-5-pali-word-burmese-senses-plain.md'),
    ('p4', ROOT / 'AI_translation/burmese/pi-4-pali-word-burmese-senses-plain.md'),
    ('p3', ROOT / 'AI_translation/burmese/pi-3-pali-word-burmese-senses-plain.md'),
    ('p2', ROOT / 'AI_translation/burmese/pi-2-pali-word-burmese-senses-plain.md'),
    ('p1', ROOT / 'AI_translation/burmese/pi-1-pali-word-burmese-senses-plain.md'),
])
BOOK = {'p6': 'pi-6', 'p5': 'pi-5', 'p4': 'pi-4', 'p3': 'pi-3', 'p2': 'pi-2', 'p1': 'pi-1'}
MR_SENSES = ROOT / 'AI_translation/marathi/pi-7-pali-word-marathi-senses-plain.md'
VAL_RE = re.compile(r'^(.*)=(\d+)\[[^\]]*\]$')
NONLATIN = re.compile(r'[\u0900-\u097f\u1000-\u109f]')

# Hand decisions: headword -> [(English tag, [Burmese values])]. Values must be attested.
# Binding senses first (pi-6, else pi-5, pi-4, pi-3, pi-2, pi-1 order and tag), then the senses new in pi-7.
MANUAL = OrderedDict([
    # ======== sample (agg-sample.tsv, the first 80 headwords) ========
    # @@MANUAL-SAMPLE
    # ======== full run (agg-part1.tsv) ========
    # @@MANUAL-FULL
])

# Binding headwords whose MANUAL entry deliberately departs from a binding tag (headword: reason).
TAG_CHANGED = {
    # @@TAGCH
}

# Binding headwords whose MANUAL entry adds a sense with values the binding senses do not list (headword: reason).
NEW_SENSE = {
    # ---- sample ----
    # @@NEW-SAMPLE
    # ---- full run ----
    # @@NEW-FULL
}

# Several Burmese values under one sense, or a value the binding sense does not list, checked by hand
# (variants or synonyms of one meaning, or the pi-7 text's own word for the binding meaning).
LUMP_OK = {
    # ---- sample ----
    # @@LUMP-SAMPLE
    # ---- full run: REVIEW headwords checked by hand ----
    # @@LUMP-FULL
}

# Headwords new in pi-7 (no binding line) whose single Marathi pi-7 tag does not describe the headword as the Burmese
# values show it: headword -> (adjusted English tag, reason).
MR_ADJUST = {
    # ---- sample ----
    # @@ADJ-SAMPLE
    # ---- full run ----
    # @@ADJ
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
    bind = OrderedDict((k, read_senses(p, True)) for k, p in BIND_FILES.items())
    mr = read_senses(MR_SENSES, False)
    out, unresolved, review, errs = [], [], [], []
    stats = OrderedDict([('manual', 0)])
    for k in bind:
        for s in ('same', 'subset', 'plus', 'lump'):
            stats[f'{k}_{s}'] = 0
    stats['mr'] = 0
    stats['mr_adjusted'] = 0
    adjusted = set()
    stats['case_only'] = 0
    for hw, vals in rows.items():
        if not vals:
            continue
        found = OrderedDict()                                   # src -> senses, in binding order
        for k, d in bind.items():
            kk = lookup(d, hw)
            if kk:
                found[k] = d[kk]
                if kk != hw and not [x for x in found if x != k]:
                    stats['case_only'] += 1
        of = {k: {v: t for t, vs in s for v in vs} for k, s in found.items()}
        bind_of = {}
        for k in reversed(list(found)):                         # pi-6 first where several list a value
            bind_of.update(of[k])
        bind_tags = [t for s in found.values() for t, _ in s]
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
            if found and hw not in TAG_CHANGED:
                for t, vs in senses:
                    for v in vs:
                        if v in bind_of and not t.startswith(bind_of[v]):
                            errs.append(f'{hw}: {v!r} leaves its binding sense {bind_of[v]!r}')
            if found:
                for t, vs in senses:
                    if all(v not in bind_of for v in vs) and not any(t.startswith(b) for b in bind_tags) \
                            and hw not in NEW_SENSE:
                        errs.append(f'{hw}: new sense {t!r} not logged in NEW_SENSE')
        elif found:
            src = next(iter(found))
            ref, ref_of = found[src], of[src]
            later = [k for k in found if k != src]
            new = [v for v in vals if v not in ref_of]
            senses = [(t, [v for v in vs if v in vals]) for t, vs in ref]
            senses = [(t, list(vs)) for t, vs in senses if vs]
            if not new:
                full = len(senses) == len(ref) and len(vals) == len(ref_of)
                stats[f'{src}_{"same" if full else "subset"}'] += 1
            elif all(any(v in of[k] for k in later) for v in new):
                for v in new:
                    k = next(k for k in later if v in of[k])
                    t1 = of[k][v]
                    hit = [s for s in senses if s[0] == t1]
                    if hit:
                        hit[0][1].append(v)
                    else:
                        senses.append((t1, [v]))
                stats[f'{src}_plus'] += 1
                if hw not in LUMP_OK:
                    review.append((hw, f'{BOOK[src]} senses + later binding sense for ' + ' / '.join(new),
                                   list(vals)))
            elif len(ref) == 1:
                senses = [(ref[0][0], list(vals))]
                stats[f'{src}_lump'] += 1
                if hw not in LUMP_OK:
                    review.append((hw, f'{BOOK[src]} one sense, new values ' + ' / '.join(new), list(vals)))
            else:
                unresolved.append((hw, f'{BOOK[src]} senses ' + str([t for t, _ in ref]), list(vals)))
                continue
        else:
            k3 = lookup(mr, hw)
            tags = mr.get(k3) if k3 else None
            if tags and len(tags) == 1:
                tag = tags[0]
                if hw in MR_ADJUST:
                    tag = MR_ADJUST[hw][0]
                    adjusted.add(hw)
                    stats['mr_adjusted'] += 1
                senses = [(tag, list(vals))]
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
    for h in MR_ADJUST:
        if h in rows and h not in adjusted:
            errs.append(f'{h}: MR_ADJUST entry for a headword that does not take a single Marathi tag')
        if not MR_ADJUST[h][1].strip():
            errs.append(f'{h}: MR_ADJUST entry without a reason')
    unused = [h for h in list(MANUAL) + list(LUMP_OK) + list(MR_ADJUST) if h not in rows]
    if unused:
        print(f'note: MANUAL / LUMP_OK entries not in this input (fine for a part run): {unused}')
    with open(outp, 'w', encoding='utf-8', newline='\n') as f:
        f.write(f'# Pāli→Burmese pi-7 sense decisions, written by gen_decisions_my.py from {pathlib.Path(aggp).name}\n')
        f.write('# English tags: pi-6, then pi-5, pi-4, pi-3, pi-2, pi-1 Burmese senses (binding), else Marathi pi-7 senses '
                '(tags only), or MANUAL;\n')
        f.write('# values: pi-7 Burmese keyword map only.\n')
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
