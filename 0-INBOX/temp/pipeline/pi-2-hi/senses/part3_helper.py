"""part-3 helper: compact listing of agg-part3.tsv rows (hint, values with counts, NDE) with the pi-1 (else other book) senses line for the same headword."""
import os
import re
import sys

ROOT = r'D:\Work\OpenPecha\abhidhamma-rails'
SD = os.path.join(ROOT, r'0-INBOX\temp\pipeline\pi-2-hi\senses')
REFS = [os.path.join(ROOT, r'AI_translation\hindi', f'pi-{n}-pali-word-hindi-senses-plain.md') for n in (1, 4, 5, 3, 6, 7)]
VAL_RE = re.compile(r'^(.*)=(\d+)\[[^\]]*\]$')


def main(start, end, outp):
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
    rows = open(os.path.join(SD, 'agg-part3.tsv'), encoding='utf-8-sig').read().splitlines()
    out = []
    for n, r in enumerate(rows[int(start):int(end)], int(start) + 1):
        hw, eng, hin, nde = r.split('\t')
        vals = []
        for item in [x.strip() for x in hin.split(' | ') if x.strip()]:
            m = VAL_RE.match(item)
            vals.append(f'{m.group(1)}={m.group(2)}' if m else item)
        out.append(f'{n}. {hw} || {eng[:160]} || {" | ".join(vals)} || {nde}')
        for x in refs.get(hw.lower(), [])[:2]:
            out.append('    ' + x[:260])
    with open(outp, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(out) + '\n')
    print(len(out))


if __name__ == '__main__':
    main(*sys.argv[1:])
