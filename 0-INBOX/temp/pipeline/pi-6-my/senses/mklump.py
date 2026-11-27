"""Write the LUMP_OK block for the REVIEW headwords left after the hand pass (each one looked at in rv-compact.txt):
headword, then a comment with its pi-6 values and the mapper's kept category. usage: mklump.py rv-review.txt out.txt"""
import re, sys
CAT = {'form': 'one lemma, the text\'s form / spacing (kept: form)',
       'construction': 'one phrase, glued or gapped (kept: construction)',
       'sense': 'the text\'s own word for the one meaning (kept: sense)',
       'none': 'one meaning (kept: none)', '-': 'one meaning'}
out = ['    # batch 5: one-stem groups and binding values checked by hand (rv-compact.txt)']
for b in open(sys.argv[1], encoding='utf-8').read().split('## ')[1:]:
    ls = b.split('\n')
    hw = ls[0].split('  (')[0]
    why = ls[0].split('  (', 1)[1].rsplit(') kept=', 1)
    kept = why[1].strip()
    vals = re.findall(r'(?:^|\| )([^=|]+)=(\d+)\[', ls[1].split('pi-6: ', 1)[1])
    vs = ' / '.join(f'«{v.strip()}»' for v, _ in vals)
    src = why[0]
    if 'later binding' in src:
        note = 'binding senses of ' + src.split(' senses')[0] + ' and a later binding file'
    elif 'one sense' in src:
        note = CAT.get(kept, 'one meaning') + ', = the ' + src.split(' one sense')[0] + ' sense'
    else:
        note = CAT.get(kept, 'one meaning')
    out.append(f'    {hw!r},  # {vs}: {note}')
open(sys.argv[2], 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print(len(out) - 1)
