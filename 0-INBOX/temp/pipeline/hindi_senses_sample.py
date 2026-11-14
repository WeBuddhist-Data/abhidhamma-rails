"""word-sense-grouper helper, Pāli→Hindi (brief: 0-INBOX/temp/pipeline/hindi-senses-brief.md).

Build:   python -I -X utf8 senses_sample.py build  <agg.tsv> <decisions.txt> <out.md>
Verify:  python -I -X utf8 senses_sample.py verify <agg.tsv> <out.md>

agg.tsv line:   headword <TAB> english tags <TAB> hindi=count[ids] | ... <TAB> NDE=n
decisions.txt:  output-format lines for headwords that need a judgement call
                (multi-sense, empty English tags, or a split of one English sense).
                '#' lines and blank lines are ignored.
Default (headword not in decisions): one sense, tag = the single English tag's
description, candidates = every attested Hindi value, most frequent first.
Headwords whose default cannot be built (empty or multi-sense English) are
listed as UNRESOLVED and the build fails until a decision is written.
Inside each sense, candidates are re-sorted by attested count (desc).
An attested value containing " / " is written with " और " instead.
"""
import re
import sys
from collections import OrderedDict

DEVA = re.compile(r'[ऀ-ॿ]')
VAL_RE = re.compile(r'^(.*)=(\d+)\[[^\]]*\]$')


def norm_value(v):
    return v.replace(' / ', ' और ')


def parse_english(col):
    """'desc: val; desc2: val2' -> [desc, desc2]. Pieces without ': ' are glued back."""
    col = col.strip()
    if not col:
        return []
    pieces = []
    for p in col.split('; '):
        if pieces and ': ' not in p:
            pieces[-1] += '; ' + p
        else:
            pieces.append(p)
    tags = []
    for p in pieces:
        tags.append(p.rsplit(': ', 1)[0].strip() if ': ' in p else p.strip())
    return tags


def read_agg(path):
    rows = OrderedDict()
    order = []
    with open(path, encoding='utf-8-sig') as f:
        for n, line in enumerate(f, 1):
            line = line.rstrip('\n').rstrip('\r')
            if not line.strip():
                continue
            cols = line.split('\t')
            if len(cols) != 4:
                sys.exit(f'agg line {n}: expected 4 columns, got {len(cols)}')
            hw, eng, hin, nde = cols
            vals = OrderedDict()
            for item in [x.strip() for x in hin.split(' | ') if x.strip()]:
                m = VAL_RE.match(item)
                if not m:
                    sys.exit(f'agg line {n}: cannot parse value {item!r}')
                vals[m.group(1)] = vals.get(m.group(1), 0) + int(m.group(2))
            order.append(hw)
            rows[hw] = {'eng': parse_english(eng), 'vals': vals, 'nde': nde, 'line': n}
    return order, rows


def parse_out_line(line):
    """'hw: {t: a / b; t2: c}' -> (hw, [(t, [a, b]), (t2, [c])])"""
    i = line.find(': {')
    if i < 0 or not line.endswith('}'):
        raise ValueError(f'bad line: {line!r}')
    hw = line[:i]
    body = line[i + 3:-1]
    senses = []
    for s in body.split('; '):
        if ': ' not in s:
            raise ValueError(f'sense without "tag: value" in {hw!r}: {s!r}')
        tag, vals = s.rsplit(': ', 1)
        senses.append((tag.strip(), [v.strip() for v in vals.split(' / ')]))
    return hw, senses


def read_decisions(path):
    dec = OrderedDict()
    with open(path, encoding='utf-8-sig') as f:
        for n, line in enumerate(f, 1):
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            hw, senses = parse_out_line(line)
            if hw in dec:
                sys.exit(f'decisions line {n}: duplicate headword {hw!r}')
            dec[hw] = senses
    return dec


def fmt(hw, senses):
    return hw + ': {' + '; '.join(t + ': ' + ' / '.join(v) for t, v in senses) + '}'


def build(agg, decp, outp):
    order, rows = read_agg(agg)
    dec = read_decisions(decp)
    unknown = [h for h in dec if h not in rows]
    if unknown:
        sys.exit(f'decisions for headwords not in input: {unknown}')
    out, unresolved, lumped, rewrites = [], [], [], []
    for hw in order:
        r = rows[hw]
        counts = {norm_value(v): c for v, c in r['vals'].items()}
        rewrites += [(hw, v) for v in r['vals'] if ' / ' in v]
        if not r['vals']:
            continue  # NDE-only: omitted (skill step 4)
        if hw in dec:
            senses = [(t, sorted(vs, key=lambda v: -counts.get(v, 0))) for t, vs in dec[hw]]
        elif len(r['eng']) == 1:
            vs = sorted(counts, key=lambda v: -counts[v])
            senses = [(r['eng'][0], vs)]
            if len(vs) > 1:
                lumped.append((hw, vs))
        else:
            unresolved.append((hw, r['eng'], list(counts)))
            continue
        out.append(fmt(hw, senses))
    if unresolved:
        print(f'UNRESOLVED ({len(unresolved)}): write a decision line for each')
        for hw, eng, vs in unresolved:
            print(f'  {hw}\teng={eng}\thindi={vs}')
        sys.exit(1)
    with open(outp, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(out) + '\n')
    print(f'wrote {len(out)} lines -> {outp}')
    if lumped:
        print(f'REVIEW: {len(lumped)} default single-sense lines lump several values '
              f'(check they are synonyms, else add a decision):')
        for hw, vs in lumped:
            print(f'  {hw}: {" / ".join(vs)}')
    if rewrites:
        print(f'" / " -> " और " rewrites ({len(rewrites)}):')
        for hw, v in rewrites:
            print(f'  {hw}: {v!r}')
    return verify(agg, outp)


def verify(agg, outp):
    order, rows = read_agg(agg)
    expected = [h for h in order if rows[h]['vals']]  # NDE-only words are omitted
    nde_only = [h for h in order if not rows[h]['vals']]
    errs = []
    got, parsed = [], {}
    with open(outp, encoding='utf-8-sig') as f:
        for n, line in enumerate(f, 1):
            line = line.rstrip('\n')
            if not line.strip():
                continue
            try:
                hw, senses = parse_out_line(line)
            except ValueError as e:
                errs.append(f'line {n}: {e}')
                continue
            if hw in parsed:
                errs.append(f'line {n}: duplicate headword {hw!r}')
            got.append(hw)
            parsed[hw] = senses
    print(f'input headwords: {len(order)} (NDE-only omitted: {len(nde_only)}) | '
          f'expected lines: {len(expected)} | output lines: {len(got)}')
    if got != expected:
        missing = [h for h in expected if h not in parsed]
        extra = [h for h in got if h not in rows or h in nde_only]
        errs.append(f'headword list differs: missing={missing} extra={extra}')
        if not missing and not extra:
            for i, (a, b) in enumerate(zip(expected, got)):
                if a != b:
                    errs.append(f'order differs first at #{i + 1}: expected {a!r}, got {b!r}')
                    break
    multi_sense = multi_cand = n_senses = 0
    for hw, senses in parsed.items():
        if hw not in rows:
            continue
        att = {norm_value(v) for v in rows[hw]['vals']}
        seen = []
        n_senses += len(senses)
        if len(senses) > 1:
            multi_sense += 1
        for tag, vs in senses:
            if len(vs) > 1:
                multi_cand += 1
            if not tag:
                errs.append(f'{hw}: empty tag')
            if DEVA.search(tag):
                errs.append(f'{hw}: tag not in English: {tag!r}')
            for v in vs:
                if not v:
                    errs.append(f'{hw}: empty candidate')
                if v == tag:
                    errs.append(f'{hw}: tag copies value {v!r}')
                if '/' in v or '; ' in v:
                    errs.append(f'{hw}: candidate contains "/" or "; ": {v!r}')
                if v in seen:
                    errs.append(f'{hw}: candidate listed twice: {v!r}')
                seen.append(v)
        missing = att - set(seen)
        extra = set(seen) - att
        if missing:
            errs.append(f'{hw}: attested values missing: {sorted(missing)}')
        if extra:
            errs.append(f'{hw}: values not attested in input: {sorted(extra)}')
    print(f'senses: {n_senses} | headwords with >1 sense: {multi_sense} | '
          f'senses with >1 candidate: {multi_cand}')
    if errs:
        print(f'VERIFY FAILED ({len(errs)}):')
        for e in errs:
            print('  ' + e)
        return 1
    print('VERIFY OK: headwords equal and in order, no duplicates, all attested values present')
    return 0


if __name__ == '__main__':
    if len(sys.argv) == 5 and sys.argv[1] == 'build':
        sys.exit(build(*sys.argv[2:]))
    if len(sys.argv) == 4 and sys.argv[1] == 'verify':
        sys.exit(verify(*sys.argv[2:]))
    sys.exit(__doc__)
