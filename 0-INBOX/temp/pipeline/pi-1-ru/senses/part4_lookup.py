import sys
base = r'D:\Work\OpenPecha\abhidhamma-rails'
hws = [l.split('\t')[0] for l in open(base + r'\0-INBOX\temp\pipeline\pi-1-ru\senses\agg-part4.tsv', encoding='utf8').read().splitlines() if l.strip()]
ref = {}
for f in ['pi-4', 'pi-5', 'pi-3']:
    for line in open(base + r'\AI_translation\russian\%s-pali-word-russian-senses-plain.md' % f, encoding='utf8'):
        if ': {' in line:
            k = line.split(': {', 1)[0]
            ref.setdefault(k, (f, line.strip()))
for h in hws:
    if h in ref:
        print(ref[h][0], ref[h][1])
