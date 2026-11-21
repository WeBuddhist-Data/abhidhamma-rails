"""word-sense-grouper helper, Pāli→Vietnamese, pi-4 Puggalapaññatti (brief: 0-INBOX/temp/pipeline/pi-4-vi-ai/vi-senses-brief.md).
Adapted 2026-11-20 from ../../pi-3-vi-ai/senses/senses_tool_vi.py (pi-4 paths; `prior` shows the approved
pi-3, pi-2 and pi-1 Vietnamese and the pi-4 Russian senses lines, plus the pi-4 English hint; `reuse` counts
tags copied from pi-1, pi-2 OR pi-3 Vietnamese).
EVERY headword needs a hand-written decision line (the tag table is written headword by headword).
Parts 1-3: use this file READ-ONLY (call it, do not edit it).

Run from anywhere; paths are resolved against this folder. K = 1..3 or sample.

  python -I -X utf8 senses_tool_vi.py build  --part K     # agg-partK.tsv + decisions-partK.txt -> partK-senses.md, then verify
  python -I -X utf8 senses_tool_vi.py verify --part K     # agg-partK.tsv vs partK-senses.md
  python -I -X utf8 senses_tool_vi.py todo   --part K     # headwords of agg-partK.tsv still without a decision line
  python -I -X utf8 senses_tool_vi.py prior  --part K     # each todo headword: agg row + [pi-3 vi] + [pi-2 vi] + [pi-1 vi]
                                                           # + [pi-4 ru] senses lines (+ [pi-4 en] hint)
  python -I -X utf8 senses_tool_vi.py reuse  --part K     # lines of partK-senses.md reusing a pi-1 / pi-2 / pi-3 Vietnamese tag verbatim
  (--part sample uses agg-sample.tsv, decisions-sample.txt, sample-senses.md)
  python -I -X utf8 senses_tool_vi.py sample --part K     # same as build, kept for the brief's wording (build + verify)
  python -I -X utf8 senses_tool_vi.py prior <headword> [<headword> ...]
  python -I -X utf8 senses_tool_vi.py show <headword> [<vietnamese value>] [<max segments>] [<width>]
     all ids of that headword[=value] in the pi-4 Vietnamese map (case-insensitive headword), then, for
     the first segments, the Pāli/Vietnamese line pairs whose Vietnamese contains the value (the part
     before " … " for gapped values), or whose Pāli contains the headword when no value is given; default 4.
     '' or '-' as value = any value (in PowerShell use '-'). <width> > 0 cuts each printed line to that many characters around the match.
  python -I -X utf8 senses_tool_vi.py words <headword> [<vietnamese value>]
     per Vietnamese value, the Pāli words of its segments that contain the headword's stem, with counts.
  Explicit paths still work:  build <agg.tsv> <decisions.txt> <out.md> | verify <agg.tsv> <out.md> | todo <agg.tsv> <decisions.txt>

agg.tsv line:   headword <TAB> en≈ hints <TAB> vietnamese=count[ids] | ... <TAB> NDE=n
decisions file: one line per headword ('#' lines and blank lines are ignored), two forms:
  hw: {tag}                         single sense; candidates = every attested value
  hw: {tag1: v1 / v2; tag2: v3 / *} explicit senses; '*' = every attested value not listed elsewhere
                                    on the line. Each attested value must be placed at least once.
  A value may be listed in TWO senses only when the identical Vietnamese string is attested in both
  meanings (checked with "show"); build and verify print every such shared candidate.
Inside each sense, candidates are re-sorted by attested count (desc); senses keep the written order.
An attested value containing " / " is written with " và " instead (use the rewritten form in decisions).
Tags: English, no Vietnamese letters, no ': ', no '; ', no braces, not equal to a value, not a bare
English hint, no two senses of one headword with the same tag.
"""
import os
import re
import sys
import unicodedata
from collections import OrderedDict

sys.dont_write_bytecode = True

ROOT = r'D:\Work\OpenPecha\abhidhamma-rails'
HERE = os.path.dirname(os.path.abspath(__file__))
MAP = os.path.join(ROOT, r'AI_translation\vietnamese\pi-4-keywords-by-reference-pali-vietnamese-plain.md')
PDIR = os.path.join(ROOT, r'AI_translation\pali\pi-4_split_chapters')
VDIR = os.path.join(ROOT, r'AI_translation\vietnamese\pi-4-vietnamese-plain-zeroshot_split_chapters')
PI1_VI = os.path.join(ROOT, r'AI_translation\vietnamese\pi-1-pali-word-vietnamese-senses-plain.md')
PI2_VI = os.path.join(ROOT, r'AI_translation\vietnamese\pi-2-pali-word-vietnamese-senses-plain.md')
PI3_VI = os.path.join(ROOT, r'AI_translation\vietnamese\pi-3-pali-word-vietnamese-senses-plain.md')
PRIOR = [
    ('pi-3 vi', PI3_VI),
    ('pi-2 vi', PI2_VI),
    ('pi-1 vi', PI1_VI),
    ('pi-4 ru', os.path.join(ROOT, r'AI_translation\russian\pi-4-pali-word-russian-senses-plain.md')),
    ('pi-4 en', os.path.join(ROOT, r'AI_translation\english\pi-4-pali-word-english-senses-plain.md')),
]
HINT_ONLY = ('pi-4 en',)   # printed only when present

# Vietnamese-only letters (none of them is used in Pāli IAST): a tag must not contain them.
VIET = re.compile('[àáảãạăằắẳẵặâầấẩẫậđèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵ]', re.I)
VAL_RE = re.compile(r'^(.*)=(\d+)\[[^\]]*\]$')
HINT_RE = re.compile(r'^(.*) ×\d+$')
IDRE = re.compile(r'\^([0-9A-Za-z-]+)\s*$')


def nfc(s):
    return unicodedata.normalize('NFC', s)


def norm_value(v):
    return v.replace(' / ', ' và ')


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
            line = nfc(line.rstrip('\r\n'))
            if not line.strip():
                continue
            cols = line.split('\t')
            if len(cols) != 4:
                sys.exit(f'agg line {n}: expected 4 columns, got {len(cols)}')
            hw, eng, viet, nde = cols
            if hw in rows:
                sys.exit(f'agg line {n}: duplicate headword {hw!r}')
            vals = OrderedDict()
            for item in [x.strip() for x in viet.split(' | ') if x.strip()]:
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
            line = nfc(line.strip())
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
    for tag, vs in senses:
        dup = {v for v in vs if vs.count(v) > 1}
        if dup:
            errs.append(f'{hw}: value listed twice in one sense: {sorted(dup)}')
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
        print(f'" / " -> " và " rewrites ({len(rewrites)}):')
        for hw, v in rewrites:
            print(f'  {hw}: {v!r}')
    else:
        print('" / " -> " và " rewrites: 0')
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
            if line != nfc(line):
                errs.append(f'line {n}: not NFC')
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
    shared = []
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
            if VIET.search(tag):
                errs.append(f'{hw}: tag not in English (Vietnamese letters): {tag!r}')
            if any(c in tag for c in '{}') or '; ' in tag:
                errs.append(f'{hw}: tag contains a brace or "; ": {tag!r}')
            if tag.lower() in hints:
                errs.append(f'{hw}: tag is a bare copy of an English hint: {tag!r}')
            if tag in tags:
                errs.append(f'{hw}: two senses share the tag {tag!r}')
            tags.append(tag)
            in_sense = []
            for v in vs:
                if not v:
                    errs.append(f'{hw}: empty candidate')
                if v.lower() == tag.lower():
                    errs.append(f'{hw}: tag copies value {v!r}')
                if '/' in v or '; ' in v:
                    errs.append(f'{hw}: candidate contains "/" or "; ": {v!r}')
                if v in in_sense:
                    errs.append(f'{hw}: candidate listed twice in one sense: {v!r}')
                in_sense.append(v)
            for v in in_sense:
                if v in seen:
                    shared.append((hw, v))
                seen.append(v)
        miss = att - set(seen)
        extra = set(seen) - att
        if miss:
            errs.append(f'{hw}: attested values missing: {sorted(miss)}')
        if extra:
            errs.append(f'{hw}: values not attested in input: {sorted(extra)}')
    print(f'senses: {n_senses} | headwords with >1 sense: {multi_sense} | '
          f'senses with >1 candidate: {multi_cand}')
    print(f'shared candidates (same string in two senses of one headword): {len(shared)}')
    for hw, v in shared:
        print(f'  {hw}: {v!r}')
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


def _lines(path):
    with open(path, encoding='utf-8-sig') as f:
        return [nfc(l) for l in f.read().splitlines() if l.strip()]


def _prior_index():
    idx = []
    for label, path in PRIOR:
        d = {}
        if os.path.exists(path):
            for line in _lines(path):
                if ': {' in line:
                    d.setdefault(line.split(': {', 1)[0].lower(), []).append(line)
        idx.append((label, d))
    return idx


def prior(hws, rows=None):
    idx = _prior_index()
    for h in hws:
        h = nfc(h)
        if rows and h in rows:
            r = rows[h]
            print(f'== {h}\t' + ' | '.join(f'{v}={c}' for v, c in r['vals'].items()) + f'\t{r["eng"]}')
        else:
            print(f'== {h}')
        for label, d in idx:
            hit = d.get(h.lower(), [])
            if not hit and label not in HINT_ONLY:
                print(f'   [{label}] (none)')
            for line in hit:
                print(f'   [{label}] {line}')
    return 0


def reuse(outp):
    """Count output lines with at least one tag copied verbatim from the pi-1, pi-2 or pi-3 Vietnamese senses file."""
    prior_vi = {}
    for path in (PI3_VI, PI2_VI, PI1_VI):
        for line in _lines(path):
            if ': {' in line:
                try:
                    hw, senses = parse_out_line(line)
                except ValueError:
                    continue
                prior_vi.setdefault(hw.lower(), set()).update(t for t, _ in senses)
    n = has = full = 0
    for line in _lines(outp):
        hw, senses = parse_out_line(line)
        n += 1
        prior_tags = prior_vi.get(hw.lower())
        if prior_tags is None:
            continue
        has += 1
        if any(t in prior_tags for t, _ in senses):
            full += 1
    print(f'lines: {n} | headword also in pi-1 / pi-2 / pi-3 Vietnamese: {has} | '
          f'lines reusing a pi-1 / pi-2 / pi-3 Vietnamese tag verbatim: {full}')
    return 0


def _win(text, probe, width):
    """Cut a long line to `width` chars around the first match of probe (whole line if width is 0)."""
    if not width or len(text) <= width:
        return text
    i = text.lower().find(probe.lower()) if probe else -1
    if i < 0:
        return text[:width] + ' …'
    a = max(0, i - width // 2)
    return ('… ' if a else '') + text[a:a + width] + (' …' if a + width < len(text) else '')


def _map_ids(hw, value=None):
    ids = []
    with open(MAP, encoding='utf-8-sig') as f:
        for line in f:
            line = nfc(line)
            if '] ' not in line or not line.startswith('['):
                continue
            i, body = line.rstrip('\n').split('] ', 1)
            for pair in body.split(', '):
                k, _, v = pair.partition('=')
                if k.lower() == hw.lower() and (value is None or v == value):
                    ids.append((i[1:], v))
    return ids


def show(hw, value=None, maxn=4, width=0):
    hw, value = nfc(hw), (nfc(value) if value else None)
    ids = _map_ids(hw, value)
    print(f'{hw}{"=" + value if value else ""}: {len(ids)} occurrences')
    print('  ' + ' '.join(f'{i}={v}' if value is None else i for i, v in ids))
    want = []
    for i, _ in ids:
        if i not in want:
            want.append(i)
    want = want[:maxn]
    for name in sorted(os.listdir(PDIR)):
        if not name.endswith('.md') or not want or not os.path.exists(os.path.join(VDIR, name)):
            continue
        p = _lines(os.path.join(PDIR, name))
        r = _lines(os.path.join(VDIR, name))
        if len(p) != len(r):
            print(f'  (skip {name}: line counts differ)')
            continue
        bp, br = [], []
        for a, b in zip(p, r):
            bp.append(a)
            br.append(b)
            m = IDRE.search(a)
            if m:
                if m.group(1) in want:
                    print(f'--- {name} ^{m.group(1)}')
                    probe = value.split(' … ')[0] if value else None
                    hits = [(x, y) for x, y in zip(bp, br)
                            if (probe.lower() in y.lower() if probe else hw.lower() in x.lower())]
                    for x, y in (hits or list(zip(bp, br))[:3]):
                        print(f'P: {_win(x, hw, width)}\nV: {_win(y, probe, width)}')
                bp, br = [], []
    return 0


def _segments():
    """{block id: Pāli text of the segment} for all pi-4 split chapters."""
    segs = {}
    for name in sorted(os.listdir(PDIR)):
        if not name.endswith('.md'):
            continue
        buf = []
        for a in _lines(os.path.join(PDIR, name)):
            buf.append(a)
            m = IDRE.search(a)
            if m:
                segs[m.group(1)] = ' '.join(buf)
                buf = []
    return segs


def words(hw, value=None):
    """Per Vietnamese value: which Pāli words (tokens containing the headword's stem) occur in its segments."""
    from collections import Counter, defaultdict
    hw = nfc(hw)
    stem = hw.lower().split(' ')[0]
    stem = stem[:-1] if len(stem) > 3 and stem[-1] in 'ṃoāaiīuū' else stem
    segs = _segments()
    by_val = defaultdict(Counter)
    for i, v in _map_ids(hw, nfc(value) if value else None):
        toks = re.findall(r"[^\s,.;:?!‘’“”'\"()\[\]–—…]+", segs.get(i, ''))
        hit = sorted({t for t in toks if stem in t.lower()})
        by_val[v].update(hit or ['(no Pāli token with the stem)'])
    for v, c in by_val.items():
        print(f'== {v}')
        print('   ' + ', '.join(f'{t}×{n}' for t, n in c.most_common(25)))
    return 0


if __name__ == '__main__':
    a = [nfc(x) for x in sys.argv[1:]]
    if len(a) == 3 and a[1] == '--part' and a[0] in ('build', 'sample', 'verify', 'todo', 'prior', 'reuse'):
        aggp, decp, outp = part_paths(a[2])
        if a[0] in ('build', 'sample'):
            sys.exit(build(aggp, decp, outp))
        if a[0] == 'verify':
            sys.exit(verify(aggp, outp))
        if a[0] == 'reuse':
            sys.exit(reuse(outp))
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
    # '' (bash), '-' or '*' (PowerShell 5.1 drops empty arguments) = any value
    anyval = lambda i: None if len(a) <= i or a[i] in ('', '-', '*') else a[i]
    if len(a) >= 2 and a[0] == 'show':
        sys.exit(show(a[1], anyval(2), int(a[3]) if len(a) > 3 else 4,
                      int(a[4]) if len(a) > 4 else 0))
    if len(a) >= 2 and a[0] == 'words':
        sys.exit(words(a[1], anyval(2)))
    sys.exit(__doc__)
