"""part-1 helper: make agg-sample.tsv (first N lines of agg-part1.tsv) and look up headwords in pi-1 / pi-4 / pi-5 senses."""
import os
import sys

ROOT = r'D:\Work\OpenPecha\abhidhamma-rails'
SD = os.path.join(ROOT, r'0-INBOX\temp\pipeline\pi-2-hi\senses')
REFS = [os.path.join(ROOT, r'AI_translation\hindi', f) for f in
        ('pi-1-pali-word-hindi-senses-plain.md', 'pi-4-pali-word-hindi-senses-plain.md',
         'pi-5-pali-word-hindi-senses-plain.md', 'pi-3-pali-word-hindi-senses-plain.md',
         'pi-6-pali-word-hindi-senses-plain.md', 'pi-7-pali-word-hindi-senses-plain.md')]


def sample(n):
    with open(os.path.join(SD, 'agg-part1.tsv'), encoding='utf-8-sig') as f:
        lines = f.read().splitlines()[:n]
    with open(os.path.join(SD, 'agg-sample.tsv'), 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(lines) + '\n')
    print('wrote', len(lines))


def lookup(aggp, start, end):
    refs = {}
    for p in REFS:
        if not os.path.exists(p):
            continue
        tag = os.path.basename(p)[:4]
        for line in open(p, encoding='utf-8-sig'):
            line = line.rstrip('\n')
            i = line.find(': {')
            if i > 0:
                refs.setdefault(line[:i].lower(), []).append(tag + ' ' + line)
    with open(aggp, encoding='utf-8-sig') as f:
        rows = f.read().splitlines()[int(start):int(end)]
    for r in rows:
        hw = r.split('\t')[0]
        print('##', r)
        for x in refs.get(hw.lower(), [])[:3]:
            print('   ', x)


if __name__ == '__main__':
    if sys.argv[1] == 'sample':
        sample(int(sys.argv[2]))
    else:
        lookup(*sys.argv[2:])
