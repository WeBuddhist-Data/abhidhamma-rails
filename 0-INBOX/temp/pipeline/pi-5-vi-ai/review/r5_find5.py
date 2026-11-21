import os, sys
d5 = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation\vietnamese\pi-5-vietnamese-plain-rails_split_chapters'
for ph in sys.argv[1:]:
    for f in sorted(os.listdir(d5)):
        t = open(os.path.join(d5, f), encoding='utf-8').read()
        i = t.find(ph)
        n = t.count(ph)
        if n:
            print(ph, '|', f, n, '|', t[max(0, i - 60):i + len(ph) + 60].replace('\n', ' '))
