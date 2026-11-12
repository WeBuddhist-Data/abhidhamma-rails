"""part-5 helper: list part-5 headwords that also exist in the pi-1 Hindi senses file (case-insensitive),
and list part-5 headwords with more than one attested Hindi value."""
import os
import sys

ROOT = r'D:\Work\OpenPecha\abhidhamma-rails'
SD = os.path.join(ROOT, r'0-INBOX\temp\pipeline\pi-2-hi\senses')
PI1 = os.path.join(ROOT, r'AI_translation\hindi\pi-1-pali-word-hindi-senses-plain.md')


def main(mode):
    refs = {}
    for line in open(PI1, encoding='utf-8-sig'):
        line = line.rstrip('\n')
        i = line.find(': {')
        if i > 0:
            refs.setdefault(line[:i].lower(), []).append(line)
    rows = open(os.path.join(SD, 'agg-part5.tsv'), encoding='utf-8-sig').read().splitlines()
    for n, r in enumerate(rows, 1):
        c = r.split('\t')
        hw = c[0]
        if mode == 'pi1' and hw.lower() in refs:
            print(f'{n}\t{hw}\t{c[2]}')
            for x in refs[hw.lower()]:
                print('    pi1 ' + x)
        if mode == 'multi' and ' | ' in c[2]:
            print(f'{n}\t{hw}\t{c[1]}\t{c[2]}')


if __name__ == '__main__':
    main(sys.argv[1])
