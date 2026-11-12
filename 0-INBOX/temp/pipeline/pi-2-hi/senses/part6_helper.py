"""part-6 helper: compact view of agg-part6.tsv rows (no ids) with pi-1 (and pi-4/5) matches for each headword.
Usage: python -I -X utf8 part6_helper.py <start> <end>
"""
import os
import re
import sys

ROOT = r'D:\Work\OpenPecha\abhidhamma-rails'
SD = os.path.join(ROOT, r'0-INBOX\temp\pipeline\pi-2-hi\senses')
REFS = [os.path.join(ROOT, r'AI_translation\hindi', f) for f in
        ('pi-1-pali-word-hindi-senses-plain.md', 'pi-4-pali-word-hindi-senses-plain.md',
         'pi-5-pali-word-hindi-senses-plain.md')]


def main(start, end):
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
    with open(os.path.join(SD, 'agg-part6.tsv'), encoding='utf-8-sig') as f:
        rows = f.read().splitlines()
    for n, r in enumerate(rows[int(start):int(end)], int(start) + 1):
        hw, eng, hin, nde = r.split('\t')
        hin = re.sub(r'\[[^\]]*\]', '', hin)
        nde = '' if nde == 'NDE=0' else ' ' + nde
        print(f'{n} {hw}\t{eng[3:]}\t{hin}{nde}')
        for x in refs.get(hw.lower(), [])[:2]:
            print('    ', x[:300])


def kwic(words):
    """Pāli context (±70 chars) of the first occurrence of each word in the pi-2 Pāli split chapters."""
    pdir = os.path.join(ROOT, r'AI_translation\pali\pi-2_split_chapters')
    files = sorted(n for n in os.listdir(pdir) if n.endswith('.md'))
    texts = [open(os.path.join(pdir, n), encoding='utf-8-sig').read() for n in files]
    for w in words:
        hits = 0
        for t in texts:
            for m in re.finditer(re.escape(w), t, re.I):
                s = t[max(0, m.start() - 70):m.end() + 70].replace('\n', ' ')
                print(f'{w}: …{s}…')
                hits += 1
                if hits >= 2:
                    break
            if hits >= 2:
                break
        if not hits:
            print(f'{w}: (not found)')


if __name__ == '__main__':
    if sys.argv[1] == 'kwic':
        kwic(sys.argv[2:])
    else:
        main(*sys.argv[1:3])
