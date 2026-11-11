import re,sys
sys.path.insert(0,r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-hi\review')
import B_load
from B_load import *
B_load.IDRE=re.compile(r'\^([0-9a-zA-Z\-]+)\s*$')
d=load()
ind=[(x['id'] or x['f'][:4]+':'+str(x['i'])) for x in d if re.search(r'इंद्रियों|इंद्रिय(?![-])',x['h'])]
print('indriya-plain',ind)
print('indriyanam P',[(x['id'] or x['i']) for x in d if re.search(r'indriyānaṃ|anindriya',x['p'])])
adj=[]
for x in d:
    h=x['h']
    m=re.match(r'कौन-सा भौतिक रूप (.*?)\?',h)
    if m and 'वाला है और' in m.group(1) and 'नहीं' not in m.group(1) and 'महाभूत' not in m.group(1) and 'क्षमता' not in m.group(1): adj.append(x['id'])
print('adj-hai-aur',adj)
print('Q-end',[x['id'] for x in d if re.search(r'\?\s*\^',x['h']) and re.search(r'\?\s*\^',x['p']) and 'Katam' in x['p'] and x['p'].count('?')>=2][:12])
