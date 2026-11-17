"""word-sense-grouper helper, Pāli→Russian, pi-2 Vibhaṅga (brief: 0-INBOX/temp/pipeline/pi-2-ru/ru-senses-brief.md).
Adapted 2026-11-17 from ../../pi-1-ru/senses/senses_tool_ru.py (pi-2 paths; new `prior` command).
EVERY headword needs a hand-written decision line (the tag table is written headword by headword).

Run from anywhere; paths are resolved against this folder.

  python -I -X utf8 senses_tool_ru.py build  --part K     # agg-partK.tsv + decisions-partK.txt -> partK-senses.md, then verify
  python -I -X utf8 senses_tool_ru.py verify --part K     # agg-partK.tsv vs partK-senses.md
  python -I -X utf8 senses_tool_ru.py todo   --part K     # headwords of agg-partK.tsv still without a decision line
  python -I -X utf8 senses_tool_ru.py prior  --part K     # for each todo headword: agg row + approved pi-1/pi-4/pi-5
                                                           # Russian senses lines + pi-2 English senses line
  python -I -X utf8 senses_tool_ru.py reuse  --part K     # lines of partK-senses.md reusing a pi-1 tag verbatim (report)
  (--part sample uses agg-sample.tsv, decisions-sample.txt, sample-senses.md)
  python -I -X utf8 senses_tool_ru.py prior <headword> [<headword> ...]
  python -I -X utf8 senses_tool_ru.py show <headword> [<russian value>] [<max segments>] [<width>]
     (<width> > 0 cuts each printed line to that many characters around the match; '' as value = any)
     all ids of that headword[=value] in the pi-2 Russian map (case-insensitive headword), then, for
     the first segments, the Pāli/Russian line pairs whose Russian contains the value (the part before
     " … " for gapped values), or whose Pāli contains the headword when no value is given; default 4.
  Explicit paths still work:  build <agg.tsv> <decisions.txt> <out.md> | verify <agg.tsv> <out.md> | todo <agg.tsv> <decisions.txt>

agg.tsv line:   headword <TAB> en≈ hints <TAB> russian=count[ids] | ... <TAB> NDE=n
decisions file: one line per headword ('#' lines and blank lines are ignored), two forms:
  hw: {tag}                         single sense; candidates = every attested value
  hw: {tag1: v1 / v2; tag2: v3 / *} explicit senses; '*' = every attested value not listed elsewhere
                                    on the line. Each attested value must be placed exactly once.
Inside each sense, candidates are re-sorted by attested count (desc); senses keep the written order.
An attested value containing " / " is written with " и " instead (use the rewritten form in decisions).
Tags: English, no Cyrillic, no ': ', no '; ', no braces, not equal to a value, not a bare English hint,
no two senses of one headword with the same tag.
"""
import os
import re
import sys
from collections import OrderedDict

ROOT = r'D:\Work\OpenPecha\abhidhamma-rails'
HERE = os.path.dirname(os.path.abspath(__file__))
MAP = os.path.join(ROOT, r'AI_translation\russian\pi-2-keywords-by-reference-pali-russian-plain.md')
PDIR = os.path.join(ROOT, r'AI_translation\pali\pi-2_split_chapters')
RDIR = os.path.join(ROOT, r'AI_translation\russian\pi-2-russian-plain-zeroshot_split_chapters')
PRIOR = [
    ('pi-1 ru', os.path.join(ROOT, r'AI_translation\russian\pi-1-pali-word-russian-senses-plain.md')),
    ('pi-4 ru', os.path.join(ROOT, r'AI_translation\russian\pi-4-pali-word-russian-senses-plain.md')),
    ('pi-5 ru', os.path.join(ROOT, r'AI_translation\russian\pi-5-pali-word-russian-senses-plain.md')),
    ('pi-2 en', os.path.join(ROOT, r'AI_translation\english\pi-2-english-senses-plain.md')),
]

CYR = re.compile(r'[Ѐ-ӿ]')
VAL_RE = re.compile(r'^(.*)=(\d+)\[[^\]]*\]$')
HINT_RE = re.compile(r'^(.*) ×\d+$')


def norm_value(v):
    return v.replace(' / ', ' и ')


def part_paths(k):
    if k == 'sample':
        return (os.path.join(HERE, 'agg-sample.tsv'), os.path.join(HERE, 'decisions-sample.txt'),
                os.path.join(HERE, 'sample-senses.md'))
    return (os.path.join(HERE, f'agg-part{k}.tsv'), os.path.join(HERE, f'decisions-part{k}.txt'),
            os.path.join(HERE, f'part{k}-senses.md'))


def read_agg(path):
    rows = OrderedDict()
    with open(path, encoding='utf-8-sig') as f:
        for n, line in enumerate(f, 1):
            line = line.rstrip('\r\n')
            if not line.strip():
                continue
            cols = line.split('\t')
            if len(cols) != 4:
                sys.exit(f'agg line {n}: expected 4 columns, got {len(cols)}')
            hw, eng, rus, nde = cols
            if hw in rows:
                sys.exit(f'agg line {n}: duplicate headword {hw!r}')
            vals = OrderedDict()
            for item in [x.strip() for x in rus.split(' | ') if x.strip()]:
                m = VAL_RE.match(item)
                if not m:
                    sys.exit(f'agg line {n}: cannot parse value {item!r}')
                vals[m.group(1)] = vals.get(m.group(1), 0) + int(m.group(2))
            hints = []
            e = eng.strip()
            if e.startswith('en≈'):
                for h in e[3:].split(' | '):
                    m = HINT_RE.match(h.strip())
                    hints.append((m.group(1) if m else h).strip())
            rows[hw] = {'hints': hints, 'eng': eng, 'vals': vals, 'nde': nde, 'line': n}
    return rows


def parse_out_line(line, allow_tag_only=False):
    """'hw: {t: a / b; t2: c}' -> (hw, [(t, [a, b]), (t2, [c])]); 'hw: {t}' -> (hw, [(t, None)])"""
    i = line.find(': {')
    if i < 0 or not line.endswith('}'):
        raise ValueError(f'bad line: {line!r}')
    hw = line[:i]
    body = line[i + 3:-1]
    if allow_tag_only and ': ' not in body:
        return hw, [(body.strip(), None)]
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
            try:
                hw, senses = parse_out_line(line, allow_tag_only=True)
            except ValueError as e:
                sys.exit(f'decisions line {n}: {e}')
            if hw in dec:
                sys.exit(f'decisions line {n}: duplicate headword {hw!r}')
            dec[hw] = (n, senses)
    return dec


def fmt(hw, senses):
    return hw + ': {' + '; '.join(t + ': ' + ' / '.join(v) for t, v in senses) + '}'


def resolve(hw, row, senses):
    """Expand tag-only and '*' forms; return (senses, errors)."""
    counts = OrderedDict((norm_value(v), c) for v, c in row['vals'].items())
    errs = []
    if len(senses) == 1 and senses[0][1] is None:
        return [(senses[0][0], sorted(counts, key=lambda v: -counts[v]))], errs
    listed = [v for _, vs in senses for v in vs if v != '*']
    for v in listed:
        if v not in counts:
            errs.append(f'{hw}: decision lists a value that is not attested: {v!r}')
    rest = [v for v in counts if v not in listed]
    stars = sum(vs.count('*') for _, vs in senses)
    if stars > 1:
        errs.append(f'{hw}: more than one "*"')
    out = []
    for tag, vs in senses:
        full = []
        for v in vs:
            full.extend(rest if v == '*' else [v])
        out.append((tag, sorted(full, key=lambda v: -counts.get(v, 0))))
    if stars == 0 and rest:
        errs.append(f'{hw}: attested values not placed: {rest}')
    return out, errs


def build(aggp, decp, outp):
    rows = read_agg(aggp)
    dec = read_decisions(decp)
    errs = [f'decision for headword not in input: {h!r}' for h in dec if h not in rows]
    missing = [h for h in rows if h not in dec and rows[h]['vals']]
    if missing:
        errs.append(f'{len(missing)} headwords without a decision (run "todo"): {missing[:20]}')
    out, rewrites = [], []
    for hw, r in rows.items():
        rewrites += [(hw, v) for v in r['vals'] if ' / ' in v]
        if not r['vals'] or hw not in dec:
            continue
        senses, e = resolve(hw, r, dec[hw][1])
        errs += e
        out.append(fmt(hw, senses))
    if errs:
        print(f'BUILD FAILED ({len(errs)}):')
        for e in errs:
            print('  ' + e)
        return 1
    with open(outp, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(out) + '\n')
    print(f'wrote {len(out)} lines -> {outp}')
    if rewrites:
        print(f'" / " -> " и " rewrites ({len(rewrites)}):')
        for hw, v in rewrites:
            print(f'  {hw}: {v!r}')
    else:
        print('" / " -> " и " rewrites: 0')
    return verify(aggp, outp)


def verify(aggp, outp):
    rows = read_agg(aggp)
    expected = [h for h in rows if rows[h]['vals']]
    nde_only = [h for h in rows if not rows[h]['vals']]
    errs, got, parsed = [], [], {}
    with open(outp, encoding='utf-8-sig') as f:
        for n, line in enumerate(f, 1):
            line = line.rstrip('\r\n')
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
    print(f'input headwords: {len(rows)} (NDE-only omitted: {len(nde_only)}) | '
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
    else:
        print('headword list: equal to input, same order, no duplicates')
    multi_sense = multi_cand = n_senses = 0
    for hw, senses in parsed.items():
        if hw not in rows:
            continue
        att = {norm_value(v) for v in rows[hw]['vals']}
        hints = {h.lower() for h in rows[hw]['hints']}
        seen, tags = [], []
        n_senses += len(senses)
        multi_sense += len(senses) > 1
        for tag, vs in senses:
            multi_cand += len(vs) > 1
            if not tag:
                errs.append(f'{hw}: empty tag')
            if CYR.search(tag):
                errs.append(f'{hw}: tag not in English: {tag!r}')
            if any(c in tag for c in '{}') or '; ' in tag:
                errs.append(f'{hw}: tag contains a brace or "; ": {tag!r}')
            if tag.lower() in hints:
                errs.append(f'{hw}: tag is a bare copy of an English hint: {tag!r}')
            if tag in tags:
                errs.append(f'{hw}: two senses share the tag {tag!r}')
            tags.append(tag)
            for v in vs:
                if not v:
                    errs.append(f'{hw}: empty candidate')
                if v.lower() == tag.lower():
                    errs.append(f'{hw}: tag copies value {v!r}')
                if '/' in v or '; ' in v:
                    errs.append(f'{hw}: candidate contains "/" or "; ": {v!r}')
                if v in seen:
                    errs.append(f'{hw}: candidate listed twice: {v!r}')
                seen.append(v)
        miss = att - set(seen)
        extra = set(seen) - att
        if miss:
            errs.append(f'{hw}: attested values missing: {sorted(miss)}')
        if extra:
            errs.append(f'{hw}: values not attested in input: {sorted(extra)}')
    print(f'senses: {n_senses} | headwords with >1 sense: {multi_sense} | '
          f'senses with >1 candidate: {multi_cand}')
    if errs:
        print(f'VERIFY FAILED ({len(errs)}):')
        for e in errs:
            print('  ' + e)
        return 1
    print('VERIFY OK: headwords equal and in order, no duplicates, all attested values present, '
          'lines parse, tags English and not copies of values or hints')
    return 0


def todo(aggp, decp):
    rows = read_agg(aggp)
    dec = read_decisions(decp) if os.path.exists(decp) else {}
    left = [h for h in rows if h not in dec and rows[h]['vals']]
    print(f'{len(left)} of {len(rows)} headwords without a decision')
    for h in left:
        r = rows[h]
        vs = ' | '.join(f'{v}={c}' for v, c in r['vals'].items())
        print(f'{h}\t{r["eng"]}\t{vs}')
    return 0


def _prior_index():
    idx = []
    for label, path in PRIOR:
        d = {}
        if os.path.exists(path):
            with open(path, encoding='utf-8-sig') as f:
                for line in f:
                    line = line.rstrip('\r\n')
                    if ': {' in line:
                        d.setdefault(line.split(': {', 1)[0].lower(), []).append(line)
        idx.append((label, d))
    return idx


def prior(hws, rows=None):
    idx = _prior_index()
    for h in hws:
        if rows and h in rows:
            r = rows[h]
            print(f'== {h}\t' + ' | '.join(f'{v}={c}' for v, c in r['vals'].items()) + f'\t{r["eng"]}')
        else:
            print(f'== {h}')
        for label, d in idx:
            for line in d.get(h.lower(), []):
                print(f'   [{label}] {line}')
    return 0


def reuse(outp):
    """Count output lines with at least one tag copied verbatim from the pi-1 Russian senses file."""
    pi1 = {}
    with open(PRIOR[0][1], encoding='utf-8-sig') as f:
        for line in f:
            line = line.rstrip('\r\n')
            if ': {' in line:
                try:
                    hw, senses = parse_out_line(line)
                except ValueError:
                    continue
                pi1.setdefault(hw.lower(), set()).update(t for t, _ in senses)
    n = full = has = 0
    for line in _lines(outp):
        hw, senses = parse_out_line(line)
        n += 1
        prior_tags = pi1.get(hw.lower())
        if prior_tags is None:
            continue
        has += 1
        same = [t for t, _ in senses if t in prior_tags]
        if same:
            full += 1
    print(f'lines: {n} | headword also in pi-1: {has} | lines reusing a pi-1 tag verbatim: {full}')
    return 0


def _lines(path):
    with open(path, encoding='utf-8-sig') as f:
        return [l for l in f.read().splitlines() if l.strip()]


def _win(text, probe, width):
    """Cut a long line to `width` chars around the first match of probe (whole line if width is 0)."""
    if not width or len(text) <= width:
        return text
    i = text.lower().find(probe.lower()) if probe else -1
    if i < 0:
        return text[:width] + ' …'
    a = max(0, i - width // 2)
    return ('… ' if a else '') + text[a:a + width] + (' …' if a + width < len(text) else '')


def show(hw, value=None, maxn=4, width=0):
    ids = []
    with open(MAP, encoding='utf-8-sig') as f:
        for line in f:
            if '] ' not in line:
                continue
            i, body = line.rstrip('\n').split('] ', 1)
            for pair in body.split(', '):
                k, _, v = pair.partition('=')
                if k.lower() == hw.lower() and (value is None or v == value):
                    ids.append((i[1:], v))
    print(f'{hw}{"=" + value if value else ""}: {len(ids)} occurrences')
    print('  ' + ' '.join(f'{i}={v}' if value is None else i for i, v in ids))
    want = []
    for i, _ in ids:
        if i not in want:
            want.append(i)
    want = want[:maxn]
    idre = re.compile(r'\^([0-9A-Za-z-]+)\s*$')
    for name in sorted(os.listdir(PDIR)):
        if not name.endswith('.md') or not want or not os.path.exists(os.path.join(RDIR, name)):
            continue
        p = _lines(os.path.join(PDIR, name))
        r = _lines(os.path.join(RDIR, name))
        if len(p) != len(r):
            print(f'  (skip {name}: line counts differ)')
            continue
        bp, br = [], []
        for a, b in zip(p, r):
            bp.append(a)
            br.append(b)
            m = idre.search(a)
            if m:
                if m.group(1) in want:
                    print(f'--- {name} ^{m.group(1)}')
                    probe = value.split(' … ')[0] if value else None
                    if probe and len(probe) > 5:
                        probe = probe[:-2]  # crude stem, so inflected Russian forms match
                    hits = [(x, y) for x, y in zip(bp, br)
                            if (probe.lower() in y.lower() if probe else hw.lower() in x.lower())]
                    for x, y in (hits or list(zip(bp, br))[:3]):
                        print(f'P: {_win(x, hw, width)}\nR: {_win(y, probe, width)}')
                bp, br = [], []
    return 0


if __name__ == '__main__':
    a = sys.argv[1:]
    if len(a) == 3 and a[1] == '--part' and a[0] in ('build', 'verify', 'todo', 'prior', 'reuse'):
        aggp, decp, outp = part_paths(a[2])
        if a[0] == 'reuse':
            sys.exit(reuse(outp))
        if a[0] == 'build':
            sys.exit(build(aggp, decp, outp))
        if a[0] == 'verify':
            sys.exit(verify(aggp, outp))
        if a[0] == 'prior':
            rows = read_agg(aggp)
            dec = read_decisions(decp) if os.path.exists(decp) else {}
            sys.exit(prior([h for h in rows if h not in dec and rows[h]['vals']], rows))
        sys.exit(todo(aggp, decp))
    if len(a) == 4 and a[0] == 'build':
        sys.exit(build(*a[1:]))
    if len(a) == 3 and a[0] == 'verify':
        sys.exit(verify(*a[1:]))
    if len(a) == 3 and a[0] == 'todo':
        sys.exit(todo(*a[1:]))
    if len(a) >= 2 and a[0] == 'prior':
        sys.exit(prior(a[1:]))
    if len(a) >= 2 and a[0] == 'show':
        sys.exit(show(a[1], a[2] if len(a) > 2 and a[2] else None, int(a[3]) if len(a) > 3 else 4,
                      int(a[4]) if len(a) > 4 else 0))
    sys.exit(__doc__)
