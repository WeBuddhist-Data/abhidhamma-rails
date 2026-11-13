"""part 2 helper: for each agg-part2 headword, print matching lines from the approved pi-1/pi-2 Hindi senses files."""
import os
import sys

sys.dont_write_bytecode = True
ROOT = r'D:\Work\OpenPecha\abhidhamma-rails'
FILES = [os.path.join(ROOT, r'AI_translation\hindi', f) for f in
         ('pi-1-pali-word-hindi-senses-plain.md', 'pi-2-pali-word-hindi-senses-plain.md')]
AGG = os.path.join(ROOT, r'0-INBOX\temp\pipeline\pi-6-hi\senses\agg-part2.tsv')

prior = {}
for p in FILES:
    tag = os.path.basename(p)[:4]
    for line in open(p, encoding='utf-8-sig'):
        line = line.rstrip('\n')
        i = line.find(': {')
        if i < 0:
            continue
        hw = line[:i].strip().lower()
        prior.setdefault(hw, []).append(f'{tag} {line}')

for line in open(AGG, encoding='utf-8-sig'):
    hw = line.split('\t')[0]
    hits = prior.get(hw.lower())
    if hits:
        for h in hits:
            print(f'{hw}\t{h}')
