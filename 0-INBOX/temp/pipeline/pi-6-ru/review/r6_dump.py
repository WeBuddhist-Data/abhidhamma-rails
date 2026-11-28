"""r6: collapse K/A/B members to X and dump unique Pāli->Russian templates to r6_tpl.txt."""
import re, sys, collections, subprocess
sys.path.insert(0, r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-ru\review')
out = subprocess.run([sys.executable, '-I', '-X', 'utf8', '-B',
                      r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-ru\review\r6_tpl.py', 'tpl'],
                     capture_output=True, text=True, encoding='utf-8').stdout
d = collections.OrderedDict()
p = None
for l in out.split('\n'):
    if l.startswith('P '):
        p = re.sub(r'[KAB]·', 'X·', l.split(' ', 2)[2])
        d.setdefault(p, collections.OrderedDict())
    elif l.startswith('   R'):
        parts = l.split(' ', 6)
        ref = parts[5]
        r = re.sub(r'[KAB]·', 'X·', parts[6])
        r = re.sub(r'X·ы', 'X·и', r)
        r = re.sub(r'X·ая', 'X·ая', r)
        d[p].setdefault(r, ref)
with open(r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-ru\review\r6_tpl.txt', 'w', encoding='utf-8') as f:
    for k, v in d.items():
        f.write('P ' + k + '\n')
        for x, y in v.items():
            f.write('   R ' + y + ' ' + x + '\n')
print(len(d), sum(len(v) > 1 for v in d.values()))
for k, v in d.items():
    if len(v) > 1:
        print('MULTI', k)
        for x, y in v.items():
            print('    ', y, x)
