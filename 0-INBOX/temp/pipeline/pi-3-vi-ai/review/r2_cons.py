# r2 helper: count Vietnamese renderings in our own pi-1 / pi-2 / pi-3 files (console only).
import re, sys, os
R = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation\vietnamese'
files = {
    'pi1': os.path.join(R, 'pi-1-vietnamese-plain.md'),
    'pi2': os.path.join(R, 'pi-2-vietnamese-plain.md'),
}
d3 = os.path.join(R, 'pi-3-vietnamese-plain-rails_split_chapters')
for ch in ['1-uddeso','2-pathamanayo','3-dutiyanayo','4-tatiyanayo','5-catutthanayo','6-pancamanayo','7-chatthanayo','8-sattamanayo','9-atthamanayo','10-navamanayo','11-dasamanayo','12-ekadasamanayo','13-dvadasamanayo','14-terasamanayo','15-cuddasamanayo']:
    files['3/' + ch.split('-')[0]] = os.path.join(d3, ch + '.md')
txt = {k: open(v, encoding='utf-8').read() for k, v in files.items()}
terms = sys.argv[1:]
for t in terms:
    row = []
    for k, v in txt.items():
        n = len(re.findall(t, v))
        if n:
            row.append('%s:%d' % (k, n))
    print('%-60s %s' % (t[:60], ' '.join(row) or '-'))
