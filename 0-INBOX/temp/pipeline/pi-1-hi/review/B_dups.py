import re,sys,collections
sys.path.insert(0,r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-hi\review')
from B_load import *
import B_load
B_load.IDRE=re.compile(r'\^([0-9a-zA-Z\-]+)\s*$')
d=load()
print(sum(1 for x in d if x['id']), sum(1 for x in d if x['id']!=x['hid']))
strip=lambda s: re.sub(r'\s*\^[0-9a-zA-Z\-]+\s*$','',s).strip()
g=collections.defaultdict(list)
for x in d: g[strip(x['p'])].append(x)
print('distinct',len(g), sum(len(k) for k in g))
for k,v in g.items():
    hs=set(strip(x['h']) for x in v)
    if len(hs)>1:
        print('VAR',len(v),[x['id'] or x['f']+':'+str(x['i']) for x in v][:6],k[:100])
        for h in hs: print('   ',h[:300])
for x in d:
    if x['id'] is None: pass
# bytes per file distinct
c=collections.Counter()
seen=set()
for x in d:
    k=strip(x['p'])
    if k in seen: continue
    seen.add(k); c[x['f']]+=len(x['p'])+len(x['h'])
print(c, sum(c.values()))
