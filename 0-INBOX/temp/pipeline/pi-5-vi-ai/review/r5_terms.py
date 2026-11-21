import os, re, sys
R = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation\vietnamese'
FILES = ['pi-1-vietnamese-plain.md', 'pi-2-vietnamese-plain.md', 'pi-3-vietnamese-plain.md', 'pi-4-vietnamese-plain.md']
texts = {}
for f in FILES:
    p = os.path.join(R, f)
    texts[f[:4]] = open(p, encoding='utf-8').read() if os.path.exists(p) else ''
d5 = os.path.join(R, 'pi-5-vietnamese-plain-rails_split_chapters')
t5 = ''
for f in sorted(os.listdir(d5)):
    t5 += open(os.path.join(d5, f), encoding='utf-8').read()
texts['pi-5'] = t5
phrases = [l.strip() for l in open(sys.argv[1], encoding='utf-8') if l.strip()]
ctx = '-c' in sys.argv
for ph in phrases:
    row = [ph]
    for k, t in texts.items():
        row.append('%s=%d' % (k, t.count(ph)))
    print(' | '.join(row))
    if ctx:
        for k, t in texts.items():
            if k == 'pi-5':
                continue
            i = t.find(ph)
            if i >= 0:
                print('   ', k, t[max(0, i - 80):i + len(ph) + 80].replace('\n', ' '))
