import re,sys,collections
sys.path.insert(0,r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-hi\review')
import B_load
from B_load import *
B_load.IDRE=re.compile(r'\^([0-9a-zA-Z\-]+)\s*$')
d=load()
strip=lambda s: re.sub(r'\s*\^[0-9a-zA-Z\-]+\s*$','',s).strip()
pm=[l for l in lines(os.path.join(P,'1-matika.md')) if l.strip()]
hm=[l for l in lines(os.path.join(H,'1-matika.md')) if l.strip()]
print(len(pm),len(hm))
M={}
for a,b in zip(pm,hm):
    a=strip(a);b=strip(b)
    if a.startswith('#'): continue
    pa=[t.strip(' .') for t in re.split(r'[,;]',re.sub(r'\[[^\]]*\]','',a))]
    pb=[t.strip(' ।') for t in re.split(r'[,;]',re.sub(r'\[[^\]]*\]','',b))]
    if len(pa)==len(pb):
        for u,v in zip(pa,pb):
            M[u.lower().replace(' dhammā','').strip()]=v
    else:
        print('M-UNEQ',a[:60],'|',b[:60])
print('matrix items',len(M))
heads=collections.OrderedDict()
for x in d:
    if not x['f'].startswith(('4-','5-')): continue
    p=strip(x['p'])
    m=re.match(r'(Katame|Katamaṃ|Katamā|Katamo)\s+(.*?)\?',p)
    if not m: continue
    q=m.group(2).strip()
    h=strip(x['h']).split('?')[0]
    heads.setdefault(q.lower(),[]).append((x['id'] or x['f'][:4]+':'+str(x['i']),h))
print('heads',len(heads))
n=0
for q,v in heads.items():
    k=q.replace('dhammā','').strip()
    hs=set(h for _,h in v)
    mm=M.get(k)
    print('%s\t%s\t%s\t%s'%(k,v[0][0],' || '.join(sorted(hs))[:150],('M:'+mm[:70]) if mm else 'M:-'))
