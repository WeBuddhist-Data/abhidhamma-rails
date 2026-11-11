import re, os, collections
P = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation\pali\pi-1_split_chapters'
H = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi\pi-1-hindi-plain-rails_split_chapters'
FILES = ['2-01-cittuppadakandam.md', '2-02-cittuppadakandam.md', '2-03-cittuppadakandam.md', '2-04-cittuppadakandam.md', '2-05-cittuppadakandam.md']
pats = {
 'kasina-vala': r'पृथ्वी के ध्यान-मंडल वाला',
 'kasina-adharit': r'पृथ्वी के ध्यान-मंडल पर आधारित',
 'kasina-par': r'पृथ्वी के ध्यान-मंडल पर (पहला|पाँचवाँ)',
 'jhana-ko': r'ध्यान को प्राप्त करके',
 'jhana-nom': r'ध्यान प्राप्त करके',
 'prag-vala-comma': r'प्रगति वाला, (धीमे|शीघ्र) उच्च',
 'prag-vala-aur': r'प्रगति वाला और (धीमे|शीघ्र) उच्च',
 'prag-aur': r'प्रगति और (धीमे|शीघ्र) उच्च',
 'chhod-aur': r'पहचान के समूह को छोड़कर और चेतना',
 'chhod-comma': r'पहचान के समूह को छोड़कर, चेतना',
 'purnataya-first': r'पूरी तरह (भौतिक रूप|अनंत|कुछ भी)',
 'purnataya-later': r'को पूरी तरह पार',
 'jis-samay-vah': r'कारण जिस समय वह',
 'karan-comma': r'कारण, (इंद्रिय|आरंभिक|सुख)',
 'vipak-hoti-hai': r'होने वाली होती है',
 'vipak-hai': r'होने वाली है और जिसका',
}
res = collections.defaultdict(lambda: collections.defaultdict(list))
for f in FILES:
    for i, l in enumerate([x for x in open(os.path.join(H, f), encoding='utf-8') if x.strip()], 1):
        m = re.search(r'\^([\w-]+)\s*$', l.strip())
        t = m.group(1) if m else f'L{i}'
        for k, p in pats.items():
            n = len(re.findall(p, l))
            if n:
                res[k][f[:4]].append(f'{t}x{n}' if n > 1 else t)
for k in pats:
    print(k)
    for f, v in res[k].items():
        print('  ', f, len(v), ' '.join(v[:14]))
