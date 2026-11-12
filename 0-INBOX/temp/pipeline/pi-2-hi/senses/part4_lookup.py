"""part 4 helper: print pi-1 (and pi-4) sense lines for headwords of agg-part4.tsv that exist there."""
import sys
R = r'D:\Work\OpenPecha\abhidhamma-rails'
files = [('pi1', R + r'\AI_translation\hindi\pi-1-pali-word-hindi-senses-plain.md'),
         ('pi4', R + r'\AI_translation\hindi\pi-4-pali-word-hindi-senses-plain.md')]
agg = R + r'\0-INBOX\temp\pipeline\pi-2-hi\senses\agg-part4.tsv'
idx = {}
for tag, p in files:
    for line in open(p, encoding='utf-8-sig'):
        line = line.rstrip('\n')
        i = line.find(': {')
        if i > 0:
            idx.setdefault(line[:i], []).append(tag + ' ' + line[i + 2:])
which = sys.argv[1] if len(sys.argv) > 1 else 'pi1'
for line in open(agg, encoding='utf-8-sig'):
    hw = line.split('\t')[0]
    for e in idx.get(hw, []):
        if e.startswith(which):
            print(hw, '|', e)
