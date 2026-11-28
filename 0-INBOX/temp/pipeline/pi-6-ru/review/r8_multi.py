"""r8: list Pāli templates (from r8_tpl.txt) that have more than one Russian rendering."""
import sys
lines = open(r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-ru\review\r8_tpl.txt', encoding='utf-8').read().split('\n')
blocks = []
cur = None
for l in lines:
    if l.startswith('P '):
        cur = [l]; blocks.append(cur)
    elif l.startswith('   R') and cur is not None:
        cur.append(l)
for b in blocks:
    if len(b) > 2:
        print('\n'.join(b)); print()
