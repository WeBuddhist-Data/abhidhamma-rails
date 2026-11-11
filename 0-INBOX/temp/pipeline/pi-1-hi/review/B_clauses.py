import re,sys,collections
sys.path.insert(0,r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-hi\review')
import B_load
from B_load import *
B_load.IDRE=re.compile(r'\^([0-9a-zA-Z\-]+)\s*$')
d=load()
strip=lambda s: re.sub(r'\s*\^[0-9a-zA-Z\-]+\s*$','',s).strip()
def clean(s):
    s=strip(s)
    s=re.sub(r'\[[^\]]*\]','',s)
    s=re.sub(r'\([^)]*\)','',s)
    s=re.sub(r'^[#\s*]+','',s)
    return s
sp=re.compile(r'\s*(?:[,;.?!–—:“”‘’]|\.\.\.|…pe…|…|पे)\s*')
def sp_p(s):
    s=s.replace('…pe…','|').replace('… pe …','|')
    return [t.strip() for t in re.split(r'[,;.?!–—:“”‘’…|]+',s) if t.strip()]
def sp_h(s):
    return [t.strip() for t in re.split(r'[,;।?!–—:“”‘’…|]+',s) if t.strip()]
pairs=collections.defaultdict(lambda: collections.defaultdict(list))
bad=[]
for x in d:
    a=sp_p(clean(x['p'])); b=sp_h(clean(x['h']))
    x['a']=a;x['b']=b
    if len(a)==len(b):
        for u,v in zip(a,b): pairs[u.lower()][v].append(x['id'] or x['f'][:4]+':'+str(x['i']))
    else: bad.append(x)
print('lines',len(d),'unequal',len(bad),sum(len(x['p'])+len(x['h']) for x in bad))
print('clausepairs',len(pairs), sum(len(k)+sum(len(v) for v in m) for k,m in pairs.items()))
print('multi',sum(1 for m in pairs.values() if len(m)>1))
import pickle
pickle.dump(dict(bad=[{k:x[k] for k in ('f','i','id','p','h','a','b')} for x in bad],pairs={k:dict(m) for k,m in pairs.items()}),open(r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-hi\review\B_pairs.pkl','wb'))
for x in bad[:40]: print(x['id'],len(x['a']),len(x['b']),x['p'][:70])
