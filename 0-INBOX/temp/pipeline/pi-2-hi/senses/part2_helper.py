"""part-2 helper: print agg-part2.tsv rows [start:end] compactly (ids dropped) with pi-1 (and pi-4/5) sense lines
for the same headword (case-insensitive).
usage: python -I -X utf8 part2_helper.py <start> <end>
"""
import os
import re
import sys

ROOT = r'D:\Work\OpenPecha\abhidhamma-rails'
SD = os.path.join(ROOT, r'0-INBOX\temp\pipeline\pi-2-hi\senses')
REFS = [os.path.join(ROOT, r'AI_translation\hindi', f) for f in
        ('pi-1-pali-word-hindi-senses-plain.md', 'pi-4-pali-word-hindi-senses-plain.md',
         'pi-5-pali-word-hindi-senses-plain.md')]

refs = {}
for p in REFS:
    if not os.path.exists(p):
        continue
    tag = os.path.basename(p)[:4]
    for line in open(p, encoding='utf-8-sig'):
        line = line.rstrip('\n')
        i = line.find(': {')
        if i > 0:
            refs.setdefault(line[:i].lower(), []).append(tag + ' ' + line[i + 2:])

def ctx(text, probe, w=70):
    i = text.lower().find(probe.lower())
    if i < 0:
        return text[:2 * w]
    return text[max(0, i - w):i + len(probe) + w]


def snip(args):
    """snip hw=value [hw=value ...]: one short Pāli/Hindi context per value (first segment)"""
    sys.path.insert(0, SD)
    import senses_tool_pi2 as T
    pmap = {}
    for name in sorted(os.listdir(T.PDIR)):
        if not name.endswith('.md'):
            continue
        p = T._lines(os.path.join(T.PDIR, name))
        h = T._lines(os.path.join(T.HDIR, name))
        if len(p) != len(h):
            continue
        bp, bh = [], []
        for a, b in zip(p, h):
            bp.append(a); bh.append(b)
            m = re.search(r'\^([0-9A-Za-z-]+)\s*$', a)
            if m:
                pmap[m.group(1)] = (bp, bh)
                bp, bh = [], []
    mp = {}
    for line in open(T.MAP, encoding='utf-8-sig'):
        if '] ' not in line:
            continue
        i, body = line.rstrip('\n').split('] ', 1)
        for pair in body.split(', '):
            k, _, v = pair.partition('=')
            mp.setdefault((k.lower(), v), []).append(i[1:])
    for a in args:
        hw, _, val = a.partition('=')
        ids = mp.get((hw.lower(), val), [])
        print(f'## {hw}={val}: {len(ids)} {ids[:6]}')
        for sid in ids[:1]:
            if sid not in pmap:
                print('   (no seg)'); continue
            bp, bh = pmap[sid]
            probe = val.split(' … ')[0]
            for x, y in zip(bp, bh):
                if probe in y:
                    print('   P:', ctx(x, hw[:max(3, len(hw) - 2)]))
                    print('   H:', ctx(y, probe))
                    break


if sys.argv[1] == 'snip':
    snip(sys.argv[2:])
    sys.exit()
start, end = int(sys.argv[1]), int(sys.argv[2])
with open(os.path.join(SD, 'agg-part2.tsv'), encoding='utf-8-sig') as f:
    rows = [r for r in f.read().splitlines() if r.strip()][start:end]
for k, r in enumerate(rows, start):
    hw, eng, hin, nde = r.split('\t')
    hin = re.sub(r'\[[^\]]*\]', '', hin)
    eng = eng.replace('en≈ ', '')
    print(f'{k}|{hw}|{eng}|{hin}')
    for x in refs.get(hw.lower(), [])[:2]:
        print('    ', x[:300])
