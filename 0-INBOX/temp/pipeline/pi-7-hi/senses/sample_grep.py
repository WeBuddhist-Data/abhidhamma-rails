"""Sample helper: print prior-book senses lines (pi-1..pi-6) for the headwords of an agg file (case-insensitive)."""
import os
import sys

ROOT = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi'
BOOKS = [1, 2, 3, 4, 5, 6]


def load():
    d = {}
    for b in BOOKS:
        p = os.path.join(ROOT, f'pi-{b}-pali-word-hindi-senses-plain.md')
        for line in open(p, encoding='utf-8-sig'):
            line = line.rstrip('\n')
            i = line.find(': {')
            if i < 0:
                continue
            d.setdefault(line[:i].lower(), []).append((b, line[i + 2:]))
    return d


if __name__ == '__main__':
    agg = sys.argv[1]
    only = set(a.lower() for a in sys.argv[2:])
    d = load()
    for line in open(agg, encoding='utf-8-sig'):
        hw = line.split('\t')[0]
        if only and hw.lower() not in only:
            continue
        hits = d.get(hw.lower(), [])
        print(f'== {hw}' + ('' if hits else '  (none)'))
        for b, s in hits:
            print(f'   pi-{b}: {s[:400]}')
