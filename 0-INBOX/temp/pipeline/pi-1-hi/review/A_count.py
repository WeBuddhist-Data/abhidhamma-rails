import re, os, collections
H = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi\pi-1-hindi-plain-rails_split_chapters'
FILES = ['preamble.md', '1-matika.md', '2-01-cittuppadakandam.md', '2-02-cittuppadakandam.md', '2-03-cittuppadakandam.md', '2-04-cittuppadakandam.md', '2-05-cittuppadakandam.md']
pats = {'manasik-kriya': 'मानसिक क्रिया', 'sharir-se-sukh': 'शरीर से सुख का अनुभव', 'sammappadhana': 'लोकोत्तर सही प्रयास का अभ्यास',
        'hone-vala-hota': 'होने वाला होता है|होने वाली होती है', 'prabal-rag': 'प्रबल राग', 'rag-abhav': 'राग का अभाव', 'mool-suchi': 'मूल सूची',
        'hone-vali-hai-vipak': 'होने वाली है'}
for k, p in pats.items():
    tot = 0; where = collections.defaultdict(list)
    for f in FILES:
        ls = [x.strip() for x in open(os.path.join(H, f), encoding='utf-8') if x.strip()]
        for i, l in enumerate(ls):
            n = len(re.findall(p, l))
            if n:
                tot += n
                m = re.search(r'\^([\w-]+)$', l)
                if m: t = m.group(1)
                else:
                    t = 'L%d' % (i + 1)
                    for j in range(i + 1, len(ls)):
                        mm = re.search(r'\^([\w-]+)$', ls[j])
                        if mm:
                            t += '(before ^' + mm.group(1) + ')'; break
                where[f[:4]].append(t)
    print(k, tot, {f: (len(v), v[:6]) for f, v in where.items()})
ids = 0
for f in FILES:
    for x in open(os.path.join(H, f), encoding='utf-8'):
        if re.search(r'\^[\w-]+\s*$', x): ids += 1
print('ids', ids)
