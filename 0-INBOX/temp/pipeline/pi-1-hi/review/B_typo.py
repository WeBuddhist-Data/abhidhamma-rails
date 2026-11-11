import re,sys
sys.path.insert(0,r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-hi\review')
from B_load import *
d=load()
print(len(d))
print('idmis',[ (x['f'],x['i'],x['id'],x['hid']) for x in d if x['id']!=x['hid']])
import collections
cnt=collections.Counter(x['f'] for x in d); print(cnt)
tot=collections.Counter()
for x in d:
    tot[x['f']]+=len(x['p'])
print(tot)
L=sorted(d,key=lambda x:-len(x['p']))[:10]
print([(x['id'],len(x['p'])) for x in L])
# dash counts
for x in d:
    pc=len(re.findall('[–—]',x['p'])); hc=len(re.findall('[–—]',x['h']))
    if pc!=hc: print('DASH',x['f'],x['i'],x['id'],pc,hc,x['p'][-80:],'||',x['h'][-80:])
for x in d:
    h=re.sub(r'\s*\^[0-9a-z\-]+\s*$','',x['h']).strip()
    if h.startswith('#'): continue
    if not re.search(r'[।?”–:…]$|\]$|\)$',h): print('END',x['f'],x['i'],x['id'],h[-60:],'|',x['p'][-50:])
    if re.search(r'[\"\'«»]',h): print('QUOTE',x['f'],x['i'],x['id'],h[:100])
    if re.search(r'[a-zA-Zāīūṃṅñṭḍṇḷ]{2,}',h): print('LATIN',x['f'],x['i'],x['id'],re.findall(r'[\[\(]?[a-zA-Zāīūṃṅñṭḍṇḷ]{2,}[\]\)]?',h)[:8])
    if '..' in h or re.search(r'  ',h): print('DOTS/SP',x['f'],x['i'],x['id'],h[:80])
